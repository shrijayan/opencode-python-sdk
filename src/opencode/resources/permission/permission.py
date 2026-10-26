# File generated from our OpenAPI spec by Ferrule. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional

import httpx

from .saved import (
    SavedResource,
    AsyncSavedResource,
    SavedResourceWithRawResponse,
    AsyncSavedResourceWithRawResponse,
    SavedResourceWithStreamingResponse,
    AsyncSavedResourceWithStreamingResponse,
)
from ...types import permission_reply_params, permission_create_params
from .request import (
    RequestResource,
    AsyncRequestResource,
    RequestResourceWithRawResponse,
    AsyncRequestResourceWithRawResponse,
    RequestResourceWithStreamingResponse,
    AsyncRequestResourceWithStreamingResponse,
)
from ..._types import Body, Omit, Query, Headers, NoneType, NotGiven, SequenceNotStr, omit, not_given
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
from ...types.shared.agent_id import AgentID
from ...types.shared.session_id import SessionID
from ...types.shared.permission_id import PermissionID
from ...types.permission_get_response import PermissionGetResponse
from ...types.shared.permission_reply import PermissionReply
from ...types.permission_list_response import PermissionListResponse
from ...types.shared.permission_source import PermissionSource
from ...types.permission_create_response import PermissionCreateResponse

__all__ = ["PermissionResource", "AsyncPermissionResource"]


class PermissionResource(SyncAPIResource):
    @cached_property
    def request(self) -> RequestResource:
        return RequestResource(self._client)

    @cached_property
    def saved(self) -> SavedResource:
        return SavedResource(self._client)

    @cached_property
    def with_raw_response(self) -> PermissionResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/#accessing-raw-response-data-eg-headers
        """
        return PermissionResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PermissionResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/#with_streaming_response
        """
        return PermissionResourceWithStreamingResponse(self)

    def create(
        self,
        session_id: SessionID,
        *,
        action: str,
        resources: SequenceNotStr[str],
        id: Optional[PermissionID] | Omit = omit,
        agent: Optional[AgentID] | Omit = omit,
        metadata: Dict[str, object] | Omit = omit,
        save: SequenceNotStr[str] | Omit = omit,
        source: PermissionSource | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PermissionCreateResponse:
        """
        Evaluate and, when approval is required, create a permission request for a
        session.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        return self._post(
            path_template("/api/session/{session_id}/permission", session_id=session_id),
            body=maybe_transform(
                {
                    "action": action,
                    "resources": resources,
                    "id": id,
                    "agent": agent,
                    "metadata": metadata,
                    "save": save,
                    "source": source,
                },
                permission_create_params.PermissionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PermissionCreateResponse,
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
    ) -> PermissionListResponse:
        """
        Retrieve pending permission requests owned by a session.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        return self._get(
            path_template("/api/session/{session_id}/permission", session_id=session_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PermissionListResponse,
        )

    def get(
        self,
        request_id: PermissionID,
        *,
        session_id: SessionID,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PermissionGetResponse:
        """
        Retrieve a pending permission request owned by a session.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        if not request_id:
            raise ValueError(f"Expected a non-empty value for `request_id` but received {request_id!r}")
        return self._get(
            path_template(
                "/api/session/{session_id}/permission/{request_id}", session_id=session_id, request_id=request_id
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PermissionGetResponse,
        )

    def reply(
        self,
        request_id: PermissionID,
        *,
        session_id: SessionID,
        decision: PermissionReply,
        message: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Respond to a pending permission request owned by a session.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        if not request_id:
            raise ValueError(f"Expected a non-empty value for `request_id` but received {request_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            path_template(
                "/api/session/{session_id}/permission/{request_id}/reply", session_id=session_id, request_id=request_id
            ),
            body=maybe_transform(
                {
                    "decision": decision,
                    "message": message,
                },
                permission_reply_params.PermissionReplyParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncPermissionResource(AsyncAPIResource):
    @cached_property
    def request(self) -> AsyncRequestResource:
        return AsyncRequestResource(self._client)

    @cached_property
    def saved(self) -> AsyncSavedResource:
        return AsyncSavedResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncPermissionResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/#accessing-raw-response-data-eg-headers
        """
        return AsyncPermissionResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPermissionResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/#with_streaming_response
        """
        return AsyncPermissionResourceWithStreamingResponse(self)

    async def create(
        self,
        session_id: SessionID,
        *,
        action: str,
        resources: SequenceNotStr[str],
        id: Optional[PermissionID] | Omit = omit,
        agent: Optional[AgentID] | Omit = omit,
        metadata: Dict[str, object] | Omit = omit,
        save: SequenceNotStr[str] | Omit = omit,
        source: PermissionSource | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PermissionCreateResponse:
        """
        Evaluate and, when approval is required, create a permission request for a
        session.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        return await self._post(
            path_template("/api/session/{session_id}/permission", session_id=session_id),
            body=await async_maybe_transform(
                {
                    "action": action,
                    "resources": resources,
                    "id": id,
                    "agent": agent,
                    "metadata": metadata,
                    "save": save,
                    "source": source,
                },
                permission_create_params.PermissionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PermissionCreateResponse,
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
    ) -> PermissionListResponse:
        """
        Retrieve pending permission requests owned by a session.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        return await self._get(
            path_template("/api/session/{session_id}/permission", session_id=session_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PermissionListResponse,
        )

    async def get(
        self,
        request_id: PermissionID,
        *,
        session_id: SessionID,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PermissionGetResponse:
        """
        Retrieve a pending permission request owned by a session.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        if not request_id:
            raise ValueError(f"Expected a non-empty value for `request_id` but received {request_id!r}")
        return await self._get(
            path_template(
                "/api/session/{session_id}/permission/{request_id}", session_id=session_id, request_id=request_id
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PermissionGetResponse,
        )

    async def reply(
        self,
        request_id: PermissionID,
        *,
        session_id: SessionID,
        decision: PermissionReply,
        message: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Respond to a pending permission request owned by a session.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        if not request_id:
            raise ValueError(f"Expected a non-empty value for `request_id` but received {request_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            path_template(
                "/api/session/{session_id}/permission/{request_id}/reply", session_id=session_id, request_id=request_id
            ),
            body=await async_maybe_transform(
                {
                    "decision": decision,
                    "message": message,
                },
                permission_reply_params.PermissionReplyParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class PermissionResourceWithRawResponse:
    def __init__(self, permission: PermissionResource) -> None:
        self._permission = permission

        self.create = to_raw_response_wrapper(
            permission.create,
        )
        self.list = to_raw_response_wrapper(
            permission.list,
        )
        self.get = to_raw_response_wrapper(
            permission.get,
        )
        self.reply = to_raw_response_wrapper(
            permission.reply,
        )

    @cached_property
    def request(self) -> RequestResourceWithRawResponse:
        return RequestResourceWithRawResponse(self._permission.request)

    @cached_property
    def saved(self) -> SavedResourceWithRawResponse:
        return SavedResourceWithRawResponse(self._permission.saved)


class AsyncPermissionResourceWithRawResponse:
    def __init__(self, permission: AsyncPermissionResource) -> None:
        self._permission = permission

        self.create = async_to_raw_response_wrapper(
            permission.create,
        )
        self.list = async_to_raw_response_wrapper(
            permission.list,
        )
        self.get = async_to_raw_response_wrapper(
            permission.get,
        )
        self.reply = async_to_raw_response_wrapper(
            permission.reply,
        )

    @cached_property
    def request(self) -> AsyncRequestResourceWithRawResponse:
        return AsyncRequestResourceWithRawResponse(self._permission.request)

    @cached_property
    def saved(self) -> AsyncSavedResourceWithRawResponse:
        return AsyncSavedResourceWithRawResponse(self._permission.saved)


class PermissionResourceWithStreamingResponse:
    def __init__(self, permission: PermissionResource) -> None:
        self._permission = permission

        self.create = to_streamed_response_wrapper(
            permission.create,
        )
        self.list = to_streamed_response_wrapper(
            permission.list,
        )
        self.get = to_streamed_response_wrapper(
            permission.get,
        )
        self.reply = to_streamed_response_wrapper(
            permission.reply,
        )

    @cached_property
    def request(self) -> RequestResourceWithStreamingResponse:
        return RequestResourceWithStreamingResponse(self._permission.request)

    @cached_property
    def saved(self) -> SavedResourceWithStreamingResponse:
        return SavedResourceWithStreamingResponse(self._permission.saved)


class AsyncPermissionResourceWithStreamingResponse:
    def __init__(self, permission: AsyncPermissionResource) -> None:
        self._permission = permission

        self.create = async_to_streamed_response_wrapper(
            permission.create,
        )
        self.list = async_to_streamed_response_wrapper(
            permission.list,
        )
        self.get = async_to_streamed_response_wrapper(
            permission.get,
        )
        self.reply = async_to_streamed_response_wrapper(
            permission.reply,
        )

    @cached_property
    def request(self) -> AsyncRequestResourceWithStreamingResponse:
        return AsyncRequestResourceWithStreamingResponse(self._permission.request)

    @cached_property
    def saved(self) -> AsyncSavedResourceWithStreamingResponse:
        return AsyncSavedResourceWithStreamingResponse(self._permission.saved)
