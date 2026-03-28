from __future__ import annotations

from typing import Any
from typing_extensions import override

from ._proxy import LazyProxy


class ResourcesProxy(LazyProxy[Any]):
    """A proxy for the `jenna_stream_orders.resources` module.

    This is used so that we can lazily import `jenna_stream_orders.resources` only when
    needed *and* so that users can just import `jenna_stream_orders` and reference `jenna_stream_orders.resources`
    """

    @override
    def __load__(self) -> Any:
        import importlib

        mod = importlib.import_module("jenna_stream_orders.resources")
        return mod


resources = ResourcesProxy().__as_proxied__()
