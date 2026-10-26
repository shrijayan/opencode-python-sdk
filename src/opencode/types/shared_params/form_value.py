# File generated from our OpenAPI spec by Ferrule. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Literal, TypeAlias

from ..._types import SequenceNotStr

__all__ = ["FormValue"]

FormValue: TypeAlias = Union[Literal["Infinity", "-Infinity", "NaN"], str, float, bool, SequenceNotStr[str]]
