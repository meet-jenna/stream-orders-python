# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["AddressParam"]


class AddressParam(TypedDict, total=False):
    address_line_1: Required[str]

    city: Required[str]

    country: Required[str]

    postal_code: Required[str]

    state: Required[str]

    address_line_2: str
