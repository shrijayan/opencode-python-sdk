# File generated from our OpenAPI spec by Ferrule. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union
from typing_extensions import Required, Annotated, TypeAlias, TypedDict

from ..._utils import PropertyInfo

__all__ = ["PersistentPtyUpdateParams", "Size"]


class PersistentPtyUpdateParams(TypedDict, total=False):
    size: Required[Size]

    attachment_id: Annotated[str, PropertyInfo(alias="attachmentID")]


class SizeTyped(TypedDict, total=False):
    cols: Required[int]

    rows: Required[int]


Size: TypeAlias = Union[SizeTyped, Dict[str, object]]
