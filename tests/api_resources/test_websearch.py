# File generated from our OpenAPI spec by Ferrule. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from opencode import Opencode, AsyncOpencode
from tests.utils import assert_matches_type
from opencode.types import WebsearchQueryResponse, WebsearchProvidersResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestWebsearch:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_providers(self, client: Opencode) -> None:
        websearch = client.websearch.providers()
        assert_matches_type(WebsearchProvidersResponse, websearch, path=["response"])

    @parametrize
    def test_method_providers_with_all_params(self, client: Opencode) -> None:
        websearch = client.websearch.providers(
            location={
                "directory": "string",
            },
        )
        assert_matches_type(WebsearchProvidersResponse, websearch, path=["response"])

    @parametrize
    def test_raw_response_providers(self, client: Opencode) -> None:
        response = client.websearch.with_raw_response.providers()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        websearch = response.parse()
        assert_matches_type(WebsearchProvidersResponse, websearch, path=["response"])

    @parametrize
    def test_streaming_response_providers(self, client: Opencode) -> None:
        with client.websearch.with_streaming_response.providers() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            websearch = response.parse()
            assert_matches_type(WebsearchProvidersResponse, websearch, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_query(self, client: Opencode) -> None:
        websearch = client.websearch.query(
            query="query",
        )
        assert_matches_type(WebsearchQueryResponse, websearch, path=["response"])

    @parametrize
    def test_method_query_with_all_params(self, client: Opencode) -> None:
        websearch = client.websearch.query(
            query="query",
            location={
                "directory": "string",
            },
            provider_id={},
        )
        assert_matches_type(WebsearchQueryResponse, websearch, path=["response"])

    @parametrize
    def test_raw_response_query(self, client: Opencode) -> None:
        response = client.websearch.with_raw_response.query(
            query="query",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        websearch = response.parse()
        assert_matches_type(WebsearchQueryResponse, websearch, path=["response"])

    @parametrize
    def test_streaming_response_query(self, client: Opencode) -> None:
        with client.websearch.with_streaming_response.query(
            query="query",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            websearch = response.parse()
            assert_matches_type(WebsearchQueryResponse, websearch, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncWebsearch:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_providers(self, async_client: AsyncOpencode) -> None:
        websearch = await async_client.websearch.providers()
        assert_matches_type(WebsearchProvidersResponse, websearch, path=["response"])

    @parametrize
    async def test_method_providers_with_all_params(self, async_client: AsyncOpencode) -> None:
        websearch = await async_client.websearch.providers(
            location={
                "directory": "string",
            },
        )
        assert_matches_type(WebsearchProvidersResponse, websearch, path=["response"])

    @parametrize
    async def test_raw_response_providers(self, async_client: AsyncOpencode) -> None:
        response = await async_client.websearch.with_raw_response.providers()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        websearch = await response.parse()
        assert_matches_type(WebsearchProvidersResponse, websearch, path=["response"])

    @parametrize
    async def test_streaming_response_providers(self, async_client: AsyncOpencode) -> None:
        async with async_client.websearch.with_streaming_response.providers() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            websearch = await response.parse()
            assert_matches_type(WebsearchProvidersResponse, websearch, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_query(self, async_client: AsyncOpencode) -> None:
        websearch = await async_client.websearch.query(
            query="query",
        )
        assert_matches_type(WebsearchQueryResponse, websearch, path=["response"])

    @parametrize
    async def test_method_query_with_all_params(self, async_client: AsyncOpencode) -> None:
        websearch = await async_client.websearch.query(
            query="query",
            location={
                "directory": "string",
            },
            provider_id={},
        )
        assert_matches_type(WebsearchQueryResponse, websearch, path=["response"])

    @parametrize
    async def test_raw_response_query(self, async_client: AsyncOpencode) -> None:
        response = await async_client.websearch.with_raw_response.query(
            query="query",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        websearch = await response.parse()
        assert_matches_type(WebsearchQueryResponse, websearch, path=["response"])

    @parametrize
    async def test_streaming_response_query(self, async_client: AsyncOpencode) -> None:
        async with async_client.websearch.with_streaming_response.query(
            query="query",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            websearch = await response.parse()
            assert_matches_type(WebsearchQueryResponse, websearch, path=["response"])

        assert cast(Any, response.is_closed) is True
