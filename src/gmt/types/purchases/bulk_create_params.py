# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["BulkCreateParams"]


class BulkCreateParams(TypedDict, total=False):
    country_code: Required[str]
    """ISO 3166-1 alpha-2 country code."""

    quantity: Required[int]
    """Number of accounts to purchase"""

    callback_url: str
    """URL to receive webhook notification when bulk archive is ready.

    POST request will be sent with `WebhookBulkReadyPayload`.

    **Retry policy.** If your endpoint does not return HTTP 200, webhook will be
    retried up to 3 times with delays: immediately, after 10 seconds, after 30
    seconds. Any non-200 response triggers retry.
    """
