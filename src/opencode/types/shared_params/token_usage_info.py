# File generated from our OpenAPI spec by Ferrule. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["TokenUsageInfo", "Cache"]


class Cache(  # type: ignore[call-arg]
    TypedDict,
    total=False,
    extra_items=object,  # pyright: ignore[reportGeneralTypeIssues]
):
    read: Required[float]

    write: Required[float]


class TokenUsageInfo(  # type: ignore[call-arg]
    TypedDict,
    total=False,
    extra_items=object,  # pyright: ignore[reportGeneralTypeIssues]
):
    cache: Required[Cache]

    input: Required[float]

    output: Required[float]

    reasoning: Required[float]
