# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["Tax"]


class Tax(BaseModel):
    name: str

    rate: float

    stream_id: str

    is_default: Optional[bool] = None

    is_inclusive: Optional[bool] = None
    """Determines if the tax amount is already included in the item price"""
