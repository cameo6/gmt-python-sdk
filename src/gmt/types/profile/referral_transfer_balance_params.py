# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["ReferralTransferBalanceParams"]


class ReferralTransferBalanceParams(TypedDict, total=False):
    amount: Required[float]
    """Amount to transfer from referral balance"""
