# File generated from our OpenAPI spec by Ferrule. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Literal, Required, TypedDict

from ..._types import SequenceNotStr
from .mcp_protocol import McpProtocol

__all__ = ["McpLocalConfig", "Timeout"]


class Timeout(  # type: ignore[call-arg]
    TypedDict,
    total=False,
    extra_items=object,  # pyright: ignore[reportGeneralTypeIssues]
):
    catalog: int

    execution: int

    startup: int


class McpLocalConfig(  # type: ignore[call-arg]
    TypedDict,
    total=False,
    extra_items=object,  # pyright: ignore[reportGeneralTypeIssues]
):
    command: Required[SequenceNotStr[str]]

    type: Required[Literal["local"]]

    codemode: bool

    cwd: str

    disabled: bool

    environment: Dict[str, str]

    protocol: McpProtocol
    """MCP protocol negotiation.

    "legacy" (default) opens with the initialize handshake and speaks protocol
    revisions up to 2025-11-25. "auto" probes for the 2026-07-28 revision and falls
    back to legacy when the server does not support it. "2026-07-28" requires that
    revision and fails otherwise.
    """

    timeout: Timeout
