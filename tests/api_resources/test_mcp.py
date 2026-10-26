# File generated from our OpenAPI spec by Ferrule. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from opencode import Opencode, AsyncOpencode
from tests.utils import assert_matches_type
from opencode.types import McpListResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestMcp:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Opencode) -> None:
        mcp = client.mcp.list()
        assert_matches_type(McpListResponse, mcp, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Opencode) -> None:
        mcp = client.mcp.list(
            location={
                "directory": "string",
            },
        )
        assert_matches_type(McpListResponse, mcp, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Opencode) -> None:
        response = client.mcp.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        mcp = response.parse()
        assert_matches_type(McpListResponse, mcp, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Opencode) -> None:
        with client.mcp.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            mcp = response.parse()
            assert_matches_type(McpListResponse, mcp, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_add(self, client: Opencode) -> None:
        mcp = client.mcp.add(
            server="server",
            config={},
        )
        assert mcp is None

    @parametrize
    def test_method_add_with_all_params(self, client: Opencode) -> None:
        mcp = client.mcp.add(
            server="server",
            config={},
            location={
                "directory": "string",
            },
        )
        assert mcp is None

    @parametrize
    def test_raw_response_add(self, client: Opencode) -> None:
        response = client.mcp.with_raw_response.add(
            server="server",
            config={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        mcp = response.parse()
        assert mcp is None

    @parametrize
    def test_streaming_response_add(self, client: Opencode) -> None:
        with client.mcp.with_streaming_response.add(
            server="server",
            config={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            mcp = response.parse()
            assert mcp is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_add(self, client: Opencode) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `server` but received ''"):
            client.mcp.with_raw_response.add(
                server="",
                config={},
            )

    @parametrize
    def test_method_connect(self, client: Opencode) -> None:
        mcp = client.mcp.connect(
            server="server",
        )
        assert mcp is None

    @parametrize
    def test_method_connect_with_all_params(self, client: Opencode) -> None:
        mcp = client.mcp.connect(
            server="server",
            location={
                "directory": "string",
            },
        )
        assert mcp is None

    @parametrize
    def test_raw_response_connect(self, client: Opencode) -> None:
        response = client.mcp.with_raw_response.connect(
            server="server",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        mcp = response.parse()
        assert mcp is None

    @parametrize
    def test_streaming_response_connect(self, client: Opencode) -> None:
        with client.mcp.with_streaming_response.connect(
            server="server",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            mcp = response.parse()
            assert mcp is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_connect(self, client: Opencode) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `server` but received ''"):
            client.mcp.with_raw_response.connect(
                server="",
            )

    @parametrize
    def test_method_disconnect(self, client: Opencode) -> None:
        mcp = client.mcp.disconnect(
            server="server",
        )
        assert mcp is None

    @parametrize
    def test_method_disconnect_with_all_params(self, client: Opencode) -> None:
        mcp = client.mcp.disconnect(
            server="server",
            location={
                "directory": "string",
            },
        )
        assert mcp is None

    @parametrize
    def test_raw_response_disconnect(self, client: Opencode) -> None:
        response = client.mcp.with_raw_response.disconnect(
            server="server",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        mcp = response.parse()
        assert mcp is None

    @parametrize
    def test_streaming_response_disconnect(self, client: Opencode) -> None:
        with client.mcp.with_streaming_response.disconnect(
            server="server",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            mcp = response.parse()
            assert mcp is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_disconnect(self, client: Opencode) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `server` but received ''"):
            client.mcp.with_raw_response.disconnect(
                server="",
            )

    @parametrize
    def test_method_remove(self, client: Opencode) -> None:
        mcp = client.mcp.remove(
            server="server",
        )
        assert mcp is None

    @parametrize
    def test_method_remove_with_all_params(self, client: Opencode) -> None:
        mcp = client.mcp.remove(
            server="server",
            location={
                "directory": "string",
            },
        )
        assert mcp is None

    @parametrize
    def test_raw_response_remove(self, client: Opencode) -> None:
        response = client.mcp.with_raw_response.remove(
            server="server",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        mcp = response.parse()
        assert mcp is None

    @parametrize
    def test_streaming_response_remove(self, client: Opencode) -> None:
        with client.mcp.with_streaming_response.remove(
            server="server",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            mcp = response.parse()
            assert mcp is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_remove(self, client: Opencode) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `server` but received ''"):
            client.mcp.with_raw_response.remove(
                server="",
            )


class TestAsyncMcp:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_list(self, async_client: AsyncOpencode) -> None:
        mcp = await async_client.mcp.list()
        assert_matches_type(McpListResponse, mcp, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncOpencode) -> None:
        mcp = await async_client.mcp.list(
            location={
                "directory": "string",
            },
        )
        assert_matches_type(McpListResponse, mcp, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncOpencode) -> None:
        response = await async_client.mcp.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        mcp = await response.parse()
        assert_matches_type(McpListResponse, mcp, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncOpencode) -> None:
        async with async_client.mcp.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            mcp = await response.parse()
            assert_matches_type(McpListResponse, mcp, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_add(self, async_client: AsyncOpencode) -> None:
        mcp = await async_client.mcp.add(
            server="server",
            config={},
        )
        assert mcp is None

    @parametrize
    async def test_method_add_with_all_params(self, async_client: AsyncOpencode) -> None:
        mcp = await async_client.mcp.add(
            server="server",
            config={},
            location={
                "directory": "string",
            },
        )
        assert mcp is None

    @parametrize
    async def test_raw_response_add(self, async_client: AsyncOpencode) -> None:
        response = await async_client.mcp.with_raw_response.add(
            server="server",
            config={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        mcp = await response.parse()
        assert mcp is None

    @parametrize
    async def test_streaming_response_add(self, async_client: AsyncOpencode) -> None:
        async with async_client.mcp.with_streaming_response.add(
            server="server",
            config={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            mcp = await response.parse()
            assert mcp is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_add(self, async_client: AsyncOpencode) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `server` but received ''"):
            await async_client.mcp.with_raw_response.add(
                server="",
                config={},
            )

    @parametrize
    async def test_method_connect(self, async_client: AsyncOpencode) -> None:
        mcp = await async_client.mcp.connect(
            server="server",
        )
        assert mcp is None

    @parametrize
    async def test_method_connect_with_all_params(self, async_client: AsyncOpencode) -> None:
        mcp = await async_client.mcp.connect(
            server="server",
            location={
                "directory": "string",
            },
        )
        assert mcp is None

    @parametrize
    async def test_raw_response_connect(self, async_client: AsyncOpencode) -> None:
        response = await async_client.mcp.with_raw_response.connect(
            server="server",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        mcp = await response.parse()
        assert mcp is None

    @parametrize
    async def test_streaming_response_connect(self, async_client: AsyncOpencode) -> None:
        async with async_client.mcp.with_streaming_response.connect(
            server="server",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            mcp = await response.parse()
            assert mcp is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_connect(self, async_client: AsyncOpencode) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `server` but received ''"):
            await async_client.mcp.with_raw_response.connect(
                server="",
            )

    @parametrize
    async def test_method_disconnect(self, async_client: AsyncOpencode) -> None:
        mcp = await async_client.mcp.disconnect(
            server="server",
        )
        assert mcp is None

    @parametrize
    async def test_method_disconnect_with_all_params(self, async_client: AsyncOpencode) -> None:
        mcp = await async_client.mcp.disconnect(
            server="server",
            location={
                "directory": "string",
            },
        )
        assert mcp is None

    @parametrize
    async def test_raw_response_disconnect(self, async_client: AsyncOpencode) -> None:
        response = await async_client.mcp.with_raw_response.disconnect(
            server="server",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        mcp = await response.parse()
        assert mcp is None

    @parametrize
    async def test_streaming_response_disconnect(self, async_client: AsyncOpencode) -> None:
        async with async_client.mcp.with_streaming_response.disconnect(
            server="server",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            mcp = await response.parse()
            assert mcp is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_disconnect(self, async_client: AsyncOpencode) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `server` but received ''"):
            await async_client.mcp.with_raw_response.disconnect(
                server="",
            )

    @parametrize
    async def test_method_remove(self, async_client: AsyncOpencode) -> None:
        mcp = await async_client.mcp.remove(
            server="server",
        )
        assert mcp is None

    @parametrize
    async def test_method_remove_with_all_params(self, async_client: AsyncOpencode) -> None:
        mcp = await async_client.mcp.remove(
            server="server",
            location={
                "directory": "string",
            },
        )
        assert mcp is None

    @parametrize
    async def test_raw_response_remove(self, async_client: AsyncOpencode) -> None:
        response = await async_client.mcp.with_raw_response.remove(
            server="server",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        mcp = await response.parse()
        assert mcp is None

    @parametrize
    async def test_streaming_response_remove(self, async_client: AsyncOpencode) -> None:
        async with async_client.mcp.with_streaming_response.remove(
            server="server",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            mcp = await response.parse()
            assert mcp is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_remove(self, async_client: AsyncOpencode) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `server` but received ''"):
            await async_client.mcp.with_raw_response.remove(
                server="",
            )
