# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from jenna_stream_orders import JennaStreamOrders, AsyncJennaStreamOrders
from jenna_stream_orders.types.stream_dsp.v1.locations import (
    ConnectionRetrieveResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestConnection:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: JennaStreamOrders) -> None:
        connection = client.stream_dsp.v1.locations.connection.create(
            location_id="location_id",
        )
        assert connection is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: JennaStreamOrders) -> None:
        response = client.stream_dsp.v1.locations.connection.with_raw_response.create(
            location_id="location_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        connection = response.parse()
        assert connection is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: JennaStreamOrders) -> None:
        with client.stream_dsp.v1.locations.connection.with_streaming_response.create(
            location_id="location_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            connection = response.parse()
            assert connection is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: JennaStreamOrders) -> None:
        connection = client.stream_dsp.v1.locations.connection.retrieve(
            location_id="location_id",
        )
        assert_matches_type(ConnectionRetrieveResponse, connection, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: JennaStreamOrders) -> None:
        response = client.stream_dsp.v1.locations.connection.with_raw_response.retrieve(
            location_id="location_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        connection = response.parse()
        assert_matches_type(ConnectionRetrieveResponse, connection, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: JennaStreamOrders) -> None:
        with client.stream_dsp.v1.locations.connection.with_streaming_response.retrieve(
            location_id="location_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            connection = response.parse()
            assert_matches_type(ConnectionRetrieveResponse, connection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: JennaStreamOrders) -> None:
        connection = client.stream_dsp.v1.locations.connection.delete(
            location_id="location_id",
        )
        assert connection is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: JennaStreamOrders) -> None:
        response = client.stream_dsp.v1.locations.connection.with_raw_response.delete(
            location_id="location_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        connection = response.parse()
        assert connection is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: JennaStreamOrders) -> None:
        with client.stream_dsp.v1.locations.connection.with_streaming_response.delete(
            location_id="location_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            connection = response.parse()
            assert connection is None

        assert cast(Any, response.is_closed) is True


class TestAsyncConnection:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncJennaStreamOrders) -> None:
        connection = await async_client.stream_dsp.v1.locations.connection.create(
            location_id="location_id",
        )
        assert connection is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncJennaStreamOrders) -> None:
        response = await async_client.stream_dsp.v1.locations.connection.with_raw_response.create(
            location_id="location_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        connection = await response.parse()
        assert connection is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncJennaStreamOrders) -> None:
        async with async_client.stream_dsp.v1.locations.connection.with_streaming_response.create(
            location_id="location_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            connection = await response.parse()
            assert connection is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncJennaStreamOrders) -> None:
        connection = await async_client.stream_dsp.v1.locations.connection.retrieve(
            location_id="location_id",
        )
        assert_matches_type(ConnectionRetrieveResponse, connection, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncJennaStreamOrders) -> None:
        response = await async_client.stream_dsp.v1.locations.connection.with_raw_response.retrieve(
            location_id="location_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        connection = await response.parse()
        assert_matches_type(ConnectionRetrieveResponse, connection, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncJennaStreamOrders) -> None:
        async with async_client.stream_dsp.v1.locations.connection.with_streaming_response.retrieve(
            location_id="location_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            connection = await response.parse()
            assert_matches_type(ConnectionRetrieveResponse, connection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncJennaStreamOrders) -> None:
        connection = await async_client.stream_dsp.v1.locations.connection.delete(
            location_id="location_id",
        )
        assert connection is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncJennaStreamOrders) -> None:
        response = await async_client.stream_dsp.v1.locations.connection.with_raw_response.delete(
            location_id="location_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        connection = await response.parse()
        assert connection is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncJennaStreamOrders) -> None:
        async with async_client.stream_dsp.v1.locations.connection.with_streaming_response.delete(
            location_id="location_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            connection = await response.parse()
            assert connection is None

        assert cast(Any, response.is_closed) is True
