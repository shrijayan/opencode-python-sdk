# File generated from our OpenAPI spec by Ferrule. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .skill_id import SkillID
from .prompt_mention import PromptMention

__all__ = ["PromptInputSkillAttachment"]


class PromptInputSkillAttachment(  # type: ignore[call-arg]
    TypedDict,
    total=False,
    extra_items=object,  # pyright: ignore[reportGeneralTypeIssues]
):
    id: Required[SkillID]

    mention: PromptMention
