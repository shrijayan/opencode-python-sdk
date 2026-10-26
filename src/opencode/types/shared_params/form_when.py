# File generated from our OpenAPI spec by Ferrule. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Literal, Required, TypedDict

__all__ = ["FormWhen"]


class FormWhen(  # type: ignore[call-arg]
    TypedDict,
    total=False,
    extra_items=object,  # pyright: ignore[reportGeneralTypeIssues]
):
    key: Required[str]

    op: Required[Literal["eq", "neq"]]

    value: Required[Union[Literal["Infinity", "-Infinity", "NaN"], str, float, bool]]
