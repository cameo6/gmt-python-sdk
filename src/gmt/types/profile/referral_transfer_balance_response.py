# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

__all__ = ["ReferralTransferBalanceResponse", "Balance", "ReferralInfo", "ReferralInfoBalance", "ReferralInfoProfit"]


class Balance(BaseModel):
    amount: str
    """Monetary amount as a string with up to 2 decimal places."""

    currency_code: str
    """ISO 4217 currency code."""


class ReferralInfoBalance(BaseModel):
    """Current referral balance"""

    amount: str
    """Monetary amount as a string with up to 2 decimal places."""

    currency_code: str
    """ISO 4217 currency code."""


class ReferralInfoProfit(BaseModel):
    """Total lifetime referral earnings"""

    amount: str
    """Monetary amount as a string with up to 2 decimal places."""

    currency_code: str
    """ISO 4217 currency code."""


class ReferralInfo(BaseModel):
    balance: ReferralInfoBalance
    """Current referral balance"""

    profit: ReferralInfoProfit
    """Total lifetime referral earnings"""

    referrals_count: int
    """Total number of referrals"""


class ReferralTransferBalanceResponse(BaseModel):
    balance: Balance

    referral_info: ReferralInfo
