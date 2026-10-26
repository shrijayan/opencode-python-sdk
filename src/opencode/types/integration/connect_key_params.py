# File generated from our OpenAPI spec by Ferrule. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Optional
from typing_extensions import Required, TypeAlias, TypedDict

from ..shared_params.form_answer import FormAnswer

__all__ = ["ConnectKeyParams", "Location"]


class ConnectKeyParams(TypedDict, total=False):
    key: Required[str]

    answer: Optional[FormAnswer]

    label: Optional[str]

    location: Optional[Location]


class LocationTyped(TypedDict, total=False):
    directory: Optional[str]


Location: TypeAlias = Union[LocationTyped, Dict[str, object]]
