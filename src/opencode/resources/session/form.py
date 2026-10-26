# File generated from our OpenAPI spec by Ferrule. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, Optional, cast

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
from ..._wrappers import DataWrapper
from ..._base_client import make_request_options
from ...types.session import form_reply_params, form_cancel_params, form_create_params
from ...types.shared.form_info import FormInfo
from ...types.shared.form_detail import FormDetail
from ...types.shared_params.form_id import FormID
from ...types.shared_params.form_answer import FormAnswer
from ...types.shared_params.form_fields import FormFields
from ...types.session.form_list_response import FormListResponse
from ...types.shared_params.form_metadata import FormMetadata

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

    def create(
        self,
        session_id: str,
        *,
        fields: FormFields,
        title: str,
        id: Optional[FormID] | Omit = omit,
        metadata: FormMetadata | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FormInfo:
        """
        Create a form for a session.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        return self._post(
            path_template("/api/session/{session_id}/form", session_id=session_id),
            body=maybe_transform(
                {
                    "fields": fields,
                    "title": title,
                    "id": id,
                    "metadata": metadata,
                },
                form_create_params.FormCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=DataWrapper[FormInfo]._unwrapper,
            ),
            cast_to=cast(Type[FormInfo], DataWrapper[FormInfo]),
        )

    def list(
        self,
        session_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FormListResponse:
        """
        Retrieve pending forms for a session.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        return self._get(
            path_template("/api/session/{session_id}/form", session_id=session_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=DataWrapper[FormListResponse]._unwrapper,
            ),
            cast_to=cast(Type[FormListResponse], DataWrapper[FormListResponse]),
        )

    def cancel(
        self,
        form_id: FormID,
        *,
        session_id: str,
        message: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Cancel a pending form, optionally telling the asker why it was not answered.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        if not form_id:
            raise ValueError(f"Expected a non-empty value for `form_id` but received {form_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            path_template("/api/session/{session_id}/form/{form_id}", session_id=session_id, form_id=form_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"message": message}, form_cancel_params.FormCancelParams),
            ),
            cast_to=NoneType,
        )

    def get(
        self,
        form_id: FormID,
        *,
        session_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FormDetail:
        """
        Retrieve a form and its current state for a session.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        if not form_id:
            raise ValueError(f"Expected a non-empty value for `form_id` but received {form_id!r}")
        return self._get(
            path_template("/api/session/{session_id}/form/{form_id}", session_id=session_id, form_id=form_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=DataWrapper[FormDetail]._unwrapper,
            ),
            cast_to=cast(Type[FormDetail], DataWrapper[FormDetail]),
        )

    def reply(
        self,
        form_id: FormID,
        *,
        session_id: str,
        answer: FormAnswer,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Submit an answer to a pending form.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        if not form_id:
            raise ValueError(f"Expected a non-empty value for `form_id` but received {form_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            path_template("/api/session/{session_id}/form/{form_id}/reply", session_id=session_id, form_id=form_id),
            body=maybe_transform({"answer": answer}, form_reply_params.FormReplyParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
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

    async def create(
        self,
        session_id: str,
        *,
        fields: FormFields,
        title: str,
        id: Optional[FormID] | Omit = omit,
        metadata: FormMetadata | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FormInfo:
        """
        Create a form for a session.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        return await self._post(
            path_template("/api/session/{session_id}/form", session_id=session_id),
            body=await async_maybe_transform(
                {
                    "fields": fields,
                    "title": title,
                    "id": id,
                    "metadata": metadata,
                },
                form_create_params.FormCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=DataWrapper[FormInfo]._unwrapper,
            ),
            cast_to=cast(Type[FormInfo], DataWrapper[FormInfo]),
        )

    async def list(
        self,
        session_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FormListResponse:
        """
        Retrieve pending forms for a session.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        return await self._get(
            path_template("/api/session/{session_id}/form", session_id=session_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=DataWrapper[FormListResponse]._unwrapper,
            ),
            cast_to=cast(Type[FormListResponse], DataWrapper[FormListResponse]),
        )

    async def cancel(
        self,
        form_id: FormID,
        *,
        session_id: str,
        message: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Cancel a pending form, optionally telling the asker why it was not answered.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        if not form_id:
            raise ValueError(f"Expected a non-empty value for `form_id` but received {form_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            path_template("/api/session/{session_id}/form/{form_id}", session_id=session_id, form_id=form_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"message": message}, form_cancel_params.FormCancelParams),
            ),
            cast_to=NoneType,
        )

    async def get(
        self,
        form_id: FormID,
        *,
        session_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FormDetail:
        """
        Retrieve a form and its current state for a session.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        if not form_id:
            raise ValueError(f"Expected a non-empty value for `form_id` but received {form_id!r}")
        return await self._get(
            path_template("/api/session/{session_id}/form/{form_id}", session_id=session_id, form_id=form_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=DataWrapper[FormDetail]._unwrapper,
            ),
            cast_to=cast(Type[FormDetail], DataWrapper[FormDetail]),
        )

    async def reply(
        self,
        form_id: FormID,
        *,
        session_id: str,
        answer: FormAnswer,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Submit an answer to a pending form.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        if not form_id:
            raise ValueError(f"Expected a non-empty value for `form_id` but received {form_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            path_template("/api/session/{session_id}/form/{form_id}/reply", session_id=session_id, form_id=form_id),
            body=await async_maybe_transform({"answer": answer}, form_reply_params.FormReplyParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class FormResourceWithRawResponse:
    def __init__(self, form: FormResource) -> None:
        self._form = form

        self.create = to_raw_response_wrapper(
            form.create,
        )
        self.list = to_raw_response_wrapper(
            form.list,
        )
        self.cancel = to_raw_response_wrapper(
            form.cancel,
        )
        self.get = to_raw_response_wrapper(
            form.get,
        )
        self.reply = to_raw_response_wrapper(
            form.reply,
        )


class AsyncFormResourceWithRawResponse:
    def __init__(self, form: AsyncFormResource) -> None:
        self._form = form

        self.create = async_to_raw_response_wrapper(
            form.create,
        )
        self.list = async_to_raw_response_wrapper(
            form.list,
        )
        self.cancel = async_to_raw_response_wrapper(
            form.cancel,
        )
        self.get = async_to_raw_response_wrapper(
            form.get,
        )
        self.reply = async_to_raw_response_wrapper(
            form.reply,
        )


class FormResourceWithStreamingResponse:
    def __init__(self, form: FormResource) -> None:
        self._form = form

        self.create = to_streamed_response_wrapper(
            form.create,
        )
        self.list = to_streamed_response_wrapper(
            form.list,
        )
        self.cancel = to_streamed_response_wrapper(
            form.cancel,
        )
        self.get = to_streamed_response_wrapper(
            form.get,
        )
        self.reply = to_streamed_response_wrapper(
            form.reply,
        )


class AsyncFormResourceWithStreamingResponse:
    def __init__(self, form: AsyncFormResource) -> None:
        self._form = form

        self.create = async_to_streamed_response_wrapper(
            form.create,
        )
        self.list = async_to_streamed_response_wrapper(
            form.list,
        )
        self.cancel = async_to_streamed_response_wrapper(
            form.cancel,
        )
        self.get = async_to_streamed_response_wrapper(
            form.get,
        )
        self.reply = async_to_streamed_response_wrapper(
            form.reply,
        )
