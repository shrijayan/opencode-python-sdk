# File generated from our OpenAPI spec by Ferrule. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

import httpx

from ..types import websearch_query_params, websearch_providers_params
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
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
from ..types.shared.web_search_id import WebSearchID
from ..types.websearch_query_response import WebsearchQueryResponse
from ..types.websearch_providers_response import WebsearchProvidersResponse

__all__ = ["WebsearchResource", "AsyncWebsearchResource"]


class WebsearchResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> WebsearchResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/#accessing-raw-response-data-eg-headers
        """
        return WebsearchResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> WebsearchResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/#with_streaming_response
        """
        return WebsearchResourceWithStreamingResponse(self)

    def providers(
        self,
        *,
        location: Optional[websearch_providers_params.Location] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WebsearchProvidersResponse:
        """
        Return the registered web search providers.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/api/websearch/provider",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"location": location}, websearch_providers_params.WebsearchProvidersParams),
            ),
            cast_to=WebsearchProvidersResponse,
        )

    def query(
        self,
        *,
        query: str,
        location: Optional[websearch_query_params.Location] | Omit = omit,
        provider_id: WebSearchID | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WebsearchQueryResponse:
        """
        Run one web search through the selected provider. Specify a provider to override
        the configured default.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/websearch",
            body=maybe_transform(
                {
                    "query": query,
                    "provider_id": provider_id,
                },
                websearch_query_params.WebsearchQueryParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"location": location}, websearch_query_params.WebsearchQueryParams),
            ),
            cast_to=WebsearchQueryResponse,
        )


class AsyncWebsearchResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncWebsearchResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/#accessing-raw-response-data-eg-headers
        """
        return AsyncWebsearchResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncWebsearchResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/#with_streaming_response
        """
        return AsyncWebsearchResourceWithStreamingResponse(self)

    async def providers(
        self,
        *,
        location: Optional[websearch_providers_params.Location] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WebsearchProvidersResponse:
        """
        Return the registered web search providers.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/api/websearch/provider",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"location": location}, websearch_providers_params.WebsearchProvidersParams
                ),
            ),
            cast_to=WebsearchProvidersResponse,
        )

    async def query(
        self,
        *,
        query: str,
        location: Optional[websearch_query_params.Location] | Omit = omit,
        provider_id: WebSearchID | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WebsearchQueryResponse:
        """
        Run one web search through the selected provider. Specify a provider to override
        the configured default.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/websearch",
            body=await async_maybe_transform(
                {
                    "query": query,
                    "provider_id": provider_id,
                },
                websearch_query_params.WebsearchQueryParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"location": location}, websearch_query_params.WebsearchQueryParams),
            ),
            cast_to=WebsearchQueryResponse,
        )


class WebsearchResourceWithRawResponse:
    def __init__(self, websearch: WebsearchResource) -> None:
        self._websearch = websearch

        self.providers = to_raw_response_wrapper(
            websearch.providers,
        )
        self.query = to_raw_response_wrapper(
            websearch.query,
        )


class AsyncWebsearchResourceWithRawResponse:
    def __init__(self, websearch: AsyncWebsearchResource) -> None:
        self._websearch = websearch

        self.providers = async_to_raw_response_wrapper(
            websearch.providers,
        )
        self.query = async_to_raw_response_wrapper(
            websearch.query,
        )


class WebsearchResourceWithStreamingResponse:
    def __init__(self, websearch: WebsearchResource) -> None:
        self._websearch = websearch

        self.providers = to_streamed_response_wrapper(
            websearch.providers,
        )
        self.query = to_streamed_response_wrapper(
            websearch.query,
        )


class AsyncWebsearchResourceWithStreamingResponse:
    def __init__(self, websearch: AsyncWebsearchResource) -> None:
        self._websearch = websearch

        self.providers = async_to_streamed_response_wrapper(
            websearch.providers,
        )
        self.query = async_to_streamed_response_wrapper(
            websearch.query,
        )
