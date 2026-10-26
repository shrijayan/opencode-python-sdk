# File generated from our OpenAPI spec by Ferrule. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional

import httpx

from ...types import pty_get_params, pty_list_params, pty_create_params, pty_remove_params, pty_update_params
from .connect import (
    ConnectResource,
    AsyncConnectResource,
    ConnectResourceWithRawResponse,
    AsyncConnectResourceWithRawResponse,
    ConnectResourceWithStreamingResponse,
    AsyncConnectResourceWithStreamingResponse,
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
from ...types.pty_get_response import PtyGetResponse
from ...types.pty_list_response import PtyListResponse
from ...types.pty_create_response import PtyCreateResponse
from ...types.pty_update_response import PtyUpdateResponse
from ...types.shared_params.pty_id import PtyID

__all__ = ["PtyResource", "AsyncPtyResource"]


class PtyResource(SyncAPIResource):
    @cached_property
    def connect(self) -> ConnectResource:
        return ConnectResource(self._client)

    @cached_property
    def with_raw_response(self) -> PtyResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/#accessing-raw-response-data-eg-headers
        """
        return PtyResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PtyResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/#with_streaming_response
        """
        return PtyResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        args: SequenceNotStr[str] | Omit = omit,
        command: str | Omit = omit,
        cwd: str | Omit = omit,
        env: Dict[str, str] | Omit = omit,
        location: Optional[pty_create_params.Location] | Omit = omit,
        title: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PtyCreateResponse:
        """
        Create a pseudo-terminal session for a location.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/pty",
            body=maybe_transform(
                {
                    "args": args,
                    "command": command,
                    "cwd": cwd,
                    "env": env,
                    "title": title,
                },
                pty_create_params.PtyCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"location": location}, pty_create_params.PtyCreateParams),
            ),
            cast_to=PtyCreateResponse,
        )

    def update(
        self,
        pty_id: PtyID,
        *,
        location: Optional[pty_update_params.Location] | Omit = omit,
        size: pty_update_params.Size | Omit = omit,
        title: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PtyUpdateResponse:
        """
        Update the title or viewport size of one PTY session.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not pty_id:
            raise ValueError(f"Expected a non-empty value for `pty_id` but received {pty_id!r}")
        return self._put(
            path_template("/api/pty/{pty_id}", pty_id=pty_id),
            body=maybe_transform(
                {
                    "size": size,
                    "title": title,
                },
                pty_update_params.PtyUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"location": location}, pty_update_params.PtyUpdateParams),
            ),
            cast_to=PtyUpdateResponse,
        )

    def list(
        self,
        *,
        location: Optional[pty_list_params.Location] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PtyListResponse:
        """
        List PTY sessions for a location, including exited sessions retained until
        removal.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/api/pty",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"location": location}, pty_list_params.PtyListParams),
            ),
            cast_to=PtyListResponse,
        )

    def get(
        self,
        pty_id: PtyID,
        *,
        location: Optional[pty_get_params.Location] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PtyGetResponse:
        """
        Get one PTY session, including its exit code once exited.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not pty_id:
            raise ValueError(f"Expected a non-empty value for `pty_id` but received {pty_id!r}")
        return self._get(
            path_template("/api/pty/{pty_id}", pty_id=pty_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"location": location}, pty_get_params.PtyGetParams),
            ),
            cast_to=PtyGetResponse,
        )

    def remove(
        self,
        pty_id: PtyID,
        *,
        location: Optional[pty_remove_params.Location] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Terminate and remove one PTY session.

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
            path_template("/api/pty/{pty_id}", pty_id=pty_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"location": location}, pty_remove_params.PtyRemoveParams),
            ),
            cast_to=NoneType,
        )


class AsyncPtyResource(AsyncAPIResource):
    @cached_property
    def connect(self) -> AsyncConnectResource:
        return AsyncConnectResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncPtyResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/#accessing-raw-response-data-eg-headers
        """
        return AsyncPtyResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPtyResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/#with_streaming_response
        """
        return AsyncPtyResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        args: SequenceNotStr[str] | Omit = omit,
        command: str | Omit = omit,
        cwd: str | Omit = omit,
        env: Dict[str, str] | Omit = omit,
        location: Optional[pty_create_params.Location] | Omit = omit,
        title: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PtyCreateResponse:
        """
        Create a pseudo-terminal session for a location.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/pty",
            body=await async_maybe_transform(
                {
                    "args": args,
                    "command": command,
                    "cwd": cwd,
                    "env": env,
                    "title": title,
                },
                pty_create_params.PtyCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"location": location}, pty_create_params.PtyCreateParams),
            ),
            cast_to=PtyCreateResponse,
        )

    async def update(
        self,
        pty_id: PtyID,
        *,
        location: Optional[pty_update_params.Location] | Omit = omit,
        size: pty_update_params.Size | Omit = omit,
        title: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PtyUpdateResponse:
        """
        Update the title or viewport size of one PTY session.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not pty_id:
            raise ValueError(f"Expected a non-empty value for `pty_id` but received {pty_id!r}")
        return await self._put(
            path_template("/api/pty/{pty_id}", pty_id=pty_id),
            body=await async_maybe_transform(
                {
                    "size": size,
                    "title": title,
                },
                pty_update_params.PtyUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"location": location}, pty_update_params.PtyUpdateParams),
            ),
            cast_to=PtyUpdateResponse,
        )

    async def list(
        self,
        *,
        location: Optional[pty_list_params.Location] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PtyListResponse:
        """
        List PTY sessions for a location, including exited sessions retained until
        removal.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/api/pty",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"location": location}, pty_list_params.PtyListParams),
            ),
            cast_to=PtyListResponse,
        )

    async def get(
        self,
        pty_id: PtyID,
        *,
        location: Optional[pty_get_params.Location] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PtyGetResponse:
        """
        Get one PTY session, including its exit code once exited.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not pty_id:
            raise ValueError(f"Expected a non-empty value for `pty_id` but received {pty_id!r}")
        return await self._get(
            path_template("/api/pty/{pty_id}", pty_id=pty_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"location": location}, pty_get_params.PtyGetParams),
            ),
            cast_to=PtyGetResponse,
        )

    async def remove(
        self,
        pty_id: PtyID,
        *,
        location: Optional[pty_remove_params.Location] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Terminate and remove one PTY session.

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
            path_template("/api/pty/{pty_id}", pty_id=pty_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"location": location}, pty_remove_params.PtyRemoveParams),
            ),
            cast_to=NoneType,
        )


class PtyResourceWithRawResponse:
    def __init__(self, pty: PtyResource) -> None:
        self._pty = pty

        self.create = to_raw_response_wrapper(
            pty.create,
        )
        self.update = to_raw_response_wrapper(
            pty.update,
        )
        self.list = to_raw_response_wrapper(
            pty.list,
        )
        self.get = to_raw_response_wrapper(
            pty.get,
        )
        self.remove = to_raw_response_wrapper(
            pty.remove,
        )

    @cached_property
    def connect(self) -> ConnectResourceWithRawResponse:
        return ConnectResourceWithRawResponse(self._pty.connect)


class AsyncPtyResourceWithRawResponse:
    def __init__(self, pty: AsyncPtyResource) -> None:
        self._pty = pty

        self.create = async_to_raw_response_wrapper(
            pty.create,
        )
        self.update = async_to_raw_response_wrapper(
            pty.update,
        )
        self.list = async_to_raw_response_wrapper(
            pty.list,
        )
        self.get = async_to_raw_response_wrapper(
            pty.get,
        )
        self.remove = async_to_raw_response_wrapper(
            pty.remove,
        )

    @cached_property
    def connect(self) -> AsyncConnectResourceWithRawResponse:
        return AsyncConnectResourceWithRawResponse(self._pty.connect)


class PtyResourceWithStreamingResponse:
    def __init__(self, pty: PtyResource) -> None:
        self._pty = pty

        self.create = to_streamed_response_wrapper(
            pty.create,
        )
        self.update = to_streamed_response_wrapper(
            pty.update,
        )
        self.list = to_streamed_response_wrapper(
            pty.list,
        )
        self.get = to_streamed_response_wrapper(
            pty.get,
        )
        self.remove = to_streamed_response_wrapper(
            pty.remove,
        )

    @cached_property
    def connect(self) -> ConnectResourceWithStreamingResponse:
        return ConnectResourceWithStreamingResponse(self._pty.connect)


class AsyncPtyResourceWithStreamingResponse:
    def __init__(self, pty: AsyncPtyResource) -> None:
        self._pty = pty

        self.create = async_to_streamed_response_wrapper(
            pty.create,
        )
        self.update = async_to_streamed_response_wrapper(
            pty.update,
        )
        self.list = async_to_streamed_response_wrapper(
            pty.list,
        )
        self.get = async_to_streamed_response_wrapper(
            pty.get,
        )
        self.remove = async_to_streamed_response_wrapper(
            pty.remove,
        )

    @cached_property
    def connect(self) -> AsyncConnectResourceWithStreamingResponse:
        return AsyncConnectResourceWithStreamingResponse(self._pty.connect)
