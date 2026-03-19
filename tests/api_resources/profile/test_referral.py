# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from gmt import Gmt, AsyncGmt
from tests.utils import assert_matches_type
from gmt.types.profile import (
    ReferralRetrieveResponse,
    ReferralTransferBalanceResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestReferral:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Gmt) -> None:
        referral = client.profile.referral.retrieve()
        assert_matches_type(ReferralRetrieveResponse, referral, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Gmt) -> None:
        response = client.profile.referral.with_raw_response.retrieve()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        referral = response.parse()
        assert_matches_type(ReferralRetrieveResponse, referral, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Gmt) -> None:
        with client.profile.referral.with_streaming_response.retrieve() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            referral = response.parse()
            assert_matches_type(ReferralRetrieveResponse, referral, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_transfer_balance(self, client: Gmt) -> None:
        referral = client.profile.referral.transfer_balance(
            amount=100,
        )
        assert_matches_type(ReferralTransferBalanceResponse, referral, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_transfer_balance(self, client: Gmt) -> None:
        response = client.profile.referral.with_raw_response.transfer_balance(
            amount=100,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        referral = response.parse()
        assert_matches_type(ReferralTransferBalanceResponse, referral, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_transfer_balance(self, client: Gmt) -> None:
        with client.profile.referral.with_streaming_response.transfer_balance(
            amount=100,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            referral = response.parse()
            assert_matches_type(ReferralTransferBalanceResponse, referral, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncReferral:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncGmt) -> None:
        referral = await async_client.profile.referral.retrieve()
        assert_matches_type(ReferralRetrieveResponse, referral, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncGmt) -> None:
        response = await async_client.profile.referral.with_raw_response.retrieve()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        referral = await response.parse()
        assert_matches_type(ReferralRetrieveResponse, referral, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncGmt) -> None:
        async with async_client.profile.referral.with_streaming_response.retrieve() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            referral = await response.parse()
            assert_matches_type(ReferralRetrieveResponse, referral, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_transfer_balance(self, async_client: AsyncGmt) -> None:
        referral = await async_client.profile.referral.transfer_balance(
            amount=100,
        )
        assert_matches_type(ReferralTransferBalanceResponse, referral, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_transfer_balance(self, async_client: AsyncGmt) -> None:
        response = await async_client.profile.referral.with_raw_response.transfer_balance(
            amount=100,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        referral = await response.parse()
        assert_matches_type(ReferralTransferBalanceResponse, referral, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_transfer_balance(self, async_client: AsyncGmt) -> None:
        async with async_client.profile.referral.with_streaming_response.transfer_balance(
            amount=100,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            referral = await response.parse()
            assert_matches_type(ReferralTransferBalanceResponse, referral, path=["response"])

        assert cast(Any, response.is_closed) is True
