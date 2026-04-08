# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["PurchaseCreateStarsResponse"]


class PurchaseCreateStarsResponse(BaseModel):
    amount: float
    """The amount of stars to purchase (50-10000)"""

    price: float
    """The price of the stars"""

    status: Literal["success", "failure"]
    """The status of the purchase"""

    username: str
    """The username of the recipient"""
