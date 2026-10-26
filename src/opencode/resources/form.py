# File generated from our OpenAPI spec by Ferrule. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

import httpx

from ..types import form_list_params
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
from ..types.form_list_response import FormListResponse

__all__ = ["FormResource", "AsyncFormResource"]


class FormResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> FormResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/#accessing-raw-response-data-eg-headers
        """
        return FormResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> FormResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/#with_streaming_response
        """
        return FormResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        location: Optional[form_list_params.Location] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FormListResponse:
        """
        Retrieve pending forms for a location.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/api/form",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"location": location}, form_list_params.FormListParams),
            ),
            cast_to=FormListResponse,
        )


class AsyncFormResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncFormResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/#accessing-raw-response-data-eg-headers
        """
        return AsyncFormResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncFormResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/#with_streaming_response
        """
        return AsyncFormResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        location: Optional[form_list_params.Location] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FormListResponse:
        """
        Retrieve pending forms for a location.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/api/form",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"location": location}, form_list_params.FormListParams),
            ),
            cast_to=FormListResponse,
        )


class FormResourceWithRawResponse:
    def __init__(self, form: FormResource) -> None:
        self._form = form

        self.list = to_raw_response_wrapper(
            form.list,
        )


class AsyncFormResourceWithRawResponse:
    def __init__(self, form: AsyncFormResource) -> None:
        self._form = form

        self.list = async_to_raw_response_wrapper(
            form.list,
        )


class FormResourceWithStreamingResponse:
    def __init__(self, form: FormResource) -> None:
        self._form = form

        self.list = to_streamed_response_wrapper(
            form.list,
        )


class AsyncFormResourceWithStreamingResponse:
    def __init__(self, form: AsyncFormResource) -> None:
        self._form = form

        self.list = async_to_streamed_response_wrapper(
            form.list,
        )
