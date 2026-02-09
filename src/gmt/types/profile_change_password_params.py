# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["ProfileChangePasswordParams"]


class ProfileChangePasswordParams(TypedDict, total=False):
    new_password: Required[str]
    """User password.

    Must contain at least two character types: lowercase, uppercase, digits, or
    special characters
    """
