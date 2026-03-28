# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["V1RequestTokenResponse"]


class V1RequestTokenResponse(BaseModel):
    access_token: str

    expire_time: float
    """Access token expiration, set to UNIX epoch MS time of expiration"""

    refresh_token: str

    id: Optional[str] = None
    """
    Provider Account ID for the integration, used to maintain one set of tokens per
    login
    """

    refresh_token_expire_time: Optional[float] = None
    """Refresh token expiration, only use if refresh token rotation not supported"""
