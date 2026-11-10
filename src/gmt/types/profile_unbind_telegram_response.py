from .._models import BaseModel

__all__ = ["ProfileUnbindTelegramResponse"]


class ProfileUnbindTelegramResponse(BaseModel):
    success: bool
    """Indicates if the operation was successful"""
