"""Request encoding: query strings, path segments and JSON bodies.

The rules match the official TypeScript client so both send byte-identical requests:

- ``None`` becomes the string ``"null"``; ``NOT_GIVEN`` leaves the parameter out;
- booleans become ``"true"`` / ``"false"``;
- lists repeat the key once per item;
- objects use deep-object style, ``location[directory]=/repo``.
"""

from __future__ import annotations

import base64
import datetime as dt
import enum
from collections.abc import Mapping, Sequence
from typing import Any
from urllib.parse import quote

import pydantic

from ._types import NotGiven

__all__ = ["encode_path", "encode_path_segment", "encode_query", "to_jsonable"]


def encode_query(params: Mapping[str, object]) -> list[tuple[str, str]]:
    """Flattens query parameters into ordered ``(key, value)`` pairs."""
    pairs: list[tuple[str, str]] = []
    for key, value in params.items():
        _append(pairs, key, to_jsonable(value))
    return pairs


def _append(pairs: list[tuple[str, str]], key: str, value: object) -> None:
    if isinstance(value, NotGiven):
        return
    if value is None:
        pairs.append((key, "null"))
    elif isinstance(value, bool):
        pairs.append((key, "true" if value else "false"))
    elif isinstance(value, (list, tuple)):
        for item in value:  # pyright: ignore[reportUnknownVariableType]
            _append(pairs, key, item)
    elif isinstance(value, dict):
        for child, item in value.items():  # pyright: ignore[reportUnknownVariableType]
            _append(pairs, f"{key}[{child}]", item)
    else:
        pairs.append((key, str(value)))


def encode_path_segment(value: object) -> str:
    """Encodes one path parameter, escaping ``/`` and every other reserved character."""
    return quote(str(value), safe="")


def encode_path(value: str) -> str:
    """Encodes a trailing wildcard path, keeping ``/`` separators."""
    return "/".join(quote(part, safe="") for part in value.split("/"))


def to_jsonable(value: Any) -> Any:
    """Converts models and standard containers to plain JSON values, dropping ``NOT_GIVEN`` entries."""
    if isinstance(value, pydantic.BaseModel):
        return value.model_dump(mode="json", by_alias=True, exclude_unset=True)
    if isinstance(value, NotGiven) or value is None or isinstance(value, (str, int, float, bool)):
        return value
    if isinstance(value, Mapping):
        return {
            str(key): to_jsonable(item)  # pyright: ignore[reportUnknownArgumentType]
            for key, item in value.items()  # pyright: ignore[reportUnknownVariableType]
            if not isinstance(item, NotGiven)
        }
    if isinstance(value, (bytes, bytearray, memoryview)):
        return base64.b64encode(bytes(value)).decode("ascii")
    if isinstance(value, Sequence):
        return [to_jsonable(item) for item in value]  # pyright: ignore[reportUnknownVariableType]
    if isinstance(value, (set, frozenset)):
        return [to_jsonable(item) for item in value]  # pyright: ignore[reportUnknownVariableType]
    if isinstance(value, enum.Enum):
        return to_jsonable(value.value)
    if isinstance(value, (dt.datetime, dt.date)):
        return value.isoformat()
    return pydantic.TypeAdapter(type(value)).dump_python(value, mode="json", by_alias=True)
