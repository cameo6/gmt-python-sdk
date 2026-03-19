# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ...._models import BaseModel

__all__ = ["TransactionListResponse", "Amount", "BalanceAfter", "BalanceBefore"]


class Amount(BaseModel):
    amount: str
    """Monetary amount as a string with up to 2 decimal places."""

    currency_code: str
    """ISO 4217 currency code."""


class BalanceAfter(BaseModel):
    amount: str
    """Monetary amount as a string with up to 2 decimal places."""

    currency_code: str
    """ISO 4217 currency code."""


class BalanceBefore(BaseModel):
    amount: str
    """Monetary amount as a string with up to 2 decimal places."""

    currency_code: str
    """ISO 4217 currency code."""


class TransactionListResponse(BaseModel):
    id: int

    amount: Amount

    balance_after: BalanceAfter

    balance_before: BalanceBefore

    created_at: str

    from_user_id: Optional[str] = None
