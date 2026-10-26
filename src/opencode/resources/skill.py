# File generated from our OpenAPI spec by Ferrule. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

import httpx

from ..types import skill_list_params
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
from ..types.skill_list_response import SkillListResponse

__all__ = ["SkillResource", "AsyncSkillResource"]


class SkillResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SkillResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/#accessing-raw-response-data-eg-headers
        """
        return SkillResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SkillResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/#with_streaming_response
        """
        return SkillResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        location: Optional[skill_list_params.Location] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SkillListResponse:
        """
        Retrieve currently registered skills.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/api/skill",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"location": location}, skill_list_params.SkillListParams),
            ),
            cast_to=SkillListResponse,
        )


class AsyncSkillResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSkillResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/#accessing-raw-response-data-eg-headers
        """
        return AsyncSkillResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSkillResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/#with_streaming_response
        """
        return AsyncSkillResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        location: Optional[skill_list_params.Location] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SkillListResponse:
        """
        Retrieve currently registered skills.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/api/skill",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"location": location}, skill_list_params.SkillListParams),
            ),
            cast_to=SkillListResponse,
        )


class SkillResourceWithRawResponse:
    def __init__(self, skill: SkillResource) -> None:
        self._skill = skill

        self.list = to_raw_response_wrapper(
            skill.list,
        )


class AsyncSkillResourceWithRawResponse:
    def __init__(self, skill: AsyncSkillResource) -> None:
        self._skill = skill

        self.list = async_to_raw_response_wrapper(
            skill.list,
        )


class SkillResourceWithStreamingResponse:
    def __init__(self, skill: SkillResource) -> None:
        self._skill = skill

        self.list = to_streamed_response_wrapper(
            skill.list,
        )


class AsyncSkillResourceWithStreamingResponse:
    def __init__(self, skill: AsyncSkillResource) -> None:
        self._skill = skill

        self.list = async_to_streamed_response_wrapper(
            skill.list,
        )
