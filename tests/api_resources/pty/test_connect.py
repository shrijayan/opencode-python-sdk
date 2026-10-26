# File generated from our OpenAPI spec by Ferrule. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from opencode import Opencode, AsyncOpencode
from tests.utils import assert_matches_type
from opencode.types.pty import ConnectTokenResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestConnect:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_token(self, client: Opencode) -> None:
        connect = client.pty.connect.token(
            pty_id={},
        )
        assert_matches_type(ConnectTokenResponse, connect, path=["response"])

    @parametrize
    def test_method_token_with_all_params(self, client: Opencode) -> None:
        connect = client.pty.connect.token(
            pty_id={},
            location={
                "directory": "string",
            },
            x_opencode_ticket="x-opencode-ticket",
        )
        assert_matches_type(ConnectTokenResponse, connect, path=["response"])

    @parametrize
    def test_raw_response_token(self, client: Opencode) -> None:
        response = client.pty.connect.with_raw_response.token(
            pty_id={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        connect = response.parse()
        assert_matches_type(ConnectTokenResponse, connect, path=["response"])

    @parametrize
    def test_streaming_response_token(self, client: Opencode) -> None:
        with client.pty.connect.with_streaming_response.token(
            pty_id={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            connect = response.parse()
            assert_matches_type(ConnectTokenResponse, connect, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_token(self, client: Opencode) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `pty_id` but received ''"):
            client.pty.connect.with_raw_response.token(
                pty_id="",
            )


class TestAsyncConnect:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_token(self, async_client: AsyncOpencode) -> None:
        connect = await async_client.pty.connect.token(
            pty_id={},
        )
        assert_matches_type(ConnectTokenResponse, connect, path=["response"])

    @parametrize
    async def test_method_token_with_all_params(self, async_client: AsyncOpencode) -> None:
        connect = await async_client.pty.connect.token(
            pty_id={},
            location={
                "directory": "string",
            },
            x_opencode_ticket="x-opencode-ticket",
        )
        assert_matches_type(ConnectTokenResponse, connect, path=["response"])

    @parametrize
    async def test_raw_response_token(self, async_client: AsyncOpencode) -> None:
        response = await async_client.pty.connect.with_raw_response.token(
            pty_id={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        connect = await response.parse()
        assert_matches_type(ConnectTokenResponse, connect, path=["response"])

    @parametrize
    async def test_streaming_response_token(self, async_client: AsyncOpencode) -> None:
        async with async_client.pty.connect.with_streaming_response.token(
            pty_id={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            connect = await response.parse()
            assert_matches_type(ConnectTokenResponse, connect, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_token(self, async_client: AsyncOpencode) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `pty_id` but received ''"):
            await async_client.pty.connect.with_raw_response.token(
                pty_id="",
            )
