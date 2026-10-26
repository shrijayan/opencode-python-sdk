"""``client.wait_until_ready``: poll until agents and MCP servers have loaded.

OpenCode loads agents and connects MCP servers in the background after it starts listening, so a freshly booted
server can answer requests before the agent a caller needs exists.
"""

from __future__ import annotations

import time
from typing import TYPE_CHECKING

import anyio

from .._errors import ServiceUnavailableError
from .._exceptions import APIConnectionError

if TYPE_CHECKING:
    from collections.abc import Iterable

    from ..types import McpListResponse, AgentListResponse
    from ._client import Opencode, AsyncOpencode

__all__ = ["POLL_INTERVAL", "async_wait_until_ready", "wait_until_ready"]

POLL_INTERVAL = 0.25
"""Seconds between polls."""

_TRANSIENT = (APIConnectionError, ServiceUnavailableError)


def _missing(
    agents: frozenset[str],
    mcp_servers: frozenset[str],
    agent_list: AgentListResponse | None,
    mcp_list: McpListResponse | None,
) -> list[str]:
    missing: list[str] = []
    if agents:
        present = {agent.id for agent in agent_list.data} if agent_list is not None else set[str]()
        missing += [f"agent {name!r}" for name in sorted(agents - present)]
    if mcp_servers:
        connected = (
            {server.name for server in mcp_list.data if server.status.status == "connected"}
            if mcp_list is not None
            else set[str]()
        )
        missing += [f"MCP server {name!r}" for name in sorted(mcp_servers - connected)]
    return missing


def wait_until_ready(
    client: Opencode, *, agents: Iterable[str] = (), mcp_servers: Iterable[str] = (), timeout: float = 60
) -> None:
    wanted_agents, wanted_mcp = frozenset(agents), frozenset(mcp_servers)
    deadline = time.monotonic() + timeout
    while True:
        agent_list = mcp_list = None
        missing = ["server"]
        try:
            client.server.info()
            agent_list = client.agent.list() if wanted_agents else None
            mcp_list = client.mcp.list() if wanted_mcp else None
            missing = _missing(wanted_agents, wanted_mcp, agent_list, mcp_list)
        except _TRANSIENT:
            pass
        if not missing:
            return
        if time.monotonic() >= deadline:
            raise TimeoutError(f"OpenCode not ready after {timeout}s; still waiting for {', '.join(missing)}")
        time.sleep(POLL_INTERVAL)


async def async_wait_until_ready(
    client: AsyncOpencode, *, agents: Iterable[str] = (), mcp_servers: Iterable[str] = (), timeout: float = 60
) -> None:
    wanted_agents, wanted_mcp = frozenset(agents), frozenset(mcp_servers)
    deadline = time.monotonic() + timeout
    while True:
        agent_list = mcp_list = None
        missing = ["server"]
        try:
            await client.server.info()
            agent_list = await client.agent.list() if wanted_agents else None
            mcp_list = await client.mcp.list() if wanted_mcp else None
            missing = _missing(wanted_agents, wanted_mcp, agent_list, mcp_list)
        except _TRANSIENT:
            pass
        if not missing:
            return
        if time.monotonic() >= deadline:
            raise TimeoutError(f"OpenCode not ready after {timeout}s; still waiting for {', '.join(missing)}")
        await anyio.sleep(POLL_INTERVAL)
