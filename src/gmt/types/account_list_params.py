from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["AccountListParams"]


class AccountListParams(TypedDict, total=False):
    page: int
    """Page number."""

    page_size: int
    """Number of items per page."""

    sort: Literal["price_asc", "price_desc", "name_asc", "name_desc", "popularity_asc", "popularity_desc"]
    """Sort order for accounts."""

    country_codes: str
    """Filter by country codes.

    Comma-separated list of ISO 3166-1 alpha-2 codes (e.g., 'US,RU,GB').
    """
