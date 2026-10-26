# File generated from our OpenAPI spec by Ferrule. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, cast

import httpx

from ..._types import Body, Query, Headers, NotGiven, not_given
from ..._utils import path_template
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
from ...types.shared.session_id import SessionID
from ...types.shared.session_message_id import SessionMessageID
from ...types.shared.session_message_info import SessionMessageInfo

__all__ = ["MessageResource", "AsyncMessageResource"]


class MessageResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> MessageResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/#accessing-raw-response-data-eg-headers
        """
        return MessageResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> MessageResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/#with_streaming_response
        """
        return MessageResourceWithStreamingResponse(self)

    def get(
        self,
        message_id: SessionMessageID,
        *,
        session_id: SessionID,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SessionMessageInfo:
        """
        Retrieve one projected message owned by the Session.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        if not message_id:
            raise ValueError(f"Expected a non-empty value for `message_id` but received {message_id!r}")
        return self._get(
            path_template(
                "/api/session/{session_id}/message/{message_id}", session_id=session_id, message_id=message_id
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=DataWrapper[SessionMessageInfo]._unwrapper,
            ),
            cast_to=cast(Type[SessionMessageInfo], DataWrapper[SessionMessageInfo]),
        )


class AsyncMessageResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncMessageResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/#accessing-raw-response-data-eg-headers
        """
        return AsyncMessageResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMessageResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/#with_streaming_response
        """
        return AsyncMessageResourceWithStreamingResponse(self)

    async def get(
        self,
        message_id: SessionMessageID,
        *,
        session_id: SessionID,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SessionMessageInfo:
        """
        Retrieve one projected message owned by the Session.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        if not message_id:
            raise ValueError(f"Expected a non-empty value for `message_id` but received {message_id!r}")
        return await self._get(
            path_template(
                "/api/session/{session_id}/message/{message_id}", session_id=session_id, message_id=message_id
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=DataWrapper[SessionMessageInfo]._unwrapper,
            ),
            cast_to=cast(Type[SessionMessageInfo], DataWrapper[SessionMessageInfo]),
        )


class MessageResourceWithRawResponse:
    def __init__(self, message: MessageResource) -> None:
        self._message = message

        self.get = to_raw_response_wrapper(
            message.get,
        )


class AsyncMessageResourceWithRawResponse:
    def __init__(self, message: AsyncMessageResource) -> None:
        self._message = message

        self.get = async_to_raw_response_wrapper(
            message.get,
        )


class MessageResourceWithStreamingResponse:
    def __init__(self, message: MessageResource) -> None:
        self._message = message

        self.get = to_streamed_response_wrapper(
            message.get,
        )


class AsyncMessageResourceWithStreamingResponse:
    def __init__(self, message: AsyncMessageResource) -> None:
        self._message = message

        self.get = async_to_streamed_response_wrapper(
            message.get,
        )
