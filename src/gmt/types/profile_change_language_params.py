from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["ProfileChangeLanguageParams"]


class ProfileChangeLanguageParams(TypedDict, total=False):
    language: Required[Literal["ru", "uk", "en", "es", "zh"]]
    """Preferred user interface language"""
