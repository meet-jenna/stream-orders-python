# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, overload

import httpx

from ..types import order_submit_params
from .._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
from .._utils import path_template, required_args, maybe_transform, strip_not_given, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options

__all__ = ["OrderResource", "AsyncOrderResource"]


class OrderResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> OrderResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/meet-jenna/stream-orders-python#accessing-raw-response-data-eg-headers
        """
        return OrderResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> OrderResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/meet-jenna/stream-orders-python#with_streaming_response
        """
        return OrderResourceWithStreamingResponse(self)

    @overload
    def submit(
        self,
        partner_id: str,
        *,
        location_id: str,
        order: order_submit_params.StreamWebhookNewOrderEventOrder,
        type: str,
        stream_webhook_signature: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """You will have to call this endpoint from your system.

        This is how you will
        notify Stream about events that happen in your system.

        Args:
          location_id: The ID of the location that this event is for.

          order: A new order. This property should only exist if this is a new order event.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def submit(
        self,
        partner_id: str,
        *,
        location_id: str,
        order_id: str,
        type: str,
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
        | Omit = omit,
        cancel_source: Literal["customer", "restaurant", "driver", "dsp", "stream", "unknown"] | Omit = omit,
        stream_webhook_signature: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """You will have to call this endpoint from your system.

        This is how you will
        notify Stream about events that happen in your system.

        Args:
          location_id: The ID of the location that this event is for.

          order_id: A canceled Order ID. This property should only exist if this is a cancel order
              event.

          cancel_reason: The reason for the cancelation. Can be a free-text string or one of the
              normalized values: customer_requested, customer_no_show, item_out_of_stock,
              store_closed, store_too_busy, driver_unavailable, delivery_failed, pos_rejected,
              payment_failed, duplicate_order, other.

          cancel_source: Who initiated the cancelation. Accepted values: customer, restaurant, driver,
              dsp.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def submit(
        self,
        partner_id: str,
        *,
        location_id: str,
        status_update: order_submit_params.StreamWebhookStoreStatusUpdateEventStatusUpdate,
        type: str,
        stream_webhook_signature: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """You will have to call this endpoint from your system.

        This is how you will
        notify Stream about events that happen in your system.

        Args:
          location_id: The ID of the location that this event is for.

          status_update: Status update for the given location

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def submit(
        self,
        partner_id: str,
        *,
        delivery_status: Literal[
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
        ],
        location_id: str,
        order_id: str,
        type: str,
        driver_details: order_submit_params.StreamWebhookDeliveryStatusUpdateEventDriverDetails | Omit = omit,
        stream_webhook_signature: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """You will have to call this endpoint from your system.

        This is how you will
        notify Stream about events that happen in your system.

        Args:
          delivery_status: The delivery status for the given order

          location_id: The DSP Location ID that this event is for.

          order_id: The DSP Order ID that this event is for.

          driver_details: The driver details for the given order

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(
        ["location_id", "order", "type"],
        ["location_id", "order_id", "type"],
        ["location_id", "status_update", "type"],
        ["delivery_status", "location_id", "order_id", "type"],
    )
    def submit(
        self,
        partner_id: str,
        *,
        location_id: str,
        order: order_submit_params.StreamWebhookNewOrderEventOrder | Omit = omit,
        type: str,
        stream_webhook_signature: str | Omit = omit,
        order_id: str | Omit = omit,
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
        | Omit = omit,
        cancel_source: Literal["customer", "restaurant", "driver", "dsp", "stream", "unknown"] | Omit = omit,
        status_update: order_submit_params.StreamWebhookStoreStatusUpdateEventStatusUpdate | Omit = omit,
        delivery_status: Literal[
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
        | Omit = omit,
        driver_details: order_submit_params.StreamWebhookDeliveryStatusUpdateEventDriverDetails | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        if not partner_id:
            raise ValueError(f"Expected a non-empty value for `partner_id` but received {partner_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        extra_headers = {
            **strip_not_given({"Stream-Webhook-Signature": stream_webhook_signature}),
            **(extra_headers or {}),
        }
        return self._post(
            ("https://dev-unstable-orders.hookedapi.com" if not self._client._base_url_overridden else "")
            + path_template("/order/{partner_id}", partner_id=partner_id),
            body=maybe_transform(
                {
                    "location_id": location_id,
                    "order": order,
                    "type": type,
                    "order_id": order_id,
                    "cancel_reason": cancel_reason,
                    "cancel_source": cancel_source,
                    "status_update": status_update,
                    "delivery_status": delivery_status,
                    "driver_details": driver_details,
                },
                order_submit_params.OrderSubmitParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncOrderResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncOrderResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/meet-jenna/stream-orders-python#accessing-raw-response-data-eg-headers
        """
        return AsyncOrderResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncOrderResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/meet-jenna/stream-orders-python#with_streaming_response
        """
        return AsyncOrderResourceWithStreamingResponse(self)

    @overload
    async def submit(
        self,
        partner_id: str,
        *,
        location_id: str,
        order: order_submit_params.StreamWebhookNewOrderEventOrder,
        type: str,
        stream_webhook_signature: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """You will have to call this endpoint from your system.

        This is how you will
        notify Stream about events that happen in your system.

        Args:
          location_id: The ID of the location that this event is for.

          order: A new order. This property should only exist if this is a new order event.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def submit(
        self,
        partner_id: str,
        *,
        location_id: str,
        order_id: str,
        type: str,
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
        | Omit = omit,
        cancel_source: Literal["customer", "restaurant", "driver", "dsp", "stream", "unknown"] | Omit = omit,
        stream_webhook_signature: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """You will have to call this endpoint from your system.

        This is how you will
        notify Stream about events that happen in your system.

        Args:
          location_id: The ID of the location that this event is for.

          order_id: A canceled Order ID. This property should only exist if this is a cancel order
              event.

          cancel_reason: The reason for the cancelation. Can be a free-text string or one of the
              normalized values: customer_requested, customer_no_show, item_out_of_stock,
              store_closed, store_too_busy, driver_unavailable, delivery_failed, pos_rejected,
              payment_failed, duplicate_order, other.

          cancel_source: Who initiated the cancelation. Accepted values: customer, restaurant, driver,
              dsp.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def submit(
        self,
        partner_id: str,
        *,
        location_id: str,
        status_update: order_submit_params.StreamWebhookStoreStatusUpdateEventStatusUpdate,
        type: str,
        stream_webhook_signature: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """You will have to call this endpoint from your system.

        This is how you will
        notify Stream about events that happen in your system.

        Args:
          location_id: The ID of the location that this event is for.

          status_update: Status update for the given location

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def submit(
        self,
        partner_id: str,
        *,
        delivery_status: Literal[
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
        ],
        location_id: str,
        order_id: str,
        type: str,
        driver_details: order_submit_params.StreamWebhookDeliveryStatusUpdateEventDriverDetails | Omit = omit,
        stream_webhook_signature: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """You will have to call this endpoint from your system.

        This is how you will
        notify Stream about events that happen in your system.

        Args:
          delivery_status: The delivery status for the given order

          location_id: The DSP Location ID that this event is for.

          order_id: The DSP Order ID that this event is for.

          driver_details: The driver details for the given order

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(
        ["location_id", "order", "type"],
        ["location_id", "order_id", "type"],
        ["location_id", "status_update", "type"],
        ["delivery_status", "location_id", "order_id", "type"],
    )
    async def submit(
        self,
        partner_id: str,
        *,
        location_id: str,
        order: order_submit_params.StreamWebhookNewOrderEventOrder | Omit = omit,
        type: str,
        stream_webhook_signature: str | Omit = omit,
        order_id: str | Omit = omit,
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
        | Omit = omit,
        cancel_source: Literal["customer", "restaurant", "driver", "dsp", "stream", "unknown"] | Omit = omit,
        status_update: order_submit_params.StreamWebhookStoreStatusUpdateEventStatusUpdate | Omit = omit,
        delivery_status: Literal[
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
        | Omit = omit,
        driver_details: order_submit_params.StreamWebhookDeliveryStatusUpdateEventDriverDetails | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        if not partner_id:
            raise ValueError(f"Expected a non-empty value for `partner_id` but received {partner_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        extra_headers = {
            **strip_not_given({"Stream-Webhook-Signature": stream_webhook_signature}),
            **(extra_headers or {}),
        }
        return await self._post(
            ("https://dev-unstable-orders.hookedapi.com" if not self._client._base_url_overridden else "")
            + path_template("/order/{partner_id}", partner_id=partner_id),
            body=await async_maybe_transform(
                {
                    "location_id": location_id,
                    "order": order,
                    "type": type,
                    "order_id": order_id,
                    "cancel_reason": cancel_reason,
                    "cancel_source": cancel_source,
                    "status_update": status_update,
                    "delivery_status": delivery_status,
                    "driver_details": driver_details,
                },
                order_submit_params.OrderSubmitParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class OrderResourceWithRawResponse:
    def __init__(self, order: OrderResource) -> None:
        self._order = order

        self.submit = to_raw_response_wrapper(
            order.submit,
        )


class AsyncOrderResourceWithRawResponse:
    def __init__(self, order: AsyncOrderResource) -> None:
        self._order = order

        self.submit = async_to_raw_response_wrapper(
            order.submit,
        )


class OrderResourceWithStreamingResponse:
    def __init__(self, order: OrderResource) -> None:
        self._order = order

        self.submit = to_streamed_response_wrapper(
            order.submit,
        )


class AsyncOrderResourceWithStreamingResponse:
    def __init__(self, order: AsyncOrderResource) -> None:
        self._order = order

        self.submit = async_to_streamed_response_wrapper(
            order.submit,
        )
