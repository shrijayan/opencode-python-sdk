# File generated from our OpenAPI spec by Ferrule. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from .mcp_protocol import McpProtocol
from .mcp_o_auth_config import McpOAuthConfig

__all__ = ["McpRemoteConfig", "Oauth", "Timeout"]

Oauth: TypeAlias = Union[Literal[False], McpOAuthConfig]


class Timeout(  # type: ignore[call-arg]
    TypedDict,
    total=False,
    extra_items=object,  # pyright: ignore[reportGeneralTypeIssues]
):
    catalog: int

    execution: int

    startup: int


class McpRemoteConfig(  # type: ignore[call-arg]
    TypedDict,
    total=False,
    extra_items=object,  # pyright: ignore[reportGeneralTypeIssues]
):
    type: Required[Literal["remote"]]

    url: Required[str]

    codemode: bool

    disabled: bool

    headers: Dict[str, str]

    oauth: Oauth

    protocol: McpProtocol
    """MCP protocol negotiation.

    "legacy" (default) opens with the initialize handshake and speaks protocol
    revisions up to 2025-11-25. "auto" probes for the 2026-07-28 revision and falls
    back to legacy when the server does not support it. "2026-07-28" requires that
    revision and fails otherwise.
    """

    timeout: Timeout
