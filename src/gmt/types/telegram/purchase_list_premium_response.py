# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

__all__ = ["PurchaseListPremiumResponse"]


class PurchaseListPremiumResponse(BaseModel):
    id: float
    """The ID of the purchase"""

    created_at: str
    """The date and time when the purchase was made"""

    mounts: float
    """The number of months for the premium subscription"""

    price: float
    """The price of the purchase"""

    username: str
    """The username of the recipient"""
