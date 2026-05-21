# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...._types import Body, Query, Headers, NotGiven, not_given
from ...._utils import maybe_transform, async_maybe_transform
from ...._compat import cached_property
from .transaction import (
    TransactionResource,
    AsyncTransactionResource,
    TransactionResourceWithRawResponse,
    AsyncTransactionResourceWithRawResponse,
    TransactionResourceWithStreamingResponse,
    AsyncTransactionResourceWithStreamingResponse,
)
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.profile import referral_transfer_balance_params
from ....types.profile.referral_retrieve_response import ReferralRetrieveResponse
from ....types.profile.referral_transfer_balance_response import ReferralTransferBalanceResponse

__all__ = ["ReferralResource", "AsyncReferralResource"]


class ReferralResource(SyncAPIResource):
    """User profile management."""

    @cached_property
    def transaction(self) -> TransactionResource:
        """User profile management."""
        return TransactionResource(self._client)

    @cached_property
    def with_raw_response(self) -> ReferralResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cameo6/gmt-python-sdk#accessing-raw-response-data-eg-headers
        """
        return ReferralResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ReferralResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cameo6/gmt-python-sdk#with_streaming_response
        """
        return ReferralResourceWithStreamingResponse(self)

    def retrieve(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ReferralRetrieveResponse:
        """
        Returns user's referral program status, including current level, commission
        percentage, referral count, and earnings.
        """
        return self._get(
            "/v1/profile/referral",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ReferralRetrieveResponse,
        )

    def transfer_balance(
        self,
        *,
        amount: float,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ReferralTransferBalanceResponse:
        """
        Transfers a specified amount from the user's referral balance to their main
        balance. The amount must be between 1 and 100,000 USD.

        Args:
          amount: Amount to transfer from referral balance

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/profile/referral/transfer-balance",
            body=maybe_transform({"amount": amount}, referral_transfer_balance_params.ReferralTransferBalanceParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ReferralTransferBalanceResponse,
        )


class AsyncReferralResource(AsyncAPIResource):
    """User profile management."""

    @cached_property
    def transaction(self) -> AsyncTransactionResource:
        """User profile management."""
        return AsyncTransactionResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncReferralResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cameo6/gmt-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncReferralResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncReferralResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cameo6/gmt-python-sdk#with_streaming_response
        """
        return AsyncReferralResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ReferralRetrieveResponse:
        """
        Returns user's referral program status, including current level, commission
        percentage, referral count, and earnings.
        """
        return await self._get(
            "/v1/profile/referral",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ReferralRetrieveResponse,
        )

    async def transfer_balance(
        self,
        *,
        amount: float,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ReferralTransferBalanceResponse:
        """
        Transfers a specified amount from the user's referral balance to their main
        balance. The amount must be between 1 and 100,000 USD.

        Args:
          amount: Amount to transfer from referral balance

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/profile/referral/transfer-balance",
            body=await async_maybe_transform(
                {"amount": amount}, referral_transfer_balance_params.ReferralTransferBalanceParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ReferralTransferBalanceResponse,
        )


class ReferralResourceWithRawResponse:
    def __init__(self, referral: ReferralResource) -> None:
        self._referral = referral

        self.retrieve = to_raw_response_wrapper(
            referral.retrieve,
        )
        self.transfer_balance = to_raw_response_wrapper(
            referral.transfer_balance,
        )

    @cached_property
    def transaction(self) -> TransactionResourceWithRawResponse:
        """User profile management."""
        return TransactionResourceWithRawResponse(self._referral.transaction)


class AsyncReferralResourceWithRawResponse:
    def __init__(self, referral: AsyncReferralResource) -> None:
        self._referral = referral

        self.retrieve = async_to_raw_response_wrapper(
            referral.retrieve,
        )
        self.transfer_balance = async_to_raw_response_wrapper(
            referral.transfer_balance,
        )

    @cached_property
    def transaction(self) -> AsyncTransactionResourceWithRawResponse:
        """User profile management."""
        return AsyncTransactionResourceWithRawResponse(self._referral.transaction)


class ReferralResourceWithStreamingResponse:
    def __init__(self, referral: ReferralResource) -> None:
        self._referral = referral

        self.retrieve = to_streamed_response_wrapper(
            referral.retrieve,
        )
        self.transfer_balance = to_streamed_response_wrapper(
            referral.transfer_balance,
        )

    @cached_property
    def transaction(self) -> TransactionResourceWithStreamingResponse:
        """User profile management."""
        return TransactionResourceWithStreamingResponse(self._referral.transaction)


class AsyncReferralResourceWithStreamingResponse:
    def __init__(self, referral: AsyncReferralResource) -> None:
        self._referral = referral

        self.retrieve = async_to_streamed_response_wrapper(
            referral.retrieve,
        )
        self.transfer_balance = async_to_streamed_response_wrapper(
            referral.transfer_balance,
        )

    @cached_property
    def transaction(self) -> AsyncTransactionResourceWithStreamingResponse:
        """User profile management."""
        return AsyncTransactionResourceWithStreamingResponse(self._referral.transaction)
