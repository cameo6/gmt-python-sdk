# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import TYPE_CHECKING, Any, Mapping
from typing_extensions import Self, override

import httpx

from . import _exceptions
from ._qs import Querystring
from ._types import (
    Omit,
    Timeout,
    NotGiven,
    Transport,
    ProxiesTypes,
    RequestOptions,
    not_given,
)
from ._utils import (
    is_given,
    is_mapping_t,
    get_async_library,
)
from ._compat import cached_property
from ._version import __version__
from ._streaming import Stream as Stream, AsyncStream as AsyncStream
from ._exceptions import APIStatusError
from ._base_client import (
    DEFAULT_MAX_RETRIES,
    SyncAPIClient,
    AsyncAPIClient,
)

if TYPE_CHECKING:
    from .resources import profile, service, accounts, webhooks, purchases, purchases_by_hash
    from .resources.service import ServiceResource, AsyncServiceResource
    from .resources.accounts import AccountsResource, AsyncAccountsResource
    from .resources.webhooks import WebhooksResource, AsyncWebhooksResource
    from .resources.profile.profile import ProfileResource, AsyncProfileResource
    from .resources.purchases_by_hash import PurchasesByHashResource, AsyncPurchasesByHashResource
    from .resources.purchases.purchases import PurchasesResource, AsyncPurchasesResource

__all__ = ["Timeout", "Transport", "ProxiesTypes", "RequestOptions", "Gmt", "AsyncGmt", "Client", "AsyncClient"]


class Gmt(SyncAPIClient):
    # client options
    api_key: str | None

    def __init__(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#client) for more details.
        http_client: httpx.Client | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new synchronous Gmt client instance.

        This automatically infers the `api_key` argument from the `GMT_API_KEY` environment variable if it is not provided.
        """
        if api_key is None:
            api_key = os.environ.get("GMT_API_KEY")
        self.api_key = api_key

        if base_url is None:
            base_url = os.environ.get("GMT_BASE_URL")
        if base_url is None:
            base_url = f"https://api.getmytg.com"

        custom_headers_env = os.environ.get("GMT_CUSTOM_HEADERS")
        if custom_headers_env is not None:
            parsed: dict[str, str] = {}
            for line in custom_headers_env.split("\n"):
                colon = line.find(":")
                if colon >= 0:
                    parsed[line[:colon].strip()] = line[colon + 1 :].strip()
            default_headers = {**parsed, **(default_headers if is_mapping_t(default_headers) else {})}

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

    @cached_property
    def service(self) -> ServiceResource:
        """Service endpoints for API health checks."""
        from .resources.service import ServiceResource

        return ServiceResource(self)

    @cached_property
    def accounts(self) -> AccountsResource:
        """Browse and purchase Telegram accounts.

        **Endpoints overview:**
        - `GET /accounts/countries` — Public catalog with base prices (no auth required)
        - `GET /accounts` — Personalized list with user's discounted prices (auth required)
        - `GET /accounts/:country_code` — Detailed pricing breakdown with discount info (auth required)

        **Pricing model.** Base prices are set per country. Authenticated users may receive a personal discount based on their purchase history (discount level). Use `/accounts/:country_code` to see the full price breakdown.
        """
        from .resources.accounts import AccountsResource

        return AccountsResource(self)

    @cached_property
    def profile(self) -> ProfileResource:
        """User profile management."""
        from .resources.profile import ProfileResource

        return ProfileResource(self)

    @cached_property
    def purchases(self) -> PurchasesResource:
        """Purchase history and management."""
        from .resources.purchases import PurchasesResource

        return PurchasesResource(self)

    @cached_property
    def purchases_by_hash(self) -> PurchasesByHashResource:
        """
        Endpoints for accessing purchase details and requesting verification codes using a unique hash identifier instead of purchase ID. This allows retrieval of purchase information without authentication, using the hash as a secure access token.
        """
        from .resources.purchases_by_hash import PurchasesByHashResource

        return PurchasesByHashResource(self)

    @cached_property
    def webhooks(self) -> WebhooksResource:
        """Webhook testing and documentation.

        ## Webhook Payload Types

        When you provide `callback_url` in `POST /purchases/:id/request-code`, your endpoint will receive one of the following payloads:

        - **WebhookSuccessPayload** — sent when verification code is successfully retrieved
        - **WebhookFailedPayload** — sent when code retrieval fails after all retry attempts

        When you provide `callback_url` in `POST /purchases/bulk`, your endpoint will receive:

        - **WebhookBulkReadyPayload** — sent when bulk archive is ready

        See the **Models** section below for detailed payload structure.

        ## Requirements

        - Your endpoint **must return HTTP 200** to acknowledge receipt
        - Response timeout: **5 seconds**
        - Failed deliveries are retried up to **3 times** (immediately, after 10s, after 30s)

        ## Testing

        Use `POST /v1/webhooks/test` to verify your endpoint. Get a temporary test URL at https://webhook.site
        """
        from .resources.webhooks import WebhooksResource

        return WebhooksResource(self)

    @cached_property
    def with_raw_response(self) -> GmtWithRawResponse:
        return GmtWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> GmtWithStreamedResponse:
        return GmtWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        api_key = self.api_key
        if api_key is None:
            return {}
        return {"x-api-key": api_key}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": "false",
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        http_client: httpx.Client | None = None,
        max_retries: int | NotGiven = not_given,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            api_key=api_key or self.api_key,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class AsyncGmt(AsyncAPIClient):
    # client options
    api_key: str | None

    def __init__(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultAsyncHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#asyncclient) for more details.
        http_client: httpx.AsyncClient | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new async AsyncGmt client instance.

        This automatically infers the `api_key` argument from the `GMT_API_KEY` environment variable if it is not provided.
        """
        if api_key is None:
            api_key = os.environ.get("GMT_API_KEY")
        self.api_key = api_key

        if base_url is None:
            base_url = os.environ.get("GMT_BASE_URL")
        if base_url is None:
            base_url = f"https://api.getmytg.com"

        custom_headers_env = os.environ.get("GMT_CUSTOM_HEADERS")
        if custom_headers_env is not None:
            parsed: dict[str, str] = {}
            for line in custom_headers_env.split("\n"):
                colon = line.find(":")
                if colon >= 0:
                    parsed[line[:colon].strip()] = line[colon + 1 :].strip()
            default_headers = {**parsed, **(default_headers if is_mapping_t(default_headers) else {})}

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

    @cached_property
    def service(self) -> AsyncServiceResource:
        """Service endpoints for API health checks."""
        from .resources.service import AsyncServiceResource

        return AsyncServiceResource(self)

    @cached_property
    def accounts(self) -> AsyncAccountsResource:
        """Browse and purchase Telegram accounts.

        **Endpoints overview:**
        - `GET /accounts/countries` — Public catalog with base prices (no auth required)
        - `GET /accounts` — Personalized list with user's discounted prices (auth required)
        - `GET /accounts/:country_code` — Detailed pricing breakdown with discount info (auth required)

        **Pricing model.** Base prices are set per country. Authenticated users may receive a personal discount based on their purchase history (discount level). Use `/accounts/:country_code` to see the full price breakdown.
        """
        from .resources.accounts import AsyncAccountsResource

        return AsyncAccountsResource(self)

    @cached_property
    def profile(self) -> AsyncProfileResource:
        """User profile management."""
        from .resources.profile import AsyncProfileResource

        return AsyncProfileResource(self)

    @cached_property
    def purchases(self) -> AsyncPurchasesResource:
        """Purchase history and management."""
        from .resources.purchases import AsyncPurchasesResource

        return AsyncPurchasesResource(self)

    @cached_property
    def purchases_by_hash(self) -> AsyncPurchasesByHashResource:
        """
        Endpoints for accessing purchase details and requesting verification codes using a unique hash identifier instead of purchase ID. This allows retrieval of purchase information without authentication, using the hash as a secure access token.
        """
        from .resources.purchases_by_hash import AsyncPurchasesByHashResource

        return AsyncPurchasesByHashResource(self)

    @cached_property
    def webhooks(self) -> AsyncWebhooksResource:
        """Webhook testing and documentation.

        ## Webhook Payload Types

        When you provide `callback_url` in `POST /purchases/:id/request-code`, your endpoint will receive one of the following payloads:

        - **WebhookSuccessPayload** — sent when verification code is successfully retrieved
        - **WebhookFailedPayload** — sent when code retrieval fails after all retry attempts

        When you provide `callback_url` in `POST /purchases/bulk`, your endpoint will receive:

        - **WebhookBulkReadyPayload** — sent when bulk archive is ready

        See the **Models** section below for detailed payload structure.

        ## Requirements

        - Your endpoint **must return HTTP 200** to acknowledge receipt
        - Response timeout: **5 seconds**
        - Failed deliveries are retried up to **3 times** (immediately, after 10s, after 30s)

        ## Testing

        Use `POST /v1/webhooks/test` to verify your endpoint. Get a temporary test URL at https://webhook.site
        """
        from .resources.webhooks import AsyncWebhooksResource

        return AsyncWebhooksResource(self)

    @cached_property
    def with_raw_response(self) -> AsyncGmtWithRawResponse:
        return AsyncGmtWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncGmtWithStreamedResponse:
        return AsyncGmtWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        api_key = self.api_key
        if api_key is None:
            return {}
        return {"x-api-key": api_key}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": f"async:{get_async_library()}",
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        http_client: httpx.AsyncClient | None = None,
        max_retries: int | NotGiven = not_given,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            api_key=api_key or self.api_key,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class GmtWithRawResponse:
    _client: Gmt

    def __init__(self, client: Gmt) -> None:
        self._client = client

    @cached_property
    def service(self) -> service.ServiceResourceWithRawResponse:
        """Service endpoints for API health checks."""
        from .resources.service import ServiceResourceWithRawResponse

        return ServiceResourceWithRawResponse(self._client.service)

    @cached_property
    def accounts(self) -> accounts.AccountsResourceWithRawResponse:
        """Browse and purchase Telegram accounts.

        **Endpoints overview:**
        - `GET /accounts/countries` — Public catalog with base prices (no auth required)
        - `GET /accounts` — Personalized list with user's discounted prices (auth required)
        - `GET /accounts/:country_code` — Detailed pricing breakdown with discount info (auth required)

        **Pricing model.** Base prices are set per country. Authenticated users may receive a personal discount based on their purchase history (discount level). Use `/accounts/:country_code` to see the full price breakdown.
        """
        from .resources.accounts import AccountsResourceWithRawResponse

        return AccountsResourceWithRawResponse(self._client.accounts)

    @cached_property
    def profile(self) -> profile.ProfileResourceWithRawResponse:
        """User profile management."""
        from .resources.profile import ProfileResourceWithRawResponse

        return ProfileResourceWithRawResponse(self._client.profile)

    @cached_property
    def purchases(self) -> purchases.PurchasesResourceWithRawResponse:
        """Purchase history and management."""
        from .resources.purchases import PurchasesResourceWithRawResponse

        return PurchasesResourceWithRawResponse(self._client.purchases)

    @cached_property
    def purchases_by_hash(self) -> purchases_by_hash.PurchasesByHashResourceWithRawResponse:
        """
        Endpoints for accessing purchase details and requesting verification codes using a unique hash identifier instead of purchase ID. This allows retrieval of purchase information without authentication, using the hash as a secure access token.
        """
        from .resources.purchases_by_hash import PurchasesByHashResourceWithRawResponse

        return PurchasesByHashResourceWithRawResponse(self._client.purchases_by_hash)

    @cached_property
    def webhooks(self) -> webhooks.WebhooksResourceWithRawResponse:
        """Webhook testing and documentation.

        ## Webhook Payload Types

        When you provide `callback_url` in `POST /purchases/:id/request-code`, your endpoint will receive one of the following payloads:

        - **WebhookSuccessPayload** — sent when verification code is successfully retrieved
        - **WebhookFailedPayload** — sent when code retrieval fails after all retry attempts

        When you provide `callback_url` in `POST /purchases/bulk`, your endpoint will receive:

        - **WebhookBulkReadyPayload** — sent when bulk archive is ready

        See the **Models** section below for detailed payload structure.

        ## Requirements

        - Your endpoint **must return HTTP 200** to acknowledge receipt
        - Response timeout: **5 seconds**
        - Failed deliveries are retried up to **3 times** (immediately, after 10s, after 30s)

        ## Testing

        Use `POST /v1/webhooks/test` to verify your endpoint. Get a temporary test URL at https://webhook.site
        """
        from .resources.webhooks import WebhooksResourceWithRawResponse

        return WebhooksResourceWithRawResponse(self._client.webhooks)


class AsyncGmtWithRawResponse:
    _client: AsyncGmt

    def __init__(self, client: AsyncGmt) -> None:
        self._client = client

    @cached_property
    def service(self) -> service.AsyncServiceResourceWithRawResponse:
        """Service endpoints for API health checks."""
        from .resources.service import AsyncServiceResourceWithRawResponse

        return AsyncServiceResourceWithRawResponse(self._client.service)

    @cached_property
    def accounts(self) -> accounts.AsyncAccountsResourceWithRawResponse:
        """Browse and purchase Telegram accounts.

        **Endpoints overview:**
        - `GET /accounts/countries` — Public catalog with base prices (no auth required)
        - `GET /accounts` — Personalized list with user's discounted prices (auth required)
        - `GET /accounts/:country_code` — Detailed pricing breakdown with discount info (auth required)

        **Pricing model.** Base prices are set per country. Authenticated users may receive a personal discount based on their purchase history (discount level). Use `/accounts/:country_code` to see the full price breakdown.
        """
        from .resources.accounts import AsyncAccountsResourceWithRawResponse

        return AsyncAccountsResourceWithRawResponse(self._client.accounts)

    @cached_property
    def profile(self) -> profile.AsyncProfileResourceWithRawResponse:
        """User profile management."""
        from .resources.profile import AsyncProfileResourceWithRawResponse

        return AsyncProfileResourceWithRawResponse(self._client.profile)

    @cached_property
    def purchases(self) -> purchases.AsyncPurchasesResourceWithRawResponse:
        """Purchase history and management."""
        from .resources.purchases import AsyncPurchasesResourceWithRawResponse

        return AsyncPurchasesResourceWithRawResponse(self._client.purchases)

    @cached_property
    def purchases_by_hash(self) -> purchases_by_hash.AsyncPurchasesByHashResourceWithRawResponse:
        """
        Endpoints for accessing purchase details and requesting verification codes using a unique hash identifier instead of purchase ID. This allows retrieval of purchase information without authentication, using the hash as a secure access token.
        """
        from .resources.purchases_by_hash import AsyncPurchasesByHashResourceWithRawResponse

        return AsyncPurchasesByHashResourceWithRawResponse(self._client.purchases_by_hash)

    @cached_property
    def webhooks(self) -> webhooks.AsyncWebhooksResourceWithRawResponse:
        """Webhook testing and documentation.

        ## Webhook Payload Types

        When you provide `callback_url` in `POST /purchases/:id/request-code`, your endpoint will receive one of the following payloads:

        - **WebhookSuccessPayload** — sent when verification code is successfully retrieved
        - **WebhookFailedPayload** — sent when code retrieval fails after all retry attempts

        When you provide `callback_url` in `POST /purchases/bulk`, your endpoint will receive:

        - **WebhookBulkReadyPayload** — sent when bulk archive is ready

        See the **Models** section below for detailed payload structure.

        ## Requirements

        - Your endpoint **must return HTTP 200** to acknowledge receipt
        - Response timeout: **5 seconds**
        - Failed deliveries are retried up to **3 times** (immediately, after 10s, after 30s)

        ## Testing

        Use `POST /v1/webhooks/test` to verify your endpoint. Get a temporary test URL at https://webhook.site
        """
        from .resources.webhooks import AsyncWebhooksResourceWithRawResponse

        return AsyncWebhooksResourceWithRawResponse(self._client.webhooks)


class GmtWithStreamedResponse:
    _client: Gmt

    def __init__(self, client: Gmt) -> None:
        self._client = client

    @cached_property
    def service(self) -> service.ServiceResourceWithStreamingResponse:
        """Service endpoints for API health checks."""
        from .resources.service import ServiceResourceWithStreamingResponse

        return ServiceResourceWithStreamingResponse(self._client.service)

    @cached_property
    def accounts(self) -> accounts.AccountsResourceWithStreamingResponse:
        """Browse and purchase Telegram accounts.

        **Endpoints overview:**
        - `GET /accounts/countries` — Public catalog with base prices (no auth required)
        - `GET /accounts` — Personalized list with user's discounted prices (auth required)
        - `GET /accounts/:country_code` — Detailed pricing breakdown with discount info (auth required)

        **Pricing model.** Base prices are set per country. Authenticated users may receive a personal discount based on their purchase history (discount level). Use `/accounts/:country_code` to see the full price breakdown.
        """
        from .resources.accounts import AccountsResourceWithStreamingResponse

        return AccountsResourceWithStreamingResponse(self._client.accounts)

    @cached_property
    def profile(self) -> profile.ProfileResourceWithStreamingResponse:
        """User profile management."""
        from .resources.profile import ProfileResourceWithStreamingResponse

        return ProfileResourceWithStreamingResponse(self._client.profile)

    @cached_property
    def purchases(self) -> purchases.PurchasesResourceWithStreamingResponse:
        """Purchase history and management."""
        from .resources.purchases import PurchasesResourceWithStreamingResponse

        return PurchasesResourceWithStreamingResponse(self._client.purchases)

    @cached_property
    def purchases_by_hash(self) -> purchases_by_hash.PurchasesByHashResourceWithStreamingResponse:
        """
        Endpoints for accessing purchase details and requesting verification codes using a unique hash identifier instead of purchase ID. This allows retrieval of purchase information without authentication, using the hash as a secure access token.
        """
        from .resources.purchases_by_hash import PurchasesByHashResourceWithStreamingResponse

        return PurchasesByHashResourceWithStreamingResponse(self._client.purchases_by_hash)

    @cached_property
    def webhooks(self) -> webhooks.WebhooksResourceWithStreamingResponse:
        """Webhook testing and documentation.

        ## Webhook Payload Types

        When you provide `callback_url` in `POST /purchases/:id/request-code`, your endpoint will receive one of the following payloads:

        - **WebhookSuccessPayload** — sent when verification code is successfully retrieved
        - **WebhookFailedPayload** — sent when code retrieval fails after all retry attempts

        When you provide `callback_url` in `POST /purchases/bulk`, your endpoint will receive:

        - **WebhookBulkReadyPayload** — sent when bulk archive is ready

        See the **Models** section below for detailed payload structure.

        ## Requirements

        - Your endpoint **must return HTTP 200** to acknowledge receipt
        - Response timeout: **5 seconds**
        - Failed deliveries are retried up to **3 times** (immediately, after 10s, after 30s)

        ## Testing

        Use `POST /v1/webhooks/test` to verify your endpoint. Get a temporary test URL at https://webhook.site
        """
        from .resources.webhooks import WebhooksResourceWithStreamingResponse

        return WebhooksResourceWithStreamingResponse(self._client.webhooks)


class AsyncGmtWithStreamedResponse:
    _client: AsyncGmt

    def __init__(self, client: AsyncGmt) -> None:
        self._client = client

    @cached_property
    def service(self) -> service.AsyncServiceResourceWithStreamingResponse:
        """Service endpoints for API health checks."""
        from .resources.service import AsyncServiceResourceWithStreamingResponse

        return AsyncServiceResourceWithStreamingResponse(self._client.service)

    @cached_property
    def accounts(self) -> accounts.AsyncAccountsResourceWithStreamingResponse:
        """Browse and purchase Telegram accounts.

        **Endpoints overview:**
        - `GET /accounts/countries` — Public catalog with base prices (no auth required)
        - `GET /accounts` — Personalized list with user's discounted prices (auth required)
        - `GET /accounts/:country_code` — Detailed pricing breakdown with discount info (auth required)

        **Pricing model.** Base prices are set per country. Authenticated users may receive a personal discount based on their purchase history (discount level). Use `/accounts/:country_code` to see the full price breakdown.
        """
        from .resources.accounts import AsyncAccountsResourceWithStreamingResponse

        return AsyncAccountsResourceWithStreamingResponse(self._client.accounts)

    @cached_property
    def profile(self) -> profile.AsyncProfileResourceWithStreamingResponse:
        """User profile management."""
        from .resources.profile import AsyncProfileResourceWithStreamingResponse

        return AsyncProfileResourceWithStreamingResponse(self._client.profile)

    @cached_property
    def purchases(self) -> purchases.AsyncPurchasesResourceWithStreamingResponse:
        """Purchase history and management."""
        from .resources.purchases import AsyncPurchasesResourceWithStreamingResponse

        return AsyncPurchasesResourceWithStreamingResponse(self._client.purchases)

    @cached_property
    def purchases_by_hash(self) -> purchases_by_hash.AsyncPurchasesByHashResourceWithStreamingResponse:
        """
        Endpoints for accessing purchase details and requesting verification codes using a unique hash identifier instead of purchase ID. This allows retrieval of purchase information without authentication, using the hash as a secure access token.
        """
        from .resources.purchases_by_hash import AsyncPurchasesByHashResourceWithStreamingResponse

        return AsyncPurchasesByHashResourceWithStreamingResponse(self._client.purchases_by_hash)

    @cached_property
    def webhooks(self) -> webhooks.AsyncWebhooksResourceWithStreamingResponse:
        """Webhook testing and documentation.

        ## Webhook Payload Types

        When you provide `callback_url` in `POST /purchases/:id/request-code`, your endpoint will receive one of the following payloads:

        - **WebhookSuccessPayload** — sent when verification code is successfully retrieved
        - **WebhookFailedPayload** — sent when code retrieval fails after all retry attempts

        When you provide `callback_url` in `POST /purchases/bulk`, your endpoint will receive:

        - **WebhookBulkReadyPayload** — sent when bulk archive is ready

        See the **Models** section below for detailed payload structure.

        ## Requirements

        - Your endpoint **must return HTTP 200** to acknowledge receipt
        - Response timeout: **5 seconds**
        - Failed deliveries are retried up to **3 times** (immediately, after 10s, after 30s)

        ## Testing

        Use `POST /v1/webhooks/test` to verify your endpoint. Get a temporary test URL at https://webhook.site
        """
        from .resources.webhooks import AsyncWebhooksResourceWithStreamingResponse

        return AsyncWebhooksResourceWithStreamingResponse(self._client.webhooks)


Client = Gmt

AsyncClient = AsyncGmt
