# File generated from our OpenAPI spec by Ferrule. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["SessionGenerateParams"]


class SessionGenerateParams(TypedDict, total=False):
    prompt: Required[str]
