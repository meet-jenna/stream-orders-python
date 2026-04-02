# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

__all__ = ["OrderModifierParam"]


class OrderModifierParam(TypedDict, total=False):
    id: Required[str]
    """The ID of the modifier on Stream"""

    currency: Required[str]
    """
    We use lower-cased ISO 4127 alphabetic currency codes
    (https://www.iso.org/iso-4217-currency-codes.html)
    """

    modifiers: Required[Iterable["OrderModifierParam"]]
    """Nested modifier selections"""

    name: Required[str]

    price: Required[float]
    """The price of the modifier in cents"""

    quantity: Required[float]

    modifier_group_id: str
    """The Parent Group ID of the modifier on Stream"""
