# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.purchases import bulk_create_params
from ...types.purchases.bulk_create_response import BulkCreateResponse
from ...types.purchases.bulk_retrieve_response import BulkRetrieveResponse

__all__ = ["BulkResource", "AsyncBulkResource"]


class BulkResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> BulkResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cameo6/gmt-python-sdk#accessing-raw-response-data-eg-headers
        """
        return BulkResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BulkResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cameo6/gmt-python-sdk#with_streaming_response
        """
        return BulkResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        country_code: str,
        quantity: int,
        callback_url: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BulkCreateResponse:
        """Creates a new wholesale purchase for the specified country.

        Immediately debits
        the balance and returns the purchase with the status “PENDING”.

        **Wholesale purchase creation process**

        1. Checks the availability of the country and the user's balance.
        2. Reserves multiple accounts with the provider.
        3. Atomically debits the balance and creates a bulk purchase record.
        4. Returns the bulk purchase with the status “PENDING”.

        **Webhook notification.** Optionally provide `callback_url` to receive a webhook
        when the archive is ready.

        **Next steps.** Call “GET /bulk/:purchaseId” to get the account archive link.

        Args:
          country_code: ISO 3166-1 alpha-2 country code.

          quantity: Number of accounts to purchase

          callback_url: URL to receive webhook notification when bulk archive is ready. POST request
              will be sent with `WebhookBulkReadyPayload`.

              **Retry policy.** If your endpoint does not return HTTP 200, webhook will be
              retried up to 3 times with delays: immediately, after 10 seconds, after 30
              seconds. Any non-200 response triggers retry.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/purchases/bulk",
            body=maybe_transform(
                {
                    "country_code": country_code,
                    "quantity": quantity,
                    "callback_url": callback_url,
                },
                bulk_create_params.BulkCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BulkCreateResponse,
        )

    def retrieve(
        self,
        purchase_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BulkRetrieveResponse:
        """
        Returns the status of a bulk purchase, including details and link to download
        archive.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not purchase_id:
            raise ValueError(f"Expected a non-empty value for `purchase_id` but received {purchase_id!r}")
        return self._get(
            f"/v1/purchases/bulk/{purchase_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BulkRetrieveResponse,
        )

    def download(
        self,
        purchase_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Download the archive file containing multiple accounts from a successful bulk
        purchase

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not purchase_id:
            raise ValueError(f"Expected a non-empty value for `purchase_id` but received {purchase_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._get(
            f"/v1/purchases/bulk/{purchase_id}/download",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncBulkResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncBulkResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cameo6/gmt-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncBulkResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBulkResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cameo6/gmt-python-sdk#with_streaming_response
        """
        return AsyncBulkResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        country_code: str,
        quantity: int,
        callback_url: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BulkCreateResponse:
        """Creates a new wholesale purchase for the specified country.

        Immediately debits
        the balance and returns the purchase with the status “PENDING”.

        **Wholesale purchase creation process**

        1. Checks the availability of the country and the user's balance.
        2. Reserves multiple accounts with the provider.
        3. Atomically debits the balance and creates a bulk purchase record.
        4. Returns the bulk purchase with the status “PENDING”.

        **Webhook notification.** Optionally provide `callback_url` to receive a webhook
        when the archive is ready.

        **Next steps.** Call “GET /bulk/:purchaseId” to get the account archive link.

        Args:
          country_code: ISO 3166-1 alpha-2 country code.

          quantity: Number of accounts to purchase

          callback_url: URL to receive webhook notification when bulk archive is ready. POST request
              will be sent with `WebhookBulkReadyPayload`.

              **Retry policy.** If your endpoint does not return HTTP 200, webhook will be
              retried up to 3 times with delays: immediately, after 10 seconds, after 30
              seconds. Any non-200 response triggers retry.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/purchases/bulk",
            body=await async_maybe_transform(
                {
                    "country_code": country_code,
                    "quantity": quantity,
                    "callback_url": callback_url,
                },
                bulk_create_params.BulkCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BulkCreateResponse,
        )

    async def retrieve(
        self,
        purchase_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BulkRetrieveResponse:
        """
        Returns the status of a bulk purchase, including details and link to download
        archive.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not purchase_id:
            raise ValueError(f"Expected a non-empty value for `purchase_id` but received {purchase_id!r}")
        return await self._get(
            f"/v1/purchases/bulk/{purchase_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BulkRetrieveResponse,
        )

    async def download(
        self,
        purchase_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Download the archive file containing multiple accounts from a successful bulk
        purchase

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not purchase_id:
            raise ValueError(f"Expected a non-empty value for `purchase_id` but received {purchase_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._get(
            f"/v1/purchases/bulk/{purchase_id}/download",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class BulkResourceWithRawResponse:
    def __init__(self, bulk: BulkResource) -> None:
        self._bulk = bulk

        self.create = to_raw_response_wrapper(
            bulk.create,
        )
        self.retrieve = to_raw_response_wrapper(
            bulk.retrieve,
        )
        self.download = to_raw_response_wrapper(
            bulk.download,
        )


class AsyncBulkResourceWithRawResponse:
    def __init__(self, bulk: AsyncBulkResource) -> None:
        self._bulk = bulk

        self.create = async_to_raw_response_wrapper(
            bulk.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            bulk.retrieve,
        )
        self.download = async_to_raw_response_wrapper(
            bulk.download,
        )


class BulkResourceWithStreamingResponse:
    def __init__(self, bulk: BulkResource) -> None:
        self._bulk = bulk

        self.create = to_streamed_response_wrapper(
            bulk.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            bulk.retrieve,
        )
        self.download = to_streamed_response_wrapper(
            bulk.download,
        )


class AsyncBulkResourceWithStreamingResponse:
    def __init__(self, bulk: AsyncBulkResource) -> None:
        self._bulk = bulk

        self.create = async_to_streamed_response_wrapper(
            bulk.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            bulk.retrieve,
        )
        self.download = async_to_streamed_response_wrapper(
            bulk.download,
        )
