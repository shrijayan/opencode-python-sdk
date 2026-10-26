# File generated from our OpenAPI spec by Ferrule. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["FileDiffInfo"]


class FileDiffInfo(  # type: ignore[call-arg]
    TypedDict,
    total=False,
    extra_items=object,  # pyright: ignore[reportGeneralTypeIssues]
):
    additions: Required[int]

    deletions: Required[int]

    file: Required[str]

    patch: Required[str]

    status: Required[Literal["added", "deleted", "modified"]]
