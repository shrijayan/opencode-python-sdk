"""Helpers the hand-written modules share, moved here from the SDK's former runtime.

Ferrule's runtime replaced ``_base_client``, ``_exceptions``, ``_qs`` and ``_constants``; what the
RPC, PTY, server and service modules still need from them lives here, in ``lib/`` where custom
code is never regenerated.
"""

from __future__ import annotations

import base64
import datetime as dt
import enum
import functools
from collections.abc import Mapping, Sequence
from typing import Any, Union, cast
from urllib.parse import quote

import httpx
import pydantic

from .._types import NotGiven, Omit

__all__ = [
    "DEFAULT_USERNAME",
    "Timeout",
    "encode_path",
    "encode_path_segment",
    "encode_query",
    "to_jsonable",
    "type_adapter",
    "validation_summary",
]

DEFAULT_USERNAME = "opencode"
"""The Basic auth user name the OpenCode server expects."""

Timeout = Union[float, httpx.Timeout, None]
"""A timeout in seconds, an ``httpx.Timeout``, or ``None`` for none."""


@functools.cache
def _cached_adapter(tp: Any) -> pydantic.TypeAdapter[Any]:
    return pydantic.TypeAdapter(tp)


def type_adapter(tp: Any) -> pydantic.TypeAdapter[Any]:
    """Returns a cached ``TypeAdapter`` for ``tp``."""
    try:
        return _cached_adapter(tp)
    except TypeError:  # unhashable type expression
        return pydantic.TypeAdapter(tp)


def validation_summary(error: pydantic.ValidationError, limit: int = 5) -> str:
    """Describes a validation failure by location and reason only, never echoing response values."""
    issues = error.errors(include_input=False, include_url=False)
    parts = [f"{'.'.join(str(item) for item in issue['loc']) or '<root>'}: {issue['msg']}" for issue in issues[:limit]]
    more = f" (+{len(issues) - limit} more)" if len(issues) > limit else ""
    return f"Response did not match the expected schema: {'; '.join(parts)}{more}"


def encode_query(params: Mapping[str, object]) -> list[tuple[str, str]]:
    """Flattens query parameters into ordered ``(key, value)`` pairs."""
    pairs: list[tuple[str, str]] = []
    for key, value in params.items():
        _append(pairs, key, to_jsonable(value))
    return pairs


def _append(pairs: list[tuple[str, str]], key: str, value: object) -> None:
    if isinstance(value, (NotGiven, Omit)):
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
    if isinstance(value, (NotGiven, Omit)) or value is None or isinstance(value, (str, int, float, bool)):
        return value
    if isinstance(value, Mapping):
        mapping = cast("Mapping[object, object]", value)
        return {str(key): to_jsonable(item) for key, item in mapping.items() if not isinstance(item, (NotGiven, Omit))}
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
