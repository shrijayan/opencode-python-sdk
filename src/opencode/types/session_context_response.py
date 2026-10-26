# File generated from our OpenAPI spec by Ferrule. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .shared.session_message_info import SessionMessageInfo

__all__ = ["SessionContextResponse"]

SessionContextResponse: TypeAlias = List[SessionMessageInfo]
