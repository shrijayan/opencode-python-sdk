# File generated from our OpenAPI spec by Ferrule. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional

import httpx

from ..types import shell_get_params, shell_list_params, shell_create_params, shell_output_params, shell_remove_params
from .._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
from .._utils import path_template, maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.shell_get_response import ShellGetResponse
from ..types.shell_list_response import ShellListResponse
from ..types.shell_create_response import ShellCreateResponse
from ..types.shell_output_response import ShellOutputResponse
from ..types.shared_params.shell_id import ShellID

__all__ = ["ShellResource", "AsyncShellResource"]


class ShellResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ShellResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/#accessing-raw-response-data-eg-headers
        """
        return ShellResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ShellResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/#with_streaming_response
        """
        return ShellResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        command: str,
        cwd: str | Omit = omit,
        location: Optional[shell_create_params.Location] | Omit = omit,
        metadata: Dict[str, object] | Omit = omit,
        api_timeout: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ShellCreateResponse:
        """
        Spawn one non-interactive shell command for a location. Combined stdout/stderr
        is captured to a file pageable via output.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/shell",
            body=maybe_transform(
                {
                    "command": command,
                    "cwd": cwd,
                    "metadata": metadata,
                    "api_timeout": api_timeout,
                },
                shell_create_params.ShellCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"location": location}, shell_create_params.ShellCreateParams),
            ),
            cast_to=ShellCreateResponse,
        )

    def list(
        self,
        *,
        location: Optional[shell_list_params.Location] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ShellListResponse:
        """
        List currently running shell commands for a location. Exited commands are not
        included.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/api/shell",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"location": location}, shell_list_params.ShellListParams),
            ),
            cast_to=ShellListResponse,
        )

    def get(
        self,
        id: ShellID,
        *,
        location: Optional[shell_get_params.Location] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ShellGetResponse:
        """
        Get one shell command, including its status and exit code once exited.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            path_template("/api/shell/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"location": location}, shell_get_params.ShellGetParams),
            ),
            cast_to=ShellGetResponse,
        )

    def output(
        self,
        id: ShellID,
        *,
        cursor: Optional[int] | Omit = omit,
        limit: Optional[int] | Omit = omit,
        location: Optional[shell_output_params.Location] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ShellOutputResponse:
        """
        Page through captured combined output by absolute byte cursor.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            path_template("/api/shell/{id}/output", id=id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "limit": limit,
                        "location": location,
                    },
                    shell_output_params.ShellOutputParams,
                ),
            ),
            cast_to=ShellOutputResponse,
        )

    def remove(
        self,
        id: ShellID,
        *,
        location: Optional[shell_remove_params.Location] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Terminate and remove one shell command and its retained output.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            path_template("/api/shell/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"location": location}, shell_remove_params.ShellRemoveParams),
            ),
            cast_to=NoneType,
        )


class AsyncShellResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncShellResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/#accessing-raw-response-data-eg-headers
        """
        return AsyncShellResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncShellResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/#with_streaming_response
        """
        return AsyncShellResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        command: str,
        cwd: str | Omit = omit,
        location: Optional[shell_create_params.Location] | Omit = omit,
        metadata: Dict[str, object] | Omit = omit,
        api_timeout: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ShellCreateResponse:
        """
        Spawn one non-interactive shell command for a location. Combined stdout/stderr
        is captured to a file pageable via output.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/shell",
            body=await async_maybe_transform(
                {
                    "command": command,
                    "cwd": cwd,
                    "metadata": metadata,
                    "api_timeout": api_timeout,
                },
                shell_create_params.ShellCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"location": location}, shell_create_params.ShellCreateParams),
            ),
            cast_to=ShellCreateResponse,
        )

    async def list(
        self,
        *,
        location: Optional[shell_list_params.Location] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ShellListResponse:
        """
        List currently running shell commands for a location. Exited commands are not
        included.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/api/shell",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"location": location}, shell_list_params.ShellListParams),
            ),
            cast_to=ShellListResponse,
        )

    async def get(
        self,
        id: ShellID,
        *,
        location: Optional[shell_get_params.Location] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ShellGetResponse:
        """
        Get one shell command, including its status and exit code once exited.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            path_template("/api/shell/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"location": location}, shell_get_params.ShellGetParams),
            ),
            cast_to=ShellGetResponse,
        )

    async def output(
        self,
        id: ShellID,
        *,
        cursor: Optional[int] | Omit = omit,
        limit: Optional[int] | Omit = omit,
        location: Optional[shell_output_params.Location] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ShellOutputResponse:
        """
        Page through captured combined output by absolute byte cursor.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            path_template("/api/shell/{id}/output", id=id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "cursor": cursor,
                        "limit": limit,
                        "location": location,
                    },
                    shell_output_params.ShellOutputParams,
                ),
            ),
            cast_to=ShellOutputResponse,
        )

    async def remove(
        self,
        id: ShellID,
        *,
        location: Optional[shell_remove_params.Location] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Terminate and remove one shell command and its retained output.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            path_template("/api/shell/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"location": location}, shell_remove_params.ShellRemoveParams),
            ),
            cast_to=NoneType,
        )


class ShellResourceWithRawResponse:
    def __init__(self, shell: ShellResource) -> None:
        self._shell = shell

        self.create = to_raw_response_wrapper(
            shell.create,
        )
        self.list = to_raw_response_wrapper(
            shell.list,
        )
        self.get = to_raw_response_wrapper(
            shell.get,
        )
        self.output = to_raw_response_wrapper(
            shell.output,
        )
        self.remove = to_raw_response_wrapper(
            shell.remove,
        )


class AsyncShellResourceWithRawResponse:
    def __init__(self, shell: AsyncShellResource) -> None:
        self._shell = shell

        self.create = async_to_raw_response_wrapper(
            shell.create,
        )
        self.list = async_to_raw_response_wrapper(
            shell.list,
        )
        self.get = async_to_raw_response_wrapper(
            shell.get,
        )
        self.output = async_to_raw_response_wrapper(
            shell.output,
        )
        self.remove = async_to_raw_response_wrapper(
            shell.remove,
        )


class ShellResourceWithStreamingResponse:
    def __init__(self, shell: ShellResource) -> None:
        self._shell = shell

        self.create = to_streamed_response_wrapper(
            shell.create,
        )
        self.list = to_streamed_response_wrapper(
            shell.list,
        )
        self.get = to_streamed_response_wrapper(
            shell.get,
        )
        self.output = to_streamed_response_wrapper(
            shell.output,
        )
        self.remove = to_streamed_response_wrapper(
            shell.remove,
        )


class AsyncShellResourceWithStreamingResponse:
    def __init__(self, shell: AsyncShellResource) -> None:
        self._shell = shell

        self.create = async_to_streamed_response_wrapper(
            shell.create,
        )
        self.list = async_to_streamed_response_wrapper(
            shell.list,
        )
        self.get = async_to_streamed_response_wrapper(
            shell.get,
        )
        self.output = async_to_streamed_response_wrapper(
            shell.output,
        )
        self.remove = async_to_streamed_response_wrapper(
            shell.remove,
        )
