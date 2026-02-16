# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import httpx
import pytest
from respx import MockRouter

from gmt import Gmt, AsyncGmt
from tests.utils import assert_matches_type
from gmt._response import (
    BinaryAPIResponse,
    AsyncBinaryAPIResponse,
    StreamedBinaryAPIResponse,
    AsyncStreamedBinaryAPIResponse,
)
from gmt.types.purchases import BulkCreateResponse, BulkRetrieveResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestBulk:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: Gmt) -> None:
        bulk = client.purchases.bulk.create(
            country_code="US",
            quantity=10,
        )
        assert_matches_type(BulkCreateResponse, bulk, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Gmt) -> None:
        bulk = client.purchases.bulk.create(
            country_code="US",
            quantity=10,
            callback_url="https://example.com/webhooks/code-received",
        )
        assert_matches_type(BulkCreateResponse, bulk, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Gmt) -> None:
        response = client.purchases.bulk.with_raw_response.create(
            country_code="US",
            quantity=10,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bulk = response.parse()
        assert_matches_type(BulkCreateResponse, bulk, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Gmt) -> None:
        with client.purchases.bulk.with_streaming_response.create(
            country_code="US",
            quantity=10,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bulk = response.parse()
            assert_matches_type(BulkCreateResponse, bulk, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Gmt) -> None:
        bulk = client.purchases.bulk.retrieve(
            "purchase_id",
        )
        assert_matches_type(BulkRetrieveResponse, bulk, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Gmt) -> None:
        response = client.purchases.bulk.with_raw_response.retrieve(
            "purchase_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bulk = response.parse()
        assert_matches_type(BulkRetrieveResponse, bulk, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Gmt) -> None:
        with client.purchases.bulk.with_streaming_response.retrieve(
            "purchase_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bulk = response.parse()
            assert_matches_type(BulkRetrieveResponse, bulk, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Gmt) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `purchase_id` but received ''"):
            client.purchases.bulk.with_raw_response.retrieve(
                "",
            )

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_download(self, client: Gmt, respx_mock: MockRouter) -> None:
        respx_mock.get("/v1/purchases/bulk/purchase_id/download").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        bulk = client.purchases.bulk.download(
            "purchase_id",
        )
        assert bulk.is_closed
        assert bulk.json() == {"foo": "bar"}
        assert cast(Any, bulk.is_closed) is True
        assert isinstance(bulk, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_raw_response_download(self, client: Gmt, respx_mock: MockRouter) -> None:
        respx_mock.get("/v1/purchases/bulk/purchase_id/download").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        bulk = client.purchases.bulk.with_raw_response.download(
            "purchase_id",
        )

        assert bulk.is_closed is True
        assert bulk.http_request.headers.get("X-Stainless-Lang") == "python"
        assert bulk.json() == {"foo": "bar"}
        assert isinstance(bulk, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_streaming_response_download(self, client: Gmt, respx_mock: MockRouter) -> None:
        respx_mock.get("/v1/purchases/bulk/purchase_id/download").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        with client.purchases.bulk.with_streaming_response.download(
            "purchase_id",
        ) as bulk:
            assert not bulk.is_closed
            assert bulk.http_request.headers.get("X-Stainless-Lang") == "python"

            assert bulk.json() == {"foo": "bar"}
            assert cast(Any, bulk.is_closed) is True
            assert isinstance(bulk, StreamedBinaryAPIResponse)

        assert cast(Any, bulk.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_path_params_download(self, client: Gmt) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `purchase_id` but received ''"):
            client.purchases.bulk.with_raw_response.download(
                "",
            )


class TestAsyncBulk:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncGmt) -> None:
        bulk = await async_client.purchases.bulk.create(
            country_code="US",
            quantity=10,
        )
        assert_matches_type(BulkCreateResponse, bulk, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncGmt) -> None:
        bulk = await async_client.purchases.bulk.create(
            country_code="US",
            quantity=10,
            callback_url="https://example.com/webhooks/code-received",
        )
        assert_matches_type(BulkCreateResponse, bulk, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncGmt) -> None:
        response = await async_client.purchases.bulk.with_raw_response.create(
            country_code="US",
            quantity=10,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bulk = await response.parse()
        assert_matches_type(BulkCreateResponse, bulk, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncGmt) -> None:
        async with async_client.purchases.bulk.with_streaming_response.create(
            country_code="US",
            quantity=10,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bulk = await response.parse()
            assert_matches_type(BulkCreateResponse, bulk, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncGmt) -> None:
        bulk = await async_client.purchases.bulk.retrieve(
            "purchase_id",
        )
        assert_matches_type(BulkRetrieveResponse, bulk, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncGmt) -> None:
        response = await async_client.purchases.bulk.with_raw_response.retrieve(
            "purchase_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bulk = await response.parse()
        assert_matches_type(BulkRetrieveResponse, bulk, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncGmt) -> None:
        async with async_client.purchases.bulk.with_streaming_response.retrieve(
            "purchase_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bulk = await response.parse()
            assert_matches_type(BulkRetrieveResponse, bulk, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncGmt) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `purchase_id` but received ''"):
            await async_client.purchases.bulk.with_raw_response.retrieve(
                "",
            )

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_download(self, async_client: AsyncGmt, respx_mock: MockRouter) -> None:
        respx_mock.get("/v1/purchases/bulk/purchase_id/download").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        bulk = await async_client.purchases.bulk.download(
            "purchase_id",
        )
        assert bulk.is_closed
        assert await bulk.json() == {"foo": "bar"}
        assert cast(Any, bulk.is_closed) is True
        assert isinstance(bulk, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_raw_response_download(self, async_client: AsyncGmt, respx_mock: MockRouter) -> None:
        respx_mock.get("/v1/purchases/bulk/purchase_id/download").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        bulk = await async_client.purchases.bulk.with_raw_response.download(
            "purchase_id",
        )

        assert bulk.is_closed is True
        assert bulk.http_request.headers.get("X-Stainless-Lang") == "python"
        assert await bulk.json() == {"foo": "bar"}
        assert isinstance(bulk, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_streaming_response_download(self, async_client: AsyncGmt, respx_mock: MockRouter) -> None:
        respx_mock.get("/v1/purchases/bulk/purchase_id/download").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        async with async_client.purchases.bulk.with_streaming_response.download(
            "purchase_id",
        ) as bulk:
            assert not bulk.is_closed
            assert bulk.http_request.headers.get("X-Stainless-Lang") == "python"

            assert await bulk.json() == {"foo": "bar"}
            assert cast(Any, bulk.is_closed) is True
            assert isinstance(bulk, AsyncStreamedBinaryAPIResponse)

        assert cast(Any, bulk.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_path_params_download(self, async_client: AsyncGmt) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `purchase_id` but received ''"):
            await async_client.purchases.bulk.with_raw_response.download(
                "",
            )
