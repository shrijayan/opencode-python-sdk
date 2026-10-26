# File generated from our OpenAPI spec by Ferrule. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .._types import Body, Query, Headers, NotGiven, not_given
from .._utils import path_template
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.shared.server_info import ServerInfo
from ..types.shared.pairing_code import PairingCode
from ..types.shared.pairing_session import PairingSession

__all__ = ["ServerResource", "AsyncServerResource"]


class ServerResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ServerResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/#accessing-raw-response-data-eg-headers
        """
        return ServerResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ServerResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/#with_streaming_response
        """
        return ServerResourceWithStreamingResponse(self)

    def connect(
        self,
        code: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PairingSession:
        """
        Redeem a pairing code. Browsers receive a session cookie and a redirect to the
        web app; requests that accept JSON receive a session token to use as the
        password.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not code:
            raise ValueError(f"Expected a non-empty value for `code` but received {code!r}")
        return self._get(
            path_template("/auth/connect/{code}", code=code),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PairingSession,
        )

    def info(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ServerInfo:
        """Return the server identity, connection URLs, paths, and readiness status."""
        return self._get(
            "/api/info",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ServerInfo,
        )

    def pair(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PairingCode:
        """Create a short-lived, single-use code for a /auth/connect/:code pairing link."""
        return self._post(
            "/api/pair",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PairingCode,
        )


class AsyncServerResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncServerResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/#accessing-raw-response-data-eg-headers
        """
        return AsyncServerResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncServerResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/#with_streaming_response
        """
        return AsyncServerResourceWithStreamingResponse(self)

    async def connect(
        self,
        code: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PairingSession:
        """
        Redeem a pairing code. Browsers receive a session cookie and a redirect to the
        web app; requests that accept JSON receive a session token to use as the
        password.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not code:
            raise ValueError(f"Expected a non-empty value for `code` but received {code!r}")
        return await self._get(
            path_template("/auth/connect/{code}", code=code),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PairingSession,
        )

    async def info(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ServerInfo:
        """Return the server identity, connection URLs, paths, and readiness status."""
        return await self._get(
            "/api/info",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ServerInfo,
        )

    async def pair(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PairingCode:
        """Create a short-lived, single-use code for a /auth/connect/:code pairing link."""
        return await self._post(
            "/api/pair",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PairingCode,
        )


class ServerResourceWithRawResponse:
    def __init__(self, server: ServerResource) -> None:
        self._server = server

        self.connect = to_raw_response_wrapper(
            server.connect,
        )
        self.info = to_raw_response_wrapper(
            server.info,
        )
        self.pair = to_raw_response_wrapper(
            server.pair,
        )


class AsyncServerResourceWithRawResponse:
    def __init__(self, server: AsyncServerResource) -> None:
        self._server = server

        self.connect = async_to_raw_response_wrapper(
            server.connect,
        )
        self.info = async_to_raw_response_wrapper(
            server.info,
        )
        self.pair = async_to_raw_response_wrapper(
            server.pair,
        )


class ServerResourceWithStreamingResponse:
    def __init__(self, server: ServerResource) -> None:
        self._server = server

        self.connect = to_streamed_response_wrapper(
            server.connect,
        )
        self.info = to_streamed_response_wrapper(
            server.info,
        )
        self.pair = to_streamed_response_wrapper(
            server.pair,
        )


class AsyncServerResourceWithStreamingResponse:
    def __init__(self, server: AsyncServerResource) -> None:
        self._server = server

        self.connect = async_to_streamed_response_wrapper(
            server.connect,
        )
        self.info = async_to_streamed_response_wrapper(
            server.info,
        )
        self.pair = async_to_streamed_response_wrapper(
            server.pair,
        )
