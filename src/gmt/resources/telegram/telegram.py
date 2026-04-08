# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...types import telegram_get_stars_price_params, telegram_get_premium_price_params
from ..._types import Body, Query, Headers, NotGiven, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from .purchases import (
    PurchasesResource,
    AsyncPurchasesResource,
    PurchasesResourceWithRawResponse,
    AsyncPurchasesResourceWithRawResponse,
    PurchasesResourceWithStreamingResponse,
    AsyncPurchasesResourceWithStreamingResponse,
)
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.telegram_get_stars_price_response import TelegramGetStarsPriceResponse
from ...types.telegram_get_premium_price_response import TelegramGetPremiumPriceResponse

__all__ = ["TelegramResource", "AsyncTelegramResource"]


class TelegramResource(SyncAPIResource):
    @cached_property
    def purchases(self) -> PurchasesResource:
        return PurchasesResource(self._client)

    @cached_property
    def with_raw_response(self) -> TelegramResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cameo6/gmt-python-sdk#accessing-raw-response-data-eg-headers
        """
        return TelegramResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TelegramResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cameo6/gmt-python-sdk#with_streaming_response
        """
        return TelegramResourceWithStreamingResponse(self)

    def get_premium_price(
        self,
        *,
        mounts: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TelegramGetPremiumPriceResponse:
        """
        Returns the current price of Telegram premium subscription in USD.

        Args:
          mounts: The number of months for the premium subscription (3, 6, or 12)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v1/telegram/premium",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"mounts": mounts}, telegram_get_premium_price_params.TelegramGetPremiumPriceParams
                ),
            ),
            cast_to=TelegramGetPremiumPriceResponse,
        )

    def get_stars_price(
        self,
        *,
        amount: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TelegramGetStarsPriceResponse:
        """
        Returns the current price of stars in USD.

        Args:
          amount: The amount of stars to purchase (50-10000)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v1/telegram/stars",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"amount": amount}, telegram_get_stars_price_params.TelegramGetStarsPriceParams),
            ),
            cast_to=TelegramGetStarsPriceResponse,
        )


class AsyncTelegramResource(AsyncAPIResource):
    @cached_property
    def purchases(self) -> AsyncPurchasesResource:
        return AsyncPurchasesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncTelegramResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cameo6/gmt-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncTelegramResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTelegramResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cameo6/gmt-python-sdk#with_streaming_response
        """
        return AsyncTelegramResourceWithStreamingResponse(self)

    async def get_premium_price(
        self,
        *,
        mounts: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TelegramGetPremiumPriceResponse:
        """
        Returns the current price of Telegram premium subscription in USD.

        Args:
          mounts: The number of months for the premium subscription (3, 6, or 12)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v1/telegram/premium",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"mounts": mounts}, telegram_get_premium_price_params.TelegramGetPremiumPriceParams
                ),
            ),
            cast_to=TelegramGetPremiumPriceResponse,
        )

    async def get_stars_price(
        self,
        *,
        amount: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TelegramGetStarsPriceResponse:
        """
        Returns the current price of stars in USD.

        Args:
          amount: The amount of stars to purchase (50-10000)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v1/telegram/stars",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"amount": amount}, telegram_get_stars_price_params.TelegramGetStarsPriceParams
                ),
            ),
            cast_to=TelegramGetStarsPriceResponse,
        )


class TelegramResourceWithRawResponse:
    def __init__(self, telegram: TelegramResource) -> None:
        self._telegram = telegram

        self.get_premium_price = to_raw_response_wrapper(
            telegram.get_premium_price,
        )
        self.get_stars_price = to_raw_response_wrapper(
            telegram.get_stars_price,
        )

    @cached_property
    def purchases(self) -> PurchasesResourceWithRawResponse:
        return PurchasesResourceWithRawResponse(self._telegram.purchases)


class AsyncTelegramResourceWithRawResponse:
    def __init__(self, telegram: AsyncTelegramResource) -> None:
        self._telegram = telegram

        self.get_premium_price = async_to_raw_response_wrapper(
            telegram.get_premium_price,
        )
        self.get_stars_price = async_to_raw_response_wrapper(
            telegram.get_stars_price,
        )

    @cached_property
    def purchases(self) -> AsyncPurchasesResourceWithRawResponse:
        return AsyncPurchasesResourceWithRawResponse(self._telegram.purchases)


class TelegramResourceWithStreamingResponse:
    def __init__(self, telegram: TelegramResource) -> None:
        self._telegram = telegram

        self.get_premium_price = to_streamed_response_wrapper(
            telegram.get_premium_price,
        )
        self.get_stars_price = to_streamed_response_wrapper(
            telegram.get_stars_price,
        )

    @cached_property
    def purchases(self) -> PurchasesResourceWithStreamingResponse:
        return PurchasesResourceWithStreamingResponse(self._telegram.purchases)


class AsyncTelegramResourceWithStreamingResponse:
    def __init__(self, telegram: AsyncTelegramResource) -> None:
        self._telegram = telegram

        self.get_premium_price = async_to_streamed_response_wrapper(
            telegram.get_premium_price,
        )
        self.get_stars_price = async_to_streamed_response_wrapper(
            telegram.get_stars_price,
        )

    @cached_property
    def purchases(self) -> AsyncPurchasesResourceWithStreamingResponse:
        return AsyncPurchasesResourceWithStreamingResponse(self._telegram.purchases)
