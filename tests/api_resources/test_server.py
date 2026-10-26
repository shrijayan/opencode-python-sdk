# File generated from our OpenAPI spec by Ferrule. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from opencode import Opencode, AsyncOpencode
from tests.utils import assert_matches_type
from opencode.types.shared import ServerInfo, PairingCode, PairingSession

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestServer:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_connect(self, client: Opencode) -> None:
        server = client.server.connect(
            "code",
        )
        assert_matches_type(PairingSession, server, path=["response"])

    @parametrize
    def test_raw_response_connect(self, client: Opencode) -> None:
        response = client.server.with_raw_response.connect(
            "code",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        server = response.parse()
        assert_matches_type(PairingSession, server, path=["response"])

    @parametrize
    def test_streaming_response_connect(self, client: Opencode) -> None:
        with client.server.with_streaming_response.connect(
            "code",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            server = response.parse()
            assert_matches_type(PairingSession, server, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_connect(self, client: Opencode) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `code` but received ''"):
            client.server.with_raw_response.connect(
                "",
            )

    @parametrize
    def test_method_info(self, client: Opencode) -> None:
        server = client.server.info()
        assert_matches_type(ServerInfo, server, path=["response"])

    @parametrize
    def test_raw_response_info(self, client: Opencode) -> None:
        response = client.server.with_raw_response.info()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        server = response.parse()
        assert_matches_type(ServerInfo, server, path=["response"])

    @parametrize
    def test_streaming_response_info(self, client: Opencode) -> None:
        with client.server.with_streaming_response.info() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            server = response.parse()
            assert_matches_type(ServerInfo, server, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_pair(self, client: Opencode) -> None:
        server = client.server.pair()
        assert_matches_type(PairingCode, server, path=["response"])

    @parametrize
    def test_raw_response_pair(self, client: Opencode) -> None:
        response = client.server.with_raw_response.pair()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        server = response.parse()
        assert_matches_type(PairingCode, server, path=["response"])

    @parametrize
    def test_streaming_response_pair(self, client: Opencode) -> None:
        with client.server.with_streaming_response.pair() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            server = response.parse()
            assert_matches_type(PairingCode, server, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncServer:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_connect(self, async_client: AsyncOpencode) -> None:
        server = await async_client.server.connect(
            "code",
        )
        assert_matches_type(PairingSession, server, path=["response"])

    @parametrize
    async def test_raw_response_connect(self, async_client: AsyncOpencode) -> None:
        response = await async_client.server.with_raw_response.connect(
            "code",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        server = await response.parse()
        assert_matches_type(PairingSession, server, path=["response"])

    @parametrize
    async def test_streaming_response_connect(self, async_client: AsyncOpencode) -> None:
        async with async_client.server.with_streaming_response.connect(
            "code",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            server = await response.parse()
            assert_matches_type(PairingSession, server, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_connect(self, async_client: AsyncOpencode) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `code` but received ''"):
            await async_client.server.with_raw_response.connect(
                "",
            )

    @parametrize
    async def test_method_info(self, async_client: AsyncOpencode) -> None:
        server = await async_client.server.info()
        assert_matches_type(ServerInfo, server, path=["response"])

    @parametrize
    async def test_raw_response_info(self, async_client: AsyncOpencode) -> None:
        response = await async_client.server.with_raw_response.info()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        server = await response.parse()
        assert_matches_type(ServerInfo, server, path=["response"])

    @parametrize
    async def test_streaming_response_info(self, async_client: AsyncOpencode) -> None:
        async with async_client.server.with_streaming_response.info() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            server = await response.parse()
            assert_matches_type(ServerInfo, server, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_pair(self, async_client: AsyncOpencode) -> None:
        server = await async_client.server.pair()
        assert_matches_type(PairingCode, server, path=["response"])

    @parametrize
    async def test_raw_response_pair(self, async_client: AsyncOpencode) -> None:
        response = await async_client.server.with_raw_response.pair()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        server = await response.parse()
        assert_matches_type(PairingCode, server, path=["response"])

    @parametrize
    async def test_streaming_response_pair(self, async_client: AsyncOpencode) -> None:
        async with async_client.server.with_streaming_response.pair() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            server = await response.parse()
            assert_matches_type(PairingCode, server, path=["response"])

        assert cast(Any, response.is_closed) is True
