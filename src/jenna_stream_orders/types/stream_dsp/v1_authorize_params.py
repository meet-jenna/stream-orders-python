# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["V1AuthorizeParams"]


class V1AuthorizeParams(TypedDict, total=False):
    client_id: Required[str]

    redirect_uri: Required[str]

    response_type: Required[Literal["code"]]
