# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from gmt import Gmt, AsyncGmt
from gmt.types import (
    PurchasesByHashRetrieveResponse,
    PurchasesByHashRequestVerificationCodeResponse,
)
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPurchasesByHash:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Gmt) -> None:
        purchases_by_hash = client.purchases_by_hash.retrieve(
            "abc-def-1234567890",
        )
        assert_matches_type(PurchasesByHashRetrieveResponse, purchases_by_hash, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Gmt) -> None:
        response = client.purchases_by_hash.with_raw_response.retrieve(
            "abc-def-1234567890",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        purchases_by_hash = response.parse()
        assert_matches_type(PurchasesByHashRetrieveResponse, purchases_by_hash, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Gmt) -> None:
        with client.purchases_by_hash.with_streaming_response.retrieve(
            "abc-def-1234567890",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            purchases_by_hash = response.parse()
            assert_matches_type(PurchasesByHashRetrieveResponse, purchases_by_hash, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Gmt) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `hash` but received ''"):
            client.purchases_by_hash.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_request_verification_code(self, client: Gmt) -> None:
        purchases_by_hash = client.purchases_by_hash.request_verification_code(
            hash="abc-def-1234567890",
        )
        assert_matches_type(PurchasesByHashRequestVerificationCodeResponse, purchases_by_hash, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_request_verification_code_with_all_params(self, client: Gmt) -> None:
        purchases_by_hash = client.purchases_by_hash.request_verification_code(
            hash="abc-def-1234567890",
            callback_url="https://example.com/webhooks/code-received",
        )
        assert_matches_type(PurchasesByHashRequestVerificationCodeResponse, purchases_by_hash, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_request_verification_code(self, client: Gmt) -> None:
        response = client.purchases_by_hash.with_raw_response.request_verification_code(
            hash="abc-def-1234567890",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        purchases_by_hash = response.parse()
        assert_matches_type(PurchasesByHashRequestVerificationCodeResponse, purchases_by_hash, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_request_verification_code(self, client: Gmt) -> None:
        with client.purchases_by_hash.with_streaming_response.request_verification_code(
            hash="abc-def-1234567890",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            purchases_by_hash = response.parse()
            assert_matches_type(PurchasesByHashRequestVerificationCodeResponse, purchases_by_hash, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_request_verification_code(self, client: Gmt) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `hash` but received ''"):
            client.purchases_by_hash.with_raw_response.request_verification_code(
                hash="",
            )


class TestAsyncPurchasesByHash:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncGmt) -> None:
        purchases_by_hash = await async_client.purchases_by_hash.retrieve(
            "abc-def-1234567890",
        )
        assert_matches_type(PurchasesByHashRetrieveResponse, purchases_by_hash, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncGmt) -> None:
        response = await async_client.purchases_by_hash.with_raw_response.retrieve(
            "abc-def-1234567890",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        purchases_by_hash = await response.parse()
        assert_matches_type(PurchasesByHashRetrieveResponse, purchases_by_hash, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncGmt) -> None:
        async with async_client.purchases_by_hash.with_streaming_response.retrieve(
            "abc-def-1234567890",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            purchases_by_hash = await response.parse()
            assert_matches_type(PurchasesByHashRetrieveResponse, purchases_by_hash, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncGmt) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `hash` but received ''"):
            await async_client.purchases_by_hash.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_request_verification_code(self, async_client: AsyncGmt) -> None:
        purchases_by_hash = await async_client.purchases_by_hash.request_verification_code(
            hash="abc-def-1234567890",
        )
        assert_matches_type(PurchasesByHashRequestVerificationCodeResponse, purchases_by_hash, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_request_verification_code_with_all_params(self, async_client: AsyncGmt) -> None:
        purchases_by_hash = await async_client.purchases_by_hash.request_verification_code(
            hash="abc-def-1234567890",
            callback_url="https://example.com/webhooks/code-received",
        )
        assert_matches_type(PurchasesByHashRequestVerificationCodeResponse, purchases_by_hash, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_request_verification_code(self, async_client: AsyncGmt) -> None:
        response = await async_client.purchases_by_hash.with_raw_response.request_verification_code(
            hash="abc-def-1234567890",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        purchases_by_hash = await response.parse()
        assert_matches_type(PurchasesByHashRequestVerificationCodeResponse, purchases_by_hash, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_request_verification_code(self, async_client: AsyncGmt) -> None:
        async with async_client.purchases_by_hash.with_streaming_response.request_verification_code(
            hash="abc-def-1234567890",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            purchases_by_hash = await response.parse()
            assert_matches_type(PurchasesByHashRequestVerificationCodeResponse, purchases_by_hash, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_request_verification_code(self, async_client: AsyncGmt) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `hash` but received ''"):
            await async_client.purchases_by_hash.with_raw_response.request_verification_code(
                hash="",
            )
