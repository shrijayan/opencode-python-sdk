# File generated from our OpenAPI spec by Ferrule. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, cast

import httpx

from ..types import credential_create_params, credential_update_params
from .._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
from .._utils import path_template, maybe_transform, async_maybe_transform
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
from ..types.shared.credential_entry import CredentialEntry
from ..types.credential_list_response import CredentialListResponse
from ..types.shared_params.credential_id import CredentialID
from ..types.shared_params.integration_id import IntegrationID
from ..types.shared_params.credential_value import CredentialValue

__all__ = ["CredentialResource", "AsyncCredentialResource"]


class CredentialResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CredentialResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/#accessing-raw-response-data-eg-headers
        """
        return CredentialResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CredentialResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/#with_streaming_response
        """
        return CredentialResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        integration_id: IntegrationID,
        value: CredentialValue,
        id: CredentialID | Omit = omit,
        activate: bool | Omit = omit,
        label: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CredentialEntry:
        """
        Store an integration credential. It becomes the integration's active credential
        unless activate is false and the integration already has one. Fails with a
        conflict when the requested ID already exists.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/credential",
            body=maybe_transform(
                {
                    "integration_id": integration_id,
                    "value": value,
                    "id": id,
                    "activate": activate,
                    "label": label,
                },
                credential_create_params.CredentialCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=DataWrapper[CredentialEntry]._unwrapper,
            ),
            cast_to=cast(Type[CredentialEntry], DataWrapper[CredentialEntry]),
        )

    def update(
        self,
        credential_id: CredentialID,
        *,
        label: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Update a stored credential label.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not credential_id:
            raise ValueError(f"Expected a non-empty value for `credential_id` but received {credential_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._patch(
            path_template("/api/credential/{credential_id}", credential_id=credential_id),
            body=maybe_transform({"label": label}, credential_update_params.CredentialUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CredentialListResponse:
        """List every stored integration credential, including its secret value."""
        return self._get(
            "/api/credential",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=DataWrapper[CredentialListResponse]._unwrapper,
            ),
            cast_to=cast(Type[CredentialListResponse], DataWrapper[CredentialListResponse]),
        )

    def activate(
        self,
        credential_id: CredentialID,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Activate a stored integration credential.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not credential_id:
            raise ValueError(f"Expected a non-empty value for `credential_id` but received {credential_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            path_template("/api/credential/{credential_id}/activate", credential_id=credential_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def remove(
        self,
        credential_id: CredentialID,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Remove a stored integration credential.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not credential_id:
            raise ValueError(f"Expected a non-empty value for `credential_id` but received {credential_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            path_template("/api/credential/{credential_id}", credential_id=credential_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncCredentialResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCredentialResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/#accessing-raw-response-data-eg-headers
        """
        return AsyncCredentialResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCredentialResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/#with_streaming_response
        """
        return AsyncCredentialResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        integration_id: IntegrationID,
        value: CredentialValue,
        id: CredentialID | Omit = omit,
        activate: bool | Omit = omit,
        label: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CredentialEntry:
        """
        Store an integration credential. It becomes the integration's active credential
        unless activate is false and the integration already has one. Fails with a
        conflict when the requested ID already exists.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/credential",
            body=await async_maybe_transform(
                {
                    "integration_id": integration_id,
                    "value": value,
                    "id": id,
                    "activate": activate,
                    "label": label,
                },
                credential_create_params.CredentialCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=DataWrapper[CredentialEntry]._unwrapper,
            ),
            cast_to=cast(Type[CredentialEntry], DataWrapper[CredentialEntry]),
        )

    async def update(
        self,
        credential_id: CredentialID,
        *,
        label: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Update a stored credential label.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not credential_id:
            raise ValueError(f"Expected a non-empty value for `credential_id` but received {credential_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._patch(
            path_template("/api/credential/{credential_id}", credential_id=credential_id),
            body=await async_maybe_transform({"label": label}, credential_update_params.CredentialUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CredentialListResponse:
        """List every stored integration credential, including its secret value."""
        return await self._get(
            "/api/credential",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=DataWrapper[CredentialListResponse]._unwrapper,
            ),
            cast_to=cast(Type[CredentialListResponse], DataWrapper[CredentialListResponse]),
        )

    async def activate(
        self,
        credential_id: CredentialID,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Activate a stored integration credential.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not credential_id:
            raise ValueError(f"Expected a non-empty value for `credential_id` but received {credential_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            path_template("/api/credential/{credential_id}/activate", credential_id=credential_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def remove(
        self,
        credential_id: CredentialID,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Remove a stored integration credential.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not credential_id:
            raise ValueError(f"Expected a non-empty value for `credential_id` but received {credential_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            path_template("/api/credential/{credential_id}", credential_id=credential_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class CredentialResourceWithRawResponse:
    def __init__(self, credential: CredentialResource) -> None:
        self._credential = credential

        self.create = to_raw_response_wrapper(
            credential.create,
        )
        self.update = to_raw_response_wrapper(
            credential.update,
        )
        self.list = to_raw_response_wrapper(
            credential.list,
        )
        self.activate = to_raw_response_wrapper(
            credential.activate,
        )
        self.remove = to_raw_response_wrapper(
            credential.remove,
        )


class AsyncCredentialResourceWithRawResponse:
    def __init__(self, credential: AsyncCredentialResource) -> None:
        self._credential = credential

        self.create = async_to_raw_response_wrapper(
            credential.create,
        )
        self.update = async_to_raw_response_wrapper(
            credential.update,
        )
        self.list = async_to_raw_response_wrapper(
            credential.list,
        )
        self.activate = async_to_raw_response_wrapper(
            credential.activate,
        )
        self.remove = async_to_raw_response_wrapper(
            credential.remove,
        )


class CredentialResourceWithStreamingResponse:
    def __init__(self, credential: CredentialResource) -> None:
        self._credential = credential

        self.create = to_streamed_response_wrapper(
            credential.create,
        )
        self.update = to_streamed_response_wrapper(
            credential.update,
        )
        self.list = to_streamed_response_wrapper(
            credential.list,
        )
        self.activate = to_streamed_response_wrapper(
            credential.activate,
        )
        self.remove = to_streamed_response_wrapper(
            credential.remove,
        )


class AsyncCredentialResourceWithStreamingResponse:
    def __init__(self, credential: AsyncCredentialResource) -> None:
        self._credential = credential

        self.create = async_to_streamed_response_wrapper(
            credential.create,
        )
        self.update = async_to_streamed_response_wrapper(
            credential.update,
        )
        self.list = async_to_streamed_response_wrapper(
            credential.list,
        )
        self.activate = async_to_streamed_response_wrapper(
            credential.activate,
        )
        self.remove = async_to_streamed_response_wrapper(
            credential.remove,
        )
