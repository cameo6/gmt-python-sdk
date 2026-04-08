# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import Body, Query, Headers, NotGiven, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...pagination import SyncPageNumber, AsyncPageNumber
from ..._base_client import AsyncPaginator, make_request_options
from ...types.telegram import (
    purchase_list_stars_params,
    purchase_create_stars_params,
    purchase_list_premium_params,
    purchase_create_premium_params,
)
from ...types.telegram.purchase_list_stars_response import PurchaseListStarsResponse
from ...types.telegram.purchase_create_stars_response import PurchaseCreateStarsResponse
from ...types.telegram.purchase_list_premium_response import PurchaseListPremiumResponse
from ...types.telegram.purchase_create_premium_response import PurchaseCreatePremiumResponse

__all__ = ["PurchasesResource", "AsyncPurchasesResource"]


class PurchasesResource(SyncAPIResource):
    """Stars and premium subscription for Telegram."""

    @cached_property
    def with_raw_response(self) -> PurchasesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cameo6/gmt-python-sdk#accessing-raw-response-data-eg-headers
        """
        return PurchasesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PurchasesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cameo6/gmt-python-sdk#with_streaming_response
        """
        return PurchasesResourceWithStreamingResponse(self)

    def create_premium(
        self,
        *,
        mounts: float,
        username: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PurchaseCreatePremiumResponse:
        """Creates a new purchase for Telegram premium subscription.

        Deducts balance
        immediately and returns purchase details.

        Args:
          mounts: The number of months for the premium subscription (3, 6, or 12)

          username: Recipient Telegram username (@optional, 5-32 chars)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/telegram/purchases/premium",
            body=maybe_transform(
                {
                    "mounts": mounts,
                    "username": username,
                },
                purchase_create_premium_params.PurchaseCreatePremiumParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PurchaseCreatePremiumResponse,
        )

    def create_stars(
        self,
        *,
        amount: float,
        username: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PurchaseCreateStarsResponse:
        """Creates a new purchase for Telegram stars.

        Deducts balance immediately and
        returns purchase details.

        Args:
          amount: The amount of stars to purchase (50-10000)

          username: Recipient Telegram username (@optional, 5-32 chars)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/telegram/purchases/stars",
            body=maybe_transform(
                {
                    "amount": amount,
                    "username": username,
                },
                purchase_create_stars_params.PurchaseCreateStarsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PurchaseCreateStarsResponse,
        )

    def list_premium(
        self,
        *,
        page: int,
        page_size: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncPageNumber[PurchaseListPremiumResponse]:
        """
        Returns paginated history of Telegram premium subscription purchases for the
        authenticated user.

        Args:
          page: Page number.

          page_size: Number of items per page.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/v1/telegram/purchases/premium",
            page=SyncPageNumber[PurchaseListPremiumResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "page": page,
                        "page_size": page_size,
                    },
                    purchase_list_premium_params.PurchaseListPremiumParams,
                ),
            ),
            model=PurchaseListPremiumResponse,
        )

    def list_stars(
        self,
        *,
        page: int,
        page_size: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncPageNumber[PurchaseListStarsResponse]:
        """
        Returns paginated history of star purchases for the authenticated user.

        Args:
          page: Page number.

          page_size: Number of items per page.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/v1/telegram/purchases/stars",
            page=SyncPageNumber[PurchaseListStarsResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "page": page,
                        "page_size": page_size,
                    },
                    purchase_list_stars_params.PurchaseListStarsParams,
                ),
            ),
            model=PurchaseListStarsResponse,
        )


class AsyncPurchasesResource(AsyncAPIResource):
    """Stars and premium subscription for Telegram."""

    @cached_property
    def with_raw_response(self) -> AsyncPurchasesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cameo6/gmt-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncPurchasesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPurchasesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cameo6/gmt-python-sdk#with_streaming_response
        """
        return AsyncPurchasesResourceWithStreamingResponse(self)

    async def create_premium(
        self,
        *,
        mounts: float,
        username: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PurchaseCreatePremiumResponse:
        """Creates a new purchase for Telegram premium subscription.

        Deducts balance
        immediately and returns purchase details.

        Args:
          mounts: The number of months for the premium subscription (3, 6, or 12)

          username: Recipient Telegram username (@optional, 5-32 chars)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/telegram/purchases/premium",
            body=await async_maybe_transform(
                {
                    "mounts": mounts,
                    "username": username,
                },
                purchase_create_premium_params.PurchaseCreatePremiumParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PurchaseCreatePremiumResponse,
        )

    async def create_stars(
        self,
        *,
        amount: float,
        username: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PurchaseCreateStarsResponse:
        """Creates a new purchase for Telegram stars.

        Deducts balance immediately and
        returns purchase details.

        Args:
          amount: The amount of stars to purchase (50-10000)

          username: Recipient Telegram username (@optional, 5-32 chars)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/telegram/purchases/stars",
            body=await async_maybe_transform(
                {
                    "amount": amount,
                    "username": username,
                },
                purchase_create_stars_params.PurchaseCreateStarsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PurchaseCreateStarsResponse,
        )

    def list_premium(
        self,
        *,
        page: int,
        page_size: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[PurchaseListPremiumResponse, AsyncPageNumber[PurchaseListPremiumResponse]]:
        """
        Returns paginated history of Telegram premium subscription purchases for the
        authenticated user.

        Args:
          page: Page number.

          page_size: Number of items per page.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/v1/telegram/purchases/premium",
            page=AsyncPageNumber[PurchaseListPremiumResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "page": page,
                        "page_size": page_size,
                    },
                    purchase_list_premium_params.PurchaseListPremiumParams,
                ),
            ),
            model=PurchaseListPremiumResponse,
        )

    def list_stars(
        self,
        *,
        page: int,
        page_size: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[PurchaseListStarsResponse, AsyncPageNumber[PurchaseListStarsResponse]]:
        """
        Returns paginated history of star purchases for the authenticated user.

        Args:
          page: Page number.

          page_size: Number of items per page.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/v1/telegram/purchases/stars",
            page=AsyncPageNumber[PurchaseListStarsResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "page": page,
                        "page_size": page_size,
                    },
                    purchase_list_stars_params.PurchaseListStarsParams,
                ),
            ),
            model=PurchaseListStarsResponse,
        )


class PurchasesResourceWithRawResponse:
    def __init__(self, purchases: PurchasesResource) -> None:
        self._purchases = purchases

        self.create_premium = to_raw_response_wrapper(
            purchases.create_premium,
        )
        self.create_stars = to_raw_response_wrapper(
            purchases.create_stars,
        )
        self.list_premium = to_raw_response_wrapper(
            purchases.list_premium,
        )
        self.list_stars = to_raw_response_wrapper(
            purchases.list_stars,
        )


class AsyncPurchasesResourceWithRawResponse:
    def __init__(self, purchases: AsyncPurchasesResource) -> None:
        self._purchases = purchases

        self.create_premium = async_to_raw_response_wrapper(
            purchases.create_premium,
        )
        self.create_stars = async_to_raw_response_wrapper(
            purchases.create_stars,
        )
        self.list_premium = async_to_raw_response_wrapper(
            purchases.list_premium,
        )
        self.list_stars = async_to_raw_response_wrapper(
            purchases.list_stars,
        )


class PurchasesResourceWithStreamingResponse:
    def __init__(self, purchases: PurchasesResource) -> None:
        self._purchases = purchases

        self.create_premium = to_streamed_response_wrapper(
            purchases.create_premium,
        )
        self.create_stars = to_streamed_response_wrapper(
            purchases.create_stars,
        )
        self.list_premium = to_streamed_response_wrapper(
            purchases.list_premium,
        )
        self.list_stars = to_streamed_response_wrapper(
            purchases.list_stars,
        )


class AsyncPurchasesResourceWithStreamingResponse:
    def __init__(self, purchases: AsyncPurchasesResource) -> None:
        self._purchases = purchases

        self.create_premium = async_to_streamed_response_wrapper(
            purchases.create_premium,
        )
        self.create_stars = async_to_streamed_response_wrapper(
            purchases.create_stars,
        )
        self.list_premium = async_to_streamed_response_wrapper(
            purchases.list_premium,
        )
        self.list_stars = async_to_streamed_response_wrapper(
            purchases.list_stars,
        )
