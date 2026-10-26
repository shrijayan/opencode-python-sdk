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
from ...types.permission import saved_list_params, saved_update_params
from ...types.shared.project_id import ProjectID
from ...types.shared.permission_saved_id import PermissionSavedID
from ...types.permission.saved_list_response import SavedListResponse
from ...types.permission.saved_update_response import SavedUpdateResponse

__all__ = ["SavedResource", "AsyncSavedResource"]


class SavedResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SavedResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/#accessing-raw-response-data-eg-headers
        """
        return SavedResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SavedResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/#with_streaming_response
        """
        return SavedResourceWithStreamingResponse(self)

    def update(
        self,
        id: PermissionSavedID,
        *,
        action: Optional[str] | Omit = omit,
        resource: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SavedUpdateResponse:
        """
        Change the action or resource of a saved permission. Fails with a conflict when
        the project already has a saved permission with the same action and resource.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._patch(
            path_template("/api/permission/saved/{id}", id=id),
            body=maybe_transform(
                {
                    "action": action,
                    "resource": resource,
                },
                saved_update_params.SavedUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SavedUpdateResponse,
        )

    def list(
        self,
        *,
        project_id: Optional[ProjectID] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SavedListResponse:
        """
        Retrieve saved permissions, optionally filtered by project.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/api/permission/saved",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"project_id": project_id}, saved_list_params.SavedListParams),
            ),
            cast_to=SavedListResponse,
        )

    def remove(
        self,
        id: PermissionSavedID,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Remove a saved permission by ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            path_template("/api/permission/saved/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncSavedResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSavedResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/#accessing-raw-response-data-eg-headers
        """
        return AsyncSavedResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSavedResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/#with_streaming_response
        """
        return AsyncSavedResourceWithStreamingResponse(self)

    async def update(
        self,
        id: PermissionSavedID,
        *,
        action: Optional[str] | Omit = omit,
        resource: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SavedUpdateResponse:
        """
        Change the action or resource of a saved permission. Fails with a conflict when
        the project already has a saved permission with the same action and resource.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._patch(
            path_template("/api/permission/saved/{id}", id=id),
            body=await async_maybe_transform(
                {
                    "action": action,
                    "resource": resource,
                },
                saved_update_params.SavedUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SavedUpdateResponse,
        )

    async def list(
        self,
        *,
        project_id: Optional[ProjectID] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SavedListResponse:
        """
        Retrieve saved permissions, optionally filtered by project.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/api/permission/saved",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"project_id": project_id}, saved_list_params.SavedListParams),
            ),
            cast_to=SavedListResponse,
        )

    async def remove(
        self,
        id: PermissionSavedID,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Remove a saved permission by ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            path_template("/api/permission/saved/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class SavedResourceWithRawResponse:
    def __init__(self, saved: SavedResource) -> None:
        self._saved = saved

        self.update = to_raw_response_wrapper(
            saved.update,
        )
        self.list = to_raw_response_wrapper(
            saved.list,
        )
        self.remove = to_raw_response_wrapper(
            saved.remove,
        )


class AsyncSavedResourceWithRawResponse:
    def __init__(self, saved: AsyncSavedResource) -> None:
        self._saved = saved

        self.update = async_to_raw_response_wrapper(
            saved.update,
        )
        self.list = async_to_raw_response_wrapper(
            saved.list,
        )
        self.remove = async_to_raw_response_wrapper(
            saved.remove,
        )


class SavedResourceWithStreamingResponse:
    def __init__(self, saved: SavedResource) -> None:
        self._saved = saved

        self.update = to_streamed_response_wrapper(
            saved.update,
        )
        self.list = to_streamed_response_wrapper(
            saved.list,
        )
        self.remove = to_streamed_response_wrapper(
            saved.remove,
        )


class AsyncSavedResourceWithStreamingResponse:
    def __init__(self, saved: AsyncSavedResource) -> None:
        self._saved = saved

        self.update = async_to_streamed_response_wrapper(
            saved.update,
        )
        self.list = async_to_streamed_response_wrapper(
            saved.list,
        )
        self.remove = async_to_streamed_response_wrapper(
            saved.remove,
        )
