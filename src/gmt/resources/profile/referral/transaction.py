# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...._types import Body, Query, Headers, NotGiven, not_given
from ...._utils import maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....pagination import SyncPageNumber, AsyncPageNumber
from ...._base_client import AsyncPaginator, make_request_options
from ....types.profile.referral import transaction_list_params
from ....types.profile.referral.transaction_list_response import TransactionListResponse

__all__ = ["TransactionResource", "AsyncTransactionResource"]


class TransactionResource(SyncAPIResource):
    """User profile management."""

    @cached_property
    def with_raw_response(self) -> TransactionResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cameo6/gmt-python-sdk#accessing-raw-response-data-eg-headers
        """
        return TransactionResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TransactionResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cameo6/gmt-python-sdk#with_streaming_response
        """
        return TransactionResourceWithStreamingResponse(self)

    def list(
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
    ) -> SyncPageNumber[TransactionListResponse]:
        """
        Returns paginated referral transaction history for the authenticated user,
        ordered by newest first.

        Args:
          page: Page number.

          page_size: Number of items per page.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/v1/profile/referral/transaction",
            page=SyncPageNumber[TransactionListResponse],
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
                    transaction_list_params.TransactionListParams,
                ),
            ),
            model=TransactionListResponse,
        )


class AsyncTransactionResource(AsyncAPIResource):
    """User profile management."""

    @cached_property
    def with_raw_response(self) -> AsyncTransactionResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cameo6/gmt-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncTransactionResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTransactionResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cameo6/gmt-python-sdk#with_streaming_response
        """
        return AsyncTransactionResourceWithStreamingResponse(self)

    def list(
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
    ) -> AsyncPaginator[TransactionListResponse, AsyncPageNumber[TransactionListResponse]]:
        """
        Returns paginated referral transaction history for the authenticated user,
        ordered by newest first.

        Args:
          page: Page number.

          page_size: Number of items per page.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/v1/profile/referral/transaction",
            page=AsyncPageNumber[TransactionListResponse],
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
                    transaction_list_params.TransactionListParams,
                ),
            ),
            model=TransactionListResponse,
        )


class TransactionResourceWithRawResponse:
    def __init__(self, transaction: TransactionResource) -> None:
        self._transaction = transaction

        self.list = to_raw_response_wrapper(
            transaction.list,
        )


class AsyncTransactionResourceWithRawResponse:
    def __init__(self, transaction: AsyncTransactionResource) -> None:
        self._transaction = transaction

        self.list = async_to_raw_response_wrapper(
            transaction.list,
        )


class TransactionResourceWithStreamingResponse:
    def __init__(self, transaction: TransactionResource) -> None:
        self._transaction = transaction

        self.list = to_streamed_response_wrapper(
            transaction.list,
        )


class AsyncTransactionResourceWithStreamingResponse:
    def __init__(self, transaction: AsyncTransactionResource) -> None:
        self._transaction = transaction

        self.list = async_to_streamed_response_wrapper(
            transaction.list,
        )
