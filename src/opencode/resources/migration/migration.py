# File generated from our OpenAPI spec by Ferrule. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .v1 import (
    V1Resource,
    AsyncV1Resource,
    V1ResourceWithRawResponse,
    AsyncV1ResourceWithRawResponse,
    V1ResourceWithStreamingResponse,
    AsyncV1ResourceWithStreamingResponse,
)
from ..._types import Body, Query, Headers, NotGiven, not_given
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["MigrationResource", "AsyncMigrationResource"]


class MigrationResource(SyncAPIResource):
    @cached_property
    def v1(self) -> V1Resource:
        return V1Resource(self._client)

    @cached_property
    def with_raw_response(self) -> MigrationResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/#accessing-raw-response-data-eg-headers
        """
        return MigrationResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> MigrationResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/#with_streaming_response
        """
        return MigrationResourceWithStreamingResponse(self)


class AsyncMigrationResource(AsyncAPIResource):
    @cached_property
    def v1(self) -> AsyncV1Resource:
        return AsyncV1Resource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncMigrationResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/#accessing-raw-response-data-eg-headers
        """
        return AsyncMigrationResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMigrationResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/#with_streaming_response
        """
        return AsyncMigrationResourceWithStreamingResponse(self)


class MigrationResourceWithRawResponse:
    def __init__(self, migration: MigrationResource) -> None:
        self._migration = migration

    @cached_property
    def v1(self) -> V1ResourceWithRawResponse:
        return V1ResourceWithRawResponse(self._migration.v1)


class AsyncMigrationResourceWithRawResponse:
    def __init__(self, migration: AsyncMigrationResource) -> None:
        self._migration = migration

    @cached_property
    def v1(self) -> AsyncV1ResourceWithRawResponse:
        return AsyncV1ResourceWithRawResponse(self._migration.v1)


class MigrationResourceWithStreamingResponse:
    def __init__(self, migration: MigrationResource) -> None:
        self._migration = migration

    @cached_property
    def v1(self) -> V1ResourceWithStreamingResponse:
        return V1ResourceWithStreamingResponse(self._migration.v1)


class AsyncMigrationResourceWithStreamingResponse:
    def __init__(self, migration: AsyncMigrationResource) -> None:
        self._migration = migration

    @cached_property
    def v1(self) -> AsyncV1ResourceWithStreamingResponse:
        return AsyncV1ResourceWithStreamingResponse(self._migration.v1)
