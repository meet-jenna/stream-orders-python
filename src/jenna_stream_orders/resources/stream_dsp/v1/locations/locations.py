# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ....._types import Body, Query, Headers, NotGiven, not_given
from .connection import (
    ConnectionResource,
    AsyncConnectionResource,
    ConnectionResourceWithRawResponse,
    AsyncConnectionResourceWithRawResponse,
    ConnectionResourceWithStreamingResponse,
    AsyncConnectionResourceWithStreamingResponse,
)
from ....._compat import cached_property
from ....._resource import SyncAPIResource, AsyncAPIResource
from ....._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....._base_client import make_request_options
from .....types.stream_dsp.v1.location_list_response import LocationListResponse

__all__ = ["LocationsResource", "AsyncLocationsResource"]


class LocationsResource(SyncAPIResource):
    @cached_property
    def connection(self) -> ConnectionResource:
        return ConnectionResource(self._client)

    @cached_property
    def with_raw_response(self) -> LocationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/meet-jenna/stream-orders-python#accessing-raw-response-data-eg-headers
        """
        return LocationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> LocationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/meet-jenna/stream-orders-python#with_streaming_response
        """
        return LocationsResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LocationListResponse:
        """You will have to build this endpoint into your system.

        This is where Stream will
        query the locations attached to the OAuth token.
        """
        return self._get(
            "/stream-dsp/v1/locations",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LocationListResponse,
        )


class AsyncLocationsResource(AsyncAPIResource):
    @cached_property
    def connection(self) -> AsyncConnectionResource:
        return AsyncConnectionResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncLocationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/meet-jenna/stream-orders-python#accessing-raw-response-data-eg-headers
        """
        return AsyncLocationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncLocationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/meet-jenna/stream-orders-python#with_streaming_response
        """
        return AsyncLocationsResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LocationListResponse:
        """You will have to build this endpoint into your system.

        This is where Stream will
        query the locations attached to the OAuth token.
        """
        return await self._get(
            "/stream-dsp/v1/locations",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LocationListResponse,
        )


class LocationsResourceWithRawResponse:
    def __init__(self, locations: LocationsResource) -> None:
        self._locations = locations

        self.list = to_raw_response_wrapper(
            locations.list,
        )

    @cached_property
    def connection(self) -> ConnectionResourceWithRawResponse:
        return ConnectionResourceWithRawResponse(self._locations.connection)


class AsyncLocationsResourceWithRawResponse:
    def __init__(self, locations: AsyncLocationsResource) -> None:
        self._locations = locations

        self.list = async_to_raw_response_wrapper(
            locations.list,
        )

    @cached_property
    def connection(self) -> AsyncConnectionResourceWithRawResponse:
        return AsyncConnectionResourceWithRawResponse(self._locations.connection)


class LocationsResourceWithStreamingResponse:
    def __init__(self, locations: LocationsResource) -> None:
        self._locations = locations

        self.list = to_streamed_response_wrapper(
            locations.list,
        )

    @cached_property
    def connection(self) -> ConnectionResourceWithStreamingResponse:
        return ConnectionResourceWithStreamingResponse(self._locations.connection)


class AsyncLocationsResourceWithStreamingResponse:
    def __init__(self, locations: AsyncLocationsResource) -> None:
        self._locations = locations

        self.list = async_to_streamed_response_wrapper(
            locations.list,
        )

    @cached_property
    def connection(self) -> AsyncConnectionResourceWithStreamingResponse:
        return AsyncConnectionResourceWithStreamingResponse(self._locations.connection)
