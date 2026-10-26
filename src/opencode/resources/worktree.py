# File generated from our OpenAPI spec by Ferrule. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import worktree_list_params, worktree_create_params, worktree_remove_params, worktree_refresh_params
from .._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.shared.worktree_info import WorktreeInfo
from ..types.shared.worktree_list import WorktreeList
from ..types.shared_params.project_id import ProjectID
from ..types.shared_params.absolute_path import AbsolutePath

__all__ = ["WorktreeResource", "AsyncWorktreeResource"]


class WorktreeResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> WorktreeResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/#accessing-raw-response-data-eg-headers
        """
        return WorktreeResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> WorktreeResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/#with_streaming_response
        """
        return WorktreeResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        project_id: ProjectID,
        branch: str | Omit = omit,
        directory: AbsolutePath | Omit = omit,
        from_: AbsolutePath | Omit = omit,
        name: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WorktreeInfo:
        """
        Load the project's canonical configuration, create a local worktree using its
        selected strategy, then run the project's setup script.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/worktree",
            body=maybe_transform(
                {
                    "project_id": project_id,
                    "branch": branch,
                    "directory": directory,
                    "from_": from_,
                    "name": name,
                },
                worktree_create_params.WorktreeCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WorktreeInfo,
        )

    def list(
        self,
        *,
        project_id: ProjectID,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WorktreeList:
        """
        Return the project's saved worktree inventory without loading configuration or
        running discovery.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/api/worktree",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"project_id": project_id}, worktree_list_params.WorktreeListParams),
            ),
            cast_to=WorktreeList,
        )

    def refresh(
        self,
        *,
        project_id: ProjectID,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Load the project's canonical configuration, discover worktrees across known
        checkout roots using all available strategies, and reconcile saved state.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/api/worktree/refresh",
            body=maybe_transform({"project_id": project_id}, worktree_refresh_params.WorktreeRefreshParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def remove(
        self,
        *,
        directory: AbsolutePath,
        force: bool,
        project_id: ProjectID,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Load the project's canonical configuration and remove a saved worktree using its
        recorded strategy.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            "/api/worktree",
            body=maybe_transform(
                {
                    "directory": directory,
                    "force": force,
                    "project_id": project_id,
                },
                worktree_remove_params.WorktreeRemoveParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncWorktreeResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncWorktreeResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/#accessing-raw-response-data-eg-headers
        """
        return AsyncWorktreeResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncWorktreeResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/#with_streaming_response
        """
        return AsyncWorktreeResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        project_id: ProjectID,
        branch: str | Omit = omit,
        directory: AbsolutePath | Omit = omit,
        from_: AbsolutePath | Omit = omit,
        name: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WorktreeInfo:
        """
        Load the project's canonical configuration, create a local worktree using its
        selected strategy, then run the project's setup script.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/worktree",
            body=await async_maybe_transform(
                {
                    "project_id": project_id,
                    "branch": branch,
                    "directory": directory,
                    "from_": from_,
                    "name": name,
                },
                worktree_create_params.WorktreeCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WorktreeInfo,
        )

    async def list(
        self,
        *,
        project_id: ProjectID,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WorktreeList:
        """
        Return the project's saved worktree inventory without loading configuration or
        running discovery.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/api/worktree",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"project_id": project_id}, worktree_list_params.WorktreeListParams),
            ),
            cast_to=WorktreeList,
        )

    async def refresh(
        self,
        *,
        project_id: ProjectID,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Load the project's canonical configuration, discover worktrees across known
        checkout roots using all available strategies, and reconcile saved state.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/api/worktree/refresh",
            body=await async_maybe_transform({"project_id": project_id}, worktree_refresh_params.WorktreeRefreshParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def remove(
        self,
        *,
        directory: AbsolutePath,
        force: bool,
        project_id: ProjectID,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Load the project's canonical configuration and remove a saved worktree using its
        recorded strategy.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            "/api/worktree",
            body=await async_maybe_transform(
                {
                    "directory": directory,
                    "force": force,
                    "project_id": project_id,
                },
                worktree_remove_params.WorktreeRemoveParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class WorktreeResourceWithRawResponse:
    def __init__(self, worktree: WorktreeResource) -> None:
        self._worktree = worktree

        self.create = to_raw_response_wrapper(
            worktree.create,
        )
        self.list = to_raw_response_wrapper(
            worktree.list,
        )
        self.refresh = to_raw_response_wrapper(
            worktree.refresh,
        )
        self.remove = to_raw_response_wrapper(
            worktree.remove,
        )


class AsyncWorktreeResourceWithRawResponse:
    def __init__(self, worktree: AsyncWorktreeResource) -> None:
        self._worktree = worktree

        self.create = async_to_raw_response_wrapper(
            worktree.create,
        )
        self.list = async_to_raw_response_wrapper(
            worktree.list,
        )
        self.refresh = async_to_raw_response_wrapper(
            worktree.refresh,
        )
        self.remove = async_to_raw_response_wrapper(
            worktree.remove,
        )


class WorktreeResourceWithStreamingResponse:
    def __init__(self, worktree: WorktreeResource) -> None:
        self._worktree = worktree

        self.create = to_streamed_response_wrapper(
            worktree.create,
        )
        self.list = to_streamed_response_wrapper(
            worktree.list,
        )
        self.refresh = to_streamed_response_wrapper(
            worktree.refresh,
        )
        self.remove = to_streamed_response_wrapper(
            worktree.remove,
        )


class AsyncWorktreeResourceWithStreamingResponse:
    def __init__(self, worktree: AsyncWorktreeResource) -> None:
        self._worktree = worktree

        self.create = async_to_streamed_response_wrapper(
            worktree.create,
        )
        self.list = async_to_streamed_response_wrapper(
            worktree.list,
        )
        self.refresh = async_to_streamed_response_wrapper(
            worktree.refresh,
        )
        self.remove = async_to_streamed_response_wrapper(
            worktree.remove,
        )
