# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import TYPE_CHECKING, Any, Mapping
from typing_extensions import Self, override

import httpx

from . import _exceptions
from ._qs import Querystring
from ._types import (
    Omit,
    Headers,
    Timeout,
    NotGiven,
    Transport,
    ProxiesTypes,
    RequestOptions,
    not_given,
)
from ._utils import is_given, get_async_library
from ._compat import cached_property
from ._models import SecurityOptions
from ._version import __version__
from ._streaming import Stream as Stream, AsyncStream as AsyncStream
from ._exceptions import APIStatusError
from ._base_client import (
    DEFAULT_MAX_RETRIES,
    SyncAPIClient,
    AsyncAPIClient,
)

if TYPE_CHECKING:
    from .resources import order, stream_dsp
    from .resources.order import OrderResource, AsyncOrderResource
    from .resources.stream_dsp.stream_dsp import StreamDspResource, AsyncStreamDspResource

__all__ = [
    "Timeout",
    "Transport",
    "ProxiesTypes",
    "RequestOptions",
    "JennaStreamOrders",
    "AsyncJennaStreamOrders",
    "Client",
    "AsyncClient",
]


class JennaStreamOrders(SyncAPIClient):
    # client options
    api_key: str | None
    webhook_secret: str | None

    def __init__(
        self,
        *,
        api_key: str | None = None,
        webhook_secret: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#client) for more details.
        http_client: httpx.Client | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new synchronous JennaStreamOrders client instance.

        This automatically infers the following arguments from their corresponding environment variables if they are not provided:
        - `api_key` from `JENNA_STREAM_ORDERS_API_KEY`
        - `webhook_secret` from `STREAM_DCP_WEBHOOK_SECRET`
        """
        if api_key is None:
            api_key = os.environ.get("JENNA_STREAM_ORDERS_API_KEY")
        self.api_key = api_key

        if webhook_secret is None:
            webhook_secret = os.environ.get("STREAM_DCP_WEBHOOK_SECRET")
        self.webhook_secret = webhook_secret

        if base_url is None:
            base_url = os.environ.get("JENNA_STREAM_ORDERS_BASE_URL")
        self._base_url_overridden = base_url is not None
        if base_url is None:
            base_url = f"https://api.example.com"

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

    @cached_property
    def stream_dsp(self) -> StreamDspResource:
        from .resources.stream_dsp import StreamDspResource

        return StreamDspResource(self)

    @cached_property
    def order(self) -> OrderResource:
        from .resources.order import OrderResource

        return OrderResource(self)

    @cached_property
    def with_raw_response(self) -> JennaStreamOrdersWithRawResponse:
        return JennaStreamOrdersWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> JennaStreamOrdersWithStreamedResponse:
        return JennaStreamOrdersWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @override
    def _auth_headers(self, security: SecurityOptions) -> dict[str, str]:
        return {
            **(self._bearer_auth if security.get("bearer_auth", False) else {}),
            **(self._webhook_hmac if security.get("webhook_hmac", False) else {}),
        }

    @property
    def _bearer_auth(self) -> dict[str, str]:
        api_key = self.api_key
        if api_key is None:
            return {}
        return {"Authorization": f"Bearer {api_key}"}

    @property
    def _webhook_hmac(self) -> dict[str, str]:
        webhook_secret = self.webhook_secret
        if webhook_secret is None:
            return {}
        return {"Stream-Webhook-Signature": webhook_secret}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": "false",
            **self._custom_headers,
        }

    @override
    def _validate_headers(self, headers: Headers, custom_headers: Headers) -> None:
        if headers.get("Authorization") or isinstance(custom_headers.get("Authorization"), Omit):
            return

        if headers.get("Stream-Webhook-Signature") or isinstance(custom_headers.get("Stream-Webhook-Signature"), Omit):
            return

        raise TypeError(
            '"Could not resolve authentication method. Expected either api_key or webhook_secret to be set. Or for one of the `Authorization` or `Stream-Webhook-Signature` headers to be explicitly omitted"'
        )

    def copy(
        self,
        *,
        api_key: str | None = None,
        webhook_secret: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        http_client: httpx.Client | None = None,
        max_retries: int | NotGiven = not_given,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        client = self.__class__(
            api_key=api_key or self.api_key,
            webhook_secret=webhook_secret or self.webhook_secret,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )
        client._base_url_overridden = self._base_url_overridden or base_url is not None
        return client

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class AsyncJennaStreamOrders(AsyncAPIClient):
    # client options
    api_key: str | None
    webhook_secret: str | None

    def __init__(
        self,
        *,
        api_key: str | None = None,
        webhook_secret: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultAsyncHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#asyncclient) for more details.
        http_client: httpx.AsyncClient | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new async AsyncJennaStreamOrders client instance.

        This automatically infers the following arguments from their corresponding environment variables if they are not provided:
        - `api_key` from `JENNA_STREAM_ORDERS_API_KEY`
        - `webhook_secret` from `STREAM_DCP_WEBHOOK_SECRET`
        """
        if api_key is None:
            api_key = os.environ.get("JENNA_STREAM_ORDERS_API_KEY")
        self.api_key = api_key

        if webhook_secret is None:
            webhook_secret = os.environ.get("STREAM_DCP_WEBHOOK_SECRET")
        self.webhook_secret = webhook_secret

        if base_url is None:
            base_url = os.environ.get("JENNA_STREAM_ORDERS_BASE_URL")
        self._base_url_overridden = base_url is not None
        if base_url is None:
            base_url = f"https://api.example.com"

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

    @cached_property
    def stream_dsp(self) -> AsyncStreamDspResource:
        from .resources.stream_dsp import AsyncStreamDspResource

        return AsyncStreamDspResource(self)

    @cached_property
    def order(self) -> AsyncOrderResource:
        from .resources.order import AsyncOrderResource

        return AsyncOrderResource(self)

    @cached_property
    def with_raw_response(self) -> AsyncJennaStreamOrdersWithRawResponse:
        return AsyncJennaStreamOrdersWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncJennaStreamOrdersWithStreamedResponse:
        return AsyncJennaStreamOrdersWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @override
    def _auth_headers(self, security: SecurityOptions) -> dict[str, str]:
        return {
            **(self._bearer_auth if security.get("bearer_auth", False) else {}),
            **(self._webhook_hmac if security.get("webhook_hmac", False) else {}),
        }

    @property
    def _bearer_auth(self) -> dict[str, str]:
        api_key = self.api_key
        if api_key is None:
            return {}
        return {"Authorization": f"Bearer {api_key}"}

    @property
    def _webhook_hmac(self) -> dict[str, str]:
        webhook_secret = self.webhook_secret
        if webhook_secret is None:
            return {}
        return {"Stream-Webhook-Signature": webhook_secret}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": f"async:{get_async_library()}",
            **self._custom_headers,
        }

    @override
    def _validate_headers(self, headers: Headers, custom_headers: Headers) -> None:
        if headers.get("Authorization") or isinstance(custom_headers.get("Authorization"), Omit):
            return

        if headers.get("Stream-Webhook-Signature") or isinstance(custom_headers.get("Stream-Webhook-Signature"), Omit):
            return

        raise TypeError(
            '"Could not resolve authentication method. Expected either api_key or webhook_secret to be set. Or for one of the `Authorization` or `Stream-Webhook-Signature` headers to be explicitly omitted"'
        )

    def copy(
        self,
        *,
        api_key: str | None = None,
        webhook_secret: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        http_client: httpx.AsyncClient | None = None,
        max_retries: int | NotGiven = not_given,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        client = self.__class__(
            api_key=api_key or self.api_key,
            webhook_secret=webhook_secret or self.webhook_secret,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )
        client._base_url_overridden = self._base_url_overridden or base_url is not None
        return client

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class JennaStreamOrdersWithRawResponse:
    _client: JennaStreamOrders

    def __init__(self, client: JennaStreamOrders) -> None:
        self._client = client

    @cached_property
    def stream_dsp(self) -> stream_dsp.StreamDspResourceWithRawResponse:
        from .resources.stream_dsp import StreamDspResourceWithRawResponse

        return StreamDspResourceWithRawResponse(self._client.stream_dsp)

    @cached_property
    def order(self) -> order.OrderResourceWithRawResponse:
        from .resources.order import OrderResourceWithRawResponse

        return OrderResourceWithRawResponse(self._client.order)


class AsyncJennaStreamOrdersWithRawResponse:
    _client: AsyncJennaStreamOrders

    def __init__(self, client: AsyncJennaStreamOrders) -> None:
        self._client = client

    @cached_property
    def stream_dsp(self) -> stream_dsp.AsyncStreamDspResourceWithRawResponse:
        from .resources.stream_dsp import AsyncStreamDspResourceWithRawResponse

        return AsyncStreamDspResourceWithRawResponse(self._client.stream_dsp)

    @cached_property
    def order(self) -> order.AsyncOrderResourceWithRawResponse:
        from .resources.order import AsyncOrderResourceWithRawResponse

        return AsyncOrderResourceWithRawResponse(self._client.order)


class JennaStreamOrdersWithStreamedResponse:
    _client: JennaStreamOrders

    def __init__(self, client: JennaStreamOrders) -> None:
        self._client = client

    @cached_property
    def stream_dsp(self) -> stream_dsp.StreamDspResourceWithStreamingResponse:
        from .resources.stream_dsp import StreamDspResourceWithStreamingResponse

        return StreamDspResourceWithStreamingResponse(self._client.stream_dsp)

    @cached_property
    def order(self) -> order.OrderResourceWithStreamingResponse:
        from .resources.order import OrderResourceWithStreamingResponse

        return OrderResourceWithStreamingResponse(self._client.order)


class AsyncJennaStreamOrdersWithStreamedResponse:
    _client: AsyncJennaStreamOrders

    def __init__(self, client: AsyncJennaStreamOrders) -> None:
        self._client = client

    @cached_property
    def stream_dsp(self) -> stream_dsp.AsyncStreamDspResourceWithStreamingResponse:
        from .resources.stream_dsp import AsyncStreamDspResourceWithStreamingResponse

        return AsyncStreamDspResourceWithStreamingResponse(self._client.stream_dsp)

    @cached_property
    def order(self) -> order.AsyncOrderResourceWithStreamingResponse:
        from .resources.order import AsyncOrderResourceWithStreamingResponse

        return AsyncOrderResourceWithStreamingResponse(self._client.order)


Client = JennaStreamOrders

AsyncClient = AsyncJennaStreamOrders
