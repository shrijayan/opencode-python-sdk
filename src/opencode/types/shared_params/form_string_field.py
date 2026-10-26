# File generated from our OpenAPI spec by Ferrule. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo
from .form_when import FormWhen
from .form_option import FormOption

__all__ = ["FormStringField"]


class FormStringField(  # type: ignore[call-arg]
    TypedDict,
    total=False,
    extra_items=object,  # pyright: ignore[reportGeneralTypeIssues]
):
    key: Required[str]

    type: Required[Literal["string"]]

    custom: bool

    default: str

    description: str

    format: Literal["email", "uri", "date", "date-time"]

    hidden: bool

    max_length: Annotated[int, PropertyInfo(alias="maxLength")]

    min_length: Annotated[int, PropertyInfo(alias="minLength")]

    options: Iterable[FormOption]

    pattern: str

    placeholder: str

    required: bool

    title: str

    when: Iterable[FormWhen]
