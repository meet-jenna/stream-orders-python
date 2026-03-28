# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["ModifierGroup", "Rules"]


class Rules(BaseModel):
    amount_of_modifiers_free: Optional[float] = None

    maximum_unique_modifiers_allowed: Optional[float] = None

    minimum_unique_modifiers_allowed: Optional[float] = None

    selection_type: Optional[Literal["single", "single_proportion", "multiple"]] = None


class ModifierGroup(BaseModel):
    modifiers: List["Modifier"]

    name: str

    stream_id: str

    default_modifier_quantities: Optional[object] = None

    rules: Optional[Rules] = None


from .modifier import Modifier
