# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["PurchaseCreatePremiumParams"]


class PurchaseCreatePremiumParams(TypedDict, total=False):
    mounts: Required[float]
    """The number of months for the premium subscription (3, 6, or 12)"""

    username: Required[str]
    """Recipient Telegram username (@optional, 5-32 chars)"""
