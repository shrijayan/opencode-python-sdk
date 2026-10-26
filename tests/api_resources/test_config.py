# File generated from our OpenAPI spec by Ferrule. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from opencode import Opencode, AsyncOpencode
from tests.utils import assert_matches_type
from opencode.types import ConfigGetResponse, ConfigShellsResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestConfig:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_update(self, client: Opencode) -> None:
        config = client.config.update(
            shell="shell",
        )
        assert config is None

    @parametrize
    def test_raw_response_update(self, client: Opencode) -> None:
        response = client.config.with_raw_response.update(
            shell="shell",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        config = response.parse()
        assert config is None

    @parametrize
    def test_streaming_response_update(self, client: Opencode) -> None:
        with client.config.with_streaming_response.update(
            shell="shell",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            config = response.parse()
            assert config is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_get(self, client: Opencode) -> None:
        config = client.config.get()
        assert_matches_type(ConfigGetResponse, config, path=["response"])

    @parametrize
    def test_method_get_with_all_params(self, client: Opencode) -> None:
        config = client.config.get(
            location={
                "directory": "string",
            },
        )
        assert_matches_type(ConfigGetResponse, config, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Opencode) -> None:
        response = client.config.with_raw_response.get()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        config = response.parse()
        assert_matches_type(ConfigGetResponse, config, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Opencode) -> None:
        with client.config.with_streaming_response.get() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            config = response.parse()
            assert_matches_type(ConfigGetResponse, config, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_shells(self, client: Opencode) -> None:
        config = client.config.shells()
        assert_matches_type(ConfigShellsResponse, config, path=["response"])

    @parametrize
    def test_raw_response_shells(self, client: Opencode) -> None:
        response = client.config.with_raw_response.shells()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        config = response.parse()
        assert_matches_type(ConfigShellsResponse, config, path=["response"])

    @parametrize
    def test_streaming_response_shells(self, client: Opencode) -> None:
        with client.config.with_streaming_response.shells() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            config = response.parse()
            assert_matches_type(ConfigShellsResponse, config, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncConfig:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_update(self, async_client: AsyncOpencode) -> None:
        config = await async_client.config.update(
            shell="shell",
        )
        assert config is None

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncOpencode) -> None:
        response = await async_client.config.with_raw_response.update(
            shell="shell",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        config = await response.parse()
        assert config is None

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncOpencode) -> None:
        async with async_client.config.with_streaming_response.update(
            shell="shell",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            config = await response.parse()
            assert config is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_get(self, async_client: AsyncOpencode) -> None:
        config = await async_client.config.get()
        assert_matches_type(ConfigGetResponse, config, path=["response"])

    @parametrize
    async def test_method_get_with_all_params(self, async_client: AsyncOpencode) -> None:
        config = await async_client.config.get(
            location={
                "directory": "string",
            },
        )
        assert_matches_type(ConfigGetResponse, config, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncOpencode) -> None:
        response = await async_client.config.with_raw_response.get()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        config = await response.parse()
        assert_matches_type(ConfigGetResponse, config, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncOpencode) -> None:
        async with async_client.config.with_streaming_response.get() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            config = await response.parse()
            assert_matches_type(ConfigGetResponse, config, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_shells(self, async_client: AsyncOpencode) -> None:
        config = await async_client.config.shells()
        assert_matches_type(ConfigShellsResponse, config, path=["response"])

    @parametrize
    async def test_raw_response_shells(self, async_client: AsyncOpencode) -> None:
        response = await async_client.config.with_raw_response.shells()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        config = await response.parse()
        assert_matches_type(ConfigShellsResponse, config, path=["response"])

    @parametrize
    async def test_streaming_response_shells(self, async_client: AsyncOpencode) -> None:
        async with async_client.config.with_streaming_response.shells() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            config = await response.parse()
            assert_matches_type(ConfigShellsResponse, config, path=["response"])

        assert cast(Any, response.is_closed) is True
