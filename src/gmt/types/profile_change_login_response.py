from .._models import BaseModel

__all__ = ["ProfileChangeLoginResponse"]


class ProfileChangeLoginResponse(BaseModel):
    success: bool
    """Indicates if the operation was successful"""
