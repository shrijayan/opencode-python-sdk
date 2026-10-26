# File generated from our OpenAPI spec by Ferrule. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

import httpx

from ..types import model_list_params, model_default_params
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
from ..types.model_list_response import ModelListResponse
from ..types.model_default_response import ModelDefaultResponse

__all__ = ["ModelResource", "AsyncModelResource"]


class ModelResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ModelResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/#accessing-raw-response-data-eg-headers
        """
        return ModelResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ModelResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/#with_streaming_response
        """
        return ModelResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        location: Optional[model_list_params.Location] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ModelListResponse:
        """
        Retrieve the current snapshot of available models ordered by release date. The
        snapshot may precede initial plugin settlement.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/api/model",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"location": location}, model_list_params.ModelListParams),
            ),
            cast_to=ModelListResponse,
        )

    def default(
        self,
        *,
        location: Optional[model_default_params.Location] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ModelDefaultResponse:
        """
        Retrieve the model used when a session has no explicit model selection.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/api/model/default",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"location": location}, model_default_params.ModelDefaultParams),
            ),
            cast_to=ModelDefaultResponse,
        )


class AsyncModelResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncModelResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/#accessing-raw-response-data-eg-headers
        """
        return AsyncModelResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncModelResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/#with_streaming_response
        """
        return AsyncModelResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        location: Optional[model_list_params.Location] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ModelListResponse:
        """
        Retrieve the current snapshot of available models ordered by release date. The
        snapshot may precede initial plugin settlement.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/api/model",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"location": location}, model_list_params.ModelListParams),
            ),
            cast_to=ModelListResponse,
        )

    async def default(
        self,
        *,
        location: Optional[model_default_params.Location] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ModelDefaultResponse:
        """
        Retrieve the model used when a session has no explicit model selection.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/api/model/default",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"location": location}, model_default_params.ModelDefaultParams),
            ),
            cast_to=ModelDefaultResponse,
        )


class ModelResourceWithRawResponse:
    def __init__(self, model: ModelResource) -> None:
        self._model = model

        self.list = to_raw_response_wrapper(
            model.list,
        )
        self.default = to_raw_response_wrapper(
            model.default,
        )


class AsyncModelResourceWithRawResponse:
    def __init__(self, model: AsyncModelResource) -> None:
        self._model = model

        self.list = async_to_raw_response_wrapper(
            model.list,
        )
        self.default = async_to_raw_response_wrapper(
            model.default,
        )


class ModelResourceWithStreamingResponse:
    def __init__(self, model: ModelResource) -> None:
        self._model = model

        self.list = to_streamed_response_wrapper(
            model.list,
        )
        self.default = to_streamed_response_wrapper(
            model.default,
        )


class AsyncModelResourceWithStreamingResponse:
    def __init__(self, model: AsyncModelResource) -> None:
        self._model = model

        self.list = async_to_streamed_response_wrapper(
            model.list,
        )
        self.default = async_to_streamed_response_wrapper(
            model.default,
        )
