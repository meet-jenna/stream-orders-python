# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from jenna_stream_orders import JennaStreamOrders, AsyncJennaStreamOrders
from jenna_stream_orders.types.stream_dsp import (
    V1RequestTokenResponse,
    V1GetMenuFileURLResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestV1:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_authorize(self, client: JennaStreamOrders) -> None:
        v1 = client.stream_dsp.v1.authorize(
            client_id="client_id",
            redirect_uri="redirect_uri",
            response_type="code",
        )
        assert v1 is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_authorize(self, client: JennaStreamOrders) -> None:
        response = client.stream_dsp.v1.with_raw_response.authorize(
            client_id="client_id",
            redirect_uri="redirect_uri",
            response_type="code",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = response.parse()
        assert v1 is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_authorize(self, client: JennaStreamOrders) -> None:
        with client.stream_dsp.v1.with_streaming_response.authorize(
            client_id="client_id",
            redirect_uri="redirect_uri",
            response_type="code",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = response.parse()
            assert v1 is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_menu_file_url(self, client: JennaStreamOrders) -> None:
        v1 = client.stream_dsp.v1.get_menu_file_url()
        assert_matches_type(V1GetMenuFileURLResponse, v1, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_menu_file_url(self, client: JennaStreamOrders) -> None:
        response = client.stream_dsp.v1.with_raw_response.get_menu_file_url()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = response.parse()
        assert_matches_type(V1GetMenuFileURLResponse, v1, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_menu_file_url(self, client: JennaStreamOrders) -> None:
        with client.stream_dsp.v1.with_streaming_response.get_menu_file_url() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = response.parse()
            assert_matches_type(V1GetMenuFileURLResponse, v1, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_new_event_overload_1(self, client: JennaStreamOrders) -> None:
        v1 = client.stream_dsp.v1.new_event(
            location_id="location_id",
            type="type",
        )
        assert_matches_type(object, v1, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_new_event_with_all_params_overload_1(self, client: JennaStreamOrders) -> None:
        v1 = client.stream_dsp.v1.new_event(
            location_id="location_id",
            type="type",
            until_ms=0,
        )
        assert_matches_type(object, v1, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_new_event_overload_1(self, client: JennaStreamOrders) -> None:
        response = client.stream_dsp.v1.with_raw_response.new_event(
            location_id="location_id",
            type="type",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = response.parse()
        assert_matches_type(object, v1, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_new_event_overload_1(self, client: JennaStreamOrders) -> None:
        with client.stream_dsp.v1.with_streaming_response.new_event(
            location_id="location_id",
            type="type",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = response.parse()
            assert_matches_type(object, v1, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_new_event_overload_2(self, client: JennaStreamOrders) -> None:
        v1 = client.stream_dsp.v1.new_event(
            location_id="location_id",
            type="type",
        )
        assert_matches_type(object, v1, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_new_event_overload_2(self, client: JennaStreamOrders) -> None:
        response = client.stream_dsp.v1.with_raw_response.new_event(
            location_id="location_id",
            type="type",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = response.parse()
        assert_matches_type(object, v1, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_new_event_overload_2(self, client: JennaStreamOrders) -> None:
        with client.stream_dsp.v1.with_streaming_response.new_event(
            location_id="location_id",
            type="type",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = response.parse()
            assert_matches_type(object, v1, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_new_event_overload_3(self, client: JennaStreamOrders) -> None:
        v1 = client.stream_dsp.v1.new_event(
            location_id="location_id",
            type="type",
        )
        assert_matches_type(object, v1, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_new_event_with_all_params_overload_3(self, client: JennaStreamOrders) -> None:
        v1 = client.stream_dsp.v1.new_event(
            location_id="location_id",
            type="type",
            download_url="download_url",
        )
        assert_matches_type(object, v1, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_new_event_overload_3(self, client: JennaStreamOrders) -> None:
        response = client.stream_dsp.v1.with_raw_response.new_event(
            location_id="location_id",
            type="type",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = response.parse()
        assert_matches_type(object, v1, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_new_event_overload_3(self, client: JennaStreamOrders) -> None:
        with client.stream_dsp.v1.with_streaming_response.new_event(
            location_id="location_id",
            type="type",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = response.parse()
            assert_matches_type(object, v1, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_new_event_overload_4(self, client: JennaStreamOrders) -> None:
        v1 = client.stream_dsp.v1.new_event(
            location_id="location_id",
            object_updates={
                "items": [
                    {
                        "is_active": True,
                        "stream_id": "stream_id",
                    }
                ],
                "modifiers": [
                    {
                        "is_active": True,
                        "stream_id": "stream_id",
                    }
                ],
                "variations": [
                    {
                        "is_active": True,
                        "stream_id": "stream_id",
                    }
                ],
            },
            type="type",
        )
        assert_matches_type(object, v1, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_new_event_overload_4(self, client: JennaStreamOrders) -> None:
        response = client.stream_dsp.v1.with_raw_response.new_event(
            location_id="location_id",
            object_updates={
                "items": [
                    {
                        "is_active": True,
                        "stream_id": "stream_id",
                    }
                ],
                "modifiers": [
                    {
                        "is_active": True,
                        "stream_id": "stream_id",
                    }
                ],
                "variations": [
                    {
                        "is_active": True,
                        "stream_id": "stream_id",
                    }
                ],
            },
            type="type",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = response.parse()
        assert_matches_type(object, v1, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_new_event_overload_4(self, client: JennaStreamOrders) -> None:
        with client.stream_dsp.v1.with_streaming_response.new_event(
            location_id="location_id",
            object_updates={
                "items": [
                    {
                        "is_active": True,
                        "stream_id": "stream_id",
                    }
                ],
                "modifiers": [
                    {
                        "is_active": True,
                        "stream_id": "stream_id",
                    }
                ],
                "variations": [
                    {
                        "is_active": True,
                        "stream_id": "stream_id",
                    }
                ],
            },
            type="type",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = response.parse()
            assert_matches_type(object, v1, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_new_event_overload_5(self, client: JennaStreamOrders) -> None:
        v1 = client.stream_dsp.v1.new_event(
            location_id="location_id",
            type="type",
        )
        assert_matches_type(object, v1, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_new_event_with_all_params_overload_5(self, client: JennaStreamOrders) -> None:
        v1 = client.stream_dsp.v1.new_event(
            location_id="location_id",
            type="type",
            estimated_ready_at_ms=0,
            order_id="order_id",
        )
        assert_matches_type(object, v1, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_new_event_overload_5(self, client: JennaStreamOrders) -> None:
        response = client.stream_dsp.v1.with_raw_response.new_event(
            location_id="location_id",
            type="type",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = response.parse()
        assert_matches_type(object, v1, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_new_event_overload_5(self, client: JennaStreamOrders) -> None:
        with client.stream_dsp.v1.with_streaming_response.new_event(
            location_id="location_id",
            type="type",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = response.parse()
            assert_matches_type(object, v1, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_new_event_overload_6(self, client: JennaStreamOrders) -> None:
        v1 = client.stream_dsp.v1.new_event(
            location_id="location_id",
            type="type",
        )
        assert_matches_type(object, v1, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_new_event_with_all_params_overload_6(self, client: JennaStreamOrders) -> None:
        v1 = client.stream_dsp.v1.new_event(
            location_id="location_id",
            type="type",
            failure_details={
                "invalid_item_ids": ["string"],
                "error_message": "error_message",
            },
            failure_reason="restaurant_not_accepting_orders",
            order_id="order_id",
        )
        assert_matches_type(object, v1, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_new_event_overload_6(self, client: JennaStreamOrders) -> None:
        response = client.stream_dsp.v1.with_raw_response.new_event(
            location_id="location_id",
            type="type",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = response.parse()
        assert_matches_type(object, v1, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_new_event_overload_6(self, client: JennaStreamOrders) -> None:
        with client.stream_dsp.v1.with_streaming_response.new_event(
            location_id="location_id",
            type="type",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = response.parse()
            assert_matches_type(object, v1, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_new_event_overload_7(self, client: JennaStreamOrders) -> None:
        v1 = client.stream_dsp.v1.new_event(
            location_id="location_id",
            type="type",
        )
        assert_matches_type(object, v1, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_new_event_with_all_params_overload_7(self, client: JennaStreamOrders) -> None:
        v1 = client.stream_dsp.v1.new_event(
            location_id="location_id",
            type="type",
            order_id="order_id",
            order_status_update="ready_for_pickup",
        )
        assert_matches_type(object, v1, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_new_event_overload_7(self, client: JennaStreamOrders) -> None:
        response = client.stream_dsp.v1.with_raw_response.new_event(
            location_id="location_id",
            type="type",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = response.parse()
        assert_matches_type(object, v1, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_new_event_overload_7(self, client: JennaStreamOrders) -> None:
        with client.stream_dsp.v1.with_streaming_response.new_event(
            location_id="location_id",
            type="type",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = response.parse()
            assert_matches_type(object, v1, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_new_event_overload_8(self, client: JennaStreamOrders) -> None:
        v1 = client.stream_dsp.v1.new_event(
            location_id="location_id",
            type="type",
        )
        assert_matches_type(object, v1, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_new_event_with_all_params_overload_8(self, client: JennaStreamOrders) -> None:
        v1 = client.stream_dsp.v1.new_event(
            location_id="location_id",
            type="type",
            order_id="order_id",
        )
        assert_matches_type(object, v1, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_new_event_overload_8(self, client: JennaStreamOrders) -> None:
        response = client.stream_dsp.v1.with_raw_response.new_event(
            location_id="location_id",
            type="type",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = response.parse()
        assert_matches_type(object, v1, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_new_event_overload_8(self, client: JennaStreamOrders) -> None:
        with client.stream_dsp.v1.with_streaming_response.new_event(
            location_id="location_id",
            type="type",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = response.parse()
            assert_matches_type(object, v1, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_request_token_overload_1(self, client: JennaStreamOrders) -> None:
        v1 = client.stream_dsp.v1.request_token(
            client_id="client_id",
            client_secret="client_secret",
            code="code",
            grant_type="grant_type",
        )
        assert_matches_type(V1RequestTokenResponse, v1, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_request_token_overload_1(self, client: JennaStreamOrders) -> None:
        response = client.stream_dsp.v1.with_raw_response.request_token(
            client_id="client_id",
            client_secret="client_secret",
            code="code",
            grant_type="grant_type",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = response.parse()
        assert_matches_type(V1RequestTokenResponse, v1, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_request_token_overload_1(self, client: JennaStreamOrders) -> None:
        with client.stream_dsp.v1.with_streaming_response.request_token(
            client_id="client_id",
            client_secret="client_secret",
            code="code",
            grant_type="grant_type",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = response.parse()
            assert_matches_type(V1RequestTokenResponse, v1, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_request_token_overload_2(self, client: JennaStreamOrders) -> None:
        v1 = client.stream_dsp.v1.request_token(
            client_id="client_id",
            client_secret="client_secret",
            grant_type="grant_type",
            refresh_token="refresh_token",
        )
        assert_matches_type(V1RequestTokenResponse, v1, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_request_token_overload_2(self, client: JennaStreamOrders) -> None:
        response = client.stream_dsp.v1.with_raw_response.request_token(
            client_id="client_id",
            client_secret="client_secret",
            grant_type="grant_type",
            refresh_token="refresh_token",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = response.parse()
        assert_matches_type(V1RequestTokenResponse, v1, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_request_token_overload_2(self, client: JennaStreamOrders) -> None:
        with client.stream_dsp.v1.with_streaming_response.request_token(
            client_id="client_id",
            client_secret="client_secret",
            grant_type="grant_type",
            refresh_token="refresh_token",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = response.parse()
            assert_matches_type(V1RequestTokenResponse, v1, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncV1:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_authorize(self, async_client: AsyncJennaStreamOrders) -> None:
        v1 = await async_client.stream_dsp.v1.authorize(
            client_id="client_id",
            redirect_uri="redirect_uri",
            response_type="code",
        )
        assert v1 is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_authorize(self, async_client: AsyncJennaStreamOrders) -> None:
        response = await async_client.stream_dsp.v1.with_raw_response.authorize(
            client_id="client_id",
            redirect_uri="redirect_uri",
            response_type="code",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = await response.parse()
        assert v1 is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_authorize(self, async_client: AsyncJennaStreamOrders) -> None:
        async with async_client.stream_dsp.v1.with_streaming_response.authorize(
            client_id="client_id",
            redirect_uri="redirect_uri",
            response_type="code",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = await response.parse()
            assert v1 is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_menu_file_url(self, async_client: AsyncJennaStreamOrders) -> None:
        v1 = await async_client.stream_dsp.v1.get_menu_file_url()
        assert_matches_type(V1GetMenuFileURLResponse, v1, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_menu_file_url(self, async_client: AsyncJennaStreamOrders) -> None:
        response = await async_client.stream_dsp.v1.with_raw_response.get_menu_file_url()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = await response.parse()
        assert_matches_type(V1GetMenuFileURLResponse, v1, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_menu_file_url(self, async_client: AsyncJennaStreamOrders) -> None:
        async with async_client.stream_dsp.v1.with_streaming_response.get_menu_file_url() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = await response.parse()
            assert_matches_type(V1GetMenuFileURLResponse, v1, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_new_event_overload_1(self, async_client: AsyncJennaStreamOrders) -> None:
        v1 = await async_client.stream_dsp.v1.new_event(
            location_id="location_id",
            type="type",
        )
        assert_matches_type(object, v1, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_new_event_with_all_params_overload_1(self, async_client: AsyncJennaStreamOrders) -> None:
        v1 = await async_client.stream_dsp.v1.new_event(
            location_id="location_id",
            type="type",
            until_ms=0,
        )
        assert_matches_type(object, v1, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_new_event_overload_1(self, async_client: AsyncJennaStreamOrders) -> None:
        response = await async_client.stream_dsp.v1.with_raw_response.new_event(
            location_id="location_id",
            type="type",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = await response.parse()
        assert_matches_type(object, v1, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_new_event_overload_1(self, async_client: AsyncJennaStreamOrders) -> None:
        async with async_client.stream_dsp.v1.with_streaming_response.new_event(
            location_id="location_id",
            type="type",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = await response.parse()
            assert_matches_type(object, v1, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_new_event_overload_2(self, async_client: AsyncJennaStreamOrders) -> None:
        v1 = await async_client.stream_dsp.v1.new_event(
            location_id="location_id",
            type="type",
        )
        assert_matches_type(object, v1, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_new_event_overload_2(self, async_client: AsyncJennaStreamOrders) -> None:
        response = await async_client.stream_dsp.v1.with_raw_response.new_event(
            location_id="location_id",
            type="type",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = await response.parse()
        assert_matches_type(object, v1, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_new_event_overload_2(self, async_client: AsyncJennaStreamOrders) -> None:
        async with async_client.stream_dsp.v1.with_streaming_response.new_event(
            location_id="location_id",
            type="type",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = await response.parse()
            assert_matches_type(object, v1, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_new_event_overload_3(self, async_client: AsyncJennaStreamOrders) -> None:
        v1 = await async_client.stream_dsp.v1.new_event(
            location_id="location_id",
            type="type",
        )
        assert_matches_type(object, v1, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_new_event_with_all_params_overload_3(self, async_client: AsyncJennaStreamOrders) -> None:
        v1 = await async_client.stream_dsp.v1.new_event(
            location_id="location_id",
            type="type",
            download_url="download_url",
        )
        assert_matches_type(object, v1, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_new_event_overload_3(self, async_client: AsyncJennaStreamOrders) -> None:
        response = await async_client.stream_dsp.v1.with_raw_response.new_event(
            location_id="location_id",
            type="type",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = await response.parse()
        assert_matches_type(object, v1, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_new_event_overload_3(self, async_client: AsyncJennaStreamOrders) -> None:
        async with async_client.stream_dsp.v1.with_streaming_response.new_event(
            location_id="location_id",
            type="type",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = await response.parse()
            assert_matches_type(object, v1, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_new_event_overload_4(self, async_client: AsyncJennaStreamOrders) -> None:
        v1 = await async_client.stream_dsp.v1.new_event(
            location_id="location_id",
            object_updates={
                "items": [
                    {
                        "is_active": True,
                        "stream_id": "stream_id",
                    }
                ],
                "modifiers": [
                    {
                        "is_active": True,
                        "stream_id": "stream_id",
                    }
                ],
                "variations": [
                    {
                        "is_active": True,
                        "stream_id": "stream_id",
                    }
                ],
            },
            type="type",
        )
        assert_matches_type(object, v1, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_new_event_overload_4(self, async_client: AsyncJennaStreamOrders) -> None:
        response = await async_client.stream_dsp.v1.with_raw_response.new_event(
            location_id="location_id",
            object_updates={
                "items": [
                    {
                        "is_active": True,
                        "stream_id": "stream_id",
                    }
                ],
                "modifiers": [
                    {
                        "is_active": True,
                        "stream_id": "stream_id",
                    }
                ],
                "variations": [
                    {
                        "is_active": True,
                        "stream_id": "stream_id",
                    }
                ],
            },
            type="type",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = await response.parse()
        assert_matches_type(object, v1, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_new_event_overload_4(self, async_client: AsyncJennaStreamOrders) -> None:
        async with async_client.stream_dsp.v1.with_streaming_response.new_event(
            location_id="location_id",
            object_updates={
                "items": [
                    {
                        "is_active": True,
                        "stream_id": "stream_id",
                    }
                ],
                "modifiers": [
                    {
                        "is_active": True,
                        "stream_id": "stream_id",
                    }
                ],
                "variations": [
                    {
                        "is_active": True,
                        "stream_id": "stream_id",
                    }
                ],
            },
            type="type",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = await response.parse()
            assert_matches_type(object, v1, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_new_event_overload_5(self, async_client: AsyncJennaStreamOrders) -> None:
        v1 = await async_client.stream_dsp.v1.new_event(
            location_id="location_id",
            type="type",
        )
        assert_matches_type(object, v1, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_new_event_with_all_params_overload_5(self, async_client: AsyncJennaStreamOrders) -> None:
        v1 = await async_client.stream_dsp.v1.new_event(
            location_id="location_id",
            type="type",
            estimated_ready_at_ms=0,
            order_id="order_id",
        )
        assert_matches_type(object, v1, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_new_event_overload_5(self, async_client: AsyncJennaStreamOrders) -> None:
        response = await async_client.stream_dsp.v1.with_raw_response.new_event(
            location_id="location_id",
            type="type",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = await response.parse()
        assert_matches_type(object, v1, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_new_event_overload_5(self, async_client: AsyncJennaStreamOrders) -> None:
        async with async_client.stream_dsp.v1.with_streaming_response.new_event(
            location_id="location_id",
            type="type",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = await response.parse()
            assert_matches_type(object, v1, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_new_event_overload_6(self, async_client: AsyncJennaStreamOrders) -> None:
        v1 = await async_client.stream_dsp.v1.new_event(
            location_id="location_id",
            type="type",
        )
        assert_matches_type(object, v1, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_new_event_with_all_params_overload_6(self, async_client: AsyncJennaStreamOrders) -> None:
        v1 = await async_client.stream_dsp.v1.new_event(
            location_id="location_id",
            type="type",
            failure_details={
                "invalid_item_ids": ["string"],
                "error_message": "error_message",
            },
            failure_reason="restaurant_not_accepting_orders",
            order_id="order_id",
        )
        assert_matches_type(object, v1, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_new_event_overload_6(self, async_client: AsyncJennaStreamOrders) -> None:
        response = await async_client.stream_dsp.v1.with_raw_response.new_event(
            location_id="location_id",
            type="type",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = await response.parse()
        assert_matches_type(object, v1, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_new_event_overload_6(self, async_client: AsyncJennaStreamOrders) -> None:
        async with async_client.stream_dsp.v1.with_streaming_response.new_event(
            location_id="location_id",
            type="type",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = await response.parse()
            assert_matches_type(object, v1, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_new_event_overload_7(self, async_client: AsyncJennaStreamOrders) -> None:
        v1 = await async_client.stream_dsp.v1.new_event(
            location_id="location_id",
            type="type",
        )
        assert_matches_type(object, v1, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_new_event_with_all_params_overload_7(self, async_client: AsyncJennaStreamOrders) -> None:
        v1 = await async_client.stream_dsp.v1.new_event(
            location_id="location_id",
            type="type",
            order_id="order_id",
            order_status_update="ready_for_pickup",
        )
        assert_matches_type(object, v1, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_new_event_overload_7(self, async_client: AsyncJennaStreamOrders) -> None:
        response = await async_client.stream_dsp.v1.with_raw_response.new_event(
            location_id="location_id",
            type="type",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = await response.parse()
        assert_matches_type(object, v1, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_new_event_overload_7(self, async_client: AsyncJennaStreamOrders) -> None:
        async with async_client.stream_dsp.v1.with_streaming_response.new_event(
            location_id="location_id",
            type="type",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = await response.parse()
            assert_matches_type(object, v1, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_new_event_overload_8(self, async_client: AsyncJennaStreamOrders) -> None:
        v1 = await async_client.stream_dsp.v1.new_event(
            location_id="location_id",
            type="type",
        )
        assert_matches_type(object, v1, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_new_event_with_all_params_overload_8(self, async_client: AsyncJennaStreamOrders) -> None:
        v1 = await async_client.stream_dsp.v1.new_event(
            location_id="location_id",
            type="type",
            order_id="order_id",
        )
        assert_matches_type(object, v1, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_new_event_overload_8(self, async_client: AsyncJennaStreamOrders) -> None:
        response = await async_client.stream_dsp.v1.with_raw_response.new_event(
            location_id="location_id",
            type="type",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = await response.parse()
        assert_matches_type(object, v1, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_new_event_overload_8(self, async_client: AsyncJennaStreamOrders) -> None:
        async with async_client.stream_dsp.v1.with_streaming_response.new_event(
            location_id="location_id",
            type="type",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = await response.parse()
            assert_matches_type(object, v1, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_request_token_overload_1(self, async_client: AsyncJennaStreamOrders) -> None:
        v1 = await async_client.stream_dsp.v1.request_token(
            client_id="client_id",
            client_secret="client_secret",
            code="code",
            grant_type="grant_type",
        )
        assert_matches_type(V1RequestTokenResponse, v1, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_request_token_overload_1(self, async_client: AsyncJennaStreamOrders) -> None:
        response = await async_client.stream_dsp.v1.with_raw_response.request_token(
            client_id="client_id",
            client_secret="client_secret",
            code="code",
            grant_type="grant_type",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = await response.parse()
        assert_matches_type(V1RequestTokenResponse, v1, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_request_token_overload_1(self, async_client: AsyncJennaStreamOrders) -> None:
        async with async_client.stream_dsp.v1.with_streaming_response.request_token(
            client_id="client_id",
            client_secret="client_secret",
            code="code",
            grant_type="grant_type",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = await response.parse()
            assert_matches_type(V1RequestTokenResponse, v1, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_request_token_overload_2(self, async_client: AsyncJennaStreamOrders) -> None:
        v1 = await async_client.stream_dsp.v1.request_token(
            client_id="client_id",
            client_secret="client_secret",
            grant_type="grant_type",
            refresh_token="refresh_token",
        )
        assert_matches_type(V1RequestTokenResponse, v1, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_request_token_overload_2(self, async_client: AsyncJennaStreamOrders) -> None:
        response = await async_client.stream_dsp.v1.with_raw_response.request_token(
            client_id="client_id",
            client_secret="client_secret",
            grant_type="grant_type",
            refresh_token="refresh_token",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = await response.parse()
        assert_matches_type(V1RequestTokenResponse, v1, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_request_token_overload_2(self, async_client: AsyncJennaStreamOrders) -> None:
        async with async_client.stream_dsp.v1.with_streaming_response.request_token(
            client_id="client_id",
            client_secret="client_secret",
            grant_type="grant_type",
            refresh_token="refresh_token",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = await response.parse()
            assert_matches_type(V1RequestTokenResponse, v1, path=["response"])

        assert cast(Any, response.is_closed) is True
