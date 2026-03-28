# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ...._models import BaseModel

__all__ = ["Address"]


class Address(BaseModel):
    address_line_1: str

    city: str

    country: str

    postal_code: str

    state: str

    address_line_2: Optional[str] = None
