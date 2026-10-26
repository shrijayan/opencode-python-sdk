# File generated from our OpenAPI spec by Ferrule. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["SavedUpdateParams"]


class SavedUpdateParams(TypedDict, total=False):
    action: Optional[str]

    resource: Optional[str]
