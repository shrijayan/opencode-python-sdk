# File generated from our OpenAPI spec by Ferrule. See CONTRIBUTING.md for details.

from typing import List, Union
from typing_extensions import Literal, TypeAlias

__all__ = ["FormValue"]

FormValue: TypeAlias = Union[Literal["Infinity", "-Infinity", "NaN"], str, float, bool, List[str]]
