"""Runtime support for discriminated unions in the generated models."""

from __future__ import annotations

import re
from typing import TYPE_CHECKING, Any, cast

if TYPE_CHECKING:
    from collections.abc import Callable, Iterable

__all__ = ["UNKNOWN_TAG", "discriminator"]

UNKNOWN_TAG = "__unknown__"
"""Tag of the fallback member that receives variants this client version does not know."""


def discriminator(
    key: str,
    attribute: str,
    tags: Iterable[str],
    patterns: Iterable[tuple[str, str]] = (),
) -> Callable[[Any], str]:
    """Builds a ``pydantic.Discriminator`` function.

    ``key`` is the wire field and ``attribute`` the model attribute that hold the tag. The tag selects a member by
    exact value, then by regular expression. Anything else selects the ``UNKNOWN_TAG`` member, so a newer server can
    add variants without breaking older clients.
    """
    known = frozenset(tags)
    compiled = [(re.compile(pattern), member) for pattern, member in patterns]

    def select(value: Any) -> str:
        tag: object = (
            cast("dict[str, Any]", value).get(key) if isinstance(value, dict) else getattr(value, attribute, None)
        )
        if isinstance(tag, bool):
            tag = "true" if tag else "false"
        if isinstance(tag, str):
            if tag in known:
                return tag
            for pattern, member in compiled:
                if pattern.search(tag):
                    return member
        return UNKNOWN_TAG

    return select
