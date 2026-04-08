# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["PurchaseCreatePremiumResponse"]


class PurchaseCreatePremiumResponse(BaseModel):
    mounts: float
    """The number of months for the premium subscription (3, 6, or 12)"""

    price: float
    """The price of the premium subscription"""

    status: Literal["success", "failure"]
    """The status of the purchase"""

    username: str
    """The username of the recipient"""
