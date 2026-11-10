from .._models import BaseModel

__all__ = ["ProfileChangePasswordResponse"]


class ProfileChangePasswordResponse(BaseModel):
    success: bool
    """Indicates if the operation was successful"""
