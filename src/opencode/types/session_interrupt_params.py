# File generated from our OpenAPI spec by Ferrule. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["SessionInterruptParams"]


class SessionInterruptParams(TypedDict, total=False):
    resume: Optional[bool]
