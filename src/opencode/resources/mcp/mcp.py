# File generated from our OpenAPI spec by Ferrule. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

import httpx

from ...types import mcp_add_params, mcp_list_params, mcp_remove_params, mcp_connect_params, mcp_disconnect_params
from ..._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
from ..._utils import path_template, maybe_transform, async_maybe_transform
from .resource import (
    ResourceResource,
    AsyncResourceResource,
    ResourceResourceWithRawResponse,
    AsyncResourceResourceWithRawResponse,
    ResourceResourceWithStreamingResponse,
    AsyncResourceResourceWithStreamingResponse,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.mcp_list_response import McpListResponse

__all__ = ["McpResource", "AsyncMcpResource"]


class McpResource(SyncAPIResource):
    @cached_property
    def resource(self) -> ResourceResource:
        return ResourceResource(self._client)

    @cached_property
    def with_raw_response(self) -> McpResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/#accessing-raw-response-data-eg-headers
        """
        return McpResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> McpResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/#with_streaming_response
        """
        return McpResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        location: Optional[mcp_list_params.Location] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> McpListResponse:
        """
        Retrieve configured MCP servers and their connection status.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/api/mcp",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"location": location}, mcp_list_params.McpListParams),
            ),
            cast_to=McpListResponse,
        )

    def add(
        self,
        server: str,
        *,
        config: mcp_add_params.Config,
        location: Optional[mcp_add_params.Location] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Add an MCP server at runtime or replace an existing one, connecting it
        immediately.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not server:
            raise ValueError(f"Expected a non-empty value for `server` but received {server!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._put(
            path_template("/api/experimental/mcp/{server}", server=server),
            body=maybe_transform({"config": config}, mcp_add_params.McpAddParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"location": location}, mcp_add_params.McpAddParams),
            ),
            cast_to=NoneType,
        )

    def connect(
        self,
        server: str,
        *,
        location: Optional[mcp_connect_params.Location] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Connect an MCP server at runtime, overriding a disabled configuration until
        restart.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not server:
            raise ValueError(f"Expected a non-empty value for `server` but received {server!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            path_template("/api/experimental/mcp/{server}/connect", server=server),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"location": location}, mcp_connect_params.McpConnectParams),
            ),
            cast_to=NoneType,
        )

    def disconnect(
        self,
        server: str,
        *,
        location: Optional[mcp_disconnect_params.Location] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Disconnect an MCP server at runtime, removing its tools until reconnected.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not server:
            raise ValueError(f"Expected a non-empty value for `server` but received {server!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            path_template("/api/experimental/mcp/{server}/disconnect", server=server),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"location": location}, mcp_disconnect_params.McpDisconnectParams),
            ),
            cast_to=NoneType,
        )

    def remove(
        self,
        server: str,
        *,
        location: Optional[mcp_remove_params.Location] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Stop an MCP server and remove it from the runtime set until restart.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not server:
            raise ValueError(f"Expected a non-empty value for `server` but received {server!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            path_template("/api/experimental/mcp/{server}", server=server),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"location": location}, mcp_remove_params.McpRemoveParams),
            ),
            cast_to=NoneType,
        )


class AsyncMcpResource(AsyncAPIResource):
    @cached_property
    def resource(self) -> AsyncResourceResource:
        return AsyncResourceResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncMcpResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/#accessing-raw-response-data-eg-headers
        """
        return AsyncMcpResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMcpResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/#with_streaming_response
        """
        return AsyncMcpResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        location: Optional[mcp_list_params.Location] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> McpListResponse:
        """
        Retrieve configured MCP servers and their connection status.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/api/mcp",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"location": location}, mcp_list_params.McpListParams),
            ),
            cast_to=McpListResponse,
        )

    async def add(
        self,
        server: str,
        *,
        config: mcp_add_params.Config,
        location: Optional[mcp_add_params.Location] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Add an MCP server at runtime or replace an existing one, connecting it
        immediately.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not server:
            raise ValueError(f"Expected a non-empty value for `server` but received {server!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._put(
            path_template("/api/experimental/mcp/{server}", server=server),
            body=await async_maybe_transform({"config": config}, mcp_add_params.McpAddParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"location": location}, mcp_add_params.McpAddParams),
            ),
            cast_to=NoneType,
        )

    async def connect(
        self,
        server: str,
        *,
        location: Optional[mcp_connect_params.Location] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Connect an MCP server at runtime, overriding a disabled configuration until
        restart.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not server:
            raise ValueError(f"Expected a non-empty value for `server` but received {server!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            path_template("/api/experimental/mcp/{server}/connect", server=server),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"location": location}, mcp_connect_params.McpConnectParams),
            ),
            cast_to=NoneType,
        )

    async def disconnect(
        self,
        server: str,
        *,
        location: Optional[mcp_disconnect_params.Location] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Disconnect an MCP server at runtime, removing its tools until reconnected.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not server:
            raise ValueError(f"Expected a non-empty value for `server` but received {server!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            path_template("/api/experimental/mcp/{server}/disconnect", server=server),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"location": location}, mcp_disconnect_params.McpDisconnectParams),
            ),
            cast_to=NoneType,
        )

    async def remove(
        self,
        server: str,
        *,
        location: Optional[mcp_remove_params.Location] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Stop an MCP server and remove it from the runtime set until restart.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not server:
            raise ValueError(f"Expected a non-empty value for `server` but received {server!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            path_template("/api/experimental/mcp/{server}", server=server),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"location": location}, mcp_remove_params.McpRemoveParams),
            ),
            cast_to=NoneType,
        )


class McpResourceWithRawResponse:
    def __init__(self, mcp: McpResource) -> None:
        self._mcp = mcp

        self.list = to_raw_response_wrapper(
            mcp.list,
        )
        self.add = to_raw_response_wrapper(
            mcp.add,
        )
        self.connect = to_raw_response_wrapper(
            mcp.connect,
        )
        self.disconnect = to_raw_response_wrapper(
            mcp.disconnect,
        )
        self.remove = to_raw_response_wrapper(
            mcp.remove,
        )

    @cached_property
    def resource(self) -> ResourceResourceWithRawResponse:
        return ResourceResourceWithRawResponse(self._mcp.resource)


class AsyncMcpResourceWithRawResponse:
    def __init__(self, mcp: AsyncMcpResource) -> None:
        self._mcp = mcp

        self.list = async_to_raw_response_wrapper(
            mcp.list,
        )
        self.add = async_to_raw_response_wrapper(
            mcp.add,
        )
        self.connect = async_to_raw_response_wrapper(
            mcp.connect,
        )
        self.disconnect = async_to_raw_response_wrapper(
            mcp.disconnect,
        )
        self.remove = async_to_raw_response_wrapper(
            mcp.remove,
        )

    @cached_property
    def resource(self) -> AsyncResourceResourceWithRawResponse:
        return AsyncResourceResourceWithRawResponse(self._mcp.resource)


class McpResourceWithStreamingResponse:
    def __init__(self, mcp: McpResource) -> None:
        self._mcp = mcp

        self.list = to_streamed_response_wrapper(
            mcp.list,
        )
        self.add = to_streamed_response_wrapper(
            mcp.add,
        )
        self.connect = to_streamed_response_wrapper(
            mcp.connect,
        )
        self.disconnect = to_streamed_response_wrapper(
            mcp.disconnect,
        )
        self.remove = to_streamed_response_wrapper(
            mcp.remove,
        )

    @cached_property
    def resource(self) -> ResourceResourceWithStreamingResponse:
        return ResourceResourceWithStreamingResponse(self._mcp.resource)


class AsyncMcpResourceWithStreamingResponse:
    def __init__(self, mcp: AsyncMcpResource) -> None:
        self._mcp = mcp

        self.list = async_to_streamed_response_wrapper(
            mcp.list,
        )
        self.add = async_to_streamed_response_wrapper(
            mcp.add,
        )
        self.connect = async_to_streamed_response_wrapper(
            mcp.connect,
        )
        self.disconnect = async_to_streamed_response_wrapper(
            mcp.disconnect,
        )
        self.remove = async_to_streamed_response_wrapper(
            mcp.remove,
        )

    @cached_property
    def resource(self) -> AsyncResourceResourceWithStreamingResponse:
        return AsyncResourceResourceWithStreamingResponse(self._mcp.resource)
