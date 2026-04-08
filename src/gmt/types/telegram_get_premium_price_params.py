# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["TelegramGetPremiumPriceParams"]


class TelegramGetPremiumPriceParams(TypedDict, total=False):
    mounts: Required[str]
    """The number of months for the premium subscription (3, 6, or 12)"""
