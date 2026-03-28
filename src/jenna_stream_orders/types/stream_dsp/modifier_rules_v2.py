# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["ModifierRulesV2"]


class ModifierRulesV2(BaseModel):
    amount_of_modifiers_free: Optional[float] = None

    default_modifier_quantities: Optional[object] = None

    maximum_unique_modifiers_allowed: Optional[float] = None

    minimum_unique_modifiers_allowed: Optional[float] = None

    selection_type: Optional[Literal["single", "single_proportion", "multiple"]] = None
