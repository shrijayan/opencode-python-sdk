# File generated from our OpenAPI spec by Ferrule. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Optional
from typing_extensions import Literal

import httpx

from ..types import file_find_params, file_list_params, file_read_params, file_write_params
from .._files import read_file_content, async_read_file_content
from .._types import (
    Body,
    Omit,
    Query,
    Headers,
    NoneType,
    NotGiven,
    BinaryTypes,
    FileContent,
    AsyncBinaryTypes,
    omit,
    not_given,
)
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
from ..types.file_find_response import FileFindResponse
from ..types.file_list_response import FileListResponse
from ..types.file_write_response import FileWriteResponse

__all__ = ["FileResource", "AsyncFileResource"]


class FileResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> FileResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/#accessing-raw-response-data-eg-headers
        """
        return FileResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> FileResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/#with_streaming_response
        """
        return FileResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        location: Optional[file_list_params.Location] | Omit = omit,
        path: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FileListResponse:
        """
        List direct children using an absolute path or a path relative to the requested
        location, including parents and siblings outside its directory. Entry paths
        remain relative to the requested location; listing does not switch locations.

        Args:
          path: An absolute path or a path relative to the requested location. Defaults to the
              location directory.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/api/fs/list",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "location": location,
                        "path": path,
                    },
                    file_list_params.FileListParams,
                ),
            ),
            cast_to=FileListResponse,
        )

    def find(
        self,
        *,
        query: str,
        limit: Optional[int] | Omit = omit,
        location: Optional[file_find_params.Location] | Omit = omit,
        type: Optional[Literal["file", "directory"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FileFindResponse:
        """
        Find recursively ranked filesystem entries relative to the requested location.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/api/fs/find",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "query": query,
                        "limit": limit,
                        "location": location,
                        "type": type,
                    },
                    file_find_params.FileFindParams,
                ),
            ),
            cast_to=FileFindResponse,
        )

    def read(
        self,
        path: str,
        *,
        location: Optional[file_read_params.Location] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Stream one file relative to the requested location with ETag, Last-Modified, and
        single-range HTTP Range support (206 Partial Content, 416 Range Not Satisfiable,
        and 304 Not Modified; multi-range and malformed Range headers fall back to 200).

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not path:
            raise ValueError(f"Expected a non-empty value for `path` but received {path!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._get(
            path_template("/api/fs/read/{path}", path=path),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"location": location}, file_read_params.FileReadParams),
            ),
            cast_to=NoneType,
        )

    def write(
        self,
        *,
        body: FileContent | BinaryTypes,
        path: str,
        location: Optional[file_write_params.Location] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FileWriteResponse:
        """
        Write the raw request body to an absolute path or a path relative to the
        requested location, creating parent directories, and return the resolved
        absolute path. Unlike read, the target is not confined to the location.
        Experimental: may change without compatibility guarantees.

        Args:
          path: An absolute path or a path relative to the requested location. Missing parent
              directories are created.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Content-Type": "application/octet-stream", **(extra_headers or {})}
        return self._post(
            "/api/experimental/fs/write",
            content=read_file_content(body) if isinstance(body, os.PathLike) else body,
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "path": path,
                        "location": location,
                    },
                    file_write_params.FileWriteParams,
                ),
            ),
            cast_to=FileWriteResponse,
        )


class AsyncFileResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncFileResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/#accessing-raw-response-data-eg-headers
        """
        return AsyncFileResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncFileResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/#with_streaming_response
        """
        return AsyncFileResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        location: Optional[file_list_params.Location] | Omit = omit,
        path: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FileListResponse:
        """
        List direct children using an absolute path or a path relative to the requested
        location, including parents and siblings outside its directory. Entry paths
        remain relative to the requested location; listing does not switch locations.

        Args:
          path: An absolute path or a path relative to the requested location. Defaults to the
              location directory.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/api/fs/list",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "location": location,
                        "path": path,
                    },
                    file_list_params.FileListParams,
                ),
            ),
            cast_to=FileListResponse,
        )

    async def find(
        self,
        *,
        query: str,
        limit: Optional[int] | Omit = omit,
        location: Optional[file_find_params.Location] | Omit = omit,
        type: Optional[Literal["file", "directory"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FileFindResponse:
        """
        Find recursively ranked filesystem entries relative to the requested location.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/api/fs/find",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "query": query,
                        "limit": limit,
                        "location": location,
                        "type": type,
                    },
                    file_find_params.FileFindParams,
                ),
            ),
            cast_to=FileFindResponse,
        )

    async def read(
        self,
        path: str,
        *,
        location: Optional[file_read_params.Location] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Stream one file relative to the requested location with ETag, Last-Modified, and
        single-range HTTP Range support (206 Partial Content, 416 Range Not Satisfiable,
        and 304 Not Modified; multi-range and malformed Range headers fall back to 200).

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not path:
            raise ValueError(f"Expected a non-empty value for `path` but received {path!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._get(
            path_template("/api/fs/read/{path}", path=path),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"location": location}, file_read_params.FileReadParams),
            ),
            cast_to=NoneType,
        )

    async def write(
        self,
        *,
        body: FileContent | AsyncBinaryTypes,
        path: str,
        location: Optional[file_write_params.Location] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FileWriteResponse:
        """
        Write the raw request body to an absolute path or a path relative to the
        requested location, creating parent directories, and return the resolved
        absolute path. Unlike read, the target is not confined to the location.
        Experimental: may change without compatibility guarantees.

        Args:
          path: An absolute path or a path relative to the requested location. Missing parent
              directories are created.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Content-Type": "application/octet-stream", **(extra_headers or {})}
        return await self._post(
            "/api/experimental/fs/write",
            content=await async_read_file_content(body) if isinstance(body, os.PathLike) else body,
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "path": path,
                        "location": location,
                    },
                    file_write_params.FileWriteParams,
                ),
            ),
            cast_to=FileWriteResponse,
        )


class FileResourceWithRawResponse:
    def __init__(self, file: FileResource) -> None:
        self._file = file

        self.list = to_raw_response_wrapper(
            file.list,
        )
        self.find = to_raw_response_wrapper(
            file.find,
        )
        self.read = to_raw_response_wrapper(
            file.read,
        )
        self.write = to_raw_response_wrapper(
            file.write,
        )


class AsyncFileResourceWithRawResponse:
    def __init__(self, file: AsyncFileResource) -> None:
        self._file = file

        self.list = async_to_raw_response_wrapper(
            file.list,
        )
        self.find = async_to_raw_response_wrapper(
            file.find,
        )
        self.read = async_to_raw_response_wrapper(
            file.read,
        )
        self.write = async_to_raw_response_wrapper(
            file.write,
        )


class FileResourceWithStreamingResponse:
    def __init__(self, file: FileResource) -> None:
        self._file = file

        self.list = to_streamed_response_wrapper(
            file.list,
        )
        self.find = to_streamed_response_wrapper(
            file.find,
        )
        self.read = to_streamed_response_wrapper(
            file.read,
        )
        self.write = to_streamed_response_wrapper(
            file.write,
        )


class AsyncFileResourceWithStreamingResponse:
    def __init__(self, file: AsyncFileResource) -> None:
        self._file = file

        self.list = async_to_streamed_response_wrapper(
            file.list,
        )
        self.find = async_to_streamed_response_wrapper(
            file.find,
        )
        self.read = async_to_streamed_response_wrapper(
            file.read,
        )
        self.write = async_to_streamed_response_wrapper(
            file.write,
        )
