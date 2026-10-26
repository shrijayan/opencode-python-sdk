# File generated from our OpenAPI spec by Ferrule. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from opencode import Opencode, AsyncOpencode
from tests.utils import assert_matches_type
from opencode.types.mcp import ResourceCatalogResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestResource:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_catalog(self, client: Opencode) -> None:
        resource = client.mcp.resource.catalog()
        assert_matches_type(ResourceCatalogResponse, resource, path=["response"])

    @parametrize
    def test_method_catalog_with_all_params(self, client: Opencode) -> None:
        resource = client.mcp.resource.catalog(
            location={
                "directory": "string",
            },
        )
        assert_matches_type(ResourceCatalogResponse, resource, path=["response"])

    @parametrize
    def test_raw_response_catalog(self, client: Opencode) -> None:
        response = client.mcp.resource.with_raw_response.catalog()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        resource = response.parse()
        assert_matches_type(ResourceCatalogResponse, resource, path=["response"])

    @parametrize
    def test_streaming_response_catalog(self, client: Opencode) -> None:
        with client.mcp.resource.with_streaming_response.catalog() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            resource = response.parse()
            assert_matches_type(ResourceCatalogResponse, resource, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncResource:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_catalog(self, async_client: AsyncOpencode) -> None:
        resource = await async_client.mcp.resource.catalog()
        assert_matches_type(ResourceCatalogResponse, resource, path=["response"])

    @parametrize
    async def test_method_catalog_with_all_params(self, async_client: AsyncOpencode) -> None:
        resource = await async_client.mcp.resource.catalog(
            location={
                "directory": "string",
            },
        )
        assert_matches_type(ResourceCatalogResponse, resource, path=["response"])

    @parametrize
    async def test_raw_response_catalog(self, async_client: AsyncOpencode) -> None:
        response = await async_client.mcp.resource.with_raw_response.catalog()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        resource = await response.parse()
        assert_matches_type(ResourceCatalogResponse, resource, path=["response"])

    @parametrize
    async def test_streaming_response_catalog(self, async_client: AsyncOpencode) -> None:
        async with async_client.mcp.resource.with_streaming_response.catalog() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            resource = await response.parse()
            assert_matches_type(ResourceCatalogResponse, resource, path=["response"])

        assert cast(Any, response.is_closed) is True
