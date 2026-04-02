# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from jenna_stream_orders import JennaStreamOrders, AsyncJennaStreamOrders

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestOrder:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_submit_overload_1(self, client: JennaStreamOrders) -> None:
        order = client.order.submit(
            partner_id="partner_id",
            location_id="location_id",
            order={
                "id": "id",
                "customer_facing_id": "customer_facing_id",
                "customers": [
                    {
                        "id": "id",
                        "email": "email",
                        "name": "name",
                        "phone": "phone",
                    }
                ],
                "fulfillment_type": "curbside",
                "items": [
                    {
                        "id": "id",
                        "currency": "currency",
                        "modifiers": [
                            {
                                "id": "id",
                                "currency": "usd",
                                "modifiers": [],
                                "name": "name",
                                "price": 0,
                                "quantity": 0,
                            }
                        ],
                        "name": "name",
                        "price": 0,
                        "quantity": 0,
                    }
                ],
                "subtotal": 0,
                "tax": 0,
                "tax_withheld": 0,
            },
            type="type",
        )
        assert order is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_submit_with_all_params_overload_1(self, client: JennaStreamOrders) -> None:
        order = client.order.submit(
            partner_id="partner_id",
            location_id="location_id",
            order={
                "id": "id",
                "customer_facing_id": "customer_facing_id",
                "customers": [
                    {
                        "id": "id",
                        "email": "email",
                        "name": "name",
                        "phone": "phone",
                        "masked_phone_code": "masked_phone_code",
                    }
                ],
                "fulfillment_type": "curbside",
                "items": [
                    {
                        "id": "id",
                        "currency": "currency",
                        "modifiers": [
                            {
                                "id": "id",
                                "currency": "usd",
                                "modifiers": [],
                                "name": "name",
                                "price": 0,
                                "quantity": 0,
                                "modifier_group_id": "modifier_group_id",
                            }
                        ],
                        "name": "name",
                        "price": 0,
                        "quantity": 0,
                        "category_id": "category_id",
                        "customer_id": "customer_id",
                        "item_id": "item_id",
                        "special_instructions": "special_instructions",
                    }
                ],
                "subtotal": 0,
                "tax": 0,
                "tax_withheld": 0,
                "brand": "brand",
                "customer": {
                    "id": "id",
                    "email": "email",
                    "name": "name",
                    "phone": "phone",
                    "masked_phone_code": "masked_phone_code",
                },
                "delivery_address": {
                    "address_line_1": "address_line_1",
                    "city": "city",
                    "country": "country",
                    "postal_code": "postal_code",
                    "state": "state",
                    "address_line_2": "address_line_2",
                },
                "delivery_fee": 0,
                "delivery_fee_taxes": 0,
                "discounts": [
                    {
                        "id": "id",
                        "amount": 0,
                        "item_id": "item_id",
                    }
                ],
                "driver_tip": 0,
                "estimated_ready_at_ms": 0,
                "fulfillment_instructions": "fulfillment_instructions",
                "is_future_order": True,
                "service_charge": 0,
                "should_include_utensils": True,
                "special_instructions": "special_instructions",
                "status": "scheduled",
                "store_tip": 0,
                "unpaid": True,
            },
            type="type",
            stream_webhook_signature="Stream-Webhook-Signature",
        )
        assert order is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_submit_overload_1(self, client: JennaStreamOrders) -> None:
        response = client.order.with_raw_response.submit(
            partner_id="partner_id",
            location_id="location_id",
            order={
                "id": "id",
                "customer_facing_id": "customer_facing_id",
                "customers": [
                    {
                        "id": "id",
                        "email": "email",
                        "name": "name",
                        "phone": "phone",
                    }
                ],
                "fulfillment_type": "curbside",
                "items": [
                    {
                        "id": "id",
                        "currency": "currency",
                        "modifiers": [
                            {
                                "id": "id",
                                "currency": "usd",
                                "modifiers": [],
                                "name": "name",
                                "price": 0,
                                "quantity": 0,
                            }
                        ],
                        "name": "name",
                        "price": 0,
                        "quantity": 0,
                    }
                ],
                "subtotal": 0,
                "tax": 0,
                "tax_withheld": 0,
            },
            type="type",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        order = response.parse()
        assert order is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_submit_overload_1(self, client: JennaStreamOrders) -> None:
        with client.order.with_streaming_response.submit(
            partner_id="partner_id",
            location_id="location_id",
            order={
                "id": "id",
                "customer_facing_id": "customer_facing_id",
                "customers": [
                    {
                        "id": "id",
                        "email": "email",
                        "name": "name",
                        "phone": "phone",
                    }
                ],
                "fulfillment_type": "curbside",
                "items": [
                    {
                        "id": "id",
                        "currency": "currency",
                        "modifiers": [
                            {
                                "id": "id",
                                "currency": "usd",
                                "modifiers": [],
                                "name": "name",
                                "price": 0,
                                "quantity": 0,
                            }
                        ],
                        "name": "name",
                        "price": 0,
                        "quantity": 0,
                    }
                ],
                "subtotal": 0,
                "tax": 0,
                "tax_withheld": 0,
            },
            type="type",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            order = response.parse()
            assert order is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_submit_overload_1(self, client: JennaStreamOrders) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `partner_id` but received ''"):
            client.order.with_raw_response.submit(
                partner_id="",
                location_id="location_id",
                order={
                    "id": "id",
                    "customer_facing_id": "customer_facing_id",
                    "customers": [
                        {
                            "id": "id",
                            "email": "email",
                            "name": "name",
                            "phone": "phone",
                        }
                    ],
                    "fulfillment_type": "curbside",
                    "items": [
                        {
                            "id": "id",
                            "currency": "currency",
                            "modifiers": [
                                {
                                    "id": "id",
                                    "currency": "usd",
                                    "modifiers": [],
                                    "name": "name",
                                    "price": 0,
                                    "quantity": 0,
                                }
                            ],
                            "name": "name",
                            "price": 0,
                            "quantity": 0,
                        }
                    ],
                    "subtotal": 0,
                    "tax": 0,
                    "tax_withheld": 0,
                },
                type="type",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_submit_overload_2(self, client: JennaStreamOrders) -> None:
        order = client.order.submit(
            partner_id="partner_id",
            location_id="location_id",
            order_id="order_id",
            type="type",
        )
        assert order is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_submit_with_all_params_overload_2(self, client: JennaStreamOrders) -> None:
        order = client.order.submit(
            partner_id="partner_id",
            location_id="location_id",
            order_id="order_id",
            type="type",
            cancel_reason="customer_requested",
            cancel_source="customer",
            stream_webhook_signature="Stream-Webhook-Signature",
        )
        assert order is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_submit_overload_2(self, client: JennaStreamOrders) -> None:
        response = client.order.with_raw_response.submit(
            partner_id="partner_id",
            location_id="location_id",
            order_id="order_id",
            type="type",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        order = response.parse()
        assert order is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_submit_overload_2(self, client: JennaStreamOrders) -> None:
        with client.order.with_streaming_response.submit(
            partner_id="partner_id",
            location_id="location_id",
            order_id="order_id",
            type="type",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            order = response.parse()
            assert order is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_submit_overload_2(self, client: JennaStreamOrders) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `partner_id` but received ''"):
            client.order.with_raw_response.submit(
                partner_id="",
                location_id="location_id",
                order_id="order_id",
                type="type",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_submit_overload_3(self, client: JennaStreamOrders) -> None:
        order = client.order.submit(
            partner_id="partner_id",
            location_id="location_id",
            status_update={"status": "online"},
            type="type",
        )
        assert order is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_submit_with_all_params_overload_3(self, client: JennaStreamOrders) -> None:
        order = client.order.submit(
            partner_id="partner_id",
            location_id="location_id",
            status_update={
                "status": "online",
                "end_time": 0,
                "start_time": 0,
            },
            type="type",
            stream_webhook_signature="Stream-Webhook-Signature",
        )
        assert order is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_submit_overload_3(self, client: JennaStreamOrders) -> None:
        response = client.order.with_raw_response.submit(
            partner_id="partner_id",
            location_id="location_id",
            status_update={"status": "online"},
            type="type",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        order = response.parse()
        assert order is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_submit_overload_3(self, client: JennaStreamOrders) -> None:
        with client.order.with_streaming_response.submit(
            partner_id="partner_id",
            location_id="location_id",
            status_update={"status": "online"},
            type="type",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            order = response.parse()
            assert order is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_submit_overload_3(self, client: JennaStreamOrders) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `partner_id` but received ''"):
            client.order.with_raw_response.submit(
                partner_id="",
                location_id="location_id",
                status_update={"status": "online"},
                type="type",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_submit_overload_4(self, client: JennaStreamOrders) -> None:
        order = client.order.submit(
            partner_id="partner_id",
            delivery_status="pending",
            location_id="location_id",
            order_id="order_id",
            type="type",
        )
        assert order is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_submit_with_all_params_overload_4(self, client: JennaStreamOrders) -> None:
        order = client.order.submit(
            partner_id="partner_id",
            delivery_status="pending",
            location_id="location_id",
            order_id="order_id",
            type="type",
            driver_details={
                "name": "name",
                "phone": {
                    "code": "code",
                    "number": "number",
                },
                "source": "source",
                "vehicle_info": {
                    "color": "color",
                    "is_autonomous": True,
                    "license_plate": "license_plate",
                    "make": "make",
                    "model": "model",
                },
                "handoff_instructions": "handoff_instructions",
                "passcode": "passcode",
                "picture_url": "picture_url",
            },
            stream_webhook_signature="Stream-Webhook-Signature",
        )
        assert order is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_submit_overload_4(self, client: JennaStreamOrders) -> None:
        response = client.order.with_raw_response.submit(
            partner_id="partner_id",
            delivery_status="pending",
            location_id="location_id",
            order_id="order_id",
            type="type",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        order = response.parse()
        assert order is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_submit_overload_4(self, client: JennaStreamOrders) -> None:
        with client.order.with_streaming_response.submit(
            partner_id="partner_id",
            delivery_status="pending",
            location_id="location_id",
            order_id="order_id",
            type="type",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            order = response.parse()
            assert order is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_submit_overload_4(self, client: JennaStreamOrders) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `partner_id` but received ''"):
            client.order.with_raw_response.submit(
                partner_id="",
                delivery_status="pending",
                location_id="location_id",
                order_id="order_id",
                type="type",
            )


class TestAsyncOrder:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_submit_overload_1(self, async_client: AsyncJennaStreamOrders) -> None:
        order = await async_client.order.submit(
            partner_id="partner_id",
            location_id="location_id",
            order={
                "id": "id",
                "customer_facing_id": "customer_facing_id",
                "customers": [
                    {
                        "id": "id",
                        "email": "email",
                        "name": "name",
                        "phone": "phone",
                    }
                ],
                "fulfillment_type": "curbside",
                "items": [
                    {
                        "id": "id",
                        "currency": "currency",
                        "modifiers": [
                            {
                                "id": "id",
                                "currency": "usd",
                                "modifiers": [],
                                "name": "name",
                                "price": 0,
                                "quantity": 0,
                            }
                        ],
                        "name": "name",
                        "price": 0,
                        "quantity": 0,
                    }
                ],
                "subtotal": 0,
                "tax": 0,
                "tax_withheld": 0,
            },
            type="type",
        )
        assert order is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_submit_with_all_params_overload_1(self, async_client: AsyncJennaStreamOrders) -> None:
        order = await async_client.order.submit(
            partner_id="partner_id",
            location_id="location_id",
            order={
                "id": "id",
                "customer_facing_id": "customer_facing_id",
                "customers": [
                    {
                        "id": "id",
                        "email": "email",
                        "name": "name",
                        "phone": "phone",
                        "masked_phone_code": "masked_phone_code",
                    }
                ],
                "fulfillment_type": "curbside",
                "items": [
                    {
                        "id": "id",
                        "currency": "currency",
                        "modifiers": [
                            {
                                "id": "id",
                                "currency": "usd",
                                "modifiers": [],
                                "name": "name",
                                "price": 0,
                                "quantity": 0,
                                "modifier_group_id": "modifier_group_id",
                            }
                        ],
                        "name": "name",
                        "price": 0,
                        "quantity": 0,
                        "category_id": "category_id",
                        "customer_id": "customer_id",
                        "item_id": "item_id",
                        "special_instructions": "special_instructions",
                    }
                ],
                "subtotal": 0,
                "tax": 0,
                "tax_withheld": 0,
                "brand": "brand",
                "customer": {
                    "id": "id",
                    "email": "email",
                    "name": "name",
                    "phone": "phone",
                    "masked_phone_code": "masked_phone_code",
                },
                "delivery_address": {
                    "address_line_1": "address_line_1",
                    "city": "city",
                    "country": "country",
                    "postal_code": "postal_code",
                    "state": "state",
                    "address_line_2": "address_line_2",
                },
                "delivery_fee": 0,
                "delivery_fee_taxes": 0,
                "discounts": [
                    {
                        "id": "id",
                        "amount": 0,
                        "item_id": "item_id",
                    }
                ],
                "driver_tip": 0,
                "estimated_ready_at_ms": 0,
                "fulfillment_instructions": "fulfillment_instructions",
                "is_future_order": True,
                "service_charge": 0,
                "should_include_utensils": True,
                "special_instructions": "special_instructions",
                "status": "scheduled",
                "store_tip": 0,
                "unpaid": True,
            },
            type="type",
            stream_webhook_signature="Stream-Webhook-Signature",
        )
        assert order is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_submit_overload_1(self, async_client: AsyncJennaStreamOrders) -> None:
        response = await async_client.order.with_raw_response.submit(
            partner_id="partner_id",
            location_id="location_id",
            order={
                "id": "id",
                "customer_facing_id": "customer_facing_id",
                "customers": [
                    {
                        "id": "id",
                        "email": "email",
                        "name": "name",
                        "phone": "phone",
                    }
                ],
                "fulfillment_type": "curbside",
                "items": [
                    {
                        "id": "id",
                        "currency": "currency",
                        "modifiers": [
                            {
                                "id": "id",
                                "currency": "usd",
                                "modifiers": [],
                                "name": "name",
                                "price": 0,
                                "quantity": 0,
                            }
                        ],
                        "name": "name",
                        "price": 0,
                        "quantity": 0,
                    }
                ],
                "subtotal": 0,
                "tax": 0,
                "tax_withheld": 0,
            },
            type="type",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        order = await response.parse()
        assert order is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_submit_overload_1(self, async_client: AsyncJennaStreamOrders) -> None:
        async with async_client.order.with_streaming_response.submit(
            partner_id="partner_id",
            location_id="location_id",
            order={
                "id": "id",
                "customer_facing_id": "customer_facing_id",
                "customers": [
                    {
                        "id": "id",
                        "email": "email",
                        "name": "name",
                        "phone": "phone",
                    }
                ],
                "fulfillment_type": "curbside",
                "items": [
                    {
                        "id": "id",
                        "currency": "currency",
                        "modifiers": [
                            {
                                "id": "id",
                                "currency": "usd",
                                "modifiers": [],
                                "name": "name",
                                "price": 0,
                                "quantity": 0,
                            }
                        ],
                        "name": "name",
                        "price": 0,
                        "quantity": 0,
                    }
                ],
                "subtotal": 0,
                "tax": 0,
                "tax_withheld": 0,
            },
            type="type",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            order = await response.parse()
            assert order is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_submit_overload_1(self, async_client: AsyncJennaStreamOrders) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `partner_id` but received ''"):
            await async_client.order.with_raw_response.submit(
                partner_id="",
                location_id="location_id",
                order={
                    "id": "id",
                    "customer_facing_id": "customer_facing_id",
                    "customers": [
                        {
                            "id": "id",
                            "email": "email",
                            "name": "name",
                            "phone": "phone",
                        }
                    ],
                    "fulfillment_type": "curbside",
                    "items": [
                        {
                            "id": "id",
                            "currency": "currency",
                            "modifiers": [
                                {
                                    "id": "id",
                                    "currency": "usd",
                                    "modifiers": [],
                                    "name": "name",
                                    "price": 0,
                                    "quantity": 0,
                                }
                            ],
                            "name": "name",
                            "price": 0,
                            "quantity": 0,
                        }
                    ],
                    "subtotal": 0,
                    "tax": 0,
                    "tax_withheld": 0,
                },
                type="type",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_submit_overload_2(self, async_client: AsyncJennaStreamOrders) -> None:
        order = await async_client.order.submit(
            partner_id="partner_id",
            location_id="location_id",
            order_id="order_id",
            type="type",
        )
        assert order is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_submit_with_all_params_overload_2(self, async_client: AsyncJennaStreamOrders) -> None:
        order = await async_client.order.submit(
            partner_id="partner_id",
            location_id="location_id",
            order_id="order_id",
            type="type",
            cancel_reason="customer_requested",
            cancel_source="customer",
            stream_webhook_signature="Stream-Webhook-Signature",
        )
        assert order is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_submit_overload_2(self, async_client: AsyncJennaStreamOrders) -> None:
        response = await async_client.order.with_raw_response.submit(
            partner_id="partner_id",
            location_id="location_id",
            order_id="order_id",
            type="type",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        order = await response.parse()
        assert order is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_submit_overload_2(self, async_client: AsyncJennaStreamOrders) -> None:
        async with async_client.order.with_streaming_response.submit(
            partner_id="partner_id",
            location_id="location_id",
            order_id="order_id",
            type="type",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            order = await response.parse()
            assert order is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_submit_overload_2(self, async_client: AsyncJennaStreamOrders) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `partner_id` but received ''"):
            await async_client.order.with_raw_response.submit(
                partner_id="",
                location_id="location_id",
                order_id="order_id",
                type="type",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_submit_overload_3(self, async_client: AsyncJennaStreamOrders) -> None:
        order = await async_client.order.submit(
            partner_id="partner_id",
            location_id="location_id",
            status_update={"status": "online"},
            type="type",
        )
        assert order is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_submit_with_all_params_overload_3(self, async_client: AsyncJennaStreamOrders) -> None:
        order = await async_client.order.submit(
            partner_id="partner_id",
            location_id="location_id",
            status_update={
                "status": "online",
                "end_time": 0,
                "start_time": 0,
            },
            type="type",
            stream_webhook_signature="Stream-Webhook-Signature",
        )
        assert order is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_submit_overload_3(self, async_client: AsyncJennaStreamOrders) -> None:
        response = await async_client.order.with_raw_response.submit(
            partner_id="partner_id",
            location_id="location_id",
            status_update={"status": "online"},
            type="type",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        order = await response.parse()
        assert order is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_submit_overload_3(self, async_client: AsyncJennaStreamOrders) -> None:
        async with async_client.order.with_streaming_response.submit(
            partner_id="partner_id",
            location_id="location_id",
            status_update={"status": "online"},
            type="type",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            order = await response.parse()
            assert order is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_submit_overload_3(self, async_client: AsyncJennaStreamOrders) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `partner_id` but received ''"):
            await async_client.order.with_raw_response.submit(
                partner_id="",
                location_id="location_id",
                status_update={"status": "online"},
                type="type",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_submit_overload_4(self, async_client: AsyncJennaStreamOrders) -> None:
        order = await async_client.order.submit(
            partner_id="partner_id",
            delivery_status="pending",
            location_id="location_id",
            order_id="order_id",
            type="type",
        )
        assert order is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_submit_with_all_params_overload_4(self, async_client: AsyncJennaStreamOrders) -> None:
        order = await async_client.order.submit(
            partner_id="partner_id",
            delivery_status="pending",
            location_id="location_id",
            order_id="order_id",
            type="type",
            driver_details={
                "name": "name",
                "phone": {
                    "code": "code",
                    "number": "number",
                },
                "source": "source",
                "vehicle_info": {
                    "color": "color",
                    "is_autonomous": True,
                    "license_plate": "license_plate",
                    "make": "make",
                    "model": "model",
                },
                "handoff_instructions": "handoff_instructions",
                "passcode": "passcode",
                "picture_url": "picture_url",
            },
            stream_webhook_signature="Stream-Webhook-Signature",
        )
        assert order is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_submit_overload_4(self, async_client: AsyncJennaStreamOrders) -> None:
        response = await async_client.order.with_raw_response.submit(
            partner_id="partner_id",
            delivery_status="pending",
            location_id="location_id",
            order_id="order_id",
            type="type",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        order = await response.parse()
        assert order is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_submit_overload_4(self, async_client: AsyncJennaStreamOrders) -> None:
        async with async_client.order.with_streaming_response.submit(
            partner_id="partner_id",
            delivery_status="pending",
            location_id="location_id",
            order_id="order_id",
            type="type",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            order = await response.parse()
            assert order is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_submit_overload_4(self, async_client: AsyncJennaStreamOrders) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `partner_id` but received ''"):
            await async_client.order.with_raw_response.submit(
                partner_id="",
                delivery_status="pending",
                location_id="location_id",
                order_id="order_id",
                type="type",
            )
