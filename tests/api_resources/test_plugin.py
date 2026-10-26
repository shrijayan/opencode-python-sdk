# File generated from our OpenAPI spec by Ferrule. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from opencode import Opencode, AsyncOpencode
from tests.utils import assert_matches_type
from opencode.types import PluginListResponse, PluginCheckResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPlugin:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_update(self, client: Opencode) -> None:
        plugin = client.plugin.update(
            targets=["string"],
        )
        assert plugin is None

    @parametrize
    def test_method_update_with_all_params(self, client: Opencode) -> None:
        plugin = client.plugin.update(
            targets=["string"],
            location={
                "directory": "string",
            },
        )
        assert plugin is None

    @parametrize
    def test_raw_response_update(self, client: Opencode) -> None:
        response = client.plugin.with_raw_response.update(
            targets=["string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        plugin = response.parse()
        assert plugin is None

    @parametrize
    def test_streaming_response_update(self, client: Opencode) -> None:
        with client.plugin.with_streaming_response.update(
            targets=["string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            plugin = response.parse()
            assert plugin is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_list(self, client: Opencode) -> None:
        plugin = client.plugin.list()
        assert_matches_type(PluginListResponse, plugin, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Opencode) -> None:
        plugin = client.plugin.list(
            location={
                "directory": "string",
            },
        )
        assert_matches_type(PluginListResponse, plugin, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Opencode) -> None:
        response = client.plugin.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        plugin = response.parse()
        assert_matches_type(PluginListResponse, plugin, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Opencode) -> None:
        with client.plugin.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            plugin = response.parse()
            assert_matches_type(PluginListResponse, plugin, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_check(self, client: Opencode) -> None:
        plugin = client.plugin.check()
        assert_matches_type(PluginCheckResponse, plugin, path=["response"])

    @parametrize
    def test_method_check_with_all_params(self, client: Opencode) -> None:
        plugin = client.plugin.check(
            location={
                "directory": "string",
            },
            target="target",
        )
        assert_matches_type(PluginCheckResponse, plugin, path=["response"])

    @parametrize
    def test_raw_response_check(self, client: Opencode) -> None:
        response = client.plugin.with_raw_response.check()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        plugin = response.parse()
        assert_matches_type(PluginCheckResponse, plugin, path=["response"])

    @parametrize
    def test_streaming_response_check(self, client: Opencode) -> None:
        with client.plugin.with_streaming_response.check() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            plugin = response.parse()
            assert_matches_type(PluginCheckResponse, plugin, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncPlugin:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_update(self, async_client: AsyncOpencode) -> None:
        plugin = await async_client.plugin.update(
            targets=["string"],
        )
        assert plugin is None

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncOpencode) -> None:
        plugin = await async_client.plugin.update(
            targets=["string"],
            location={
                "directory": "string",
            },
        )
        assert plugin is None

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncOpencode) -> None:
        response = await async_client.plugin.with_raw_response.update(
            targets=["string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        plugin = await response.parse()
        assert plugin is None

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncOpencode) -> None:
        async with async_client.plugin.with_streaming_response.update(
            targets=["string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            plugin = await response.parse()
            assert plugin is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_list(self, async_client: AsyncOpencode) -> None:
        plugin = await async_client.plugin.list()
        assert_matches_type(PluginListResponse, plugin, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncOpencode) -> None:
        plugin = await async_client.plugin.list(
            location={
                "directory": "string",
            },
        )
        assert_matches_type(PluginListResponse, plugin, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncOpencode) -> None:
        response = await async_client.plugin.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        plugin = await response.parse()
        assert_matches_type(PluginListResponse, plugin, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncOpencode) -> None:
        async with async_client.plugin.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            plugin = await response.parse()
            assert_matches_type(PluginListResponse, plugin, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_check(self, async_client: AsyncOpencode) -> None:
        plugin = await async_client.plugin.check()
        assert_matches_type(PluginCheckResponse, plugin, path=["response"])

    @parametrize
    async def test_method_check_with_all_params(self, async_client: AsyncOpencode) -> None:
        plugin = await async_client.plugin.check(
            location={
                "directory": "string",
            },
            target="target",
        )
        assert_matches_type(PluginCheckResponse, plugin, path=["response"])

    @parametrize
    async def test_raw_response_check(self, async_client: AsyncOpencode) -> None:
        response = await async_client.plugin.with_raw_response.check()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        plugin = await response.parse()
        assert_matches_type(PluginCheckResponse, plugin, path=["response"])

    @parametrize
    async def test_streaming_response_check(self, async_client: AsyncOpencode) -> None:
        async with async_client.plugin.with_streaming_response.check() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            plugin = await response.parse()
            assert_matches_type(PluginCheckResponse, plugin, path=["response"])

        assert cast(Any, response.is_closed) is True
