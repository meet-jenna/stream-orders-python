# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from ..._types import SequenceNotStr
from .object_update_param import ObjectUpdateParam

__all__ = [
    "V1NewEventParams",
    "DspLocationPauseEventDto",
    "DspLocationResumeEventDto",
    "DspLocationMenuEventDto",
    "DspLocationMenuUpdateEventDto",
    "DspLocationMenuUpdateEventDtoObjectUpdates",
    "DspLocationOrderAcceptedEventDto",
    "DspLocationOrderFailedEventDto",
    "DspLocationOrderFailedEventDtoFailureDetails",
    "DspLocationOrderUpdateEventDto",
    "DspLocationOrderCanceledEventDto",
]


class DspLocationPauseEventDto(TypedDict, total=False):
    location_id: Required[str]
    """The location ID that should be paused"""

    type: Required[str]
    """The type of event that this is."""

    until_ms: float
    """The time in milliseconds to pause until.

    If not specified, the location will be paused indefinitely.
    """


class DspLocationResumeEventDto(TypedDict, total=False):
    location_id: Required[str]
    """The location ID that should be resumed"""

    type: Required[str]
    """The type of event that this is."""


class DspLocationMenuEventDto(TypedDict, total=False):
    location_id: Required[str]
    """The location ID that this menu ingest applies to."""

    type: Required[str]
    """The type of event that this is."""

    download_url: str
    """
    This is an S3 URL pointing to a JSON file containing contents in the shape of
    DspLocationMenuEventDataDto.
    """


class DspLocationMenuUpdateEventDto(TypedDict, total=False):
    location_id: Required[str]
    """The location ID that this menu update event applies to."""

    object_updates: Required[DspLocationMenuUpdateEventDtoObjectUpdates]
    """Object updates to be applied across all menus"""

    type: Required[str]
    """The type of event that this is."""


class DspLocationMenuUpdateEventDtoObjectUpdates(TypedDict, total=False):
    """Object updates to be applied across all menus"""

    items: Required[Iterable[ObjectUpdateParam]]
    """Items with updates"""

    modifiers: Required[Iterable[ObjectUpdateParam]]
    """Modifiers with updates"""

    variations: Required[Iterable[ObjectUpdateParam]]
    """Variations with updates"""


class DspLocationOrderAcceptedEventDto(TypedDict, total=False):
    location_id: Required[str]
    """The location ID that this order is for."""

    type: Required[str]
    """The type of event that this is."""

    estimated_ready_at_ms: float
    """The estimated time in milliseconds that the order will be ready for pickup."""

    order_id: str
    """The order ID that this event is for."""


class DspLocationOrderFailedEventDto(TypedDict, total=False):
    location_id: Required[str]
    """The location ID that this order is for."""

    type: Required[str]
    """The type of event that this is."""

    failure_details: DspLocationOrderFailedEventDtoFailureDetails
    """Details related to the order failure."""

    failure_reason: Literal[
        "restaurant_not_accepting_orders",
        "location_not_found",
        "pos_missing_items",
        "items_unavailable",
        "order_validation_error",
        "unknown",
    ]
    """The reason for the order failure."""

    order_id: str
    """The order ID that this event is for."""


class DspLocationOrderFailedEventDtoFailureDetails(TypedDict, total=False):
    """Details related to the order failure."""

    invalid_item_ids: Required[SequenceNotStr[str]]
    """A list of item ids that caused the failure"""

    error_message: str
    """A message describing the error that occured"""


class DspLocationOrderUpdateEventDto(TypedDict, total=False):
    location_id: Required[str]
    """The location ID that this order is for."""

    type: Required[str]
    """The type of event that this is."""

    order_id: str
    """The order ID that this event is for."""

    order_status_update: Literal["ready_for_pickup", "completed"]
    """An updated status of the order."""


class DspLocationOrderCanceledEventDto(TypedDict, total=False):
    location_id: Required[str]
    """The location ID that this order is for."""

    type: Required[str]
    """The type of event that this is."""

    order_id: str
    """The order ID that this event is for."""


V1NewEventParams: TypeAlias = Union[
    DspLocationPauseEventDto,
    DspLocationResumeEventDto,
    DspLocationMenuEventDto,
    DspLocationMenuUpdateEventDto,
    DspLocationOrderAcceptedEventDto,
    DspLocationOrderFailedEventDto,
    DspLocationOrderUpdateEventDto,
    DspLocationOrderCanceledEventDto,
]
