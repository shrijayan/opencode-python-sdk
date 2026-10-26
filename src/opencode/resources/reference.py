# File generated from our OpenAPI spec by Ferrule. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

import httpx

from ..types import reference_list_params
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
from ..types.reference_list_response import ReferenceListResponse

__all__ = ["ReferenceResource", "AsyncReferenceResource"]


class ReferenceResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ReferenceResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/#accessing-raw-response-data-eg-headers
        """
        return ReferenceResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ReferenceResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/#with_streaming_response
        """
        return ReferenceResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        location: Optional[reference_list_params.Location] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ReferenceListResponse:
        """
        List references available in the requested location.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/api/reference",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"location": location}, reference_list_params.ReferenceListParams),
            ),
            cast_to=ReferenceListResponse,
        )


class AsyncReferenceResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncReferenceResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/#accessing-raw-response-data-eg-headers
        """
        return AsyncReferenceResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncReferenceResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/#with_streaming_response
        """
        return AsyncReferenceResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        location: Optional[reference_list_params.Location] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ReferenceListResponse:
        """
        List references available in the requested location.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/api/reference",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"location": location}, reference_list_params.ReferenceListParams),
            ),
            cast_to=ReferenceListResponse,
        )


class ReferenceResourceWithRawResponse:
    def __init__(self, reference: ReferenceResource) -> None:
        self._reference = reference

        self.list = to_raw_response_wrapper(
            reference.list,
        )


class AsyncReferenceResourceWithRawResponse:
    def __init__(self, reference: AsyncReferenceResource) -> None:
        self._reference = reference

        self.list = async_to_raw_response_wrapper(
            reference.list,
        )


class ReferenceResourceWithStreamingResponse:
    def __init__(self, reference: ReferenceResource) -> None:
        self._reference = reference

        self.list = to_streamed_response_wrapper(
            reference.list,
        )


class AsyncReferenceResourceWithStreamingResponse:
    def __init__(self, reference: AsyncReferenceResource) -> None:
        self._reference = reference

        self.list = async_to_streamed_response_wrapper(
            reference.list,
        )
