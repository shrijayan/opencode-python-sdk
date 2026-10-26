# File generated from our OpenAPI spec by Ferrule. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .prompt_mention import PromptMention

__all__ = ["PromptInputFileAttachment"]


class PromptInputFileAttachment(  # type: ignore[call-arg]
    TypedDict,
    total=False,
    extra_items=object,  # pyright: ignore[reportGeneralTypeIssues]
):
    uri: Required[str]

    description: str

    mention: PromptMention

    name: str
