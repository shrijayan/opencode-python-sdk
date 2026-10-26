# File generated from our OpenAPI spec by Ferrule. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Literal, Required, TypedDict

__all__ = ["VoiceWebRTCTransportInput"]


class VoiceWebRTCTransportInput(  # type: ignore[call-arg]
    TypedDict,
    total=False,
    extra_items=object,  # pyright: ignore[reportGeneralTypeIssues]
):
    sdp: Required[str]

    type: Required[Literal["webrtc"]]

    dcid: Union[Literal["Infinity", "-Infinity", "NaN"], float, None]
