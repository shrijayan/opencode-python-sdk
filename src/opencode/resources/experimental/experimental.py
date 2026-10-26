# File generated from our OpenAPI spec by Ferrule. See CONTRIBUTING.md for details.

from __future__ import annotations

from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from .persistent_pty import (
    PersistentPtyResource,
    AsyncPersistentPtyResource,
    PersistentPtyResourceWithRawResponse,
    AsyncPersistentPtyResourceWithRawResponse,
    PersistentPtyResourceWithStreamingResponse,
    AsyncPersistentPtyResourceWithStreamingResponse,
)

__all__ = ["ExperimentalResource", "AsyncExperimentalResource"]


class ExperimentalResource(SyncAPIResource):
    @cached_property
    def persistent_pty(self) -> PersistentPtyResource:
        return PersistentPtyResource(self._client)

    @cached_property
    def with_raw_response(self) -> ExperimentalResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/#accessing-raw-response-data-eg-headers
        """
        return ExperimentalResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ExperimentalResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/#with_streaming_response
        """
        return ExperimentalResourceWithStreamingResponse(self)


class AsyncExperimentalResource(AsyncAPIResource):
    @cached_property
    def persistent_pty(self) -> AsyncPersistentPtyResource:
        return AsyncPersistentPtyResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncExperimentalResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/#accessing-raw-response-data-eg-headers
        """
        return AsyncExperimentalResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncExperimentalResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/#with_streaming_response
        """
        return AsyncExperimentalResourceWithStreamingResponse(self)


class ExperimentalResourceWithRawResponse:
    def __init__(self, experimental: ExperimentalResource) -> None:
        self._experimental = experimental

    @cached_property
    def persistent_pty(self) -> PersistentPtyResourceWithRawResponse:
        return PersistentPtyResourceWithRawResponse(self._experimental.persistent_pty)


class AsyncExperimentalResourceWithRawResponse:
    def __init__(self, experimental: AsyncExperimentalResource) -> None:
        self._experimental = experimental

    @cached_property
    def persistent_pty(self) -> AsyncPersistentPtyResourceWithRawResponse:
        return AsyncPersistentPtyResourceWithRawResponse(self._experimental.persistent_pty)


class ExperimentalResourceWithStreamingResponse:
    def __init__(self, experimental: ExperimentalResource) -> None:
        self._experimental = experimental

    @cached_property
    def persistent_pty(self) -> PersistentPtyResourceWithStreamingResponse:
        return PersistentPtyResourceWithStreamingResponse(self._experimental.persistent_pty)


class AsyncExperimentalResourceWithStreamingResponse:
    def __init__(self, experimental: AsyncExperimentalResource) -> None:
        self._experimental = experimental

    @cached_property
    def persistent_pty(self) -> AsyncPersistentPtyResourceWithStreamingResponse:
        return AsyncPersistentPtyResourceWithStreamingResponse(self._experimental.persistent_pty)
