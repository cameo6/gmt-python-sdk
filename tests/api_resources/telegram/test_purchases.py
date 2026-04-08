# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from gmt import Gmt, AsyncGmt
from tests.utils import assert_matches_type
from gmt.pagination import SyncPageNumber, AsyncPageNumber
from gmt.types.telegram import (
    PurchaseListStarsResponse,
    PurchaseCreateStarsResponse,
    PurchaseListPremiumResponse,
    PurchaseCreatePremiumResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPurchases:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_premium(self, client: Gmt) -> None:
        purchase = client.telegram.purchases.create_premium(
            mounts=6,
            username="@john_doe",
        )
        assert_matches_type(PurchaseCreatePremiumResponse, purchase, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create_premium(self, client: Gmt) -> None:
        response = client.telegram.purchases.with_raw_response.create_premium(
            mounts=6,
            username="@john_doe",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        purchase = response.parse()
        assert_matches_type(PurchaseCreatePremiumResponse, purchase, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create_premium(self, client: Gmt) -> None:
        with client.telegram.purchases.with_streaming_response.create_premium(
            mounts=6,
            username="@john_doe",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            purchase = response.parse()
            assert_matches_type(PurchaseCreatePremiumResponse, purchase, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_stars(self, client: Gmt) -> None:
        purchase = client.telegram.purchases.create_stars(
            amount=100,
            username="@john_doe",
        )
        assert_matches_type(PurchaseCreateStarsResponse, purchase, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create_stars(self, client: Gmt) -> None:
        response = client.telegram.purchases.with_raw_response.create_stars(
            amount=100,
            username="@john_doe",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        purchase = response.parse()
        assert_matches_type(PurchaseCreateStarsResponse, purchase, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create_stars(self, client: Gmt) -> None:
        with client.telegram.purchases.with_streaming_response.create_stars(
            amount=100,
            username="@john_doe",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            purchase = response.parse()
            assert_matches_type(PurchaseCreateStarsResponse, purchase, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_premium(self, client: Gmt) -> None:
        purchase = client.telegram.purchases.list_premium(
            page=1,
            page_size=50,
        )
        assert_matches_type(SyncPageNumber[PurchaseListPremiumResponse], purchase, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_premium(self, client: Gmt) -> None:
        response = client.telegram.purchases.with_raw_response.list_premium(
            page=1,
            page_size=50,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        purchase = response.parse()
        assert_matches_type(SyncPageNumber[PurchaseListPremiumResponse], purchase, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_premium(self, client: Gmt) -> None:
        with client.telegram.purchases.with_streaming_response.list_premium(
            page=1,
            page_size=50,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            purchase = response.parse()
            assert_matches_type(SyncPageNumber[PurchaseListPremiumResponse], purchase, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_stars(self, client: Gmt) -> None:
        purchase = client.telegram.purchases.list_stars(
            page=1,
            page_size=50,
        )
        assert_matches_type(SyncPageNumber[PurchaseListStarsResponse], purchase, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_stars(self, client: Gmt) -> None:
        response = client.telegram.purchases.with_raw_response.list_stars(
            page=1,
            page_size=50,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        purchase = response.parse()
        assert_matches_type(SyncPageNumber[PurchaseListStarsResponse], purchase, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_stars(self, client: Gmt) -> None:
        with client.telegram.purchases.with_streaming_response.list_stars(
            page=1,
            page_size=50,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            purchase = response.parse()
            assert_matches_type(SyncPageNumber[PurchaseListStarsResponse], purchase, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncPurchases:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_premium(self, async_client: AsyncGmt) -> None:
        purchase = await async_client.telegram.purchases.create_premium(
            mounts=6,
            username="@john_doe",
        )
        assert_matches_type(PurchaseCreatePremiumResponse, purchase, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create_premium(self, async_client: AsyncGmt) -> None:
        response = await async_client.telegram.purchases.with_raw_response.create_premium(
            mounts=6,
            username="@john_doe",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        purchase = await response.parse()
        assert_matches_type(PurchaseCreatePremiumResponse, purchase, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create_premium(self, async_client: AsyncGmt) -> None:
        async with async_client.telegram.purchases.with_streaming_response.create_premium(
            mounts=6,
            username="@john_doe",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            purchase = await response.parse()
            assert_matches_type(PurchaseCreatePremiumResponse, purchase, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_stars(self, async_client: AsyncGmt) -> None:
        purchase = await async_client.telegram.purchases.create_stars(
            amount=100,
            username="@john_doe",
        )
        assert_matches_type(PurchaseCreateStarsResponse, purchase, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create_stars(self, async_client: AsyncGmt) -> None:
        response = await async_client.telegram.purchases.with_raw_response.create_stars(
            amount=100,
            username="@john_doe",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        purchase = await response.parse()
        assert_matches_type(PurchaseCreateStarsResponse, purchase, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create_stars(self, async_client: AsyncGmt) -> None:
        async with async_client.telegram.purchases.with_streaming_response.create_stars(
            amount=100,
            username="@john_doe",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            purchase = await response.parse()
            assert_matches_type(PurchaseCreateStarsResponse, purchase, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_premium(self, async_client: AsyncGmt) -> None:
        purchase = await async_client.telegram.purchases.list_premium(
            page=1,
            page_size=50,
        )
        assert_matches_type(AsyncPageNumber[PurchaseListPremiumResponse], purchase, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_premium(self, async_client: AsyncGmt) -> None:
        response = await async_client.telegram.purchases.with_raw_response.list_premium(
            page=1,
            page_size=50,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        purchase = await response.parse()
        assert_matches_type(AsyncPageNumber[PurchaseListPremiumResponse], purchase, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_premium(self, async_client: AsyncGmt) -> None:
        async with async_client.telegram.purchases.with_streaming_response.list_premium(
            page=1,
            page_size=50,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            purchase = await response.parse()
            assert_matches_type(AsyncPageNumber[PurchaseListPremiumResponse], purchase, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_stars(self, async_client: AsyncGmt) -> None:
        purchase = await async_client.telegram.purchases.list_stars(
            page=1,
            page_size=50,
        )
        assert_matches_type(AsyncPageNumber[PurchaseListStarsResponse], purchase, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_stars(self, async_client: AsyncGmt) -> None:
        response = await async_client.telegram.purchases.with_raw_response.list_stars(
            page=1,
            page_size=50,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        purchase = await response.parse()
        assert_matches_type(AsyncPageNumber[PurchaseListStarsResponse], purchase, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_stars(self, async_client: AsyncGmt) -> None:
        async with async_client.telegram.purchases.with_streaming_response.list_stars(
            page=1,
            page_size=50,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            purchase = await response.parse()
            assert_matches_type(AsyncPageNumber[PurchaseListStarsResponse], purchase, path=["response"])

        assert cast(Any, response.is_closed) is True
