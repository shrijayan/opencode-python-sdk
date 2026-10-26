# File generated from our OpenAPI spec by Ferrule. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .shared.agent_id import AgentID

__all__ = ["SessionSwitchAgentParams"]


class SessionSwitchAgentParams(TypedDict, total=False):
    agent: Required[AgentID]
