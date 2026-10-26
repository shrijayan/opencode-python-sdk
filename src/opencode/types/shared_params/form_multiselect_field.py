# File generated from our OpenAPI spec by Ferrule. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo
from .form_when import FormWhen
from .form_option import FormOption

__all__ = ["FormMultiselectField"]


class FormMultiselectField(  # type: ignore[call-arg]
    TypedDict,
    total=False,
    extra_items=object,  # pyright: ignore[reportGeneralTypeIssues]
):
    key: Required[str]

    options: Required[Iterable[FormOption]]

    type: Required[Literal["multiselect"]]

    custom: bool

    default: SequenceNotStr[str]

    description: str

    hidden: bool

    max_items: Annotated[int, PropertyInfo(alias="maxItems")]

    min_items: Annotated[int, PropertyInfo(alias="minItems")]

    required: bool

    title: str

    when: Iterable[FormWhen]
