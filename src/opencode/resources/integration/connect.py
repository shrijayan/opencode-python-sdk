# File generated from our OpenAPI spec by Ferrule. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

import httpx

from ..._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
from ..._utils import path_template, maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.integration import connect_key_params, connect_external_params
from ...types.shared_params.form_answer import FormAnswer
from ...types.shared_params.integration_id import IntegrationID
from ...types.shared_params.integration_method_id import IntegrationMethodID

__all__ = ["ConnectResource", "AsyncConnectResource"]


class ConnectResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ConnectResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/#accessing-raw-response-data-eg-headers
        """
        return ConnectResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ConnectResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/#with_streaming_response
        """
        return ConnectResourceWithStreamingResponse(self)

    def external(
        self,
        integration_id: IntegrationID,
        *,
        method_id: IntegrationMethodID,
        answer: Optional[FormAnswer] | Omit = omit,
        label: Optional[str] | Omit = omit,
        location: Optional[connect_external_params.Location] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Run an external authentication method and store a reference to its credential
        source.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not integration_id:
            raise ValueError(f"Expected a non-empty value for `integration_id` but received {integration_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            path_template("/api/integration/{integration_id}/connect/external", integration_id=integration_id),
            body=maybe_transform(
                {
                    "method_id": method_id,
                    "answer": answer,
                    "label": label,
                },
                connect_external_params.ConnectExternalParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"location": location}, connect_external_params.ConnectExternalParams),
            ),
            cast_to=NoneType,
        )

    def key(
        self,
        integration_id: IntegrationID,
        *,
        key: str,
        answer: Optional[FormAnswer] | Omit = omit,
        label: Optional[str] | Omit = omit,
        location: Optional[connect_key_params.Location] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Run a key authentication method and store the resulting credential.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not integration_id:
            raise ValueError(f"Expected a non-empty value for `integration_id` but received {integration_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            path_template("/api/integration/{integration_id}/connect/key", integration_id=integration_id),
            body=maybe_transform(
                {
                    "key": key,
                    "answer": answer,
                    "label": label,
                },
                connect_key_params.ConnectKeyParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"location": location}, connect_key_params.ConnectKeyParams),
            ),
            cast_to=NoneType,
        )


class AsyncConnectResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncConnectResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/#accessing-raw-response-data-eg-headers
        """
        return AsyncConnectResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncConnectResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/#with_streaming_response
        """
        return AsyncConnectResourceWithStreamingResponse(self)

    async def external(
        self,
        integration_id: IntegrationID,
        *,
        method_id: IntegrationMethodID,
        answer: Optional[FormAnswer] | Omit = omit,
        label: Optional[str] | Omit = omit,
        location: Optional[connect_external_params.Location] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Run an external authentication method and store a reference to its credential
        source.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not integration_id:
            raise ValueError(f"Expected a non-empty value for `integration_id` but received {integration_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            path_template("/api/integration/{integration_id}/connect/external", integration_id=integration_id),
            body=await async_maybe_transform(
                {
                    "method_id": method_id,
                    "answer": answer,
                    "label": label,
                },
                connect_external_params.ConnectExternalParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"location": location}, connect_external_params.ConnectExternalParams
                ),
            ),
            cast_to=NoneType,
        )

    async def key(
        self,
        integration_id: IntegrationID,
        *,
        key: str,
        answer: Optional[FormAnswer] | Omit = omit,
        label: Optional[str] | Omit = omit,
        location: Optional[connect_key_params.Location] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Run a key authentication method and store the resulting credential.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not integration_id:
            raise ValueError(f"Expected a non-empty value for `integration_id` but received {integration_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            path_template("/api/integration/{integration_id}/connect/key", integration_id=integration_id),
            body=await async_maybe_transform(
                {
                    "key": key,
                    "answer": answer,
                    "label": label,
                },
                connect_key_params.ConnectKeyParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"location": location}, connect_key_params.ConnectKeyParams),
            ),
            cast_to=NoneType,
        )


class ConnectResourceWithRawResponse:
    def __init__(self, connect: ConnectResource) -> None:
        self._connect = connect

        self.external = to_raw_response_wrapper(
            connect.external,
        )
        self.key = to_raw_response_wrapper(
            connect.key,
        )


class AsyncConnectResourceWithRawResponse:
    def __init__(self, connect: AsyncConnectResource) -> None:
        self._connect = connect

        self.external = async_to_raw_response_wrapper(
            connect.external,
        )
        self.key = async_to_raw_response_wrapper(
            connect.key,
        )


class ConnectResourceWithStreamingResponse:
    def __init__(self, connect: ConnectResource) -> None:
        self._connect = connect

        self.external = to_streamed_response_wrapper(
            connect.external,
        )
        self.key = to_streamed_response_wrapper(
            connect.key,
        )


class AsyncConnectResourceWithStreamingResponse:
    def __init__(self, connect: AsyncConnectResource) -> None:
        self._connect = connect

        self.external = async_to_streamed_response_wrapper(
            connect.external,
        )
        self.key = async_to_streamed_response_wrapper(
            connect.key,
        )
