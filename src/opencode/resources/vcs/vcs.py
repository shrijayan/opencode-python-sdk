# File generated from our OpenAPI spec by Ferrule. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

import httpx

from .branch import (
    BranchResource,
    AsyncBranchResource,
    BranchResourceWithRawResponse,
    AsyncBranchResourceWithRawResponse,
    BranchResourceWithStreamingResponse,
    AsyncBranchResourceWithStreamingResponse,
)
from ...types import vc_get_params, vc_base_params, vc_diff_params, vc_init_params, vc_status_params
from ..._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.vc_get_response import VcGetResponse
from ...types.vc_base_response import VcBaseResponse
from ...types.vc_diff_response import VcDiffResponse
from ...types.vc_status_response import VcStatusResponse
from ...types.shared_params.vcs_mode import VcsMode

__all__ = ["VcsResource", "AsyncVcsResource"]


class VcsResource(SyncAPIResource):
    @cached_property
    def branch(self) -> BranchResource:
        return BranchResource(self._client)

    @cached_property
    def with_raw_response(self) -> VcsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/#accessing-raw-response-data-eg-headers
        """
        return VcsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> VcsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/#with_streaming_response
        """
        return VcsResourceWithStreamingResponse(self)

    def base(
        self,
        *,
        location: Optional[vc_base_params.Location] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VcBaseResponse:
        """
        Infer a local review base from named branch creation history, or the repository
        default only when currently on that branch. Returns null before the first commit
        or when the provider lacks base metadata; ambiguous Git history requires an
        explicit base on diff requests.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/api/vcs/base",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"location": location}, vc_base_params.VcBaseParams),
            ),
            cast_to=VcBaseResponse,
        )

    def diff(
        self,
        *,
        mode: VcsMode,
        base: Optional[str] | Omit = omit,
        context: Optional[int] | Omit = omit,
        location: Optional[vc_diff_params.Location] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VcDiffResponse:
        """
        Diff HEAD to the working copy (working), the base merge-base to the working copy
        (branch), or the base merge-base to HEAD (committed). Omitting base preserves
        repository-default comparison; supplying it overrides the comparison without
        saving it.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/api/vcs/diff",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "mode": mode,
                        "base": base,
                        "context": context,
                        "location": location,
                    },
                    vc_diff_params.VcDiffParams,
                ),
            ),
            cast_to=VcDiffResponse,
        )

    def get(
        self,
        *,
        location: Optional[vc_get_params.Location] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VcGetResponse:
        """
        Get current and default branch information for the requested location.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/api/vcs",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"location": location}, vc_get_params.VcGetParams),
            ),
            cast_to=VcGetResponse,
        )

    def init(
        self,
        *,
        location: Optional[vc_init_params.Location] | Omit = omit,
        provider: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Initialize a repository using the selected VCS provider in a markerless
        project's directory and refresh its location services. Omitting provider
        defaults to git; built-in git and hg providers support initialization. An
        unknown provider returns 400; a registered provider without init returns 501.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/api/vcs/init",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "location": location,
                        "provider": provider,
                    },
                    vc_init_params.VcInitParams,
                ),
            ),
            cast_to=NoneType,
        )

    def status(
        self,
        *,
        location: Optional[vc_status_params.Location] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VcStatusResponse:
        """
        List uncommitted working-copy changes relative to the requested location.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/api/vcs/status",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"location": location}, vc_status_params.VcStatusParams),
            ),
            cast_to=VcStatusResponse,
        )


class AsyncVcsResource(AsyncAPIResource):
    @cached_property
    def branch(self) -> AsyncBranchResource:
        return AsyncBranchResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncVcsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/#accessing-raw-response-data-eg-headers
        """
        return AsyncVcsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncVcsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/#with_streaming_response
        """
        return AsyncVcsResourceWithStreamingResponse(self)

    async def base(
        self,
        *,
        location: Optional[vc_base_params.Location] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VcBaseResponse:
        """
        Infer a local review base from named branch creation history, or the repository
        default only when currently on that branch. Returns null before the first commit
        or when the provider lacks base metadata; ambiguous Git history requires an
        explicit base on diff requests.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/api/vcs/base",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"location": location}, vc_base_params.VcBaseParams),
            ),
            cast_to=VcBaseResponse,
        )

    async def diff(
        self,
        *,
        mode: VcsMode,
        base: Optional[str] | Omit = omit,
        context: Optional[int] | Omit = omit,
        location: Optional[vc_diff_params.Location] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VcDiffResponse:
        """
        Diff HEAD to the working copy (working), the base merge-base to the working copy
        (branch), or the base merge-base to HEAD (committed). Omitting base preserves
        repository-default comparison; supplying it overrides the comparison without
        saving it.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/api/vcs/diff",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "mode": mode,
                        "base": base,
                        "context": context,
                        "location": location,
                    },
                    vc_diff_params.VcDiffParams,
                ),
            ),
            cast_to=VcDiffResponse,
        )

    async def get(
        self,
        *,
        location: Optional[vc_get_params.Location] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VcGetResponse:
        """
        Get current and default branch information for the requested location.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/api/vcs",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"location": location}, vc_get_params.VcGetParams),
            ),
            cast_to=VcGetResponse,
        )

    async def init(
        self,
        *,
        location: Optional[vc_init_params.Location] | Omit = omit,
        provider: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Initialize a repository using the selected VCS provider in a markerless
        project's directory and refresh its location services. Omitting provider
        defaults to git; built-in git and hg providers support initialization. An
        unknown provider returns 400; a registered provider without init returns 501.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/api/vcs/init",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "location": location,
                        "provider": provider,
                    },
                    vc_init_params.VcInitParams,
                ),
            ),
            cast_to=NoneType,
        )

    async def status(
        self,
        *,
        location: Optional[vc_status_params.Location] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VcStatusResponse:
        """
        List uncommitted working-copy changes relative to the requested location.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/api/vcs/status",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"location": location}, vc_status_params.VcStatusParams),
            ),
            cast_to=VcStatusResponse,
        )


class VcsResourceWithRawResponse:
    def __init__(self, vcs: VcsResource) -> None:
        self._vcs = vcs

        self.base = to_raw_response_wrapper(
            vcs.base,
        )
        self.diff = to_raw_response_wrapper(
            vcs.diff,
        )
        self.get = to_raw_response_wrapper(
            vcs.get,
        )
        self.init = to_raw_response_wrapper(
            vcs.init,
        )
        self.status = to_raw_response_wrapper(
            vcs.status,
        )

    @cached_property
    def branch(self) -> BranchResourceWithRawResponse:
        return BranchResourceWithRawResponse(self._vcs.branch)


class AsyncVcsResourceWithRawResponse:
    def __init__(self, vcs: AsyncVcsResource) -> None:
        self._vcs = vcs

        self.base = async_to_raw_response_wrapper(
            vcs.base,
        )
        self.diff = async_to_raw_response_wrapper(
            vcs.diff,
        )
        self.get = async_to_raw_response_wrapper(
            vcs.get,
        )
        self.init = async_to_raw_response_wrapper(
            vcs.init,
        )
        self.status = async_to_raw_response_wrapper(
            vcs.status,
        )

    @cached_property
    def branch(self) -> AsyncBranchResourceWithRawResponse:
        return AsyncBranchResourceWithRawResponse(self._vcs.branch)


class VcsResourceWithStreamingResponse:
    def __init__(self, vcs: VcsResource) -> None:
        self._vcs = vcs

        self.base = to_streamed_response_wrapper(
            vcs.base,
        )
        self.diff = to_streamed_response_wrapper(
            vcs.diff,
        )
        self.get = to_streamed_response_wrapper(
            vcs.get,
        )
        self.init = to_streamed_response_wrapper(
            vcs.init,
        )
        self.status = to_streamed_response_wrapper(
            vcs.status,
        )

    @cached_property
    def branch(self) -> BranchResourceWithStreamingResponse:
        return BranchResourceWithStreamingResponse(self._vcs.branch)


class AsyncVcsResourceWithStreamingResponse:
    def __init__(self, vcs: AsyncVcsResource) -> None:
        self._vcs = vcs

        self.base = async_to_streamed_response_wrapper(
            vcs.base,
        )
        self.diff = async_to_streamed_response_wrapper(
            vcs.diff,
        )
        self.get = async_to_streamed_response_wrapper(
            vcs.get,
        )
        self.init = async_to_streamed_response_wrapper(
            vcs.init,
        )
        self.status = async_to_streamed_response_wrapper(
            vcs.status,
        )

    @cached_property
    def branch(self) -> AsyncBranchResourceWithStreamingResponse:
        return AsyncBranchResourceWithStreamingResponse(self._vcs.branch)
