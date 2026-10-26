# File generated from our OpenAPI spec by Ferrule. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Type, Optional, cast

import httpx

from ..._types import Body, Omit, Query, Headers, NoneType, NotGiven, SequenceNotStr, omit, not_given
from ..._utils import is_given, path_template, maybe_transform, strip_not_given, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._wrappers import DataWrapper
from ..._base_client import make_request_options
from ...types.experimental import persistent_pty_read_params, persistent_pty_create_params, persistent_pty_update_params
from ...types.shared.pty_id import PtyID
from ...types.shared.session_id import SessionID
from ...types.shared.persistent_pty_info import PersistentPtyInfo
from ...types.shared.persistent_pty_snapshot import PersistentPtySnapshot
from ...types.shared.pty_ticket_connect_token import PtyTicketConnectToken
from ...types.shared.persistent_pty_read_lines import PersistentPtyReadLines
from ...types.experimental.persistent_pty_list_response import PersistentPtyListResponse
from ...types.experimental.persistent_pty_read_response import PersistentPtyReadResponse
from ...types.experimental.persistent_pty_handoff_response import PersistentPtyHandoffResponse

__all__ = ["PersistentPtyResource", "AsyncPersistentPtyResource"]


class PersistentPtyResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PersistentPtyResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/#accessing-raw-response-data-eg-headers
        """
        return PersistentPtyResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PersistentPtyResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/#with_streaming_response
        """
        return PersistentPtyResourceWithStreamingResponse(self)

    def create(
        self,
        session_id: SessionID,
        *,
        args: SequenceNotStr[str],
        env: Dict[str, str],
        title: str,
        command: str | Omit = omit,
        cwd: str | Omit = omit,
        size: persistent_pty_create_params.Size | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PersistentPtyInfo:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        return self._post(
            path_template("/api/experimental/session/{session_id}/terminal", session_id=session_id),
            body=maybe_transform(
                {
                    "args": args,
                    "env": env,
                    "title": title,
                    "command": command,
                    "cwd": cwd,
                    "size": size,
                },
                persistent_pty_create_params.PersistentPtyCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=DataWrapper[PersistentPtyInfo]._unwrapper,
            ),
            cast_to=cast(Type[PersistentPtyInfo], DataWrapper[PersistentPtyInfo]),
        )

    def update(
        self,
        pty_id: PtyID,
        *,
        size: persistent_pty_update_params.Size,
        attachment_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PersistentPtyInfo:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not pty_id:
            raise ValueError(f"Expected a non-empty value for `pty_id` but received {pty_id!r}")
        return self._put(
            path_template("/api/experimental/persistent-pty/{pty_id}", pty_id=pty_id),
            body=maybe_transform(
                {
                    "size": size,
                    "attachment_id": attachment_id,
                },
                persistent_pty_update_params.PersistentPtyUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=DataWrapper[PersistentPtyInfo]._unwrapper,
            ),
            cast_to=cast(Type[PersistentPtyInfo], DataWrapper[PersistentPtyInfo]),
        )

    def list(
        self,
        session_id: SessionID,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PersistentPtyListResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        return self._get(
            path_template("/api/experimental/session/{session_id}/terminal", session_id=session_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=DataWrapper[PersistentPtyListResponse]._unwrapper,
            ),
            cast_to=cast(Type[PersistentPtyListResponse], DataWrapper[PersistentPtyListResponse]),
        )

    def connect_token(
        self,
        pty_id: PtyID,
        *,
        x_opencode_ticket: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PtyTicketConnectToken:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not pty_id:
            raise ValueError(f"Expected a non-empty value for `pty_id` but received {pty_id!r}")
        extra_headers = {
            **strip_not_given(
                {"x-opencode-ticket": str(x_opencode_ticket) if is_given(x_opencode_ticket) else not_given}
            ),
            **(extra_headers or {}),
        }
        return self._post(
            path_template("/api/experimental/persistent-pty/{pty_id}/connect-token", pty_id=pty_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=DataWrapper[PtyTicketConnectToken]._unwrapper,
            ),
            cast_to=cast(Type[PtyTicketConnectToken], DataWrapper[PtyTicketConnectToken]),
        )

    def get(
        self,
        pty_id: PtyID,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PersistentPtyInfo:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not pty_id:
            raise ValueError(f"Expected a non-empty value for `pty_id` but received {pty_id!r}")
        return self._get(
            path_template("/api/experimental/persistent-pty/{pty_id}", pty_id=pty_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=DataWrapper[PersistentPtyInfo]._unwrapper,
            ),
            cast_to=cast(Type[PersistentPtyInfo], DataWrapper[PersistentPtyInfo]),
        )

    def handoff(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PersistentPtyHandoffResponse:
        return self._post(
            "/api/experimental/persistent-pty/handoff",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PersistentPtyHandoffResponse,
        )

    def read(
        self,
        session_id: SessionID,
        *,
        lines: Optional[PersistentPtyReadLines] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PersistentPtyReadResponse:
        """
        Read the last physical rows without changing selection or taking control.
        Omitted lines uses the live terminal height; larger counts include retained
        history. Blank rows are preserved. Screen dimensions and cursor remain relative
        to the live screen. Returns null when no current terminal exists. Selection is
        server-local and resets on restart. Experimental: may change without
        compatibility guarantees.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        return self._get(
            path_template("/api/experimental/session/{session_id}/terminal/read", session_id=session_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"lines": lines}, persistent_pty_read_params.PersistentPtyReadParams),
                post_parser=DataWrapper[PersistentPtyReadResponse]._unwrapper,
            ),
            cast_to=cast(Type[PersistentPtyReadResponse], DataWrapper[PersistentPtyReadResponse]),
        )

    def remove(
        self,
        pty_id: PtyID,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not pty_id:
            raise ValueError(f"Expected a non-empty value for `pty_id` but received {pty_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            path_template("/api/experimental/persistent-pty/{pty_id}", pty_id=pty_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def shutdown(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/api/experimental/persistent-pty/shutdown",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def snapshot(
        self,
        pty_id: PtyID,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PersistentPtySnapshot:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not pty_id:
            raise ValueError(f"Expected a non-empty value for `pty_id` but received {pty_id!r}")
        return self._get(
            path_template("/api/experimental/persistent-pty/{pty_id}/snapshot", pty_id=pty_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=DataWrapper[PersistentPtySnapshot]._unwrapper,
            ),
            cast_to=cast(Type[PersistentPtySnapshot], DataWrapper[PersistentPtySnapshot]),
        )


class AsyncPersistentPtyResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPersistentPtyResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/#accessing-raw-response-data-eg-headers
        """
        return AsyncPersistentPtyResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPersistentPtyResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/#with_streaming_response
        """
        return AsyncPersistentPtyResourceWithStreamingResponse(self)

    async def create(
        self,
        session_id: SessionID,
        *,
        args: SequenceNotStr[str],
        env: Dict[str, str],
        title: str,
        command: str | Omit = omit,
        cwd: str | Omit = omit,
        size: persistent_pty_create_params.Size | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PersistentPtyInfo:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        return await self._post(
            path_template("/api/experimental/session/{session_id}/terminal", session_id=session_id),
            body=await async_maybe_transform(
                {
                    "args": args,
                    "env": env,
                    "title": title,
                    "command": command,
                    "cwd": cwd,
                    "size": size,
                },
                persistent_pty_create_params.PersistentPtyCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=DataWrapper[PersistentPtyInfo]._unwrapper,
            ),
            cast_to=cast(Type[PersistentPtyInfo], DataWrapper[PersistentPtyInfo]),
        )

    async def update(
        self,
        pty_id: PtyID,
        *,
        size: persistent_pty_update_params.Size,
        attachment_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PersistentPtyInfo:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not pty_id:
            raise ValueError(f"Expected a non-empty value for `pty_id` but received {pty_id!r}")
        return await self._put(
            path_template("/api/experimental/persistent-pty/{pty_id}", pty_id=pty_id),
            body=await async_maybe_transform(
                {
                    "size": size,
                    "attachment_id": attachment_id,
                },
                persistent_pty_update_params.PersistentPtyUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=DataWrapper[PersistentPtyInfo]._unwrapper,
            ),
            cast_to=cast(Type[PersistentPtyInfo], DataWrapper[PersistentPtyInfo]),
        )

    async def list(
        self,
        session_id: SessionID,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PersistentPtyListResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        return await self._get(
            path_template("/api/experimental/session/{session_id}/terminal", session_id=session_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=DataWrapper[PersistentPtyListResponse]._unwrapper,
            ),
            cast_to=cast(Type[PersistentPtyListResponse], DataWrapper[PersistentPtyListResponse]),
        )

    async def connect_token(
        self,
        pty_id: PtyID,
        *,
        x_opencode_ticket: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PtyTicketConnectToken:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not pty_id:
            raise ValueError(f"Expected a non-empty value for `pty_id` but received {pty_id!r}")
        extra_headers = {
            **strip_not_given(
                {"x-opencode-ticket": str(x_opencode_ticket) if is_given(x_opencode_ticket) else not_given}
            ),
            **(extra_headers or {}),
        }
        return await self._post(
            path_template("/api/experimental/persistent-pty/{pty_id}/connect-token", pty_id=pty_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=DataWrapper[PtyTicketConnectToken]._unwrapper,
            ),
            cast_to=cast(Type[PtyTicketConnectToken], DataWrapper[PtyTicketConnectToken]),
        )

    async def get(
        self,
        pty_id: PtyID,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PersistentPtyInfo:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not pty_id:
            raise ValueError(f"Expected a non-empty value for `pty_id` but received {pty_id!r}")
        return await self._get(
            path_template("/api/experimental/persistent-pty/{pty_id}", pty_id=pty_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=DataWrapper[PersistentPtyInfo]._unwrapper,
            ),
            cast_to=cast(Type[PersistentPtyInfo], DataWrapper[PersistentPtyInfo]),
        )

    async def handoff(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PersistentPtyHandoffResponse:
        return await self._post(
            "/api/experimental/persistent-pty/handoff",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PersistentPtyHandoffResponse,
        )

    async def read(
        self,
        session_id: SessionID,
        *,
        lines: Optional[PersistentPtyReadLines] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PersistentPtyReadResponse:
        """
        Read the last physical rows without changing selection or taking control.
        Omitted lines uses the live terminal height; larger counts include retained
        history. Blank rows are preserved. Screen dimensions and cursor remain relative
        to the live screen. Returns null when no current terminal exists. Selection is
        server-local and resets on restart. Experimental: may change without
        compatibility guarantees.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        return await self._get(
            path_template("/api/experimental/session/{session_id}/terminal/read", session_id=session_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"lines": lines}, persistent_pty_read_params.PersistentPtyReadParams),
                post_parser=DataWrapper[PersistentPtyReadResponse]._unwrapper,
            ),
            cast_to=cast(Type[PersistentPtyReadResponse], DataWrapper[PersistentPtyReadResponse]),
        )

    async def remove(
        self,
        pty_id: PtyID,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not pty_id:
            raise ValueError(f"Expected a non-empty value for `pty_id` but received {pty_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            path_template("/api/experimental/persistent-pty/{pty_id}", pty_id=pty_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def shutdown(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/api/experimental/persistent-pty/shutdown",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def snapshot(
        self,
        pty_id: PtyID,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PersistentPtySnapshot:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not pty_id:
            raise ValueError(f"Expected a non-empty value for `pty_id` but received {pty_id!r}")
        return await self._get(
            path_template("/api/experimental/persistent-pty/{pty_id}/snapshot", pty_id=pty_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=DataWrapper[PersistentPtySnapshot]._unwrapper,
            ),
            cast_to=cast(Type[PersistentPtySnapshot], DataWrapper[PersistentPtySnapshot]),
        )


class PersistentPtyResourceWithRawResponse:
    def __init__(self, persistent_pty: PersistentPtyResource) -> None:
        self._persistent_pty = persistent_pty

        self.create = to_raw_response_wrapper(
            persistent_pty.create,
        )
        self.update = to_raw_response_wrapper(
            persistent_pty.update,
        )
        self.list = to_raw_response_wrapper(
            persistent_pty.list,
        )
        self.connect_token = to_raw_response_wrapper(
            persistent_pty.connect_token,
        )
        self.get = to_raw_response_wrapper(
            persistent_pty.get,
        )
        self.handoff = to_raw_response_wrapper(
            persistent_pty.handoff,
        )
        self.read = to_raw_response_wrapper(
            persistent_pty.read,
        )
        self.remove = to_raw_response_wrapper(
            persistent_pty.remove,
        )
        self.shutdown = to_raw_response_wrapper(
            persistent_pty.shutdown,
        )
        self.snapshot = to_raw_response_wrapper(
            persistent_pty.snapshot,
        )


class AsyncPersistentPtyResourceWithRawResponse:
    def __init__(self, persistent_pty: AsyncPersistentPtyResource) -> None:
        self._persistent_pty = persistent_pty

        self.create = async_to_raw_response_wrapper(
            persistent_pty.create,
        )
        self.update = async_to_raw_response_wrapper(
            persistent_pty.update,
        )
        self.list = async_to_raw_response_wrapper(
            persistent_pty.list,
        )
        self.connect_token = async_to_raw_response_wrapper(
            persistent_pty.connect_token,
        )
        self.get = async_to_raw_response_wrapper(
            persistent_pty.get,
        )
        self.handoff = async_to_raw_response_wrapper(
            persistent_pty.handoff,
        )
        self.read = async_to_raw_response_wrapper(
            persistent_pty.read,
        )
        self.remove = async_to_raw_response_wrapper(
            persistent_pty.remove,
        )
        self.shutdown = async_to_raw_response_wrapper(
            persistent_pty.shutdown,
        )
        self.snapshot = async_to_raw_response_wrapper(
            persistent_pty.snapshot,
        )


class PersistentPtyResourceWithStreamingResponse:
    def __init__(self, persistent_pty: PersistentPtyResource) -> None:
        self._persistent_pty = persistent_pty

        self.create = to_streamed_response_wrapper(
            persistent_pty.create,
        )
        self.update = to_streamed_response_wrapper(
            persistent_pty.update,
        )
        self.list = to_streamed_response_wrapper(
            persistent_pty.list,
        )
        self.connect_token = to_streamed_response_wrapper(
            persistent_pty.connect_token,
        )
        self.get = to_streamed_response_wrapper(
            persistent_pty.get,
        )
        self.handoff = to_streamed_response_wrapper(
            persistent_pty.handoff,
        )
        self.read = to_streamed_response_wrapper(
            persistent_pty.read,
        )
        self.remove = to_streamed_response_wrapper(
            persistent_pty.remove,
        )
        self.shutdown = to_streamed_response_wrapper(
            persistent_pty.shutdown,
        )
        self.snapshot = to_streamed_response_wrapper(
            persistent_pty.snapshot,
        )


class AsyncPersistentPtyResourceWithStreamingResponse:
    def __init__(self, persistent_pty: AsyncPersistentPtyResource) -> None:
        self._persistent_pty = persistent_pty

        self.create = async_to_streamed_response_wrapper(
            persistent_pty.create,
        )
        self.update = async_to_streamed_response_wrapper(
            persistent_pty.update,
        )
        self.list = async_to_streamed_response_wrapper(
            persistent_pty.list,
        )
        self.connect_token = async_to_streamed_response_wrapper(
            persistent_pty.connect_token,
        )
        self.get = async_to_streamed_response_wrapper(
            persistent_pty.get,
        )
        self.handoff = async_to_streamed_response_wrapper(
            persistent_pty.handoff,
        )
        self.read = async_to_streamed_response_wrapper(
            persistent_pty.read,
        )
        self.remove = async_to_streamed_response_wrapper(
            persistent_pty.remove,
        )
        self.shutdown = async_to_streamed_response_wrapper(
            persistent_pty.shutdown,
        )
        self.snapshot = async_to_streamed_response_wrapper(
            persistent_pty.snapshot,
        )
