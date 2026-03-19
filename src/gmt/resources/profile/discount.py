# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import Body, Query, Headers, NotGiven, not_given
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.profile.discount_retrieve_response import DiscountRetrieveResponse

__all__ = ["DiscountResource", "AsyncDiscountResource"]


class DiscountResource(SyncAPIResource):
    """User profile management."""

    @cached_property
    def with_raw_response(self) -> DiscountResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cameo6/gmt-python-sdk#accessing-raw-response-data-eg-headers
        """
        return DiscountResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DiscountResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cameo6/gmt-python-sdk#with_streaming_response
        """
        return DiscountResourceWithStreamingResponse(self)

    def retrieve(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DiscountRetrieveResponse:
        """
        Returns user's current discount level and percentage based on their purchase
        history.
        """
        return self._get(
            "/v1/profile/discount",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DiscountRetrieveResponse,
        )


class AsyncDiscountResource(AsyncAPIResource):
    """User profile management."""

    @cached_property
    def with_raw_response(self) -> AsyncDiscountResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cameo6/gmt-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncDiscountResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDiscountResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cameo6/gmt-python-sdk#with_streaming_response
        """
        return AsyncDiscountResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DiscountRetrieveResponse:
        """
        Returns user's current discount level and percentage based on their purchase
        history.
        """
        return await self._get(
            "/v1/profile/discount",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DiscountRetrieveResponse,
        )


class DiscountResourceWithRawResponse:
    def __init__(self, discount: DiscountResource) -> None:
        self._discount = discount

        self.retrieve = to_raw_response_wrapper(
            discount.retrieve,
        )


class AsyncDiscountResourceWithRawResponse:
    def __init__(self, discount: AsyncDiscountResource) -> None:
        self._discount = discount

        self.retrieve = async_to_raw_response_wrapper(
            discount.retrieve,
        )


class DiscountResourceWithStreamingResponse:
    def __init__(self, discount: DiscountResource) -> None:
        self._discount = discount

        self.retrieve = to_streamed_response_wrapper(
            discount.retrieve,
        )


class AsyncDiscountResourceWithStreamingResponse:
    def __init__(self, discount: AsyncDiscountResource) -> None:
        self._discount = discount

        self.retrieve = async_to_streamed_response_wrapper(
            discount.retrieve,
        )
