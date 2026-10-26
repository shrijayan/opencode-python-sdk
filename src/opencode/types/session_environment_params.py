# File generated from our OpenAPI spec by Ferrule. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Required, TypedDict

__all__ = ["SessionEnvironmentParams"]


class SessionEnvironmentParams(TypedDict, total=False):
    variables: Required[Dict[str, str]]
