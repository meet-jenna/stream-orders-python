# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Optional
from typing_extensions import Literal, TypeAlias

from .tax import Tax
from .image import Image
from .holiday import Holiday
from .schedule import Schedule
from ..._models import BaseModel
from .modifier_rules_v2 import ModifierRulesV2

__all__ = [
    "V1GetMenuFileURLResponse",
    "DspLocationMenuEventDataDto",
    "DspLocationMenuEventDataDtoMenu",
    "DspLocationMenuEventDataDtoMenuCategory",
    "DspLocationMenuEventDataDtoMenuCategoryItem",
    "DspLocationMenuEventDataDtoMenuCategoryItemVariation",
    "DspLocationMenuEventDataV2Dto",
    "DspLocationMenuEventDataV2DtoCategory",
    "DspLocationMenuEventDataV2DtoItemFamily",
    "DspLocationMenuEventDataV2DtoItem",
    "DspLocationMenuEventDataV2DtoItemMenuSpecificOverride",
    "DspLocationMenuEventDataV2DtoItemModifierOverride",
    "DspLocationMenuEventDataV2DtoMenu",
    "DspLocationMenuEventDataV2DtoModifierGroup",
    "DspLocationMenuEventDataV2DtoModifierGroupOverride",
    "DspLocationMenuEventDataV2DtoModifier",
]


class DspLocationMenuEventDataDtoMenuCategoryItemVariation(BaseModel):
    currency: str
    """
    We use lower-cased ISO 4127 alphabetic currency codes
    (https://www.iso.org/iso-4217-currency-codes.html)
    """

    name: str

    price: float
    """This will always be the lowest denomination. $1.50 USD = 150"""

    stream_id: str

    is_active: Optional[bool] = None

    sku: Optional[str] = None

    stock_count: Optional[float] = None

    upc: Optional[str] = None


class DspLocationMenuEventDataDtoMenuCategoryItem(BaseModel):
    modifier_groups: List["ModifierGroup"]

    name: str

    stream_id: str

    tax_ids: List[str]
    """Contains item level tax rate assignments (References `taxes` objects)"""

    variations: List[DspLocationMenuEventDataDtoMenuCategoryItemVariation]

    allergens: Optional[
        List[
            Literal[
                "eggs",
                "soybeans",
                "dairy",
                "sesame",
                "lupin",
                "celery",
                "mustard",
                "gluten",
                "wheat",
                "rye",
                "barley",
                "oats",
                "spelt",
                "kamut",
                "shellfish",
                "crustaceans",
                "molluscs",
                "fish",
                "almonds",
                "hazelnuts",
                "walnuts",
                "cashews",
                "pecan",
                "brazil",
                "pistachio",
                "macadamia",
                "peanuts",
                "tree_nuts",
                "sulphur_dioxide_sulphites",
            ]
        ]
    ] = None

    default_item_id: Optional[str] = None
    """The stream_id of the default variation for this item.

    Only set if a default variation is configured.
    """

    description: Optional[str] = None

    images: Optional[List[Image]] = None

    is_active: Optional[bool] = None

    is_alcohol: Optional[bool] = None
    """Provided when item is marked as Alcoholic and needs age verification"""


class DspLocationMenuEventDataDtoMenuCategory(BaseModel):
    items: List[DspLocationMenuEventDataDtoMenuCategoryItem]

    name: str

    stream_id: str

    description: Optional[str] = None


class DspLocationMenuEventDataDtoMenu(BaseModel):
    categories: List[DspLocationMenuEventDataDtoMenuCategory]

    name: str

    schedule: Schedule
    """Schedule for menu in store timezone, using 24-hour format (HH:mm-HH:mm)"""

    stream_id: str


class DspLocationMenuEventDataDto(BaseModel):
    holidays: List[Holiday]

    menus: List[DspLocationMenuEventDataDtoMenu]

    prep_time_minutes: float
    """
    Estimated prep time for the store used for display purposes,
    location.order.accept will contain order level estimated fulfillment time.
    """

    taxes: List[Tax]
    """Tax rates assigned to objects across the menu"""


class DspLocationMenuEventDataV2DtoCategory(BaseModel):
    item_family_ids: List[str]

    name: str

    stream_id: str

    description: Optional[str] = None


class DspLocationMenuEventDataV2DtoItemFamily(BaseModel):
    item_ids: List[str]

    modifier_group_ids: List[str]

    name: str

    stream_id: str

    tax_ids: List[str]

    allergens: Optional[
        List[
            Literal[
                "eggs",
                "soybeans",
                "dairy",
                "sesame",
                "lupin",
                "celery",
                "mustard",
                "gluten",
                "wheat",
                "rye",
                "barley",
                "oats",
                "spelt",
                "kamut",
                "shellfish",
                "crustaceans",
                "molluscs",
                "fish",
                "almonds",
                "hazelnuts",
                "walnuts",
                "cashews",
                "pecan",
                "brazil",
                "pistachio",
                "macadamia",
                "peanuts",
                "tree_nuts",
                "sulphur_dioxide_sulphites",
            ]
        ]
    ] = None

    default_item_id: Optional[str] = None

    description: Optional[str] = None

    images: Optional[Image] = None
    """
    @important Shoulve been an array, but committed as a single image (keep as image
    to maintain compatibility)
    """

    is_alcohol: Optional[bool] = None


class DspLocationMenuEventDataV2DtoItemMenuSpecificOverride(BaseModel):
    menu_id: str
    """which menu is this override valid for"""

    price_amount: float

    is_active: Optional[bool] = None


class DspLocationMenuEventDataV2DtoItemModifierOverride(BaseModel):
    modifier_id: str

    price_amount: float
    """cents"""


class DspLocationMenuEventDataV2DtoItem(BaseModel):
    currency: str
    """
    We use lower-cased ISO 4127 alphabetic currency codes
    (https://www.iso.org/iso-4217-currency-codes.html)
    """

    name: str

    price: float
    """This will always be the lowest denomination. $1.50 USD = 150"""

    stream_id: str

    is_active: Optional[bool] = None

    menu_specific_overrides: Optional[List[DspLocationMenuEventDataV2DtoItemMenuSpecificOverride]] = None

    modifier_overrides: Optional[List[DspLocationMenuEventDataV2DtoItemModifierOverride]] = None
    """for size specific modifier pricing"""

    sku: Optional[str] = None

    stock_count: Optional[float] = None

    upc: Optional[str] = None


class DspLocationMenuEventDataV2DtoMenu(BaseModel):
    category_ids: List[str]

    name: str

    schedule: Schedule

    stream_id: str


class DspLocationMenuEventDataV2DtoModifierGroupOverride(BaseModel):
    override_rules: ModifierRulesV2

    parent_id: str
    """can be a modifier or item family"""

    parent_type: object


class DspLocationMenuEventDataV2DtoModifierGroup(BaseModel):
    modifier_ids: List[str]

    name: str

    stream_id: str

    overrides: Optional[List[DspLocationMenuEventDataV2DtoModifierGroupOverride]] = None
    """
    If a parent item or modifier is referenced by the override, the rules of the
    override have precedence over the rules of this modifier group.
    """

    rules: Optional[ModifierRulesV2] = None


class DspLocationMenuEventDataV2DtoModifier(BaseModel):
    currency: str

    name: str

    price: float

    stream_id: str

    images: Optional[List[Image]] = None

    is_active: Optional[bool] = None

    nested_modifier_group_ids: Optional[List[str]] = None


class DspLocationMenuEventDataV2Dto(BaseModel):
    categories: List[DspLocationMenuEventDataV2DtoCategory]
    """contains all categories"""

    holidays: List[Holiday]

    item_families: List[DspLocationMenuEventDataV2DtoItemFamily]
    """contains all item families"""

    items: List[DspLocationMenuEventDataV2DtoItem]
    """Keepiung sepcific to the for now for a more stream adjacent approach."""

    menus: List[DspLocationMenuEventDataV2DtoMenu]

    modifier_groups: List[DspLocationMenuEventDataV2DtoModifierGroup]
    """contains all mod groups"""

    modifiers: List[DspLocationMenuEventDataV2DtoModifier]

    prep_time_minutes: float
    """
    Estimated prep time for the store used for display purposes,
    location.order.accept will contain order level estimated fulfillment time.
    """

    taxes: List[Tax]


V1GetMenuFileURLResponse: TypeAlias = Union[DspLocationMenuEventDataDto, DspLocationMenuEventDataV2Dto]

from .modifier_group import ModifierGroup
