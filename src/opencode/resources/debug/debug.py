# File generated from our OpenAPI spec by Ferrule. See CONTRIBUTING.md for details.

from __future__ import annotations

from .location import (
    LocationResource,
    AsyncLocationResource,
    LocationResourceWithRawResponse,
    AsyncLocationResourceWithRawResponse,
    LocationResourceWithStreamingResponse,
    AsyncLocationResourceWithStreamingResponse,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["DebugResource", "AsyncDebugResource"]


class DebugResource(SyncAPIResource):
    @cached_property
    def location(self) -> LocationResource:
        return LocationResource(self._client)

    @cached_property
    def with_raw_response(self) -> DebugResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/#accessing-raw-response-data-eg-headers
        """
        return DebugResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DebugResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/#with_streaming_response
        """
        return DebugResourceWithStreamingResponse(self)


class AsyncDebugResource(AsyncAPIResource):
    @cached_property
    def location(self) -> AsyncLocationResource:
        return AsyncLocationResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncDebugResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/#accessing-raw-response-data-eg-headers
        """
        return AsyncDebugResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDebugResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/#with_streaming_response
        """
        return AsyncDebugResourceWithStreamingResponse(self)


class DebugResourceWithRawResponse:
    def __init__(self, debug: DebugResource) -> None:
        self._debug = debug

    @cached_property
    def location(self) -> LocationResourceWithRawResponse:
        return LocationResourceWithRawResponse(self._debug.location)


class AsyncDebugResourceWithRawResponse:
    def __init__(self, debug: AsyncDebugResource) -> None:
        self._debug = debug

    @cached_property
    def location(self) -> AsyncLocationResourceWithRawResponse:
        return AsyncLocationResourceWithRawResponse(self._debug.location)


class DebugResourceWithStreamingResponse:
    def __init__(self, debug: DebugResource) -> None:
        self._debug = debug

    @cached_property
    def location(self) -> LocationResourceWithStreamingResponse:
        return LocationResourceWithStreamingResponse(self._debug.location)


class AsyncDebugResourceWithStreamingResponse:
    def __init__(self, debug: AsyncDebugResource) -> None:
        self._debug = debug

    @cached_property
    def location(self) -> AsyncLocationResourceWithStreamingResponse:
        return AsyncLocationResourceWithStreamingResponse(self._debug.location)
