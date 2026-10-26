# File generated from our OpenAPI spec by Ferrule. See CONTRIBUTING.md for details.

from __future__ import annotations

from .entry import (
    EntryResource,
    AsyncEntryResource,
    EntryResourceWithRawResponse,
    AsyncEntryResourceWithRawResponse,
    EntryResourceWithStreamingResponse,
    AsyncEntryResourceWithStreamingResponse,
)
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["InstructionsResource", "AsyncInstructionsResource"]


class InstructionsResource(SyncAPIResource):
    @cached_property
    def entry(self) -> EntryResource:
        return EntryResource(self._client)

    @cached_property
    def with_raw_response(self) -> InstructionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/#accessing-raw-response-data-eg-headers
        """
        return InstructionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> InstructionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/#with_streaming_response
        """
        return InstructionsResourceWithStreamingResponse(self)


class AsyncInstructionsResource(AsyncAPIResource):
    @cached_property
    def entry(self) -> AsyncEntryResource:
        return AsyncEntryResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncInstructionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/#accessing-raw-response-data-eg-headers
        """
        return AsyncInstructionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncInstructionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/#with_streaming_response
        """
        return AsyncInstructionsResourceWithStreamingResponse(self)


class InstructionsResourceWithRawResponse:
    def __init__(self, instructions: InstructionsResource) -> None:
        self._instructions = instructions

    @cached_property
    def entry(self) -> EntryResourceWithRawResponse:
        return EntryResourceWithRawResponse(self._instructions.entry)


class AsyncInstructionsResourceWithRawResponse:
    def __init__(self, instructions: AsyncInstructionsResource) -> None:
        self._instructions = instructions

    @cached_property
    def entry(self) -> AsyncEntryResourceWithRawResponse:
        return AsyncEntryResourceWithRawResponse(self._instructions.entry)


class InstructionsResourceWithStreamingResponse:
    def __init__(self, instructions: InstructionsResource) -> None:
        self._instructions = instructions

    @cached_property
    def entry(self) -> EntryResourceWithStreamingResponse:
        return EntryResourceWithStreamingResponse(self._instructions.entry)


class AsyncInstructionsResourceWithStreamingResponse:
    def __init__(self, instructions: AsyncInstructionsResource) -> None:
        self._instructions = instructions

    @cached_property
    def entry(self) -> AsyncEntryResourceWithStreamingResponse:
        return AsyncEntryResourceWithStreamingResponse(self._instructions.entry)
