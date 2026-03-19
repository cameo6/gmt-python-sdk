# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel

__all__ = [
    "ReferralRetrieveResponse",
    "CurrentLevel",
    "CurrentLevelProgress",
    "Level",
    "NextLevel",
    "NextLevelRequirements",
    "ReferralInfo",
    "ReferralInfoBalance",
    "ReferralInfoProfit",
]


class CurrentLevelProgress(BaseModel):
    deposits: float
    """Total deposits from referrals (in USD)"""

    referrals: int
    """Number of active referrals"""


class CurrentLevel(BaseModel):
    name: str
    """Name of the current referral level"""

    percent: float
    """Commission percentage"""

    progress: CurrentLevelProgress


class Level(BaseModel):
    name: str
    """Name of the referral level"""

    percent: float
    """Commission percentage"""

    required_deposits: float
    """Required deposits to reach this level"""

    required_referrals: int
    """Required referrals to reach this level"""


class NextLevelRequirements(BaseModel):
    deposits: float
    """Required total deposits from referrals"""

    referrals: int
    """Required number of referrals"""

    remaining_deposits: float
    """Remaining deposits to reach the next level"""

    remaining_referrals: int
    """Remaining referrals to reach the next level"""


class NextLevel(BaseModel):
    """Next level information. Null if already at max level"""

    name: str
    """Name of the next referral level"""

    percent: float
    """Commission percentage for the next level"""

    requirements: NextLevelRequirements


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


class ReferralRetrieveResponse(BaseModel):
    current_level: CurrentLevel

    levels: List[Level]
    """All available referral levels"""

    next_level: Optional[NextLevel] = None
    """Next level information. Null if already at max level"""

    referral_info: ReferralInfo

    referral_link: str
    """User's referral link"""
