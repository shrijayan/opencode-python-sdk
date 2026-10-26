# File generated from our OpenAPI spec by Ferrule. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from opencode import Opencode, AsyncOpencode
from tests.utils import assert_matches_type
from opencode.types import IntegrationGetResponse, IntegrationListResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestIntegration:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Opencode) -> None:
        integration = client.integration.list()
        assert_matches_type(IntegrationListResponse, integration, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Opencode) -> None:
        integration = client.integration.list(
            location={
                "directory": "string",
            },
        )
        assert_matches_type(IntegrationListResponse, integration, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Opencode) -> None:
        response = client.integration.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        integration = response.parse()
        assert_matches_type(IntegrationListResponse, integration, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Opencode) -> None:
        with client.integration.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            integration = response.parse()
            assert_matches_type(IntegrationListResponse, integration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_get(self, client: Opencode) -> None:
        integration = client.integration.get(
            integration_id="integrationID",
        )
        assert_matches_type(IntegrationGetResponse, integration, path=["response"])

    @parametrize
    def test_method_get_with_all_params(self, client: Opencode) -> None:
        integration = client.integration.get(
            integration_id="integrationID",
            location={
                "directory": "string",
            },
        )
        assert_matches_type(IntegrationGetResponse, integration, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Opencode) -> None:
        response = client.integration.with_raw_response.get(
            integration_id="integrationID",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        integration = response.parse()
        assert_matches_type(IntegrationGetResponse, integration, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Opencode) -> None:
        with client.integration.with_streaming_response.get(
            integration_id="integrationID",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            integration = response.parse()
            assert_matches_type(IntegrationGetResponse, integration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Opencode) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `integration_id` but received ''"):
            client.integration.with_raw_response.get(
                integration_id="",
            )


class TestAsyncIntegration:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_list(self, async_client: AsyncOpencode) -> None:
        integration = await async_client.integration.list()
        assert_matches_type(IntegrationListResponse, integration, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncOpencode) -> None:
        integration = await async_client.integration.list(
            location={
                "directory": "string",
            },
        )
        assert_matches_type(IntegrationListResponse, integration, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncOpencode) -> None:
        response = await async_client.integration.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        integration = await response.parse()
        assert_matches_type(IntegrationListResponse, integration, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncOpencode) -> None:
        async with async_client.integration.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            integration = await response.parse()
            assert_matches_type(IntegrationListResponse, integration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_get(self, async_client: AsyncOpencode) -> None:
        integration = await async_client.integration.get(
            integration_id="integrationID",
        )
        assert_matches_type(IntegrationGetResponse, integration, path=["response"])

    @parametrize
    async def test_method_get_with_all_params(self, async_client: AsyncOpencode) -> None:
        integration = await async_client.integration.get(
            integration_id="integrationID",
            location={
                "directory": "string",
            },
        )
        assert_matches_type(IntegrationGetResponse, integration, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncOpencode) -> None:
        response = await async_client.integration.with_raw_response.get(
            integration_id="integrationID",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        integration = await response.parse()
        assert_matches_type(IntegrationGetResponse, integration, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncOpencode) -> None:
        async with async_client.integration.with_streaming_response.get(
            integration_id="integrationID",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            integration = await response.parse()
            assert_matches_type(IntegrationGetResponse, integration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncOpencode) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `integration_id` but received ''"):
            await async_client.integration.with_raw_response.get(
                integration_id="",
            )
