# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from . import stream_dsp
from .. import _compat
from .customer_param import CustomerParam as CustomerParam
from .order_submit_params import OrderSubmitParams as OrderSubmitParams
from .order_modifier_param import OrderModifierParam as OrderModifierParam

# Rebuild cyclical models only after all modules are imported.
# This ensures that, when building the deferred (due to cyclical references) model schema,
# Pydantic can resolve the necessary references.
# See: https://github.com/pydantic/pydantic/issues/11250 for more context.
if _compat.PYDANTIC_V1:
    stream_dsp.modifier.Modifier.update_forward_refs()  # type: ignore
    stream_dsp.modifier_group.ModifierGroup.update_forward_refs()  # type: ignore
else:
    stream_dsp.modifier.Modifier.model_rebuild(_parent_namespace_depth=0)
    stream_dsp.modifier_group.ModifierGroup.model_rebuild(_parent_namespace_depth=0)
