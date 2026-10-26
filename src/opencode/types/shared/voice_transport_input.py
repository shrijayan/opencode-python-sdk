# File generated from our OpenAPI spec by Ferrule. See CONTRIBUTING.md for details.

from typing import Union
from typing_extensions import TypeAlias

from .voice_web_rtc_transport_input import VoiceWebRTCTransportInput
from .voice_web_socket_transport_input import VoiceWebSocketTransportInput

__all__ = ["VoiceTransportInput"]

VoiceTransportInput: TypeAlias = Union[VoiceWebRTCTransportInput, VoiceWebSocketTransportInput]
