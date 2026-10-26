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
from ...types.integration import command_cancel_params, command_status_params, command_connect_params
from ...types.shared_params.integration_id import IntegrationID
from ...types.integration.command_status_response import CommandStatusResponse
from ...types.shared_params.integration_method_id import IntegrationMethodID
from ...types.integration.command_connect_response import CommandConnectResponse
from ...types.shared_params.integration_attempt_id import IntegrationAttemptID

__all__ = ["CommandResource", "AsyncCommandResource"]


class CommandResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CommandResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/#accessing-raw-response-data-eg-headers
        """
        return CommandResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CommandResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/#with_streaming_response
        """
        return CommandResourceWithStreamingResponse(self)

    def cancel(
        self,
        attempt_id: IntegrationAttemptID,
        *,
        integration_id: IntegrationID,
        location: Optional[command_cancel_params.Location] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Cancel a command authentication attempt and terminate its process.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not integration_id:
            raise ValueError(f"Expected a non-empty value for `integration_id` but received {integration_id!r}")
        if not attempt_id:
            raise ValueError(f"Expected a non-empty value for `attempt_id` but received {attempt_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            path_template(
                "/api/integration/{integration_id}/connect/command/{attempt_id}",
                integration_id=integration_id,
                attempt_id=attempt_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"location": location}, command_cancel_params.CommandCancelParams),
            ),
            cast_to=NoneType,
        )

    def connect(
        self,
        integration_id: IntegrationID,
        *,
        method_id: IntegrationMethodID,
        label: Optional[str] | Omit = omit,
        location: Optional[command_connect_params.Location] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CommandConnectResponse:
        """
        Start a command authentication attempt.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not integration_id:
            raise ValueError(f"Expected a non-empty value for `integration_id` but received {integration_id!r}")
        return self._post(
            path_template("/api/integration/{integration_id}/connect/command", integration_id=integration_id),
            body=maybe_transform(
                {
                    "method_id": method_id,
                    "label": label,
                },
                command_connect_params.CommandConnectParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"location": location}, command_connect_params.CommandConnectParams),
            ),
            cast_to=CommandConnectResponse,
        )

    def status(
        self,
        attempt_id: IntegrationAttemptID,
        *,
        integration_id: IntegrationID,
        location: Optional[command_status_params.Location] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CommandStatusResponse:
        """
        Poll the current status and output of a command authentication attempt.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not integration_id:
            raise ValueError(f"Expected a non-empty value for `integration_id` but received {integration_id!r}")
        if not attempt_id:
            raise ValueError(f"Expected a non-empty value for `attempt_id` but received {attempt_id!r}")
        return self._get(
            path_template(
                "/api/integration/{integration_id}/connect/command/{attempt_id}",
                integration_id=integration_id,
                attempt_id=attempt_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"location": location}, command_status_params.CommandStatusParams),
            ),
            cast_to=CommandStatusResponse,
        )


class AsyncCommandResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCommandResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/#accessing-raw-response-data-eg-headers
        """
        return AsyncCommandResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCommandResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/#with_streaming_response
        """
        return AsyncCommandResourceWithStreamingResponse(self)

    async def cancel(
        self,
        attempt_id: IntegrationAttemptID,
        *,
        integration_id: IntegrationID,
        location: Optional[command_cancel_params.Location] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Cancel a command authentication attempt and terminate its process.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not integration_id:
            raise ValueError(f"Expected a non-empty value for `integration_id` but received {integration_id!r}")
        if not attempt_id:
            raise ValueError(f"Expected a non-empty value for `attempt_id` but received {attempt_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            path_template(
                "/api/integration/{integration_id}/connect/command/{attempt_id}",
                integration_id=integration_id,
                attempt_id=attempt_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"location": location}, command_cancel_params.CommandCancelParams),
            ),
            cast_to=NoneType,
        )

    async def connect(
        self,
        integration_id: IntegrationID,
        *,
        method_id: IntegrationMethodID,
        label: Optional[str] | Omit = omit,
        location: Optional[command_connect_params.Location] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CommandConnectResponse:
        """
        Start a command authentication attempt.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not integration_id:
            raise ValueError(f"Expected a non-empty value for `integration_id` but received {integration_id!r}")
        return await self._post(
            path_template("/api/integration/{integration_id}/connect/command", integration_id=integration_id),
            body=await async_maybe_transform(
                {
                    "method_id": method_id,
                    "label": label,
                },
                command_connect_params.CommandConnectParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"location": location}, command_connect_params.CommandConnectParams),
            ),
            cast_to=CommandConnectResponse,
        )

    async def status(
        self,
        attempt_id: IntegrationAttemptID,
        *,
        integration_id: IntegrationID,
        location: Optional[command_status_params.Location] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CommandStatusResponse:
        """
        Poll the current status and output of a command authentication attempt.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not integration_id:
            raise ValueError(f"Expected a non-empty value for `integration_id` but received {integration_id!r}")
        if not attempt_id:
            raise ValueError(f"Expected a non-empty value for `attempt_id` but received {attempt_id!r}")
        return await self._get(
            path_template(
                "/api/integration/{integration_id}/connect/command/{attempt_id}",
                integration_id=integration_id,
                attempt_id=attempt_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"location": location}, command_status_params.CommandStatusParams),
            ),
            cast_to=CommandStatusResponse,
        )


class CommandResourceWithRawResponse:
    def __init__(self, command: CommandResource) -> None:
        self._command = command

        self.cancel = to_raw_response_wrapper(
            command.cancel,
        )
        self.connect = to_raw_response_wrapper(
            command.connect,
        )
        self.status = to_raw_response_wrapper(
            command.status,
        )


class AsyncCommandResourceWithRawResponse:
    def __init__(self, command: AsyncCommandResource) -> None:
        self._command = command

        self.cancel = async_to_raw_response_wrapper(
            command.cancel,
        )
        self.connect = async_to_raw_response_wrapper(
            command.connect,
        )
        self.status = async_to_raw_response_wrapper(
            command.status,
        )


class CommandResourceWithStreamingResponse:
    def __init__(self, command: CommandResource) -> None:
        self._command = command

        self.cancel = to_streamed_response_wrapper(
            command.cancel,
        )
        self.connect = to_streamed_response_wrapper(
            command.connect,
        )
        self.status = to_streamed_response_wrapper(
            command.status,
        )


class AsyncCommandResourceWithStreamingResponse:
    def __init__(self, command: AsyncCommandResource) -> None:
        self._command = command

        self.cancel = async_to_streamed_response_wrapper(
            command.cancel,
        )
        self.connect = async_to_streamed_response_wrapper(
            command.connect,
        )
        self.status = async_to_streamed_response_wrapper(
            command.status,
        )
