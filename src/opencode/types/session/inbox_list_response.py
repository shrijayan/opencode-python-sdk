# File generated from our OpenAPI spec by Ferrule. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from ..shared.session_inbox_info import SessionInboxInfo

__all__ = ["InboxListResponse"]

InboxListResponse: TypeAlias = List[SessionInboxInfo]
