from .._models import BaseModel

__all__ = ["ProfileChangeLanguageResponse"]


class ProfileChangeLanguageResponse(BaseModel):
    success: bool
    """Indicates if the operation was successful"""
