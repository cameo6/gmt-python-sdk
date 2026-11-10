import os
import unittest

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
