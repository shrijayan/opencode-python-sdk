# File generated from our OpenAPI spec by Ferrule. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from typing_extensions import Literal, Required, TypedDict

from .form_when import FormWhen

__all__ = ["FormIntegerField"]


class FormIntegerField(  # type: ignore[call-arg]
    TypedDict,
    total=False,
    extra_items=object,  # pyright: ignore[reportGeneralTypeIssues]
):
    key: Required[str]

    type: Required[Literal["integer"]]

    default: Union[Literal["Infinity", "-Infinity", "NaN"], float]

    description: str

    hidden: bool

    maximum: Union[Literal["Infinity", "-Infinity", "NaN"], float]

    minimum: Union[Literal["Infinity", "-Infinity", "NaN"], float]

    required: bool

    title: str

    when: Iterable[FormWhen]
