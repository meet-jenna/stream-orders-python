# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from .customer_param import CustomerParam
from .stream_dsp.v1.address_param import AddressParam

__all__ = [
    "OrderSubmitParams",
    "StreamWebhookNewOrderEvent",
    "StreamWebhookNewOrderEventOrder",
    "StreamWebhookNewOrderEventOrderItem",
    "StreamWebhookNewOrderEventOrderDiscount",
    "StreamWebhookCancelOrderEvent",
    "StreamWebhookStoreStatusUpdateEvent",
    "StreamWebhookStoreStatusUpdateEventStatusUpdate",
    "StreamWebhookDeliveryStatusUpdateEvent",
    "StreamWebhookDeliveryStatusUpdateEventDriverDetails",
    "StreamWebhookDeliveryStatusUpdateEventDriverDetailsPhone",
    "StreamWebhookDeliveryStatusUpdateEventDriverDetailsVehicleInfo",
]


class StreamWebhookNewOrderEvent(TypedDict, total=False):
    location_id: Required[str]
    """The ID of the location that this event is for."""

    order: Required[StreamWebhookNewOrderEventOrder]
    """A new order. This property should only exist if this is a new order event."""

    type: Required[str]


class StreamWebhookNewOrderEventOrderItem(TypedDict, total=False):
    id: Required[str]
    """The ID of the **variation** on Stream (not the Item ID)"""

    currency: Required[str]
    """
    We use lower-cased
    [ISO 4127 alphabetic currency codes](https://www.iso.org/iso-4217-currency-codes.html)
    """

    modifiers: Required[Iterable["OrderModifierParam"]]
    """The modifiers that the customer selected for this item."""

    name: Required[str]

    price: Required[float]
    """The price of the item in cents"""

    quantity: Required[float]

    category_id: str
    """The ID of the item's **Category** on Stream"""

    customer_id: str
    """Assignee of this item within a group order, must map to one of `customers.id`.

    Can be ommited if customer has a single customer.
    """

    item_id: str
    """The Parent ID of the **Item** on Stream"""

    special_instructions: str
    """Item level special instructions, i.e customer modifications"""


class StreamWebhookNewOrderEventOrderDiscount(TypedDict, total=False):
    id: Required[str]
    """The ID of the discount applied to the order"""

    amount: Required[float]
    """The amount of the discount in cents"""

    item_id: str
    """
    If the item is an item-level discount, this is the `id` of the item from the
    `items` list that the discount applies to.
    """


class StreamWebhookNewOrderEventOrder(TypedDict, total=False):
    """A new order. This property should only exist if this is a new order event."""

    id: Required[str]
    """The ID of the order in your system."""

    customer_facing_id: Required[str]
    """
    This is usually a shortened ID for the customer or merchant to troubleshoot
    their order
    """

    customers: Required[Iterable[CustomerParam]]
    """The customers for this order.

    If there is a single customer, this would be an array with a single element
    """

    fulfillment_type: Required[
        Literal[
            "curbside",
            "delivery",
            "dine_in",
            "merchant_managed_delivery",
            "pickup",
            "stream_managed_delivery",
            "drive_thru",
            "kiosk",
        ]
    ]
    """The fulfillment type of the order."""

    items: Required[Iterable[StreamWebhookNewOrderEventOrderItem]]
    """The items that the customer ordered."""

    subtotal: Required[float]
    """The subtotal of the order in cents (excluding taxes)."""

    tax: Required[float]
    """The tax amount of the order in cents."""

    tax_withheld: Required[float]
    """
    If the DSP withholds tax on behalf of the merchant they should send the amount
    here
    """

    brand: str
    """Allows for a brand to be specified for the order.

    If not provided, the partner slug will be used.
    """

    customer: CustomerParam
    """Deprecated, use `customers` instead"""

    delivery_address: AddressParam
    """
    Required when fulfillment_type is "merchant_managed_delivery" or
    "stream_managed_delivery"
    """

    delivery_fee: float
    """The delivery fee of the order in cents, only on merchant_managed_delivery"""

    delivery_fee_taxes: float
    """
    The tax amount applicable to the delivery fee in cents, only on
    merchant_managed_delivery
    """

    discounts: Iterable[StreamWebhookNewOrderEventOrderDiscount]
    """A list of discounts that should be applied to the order. Optional"""

    driver_tip: float
    """
    Tip amount that should be provided to the driver, only on
    merchant_managed_delivery
    """

    estimated_ready_at_ms: float
    """
    If you have an estimate of when the order will be ready for pickup, provide it
    here in epoch milliseconds. If omitted or an invalid epoch time is passed, this
    will default to 30 min added to the time of the order
    """

    fulfillment_instructions: str
    """Driver level fulfillment instructions"""

    is_future_order: bool
    """Set to `true` when the order is not to be prepared ASAP."""

    service_charge: float
    """Miscellaneous charge that is not taxes or tips. Ex: card fee"""

    should_include_utensils: bool
    """Indicates if utensils and napkins are required to be included with the order.

    If not provided, this will default to true.
    """

    special_instructions: str
    """Order level special instructions"""

    status: Literal["scheduled"]
    """The incoming status of the order. Scheduled will queue the order on our end."""

    store_tip: float
    """Tip amount that should be provided to the store, only on pickup or dine_in"""

    unpaid: bool
    """Describes the payment state of the order.

    May only be true for drive_thru orders.
    """


class StreamWebhookCancelOrderEvent(TypedDict, total=False):
    location_id: Required[str]
    """The ID of the location that this event is for."""

    order_id: Required[str]
    """A canceled Order ID.

    This property should only exist if this is a cancel order event.
    """

    type: Required[str]

    cancel_reason: Literal[
        "customer_requested",
        "customer_no_show",
        "customer_changed_mind",
        "merchant_requested",
        "item_out_of_stock",
        "store_closed",
        "kitchen_too_busy",
        "menu_issue",
        "driver_unavailable",
        "delivery_address_issue",
        "delivery_failed",
        "pos_rejected",
        "pos_error",
        "payment_failed",
        "duplicate_order",
        "order_validation_failed",
        "fraud_suspected",
        "weather_conditions",
        "other",
        "unknown",
        "reason_not_provided",
    ]
    """The reason for the cancelation.

    Can be a free-text string or one of the normalized values: customer_requested,
    customer_no_show, item_out_of_stock, store_closed, store_too_busy,
    driver_unavailable, delivery_failed, pos_rejected, payment_failed,
    duplicate_order, other.
    """

    cancel_source: Literal["customer", "restaurant", "driver", "dsp", "stream", "unknown"]
    """Who initiated the cancelation.

    Accepted values: customer, restaurant, driver, dsp.
    """


class StreamWebhookStoreStatusUpdateEvent(TypedDict, total=False):
    location_id: Required[str]
    """The ID of the location that this event is for."""

    status_update: Required[StreamWebhookStoreStatusUpdateEventStatusUpdate]
    """Status update for the given location"""

    type: Required[str]


class StreamWebhookStoreStatusUpdateEventStatusUpdate(TypedDict, total=False):
    """Status update for the given location"""

    status: Required[Literal["online", "paused"]]
    """The new status for the location"""

    end_time: float
    """When this status will stop applying.

    Optional, if ommited, assumed to be indefinite. Timestamp as milliseconds since
    epoch
    """

    start_time: float
    """When this status started applying.

    Optional. Timestamp as milliseconds since epoch
    """


class StreamWebhookDeliveryStatusUpdateEvent(TypedDict, total=False):
    delivery_status: Required[
        Literal[
            "pending",
            "pending_driver_confirmation",
            "enroute_to_pickup",
            "arrived_at_pickup",
            "enroute_to_dropoff",
            "arrived_at_dropoff",
            "completed",
            "failed_to_assign_driver",
            "failed_to_deliver",
            "failed_to_pickup",
            "failed",
            "merchant_canceled",
            "enroute_to_return",
            "arrived_at_return",
            "returned",
        ]
    ]
    """The delivery status for the given order"""

    location_id: Required[str]
    """The DSP Location ID that this event is for."""

    order_id: Required[str]
    """The DSP Order ID that this event is for."""

    type: Required[str]

    driver_details: StreamWebhookDeliveryStatusUpdateEventDriverDetails
    """The driver details for the given order"""


class StreamWebhookDeliveryStatusUpdateEventDriverDetailsPhone(TypedDict, total=False):
    code: str

    number: str


class StreamWebhookDeliveryStatusUpdateEventDriverDetailsVehicleInfo(TypedDict, total=False):
    color: str

    is_autonomous: bool

    license_plate: str

    make: str

    model: str


class StreamWebhookDeliveryStatusUpdateEventDriverDetails(TypedDict, total=False):
    """The driver details for the given order"""

    name: Required[str]

    phone: Required[StreamWebhookDeliveryStatusUpdateEventDriverDetailsPhone]

    source: Required[str]

    vehicle_info: Required[StreamWebhookDeliveryStatusUpdateEventDriverDetailsVehicleInfo]

    handoff_instructions: str
    """Instructions for the merchant to handoff the order to the driver"""

    passcode: str
    """Passcode for the merchant to authorize the driver / robot"""

    picture_url: str


OrderSubmitParams: TypeAlias = Union[
    StreamWebhookNewOrderEvent,
    StreamWebhookCancelOrderEvent,
    StreamWebhookStoreStatusUpdateEvent,
    StreamWebhookDeliveryStatusUpdateEvent,
]

from .order_modifier_param import OrderModifierParam
