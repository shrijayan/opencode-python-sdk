# File generated from our OpenAPI spec by Ferrule. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

import httpx

from ..types import plugin_list_params, plugin_check_params, plugin_update_params
from .._types import Body, Omit, Query, Headers, NoneType, NotGiven, SequenceNotStr, omit, not_given
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
from ..types.plugin_list_response import PluginListResponse
from ..types.plugin_check_response import PluginCheckResponse

__all__ = ["PluginResource", "AsyncPluginResource"]


class PluginResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PluginResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/#accessing-raw-response-data-eg-headers
        """
        return PluginResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PluginResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/#with_streaming_response
        """
        return PluginResourceWithStreamingResponse(self)

    def update(
        self,
        *,
        targets: SequenceNotStr[str],
        location: Optional[plugin_update_params.Location] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Update package plugins concurrently and notify active locations to reload them.
        Responds once every update has finished; fails when any update fails.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/api/plugin/update",
            body=maybe_transform({"targets": targets}, plugin_update_params.PluginUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"location": location}, plugin_update_params.PluginUpdateParams),
            ),
            cast_to=NoneType,
        )

    def list(
        self,
        *,
        location: Optional[plugin_list_params.Location] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PluginListResponse:
        """
        Retrieve enabled server plugins and their current status.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/api/plugin",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"location": location}, plugin_list_params.PluginListParams),
            ),
            cast_to=PluginListResponse,
        )

    def check(
        self,
        *,
        location: Optional[plugin_check_params.Location] | Omit = omit,
        target: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PluginCheckResponse:
        """
        Check one or all package plugins for available updates.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/plugin/check",
            body=maybe_transform({"target": target}, plugin_check_params.PluginCheckParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"location": location}, plugin_check_params.PluginCheckParams),
            ),
            cast_to=PluginCheckResponse,
        )


class AsyncPluginResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPluginResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/#accessing-raw-response-data-eg-headers
        """
        return AsyncPluginResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPluginResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/#with_streaming_response
        """
        return AsyncPluginResourceWithStreamingResponse(self)

    async def update(
        self,
        *,
        targets: SequenceNotStr[str],
        location: Optional[plugin_update_params.Location] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Update package plugins concurrently and notify active locations to reload them.
        Responds once every update has finished; fails when any update fails.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/api/plugin/update",
            body=await async_maybe_transform({"targets": targets}, plugin_update_params.PluginUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"location": location}, plugin_update_params.PluginUpdateParams),
            ),
            cast_to=NoneType,
        )

    async def list(
        self,
        *,
        location: Optional[plugin_list_params.Location] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PluginListResponse:
        """
        Retrieve enabled server plugins and their current status.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/api/plugin",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"location": location}, plugin_list_params.PluginListParams),
            ),
            cast_to=PluginListResponse,
        )

    async def check(
        self,
        *,
        location: Optional[plugin_check_params.Location] | Omit = omit,
        target: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PluginCheckResponse:
        """
        Check one or all package plugins for available updates.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/plugin/check",
            body=await async_maybe_transform({"target": target}, plugin_check_params.PluginCheckParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"location": location}, plugin_check_params.PluginCheckParams),
            ),
            cast_to=PluginCheckResponse,
        )


class PluginResourceWithRawResponse:
    def __init__(self, plugin: PluginResource) -> None:
        self._plugin = plugin

        self.update = to_raw_response_wrapper(
            plugin.update,
        )
        self.list = to_raw_response_wrapper(
            plugin.list,
        )
        self.check = to_raw_response_wrapper(
            plugin.check,
        )


class AsyncPluginResourceWithRawResponse:
    def __init__(self, plugin: AsyncPluginResource) -> None:
        self._plugin = plugin

        self.update = async_to_raw_response_wrapper(
            plugin.update,
        )
        self.list = async_to_raw_response_wrapper(
            plugin.list,
        )
        self.check = async_to_raw_response_wrapper(
            plugin.check,
        )


class PluginResourceWithStreamingResponse:
    def __init__(self, plugin: PluginResource) -> None:
        self._plugin = plugin

        self.update = to_streamed_response_wrapper(
            plugin.update,
        )
        self.list = to_streamed_response_wrapper(
            plugin.list,
        )
        self.check = to_streamed_response_wrapper(
            plugin.check,
        )


class AsyncPluginResourceWithStreamingResponse:
    def __init__(self, plugin: AsyncPluginResource) -> None:
        self._plugin = plugin

        self.update = async_to_streamed_response_wrapper(
            plugin.update,
        )
        self.list = async_to_streamed_response_wrapper(
            plugin.list,
        )
        self.check = async_to_streamed_response_wrapper(
            plugin.check,
        )
