# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Any, cast
from typing_extensions import Literal, overload

import httpx

from ...._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
from ...._utils import required_args, maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.stream_dsp import v1_authorize_params, v1_new_event_params, v1_request_token_params
from .locations.locations import (
    LocationsResource,
    AsyncLocationsResource,
    LocationsResourceWithRawResponse,
    AsyncLocationsResourceWithRawResponse,
    LocationsResourceWithStreamingResponse,
    AsyncLocationsResourceWithStreamingResponse,
)
from ....types.stream_dsp.v1_request_token_response import V1RequestTokenResponse
from ....types.stream_dsp.v1_get_menu_file_url_response import V1GetMenuFileURLResponse

__all__ = ["V1Resource", "AsyncV1Resource"]


class V1Resource(SyncAPIResource):
    @cached_property
    def locations(self) -> LocationsResource:
        return LocationsResource(self._client)

    @cached_property
    def with_raw_response(self) -> V1ResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/meet-jenna/stream-orders-python#accessing-raw-response-data-eg-headers
        """
        return V1ResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> V1ResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/meet-jenna/stream-orders-python#with_streaming_response
        """
        return V1ResourceWithStreamingResponse(self)

    def authorize(
        self,
        *,
        client_id: str,
        redirect_uri: str,
        response_type: Literal["code"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """You will have to build this endpoint into your system.

        This is where Stream will
        initiate the oAuth process.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._get(
            "/stream-dsp/v1/authorize",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "client_id": client_id,
                        "redirect_uri": redirect_uri,
                        "response_type": response_type,
                    },
                    v1_authorize_params.V1AuthorizeParams,
                ),
                security={"bearer_auth": True},
            ),
            cast_to=NoneType,
        )

    def get_menu_file_url(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> V1GetMenuFileURLResponse:
        """
        This is where you will retrieve all menu contents, the URL will be provided in
        the location.publish event. Response schema version (v1 or v2) is determined by
        partner configuration flag. Partners must contact support to enable v2 schema
        access.
        """
        return cast(
            V1GetMenuFileURLResponse,
            self._get(
                "/stream-dsp/v1/menuFileS3Url",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    security={"bearer_auth": True},
                ),
                cast_to=cast(
                    Any, V1GetMenuFileURLResponse
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    @overload
    def new_event(
        self,
        *,
        location_id: str,
        type: str,
        until_ms: float | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """You will have to build this endpoint into your system.

        This is where Stream will
        send all webhook events.

        Args:
          location_id: The location ID that should be paused

          type: The type of event that this is.

          until_ms: The time in milliseconds to pause until. If not specified, the location will be
              paused indefinitely.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def new_event(
        self,
        *,
        location_id: str,
        type: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """You will have to build this endpoint into your system.

        This is where Stream will
        send all webhook events.

        Args:
          location_id: The location ID that should be resumed

          type: The type of event that this is.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def new_event(
        self,
        *,
        location_id: str,
        type: str,
        download_url: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """You will have to build this endpoint into your system.

        This is where Stream will
        send all webhook events.

        Args:
          location_id: The location ID that this menu ingest applies to.

          type: The type of event that this is.

          download_url: This is an S3 URL pointing to a JSON file containing contents in the shape of
              DspLocationMenuEventDataDto.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def new_event(
        self,
        *,
        location_id: str,
        object_updates: v1_new_event_params.DspLocationMenuUpdateEventDtoObjectUpdates,
        type: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """You will have to build this endpoint into your system.

        This is where Stream will
        send all webhook events.

        Args:
          location_id: The location ID that this menu update event applies to.

          object_updates: Object updates to be applied across all menus

          type: The type of event that this is.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def new_event(
        self,
        *,
        location_id: str,
        type: str,
        estimated_ready_at_ms: float | Omit = omit,
        order_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """You will have to build this endpoint into your system.

        This is where Stream will
        send all webhook events.

        Args:
          location_id: The location ID that this order is for.

          type: The type of event that this is.

          estimated_ready_at_ms: The estimated time in milliseconds that the order will be ready for pickup.

          order_id: The order ID that this event is for.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def new_event(
        self,
        *,
        location_id: str,
        type: str,
        failure_details: v1_new_event_params.DspLocationOrderFailedEventDtoFailureDetails | Omit = omit,
        failure_reason: Literal[
            "restaurant_not_accepting_orders",
            "location_not_found",
            "pos_missing_items",
            "items_unavailable",
            "order_validation_error",
            "unknown",
        ]
        | Omit = omit,
        order_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """You will have to build this endpoint into your system.

        This is where Stream will
        send all webhook events.

        Args:
          location_id: The location ID that this order is for.

          type: The type of event that this is.

          failure_details: Details related to the order failure.

          failure_reason: The reason for the order failure.

          order_id: The order ID that this event is for.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def new_event(
        self,
        *,
        location_id: str,
        type: str,
        order_id: str | Omit = omit,
        order_status_update: Literal["ready_for_pickup", "completed"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """You will have to build this endpoint into your system.

        This is where Stream will
        send all webhook events.

        Args:
          location_id: The location ID that this order is for.

          type: The type of event that this is.

          order_id: The order ID that this event is for.

          order_status_update: An updated status of the order.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def new_event(
        self,
        *,
        location_id: str,
        type: str,
        order_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """You will have to build this endpoint into your system.

        This is where Stream will
        send all webhook events.

        Args:
          location_id: The location ID that this order is for.

          type: The type of event that this is.

          order_id: The order ID that this event is for.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["location_id", "type"], ["location_id", "object_updates", "type"])
    def new_event(
        self,
        *,
        location_id: str,
        type: str,
        until_ms: float | Omit = omit,
        download_url: str | Omit = omit,
        object_updates: v1_new_event_params.DspLocationMenuUpdateEventDtoObjectUpdates | Omit = omit,
        estimated_ready_at_ms: float | Omit = omit,
        order_id: str | Omit = omit,
        failure_details: v1_new_event_params.DspLocationOrderFailedEventDtoFailureDetails | Omit = omit,
        failure_reason: Literal[
            "restaurant_not_accepting_orders",
            "location_not_found",
            "pos_missing_items",
            "items_unavailable",
            "order_validation_error",
            "unknown",
        ]
        | Omit = omit,
        order_status_update: Literal["ready_for_pickup", "completed"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        return self._post(
            "/stream-dsp/v1/event",
            body=maybe_transform(
                {
                    "location_id": location_id,
                    "type": type,
                    "until_ms": until_ms,
                    "download_url": download_url,
                    "object_updates": object_updates,
                    "estimated_ready_at_ms": estimated_ready_at_ms,
                    "order_id": order_id,
                    "failure_details": failure_details,
                    "failure_reason": failure_reason,
                    "order_status_update": order_status_update,
                },
                v1_new_event_params.V1NewEventParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                security={"bearer_auth": True},
            ),
            cast_to=object,
        )

    @overload
    def request_token(
        self,
        *,
        client_id: str,
        client_secret: str,
        code: str,
        grant_type: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> V1RequestTokenResponse:
        """You will have to build this endpoint into your system.

        This is where Stream will
        request and refresh access tokens.

        Args:
          client_id: The client ID to be provided to Stream for identifying us.

          client_secret: The client secret to be provided to Stream for security.

          code: The authorization code received from successful authorization.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def request_token(
        self,
        *,
        client_id: str,
        client_secret: str,
        grant_type: str,
        refresh_token: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> V1RequestTokenResponse:
        """You will have to build this endpoint into your system.

        This is where Stream will
        request and refresh access tokens.

        Args:
          client_id: The client ID to be provided to Stream for identifying us.

          client_secret: The client secret to be provided to Stream for security.

          refresh_token: The refresh token from the existing session for refresh

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(
        ["client_id", "client_secret", "code", "grant_type"],
        ["client_id", "client_secret", "grant_type", "refresh_token"],
    )
    def request_token(
        self,
        *,
        client_id: str,
        client_secret: str,
        code: str | Omit = omit,
        grant_type: str,
        refresh_token: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> V1RequestTokenResponse:
        return self._post(
            "/stream-dsp/v1/token",
            body=maybe_transform(
                {
                    "client_id": client_id,
                    "client_secret": client_secret,
                    "code": code,
                    "grant_type": grant_type,
                    "refresh_token": refresh_token,
                },
                v1_request_token_params.V1RequestTokenParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                security={"bearer_auth": True},
            ),
            cast_to=V1RequestTokenResponse,
        )


class AsyncV1Resource(AsyncAPIResource):
    @cached_property
    def locations(self) -> AsyncLocationsResource:
        return AsyncLocationsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncV1ResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/meet-jenna/stream-orders-python#accessing-raw-response-data-eg-headers
        """
        return AsyncV1ResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncV1ResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/meet-jenna/stream-orders-python#with_streaming_response
        """
        return AsyncV1ResourceWithStreamingResponse(self)

    async def authorize(
        self,
        *,
        client_id: str,
        redirect_uri: str,
        response_type: Literal["code"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """You will have to build this endpoint into your system.

        This is where Stream will
        initiate the oAuth process.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._get(
            "/stream-dsp/v1/authorize",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "client_id": client_id,
                        "redirect_uri": redirect_uri,
                        "response_type": response_type,
                    },
                    v1_authorize_params.V1AuthorizeParams,
                ),
                security={"bearer_auth": True},
            ),
            cast_to=NoneType,
        )

    async def get_menu_file_url(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> V1GetMenuFileURLResponse:
        """
        This is where you will retrieve all menu contents, the URL will be provided in
        the location.publish event. Response schema version (v1 or v2) is determined by
        partner configuration flag. Partners must contact support to enable v2 schema
        access.
        """
        return cast(
            V1GetMenuFileURLResponse,
            await self._get(
                "/stream-dsp/v1/menuFileS3Url",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    security={"bearer_auth": True},
                ),
                cast_to=cast(
                    Any, V1GetMenuFileURLResponse
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    @overload
    async def new_event(
        self,
        *,
        location_id: str,
        type: str,
        until_ms: float | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """You will have to build this endpoint into your system.

        This is where Stream will
        send all webhook events.

        Args:
          location_id: The location ID that should be paused

          type: The type of event that this is.

          until_ms: The time in milliseconds to pause until. If not specified, the location will be
              paused indefinitely.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def new_event(
        self,
        *,
        location_id: str,
        type: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """You will have to build this endpoint into your system.

        This is where Stream will
        send all webhook events.

        Args:
          location_id: The location ID that should be resumed

          type: The type of event that this is.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def new_event(
        self,
        *,
        location_id: str,
        type: str,
        download_url: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """You will have to build this endpoint into your system.

        This is where Stream will
        send all webhook events.

        Args:
          location_id: The location ID that this menu ingest applies to.

          type: The type of event that this is.

          download_url: This is an S3 URL pointing to a JSON file containing contents in the shape of
              DspLocationMenuEventDataDto.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def new_event(
        self,
        *,
        location_id: str,
        object_updates: v1_new_event_params.DspLocationMenuUpdateEventDtoObjectUpdates,
        type: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """You will have to build this endpoint into your system.

        This is where Stream will
        send all webhook events.

        Args:
          location_id: The location ID that this menu update event applies to.

          object_updates: Object updates to be applied across all menus

          type: The type of event that this is.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def new_event(
        self,
        *,
        location_id: str,
        type: str,
        estimated_ready_at_ms: float | Omit = omit,
        order_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """You will have to build this endpoint into your system.

        This is where Stream will
        send all webhook events.

        Args:
          location_id: The location ID that this order is for.

          type: The type of event that this is.

          estimated_ready_at_ms: The estimated time in milliseconds that the order will be ready for pickup.

          order_id: The order ID that this event is for.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def new_event(
        self,
        *,
        location_id: str,
        type: str,
        failure_details: v1_new_event_params.DspLocationOrderFailedEventDtoFailureDetails | Omit = omit,
        failure_reason: Literal[
            "restaurant_not_accepting_orders",
            "location_not_found",
            "pos_missing_items",
            "items_unavailable",
            "order_validation_error",
            "unknown",
        ]
        | Omit = omit,
        order_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """You will have to build this endpoint into your system.

        This is where Stream will
        send all webhook events.

        Args:
          location_id: The location ID that this order is for.

          type: The type of event that this is.

          failure_details: Details related to the order failure.

          failure_reason: The reason for the order failure.

          order_id: The order ID that this event is for.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def new_event(
        self,
        *,
        location_id: str,
        type: str,
        order_id: str | Omit = omit,
        order_status_update: Literal["ready_for_pickup", "completed"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """You will have to build this endpoint into your system.

        This is where Stream will
        send all webhook events.

        Args:
          location_id: The location ID that this order is for.

          type: The type of event that this is.

          order_id: The order ID that this event is for.

          order_status_update: An updated status of the order.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def new_event(
        self,
        *,
        location_id: str,
        type: str,
        order_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """You will have to build this endpoint into your system.

        This is where Stream will
        send all webhook events.

        Args:
          location_id: The location ID that this order is for.

          type: The type of event that this is.

          order_id: The order ID that this event is for.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["location_id", "type"], ["location_id", "object_updates", "type"])
    async def new_event(
        self,
        *,
        location_id: str,
        type: str,
        until_ms: float | Omit = omit,
        download_url: str | Omit = omit,
        object_updates: v1_new_event_params.DspLocationMenuUpdateEventDtoObjectUpdates | Omit = omit,
        estimated_ready_at_ms: float | Omit = omit,
        order_id: str | Omit = omit,
        failure_details: v1_new_event_params.DspLocationOrderFailedEventDtoFailureDetails | Omit = omit,
        failure_reason: Literal[
            "restaurant_not_accepting_orders",
            "location_not_found",
            "pos_missing_items",
            "items_unavailable",
            "order_validation_error",
            "unknown",
        ]
        | Omit = omit,
        order_status_update: Literal["ready_for_pickup", "completed"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        return await self._post(
            "/stream-dsp/v1/event",
            body=await async_maybe_transform(
                {
                    "location_id": location_id,
                    "type": type,
                    "until_ms": until_ms,
                    "download_url": download_url,
                    "object_updates": object_updates,
                    "estimated_ready_at_ms": estimated_ready_at_ms,
                    "order_id": order_id,
                    "failure_details": failure_details,
                    "failure_reason": failure_reason,
                    "order_status_update": order_status_update,
                },
                v1_new_event_params.V1NewEventParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                security={"bearer_auth": True},
            ),
            cast_to=object,
        )

    @overload
    async def request_token(
        self,
        *,
        client_id: str,
        client_secret: str,
        code: str,
        grant_type: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> V1RequestTokenResponse:
        """You will have to build this endpoint into your system.

        This is where Stream will
        request and refresh access tokens.

        Args:
          client_id: The client ID to be provided to Stream for identifying us.

          client_secret: The client secret to be provided to Stream for security.

          code: The authorization code received from successful authorization.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def request_token(
        self,
        *,
        client_id: str,
        client_secret: str,
        grant_type: str,
        refresh_token: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> V1RequestTokenResponse:
        """You will have to build this endpoint into your system.

        This is where Stream will
        request and refresh access tokens.

        Args:
          client_id: The client ID to be provided to Stream for identifying us.

          client_secret: The client secret to be provided to Stream for security.

          refresh_token: The refresh token from the existing session for refresh

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(
        ["client_id", "client_secret", "code", "grant_type"],
        ["client_id", "client_secret", "grant_type", "refresh_token"],
    )
    async def request_token(
        self,
        *,
        client_id: str,
        client_secret: str,
        code: str | Omit = omit,
        grant_type: str,
        refresh_token: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> V1RequestTokenResponse:
        return await self._post(
            "/stream-dsp/v1/token",
            body=await async_maybe_transform(
                {
                    "client_id": client_id,
                    "client_secret": client_secret,
                    "code": code,
                    "grant_type": grant_type,
                    "refresh_token": refresh_token,
                },
                v1_request_token_params.V1RequestTokenParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                security={"bearer_auth": True},
            ),
            cast_to=V1RequestTokenResponse,
        )


class V1ResourceWithRawResponse:
    def __init__(self, v1: V1Resource) -> None:
        self._v1 = v1

        self.authorize = to_raw_response_wrapper(
            v1.authorize,
        )
        self.get_menu_file_url = to_raw_response_wrapper(
            v1.get_menu_file_url,
        )
        self.new_event = to_raw_response_wrapper(
            v1.new_event,
        )
        self.request_token = to_raw_response_wrapper(
            v1.request_token,
        )

    @cached_property
    def locations(self) -> LocationsResourceWithRawResponse:
        return LocationsResourceWithRawResponse(self._v1.locations)


class AsyncV1ResourceWithRawResponse:
    def __init__(self, v1: AsyncV1Resource) -> None:
        self._v1 = v1

        self.authorize = async_to_raw_response_wrapper(
            v1.authorize,
        )
        self.get_menu_file_url = async_to_raw_response_wrapper(
            v1.get_menu_file_url,
        )
        self.new_event = async_to_raw_response_wrapper(
            v1.new_event,
        )
        self.request_token = async_to_raw_response_wrapper(
            v1.request_token,
        )

    @cached_property
    def locations(self) -> AsyncLocationsResourceWithRawResponse:
        return AsyncLocationsResourceWithRawResponse(self._v1.locations)


class V1ResourceWithStreamingResponse:
    def __init__(self, v1: V1Resource) -> None:
        self._v1 = v1

        self.authorize = to_streamed_response_wrapper(
            v1.authorize,
        )
        self.get_menu_file_url = to_streamed_response_wrapper(
            v1.get_menu_file_url,
        )
        self.new_event = to_streamed_response_wrapper(
            v1.new_event,
        )
        self.request_token = to_streamed_response_wrapper(
            v1.request_token,
        )

    @cached_property
    def locations(self) -> LocationsResourceWithStreamingResponse:
        return LocationsResourceWithStreamingResponse(self._v1.locations)


class AsyncV1ResourceWithStreamingResponse:
    def __init__(self, v1: AsyncV1Resource) -> None:
        self._v1 = v1

        self.authorize = async_to_streamed_response_wrapper(
            v1.authorize,
        )
        self.get_menu_file_url = async_to_streamed_response_wrapper(
            v1.get_menu_file_url,
        )
        self.new_event = async_to_streamed_response_wrapper(
            v1.new_event,
        )
        self.request_token = async_to_streamed_response_wrapper(
            v1.request_token,
        )

    @cached_property
    def locations(self) -> AsyncLocationsResourceWithStreamingResponse:
        return AsyncLocationsResourceWithStreamingResponse(self._v1.locations)
