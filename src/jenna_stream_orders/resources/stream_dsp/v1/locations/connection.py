# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ....._types import Body, Query, Headers, NoneType, NotGiven, not_given
from ....._utils import maybe_transform, async_maybe_transform
from ....._compat import cached_property
from ....._resource import SyncAPIResource, AsyncAPIResource
from ....._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....._base_client import make_request_options
from .....types.stream_dsp.v1.locations import (
    connection_create_params,
    connection_delete_params,
    connection_retrieve_params,
)
from .....types.stream_dsp.v1.locations.connection_retrieve_response import ConnectionRetrieveResponse

__all__ = ["ConnectionResource", "AsyncConnectionResource"]


class ConnectionResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ConnectionResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/jenna-stream-orders-python#accessing-raw-response-data-eg-headers
        """
        return ConnectionResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ConnectionResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/jenna-stream-orders-python#with_streaming_response
        """
        return ConnectionResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        location_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """You will have to build this endpoint into your system.

        This is where Stream will
        notify you about locations connected to Stream.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/stream-dsp/v1/locations/connection",
            body=maybe_transform({"location_id": location_id}, connection_create_params.ConnectionCreateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def retrieve(
        self,
        *,
        location_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ConnectionRetrieveResponse:
        """You will have to build this endpoint into your system.

        This is where Stream will
        check a locations connection state to Stream.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/stream-dsp/v1/locations/connection",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"location_id": location_id}, connection_retrieve_params.ConnectionRetrieveParams
                ),
            ),
            cast_to=ConnectionRetrieveResponse,
        )

    def delete(
        self,
        *,
        location_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """You will have to build this endpoint into your system.

        This is where Stream will
        notify you about locations disconnected from Stream.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            "/stream-dsp/v1/locations/connection",
            body=maybe_transform({"location_id": location_id}, connection_delete_params.ConnectionDeleteParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncConnectionResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncConnectionResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/jenna-stream-orders-python#accessing-raw-response-data-eg-headers
        """
        return AsyncConnectionResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncConnectionResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/jenna-stream-orders-python#with_streaming_response
        """
        return AsyncConnectionResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        location_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """You will have to build this endpoint into your system.

        This is where Stream will
        notify you about locations connected to Stream.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/stream-dsp/v1/locations/connection",
            body=await async_maybe_transform(
                {"location_id": location_id}, connection_create_params.ConnectionCreateParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def retrieve(
        self,
        *,
        location_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ConnectionRetrieveResponse:
        """You will have to build this endpoint into your system.

        This is where Stream will
        check a locations connection state to Stream.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/stream-dsp/v1/locations/connection",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"location_id": location_id}, connection_retrieve_params.ConnectionRetrieveParams
                ),
            ),
            cast_to=ConnectionRetrieveResponse,
        )

    async def delete(
        self,
        *,
        location_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """You will have to build this endpoint into your system.

        This is where Stream will
        notify you about locations disconnected from Stream.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            "/stream-dsp/v1/locations/connection",
            body=await async_maybe_transform(
                {"location_id": location_id}, connection_delete_params.ConnectionDeleteParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class ConnectionResourceWithRawResponse:
    def __init__(self, connection: ConnectionResource) -> None:
        self._connection = connection

        self.create = to_raw_response_wrapper(
            connection.create,
        )
        self.retrieve = to_raw_response_wrapper(
            connection.retrieve,
        )
        self.delete = to_raw_response_wrapper(
            connection.delete,
        )


class AsyncConnectionResourceWithRawResponse:
    def __init__(self, connection: AsyncConnectionResource) -> None:
        self._connection = connection

        self.create = async_to_raw_response_wrapper(
            connection.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            connection.retrieve,
        )
        self.delete = async_to_raw_response_wrapper(
            connection.delete,
        )


class ConnectionResourceWithStreamingResponse:
    def __init__(self, connection: ConnectionResource) -> None:
        self._connection = connection

        self.create = to_streamed_response_wrapper(
            connection.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            connection.retrieve,
        )
        self.delete = to_streamed_response_wrapper(
            connection.delete,
        )


class AsyncConnectionResourceWithStreamingResponse:
    def __init__(self, connection: AsyncConnectionResource) -> None:
        self._connection = connection

        self.create = async_to_streamed_response_wrapper(
            connection.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            connection.retrieve,
        )
        self.delete = async_to_streamed_response_wrapper(
            connection.delete,
        )
