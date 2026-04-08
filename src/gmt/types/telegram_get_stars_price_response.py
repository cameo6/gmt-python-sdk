# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["TelegramGetStarsPriceResponse"]


class TelegramGetStarsPriceResponse(BaseModel):
    amount: float
    """The amount of stars to purchase (50-10000)"""

    price: float
    """The price of the stars"""
