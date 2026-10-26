# File generated from our OpenAPI spec by Ferrule. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

from .shared.model_ref import ModelRef

__all__ = ["GenerateTextParams"]


class GenerateTextParams(TypedDict, total=False):
    prompt: Required[str]

    model: Optional[ModelRef]
