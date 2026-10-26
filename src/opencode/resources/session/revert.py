# File generated from our OpenAPI spec by Ferrule. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

import httpx

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
from ..._base_client import make_request_options
from ...types.session import revert_stage_params
from ...types.shared.session_id import SessionID
from ...types.shared.session_message_id import SessionMessageID
from ...types.session.revert_stage_response import RevertStageResponse

__all__ = ["RevertResource", "AsyncRevertResource"]


class RevertResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> RevertResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/#accessing-raw-response-data-eg-headers
        """
        return RevertResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RevertResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/#with_streaming_response
        """
        return RevertResourceWithStreamingResponse(self)

    def clear(
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
        Clear staged revert

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
            path_template("/api/session/{session_id}/revert", session_id=session_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def commit(
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
        Commit staged revert

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
            path_template("/api/session/{session_id}/revert/commit", session_id=session_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def stage(
        self,
        session_id: SessionID,
        *,
        message_id: SessionMessageID,
        files: Optional[bool] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RevertStageResponse:
        """
        Stage or move a reversible session boundary and optionally apply its file
        changes.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        return self._post(
            path_template("/api/session/{session_id}/revert/stage", session_id=session_id),
            body=maybe_transform(
                {
                    "message_id": message_id,
                    "files": files,
                },
                revert_stage_params.RevertStageParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RevertStageResponse,
        )


class AsyncRevertResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncRevertResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/#accessing-raw-response-data-eg-headers
        """
        return AsyncRevertResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRevertResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/#with_streaming_response
        """
        return AsyncRevertResourceWithStreamingResponse(self)

    async def clear(
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
        Clear staged revert

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
            path_template("/api/session/{session_id}/revert", session_id=session_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def commit(
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
        Commit staged revert

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
            path_template("/api/session/{session_id}/revert/commit", session_id=session_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def stage(
        self,
        session_id: SessionID,
        *,
        message_id: SessionMessageID,
        files: Optional[bool] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RevertStageResponse:
        """
        Stage or move a reversible session boundary and optionally apply its file
        changes.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        return await self._post(
            path_template("/api/session/{session_id}/revert/stage", session_id=session_id),
            body=await async_maybe_transform(
                {
                    "message_id": message_id,
                    "files": files,
                },
                revert_stage_params.RevertStageParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RevertStageResponse,
        )


class RevertResourceWithRawResponse:
    def __init__(self, revert: RevertResource) -> None:
        self._revert = revert

        self.clear = to_raw_response_wrapper(
            revert.clear,
        )
        self.commit = to_raw_response_wrapper(
            revert.commit,
        )
        self.stage = to_raw_response_wrapper(
            revert.stage,
        )


class AsyncRevertResourceWithRawResponse:
    def __init__(self, revert: AsyncRevertResource) -> None:
        self._revert = revert

        self.clear = async_to_raw_response_wrapper(
            revert.clear,
        )
        self.commit = async_to_raw_response_wrapper(
            revert.commit,
        )
        self.stage = async_to_raw_response_wrapper(
            revert.stage,
        )


class RevertResourceWithStreamingResponse:
    def __init__(self, revert: RevertResource) -> None:
        self._revert = revert

        self.clear = to_streamed_response_wrapper(
            revert.clear,
        )
        self.commit = to_streamed_response_wrapper(
            revert.commit,
        )
        self.stage = to_streamed_response_wrapper(
            revert.stage,
        )


class AsyncRevertResourceWithStreamingResponse:
    def __init__(self, revert: AsyncRevertResource) -> None:
        self._revert = revert

        self.clear = async_to_streamed_response_wrapper(
            revert.clear,
        )
        self.commit = async_to_streamed_response_wrapper(
            revert.commit,
        )
        self.stage = async_to_streamed_response_wrapper(
            revert.stage,
        )
