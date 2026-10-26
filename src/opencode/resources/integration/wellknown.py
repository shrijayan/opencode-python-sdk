# File generated from our OpenAPI spec by Ferrule. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

import httpx

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
from ...types.integration import wellknown_add_params

__all__ = ["WellknownResource", "AsyncWellknownResource"]


class WellknownResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> WellknownResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/#accessing-raw-response-data-eg-headers
        """
        return WellknownResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> WellknownResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/#with_streaming_response
        """
        return WellknownResourceWithStreamingResponse(self)

    def add(
        self,
        *,
        url: str,
        location: Optional[wellknown_add_params.Location] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Discover and persist an experimental wellknown integration source.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/api/experimental/integration/wellknown",
            body=maybe_transform({"url": url}, wellknown_add_params.WellknownAddParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"location": location}, wellknown_add_params.WellknownAddParams),
            ),
            cast_to=NoneType,
        )


class AsyncWellknownResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncWellknownResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/#accessing-raw-response-data-eg-headers
        """
        return AsyncWellknownResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncWellknownResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/#with_streaming_response
        """
        return AsyncWellknownResourceWithStreamingResponse(self)

    async def add(
        self,
        *,
        url: str,
        location: Optional[wellknown_add_params.Location] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Discover and persist an experimental wellknown integration source.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/api/experimental/integration/wellknown",
            body=await async_maybe_transform({"url": url}, wellknown_add_params.WellknownAddParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"location": location}, wellknown_add_params.WellknownAddParams),
            ),
            cast_to=NoneType,
        )


class WellknownResourceWithRawResponse:
    def __init__(self, wellknown: WellknownResource) -> None:
        self._wellknown = wellknown

        self.add = to_raw_response_wrapper(
            wellknown.add,
        )


class AsyncWellknownResourceWithRawResponse:
    def __init__(self, wellknown: AsyncWellknownResource) -> None:
        self._wellknown = wellknown

        self.add = async_to_raw_response_wrapper(
            wellknown.add,
        )


class WellknownResourceWithStreamingResponse:
    def __init__(self, wellknown: WellknownResource) -> None:
        self._wellknown = wellknown

        self.add = to_streamed_response_wrapper(
            wellknown.add,
        )


class AsyncWellknownResourceWithStreamingResponse:
    def __init__(self, wellknown: AsyncWellknownResource) -> None:
        self._wellknown = wellknown

        self.add = async_to_streamed_response_wrapper(
            wellknown.add,
        )
