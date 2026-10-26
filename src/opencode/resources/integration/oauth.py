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
from ...types.integration import oauth_cancel_params, oauth_status_params, oauth_connect_params, oauth_complete_params
from ...types.shared.form_answer import FormAnswer
from ...types.shared.integration_id import IntegrationID
from ...types.shared.integration_method_id import IntegrationMethodID
from ...types.shared.integration_attempt_id import IntegrationAttemptID
from ...types.integration.oauth_status_response import OauthStatusResponse
from ...types.integration.oauth_connect_response import OauthConnectResponse

__all__ = ["OauthResource", "AsyncOauthResource"]


class OauthResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> OauthResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/#accessing-raw-response-data-eg-headers
        """
        return OauthResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> OauthResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/#with_streaming_response
        """
        return OauthResourceWithStreamingResponse(self)

    def cancel(
        self,
        attempt_id: IntegrationAttemptID,
        *,
        integration_id: IntegrationID,
        location: Optional[oauth_cancel_params.Location] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Cancel an OAuth attempt and release its resources.

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
                "/api/integration/{integration_id}/connect/oauth/{attempt_id}",
                integration_id=integration_id,
                attempt_id=attempt_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"location": location}, oauth_cancel_params.OauthCancelParams),
            ),
            cast_to=NoneType,
        )

    def complete(
        self,
        attempt_id: IntegrationAttemptID,
        *,
        integration_id: IntegrationID,
        code: Optional[str] | Omit = omit,
        location: Optional[oauth_complete_params.Location] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Complete a code-based OAuth attempt and store the resulting credential.

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
        return self._post(
            path_template(
                "/api/integration/{integration_id}/connect/oauth/{attempt_id}/complete",
                integration_id=integration_id,
                attempt_id=attempt_id,
            ),
            body=maybe_transform({"code": code}, oauth_complete_params.OauthCompleteParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"location": location}, oauth_complete_params.OauthCompleteParams),
            ),
            cast_to=NoneType,
        )

    def connect(
        self,
        integration_id: IntegrationID,
        *,
        method_id: IntegrationMethodID,
        answer: Optional[FormAnswer] | Omit = omit,
        label: Optional[str] | Omit = omit,
        location: Optional[oauth_connect_params.Location] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OauthConnectResponse:
        """
        Start an OAuth attempt and return the authorization details.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not integration_id:
            raise ValueError(f"Expected a non-empty value for `integration_id` but received {integration_id!r}")
        return self._post(
            path_template("/api/integration/{integration_id}/connect/oauth", integration_id=integration_id),
            body=maybe_transform(
                {
                    "method_id": method_id,
                    "answer": answer,
                    "label": label,
                },
                oauth_connect_params.OauthConnectParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"location": location}, oauth_connect_params.OauthConnectParams),
            ),
            cast_to=OauthConnectResponse,
        )

    def status(
        self,
        attempt_id: IntegrationAttemptID,
        *,
        integration_id: IntegrationID,
        location: Optional[oauth_status_params.Location] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OauthStatusResponse:
        """
        Poll the current status of an OAuth attempt.

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
                "/api/integration/{integration_id}/connect/oauth/{attempt_id}",
                integration_id=integration_id,
                attempt_id=attempt_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"location": location}, oauth_status_params.OauthStatusParams),
            ),
            cast_to=OauthStatusResponse,
        )


class AsyncOauthResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncOauthResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/#accessing-raw-response-data-eg-headers
        """
        return AsyncOauthResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncOauthResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/#with_streaming_response
        """
        return AsyncOauthResourceWithStreamingResponse(self)

    async def cancel(
        self,
        attempt_id: IntegrationAttemptID,
        *,
        integration_id: IntegrationID,
        location: Optional[oauth_cancel_params.Location] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Cancel an OAuth attempt and release its resources.

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
                "/api/integration/{integration_id}/connect/oauth/{attempt_id}",
                integration_id=integration_id,
                attempt_id=attempt_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"location": location}, oauth_cancel_params.OauthCancelParams),
            ),
            cast_to=NoneType,
        )

    async def complete(
        self,
        attempt_id: IntegrationAttemptID,
        *,
        integration_id: IntegrationID,
        code: Optional[str] | Omit = omit,
        location: Optional[oauth_complete_params.Location] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Complete a code-based OAuth attempt and store the resulting credential.

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
        return await self._post(
            path_template(
                "/api/integration/{integration_id}/connect/oauth/{attempt_id}/complete",
                integration_id=integration_id,
                attempt_id=attempt_id,
            ),
            body=await async_maybe_transform({"code": code}, oauth_complete_params.OauthCompleteParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"location": location}, oauth_complete_params.OauthCompleteParams),
            ),
            cast_to=NoneType,
        )

    async def connect(
        self,
        integration_id: IntegrationID,
        *,
        method_id: IntegrationMethodID,
        answer: Optional[FormAnswer] | Omit = omit,
        label: Optional[str] | Omit = omit,
        location: Optional[oauth_connect_params.Location] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OauthConnectResponse:
        """
        Start an OAuth attempt and return the authorization details.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not integration_id:
            raise ValueError(f"Expected a non-empty value for `integration_id` but received {integration_id!r}")
        return await self._post(
            path_template("/api/integration/{integration_id}/connect/oauth", integration_id=integration_id),
            body=await async_maybe_transform(
                {
                    "method_id": method_id,
                    "answer": answer,
                    "label": label,
                },
                oauth_connect_params.OauthConnectParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"location": location}, oauth_connect_params.OauthConnectParams),
            ),
            cast_to=OauthConnectResponse,
        )

    async def status(
        self,
        attempt_id: IntegrationAttemptID,
        *,
        integration_id: IntegrationID,
        location: Optional[oauth_status_params.Location] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OauthStatusResponse:
        """
        Poll the current status of an OAuth attempt.

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
                "/api/integration/{integration_id}/connect/oauth/{attempt_id}",
                integration_id=integration_id,
                attempt_id=attempt_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"location": location}, oauth_status_params.OauthStatusParams),
            ),
            cast_to=OauthStatusResponse,
        )


class OauthResourceWithRawResponse:
    def __init__(self, oauth: OauthResource) -> None:
        self._oauth = oauth

        self.cancel = to_raw_response_wrapper(
            oauth.cancel,
        )
        self.complete = to_raw_response_wrapper(
            oauth.complete,
        )
        self.connect = to_raw_response_wrapper(
            oauth.connect,
        )
        self.status = to_raw_response_wrapper(
            oauth.status,
        )


class AsyncOauthResourceWithRawResponse:
    def __init__(self, oauth: AsyncOauthResource) -> None:
        self._oauth = oauth

        self.cancel = async_to_raw_response_wrapper(
            oauth.cancel,
        )
        self.complete = async_to_raw_response_wrapper(
            oauth.complete,
        )
        self.connect = async_to_raw_response_wrapper(
            oauth.connect,
        )
        self.status = async_to_raw_response_wrapper(
            oauth.status,
        )


class OauthResourceWithStreamingResponse:
    def __init__(self, oauth: OauthResource) -> None:
        self._oauth = oauth

        self.cancel = to_streamed_response_wrapper(
            oauth.cancel,
        )
        self.complete = to_streamed_response_wrapper(
            oauth.complete,
        )
        self.connect = to_streamed_response_wrapper(
            oauth.connect,
        )
        self.status = to_streamed_response_wrapper(
            oauth.status,
        )


class AsyncOauthResourceWithStreamingResponse:
    def __init__(self, oauth: AsyncOauthResource) -> None:
        self._oauth = oauth

        self.cancel = async_to_streamed_response_wrapper(
            oauth.cancel,
        )
        self.complete = async_to_streamed_response_wrapper(
            oauth.complete,
        )
        self.connect = async_to_streamed_response_wrapper(
            oauth.connect,
        )
        self.status = async_to_streamed_response_wrapper(
            oauth.status,
        )
