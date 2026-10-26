# File generated from our OpenAPI spec by Ferrule. See CONTRIBUTING.md for details.

from typing import Union
from typing_extensions import TypeAlias

from .voice_web_rtc_transport import VoiceWebRTCTransport
from .voice_web_socket_transport import VoiceWebSocketTransport

__all__ = ["VoiceTransport"]

VoiceTransport: TypeAlias = Union[VoiceWebRTCTransport, VoiceWebSocketTransport]
