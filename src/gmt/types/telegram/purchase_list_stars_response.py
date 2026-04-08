# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

__all__ = ["PurchaseListStarsResponse"]


class PurchaseListStarsResponse(BaseModel):
    id: float
    """The ID of the purchase"""

    amount: float
    """The amount of stars purchased"""

    created_at: str
    """The date and time when the purchase was made"""

    price: float
    """The price of the purchase"""

    username: str
    """The username of the recipient"""
