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
from ...types.mcp import resource_catalog_params
from ..._base_client import make_request_options
from ...types.mcp.resource_catalog_response import ResourceCatalogResponse

__all__ = ["ResourceResource", "AsyncResourceResource"]


class ResourceResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ResourceResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/#accessing-raw-response-data-eg-headers
        """
        return ResourceResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ResourceResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/#with_streaming_response
        """
        return ResourceResourceWithStreamingResponse(self)

    def catalog(
        self,
        *,
        location: Optional[resource_catalog_params.Location] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ResourceCatalogResponse:
        """
        Retrieve resources and resource templates from connected MCP servers.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/api/mcp/resource",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"location": location}, resource_catalog_params.ResourceCatalogParams),
            ),
            cast_to=ResourceCatalogResponse,
        )


class AsyncResourceResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncResourceResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/#accessing-raw-response-data-eg-headers
        """
        return AsyncResourceResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncResourceResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/#with_streaming_response
        """
        return AsyncResourceResourceWithStreamingResponse(self)

    async def catalog(
        self,
        *,
        location: Optional[resource_catalog_params.Location] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ResourceCatalogResponse:
        """
        Retrieve resources and resource templates from connected MCP servers.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/api/mcp/resource",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"location": location}, resource_catalog_params.ResourceCatalogParams
                ),
            ),
            cast_to=ResourceCatalogResponse,
        )


class ResourceResourceWithRawResponse:
    def __init__(self, resource: ResourceResource) -> None:
        self._resource = resource

        self.catalog = to_raw_response_wrapper(
            resource.catalog,
        )


class AsyncResourceResourceWithRawResponse:
    def __init__(self, resource: AsyncResourceResource) -> None:
        self._resource = resource

        self.catalog = async_to_raw_response_wrapper(
            resource.catalog,
        )


class ResourceResourceWithStreamingResponse:
    def __init__(self, resource: ResourceResource) -> None:
        self._resource = resource

        self.catalog = to_streamed_response_wrapper(
            resource.catalog,
        )


class AsyncResourceResourceWithStreamingResponse:
    def __init__(self, resource: AsyncResourceResource) -> None:
        self._resource = resource

        self.catalog = async_to_streamed_response_wrapper(
            resource.catalog,
        )
