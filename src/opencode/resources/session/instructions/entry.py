# File generated from our OpenAPI spec by Ferrule. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, cast

import httpx

from ...._types import Body, Query, Headers, NoneType, NotGiven, not_given
from ...._utils import path_template, maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._wrappers import DataWrapper
from ...._base_client import make_request_options
from ....types.shared.session_id import SessionID
from ....types.session.instructions import entry_put_params
from ....types.shared.instruction_entry_key import InstructionEntryKey
from ....types.session.instructions.entry_list_response import EntryListResponse

__all__ = ["EntryResource", "AsyncEntryResource"]


class EntryResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> EntryResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/#accessing-raw-response-data-eg-headers
        """
        return EntryResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> EntryResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/#with_streaming_response
        """
        return EntryResourceWithStreamingResponse(self)

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
    ) -> EntryListResponse:
        """
        List API-managed instruction entries attached to the session.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        return self._get(
            path_template("/api/experimental/session/{session_id}/instructions/entries", session_id=session_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=DataWrapper[EntryListResponse]._unwrapper,
            ),
            cast_to=cast(Type[EntryListResponse], DataWrapper[EntryListResponse]),
        )

    def put(
        self,
        key: InstructionEntryKey,
        *,
        session_id: SessionID,
        value: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Attach or replace one durable instruction entry. Changes announce as updates at
        the next step boundary.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        if not key:
            raise ValueError(f"Expected a non-empty value for `key` but received {key!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._put(
            path_template(
                "/api/experimental/session/{session_id}/instructions/entries/{key}", session_id=session_id, key=key
            ),
            body=maybe_transform({"value": value}, entry_put_params.EntryPutParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def remove(
        self,
        key: InstructionEntryKey,
        *,
        session_id: SessionID,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Remove one instruction entry; the removal is announced to the model at the next
        step boundary.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        if not key:
            raise ValueError(f"Expected a non-empty value for `key` but received {key!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            path_template(
                "/api/experimental/session/{session_id}/instructions/entries/{key}", session_id=session_id, key=key
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncEntryResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncEntryResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/#accessing-raw-response-data-eg-headers
        """
        return AsyncEntryResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncEntryResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/#with_streaming_response
        """
        return AsyncEntryResourceWithStreamingResponse(self)

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
    ) -> EntryListResponse:
        """
        List API-managed instruction entries attached to the session.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        return await self._get(
            path_template("/api/experimental/session/{session_id}/instructions/entries", session_id=session_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=DataWrapper[EntryListResponse]._unwrapper,
            ),
            cast_to=cast(Type[EntryListResponse], DataWrapper[EntryListResponse]),
        )

    async def put(
        self,
        key: InstructionEntryKey,
        *,
        session_id: SessionID,
        value: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Attach or replace one durable instruction entry. Changes announce as updates at
        the next step boundary.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        if not key:
            raise ValueError(f"Expected a non-empty value for `key` but received {key!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._put(
            path_template(
                "/api/experimental/session/{session_id}/instructions/entries/{key}", session_id=session_id, key=key
            ),
            body=await async_maybe_transform({"value": value}, entry_put_params.EntryPutParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def remove(
        self,
        key: InstructionEntryKey,
        *,
        session_id: SessionID,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Remove one instruction entry; the removal is announced to the model at the next
        step boundary.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        if not key:
            raise ValueError(f"Expected a non-empty value for `key` but received {key!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            path_template(
                "/api/experimental/session/{session_id}/instructions/entries/{key}", session_id=session_id, key=key
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class EntryResourceWithRawResponse:
    def __init__(self, entry: EntryResource) -> None:
        self._entry = entry

        self.list = to_raw_response_wrapper(
            entry.list,
        )
        self.put = to_raw_response_wrapper(
            entry.put,
        )
        self.remove = to_raw_response_wrapper(
            entry.remove,
        )


class AsyncEntryResourceWithRawResponse:
    def __init__(self, entry: AsyncEntryResource) -> None:
        self._entry = entry

        self.list = async_to_raw_response_wrapper(
            entry.list,
        )
        self.put = async_to_raw_response_wrapper(
            entry.put,
        )
        self.remove = async_to_raw_response_wrapper(
            entry.remove,
        )


class EntryResourceWithStreamingResponse:
    def __init__(self, entry: EntryResource) -> None:
        self._entry = entry

        self.list = to_streamed_response_wrapper(
            entry.list,
        )
        self.put = to_streamed_response_wrapper(
            entry.put,
        )
        self.remove = to_streamed_response_wrapper(
            entry.remove,
        )


class AsyncEntryResourceWithStreamingResponse:
    def __init__(self, entry: AsyncEntryResource) -> None:
        self._entry = entry

        self.list = async_to_streamed_response_wrapper(
            entry.list,
        )
        self.put = async_to_streamed_response_wrapper(
            entry.put,
        )
        self.remove = async_to_streamed_response_wrapper(
            entry.remove,
        )
