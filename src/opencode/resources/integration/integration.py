# File generated from our OpenAPI spec by Ferrule. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

import httpx

from .oauth import (
    OauthResource,
    AsyncOauthResource,
    OauthResourceWithRawResponse,
    AsyncOauthResourceWithRawResponse,
    OauthResourceWithStreamingResponse,
    AsyncOauthResourceWithStreamingResponse,
)
from ...types import integration_get_params, integration_list_params
from .command import (
    CommandResource,
    AsyncCommandResource,
    CommandResourceWithRawResponse,
    AsyncCommandResourceWithRawResponse,
    CommandResourceWithStreamingResponse,
    AsyncCommandResourceWithStreamingResponse,
)
from .connect import (
    ConnectResource,
    AsyncConnectResource,
    ConnectResourceWithRawResponse,
    AsyncConnectResourceWithRawResponse,
    ConnectResourceWithStreamingResponse,
    AsyncConnectResourceWithStreamingResponse,
)
from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import path_template, maybe_transform, async_maybe_transform
from ..._compat import cached_property
from .wellknown import (
    WellknownResource,
    AsyncWellknownResource,
    WellknownResourceWithRawResponse,
    AsyncWellknownResourceWithRawResponse,
    WellknownResourceWithStreamingResponse,
    AsyncWellknownResourceWithStreamingResponse,
)
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.shared.integration_id import IntegrationID
from ...types.integration_get_response import IntegrationGetResponse
from ...types.integration_list_response import IntegrationListResponse

__all__ = ["IntegrationResource", "AsyncIntegrationResource"]


class IntegrationResource(SyncAPIResource):
    @cached_property
    def wellknown(self) -> WellknownResource:
        return WellknownResource(self._client)

    @cached_property
    def connect(self) -> ConnectResource:
        return ConnectResource(self._client)

    @cached_property
    def oauth(self) -> OauthResource:
        return OauthResource(self._client)

    @cached_property
    def command(self) -> CommandResource:
        return CommandResource(self._client)

    @cached_property
    def with_raw_response(self) -> IntegrationResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/#accessing-raw-response-data-eg-headers
        """
        return IntegrationResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> IntegrationResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/#with_streaming_response
        """
        return IntegrationResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        location: Optional[integration_list_params.Location] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> IntegrationListResponse:
        """
        Retrieve available integrations and their authentication methods.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/api/integration",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"location": location}, integration_list_params.IntegrationListParams),
            ),
            cast_to=IntegrationListResponse,
        )

    def get(
        self,
        integration_id: IntegrationID,
        *,
        location: Optional[integration_get_params.Location] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> IntegrationGetResponse:
        """
        Retrieve one integration and its authentication methods.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not integration_id:
            raise ValueError(f"Expected a non-empty value for `integration_id` but received {integration_id!r}")
        return self._get(
            path_template("/api/integration/{integration_id}", integration_id=integration_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"location": location}, integration_get_params.IntegrationGetParams),
            ),
            cast_to=IntegrationGetResponse,
        )


class AsyncIntegrationResource(AsyncAPIResource):
    @cached_property
    def wellknown(self) -> AsyncWellknownResource:
        return AsyncWellknownResource(self._client)

    @cached_property
    def connect(self) -> AsyncConnectResource:
        return AsyncConnectResource(self._client)

    @cached_property
    def oauth(self) -> AsyncOauthResource:
        return AsyncOauthResource(self._client)

    @cached_property
    def command(self) -> AsyncCommandResource:
        return AsyncCommandResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncIntegrationResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/#accessing-raw-response-data-eg-headers
        """
        return AsyncIntegrationResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncIntegrationResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/#with_streaming_response
        """
        return AsyncIntegrationResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        location: Optional[integration_list_params.Location] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> IntegrationListResponse:
        """
        Retrieve available integrations and their authentication methods.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/api/integration",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"location": location}, integration_list_params.IntegrationListParams
                ),
            ),
            cast_to=IntegrationListResponse,
        )

    async def get(
        self,
        integration_id: IntegrationID,
        *,
        location: Optional[integration_get_params.Location] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> IntegrationGetResponse:
        """
        Retrieve one integration and its authentication methods.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not integration_id:
            raise ValueError(f"Expected a non-empty value for `integration_id` but received {integration_id!r}")
        return await self._get(
            path_template("/api/integration/{integration_id}", integration_id=integration_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"location": location}, integration_get_params.IntegrationGetParams),
            ),
            cast_to=IntegrationGetResponse,
        )


class IntegrationResourceWithRawResponse:
    def __init__(self, integration: IntegrationResource) -> None:
        self._integration = integration

        self.list = to_raw_response_wrapper(
            integration.list,
        )
        self.get = to_raw_response_wrapper(
            integration.get,
        )

    @cached_property
    def wellknown(self) -> WellknownResourceWithRawResponse:
        return WellknownResourceWithRawResponse(self._integration.wellknown)

    @cached_property
    def connect(self) -> ConnectResourceWithRawResponse:
        return ConnectResourceWithRawResponse(self._integration.connect)

    @cached_property
    def oauth(self) -> OauthResourceWithRawResponse:
        return OauthResourceWithRawResponse(self._integration.oauth)

    @cached_property
    def command(self) -> CommandResourceWithRawResponse:
        return CommandResourceWithRawResponse(self._integration.command)


class AsyncIntegrationResourceWithRawResponse:
    def __init__(self, integration: AsyncIntegrationResource) -> None:
        self._integration = integration

        self.list = async_to_raw_response_wrapper(
            integration.list,
        )
        self.get = async_to_raw_response_wrapper(
            integration.get,
        )

    @cached_property
    def wellknown(self) -> AsyncWellknownResourceWithRawResponse:
        return AsyncWellknownResourceWithRawResponse(self._integration.wellknown)

    @cached_property
    def connect(self) -> AsyncConnectResourceWithRawResponse:
        return AsyncConnectResourceWithRawResponse(self._integration.connect)

    @cached_property
    def oauth(self) -> AsyncOauthResourceWithRawResponse:
        return AsyncOauthResourceWithRawResponse(self._integration.oauth)

    @cached_property
    def command(self) -> AsyncCommandResourceWithRawResponse:
        return AsyncCommandResourceWithRawResponse(self._integration.command)


class IntegrationResourceWithStreamingResponse:
    def __init__(self, integration: IntegrationResource) -> None:
        self._integration = integration

        self.list = to_streamed_response_wrapper(
            integration.list,
        )
        self.get = to_streamed_response_wrapper(
            integration.get,
        )

    @cached_property
    def wellknown(self) -> WellknownResourceWithStreamingResponse:
        return WellknownResourceWithStreamingResponse(self._integration.wellknown)

    @cached_property
    def connect(self) -> ConnectResourceWithStreamingResponse:
        return ConnectResourceWithStreamingResponse(self._integration.connect)

    @cached_property
    def oauth(self) -> OauthResourceWithStreamingResponse:
        return OauthResourceWithStreamingResponse(self._integration.oauth)

    @cached_property
    def command(self) -> CommandResourceWithStreamingResponse:
        return CommandResourceWithStreamingResponse(self._integration.command)


class AsyncIntegrationResourceWithStreamingResponse:
    def __init__(self, integration: AsyncIntegrationResource) -> None:
        self._integration = integration

        self.list = async_to_streamed_response_wrapper(
            integration.list,
        )
        self.get = async_to_streamed_response_wrapper(
            integration.get,
        )

    @cached_property
    def wellknown(self) -> AsyncWellknownResourceWithStreamingResponse:
        return AsyncWellknownResourceWithStreamingResponse(self._integration.wellknown)

    @cached_property
    def connect(self) -> AsyncConnectResourceWithStreamingResponse:
        return AsyncConnectResourceWithStreamingResponse(self._integration.connect)

    @cached_property
    def oauth(self) -> AsyncOauthResourceWithStreamingResponse:
        return AsyncOauthResourceWithStreamingResponse(self._integration.oauth)

    @cached_property
    def command(self) -> AsyncCommandResourceWithStreamingResponse:
        return AsyncCommandResourceWithStreamingResponse(self._integration.command)
