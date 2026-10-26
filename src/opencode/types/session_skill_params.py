# File generated from our OpenAPI spec by Ferrule. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

from .shared_params.skill_id import SkillID

__all__ = ["SessionSkillParams"]


class SessionSkillParams(TypedDict, total=False):
    id: Required[SkillID]

    resume: Optional[bool]
