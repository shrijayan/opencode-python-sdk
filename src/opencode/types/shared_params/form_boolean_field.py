# File generated from our OpenAPI spec by Ferrule. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, Required, TypedDict

from .form_when import FormWhen

__all__ = ["FormBooleanField"]


class FormBooleanField(  # type: ignore[call-arg]
    TypedDict,
    total=False,
    extra_items=object,  # pyright: ignore[reportGeneralTypeIssues]
):
    key: Required[str]

    type: Required[Literal["boolean"]]

    default: bool

    description: str

    hidden: bool

    required: bool

    title: str

    when: Iterable[FormWhen]
