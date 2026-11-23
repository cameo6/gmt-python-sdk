import os
import unittest
from io import BytesIO
from pathlib import Path
from tempfile import TemporaryDirectory
from zipfile import ZipFile
from typing import Dict, List, cast

import httpx
from gmt import APIError, APITimeoutError, AsyncGmt, Gmt


PAGE = {"page": 1, "page_size": 1, "sort": "date_desc"}
OPTIONS = {"base_url": os.environ["SDK_TEST_URL"], "max_retries": 0, "timeout": 2}


def retry_transport(keys):
    def reply(request):
        keys.append(request.headers.get("Idempotency-Key"))
        return httpx.Response(
            503 if len(keys) % 2 else 200, json={"id": 103}, headers={"retry-after-ms": "1"}
        )
    return httpx.MockTransport(reply)


class SyncCompatibility(unittest.TestCase):
    def test_health_response_keeps_python_field_aliases(self):
        with Gmt(**OPTIONS) as client:
            health = client.service.health_check()
        self.assertEqual(health.status, "ok")
        self.assertEqual(health.uptime_seconds, 42)

    def test_api_key_authorizes_iteration_over_both_purchase_pages(self):
        with Gmt(**OPTIONS, api_key="test-api-key") as client:
            ids = [purchase.id for purchase in client.purchases.list(**PAGE)]
        self.assertEqual(ids, [101, 102])

    def test_api_error_keeps_http_status_and_body(self):
        with Gmt(**OPTIONS, api_key="invalid") as client:
            with self.assertRaises(APIError) as caught:
                client.purchases.list(**PAGE)
        self.assertEqual(caught.exception.status_code, 401)
        self.assertEqual(caught.exception.body["details"][0]["reason"], "INVALID_TOKEN")

    def test_exposes_typed_connection_timeout(self):
        options = {**OPTIONS, "timeout": 0.1}
        with Gmt(**options, default_headers={"x-test-slow-response": "true"}) as client:
            with self.assertRaises(APITimeoutError):
                client.service.health_check()

    def test_purchase_keeps_body_and_caller_supplied_idempotency_key(self):
        with Gmt(**OPTIONS, api_key="test-api-key") as client:
            purchase = client.purchases.create(
                country_code="US", extra_headers={"Idempotency-Key": "test-order"}
            )
        self.assertEqual(purchase.status, "PENDING")

    def test_purchase_hash_is_encoded_as_one_path_segment(self):
        with Gmt(**OPTIONS, api_key="test-api-key") as client:
            purchase = client.purchases_by_hash.retrieve("order/103")
        self.assertEqual(purchase.id, 103)

    @unittest.skipUnless(os.environ.get("SDK_COMPAT_RELEASE"), "requires release candidate")
    def test_code_page_is_parsed_as_a_typed_model(self):
        with Gmt(**OPTIONS, api_key="test-api-key") as client:
            purchase = client.purchases_by_hash.retrieve("order/103")
        self.assertEqual(purchase.code_page.title, "GMT")

    @unittest.skipUnless(os.environ.get("SDK_COMPAT_RELEASE"), "requires release candidate")
    def test_purchase_retries_with_the_same_explicit_key(self):
        keys = []
        options = {**OPTIONS, "max_retries": 1}
        with Gmt(**options, http_client=httpx.Client(transport=retry_transport(keys))) as client:
            client.purchases.create(country_code="US", extra_headers={"Idempotency-Key": "explicit-order"})
        self.assertEqual(keys, ["explicit-order", "explicit-order"])


class AsyncCompatibility(unittest.IsolatedAsyncioTestCase):
    @unittest.skipUnless(os.environ.get("SDK_COMPAT_RELEASE"), "requires release candidate")
    async def test_main_purchase_lists_preserve_typed_items(self):
        async with AsyncGmt(**OPTIONS, api_key="test-api-key") as client:
            history = await client.purchases.history(page=1)
            bulk = await client.purchases.bulk.list(page=1)
        self.assertEqual(history.items[0].kind, "purchase")
        self.assertEqual(bulk.items[0].bulk_purchase_id, 104)

    @unittest.skipUnless(os.environ.get("SDK_COMPAT_RELEASE"), "requires release candidate")
    async def test_bulk_retries_with_one_generated_key_per_call(self):
        keys = []
        options = {**OPTIONS, "max_retries": 1}
        async with AsyncGmt(
            **options, http_client=httpx.AsyncClient(transport=retry_transport(keys))
        ) as client:
            await client.purchases.bulk.create(country_code="US", quantity=1)
            await client.purchases.bulk.create(country_code="US", quantity=1)
        self.assertTrue(keys[0])
        self.assertTrue(keys[2])
        self.assertEqual(keys[0], keys[1])
        self.assertEqual(keys[2], keys[3])
        self.assertNotEqual(keys[0], keys[2])

    async def test_bearer_authorizes_async_iteration_over_both_purchase_pages(self):
        async with AsyncGmt(
            **OPTIONS, default_headers={"Authorization": "Bearer test-bearer"}
        ) as client:
            ids = [
                purchase.id
                async for purchase in client.purchases.list(**PAGE)
            ]
        self.assertEqual(ids, [101, 102])


def assert_purchase_fields(test, legacy, current, explicit_null):
    test.assertEqual(legacy.items[0].status, "SUCCESS")
    test.assertEqual(legacy.items[0].code_page.title, "GMT")
    test.assertIsNone(legacy.items[0].code_page.brand_name)
    test.assertIsNone(legacy.items[0].code_request)
    test.assertEqual(current.items[0].code_page.brand_name, "GMT Shop")
    test.assertEqual(current.items[0].code_request.status, "pending")
    test.assertEqual(current.items[0].code_request.attempt, 1)
    test.assertIsNone(explicit_null.items[0].code_page.brand_name)
    test.assertIsNone(explicit_null.items[0].code_request)


class PurchaseResponseCompatibility(unittest.IsolatedAsyncioTestCase):
    def test_sync_purchase_list_preserves_old_and_new_fields(self):
        with Gmt(**OPTIONS, api_key="test-api-key", _strict_response_validation=True) as client:
            legacy = client.purchases.list(**PAGE)
            current = client.purchases.list(**PAGE, include="code_request")
            explicit_null = client.purchases.list(**{**PAGE, "page": 2}, include="code_request")
        assert_purchase_fields(self, legacy, current, explicit_null)

    async def test_async_purchase_list_preserves_old_and_new_fields(self):
        async with AsyncGmt(**OPTIONS, api_key="test-api-key", _strict_response_validation=True) as client:
            legacy = await client.purchases.list(**PAGE)
            current = await client.purchases.list(**PAGE, include="code_request")
            explicit_null = await client.purchases.list(**{**PAGE, "page": 2}, include="code_request")
        assert_purchase_fields(self, legacy, current, explicit_null)


def list_transport(requests: List[httpx.Request]) -> httpx.MockTransport:
    def reply(request: httpx.Request) -> httpx.Response:
        requests.append(request)
        page = int(request.url.params.get("page", "1"))
        item: Dict[str, object] = {"country_code": "US"} if request.url.path.endswith("/accounts/") else {"id": page}
        return httpx.Response(200, json={
            "items": [item],
            "pagination": {"current_page": page, "total_pages": 2, "has_next": page == 1},
        })
    return httpx.MockTransport(reply)


LIST_CASES = (
    ("accounts", {"country_codes": "US,GB", "sort": "price_asc"}),
    ("purchases", {"phone_number": "123", "status": "SUCCESS", "sort": "date_asc"}),
)


class SyncOptionalLists(unittest.TestCase):
    def test_defaults_and_explicit_filters_survive_pagination(self) -> None:
        for resource, filters in LIST_CASES:
            for params in ({}, {**filters, "page": 1, "page_size": 1}):
                with self.subTest(resource=resource, params=params):
                    requests: List[httpx.Request] = []
                    with Gmt(
                        base_url=cast(str, OPTIONS["base_url"]),
                        max_retries=cast(int, OPTIONS["max_retries"]),
                        timeout=cast(int, OPTIONS["timeout"]),
                        http_client=httpx.Client(transport=list_transport(requests)),
                    ) as client:
                        items = list(getattr(client, resource).list(**params))
                    self.assertEqual(len(items), 2)
                    self.assertEqual([r.url.path for r in requests], [f"/v1/{resource}/"] * 2)
                    self.assertEqual(dict(requests[0].url.params), {k: str(v) for k, v in params.items()})
                    self.assertEqual(dict(requests[1].url.params), {**{k: str(v) for k, v in params.items()}, "page": "2"})


class AsyncOptionalLists(unittest.IsolatedAsyncioTestCase):
    async def test_defaults_and_explicit_filters_survive_pagination(self) -> None:
        for resource, filters in LIST_CASES:
            for params in ({}, {**filters, "page": 1, "page_size": 1}):
                with self.subTest(resource=resource, params=params):
                    requests: List[httpx.Request] = []
                    async with AsyncGmt(
                        base_url=cast(str, OPTIONS["base_url"]),
                        max_retries=cast(int, OPTIONS["max_retries"]),
                        timeout=cast(int, OPTIONS["timeout"]),
                        http_client=httpx.AsyncClient(transport=list_transport(requests)),
                    ) as client:
                        items = [item async for item in getattr(client, resource).list(**params)]
                    self.assertEqual(len(items), 2)
                    self.assertEqual([r.url.path for r in requests], [f"/v1/{resource}/"] * 2)
                    self.assertEqual(dict(requests[0].url.params), {k: str(v) for k, v in params.items()})
                    self.assertEqual(dict(requests[1].url.params), {**{k: str(v) for k, v in params.items()}, "page": "2"})


def single_account_zip():
    output = BytesIO()
    with ZipFile(output, "w") as archive:
        archive.writestr("account.session", bytes([0, 255, 128, 13, 10, 42]))
    return output.getvalue()


ZIP_BYTES = single_account_zip()
ARCHIVE_ERROR = {
    "code": 409, "status": "ABORTED", "message": "Archive not ready",
    "details": [{"reason": "BULK_ARCHIVE_NOT_READY", "domain": "gmt"}],
}


def archive_transport(status=200):
    def reply(request):
        assert request.method == "GET"
        assert request.url.path == "/v1/purchases/bulk/123/download"
        assert request.headers["x-api-key"] == "test-api-key"
        if status != 200:
            return httpx.Response(status, json=ARCHIVE_ERROR)
        return httpx.Response(200, stream=httpx.ByteStream(ZIP_BYTES), headers={
            "content-type": "application/octet-stream",
            "content-disposition": 'attachment; filename="accounts.zip"',
        })
    return httpx.MockTransport(reply)


@unittest.skipUnless(os.environ.get("SDK_COMPAT_RELEASE"), "requires release candidate")
class SyncArchiveDownload(unittest.TestCase):
    def test_single_account_zip_in_normal_raw_and_streaming_modes(self):
        with Gmt(**OPTIONS, api_key="test-api-key", http_client=httpx.Client(transport=archive_transport())) as client:
            for mode in ("normal", "raw", "streaming"):
                with self.subTest(mode=mode), TemporaryDirectory() as directory:
                    path = Path(directory) / "accounts.zip"
                    if mode == "streaming":
                        with client.purchases.bulk.with_streaming_response.download(123) as response:
                            self.assertFalse(response.http_response.is_stream_consumed)
                            response.stream_to_file(path)
                        self.assertTrue(response.is_closed)
                    else:
                        resource = client.purchases.bulk if mode == "normal" else client.purchases.bulk.with_raw_response
                        response = resource.download(123)
                        self.assertEqual(response.read(), ZIP_BYTES)
                        self.assertEqual(response.parse(), ZIP_BYTES)
                        response.write_to_file(path)
                    self.assertEqual(response.headers["content-type"], "application/octet-stream")
                    self.assertEqual(path.read_bytes(), ZIP_BYTES)
                    with ZipFile(path) as archive:
                        self.assertEqual(archive.namelist(), ["account.session"])
                        self.assertEqual(archive.read("account.session"), bytes([0, 255, 128, 13, 10, 42]))

    def test_not_ready_remains_a_typed_http_error_in_all_modes(self):
        from gmt import ConflictError
        with Gmt(**OPTIONS, api_key="test-api-key", http_client=httpx.Client(transport=archive_transport(409))) as client:
            for mode in ("normal", "raw", "streaming"):
                with self.subTest(mode=mode), self.assertRaises(ConflictError) as caught:
                    if mode == "streaming":
                        with client.purchases.bulk.with_streaming_response.download(123):
                            self.fail("409 must raise before exposing archive data")
                    else:
                        resource = client.purchases.bulk if mode == "normal" else client.purchases.bulk.with_raw_response
                        resource.download(123)
                self.assertEqual(caught.exception.status_code, 409)
                self.assertEqual(caught.exception.body, ARCHIVE_ERROR)


@unittest.skipUnless(os.environ.get("SDK_COMPAT_RELEASE"), "requires release candidate")
class AsyncArchiveDownload(unittest.IsolatedAsyncioTestCase):
    async def test_single_account_zip_in_normal_raw_and_streaming_modes(self):
        async with AsyncGmt(**OPTIONS, api_key="test-api-key", http_client=httpx.AsyncClient(transport=archive_transport())) as client:
            for mode in ("normal", "raw", "streaming"):
                with self.subTest(mode=mode), TemporaryDirectory() as directory:
                    path = Path(directory) / "accounts.zip"
                    if mode == "streaming":
                        async with client.purchases.bulk.with_streaming_response.download(123) as response:
                            self.assertFalse(response.http_response.is_stream_consumed)
                            await response.stream_to_file(path)
                        self.assertTrue(response.is_closed)
                    else:
                        resource = client.purchases.bulk if mode == "normal" else client.purchases.bulk.with_raw_response
                        response = await resource.download(123)
                        self.assertEqual(await response.read(), ZIP_BYTES)
                        self.assertEqual(await response.parse(), ZIP_BYTES)
                        await response.write_to_file(path)
                    self.assertEqual(response.headers["content-type"], "application/octet-stream")
                    self.assertEqual(path.read_bytes(), ZIP_BYTES)
                    with ZipFile(path) as archive:
                        self.assertEqual(archive.namelist(), ["account.session"])
                        self.assertEqual(archive.read("account.session"), bytes([0, 255, 128, 13, 10, 42]))

    async def test_not_ready_remains_a_typed_http_error_in_all_modes(self):
        from gmt import ConflictError
        async with AsyncGmt(**OPTIONS, api_key="test-api-key", http_client=httpx.AsyncClient(transport=archive_transport(409))) as client:
            for mode in ("normal", "raw", "streaming"):
                with self.subTest(mode=mode), self.assertRaises(ConflictError) as caught:
                    if mode == "streaming":
                        async with client.purchases.bulk.with_streaming_response.download(123):
                            self.fail("409 must raise before exposing archive data")
                    else:
                        resource = client.purchases.bulk if mode == "normal" else client.purchases.bulk.with_raw_response
                        await resource.download(123)
                self.assertEqual(caught.exception.status_code, 409)
                self.assertEqual(caught.exception.body, ARCHIVE_ERROR)
