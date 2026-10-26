# File generated from our OpenAPI spec by Ferrule. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .shared.model_ref import ModelRef

__all__ = ["SessionSwitchModelParams"]


class SessionSwitchModelParams(TypedDict, total=False):
    model: Required[ModelRef]
