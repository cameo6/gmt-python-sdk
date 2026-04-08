# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["PurchaseCreateStarsParams"]


class PurchaseCreateStarsParams(TypedDict, total=False):
    amount: Required[float]
    """The amount of stars to purchase (50-10000)"""

    username: Required[str]
    """Recipient Telegram username (@optional, 5-32 chars)"""
