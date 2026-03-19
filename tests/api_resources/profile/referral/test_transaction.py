# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from gmt import Gmt, AsyncGmt
from tests.utils import assert_matches_type
from gmt.pagination import SyncPageNumber, AsyncPageNumber
from gmt.types.profile.referral import TransactionListResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTransaction:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Gmt) -> None:
        transaction = client.profile.referral.transaction.list(
            page=1,
            page_size=50,
        )
        assert_matches_type(SyncPageNumber[TransactionListResponse], transaction, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Gmt) -> None:
        response = client.profile.referral.transaction.with_raw_response.list(
            page=1,
            page_size=50,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        transaction = response.parse()
        assert_matches_type(SyncPageNumber[TransactionListResponse], transaction, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Gmt) -> None:
        with client.profile.referral.transaction.with_streaming_response.list(
            page=1,
            page_size=50,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            transaction = response.parse()
            assert_matches_type(SyncPageNumber[TransactionListResponse], transaction, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncTransaction:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncGmt) -> None:
        transaction = await async_client.profile.referral.transaction.list(
            page=1,
            page_size=50,
        )
        assert_matches_type(AsyncPageNumber[TransactionListResponse], transaction, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncGmt) -> None:
        response = await async_client.profile.referral.transaction.with_raw_response.list(
            page=1,
            page_size=50,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        transaction = await response.parse()
        assert_matches_type(AsyncPageNumber[TransactionListResponse], transaction, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncGmt) -> None:
        async with async_client.profile.referral.transaction.with_streaming_response.list(
            page=1,
            page_size=50,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            transaction = await response.parse()
            assert_matches_type(AsyncPageNumber[TransactionListResponse], transaction, path=["response"])

        assert cast(Any, response.is_closed) is True
