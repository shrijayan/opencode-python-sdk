# File generated from our OpenAPI spec by Ferrule. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

import httpx

from ..types import location_get_params
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
from ..types.shared.location_public_info import LocationPublicInfo

__all__ = ["LocationResource", "AsyncLocationResource"]


class LocationResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> LocationResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/#accessing-raw-response-data-eg-headers
        """
        return LocationResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> LocationResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/#with_streaming_response
        """
        return LocationResourceWithStreamingResponse(self)

    def get(
        self,
        *,
        location: Optional[location_get_params.Location] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LocationPublicInfo:
        """
        Resolve the requested location or the server default location.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/api/location",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"location": location}, location_get_params.LocationGetParams),
            ),
            cast_to=LocationPublicInfo,
        )

    def reload(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Shut down and rebuild every loaded location. Pending permissions and forms are
        cancelled; running sessions continue with fresh services at the next step
        boundary. Emits location.shutdown for client recovery and responds once all
        replacement builds settle.
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/api/location/reload",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncLocationResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncLocationResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/#accessing-raw-response-data-eg-headers
        """
        return AsyncLocationResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncLocationResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/#with_streaming_response
        """
        return AsyncLocationResourceWithStreamingResponse(self)

    async def get(
        self,
        *,
        location: Optional[location_get_params.Location] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LocationPublicInfo:
        """
        Resolve the requested location or the server default location.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/api/location",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"location": location}, location_get_params.LocationGetParams),
            ),
            cast_to=LocationPublicInfo,
        )

    async def reload(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Shut down and rebuild every loaded location. Pending permissions and forms are
        cancelled; running sessions continue with fresh services at the next step
        boundary. Emits location.shutdown for client recovery and responds once all
        replacement builds settle.
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/api/location/reload",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class LocationResourceWithRawResponse:
    def __init__(self, location: LocationResource) -> None:
        self._location = location

        self.get = to_raw_response_wrapper(
            location.get,
        )
        self.reload = to_raw_response_wrapper(
            location.reload,
        )


class AsyncLocationResourceWithRawResponse:
    def __init__(self, location: AsyncLocationResource) -> None:
        self._location = location

        self.get = async_to_raw_response_wrapper(
            location.get,
        )
        self.reload = async_to_raw_response_wrapper(
            location.reload,
        )


class LocationResourceWithStreamingResponse:
    def __init__(self, location: LocationResource) -> None:
        self._location = location

        self.get = to_streamed_response_wrapper(
            location.get,
        )
        self.reload = to_streamed_response_wrapper(
            location.reload,
        )


class AsyncLocationResourceWithStreamingResponse:
    def __init__(self, location: AsyncLocationResource) -> None:
        self._location = location

        self.get = async_to_streamed_response_wrapper(
            location.get,
        )
        self.reload = async_to_streamed_response_wrapper(
            location.reload,
        )
