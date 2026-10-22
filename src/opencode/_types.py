"""Shared typing helpers used by the client and the generated code."""

from __future__ import annotations

from collections.abc import Mapping
from typing import Annotated, Any, Final, Literal, TypeAlias, TypeVar

import httpx
import pydantic
from typing_extensions import override

__all__ = [
    "NOT_GIVEN",
    "Body",
    "Headers",
    "NotGiven",
    "OpenEnum",
    "Query",
    "Timeout",
]

_T = TypeVar("_T")


class NotGiven:
    """Marks an argument that was not passed, as opposed to one passed as ``None``.

    The OpenCode API distinguishes a field that is absent from a field set to ``null``, so optional
    arguments default to ``NOT_GIVEN`` and are left out of the request entirely.
    """

    _instance: NotGiven | None = None

    def __new__(cls) -> NotGiven:
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __bool__(self) -> Literal[False]:
        return False

    @override
    def __repr__(self) -> str:
        return "NOT_GIVEN"

    @override
    def __reduce__(self) -> str:
        return "NOT_GIVEN"


NOT_GIVEN: Final = NotGiven()

Headers: TypeAlias = Mapping[str, str | NotGiven]
"""Extra request headers. A ``NOT_GIVEN`` value removes a header the client would otherwise send."""

Query: TypeAlias = Mapping[str, object]
"""Extra query parameters, encoded the same way as generated parameters."""

Body: TypeAlias = Mapping[str, object]
"""Extra JSON body fields, merged over the generated body."""

Timeout: TypeAlias = float | httpx.Timeout | None
"""A timeout in seconds, an ``httpx.Timeout``, or ``None`` to wait forever."""


def _accept_unknown_value(value: Any, handler: pydantic.ValidatorFunctionWrapHandler) -> Any:
    try:
        return handler(value)
    except pydantic.ValidationError:
        # Newer servers may add enum members. Keep the raw value instead of failing the whole response.
        if isinstance(value, (str, int, float, bool)):
            return value
        raise


OpenEnum = Annotated[_T, pydantic.WrapValidator(_accept_unknown_value)]
"""A ``Literal`` enum that type-checks strictly but accepts values added by newer servers at runtime."""
