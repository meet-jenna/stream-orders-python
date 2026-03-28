# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional

from .image import Image
from ..._models import BaseModel

__all__ = ["Modifier"]


class Modifier(BaseModel):
    currency: str
    """
    We use lower-cased ISO 4127 alphabetic currency codes
    (https://www.iso.org/iso-4217-currency-codes.html)
    """

    name: str

    nested_modifier_groups: List["ModifierGroup"]

    price: float
    """This will always be the lowest denomination. $1.50 USD = 150"""

    stream_id: str

    images: Optional[List[Image]] = None

    is_active: Optional[bool] = None


from .modifier_group import ModifierGroup
