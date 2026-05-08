# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["ProfileRetrieveResponse", "Balance", "Discount", "Statistics"]


class Balance(BaseModel):
    amount: str
    """Monetary amount as a string with up to 2 decimal places."""

    currency_code: str
    """ISO 4217 currency code."""


class Discount(BaseModel):
    level: Literal["none", "bronze", "silver", "gold", "platinum", "premium"]
    """Current discount level: none, bronze, silver, gold, platinum, premium."""

    percent: float
    """Discount percentage."""


class Statistics(BaseModel):
    total_purchases: int
    """Total number of successful purchases."""


class ProfileRetrieveResponse(BaseModel):
    id: str
    """User Database ID"""

    balance: Balance

    created_at: str
    """Account creation time in ISO 8601 format (UTC)"""

    discount: Discount

    language: Optional[Literal["ru", "uk", "en", "es", "zh"]] = None
    """Preferred user interface language; null until the user selects one"""

    login: Optional[str] = None
    """Web username"""

    statistics: Statistics

    telegram_id: Optional[str] = None
    """User's Telegram ID (null for web-only users)"""

    telegram_username: Optional[str] = None
    """User's Telegram username"""
