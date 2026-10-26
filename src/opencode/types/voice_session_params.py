# File generated from our OpenAPI spec by Ferrule. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Required, TypedDict

from .shared_params.voice_transport_input import VoiceTransportInput

__all__ = ["VoiceSessionParams"]


class VoiceSessionParams(TypedDict, total=False):
    model: Required[str]

    transport: Required[VoiceTransportInput]

    session: Optional[Dict[str, object]]
