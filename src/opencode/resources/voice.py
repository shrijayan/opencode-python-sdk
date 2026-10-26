# File generated from our OpenAPI spec by Ferrule. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Type, Optional, cast

import httpx

from ..types import voice_session_params
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
from .._wrappers import DataWrapper
from .._base_client import make_request_options
from ..types.voice_session_response import VoiceSessionResponse
from ..types.shared_params.voice_transport_input import VoiceTransportInput

__all__ = ["VoiceResource", "AsyncVoiceResource"]


class VoiceResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> VoiceResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/#accessing-raw-response-data-eg-headers
        """
        return VoiceResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> VoiceResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/#with_streaming_response
        """
        return VoiceResourceWithStreamingResponse(self)

    def session(
        self,
        *,
        model: str,
        transport: VoiceTransportInput,
        session: Optional[Dict[str, object]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VoiceSessionResponse:
        """
        Create a server-brokered voice session using the server's configured provider
        credentials and return the WebRTC SDP answer or WebSocket ephemeral token.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/experimental/voice/session",
            body=maybe_transform(
                {
                    "model": model,
                    "transport": transport,
                    "session": session,
                },
                voice_session_params.VoiceSessionParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=DataWrapper[VoiceSessionResponse]._unwrapper,
            ),
            cast_to=cast(Type[VoiceSessionResponse], DataWrapper[VoiceSessionResponse]),
        )


class AsyncVoiceResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncVoiceResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/#accessing-raw-response-data-eg-headers
        """
        return AsyncVoiceResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncVoiceResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/#with_streaming_response
        """
        return AsyncVoiceResourceWithStreamingResponse(self)

    async def session(
        self,
        *,
        model: str,
        transport: VoiceTransportInput,
        session: Optional[Dict[str, object]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VoiceSessionResponse:
        """
        Create a server-brokered voice session using the server's configured provider
        credentials and return the WebRTC SDP answer or WebSocket ephemeral token.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/experimental/voice/session",
            body=await async_maybe_transform(
                {
                    "model": model,
                    "transport": transport,
                    "session": session,
                },
                voice_session_params.VoiceSessionParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=DataWrapper[VoiceSessionResponse]._unwrapper,
            ),
            cast_to=cast(Type[VoiceSessionResponse], DataWrapper[VoiceSessionResponse]),
        )


class VoiceResourceWithRawResponse:
    def __init__(self, voice: VoiceResource) -> None:
        self._voice = voice

        self.session = to_raw_response_wrapper(
            voice.session,
        )


class AsyncVoiceResourceWithRawResponse:
    def __init__(self, voice: AsyncVoiceResource) -> None:
        self._voice = voice

        self.session = async_to_raw_response_wrapper(
            voice.session,
        )


class VoiceResourceWithStreamingResponse:
    def __init__(self, voice: VoiceResource) -> None:
        self._voice = voice

        self.session = to_streamed_response_wrapper(
            voice.session,
        )


class AsyncVoiceResourceWithStreamingResponse:
    def __init__(self, voice: AsyncVoiceResource) -> None:
        self._voice = voice

        self.session = async_to_streamed_response_wrapper(
            voice.session,
        )
