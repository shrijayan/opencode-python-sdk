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
from typing import Any, cast
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
        for item in cast("Sequence[object]", value):
            _append(pairs, key, item)
    elif isinstance(value, dict):
        for child, item in cast("dict[str, object]", value).items():
            _append(pairs, f"{key}[{child}]", item)
    else:
        pairs.append((key, str(value)))


def encode_path_segment(value: object) -> str:
    """Encodes one path parameter, escaping ``/`` and every other reserved character.

    ``.`` and ``..`` are percent-encoded too, so URL normalization cannot turn a parameter into a different route.
    """
    text = str(value)
    if text == "":
        raise ValueError("Path parameters must not be empty")
    return _encode_part(text)


def encode_path(value: str) -> str:
    """Encodes a trailing wildcard path, keeping ``/`` separators and encoding dot segments."""
    return "/".join(_encode_part(part) for part in value.split("/"))


def _encode_part(part: str) -> str:
    if part in (".", ".."):
        return part.replace(".", "%2E")
    return quote(part, safe="")


def to_jsonable(value: Any) -> Any:
    """Converts models and standard containers to plain JSON values, dropping ``NOT_GIVEN`` entries."""
    if isinstance(value, pydantic.BaseModel):
        return value.model_dump(mode="json", by_alias=True, exclude_unset=True)
    if isinstance(value, NotGiven) or value is None or isinstance(value, (str, int, float, bool)):
        return value
    if isinstance(value, Mapping):
        mapping = cast("Mapping[object, object]", value)
        return {str(key): to_jsonable(item) for key, item in mapping.items() if not isinstance(item, NotGiven)}
    if isinstance(value, (bytes, bytearray, memoryview)):
        return base64.b64encode(bytes(cast("bytes", value))).decode("ascii")
    if isinstance(value, Sequence):
        return [to_jsonable(item) for item in cast("Sequence[object]", value)]
    if isinstance(value, (set, frozenset)):
        return [to_jsonable(item) for item in cast("set[object]", value)]
    if isinstance(value, enum.Enum):
        return to_jsonable(value.value)
    if isinstance(value, (dt.datetime, dt.date)):
        return value.isoformat()
    value_type: Any = value.__class__
    adapter: pydantic.TypeAdapter[Any] = pydantic.TypeAdapter(value_type)
    return adapter.dump_python(value, mode="json", by_alias=True)
