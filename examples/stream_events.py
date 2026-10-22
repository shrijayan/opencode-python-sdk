"""Prints every event from a running OpenCode server until interrupted.

Usage: OPENCODE_BASE_URL=http://127.0.0.1:4096 OPENCODE_PASSWORD=... uv run python examples/stream_events.py
"""

from __future__ import annotations

import asyncio

from opencode import AsyncOpencode
from opencode.types import SessionTextDeltaEvent, UnknownEvent


async def main() -> None:
    async with AsyncOpencode() as client, await client.event.subscribe() as events:
        async for event in events:
            if isinstance(event, SessionTextDeltaEvent):
                print(event.data, flush=True)
            elif isinstance(event, UnknownEvent):
                print(f"(new event type from a newer server: {event.type})")
            else:
                print(event.type)


if __name__ == "__main__":
    asyncio.run(main())
