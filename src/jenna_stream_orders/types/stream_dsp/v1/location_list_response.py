# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .address import Address
from ...._models import BaseModel

__all__ = ["LocationListResponse", "Location"]


class Location(BaseModel):
    address: Address

    name: str
    """The name of the location in your system."""

    provider_id: str
    """The ID of the location in your system."""


class LocationListResponse(BaseModel):
    locations: List[Location]
