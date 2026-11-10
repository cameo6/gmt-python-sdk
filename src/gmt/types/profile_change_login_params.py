from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["ProfileChangeLoginParams"]


class ProfileChangeLoginParams(TypedDict, total=False):
    new_login: Required[str]
    """User login for registration"""
