# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["TelegramGetStarsPriceParams"]


class TelegramGetStarsPriceParams(TypedDict, total=False):
    amount: Required[str]
    """The amount of stars to purchase (50-10000)"""
