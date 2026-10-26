# File generated from our OpenAPI spec by Ferrule. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

import httpx

from ..types import rpc_call_params
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .._utils import path_template, maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.shared.rpc_output import RpcOutput

__all__ = ["RpcResource", "AsyncRpcResource"]


class RpcResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> RpcResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/#accessing-raw-response-data-eg-headers
        """
        return RpcResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RpcResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/#with_streaming_response
        """
        return RpcResourceWithStreamingResponse(self)

    def call(
        self,
        method: str,
        *,
        rpc_id: str,
        input: object | Omit = omit,
        location: Optional[rpc_call_params.Location] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RpcOutput:
        """
        Dispatch a method to the currently registered RPC at the requested location.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not rpc_id:
            raise ValueError(f"Expected a non-empty value for `rpc_id` but received {rpc_id!r}")
        if not method:
            raise ValueError(f"Expected a non-empty value for `method` but received {method!r}")
        return self._post(
            path_template("/api/rpc/{rpc_id}/{method}", rpc_id=rpc_id, method=method),
            body=maybe_transform({"input": input}, rpc_call_params.RpcCallParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"location": location}, rpc_call_params.RpcCallParams),
            ),
            cast_to=RpcOutput,
        )


class AsyncRpcResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncRpcResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/#accessing-raw-response-data-eg-headers
        """
        return AsyncRpcResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRpcResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/#with_streaming_response
        """
        return AsyncRpcResourceWithStreamingResponse(self)

    async def call(
        self,
        method: str,
        *,
        rpc_id: str,
        input: object | Omit = omit,
        location: Optional[rpc_call_params.Location] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RpcOutput:
        """
        Dispatch a method to the currently registered RPC at the requested location.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not rpc_id:
            raise ValueError(f"Expected a non-empty value for `rpc_id` but received {rpc_id!r}")
        if not method:
            raise ValueError(f"Expected a non-empty value for `method` but received {method!r}")
        return await self._post(
            path_template("/api/rpc/{rpc_id}/{method}", rpc_id=rpc_id, method=method),
            body=await async_maybe_transform({"input": input}, rpc_call_params.RpcCallParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"location": location}, rpc_call_params.RpcCallParams),
            ),
            cast_to=RpcOutput,
        )


class RpcResourceWithRawResponse:
    def __init__(self, rpc: RpcResource) -> None:
        self._rpc = rpc

        self.call = to_raw_response_wrapper(
            rpc.call,
        )


class AsyncRpcResourceWithRawResponse:
    def __init__(self, rpc: AsyncRpcResource) -> None:
        self._rpc = rpc

        self.call = async_to_raw_response_wrapper(
            rpc.call,
        )


class RpcResourceWithStreamingResponse:
    def __init__(self, rpc: RpcResource) -> None:
        self._rpc = rpc

        self.call = to_streamed_response_wrapper(
            rpc.call,
        )


class AsyncRpcResourceWithStreamingResponse:
    def __init__(self, rpc: AsyncRpcResource) -> None:
        self._rpc = rpc

        self.call = async_to_streamed_response_wrapper(
            rpc.call,
        )
