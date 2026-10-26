# File generated from our OpenAPI spec by Ferrule. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union
from typing_extensions import Required, TypeAlias, TypedDict

from ..._types import SequenceNotStr

__all__ = ["PersistentPtyCreateParams", "Size"]


class PersistentPtyCreateParams(TypedDict, total=False):
    args: Required[SequenceNotStr[str]]

    env: Required[Dict[str, str]]

    title: Required[str]

    command: str

    cwd: str

    size: Size


class SizeTyped(TypedDict, total=False):
    cols: Required[int]

    rows: Required[int]


Size: TypeAlias = Union[SizeTyped, Dict[str, object]]
