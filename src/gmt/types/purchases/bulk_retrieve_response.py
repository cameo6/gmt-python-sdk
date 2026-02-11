# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["BulkRetrieveResponse", "Item", "PricePerAccount", "TotalPrice"]


class Item(BaseModel):
    """Archive data (only populated when status is SUCCESS)"""

    archive_url: str
    """Path or URL to download the archive with accounts"""

    created_at: str
    """Bulk purchase creation timestamp"""

    export_id: str
    """Archive/export ID with sessions"""

    quantity: int
    """Number of accounts in the archive"""

    status: Literal["PENDING", "SUCCESS", "ERROR", "REFUND"]
    """Status of bulk purchase"""


class PricePerAccount(BaseModel):
    """Price of a single account"""

    amount: str
    """Monetary amount as a string with up to 2 decimal places."""

    currency_code: str
    """ISO 4217 currency code."""


class TotalPrice(BaseModel):
    """Total price for all accounts"""

    amount: str
    """Monetary amount as a string with up to 2 decimal places."""

    currency_code: str
    """ISO 4217 currency code."""


class BulkRetrieveResponse(BaseModel):
    bulk_purchase_id: int
    """Unique ID of the bulk purchase request"""

    country_code: str
    """ISO 3166-1 alpha-2 country code."""

    created_at: str
    """Bulk purchase creation timestamp"""

    item: Optional[Item] = None
    """Archive data (only populated when status is SUCCESS)"""

    price_per_account: PricePerAccount
    """Price of a single account"""

    quantity: int
    """Number of accounts in this purchase"""

    status: Literal["PENDING", "SUCCESS", "ERROR", "REFUND"]
    """Current status of bulk purchase"""

    total_price: TotalPrice
    """Total price for all accounts"""

    updated_at: str
    """Last update timestamp"""
