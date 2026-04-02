# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["CustomerParam"]


class CustomerParam(TypedDict, total=False):
    id: Required[str]
    """A unique id of the customer within the order"""

    email: Required[str]

    name: Required[str]
    """The full name of the customer"""

    phone: Required[str]
    """The customer phone number in E.164 format (e.g. '+14155552671')"""

    masked_phone_code: str
    """
    If you use a phone number masking service, this is the code to reach the
    customer.
    """
