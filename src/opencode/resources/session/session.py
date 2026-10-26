# File generated from our OpenAPI spec by Ferrule. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable, Optional
from typing_extensions import Literal

import httpx

from .form import (
    FormResource,
    AsyncFormResource,
    FormResourceWithRawResponse,
    AsyncFormResourceWithRawResponse,
    FormResourceWithStreamingResponse,
    AsyncFormResourceWithStreamingResponse,
)
from .inbox import (
    InboxResource,
    AsyncInboxResource,
    InboxResourceWithRawResponse,
    AsyncInboxResourceWithRawResponse,
    InboxResourceWithStreamingResponse,
    AsyncInboxResourceWithStreamingResponse,
)
from .revert import (
    RevertResource,
    AsyncRevertResource,
    RevertResourceWithRawResponse,
    AsyncRevertResourceWithRawResponse,
    RevertResourceWithStreamingResponse,
    AsyncRevertResourceWithStreamingResponse,
)
from ...types import (
    session_log_params,
    session_diff_params,
    session_fork_params,
    session_list_params,
    session_move_params,
    session_view_params,
    session_shell_params,
    session_skill_params,
    session_stats_params,
    session_create_params,
    session_export_params,
    session_prompt_params,
    session_update_params,
    session_command_params,
    session_compact_params,
    session_import__params,
    session_generate_params,
    session_interrupt_params,
    session_synthetic_params,
    session_environment_params,
    session_switch_agent_params,
    session_switch_model_params,
)
from .message import (
    MessageResource,
    AsyncMessageResource,
    MessageResourceWithRawResponse,
    AsyncMessageResourceWithRawResponse,
    MessageResourceWithStreamingResponse,
    AsyncMessageResourceWithStreamingResponse,
)
from ..._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
from ..._utils import path_template, maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...pagination import SyncCursorPage, AsyncCursorPage
from ..._base_client import AsyncPaginator, make_request_options
from ...types.shared.agent_id import AgentID
from ...types.shared.skill_id import SkillID
from ...types.shared.event_seq import EventSeq
from ...types.shared.model_ref import ModelRef
from ...types.shared.project_id import ProjectID
from ...types.shared.session_id import SessionID
from .instructions.instructions import (
    InstructionsResource,
    AsyncInstructionsResource,
    InstructionsResourceWithRawResponse,
    AsyncInstructionsResourceWithRawResponse,
    InstructionsResourceWithStreamingResponse,
    AsyncInstructionsResourceWithStreamingResponse,
)
from ...types.shared.session_info import SessionInfo
from ...types.session_get_response import SessionGetResponse
from ...types.shared.absolute_path import AbsolutePath
from ...types.shared.relative_path import RelativePath
from ...types.session_diff_response import SessionDiffResponse
from ...types.session_fork_response import SessionForkResponse
from ...types.session_stats_response import SessionStatsResponse
from ...types.shared.sessions_cursor import SessionsCursor
from ...types.session_active_response import SessionActiveResponse
from ...types.session_create_response import SessionCreateResponse
from ...types.session_export_response import SessionExportResponse
from ...types.session_prompt_response import SessionPromptResponse
from ...types.shared.session_metadata import SessionMetadata
from ...types.session_compact_response import SessionCompactResponse
from ...types.session_context_response import SessionContextResponse
from ...types.session_import__response import SessionImportResponse
from ...types.shared.permission_ruleset import PermissionRuleset
from ...types.shared.session_message_id import SessionMessageID
from ...types.session_synthetic_response import SessionSyntheticResponse
from ...types.shared.location_public_ref import LocationPublicRef
from ...types.shared.session_inbox_delivery import SessionInboxDelivery
from ...types.shared.prompt_agent_attachment import PromptAgentAttachment
from ...types.shared.session_generate_response import SessionGenerateResponse
from ...types.shared.session_interrupt_response import SessionInterruptResponse
from ...types.shared.prompt_input_file_attachment import PromptInputFileAttachment
from ...types.shared.prompt_input_skill_attachment import PromptInputSkillAttachment

__all__ = ["SessionResource", "AsyncSessionResource"]


class SessionResource(SyncAPIResource):
    @cached_property
    def revert(self) -> RevertResource:
        return RevertResource(self._client)

    @cached_property
    def inbox(self) -> InboxResource:
        return InboxResource(self._client)

    @cached_property
    def instructions(self) -> InstructionsResource:
        return InstructionsResource(self._client)

    @cached_property
    def message(self) -> MessageResource:
        return MessageResource(self._client)

    @cached_property
    def form(self) -> FormResource:
        return FormResource(self._client)

    @cached_property
    def with_raw_response(self) -> SessionResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/#accessing-raw-response-data-eg-headers
        """
        return SessionResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SessionResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/#with_streaming_response
        """
        return SessionResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        id: Optional[SessionID] | Omit = omit,
        agent: Optional[AgentID] | Omit = omit,
        location: Optional[LocationPublicRef] | Omit = omit,
        metadata: Optional[SessionMetadata] | Omit = omit,
        model: Optional[ModelRef] | Omit = omit,
        parent_id: Optional[SessionID] | Omit = omit,
        permissions: Optional[PermissionRuleset] | Omit = omit,
        title: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SessionCreateResponse:
        """
        Create a session at the requested location. A parentID creates a linked child
        session at its parent's location.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/session",
            body=maybe_transform(
                {
                    "id": id,
                    "agent": agent,
                    "location": location,
                    "metadata": metadata,
                    "model": model,
                    "parent_id": parent_id,
                    "permissions": permissions,
                    "title": title,
                },
                session_create_params.SessionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SessionCreateResponse,
        )

    def update(
        self,
        session_id: SessionID,
        *,
        archived: Optional[bool] | Omit = omit,
        metadata: Optional[SessionMetadata] | Omit = omit,
        permissions: Optional[PermissionRuleset] | Omit = omit,
        title: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Update mutable session properties.

        Args:
          archived: Archive the session with true or restore it with false. Repeating the current
              state is a no-op.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._patch(
            path_template("/api/session/{session_id}", session_id=session_id),
            body=maybe_transform(
                {
                    "archived": archived,
                    "metadata": metadata,
                    "permissions": permissions,
                    "title": title,
                },
                session_update_params.SessionUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def list(
        self,
        *,
        archived: Optional[bool] | Omit = omit,
        cursor: Optional[SessionsCursor] | Omit = omit,
        directory: Optional[AbsolutePath] | Omit = omit,
        limit: Optional[int] | Omit = omit,
        order: Optional[Literal["asc", "desc"]] | Omit = omit,
        parent_id: Optional[SessionID] | Omit = omit,
        project: Optional[ProjectID] | Omit = omit,
        search: Optional[str] | Omit = omit,
        subpath: Optional[RelativePath] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncCursorPage[SessionInfo]:
        """
        Retrieve sessions in the requested order. Items keep that order across pages;
        use cursor.next or cursor.previous to move through the ordered list.

        Args:
          limit: Maximum number of sessions to return. Defaults to the newest 50 sessions.

          order: Session order for the first page. Use desc for newest first or asc for oldest
              first.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/api/session",
            page=SyncCursorPage[SessionInfo],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "archived": archived,
                        "cursor": cursor,
                        "directory": directory,
                        "limit": limit,
                        "order": order,
                        "parent_id": parent_id,
                        "project": project,
                        "search": search,
                        "subpath": subpath,
                    },
                    session_list_params.SessionListParams,
                ),
            ),
            model=SessionInfo,
        )

    def active(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SessionActiveResponse:
        """
        Retrieve foreground Session drains currently owned by this OpenCode process.
        Sessions absent from the result are inactive.
        """
        return self._get(
            "/api/session/active",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SessionActiveResponse,
        )

    def background(
        self,
        session_id: SessionID,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Move active foreground backgroundable tools for this session into background
        observation. Idle requests are a no-op.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            path_template("/api/session/{session_id}/background", session_id=session_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def command(
        self,
        session_id: SessionID,
        *,
        name: str,
        text: str,
        agents: Iterable[PromptAgentAttachment] | Omit = omit,
        delivery: Optional[SessionInboxDelivery] | Omit = omit,
        files: Iterable[PromptInputFileAttachment] | Omit = omit,
        skills: Iterable[PromptInputSkillAttachment] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Execute a slash command callback immediately.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            path_template("/api/session/{session_id}/command", session_id=session_id),
            body=maybe_transform(
                {
                    "name": name,
                    "text": text,
                    "agents": agents,
                    "delivery": delivery,
                    "files": files,
                    "skills": skills,
                },
                session_command_params.SessionCommandParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def compact(
        self,
        session_id: SessionID,
        *,
        id: Optional[SessionMessageID] | Omit = omit,
        delivery: Optional[SessionInboxDelivery] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SessionCompactResponse:
        """
        Durably admit a session compaction request. Steers by default: it runs at the
        next step boundary instead of waiting behind queued prompts.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        return self._post(
            path_template("/api/session/{session_id}/compact", session_id=session_id),
            body=maybe_transform(
                {
                    "id": id,
                    "delivery": delivery,
                },
                session_compact_params.SessionCompactParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SessionCompactResponse,
        )

    def context(
        self,
        session_id: SessionID,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SessionContextResponse:
        """
        Retrieve the active context messages for a session (all messages after the last
        compaction).

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        return self._get(
            path_template("/api/session/{session_id}/context", session_id=session_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SessionContextResponse,
        )

    def diff(
        self,
        session_id: SessionID,
        *,
        context: Optional[int] | Omit = omit,
        from_: Optional[SessionMessageID] | Omit = omit,
        to: Optional[SessionMessageID] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SessionDiffResponse:
        """
        Structured per-file diffs of the files a turn changed. A turn runs from the
        first prompt after the session was last idle until its next idle marker, so
        prompts steered in while it was busy belong to the same turn; `to` extends the
        range through a later turn. Compares the range's first recorded snapshot with
        its last; a step still running in the active session compares against the
        working copy. Ranges that span a location change are rejected. In sessions
        without any idle marker, a prompt's turn spans until the next user message.

        Args:
          context: Unchanged lines around each hunk. Omit for full-file patches.

          from_: User message whose turn to diff. Defaults to the turn of the newest user
              message.

          to: Later user message whose turn ends the range. Defaults to the turn of `from`
              alone.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        return self._get(
            path_template("/api/session/{session_id}/diff", session_id=session_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "context": context,
                        "from_": from_,
                        "to": to,
                    },
                    session_diff_params.SessionDiffParams,
                ),
            ),
            cast_to=SessionDiffResponse,
        )

    def environment(
        self,
        session_id: SessionID,
        *,
        variables: Dict[str, str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Replace the process environment used by local shell commands for this session.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._put(
            path_template("/api/session/{session_id}/environment", session_id=session_id),
            body=maybe_transform({"variables": variables}, session_environment_params.SessionEnvironmentParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def export(
        self,
        session_id: SessionID,
        *,
        sanitize: Optional[bool] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SessionExportResponse:
        """
        Export a complete projected session transcript.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        return self._get(
            path_template("/api/experimental/session/{session_id}/export", session_id=session_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"sanitize": sanitize}, session_export_params.SessionExportParams),
            ),
            cast_to=SessionExportResponse,
        )

    def fork(
        self,
        session_id: SessionID,
        *,
        before: Optional[SessionMessageID] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SessionForkResponse:
        """
        Create a child session by copying projected history before a message. Omit
        before to copy the full history.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        return self._post(
            path_template("/api/session/{session_id}/fork", session_id=session_id),
            body=maybe_transform({"before": before}, session_fork_params.SessionForkParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SessionForkResponse,
        )

    def generate(
        self,
        session_id: SessionID,
        *,
        prompt: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SessionGenerateResponse:
        """
        Generate transient text from the current session context without mutating
        session history.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        return self._post(
            path_template("/api/session/{session_id}/generate", session_id=session_id),
            body=maybe_transform({"prompt": prompt}, session_generate_params.SessionGenerateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SessionGenerateResponse,
        )

    def get(
        self,
        session_id: SessionID,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SessionGetResponse:
        """
        Retrieve a session by ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        return self._get(
            path_template("/api/session/{session_id}", session_id=session_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SessionGetResponse,
        )

    def import_(
        self,
        *,
        info: SessionInfo,
        messages: Iterable[object],
        location: Optional[LocationPublicRef] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SessionImportResponse:
        """
        Import a projected session transcript at the requested location. Accepts
        transcripts exported by earlier releases. If parentID is supplied, the parent
        session must already exist; import parents before children.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/experimental/session/import",
            body=maybe_transform(
                {
                    "info": info,
                    "messages": messages,
                    "location": location,
                },
                session_import__params.SessionImportParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SessionImportResponse,
        )

    def interrupt(
        self,
        session_id: SessionID,
        *,
        resume: Optional[bool] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SessionInterruptResponse:
        """
        Interrupt active execution owned by this OpenCode process. Returns
        interrupted=true when an active execution was interrupted and false for the idle
        no-op. When resume=true, execution resumes pending steering input and
        next-in-line control items (manual compaction, moves) while queued prompts
        remain parked.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        return self._post(
            path_template("/api/session/{session_id}/interrupt", session_id=session_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"resume": resume}, session_interrupt_params.SessionInterruptParams),
            ),
            cast_to=SessionInterruptResponse,
        )

    def log(
        self,
        session_id: SessionID,
        *,
        after: Optional[EventSeq] | Omit = omit,
        follow: Optional[bool] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Experimental durable session event log. Reads events after an exclusive
        aggregate sequence and continues with live events when follow=true.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._get(
            path_template("/api/experimental/session/{session_id}/log", session_id=session_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after": after,
                        "follow": follow,
                    },
                    session_log_params.SessionLogParams,
                ),
            ),
            cast_to=NoneType,
        )

    def move(
        self,
        session_id: SessionID,
        *,
        directory: AbsolutePath,
        delivery: Optional[SessionInboxDelivery] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Move a session to another project directory at the requested delivery boundary.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            path_template("/api/session/{session_id}/move", session_id=session_id),
            body=maybe_transform(
                {
                    "directory": directory,
                    "delivery": delivery,
                },
                session_move_params.SessionMoveParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def prompt(
        self,
        session_id: SessionID,
        *,
        text: str,
        id: Optional[SessionMessageID] | Omit = omit,
        agents: Iterable[PromptAgentAttachment] | Omit = omit,
        delivery: Optional[SessionInboxDelivery] | Omit = omit,
        files: Iterable[PromptInputFileAttachment] | Omit = omit,
        metadata: Dict[str, object] | Omit = omit,
        resume: Optional[bool] | Omit = omit,
        skills: Iterable[PromptInputSkillAttachment] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SessionPromptResponse:
        """
        Durably admit one session input and schedule agent-loop execution unless resume
        is false.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        return self._post(
            path_template("/api/session/{session_id}/prompt", session_id=session_id),
            body=maybe_transform(
                {
                    "text": text,
                    "id": id,
                    "agents": agents,
                    "delivery": delivery,
                    "files": files,
                    "metadata": metadata,
                    "resume": resume,
                    "skills": skills,
                },
                session_prompt_params.SessionPromptParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SessionPromptResponse,
        )

    def remove(
        self,
        session_id: SessionID,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete a session and its child sessions.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            path_template("/api/session/{session_id}", session_id=session_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def shell(
        self,
        session_id: SessionID,
        *,
        command: str,
        id: Optional[SessionMessageID] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Execute one shell command in the session's working directory. Emits a
        shell.started event before execution and a shell.ended event with the merged
        output after.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            path_template("/api/session/{session_id}/shell", session_id=session_id),
            body=maybe_transform(
                {
                    "command": command,
                    "id": id,
                },
                session_shell_params.SessionShellParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def skill(
        self,
        session_id: SessionID,
        *,
        id: SkillID,
        resume: Optional[bool] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Activate a skill for a session by appending a skill message and resuming
        execution.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            path_template("/api/experimental/session/{session_id}/skill", session_id=session_id),
            body=maybe_transform(
                {
                    "id": id,
                    "resume": resume,
                },
                session_skill_params.SessionSkillParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def stats(
        self,
        *,
        from_: Union[Literal["Infinity", "-Infinity", "NaN"], float, None] | Omit = omit,
        project: Optional[ProjectID] | Omit = omit,
        timezone: Optional[str] | Omit = omit,
        to: Union[Literal["Infinity", "-Infinity", "NaN"], float, None] | Omit = omit,
        tools: Optional[Literal["none", "summary", "detail"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SessionStatsResponse:
        """
        Aggregate local session activity, usage, and tool reliability for a time range.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/api/experimental/session/stats",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "from_": from_,
                        "project": project,
                        "timezone": timezone,
                        "to": to,
                        "tools": tools,
                    },
                    session_stats_params.SessionStatsParams,
                ),
            ),
            cast_to=SessionStatsResponse,
        )

    def switch_agent(
        self,
        session_id: SessionID,
        *,
        agent: AgentID,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Switch the agent used by subsequent provider turns.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            path_template("/api/session/{session_id}/agent", session_id=session_id),
            body=maybe_transform({"agent": agent}, session_switch_agent_params.SessionSwitchAgentParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def switch_model(
        self,
        session_id: SessionID,
        *,
        model: ModelRef,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Switch the model used by subsequent provider turns.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            path_template("/api/session/{session_id}/model", session_id=session_id),
            body=maybe_transform({"model": model}, session_switch_model_params.SessionSwitchModelParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def synthetic(
        self,
        session_id: SessionID,
        *,
        text: str,
        id: Optional[SessionMessageID] | Omit = omit,
        delivery: Optional[SessionInboxDelivery] | Omit = omit,
        description: Optional[str] | Omit = omit,
        metadata: Dict[str, object] | Omit = omit,
        resume: Optional[bool] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SessionSyntheticResponse:
        """
        Durably admit synthetic session input and schedule execution unless resume is
        false.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        return self._post(
            path_template("/api/session/{session_id}/synthetic", session_id=session_id),
            body=maybe_transform(
                {
                    "text": text,
                    "id": id,
                    "delivery": delivery,
                    "description": description,
                    "metadata": metadata,
                    "resume": resume,
                },
                session_synthetic_params.SessionSyntheticParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SessionSyntheticResponse,
        )

    def view(
        self,
        session_id: SessionID,
        *,
        idle: float,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Mark the idle transition observed by the viewer as viewed.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            path_template("/api/session/{session_id}/view", session_id=session_id),
            body=maybe_transform({"idle": idle}, session_view_params.SessionViewParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def wait(
        self,
        session_id: SessionID,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Wait for a session agent loop to become idle.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            path_template("/api/experimental/session/{session_id}/wait", session_id=session_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncSessionResource(AsyncAPIResource):
    @cached_property
    def revert(self) -> AsyncRevertResource:
        return AsyncRevertResource(self._client)

    @cached_property
    def inbox(self) -> AsyncInboxResource:
        return AsyncInboxResource(self._client)

    @cached_property
    def instructions(self) -> AsyncInstructionsResource:
        return AsyncInstructionsResource(self._client)

    @cached_property
    def message(self) -> AsyncMessageResource:
        return AsyncMessageResource(self._client)

    @cached_property
    def form(self) -> AsyncFormResource:
        return AsyncFormResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncSessionResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/#accessing-raw-response-data-eg-headers
        """
        return AsyncSessionResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSessionResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/#with_streaming_response
        """
        return AsyncSessionResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        id: Optional[SessionID] | Omit = omit,
        agent: Optional[AgentID] | Omit = omit,
        location: Optional[LocationPublicRef] | Omit = omit,
        metadata: Optional[SessionMetadata] | Omit = omit,
        model: Optional[ModelRef] | Omit = omit,
        parent_id: Optional[SessionID] | Omit = omit,
        permissions: Optional[PermissionRuleset] | Omit = omit,
        title: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SessionCreateResponse:
        """
        Create a session at the requested location. A parentID creates a linked child
        session at its parent's location.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/session",
            body=await async_maybe_transform(
                {
                    "id": id,
                    "agent": agent,
                    "location": location,
                    "metadata": metadata,
                    "model": model,
                    "parent_id": parent_id,
                    "permissions": permissions,
                    "title": title,
                },
                session_create_params.SessionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SessionCreateResponse,
        )

    async def update(
        self,
        session_id: SessionID,
        *,
        archived: Optional[bool] | Omit = omit,
        metadata: Optional[SessionMetadata] | Omit = omit,
        permissions: Optional[PermissionRuleset] | Omit = omit,
        title: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Update mutable session properties.

        Args:
          archived: Archive the session with true or restore it with false. Repeating the current
              state is a no-op.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._patch(
            path_template("/api/session/{session_id}", session_id=session_id),
            body=await async_maybe_transform(
                {
                    "archived": archived,
                    "metadata": metadata,
                    "permissions": permissions,
                    "title": title,
                },
                session_update_params.SessionUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def list(
        self,
        *,
        archived: Optional[bool] | Omit = omit,
        cursor: Optional[SessionsCursor] | Omit = omit,
        directory: Optional[AbsolutePath] | Omit = omit,
        limit: Optional[int] | Omit = omit,
        order: Optional[Literal["asc", "desc"]] | Omit = omit,
        parent_id: Optional[SessionID] | Omit = omit,
        project: Optional[ProjectID] | Omit = omit,
        search: Optional[str] | Omit = omit,
        subpath: Optional[RelativePath] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[SessionInfo, AsyncCursorPage[SessionInfo]]:
        """
        Retrieve sessions in the requested order. Items keep that order across pages;
        use cursor.next or cursor.previous to move through the ordered list.

        Args:
          limit: Maximum number of sessions to return. Defaults to the newest 50 sessions.

          order: Session order for the first page. Use desc for newest first or asc for oldest
              first.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/api/session",
            page=AsyncCursorPage[SessionInfo],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "archived": archived,
                        "cursor": cursor,
                        "directory": directory,
                        "limit": limit,
                        "order": order,
                        "parent_id": parent_id,
                        "project": project,
                        "search": search,
                        "subpath": subpath,
                    },
                    session_list_params.SessionListParams,
                ),
            ),
            model=SessionInfo,
        )

    async def active(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SessionActiveResponse:
        """
        Retrieve foreground Session drains currently owned by this OpenCode process.
        Sessions absent from the result are inactive.
        """
        return await self._get(
            "/api/session/active",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SessionActiveResponse,
        )

    async def background(
        self,
        session_id: SessionID,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Move active foreground backgroundable tools for this session into background
        observation. Idle requests are a no-op.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            path_template("/api/session/{session_id}/background", session_id=session_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def command(
        self,
        session_id: SessionID,
        *,
        name: str,
        text: str,
        agents: Iterable[PromptAgentAttachment] | Omit = omit,
        delivery: Optional[SessionInboxDelivery] | Omit = omit,
        files: Iterable[PromptInputFileAttachment] | Omit = omit,
        skills: Iterable[PromptInputSkillAttachment] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Execute a slash command callback immediately.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            path_template("/api/session/{session_id}/command", session_id=session_id),
            body=await async_maybe_transform(
                {
                    "name": name,
                    "text": text,
                    "agents": agents,
                    "delivery": delivery,
                    "files": files,
                    "skills": skills,
                },
                session_command_params.SessionCommandParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def compact(
        self,
        session_id: SessionID,
        *,
        id: Optional[SessionMessageID] | Omit = omit,
        delivery: Optional[SessionInboxDelivery] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SessionCompactResponse:
        """
        Durably admit a session compaction request. Steers by default: it runs at the
        next step boundary instead of waiting behind queued prompts.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        return await self._post(
            path_template("/api/session/{session_id}/compact", session_id=session_id),
            body=await async_maybe_transform(
                {
                    "id": id,
                    "delivery": delivery,
                },
                session_compact_params.SessionCompactParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SessionCompactResponse,
        )

    async def context(
        self,
        session_id: SessionID,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SessionContextResponse:
        """
        Retrieve the active context messages for a session (all messages after the last
        compaction).

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        return await self._get(
            path_template("/api/session/{session_id}/context", session_id=session_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SessionContextResponse,
        )

    async def diff(
        self,
        session_id: SessionID,
        *,
        context: Optional[int] | Omit = omit,
        from_: Optional[SessionMessageID] | Omit = omit,
        to: Optional[SessionMessageID] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SessionDiffResponse:
        """
        Structured per-file diffs of the files a turn changed. A turn runs from the
        first prompt after the session was last idle until its next idle marker, so
        prompts steered in while it was busy belong to the same turn; `to` extends the
        range through a later turn. Compares the range's first recorded snapshot with
        its last; a step still running in the active session compares against the
        working copy. Ranges that span a location change are rejected. In sessions
        without any idle marker, a prompt's turn spans until the next user message.

        Args:
          context: Unchanged lines around each hunk. Omit for full-file patches.

          from_: User message whose turn to diff. Defaults to the turn of the newest user
              message.

          to: Later user message whose turn ends the range. Defaults to the turn of `from`
              alone.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        return await self._get(
            path_template("/api/session/{session_id}/diff", session_id=session_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "context": context,
                        "from_": from_,
                        "to": to,
                    },
                    session_diff_params.SessionDiffParams,
                ),
            ),
            cast_to=SessionDiffResponse,
        )

    async def environment(
        self,
        session_id: SessionID,
        *,
        variables: Dict[str, str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Replace the process environment used by local shell commands for this session.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._put(
            path_template("/api/session/{session_id}/environment", session_id=session_id),
            body=await async_maybe_transform(
                {"variables": variables}, session_environment_params.SessionEnvironmentParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def export(
        self,
        session_id: SessionID,
        *,
        sanitize: Optional[bool] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SessionExportResponse:
        """
        Export a complete projected session transcript.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        return await self._get(
            path_template("/api/experimental/session/{session_id}/export", session_id=session_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"sanitize": sanitize}, session_export_params.SessionExportParams),
            ),
            cast_to=SessionExportResponse,
        )

    async def fork(
        self,
        session_id: SessionID,
        *,
        before: Optional[SessionMessageID] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SessionForkResponse:
        """
        Create a child session by copying projected history before a message. Omit
        before to copy the full history.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        return await self._post(
            path_template("/api/session/{session_id}/fork", session_id=session_id),
            body=await async_maybe_transform({"before": before}, session_fork_params.SessionForkParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SessionForkResponse,
        )

    async def generate(
        self,
        session_id: SessionID,
        *,
        prompt: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SessionGenerateResponse:
        """
        Generate transient text from the current session context without mutating
        session history.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        return await self._post(
            path_template("/api/session/{session_id}/generate", session_id=session_id),
            body=await async_maybe_transform({"prompt": prompt}, session_generate_params.SessionGenerateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SessionGenerateResponse,
        )

    async def get(
        self,
        session_id: SessionID,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SessionGetResponse:
        """
        Retrieve a session by ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        return await self._get(
            path_template("/api/session/{session_id}", session_id=session_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SessionGetResponse,
        )

    async def import_(
        self,
        *,
        info: SessionInfo,
        messages: Iterable[object],
        location: Optional[LocationPublicRef] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SessionImportResponse:
        """
        Import a projected session transcript at the requested location. Accepts
        transcripts exported by earlier releases. If parentID is supplied, the parent
        session must already exist; import parents before children.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/experimental/session/import",
            body=await async_maybe_transform(
                {
                    "info": info,
                    "messages": messages,
                    "location": location,
                },
                session_import__params.SessionImportParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SessionImportResponse,
        )

    async def interrupt(
        self,
        session_id: SessionID,
        *,
        resume: Optional[bool] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SessionInterruptResponse:
        """
        Interrupt active execution owned by this OpenCode process. Returns
        interrupted=true when an active execution was interrupted and false for the idle
        no-op. When resume=true, execution resumes pending steering input and
        next-in-line control items (manual compaction, moves) while queued prompts
        remain parked.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        return await self._post(
            path_template("/api/session/{session_id}/interrupt", session_id=session_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"resume": resume}, session_interrupt_params.SessionInterruptParams),
            ),
            cast_to=SessionInterruptResponse,
        )

    async def log(
        self,
        session_id: SessionID,
        *,
        after: Optional[EventSeq] | Omit = omit,
        follow: Optional[bool] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Experimental durable session event log. Reads events after an exclusive
        aggregate sequence and continues with live events when follow=true.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._get(
            path_template("/api/experimental/session/{session_id}/log", session_id=session_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "after": after,
                        "follow": follow,
                    },
                    session_log_params.SessionLogParams,
                ),
            ),
            cast_to=NoneType,
        )

    async def move(
        self,
        session_id: SessionID,
        *,
        directory: AbsolutePath,
        delivery: Optional[SessionInboxDelivery] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Move a session to another project directory at the requested delivery boundary.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            path_template("/api/session/{session_id}/move", session_id=session_id),
            body=await async_maybe_transform(
                {
                    "directory": directory,
                    "delivery": delivery,
                },
                session_move_params.SessionMoveParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def prompt(
        self,
        session_id: SessionID,
        *,
        text: str,
        id: Optional[SessionMessageID] | Omit = omit,
        agents: Iterable[PromptAgentAttachment] | Omit = omit,
        delivery: Optional[SessionInboxDelivery] | Omit = omit,
        files: Iterable[PromptInputFileAttachment] | Omit = omit,
        metadata: Dict[str, object] | Omit = omit,
        resume: Optional[bool] | Omit = omit,
        skills: Iterable[PromptInputSkillAttachment] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SessionPromptResponse:
        """
        Durably admit one session input and schedule agent-loop execution unless resume
        is false.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        return await self._post(
            path_template("/api/session/{session_id}/prompt", session_id=session_id),
            body=await async_maybe_transform(
                {
                    "text": text,
                    "id": id,
                    "agents": agents,
                    "delivery": delivery,
                    "files": files,
                    "metadata": metadata,
                    "resume": resume,
                    "skills": skills,
                },
                session_prompt_params.SessionPromptParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SessionPromptResponse,
        )

    async def remove(
        self,
        session_id: SessionID,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete a session and its child sessions.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            path_template("/api/session/{session_id}", session_id=session_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def shell(
        self,
        session_id: SessionID,
        *,
        command: str,
        id: Optional[SessionMessageID] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Execute one shell command in the session's working directory. Emits a
        shell.started event before execution and a shell.ended event with the merged
        output after.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            path_template("/api/session/{session_id}/shell", session_id=session_id),
            body=await async_maybe_transform(
                {
                    "command": command,
                    "id": id,
                },
                session_shell_params.SessionShellParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def skill(
        self,
        session_id: SessionID,
        *,
        id: SkillID,
        resume: Optional[bool] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Activate a skill for a session by appending a skill message and resuming
        execution.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            path_template("/api/experimental/session/{session_id}/skill", session_id=session_id),
            body=await async_maybe_transform(
                {
                    "id": id,
                    "resume": resume,
                },
                session_skill_params.SessionSkillParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def stats(
        self,
        *,
        from_: Union[Literal["Infinity", "-Infinity", "NaN"], float, None] | Omit = omit,
        project: Optional[ProjectID] | Omit = omit,
        timezone: Optional[str] | Omit = omit,
        to: Union[Literal["Infinity", "-Infinity", "NaN"], float, None] | Omit = omit,
        tools: Optional[Literal["none", "summary", "detail"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SessionStatsResponse:
        """
        Aggregate local session activity, usage, and tool reliability for a time range.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/api/experimental/session/stats",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "from_": from_,
                        "project": project,
                        "timezone": timezone,
                        "to": to,
                        "tools": tools,
                    },
                    session_stats_params.SessionStatsParams,
                ),
            ),
            cast_to=SessionStatsResponse,
        )

    async def switch_agent(
        self,
        session_id: SessionID,
        *,
        agent: AgentID,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Switch the agent used by subsequent provider turns.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            path_template("/api/session/{session_id}/agent", session_id=session_id),
            body=await async_maybe_transform({"agent": agent}, session_switch_agent_params.SessionSwitchAgentParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def switch_model(
        self,
        session_id: SessionID,
        *,
        model: ModelRef,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Switch the model used by subsequent provider turns.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            path_template("/api/session/{session_id}/model", session_id=session_id),
            body=await async_maybe_transform({"model": model}, session_switch_model_params.SessionSwitchModelParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def synthetic(
        self,
        session_id: SessionID,
        *,
        text: str,
        id: Optional[SessionMessageID] | Omit = omit,
        delivery: Optional[SessionInboxDelivery] | Omit = omit,
        description: Optional[str] | Omit = omit,
        metadata: Dict[str, object] | Omit = omit,
        resume: Optional[bool] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SessionSyntheticResponse:
        """
        Durably admit synthetic session input and schedule execution unless resume is
        false.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        return await self._post(
            path_template("/api/session/{session_id}/synthetic", session_id=session_id),
            body=await async_maybe_transform(
                {
                    "text": text,
                    "id": id,
                    "delivery": delivery,
                    "description": description,
                    "metadata": metadata,
                    "resume": resume,
                },
                session_synthetic_params.SessionSyntheticParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SessionSyntheticResponse,
        )

    async def view(
        self,
        session_id: SessionID,
        *,
        idle: float,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Mark the idle transition observed by the viewer as viewed.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            path_template("/api/session/{session_id}/view", session_id=session_id),
            body=await async_maybe_transform({"idle": idle}, session_view_params.SessionViewParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def wait(
        self,
        session_id: SessionID,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Wait for a session agent loop to become idle.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            path_template("/api/experimental/session/{session_id}/wait", session_id=session_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class SessionResourceWithRawResponse:
    def __init__(self, session: SessionResource) -> None:
        self._session = session

        self.create = to_raw_response_wrapper(
            session.create,
        )
        self.update = to_raw_response_wrapper(
            session.update,
        )
        self.list = to_raw_response_wrapper(
            session.list,
        )
        self.active = to_raw_response_wrapper(
            session.active,
        )
        self.background = to_raw_response_wrapper(
            session.background,
        )
        self.command = to_raw_response_wrapper(
            session.command,
        )
        self.compact = to_raw_response_wrapper(
            session.compact,
        )
        self.context = to_raw_response_wrapper(
            session.context,
        )
        self.diff = to_raw_response_wrapper(
            session.diff,
        )
        self.environment = to_raw_response_wrapper(
            session.environment,
        )
        self.export = to_raw_response_wrapper(
            session.export,
        )
        self.fork = to_raw_response_wrapper(
            session.fork,
        )
        self.generate = to_raw_response_wrapper(
            session.generate,
        )
        self.get = to_raw_response_wrapper(
            session.get,
        )
        self.import_ = to_raw_response_wrapper(
            session.import_,
        )
        self.interrupt = to_raw_response_wrapper(
            session.interrupt,
        )
        self.log = to_raw_response_wrapper(
            session.log,
        )
        self.move = to_raw_response_wrapper(
            session.move,
        )
        self.prompt = to_raw_response_wrapper(
            session.prompt,
        )
        self.remove = to_raw_response_wrapper(
            session.remove,
        )
        self.shell = to_raw_response_wrapper(
            session.shell,
        )
        self.skill = to_raw_response_wrapper(
            session.skill,
        )
        self.stats = to_raw_response_wrapper(
            session.stats,
        )
        self.switch_agent = to_raw_response_wrapper(
            session.switch_agent,
        )
        self.switch_model = to_raw_response_wrapper(
            session.switch_model,
        )
        self.synthetic = to_raw_response_wrapper(
            session.synthetic,
        )
        self.view = to_raw_response_wrapper(
            session.view,
        )
        self.wait = to_raw_response_wrapper(
            session.wait,
        )

    @cached_property
    def revert(self) -> RevertResourceWithRawResponse:
        return RevertResourceWithRawResponse(self._session.revert)

    @cached_property
    def inbox(self) -> InboxResourceWithRawResponse:
        return InboxResourceWithRawResponse(self._session.inbox)

    @cached_property
    def instructions(self) -> InstructionsResourceWithRawResponse:
        return InstructionsResourceWithRawResponse(self._session.instructions)

    @cached_property
    def message(self) -> MessageResourceWithRawResponse:
        return MessageResourceWithRawResponse(self._session.message)

    @cached_property
    def form(self) -> FormResourceWithRawResponse:
        return FormResourceWithRawResponse(self._session.form)


class AsyncSessionResourceWithRawResponse:
    def __init__(self, session: AsyncSessionResource) -> None:
        self._session = session

        self.create = async_to_raw_response_wrapper(
            session.create,
        )
        self.update = async_to_raw_response_wrapper(
            session.update,
        )
        self.list = async_to_raw_response_wrapper(
            session.list,
        )
        self.active = async_to_raw_response_wrapper(
            session.active,
        )
        self.background = async_to_raw_response_wrapper(
            session.background,
        )
        self.command = async_to_raw_response_wrapper(
            session.command,
        )
        self.compact = async_to_raw_response_wrapper(
            session.compact,
        )
        self.context = async_to_raw_response_wrapper(
            session.context,
        )
        self.diff = async_to_raw_response_wrapper(
            session.diff,
        )
        self.environment = async_to_raw_response_wrapper(
            session.environment,
        )
        self.export = async_to_raw_response_wrapper(
            session.export,
        )
        self.fork = async_to_raw_response_wrapper(
            session.fork,
        )
        self.generate = async_to_raw_response_wrapper(
            session.generate,
        )
        self.get = async_to_raw_response_wrapper(
            session.get,
        )
        self.import_ = async_to_raw_response_wrapper(
            session.import_,
        )
        self.interrupt = async_to_raw_response_wrapper(
            session.interrupt,
        )
        self.log = async_to_raw_response_wrapper(
            session.log,
        )
        self.move = async_to_raw_response_wrapper(
            session.move,
        )
        self.prompt = async_to_raw_response_wrapper(
            session.prompt,
        )
        self.remove = async_to_raw_response_wrapper(
            session.remove,
        )
        self.shell = async_to_raw_response_wrapper(
            session.shell,
        )
        self.skill = async_to_raw_response_wrapper(
            session.skill,
        )
        self.stats = async_to_raw_response_wrapper(
            session.stats,
        )
        self.switch_agent = async_to_raw_response_wrapper(
            session.switch_agent,
        )
        self.switch_model = async_to_raw_response_wrapper(
            session.switch_model,
        )
        self.synthetic = async_to_raw_response_wrapper(
            session.synthetic,
        )
        self.view = async_to_raw_response_wrapper(
            session.view,
        )
        self.wait = async_to_raw_response_wrapper(
            session.wait,
        )

    @cached_property
    def revert(self) -> AsyncRevertResourceWithRawResponse:
        return AsyncRevertResourceWithRawResponse(self._session.revert)

    @cached_property
    def inbox(self) -> AsyncInboxResourceWithRawResponse:
        return AsyncInboxResourceWithRawResponse(self._session.inbox)

    @cached_property
    def instructions(self) -> AsyncInstructionsResourceWithRawResponse:
        return AsyncInstructionsResourceWithRawResponse(self._session.instructions)

    @cached_property
    def message(self) -> AsyncMessageResourceWithRawResponse:
        return AsyncMessageResourceWithRawResponse(self._session.message)

    @cached_property
    def form(self) -> AsyncFormResourceWithRawResponse:
        return AsyncFormResourceWithRawResponse(self._session.form)


class SessionResourceWithStreamingResponse:
    def __init__(self, session: SessionResource) -> None:
        self._session = session

        self.create = to_streamed_response_wrapper(
            session.create,
        )
        self.update = to_streamed_response_wrapper(
            session.update,
        )
        self.list = to_streamed_response_wrapper(
            session.list,
        )
        self.active = to_streamed_response_wrapper(
            session.active,
        )
        self.background = to_streamed_response_wrapper(
            session.background,
        )
        self.command = to_streamed_response_wrapper(
            session.command,
        )
        self.compact = to_streamed_response_wrapper(
            session.compact,
        )
        self.context = to_streamed_response_wrapper(
            session.context,
        )
        self.diff = to_streamed_response_wrapper(
            session.diff,
        )
        self.environment = to_streamed_response_wrapper(
            session.environment,
        )
        self.export = to_streamed_response_wrapper(
            session.export,
        )
        self.fork = to_streamed_response_wrapper(
            session.fork,
        )
        self.generate = to_streamed_response_wrapper(
            session.generate,
        )
        self.get = to_streamed_response_wrapper(
            session.get,
        )
        self.import_ = to_streamed_response_wrapper(
            session.import_,
        )
        self.interrupt = to_streamed_response_wrapper(
            session.interrupt,
        )
        self.log = to_streamed_response_wrapper(
            session.log,
        )
        self.move = to_streamed_response_wrapper(
            session.move,
        )
        self.prompt = to_streamed_response_wrapper(
            session.prompt,
        )
        self.remove = to_streamed_response_wrapper(
            session.remove,
        )
        self.shell = to_streamed_response_wrapper(
            session.shell,
        )
        self.skill = to_streamed_response_wrapper(
            session.skill,
        )
        self.stats = to_streamed_response_wrapper(
            session.stats,
        )
        self.switch_agent = to_streamed_response_wrapper(
            session.switch_agent,
        )
        self.switch_model = to_streamed_response_wrapper(
            session.switch_model,
        )
        self.synthetic = to_streamed_response_wrapper(
            session.synthetic,
        )
        self.view = to_streamed_response_wrapper(
            session.view,
        )
        self.wait = to_streamed_response_wrapper(
            session.wait,
        )

    @cached_property
    def revert(self) -> RevertResourceWithStreamingResponse:
        return RevertResourceWithStreamingResponse(self._session.revert)

    @cached_property
    def inbox(self) -> InboxResourceWithStreamingResponse:
        return InboxResourceWithStreamingResponse(self._session.inbox)

    @cached_property
    def instructions(self) -> InstructionsResourceWithStreamingResponse:
        return InstructionsResourceWithStreamingResponse(self._session.instructions)

    @cached_property
    def message(self) -> MessageResourceWithStreamingResponse:
        return MessageResourceWithStreamingResponse(self._session.message)

    @cached_property
    def form(self) -> FormResourceWithStreamingResponse:
        return FormResourceWithStreamingResponse(self._session.form)


class AsyncSessionResourceWithStreamingResponse:
    def __init__(self, session: AsyncSessionResource) -> None:
        self._session = session

        self.create = async_to_streamed_response_wrapper(
            session.create,
        )
        self.update = async_to_streamed_response_wrapper(
            session.update,
        )
        self.list = async_to_streamed_response_wrapper(
            session.list,
        )
        self.active = async_to_streamed_response_wrapper(
            session.active,
        )
        self.background = async_to_streamed_response_wrapper(
            session.background,
        )
        self.command = async_to_streamed_response_wrapper(
            session.command,
        )
        self.compact = async_to_streamed_response_wrapper(
            session.compact,
        )
        self.context = async_to_streamed_response_wrapper(
            session.context,
        )
        self.diff = async_to_streamed_response_wrapper(
            session.diff,
        )
        self.environment = async_to_streamed_response_wrapper(
            session.environment,
        )
        self.export = async_to_streamed_response_wrapper(
            session.export,
        )
        self.fork = async_to_streamed_response_wrapper(
            session.fork,
        )
        self.generate = async_to_streamed_response_wrapper(
            session.generate,
        )
        self.get = async_to_streamed_response_wrapper(
            session.get,
        )
        self.import_ = async_to_streamed_response_wrapper(
            session.import_,
        )
        self.interrupt = async_to_streamed_response_wrapper(
            session.interrupt,
        )
        self.log = async_to_streamed_response_wrapper(
            session.log,
        )
        self.move = async_to_streamed_response_wrapper(
            session.move,
        )
        self.prompt = async_to_streamed_response_wrapper(
            session.prompt,
        )
        self.remove = async_to_streamed_response_wrapper(
            session.remove,
        )
        self.shell = async_to_streamed_response_wrapper(
            session.shell,
        )
        self.skill = async_to_streamed_response_wrapper(
            session.skill,
        )
        self.stats = async_to_streamed_response_wrapper(
            session.stats,
        )
        self.switch_agent = async_to_streamed_response_wrapper(
            session.switch_agent,
        )
        self.switch_model = async_to_streamed_response_wrapper(
            session.switch_model,
        )
        self.synthetic = async_to_streamed_response_wrapper(
            session.synthetic,
        )
        self.view = async_to_streamed_response_wrapper(
            session.view,
        )
        self.wait = async_to_streamed_response_wrapper(
            session.wait,
        )

    @cached_property
    def revert(self) -> AsyncRevertResourceWithStreamingResponse:
        return AsyncRevertResourceWithStreamingResponse(self._session.revert)

    @cached_property
    def inbox(self) -> AsyncInboxResourceWithStreamingResponse:
        return AsyncInboxResourceWithStreamingResponse(self._session.inbox)

    @cached_property
    def instructions(self) -> AsyncInstructionsResourceWithStreamingResponse:
        return AsyncInstructionsResourceWithStreamingResponse(self._session.instructions)

    @cached_property
    def message(self) -> AsyncMessageResourceWithStreamingResponse:
        return AsyncMessageResourceWithStreamingResponse(self._session.message)

    @cached_property
    def form(self) -> AsyncFormResourceWithStreamingResponse:
        return AsyncFormResourceWithStreamingResponse(self._session.form)
