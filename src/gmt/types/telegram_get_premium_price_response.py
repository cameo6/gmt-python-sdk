# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["TelegramGetPremiumPriceResponse"]


class TelegramGetPremiumPriceResponse(BaseModel):
    mounts: float
    """The number of months for the premium subscription (3, 6, or 12)"""

    price: float
    """The price of the premium subscription"""
