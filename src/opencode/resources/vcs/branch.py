# File generated from our OpenAPI spec by Ferrule. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...types.vcs import branch_list_params
from ..._base_client import make_request_options
from ...types.vcs.branch_list_response import BranchListResponse

__all__ = ["BranchResource", "AsyncBranchResource"]


class BranchResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> BranchResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/#accessing-raw-response-data-eg-headers
        """
        return BranchResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BranchResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/#with_streaming_response
        """
        return BranchResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        limit: Optional[int] | Omit = omit,
        location: Optional[branch_list_params.Location] | Omit = omit,
        search: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BranchListResponse:
        """
        List local and remote branches available at the requested location.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/api/vcs/branch",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "location": location,
                        "search": search,
                    },
                    branch_list_params.BranchListParams,
                ),
            ),
            cast_to=BranchListResponse,
        )


class AsyncBranchResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncBranchResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/#accessing-raw-response-data-eg-headers
        """
        return AsyncBranchResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBranchResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/#with_streaming_response
        """
        return AsyncBranchResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        limit: Optional[int] | Omit = omit,
        location: Optional[branch_list_params.Location] | Omit = omit,
        search: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BranchListResponse:
        """
        List local and remote branches available at the requested location.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/api/vcs/branch",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "limit": limit,
                        "location": location,
                        "search": search,
                    },
                    branch_list_params.BranchListParams,
                ),
            ),
            cast_to=BranchListResponse,
        )


class BranchResourceWithRawResponse:
    def __init__(self, branch: BranchResource) -> None:
        self._branch = branch

        self.list = to_raw_response_wrapper(
            branch.list,
        )


class AsyncBranchResourceWithRawResponse:
    def __init__(self, branch: AsyncBranchResource) -> None:
        self._branch = branch

        self.list = async_to_raw_response_wrapper(
            branch.list,
        )


class BranchResourceWithStreamingResponse:
    def __init__(self, branch: BranchResource) -> None:
        self._branch = branch

        self.list = to_streamed_response_wrapper(
            branch.list,
        )


class AsyncBranchResourceWithStreamingResponse:
    def __init__(self, branch: AsyncBranchResource) -> None:
        self._branch = branch

        self.list = async_to_streamed_response_wrapper(
            branch.list,
        )
