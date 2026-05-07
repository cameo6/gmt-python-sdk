# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ...types import profile_change_login_params, profile_change_language_params, profile_change_password_params
from ..._types import Body, Query, Headers, NotGiven, not_given
from ..._utils import maybe_transform, async_maybe_transform
from .discount import (
    DiscountResource,
    AsyncDiscountResource,
    DiscountResourceWithRawResponse,
    AsyncDiscountResourceWithRawResponse,
    DiscountResourceWithStreamingResponse,
    AsyncDiscountResourceWithStreamingResponse,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from .referral.referral import (
    ReferralResource,
    AsyncReferralResource,
    ReferralResourceWithRawResponse,
    AsyncReferralResourceWithRawResponse,
    ReferralResourceWithStreamingResponse,
    AsyncReferralResourceWithStreamingResponse,
)
from ...types.profile_retrieve_response import ProfileRetrieveResponse
from ...types.profile_change_login_response import ProfileChangeLoginResponse
from ...types.profile_change_language_response import ProfileChangeLanguageResponse
from ...types.profile_change_password_response import ProfileChangePasswordResponse
from ...types.profile_unbind_telegram_response import ProfileUnbindTelegramResponse

__all__ = ["ProfileResource", "AsyncProfileResource"]


class ProfileResource(SyncAPIResource):
    """User profile management."""

    @cached_property
    def discount(self) -> DiscountResource:
        """User profile management."""
        return DiscountResource(self._client)

    @cached_property
    def referral(self) -> ReferralResource:
        """User profile management."""
        return ReferralResource(self._client)

    @cached_property
    def with_raw_response(self) -> ProfileResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cameo6/gmt-python-sdk#accessing-raw-response-data-eg-headers
        """
        return ProfileResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ProfileResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cameo6/gmt-python-sdk#with_streaming_response
        """
        return ProfileResourceWithStreamingResponse(self)

    def retrieve(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProfileRetrieveResponse:
        """
        Returns detailed user profile information including balances, statistics, and
        program levels.
        """
        return self._get(
            "/v1/profile/",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProfileRetrieveResponse,
        )

    def change_language(
        self,
        *,
        language: Literal["ru", "ua", "en", "es", "zh"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProfileChangeLanguageResponse:
        """
        Change the preferred user interface language on the website and in the bot.

        Args:
          language: Preferred user interface language

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._patch(
            "/v1/profile/language",
            body=maybe_transform({"language": language}, profile_change_language_params.ProfileChangeLanguageParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProfileChangeLanguageResponse,
        )

    def change_login(
        self,
        *,
        new_login: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProfileChangeLoginResponse:
        """
        Change the current user login to a new one.

        Args:
          new_login: User login for registration

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._patch(
            "/v1/profile/change-login",
            body=maybe_transform({"new_login": new_login}, profile_change_login_params.ProfileChangeLoginParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProfileChangeLoginResponse,
        )

    def change_password(
        self,
        *,
        new_password: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProfileChangePasswordResponse:
        """
        Change the current user password to a new one.

        Args:
          new_password: User password. Must contain at least two character types: lowercase, uppercase,
              digits, or special characters

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._patch(
            "/v1/profile/change-password",
            body=maybe_transform(
                {"new_password": new_password}, profile_change_password_params.ProfileChangePasswordParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProfileChangePasswordResponse,
        )

    def unbind_telegram(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProfileUnbindTelegramResponse:
        """
        Disables linking of the Telegram account to the user's web profile, all data
        remains on the web account.
        """
        return self._patch(
            "/v1/profile/unbind-telegram",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProfileUnbindTelegramResponse,
        )


class AsyncProfileResource(AsyncAPIResource):
    """User profile management."""

    @cached_property
    def discount(self) -> AsyncDiscountResource:
        """User profile management."""
        return AsyncDiscountResource(self._client)

    @cached_property
    def referral(self) -> AsyncReferralResource:
        """User profile management."""
        return AsyncReferralResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncProfileResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cameo6/gmt-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncProfileResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncProfileResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cameo6/gmt-python-sdk#with_streaming_response
        """
        return AsyncProfileResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProfileRetrieveResponse:
        """
        Returns detailed user profile information including balances, statistics, and
        program levels.
        """
        return await self._get(
            "/v1/profile/",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProfileRetrieveResponse,
        )

    async def change_language(
        self,
        *,
        language: Literal["ru", "ua", "en", "es", "zh"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProfileChangeLanguageResponse:
        """
        Change the preferred user interface language on the website and in the bot.

        Args:
          language: Preferred user interface language

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._patch(
            "/v1/profile/language",
            body=await async_maybe_transform(
                {"language": language}, profile_change_language_params.ProfileChangeLanguageParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProfileChangeLanguageResponse,
        )

    async def change_login(
        self,
        *,
        new_login: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProfileChangeLoginResponse:
        """
        Change the current user login to a new one.

        Args:
          new_login: User login for registration

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._patch(
            "/v1/profile/change-login",
            body=await async_maybe_transform(
                {"new_login": new_login}, profile_change_login_params.ProfileChangeLoginParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProfileChangeLoginResponse,
        )

    async def change_password(
        self,
        *,
        new_password: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProfileChangePasswordResponse:
        """
        Change the current user password to a new one.

        Args:
          new_password: User password. Must contain at least two character types: lowercase, uppercase,
              digits, or special characters

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._patch(
            "/v1/profile/change-password",
            body=await async_maybe_transform(
                {"new_password": new_password}, profile_change_password_params.ProfileChangePasswordParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProfileChangePasswordResponse,
        )

    async def unbind_telegram(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProfileUnbindTelegramResponse:
        """
        Disables linking of the Telegram account to the user's web profile, all data
        remains on the web account.
        """
        return await self._patch(
            "/v1/profile/unbind-telegram",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProfileUnbindTelegramResponse,
        )


class ProfileResourceWithRawResponse:
    def __init__(self, profile: ProfileResource) -> None:
        self._profile = profile

        self.retrieve = to_raw_response_wrapper(
            profile.retrieve,
        )
        self.change_language = to_raw_response_wrapper(
            profile.change_language,
        )
        self.change_login = to_raw_response_wrapper(
            profile.change_login,
        )
        self.change_password = to_raw_response_wrapper(
            profile.change_password,
        )
        self.unbind_telegram = to_raw_response_wrapper(
            profile.unbind_telegram,
        )

    @cached_property
    def discount(self) -> DiscountResourceWithRawResponse:
        """User profile management."""
        return DiscountResourceWithRawResponse(self._profile.discount)

    @cached_property
    def referral(self) -> ReferralResourceWithRawResponse:
        """User profile management."""
        return ReferralResourceWithRawResponse(self._profile.referral)


class AsyncProfileResourceWithRawResponse:
    def __init__(self, profile: AsyncProfileResource) -> None:
        self._profile = profile

        self.retrieve = async_to_raw_response_wrapper(
            profile.retrieve,
        )
        self.change_language = async_to_raw_response_wrapper(
            profile.change_language,
        )
        self.change_login = async_to_raw_response_wrapper(
            profile.change_login,
        )
        self.change_password = async_to_raw_response_wrapper(
            profile.change_password,
        )
        self.unbind_telegram = async_to_raw_response_wrapper(
            profile.unbind_telegram,
        )

    @cached_property
    def discount(self) -> AsyncDiscountResourceWithRawResponse:
        """User profile management."""
        return AsyncDiscountResourceWithRawResponse(self._profile.discount)

    @cached_property
    def referral(self) -> AsyncReferralResourceWithRawResponse:
        """User profile management."""
        return AsyncReferralResourceWithRawResponse(self._profile.referral)


class ProfileResourceWithStreamingResponse:
    def __init__(self, profile: ProfileResource) -> None:
        self._profile = profile

        self.retrieve = to_streamed_response_wrapper(
            profile.retrieve,
        )
        self.change_language = to_streamed_response_wrapper(
            profile.change_language,
        )
        self.change_login = to_streamed_response_wrapper(
            profile.change_login,
        )
        self.change_password = to_streamed_response_wrapper(
            profile.change_password,
        )
        self.unbind_telegram = to_streamed_response_wrapper(
            profile.unbind_telegram,
        )

    @cached_property
    def discount(self) -> DiscountResourceWithStreamingResponse:
        """User profile management."""
        return DiscountResourceWithStreamingResponse(self._profile.discount)

    @cached_property
    def referral(self) -> ReferralResourceWithStreamingResponse:
        """User profile management."""
        return ReferralResourceWithStreamingResponse(self._profile.referral)


class AsyncProfileResourceWithStreamingResponse:
    def __init__(self, profile: AsyncProfileResource) -> None:
        self._profile = profile

        self.retrieve = async_to_streamed_response_wrapper(
            profile.retrieve,
        )
        self.change_language = async_to_streamed_response_wrapper(
            profile.change_language,
        )
        self.change_login = async_to_streamed_response_wrapper(
            profile.change_login,
        )
        self.change_password = async_to_streamed_response_wrapper(
            profile.change_password,
        )
        self.unbind_telegram = async_to_streamed_response_wrapper(
            profile.unbind_telegram,
        )

    @cached_property
    def discount(self) -> AsyncDiscountResourceWithStreamingResponse:
        """User profile management."""
        return AsyncDiscountResourceWithStreamingResponse(self._profile.discount)

    @cached_property
    def referral(self) -> AsyncReferralResourceWithStreamingResponse:
        """User profile management."""
        return AsyncReferralResourceWithStreamingResponse(self._profile.referral)
