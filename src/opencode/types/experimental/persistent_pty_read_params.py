# File generated from our OpenAPI spec by Ferrule. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

from ..shared.persistent_pty_read_lines import PersistentPtyReadLines

__all__ = ["PersistentPtyReadParams"]


class PersistentPtyReadParams(TypedDict, total=False):
    lines: Optional[PersistentPtyReadLines]
