# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from gmt import Gmt, AsyncGmt
from gmt.types import (
    ProfileRetrieveResponse,
    ProfileChangeLoginResponse,
    ProfileChangePasswordResponse,
    ProfileUnbindTelegramResponse,
)
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestProfile:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Gmt) -> None:
        profile = client.profile.retrieve()
        assert_matches_type(ProfileRetrieveResponse, profile, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Gmt) -> None:
        response = client.profile.with_raw_response.retrieve()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        profile = response.parse()
        assert_matches_type(ProfileRetrieveResponse, profile, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Gmt) -> None:
        with client.profile.with_streaming_response.retrieve() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            profile = response.parse()
            assert_matches_type(ProfileRetrieveResponse, profile, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_change_login(self, client: Gmt) -> None:
        profile = client.profile.change_login(
            new_login="username",
        )
        assert_matches_type(ProfileChangeLoginResponse, profile, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_change_login(self, client: Gmt) -> None:
        response = client.profile.with_raw_response.change_login(
            new_login="username",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        profile = response.parse()
        assert_matches_type(ProfileChangeLoginResponse, profile, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_change_login(self, client: Gmt) -> None:
        with client.profile.with_streaming_response.change_login(
            new_login="username",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            profile = response.parse()
            assert_matches_type(ProfileChangeLoginResponse, profile, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_change_password(self, client: Gmt) -> None:
        profile = client.profile.change_password(
            new_password="Password123",
        )
        assert_matches_type(ProfileChangePasswordResponse, profile, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_change_password(self, client: Gmt) -> None:
        response = client.profile.with_raw_response.change_password(
            new_password="Password123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        profile = response.parse()
        assert_matches_type(ProfileChangePasswordResponse, profile, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_change_password(self, client: Gmt) -> None:
        with client.profile.with_streaming_response.change_password(
            new_password="Password123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            profile = response.parse()
            assert_matches_type(ProfileChangePasswordResponse, profile, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_unbind_telegram(self, client: Gmt) -> None:
        profile = client.profile.unbind_telegram()
        assert_matches_type(ProfileUnbindTelegramResponse, profile, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_unbind_telegram(self, client: Gmt) -> None:
        response = client.profile.with_raw_response.unbind_telegram()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        profile = response.parse()
        assert_matches_type(ProfileUnbindTelegramResponse, profile, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_unbind_telegram(self, client: Gmt) -> None:
        with client.profile.with_streaming_response.unbind_telegram() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            profile = response.parse()
            assert_matches_type(ProfileUnbindTelegramResponse, profile, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncProfile:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncGmt) -> None:
        profile = await async_client.profile.retrieve()
        assert_matches_type(ProfileRetrieveResponse, profile, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncGmt) -> None:
        response = await async_client.profile.with_raw_response.retrieve()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        profile = await response.parse()
        assert_matches_type(ProfileRetrieveResponse, profile, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncGmt) -> None:
        async with async_client.profile.with_streaming_response.retrieve() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            profile = await response.parse()
            assert_matches_type(ProfileRetrieveResponse, profile, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_change_login(self, async_client: AsyncGmt) -> None:
        profile = await async_client.profile.change_login(
            new_login="username",
        )
        assert_matches_type(ProfileChangeLoginResponse, profile, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_change_login(self, async_client: AsyncGmt) -> None:
        response = await async_client.profile.with_raw_response.change_login(
            new_login="username",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        profile = await response.parse()
        assert_matches_type(ProfileChangeLoginResponse, profile, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_change_login(self, async_client: AsyncGmt) -> None:
        async with async_client.profile.with_streaming_response.change_login(
            new_login="username",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            profile = await response.parse()
            assert_matches_type(ProfileChangeLoginResponse, profile, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_change_password(self, async_client: AsyncGmt) -> None:
        profile = await async_client.profile.change_password(
            new_password="Password123",
        )
        assert_matches_type(ProfileChangePasswordResponse, profile, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_change_password(self, async_client: AsyncGmt) -> None:
        response = await async_client.profile.with_raw_response.change_password(
            new_password="Password123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        profile = await response.parse()
        assert_matches_type(ProfileChangePasswordResponse, profile, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_change_password(self, async_client: AsyncGmt) -> None:
        async with async_client.profile.with_streaming_response.change_password(
            new_password="Password123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            profile = await response.parse()
            assert_matches_type(ProfileChangePasswordResponse, profile, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_unbind_telegram(self, async_client: AsyncGmt) -> None:
        profile = await async_client.profile.unbind_telegram()
        assert_matches_type(ProfileUnbindTelegramResponse, profile, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_unbind_telegram(self, async_client: AsyncGmt) -> None:
        response = await async_client.profile.with_raw_response.unbind_telegram()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        profile = await response.parse()
        assert_matches_type(ProfileUnbindTelegramResponse, profile, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_unbind_telegram(self, async_client: AsyncGmt) -> None:
        async with async_client.profile.with_streaming_response.unbind_telegram() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            profile = await response.parse()
            assert_matches_type(ProfileUnbindTelegramResponse, profile, path=["response"])

        assert cast(Any, response.is_closed) is True
