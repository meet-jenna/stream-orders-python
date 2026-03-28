# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Required, TypeAlias, TypedDict

__all__ = ["V1RequestTokenParams", "ExchangeTokenDto", "RefreshTokenDto"]


class ExchangeTokenDto(TypedDict, total=False):
    client_id: Required[str]
    """The client ID to be provided to Stream for identifying us."""

    client_secret: Required[str]
    """The client secret to be provided to Stream for security."""

    code: Required[str]
    """The authorization code received from successful authorization."""

    grant_type: Required[str]


class RefreshTokenDto(TypedDict, total=False):
    client_id: Required[str]
    """The client ID to be provided to Stream for identifying us."""

    client_secret: Required[str]
    """The client secret to be provided to Stream for security."""

    grant_type: Required[str]

    refresh_token: Required[str]
    """The refresh token from the existing session for refresh"""


V1RequestTokenParams: TypeAlias = Union[ExchangeTokenDto, RefreshTokenDto]
