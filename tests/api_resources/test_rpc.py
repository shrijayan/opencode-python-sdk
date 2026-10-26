# File generated from our OpenAPI spec by Ferrule. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from opencode import Opencode, AsyncOpencode
from tests.utils import assert_matches_type
from opencode.types.shared import RpcOutput

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestRpc:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_call(self, client: Opencode) -> None:
        rpc = client.rpc.call(
            method="method",
            rpc_id="rpcID",
        )
        assert_matches_type(RpcOutput, rpc, path=["response"])

    @parametrize
    def test_method_call_with_all_params(self, client: Opencode) -> None:
        rpc = client.rpc.call(
            method="method",
            rpc_id="rpcID",
            input={},
            location={
                "directory": "string",
            },
        )
        assert_matches_type(RpcOutput, rpc, path=["response"])

    @parametrize
    def test_raw_response_call(self, client: Opencode) -> None:
        response = client.rpc.with_raw_response.call(
            method="method",
            rpc_id="rpcID",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rpc = response.parse()
        assert_matches_type(RpcOutput, rpc, path=["response"])

    @parametrize
    def test_streaming_response_call(self, client: Opencode) -> None:
        with client.rpc.with_streaming_response.call(
            method="method",
            rpc_id="rpcID",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rpc = response.parse()
            assert_matches_type(RpcOutput, rpc, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_call(self, client: Opencode) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `rpc_id` but received ''"):
            client.rpc.with_raw_response.call(
                method="method",
                rpc_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `method` but received ''"):
            client.rpc.with_raw_response.call(
                method="",
                rpc_id="rpcID",
            )


class TestAsyncRpc:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_call(self, async_client: AsyncOpencode) -> None:
        rpc = await async_client.rpc.call(
            method="method",
            rpc_id="rpcID",
        )
        assert_matches_type(RpcOutput, rpc, path=["response"])

    @parametrize
    async def test_method_call_with_all_params(self, async_client: AsyncOpencode) -> None:
        rpc = await async_client.rpc.call(
            method="method",
            rpc_id="rpcID",
            input={},
            location={
                "directory": "string",
            },
        )
        assert_matches_type(RpcOutput, rpc, path=["response"])

    @parametrize
    async def test_raw_response_call(self, async_client: AsyncOpencode) -> None:
        response = await async_client.rpc.with_raw_response.call(
            method="method",
            rpc_id="rpcID",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rpc = await response.parse()
        assert_matches_type(RpcOutput, rpc, path=["response"])

    @parametrize
    async def test_streaming_response_call(self, async_client: AsyncOpencode) -> None:
        async with async_client.rpc.with_streaming_response.call(
            method="method",
            rpc_id="rpcID",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rpc = await response.parse()
            assert_matches_type(RpcOutput, rpc, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_call(self, async_client: AsyncOpencode) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `rpc_id` but received ''"):
            await async_client.rpc.with_raw_response.call(
                method="method",
                rpc_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `method` but received ''"):
            await async_client.rpc.with_raw_response.call(
                method="",
                rpc_id="rpcID",
            )
