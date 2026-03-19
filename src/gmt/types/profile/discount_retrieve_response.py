# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel

__all__ = [
    "DiscountRetrieveResponse",
    "CurrentLevel",
    "CustomDiscount",
    "Level",
    "NextLevel",
    "NextLevelProgress",
    "NextLevelRequirements",
]


class CurrentLevel(BaseModel):
    name: str
    """Name of the discount level"""

    percent: float
    """Discount percentage"""

    purchases_required: int
    """Required number of purchases to reach this level"""


class CustomDiscount(BaseModel):
    id: int
    """Custom discount rule ID"""

    country_code: Optional[str] = None
    """ISO 3166-1 alpha-2 country code. If null, applies to all countries"""

    created_at: str
    """Creation date in ISO 8601 format (UTC)"""

    discount_percent: float
    """Discount percentage"""

    expires_at: Optional[str] = None
    """Expiration date in ISO 8601 format (UTC). If null, never expires"""


class Level(BaseModel):
    name: str
    """Name of the discount level"""

    percent: float
    """Discount percentage"""

    purchases: int
    """Required purchases to reach this level"""


class NextLevelProgress(BaseModel):
    purchases: int
    """Current number of purchases"""

    purchases_remaining: int
    """Remaining purchases to reach the next level"""


class NextLevelRequirements(BaseModel):
    purchases: int
    """Required number of purchases to reach this level"""


class NextLevel(BaseModel):
    """Next level information. Null if already at max level"""

    name: str
    """Name of the next discount level"""

    percent: float
    """Discount percentage for the next level"""

    progress: NextLevelProgress

    requirements: NextLevelRequirements


class DiscountRetrieveResponse(BaseModel):
    current_level: CurrentLevel

    custom_discounts: List[CustomDiscount]
    """Personal discount rules."""

    levels: List[Level]
    """All available discount levels"""

    next_level: Optional[NextLevel] = None
    """Next level information. Null if already at max level"""
