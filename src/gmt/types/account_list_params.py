# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Literal, Required, TypedDict

from .._types import SequenceNotStr

__all__ = ["AccountListParams"]


class AccountListParams(TypedDict, total=False):
    page: Required[int]
    """Page number (starts from 1)."""

    page_size: Required[int]
    """Number of items per page (max 50)."""

    sort: Required[Literal["price_asc", "price_desc", "name_asc", "name_desc"]]
    """Sort order for accounts."""

    country_code: Union[str, SequenceNotStr[str]]
    """Filter by country codes (comma-separated, e.g., 'US,RU,GB')."""
