# File generated from our OpenAPI spec by Ferrule. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from opencode import Opencode, AsyncOpencode
from tests.utils import assert_matches_type
from opencode.types.vcs import BranchListResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestBranch:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Opencode) -> None:
        branch = client.vcs.branch.list()
        assert_matches_type(BranchListResponse, branch, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Opencode) -> None:
        branch = client.vcs.branch.list(
            limit=0,
            location={
                "directory": "string",
            },
            search="search",
        )
        assert_matches_type(BranchListResponse, branch, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Opencode) -> None:
        response = client.vcs.branch.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        branch = response.parse()
        assert_matches_type(BranchListResponse, branch, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Opencode) -> None:
        with client.vcs.branch.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            branch = response.parse()
            assert_matches_type(BranchListResponse, branch, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncBranch:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_list(self, async_client: AsyncOpencode) -> None:
        branch = await async_client.vcs.branch.list()
        assert_matches_type(BranchListResponse, branch, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncOpencode) -> None:
        branch = await async_client.vcs.branch.list(
            limit=0,
            location={
                "directory": "string",
            },
            search="search",
        )
        assert_matches_type(BranchListResponse, branch, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncOpencode) -> None:
        response = await async_client.vcs.branch.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        branch = await response.parse()
        assert_matches_type(BranchListResponse, branch, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncOpencode) -> None:
        async with async_client.vcs.branch.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            branch = await response.parse()
            assert_matches_type(BranchListResponse, branch, path=["response"])

        assert cast(Any, response.is_closed) is True
