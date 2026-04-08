# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import purchases_by_hash_request_verification_code_params
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .._utils import path_template, maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.purchases_by_hash_retrieve_response import PurchasesByHashRetrieveResponse
from ..types.purchases_by_hash_request_verification_code_response import PurchasesByHashRequestVerificationCodeResponse

__all__ = ["PurchasesByHashResource", "AsyncPurchasesByHashResource"]


class PurchasesByHashResource(SyncAPIResource):
    """Purchase history and management."""

    @cached_property
    def with_raw_response(self) -> PurchasesByHashResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cameo6/gmt-python-sdk#accessing-raw-response-data-eg-headers
        """
        return PurchasesByHashResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PurchasesByHashResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cameo6/gmt-python-sdk#with_streaming_response
        """
        return PurchasesByHashResourceWithStreamingResponse(self)

    def retrieve(
        self,
        hash: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PurchasesByHashRetrieveResponse:
        """
        Returns detailed information about specific purchase by its hash code including
        verification data if available.

        **No authentication required.** The hash code serves as the access token.

        Args:
          hash: Unique hash code of the purchase

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not hash:
            raise ValueError(f"Expected a non-empty value for `hash` but received {hash!r}")
        return self._get(
            path_template("/v1/purchases-by-hash/{hash}", hash=hash),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PurchasesByHashRetrieveResponse,
        )

    def request_verification_code(
        self,
        hash: str,
        *,
        callback_url: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PurchasesByHashRequestVerificationCodeResponse:
        """
        Requests verification code and password from provider using purchase hash code.
        Updates purchase status to SUCCESS.

        **No authentication required.** The hash code serves as the access token.

        **Idempotent Operation.** Safe to retry on network errors - will not generate
        duplicate codes.

        Args:
          hash: Unique hash code of the purchase

          callback_url: URL to receive webhook notification when code is received. POST request will be
              sent with either `WebhookSuccessPayload` or `WebhookFailedPayload`.

              **Retry policy.** If your endpoint does not return HTTP 200, webhook will be
              retried up to 3 times with delays: immediately, after 10 seconds, after 30
              seconds. Any non-200 response triggers retry.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not hash:
            raise ValueError(f"Expected a non-empty value for `hash` but received {hash!r}")
        return self._post(
            path_template("/v1/purchases-by-hash/{hash}/request-code", hash=hash),
            body=maybe_transform(
                {"callback_url": callback_url},
                purchases_by_hash_request_verification_code_params.PurchasesByHashRequestVerificationCodeParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PurchasesByHashRequestVerificationCodeResponse,
        )


class AsyncPurchasesByHashResource(AsyncAPIResource):
    """Purchase history and management."""

    @cached_property
    def with_raw_response(self) -> AsyncPurchasesByHashResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cameo6/gmt-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncPurchasesByHashResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPurchasesByHashResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cameo6/gmt-python-sdk#with_streaming_response
        """
        return AsyncPurchasesByHashResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        hash: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PurchasesByHashRetrieveResponse:
        """
        Returns detailed information about specific purchase by its hash code including
        verification data if available.

        **No authentication required.** The hash code serves as the access token.

        Args:
          hash: Unique hash code of the purchase

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not hash:
            raise ValueError(f"Expected a non-empty value for `hash` but received {hash!r}")
        return await self._get(
            path_template("/v1/purchases-by-hash/{hash}", hash=hash),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PurchasesByHashRetrieveResponse,
        )

    async def request_verification_code(
        self,
        hash: str,
        *,
        callback_url: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PurchasesByHashRequestVerificationCodeResponse:
        """
        Requests verification code and password from provider using purchase hash code.
        Updates purchase status to SUCCESS.

        **No authentication required.** The hash code serves as the access token.

        **Idempotent Operation.** Safe to retry on network errors - will not generate
        duplicate codes.

        Args:
          hash: Unique hash code of the purchase

          callback_url: URL to receive webhook notification when code is received. POST request will be
              sent with either `WebhookSuccessPayload` or `WebhookFailedPayload`.

              **Retry policy.** If your endpoint does not return HTTP 200, webhook will be
              retried up to 3 times with delays: immediately, after 10 seconds, after 30
              seconds. Any non-200 response triggers retry.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not hash:
            raise ValueError(f"Expected a non-empty value for `hash` but received {hash!r}")
        return await self._post(
            path_template("/v1/purchases-by-hash/{hash}/request-code", hash=hash),
            body=await async_maybe_transform(
                {"callback_url": callback_url},
                purchases_by_hash_request_verification_code_params.PurchasesByHashRequestVerificationCodeParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PurchasesByHashRequestVerificationCodeResponse,
        )


class PurchasesByHashResourceWithRawResponse:
    def __init__(self, purchases_by_hash: PurchasesByHashResource) -> None:
        self._purchases_by_hash = purchases_by_hash

        self.retrieve = to_raw_response_wrapper(
            purchases_by_hash.retrieve,
        )
        self.request_verification_code = to_raw_response_wrapper(
            purchases_by_hash.request_verification_code,
        )


class AsyncPurchasesByHashResourceWithRawResponse:
    def __init__(self, purchases_by_hash: AsyncPurchasesByHashResource) -> None:
        self._purchases_by_hash = purchases_by_hash

        self.retrieve = async_to_raw_response_wrapper(
            purchases_by_hash.retrieve,
        )
        self.request_verification_code = async_to_raw_response_wrapper(
            purchases_by_hash.request_verification_code,
        )


class PurchasesByHashResourceWithStreamingResponse:
    def __init__(self, purchases_by_hash: PurchasesByHashResource) -> None:
        self._purchases_by_hash = purchases_by_hash

        self.retrieve = to_streamed_response_wrapper(
            purchases_by_hash.retrieve,
        )
        self.request_verification_code = to_streamed_response_wrapper(
            purchases_by_hash.request_verification_code,
        )


class AsyncPurchasesByHashResourceWithStreamingResponse:
    def __init__(self, purchases_by_hash: AsyncPurchasesByHashResource) -> None:
        self._purchases_by_hash = purchases_by_hash

        self.retrieve = async_to_streamed_response_wrapper(
            purchases_by_hash.retrieve,
        )
        self.request_verification_code = async_to_streamed_response_wrapper(
            purchases_by_hash.request_verification_code,
        )
