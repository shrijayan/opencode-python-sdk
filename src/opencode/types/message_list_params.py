# File generated from our OpenAPI spec by Ferrule. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, TypedDict

__all__ = ["MessageListParams"]


class MessageListParams(TypedDict, total=False):
    cursor: Optional[str]

    limit: Optional[int]
    """Maximum number of messages to return.

    When omitted, the endpoint returns its default page size.
    """

    order: Optional[Literal["asc", "desc"]]
    """Message order for the first page.

    Use desc for newest first or asc for oldest first.
    """

    type: Optional[
        Literal[
            "agent-switched",
            "model-switched",
            "location-switched",
            "user",
            "synthetic",
            "system",
            "skill",
            "shell",
            "assistant",
            "compaction",
            "idle",
        ]
    ]
    """Filter by message type before pagination.

    When omitted, all message types are returned. Pass the same type when following
    cursors.
    """
