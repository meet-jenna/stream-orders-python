# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel

__all__ = ["Schedule"]


class Schedule(BaseModel):
    friday: List[str]

    monday: List[str]

    saturday: List[str]

    sunday: List[str]

    thursday: List[str]

    tuesday: List[str]

    wednesday: List[str]
