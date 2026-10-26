"""``client.session.run``: create or reuse a session, prompt it, wait until idle, and collect the result.

The generated ``SessionResource`` / ``AsyncSessionResource`` inherit from the classes here (see
``codegen/render.py``, ``HELPER_BASES``), so these methods sit next to the generated ones.
"""

from __future__ import annotations

import contextlib
from typing import TYPE_CHECKING, cast
from dataclasses import field, dataclass

import anyio

from .._types import NOT_GIVEN, Timeout, NotGiven
from .._resource import SyncAPIResource, AsyncAPIResource

if TYPE_CHECKING:
    from collections.abc import Sequence

    from ..types import (
        AgentID,
        ModelRef,
        SessionID,
        SessionInfo,
        TokenUsageInfo,
        SessionMessageInfo,
        SessionStructuredError,
        SessionMessageAssistant,
        PromptInputFileAttachment,
    )
    from ..resources.session import SessionResource, AsyncSessionResource

__all__ = ["AsyncSessionHelpers", "RunResult", "SessionHelpers"]


@dataclass
class RunResult:
    """What :meth:`SessionHelpers.run` returns."""

    session: SessionInfo
    """The session as it was after the run. ``session.cost`` and ``session.tokens`` cover the whole session."""
    messages: list[SessionMessageInfo] = field(default_factory=list)  # pyright: ignore[reportUnknownVariableType]
    """Messages this run added, oldest first, starting with the prompt."""

    @property
    def assistant_messages(self) -> list[SessionMessageAssistant]:
        """The assistant messages of this run, oldest first."""
        from ..types import SessionMessageAssistant

        return [message for message in self.messages if isinstance(message, SessionMessageAssistant)]

    @property
    def text(self) -> str:
        """Text of the last assistant message, or ``""`` when the agent produced none."""
        from ..types import SessionMessageAssistantText

        for message in reversed(self.assistant_messages):
            parts = [item.text for item in message.content if isinstance(item, SessionMessageAssistantText)]
            if parts:
                return "".join(parts)
        return ""

    @property
    def outcome(self) -> str | None:
        """``succeeded``, ``failed`` or ``interrupted``, from the run's idle marker or the session."""
        from ..types import SessionMessageIdle

        for message in reversed(self.messages):
            if isinstance(message, SessionMessageIdle):
                return message.outcome
        return self.session.outcome

    @property
    def error(self) -> SessionStructuredError | None:
        """Why the run failed, from its idle marker or last assistant message, or ``None``."""
        from ..types import SessionMessageIdle, SessionMessageAssistant

        for message in reversed(self.messages):
            if isinstance(message, (SessionMessageIdle, SessionMessageAssistant)) and message.error is not None:
                return message.error
        return None

    @property
    def cost(self) -> float:
        """Cost of this run in USD, summed over its assistant messages."""
        return sum(message.cost or 0.0 for message in self.assistant_messages)

    @property
    def tokens(self) -> TokenUsageInfo:
        """Token usage of this run, summed over its assistant messages."""
        from ..types import TokenUsageInfo
        from ..types.shared.token_usage_info import Cache as TokenUsageInfoCache

        total = TokenUsageInfo(input=0, output=0, reasoning=0, cache=TokenUsageInfoCache(read=0, write=0))
        for message in self.assistant_messages:
            usage = message.tokens
            if usage is None:
                continue
            total.input += usage.input
            total.output += usage.output
            total.reasoning += usage.reasoning
            total.cache.read += usage.cache.read
            total.cache.write += usage.cache.write
        return total


def _new_messages(newest_first: list[SessionMessageInfo], marker: str | None) -> list[SessionMessageInfo]:
    from ..types import SessionMessageUser

    collected: list[SessionMessageInfo] = []
    for message in newest_first:
        if marker is not None and message.id == marker:
            break
        collected.append(message)
    collected.reverse()
    # Drop anything that was already queued before our prompt.
    for index, message in enumerate(collected):
        if isinstance(message, SessionMessageUser):
            return collected[index:]
    return collected


class SessionHelpers(SyncAPIResource):
    """Hand-written helpers on ``client.session``."""

    def run(
        self,
        text: str,
        *,
        agent: AgentID | None = None,
        model: ModelRef | None = None,
        files: Sequence[PromptInputFileAttachment] | NotGiven = NOT_GIVEN,
        session_id: SessionID | None = None,
        timeout: Timeout = None,
    ) -> RunResult:
        """Runs one prompt to completion and returns what the agent produced.

        Creates a session with ``agent`` and ``model`` (or reuses ``session_id``, switching its agent and model when
        given), sends ``text``, blocks until the session is idle, and reads back the new messages and the session's
        usage.

        If the wait is interrupted (``KeyboardInterrupt``, a timeout, or any other error), the session is
        interrupted on the server before the error propagates, so no agent keeps running unattended.

        Args:
          text: The prompt.
          agent: Agent for a new session, or to switch an existing one to.
          model: Model for a new session, or to switch an existing one to. Set it with ``agent`` so the session
            does not start on another model.
          files: File attachments; images can be ``data:`` URLs.
          session_id: Continue this session instead of creating one.
          timeout: Seconds to wait for the session to become idle. ``None`` waits forever.

        Example::

            result = client.session.run("Summarize README.md", agent="build")
            print(result.text, result.cost)
        """
        resource = cast("SessionResource", self)
        if session_id is None:
            session = resource.create(agent=agent or NOT_GIVEN, model=model or NOT_GIVEN)
            session_id = session.id
            marker = None
        else:
            if agent is not None:
                resource.switch_agent(session_id, agent=agent)
            if model is not None:
                resource.switch_model(session_id, model=model)
            latest = self._client.message.list(session_id, order="desc", limit=1).data
            marker = latest[0].id if latest else None

        resource.prompt(session_id, text=text, files=files)
        try:
            resource.wait(session_id, timeout=timeout)
        except BaseException:
            with contextlib.suppress(Exception):
                resource.interrupt(session_id)
            raise

        newest_first: list[SessionMessageInfo] = []
        for message in self._client.message.list(session_id, order="desc"):
            if marker is not None and message.id == marker:
                break
            newest_first.append(message)
        return RunResult(session=resource.get(session_id), messages=_new_messages(newest_first, marker))


class AsyncSessionHelpers(AsyncAPIResource):
    """Hand-written helpers on ``client.session`` of :class:`opencode.AsyncOpencode`."""

    async def run(
        self,
        text: str,
        *,
        agent: AgentID | None = None,
        model: ModelRef | None = None,
        files: Sequence[PromptInputFileAttachment] | NotGiven = NOT_GIVEN,
        session_id: SessionID | None = None,
        timeout: Timeout = None,
    ) -> RunResult:
        """Runs one prompt to completion. See :meth:`SessionHelpers.run`.

        Cancelling the task interrupts the session on the server before the cancellation propagates.
        """
        resource = cast("AsyncSessionResource", self)
        if session_id is None:
            session = await resource.create(agent=agent or NOT_GIVEN, model=model or NOT_GIVEN)
            session_id = session.id
            marker = None
        else:
            if agent is not None:
                await resource.switch_agent(session_id, agent=agent)
            if model is not None:
                await resource.switch_model(session_id, model=model)
            latest = (await self._client.message.list(session_id, order="desc", limit=1)).data
            marker = latest[0].id if latest else None

        await resource.prompt(session_id, text=text, files=files)
        try:
            await resource.wait(session_id, timeout=timeout)
        except BaseException:
            with anyio.CancelScope(shield=True), contextlib.suppress(Exception):
                await resource.interrupt(session_id)
            raise

        newest_first: list[SessionMessageInfo] = []
        async for message in self._client.message.list(session_id, order="desc"):
            if marker is not None and message.id == marker:
                break
            newest_first.append(message)
        return RunResult(session=await resource.get(session_id), messages=_new_messages(newest_first, marker))
