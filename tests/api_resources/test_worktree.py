# File generated from our OpenAPI spec by Ferrule. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from opencode import Opencode, AsyncOpencode
from tests.utils import assert_matches_type
from opencode.types.shared import WorktreeInfo, WorktreeList

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestWorktree:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Opencode) -> None:
        worktree = client.worktree.create(
            project_id={},
        )
        assert_matches_type(WorktreeInfo, worktree, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Opencode) -> None:
        worktree = client.worktree.create(
            project_id={},
            branch="branch",
            directory={},
            from_={},
            name="name",
        )
        assert_matches_type(WorktreeInfo, worktree, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Opencode) -> None:
        response = client.worktree.with_raw_response.create(
            project_id={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        worktree = response.parse()
        assert_matches_type(WorktreeInfo, worktree, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Opencode) -> None:
        with client.worktree.with_streaming_response.create(
            project_id={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            worktree = response.parse()
            assert_matches_type(WorktreeInfo, worktree, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_list(self, client: Opencode) -> None:
        worktree = client.worktree.list(
            project_id={},
        )
        assert_matches_type(WorktreeList, worktree, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Opencode) -> None:
        response = client.worktree.with_raw_response.list(
            project_id={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        worktree = response.parse()
        assert_matches_type(WorktreeList, worktree, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Opencode) -> None:
        with client.worktree.with_streaming_response.list(
            project_id={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            worktree = response.parse()
            assert_matches_type(WorktreeList, worktree, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_refresh(self, client: Opencode) -> None:
        worktree = client.worktree.refresh(
            project_id={},
        )
        assert worktree is None

    @parametrize
    def test_raw_response_refresh(self, client: Opencode) -> None:
        response = client.worktree.with_raw_response.refresh(
            project_id={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        worktree = response.parse()
        assert worktree is None

    @parametrize
    def test_streaming_response_refresh(self, client: Opencode) -> None:
        with client.worktree.with_streaming_response.refresh(
            project_id={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            worktree = response.parse()
            assert worktree is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_remove(self, client: Opencode) -> None:
        worktree = client.worktree.remove(
            directory={},
            force=True,
            project_id={},
        )
        assert worktree is None

    @parametrize
    def test_raw_response_remove(self, client: Opencode) -> None:
        response = client.worktree.with_raw_response.remove(
            directory={},
            force=True,
            project_id={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        worktree = response.parse()
        assert worktree is None

    @parametrize
    def test_streaming_response_remove(self, client: Opencode) -> None:
        with client.worktree.with_streaming_response.remove(
            directory={},
            force=True,
            project_id={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            worktree = response.parse()
            assert worktree is None

        assert cast(Any, response.is_closed) is True


class TestAsyncWorktree:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncOpencode) -> None:
        worktree = await async_client.worktree.create(
            project_id={},
        )
        assert_matches_type(WorktreeInfo, worktree, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncOpencode) -> None:
        worktree = await async_client.worktree.create(
            project_id={},
            branch="branch",
            directory={},
            from_={},
            name="name",
        )
        assert_matches_type(WorktreeInfo, worktree, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncOpencode) -> None:
        response = await async_client.worktree.with_raw_response.create(
            project_id={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        worktree = await response.parse()
        assert_matches_type(WorktreeInfo, worktree, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncOpencode) -> None:
        async with async_client.worktree.with_streaming_response.create(
            project_id={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            worktree = await response.parse()
            assert_matches_type(WorktreeInfo, worktree, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_list(self, async_client: AsyncOpencode) -> None:
        worktree = await async_client.worktree.list(
            project_id={},
        )
        assert_matches_type(WorktreeList, worktree, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncOpencode) -> None:
        response = await async_client.worktree.with_raw_response.list(
            project_id={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        worktree = await response.parse()
        assert_matches_type(WorktreeList, worktree, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncOpencode) -> None:
        async with async_client.worktree.with_streaming_response.list(
            project_id={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            worktree = await response.parse()
            assert_matches_type(WorktreeList, worktree, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_refresh(self, async_client: AsyncOpencode) -> None:
        worktree = await async_client.worktree.refresh(
            project_id={},
        )
        assert worktree is None

    @parametrize
    async def test_raw_response_refresh(self, async_client: AsyncOpencode) -> None:
        response = await async_client.worktree.with_raw_response.refresh(
            project_id={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        worktree = await response.parse()
        assert worktree is None

    @parametrize
    async def test_streaming_response_refresh(self, async_client: AsyncOpencode) -> None:
        async with async_client.worktree.with_streaming_response.refresh(
            project_id={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            worktree = await response.parse()
            assert worktree is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_remove(self, async_client: AsyncOpencode) -> None:
        worktree = await async_client.worktree.remove(
            directory={},
            force=True,
            project_id={},
        )
        assert worktree is None

    @parametrize
    async def test_raw_response_remove(self, async_client: AsyncOpencode) -> None:
        response = await async_client.worktree.with_raw_response.remove(
            directory={},
            force=True,
            project_id={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        worktree = await response.parse()
        assert worktree is None

    @parametrize
    async def test_streaming_response_remove(self, async_client: AsyncOpencode) -> None:
        async with async_client.worktree.with_streaming_response.remove(
            directory={},
            force=True,
            project_id={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            worktree = await response.parse()
            assert worktree is None

        assert cast(Any, response.is_closed) is True
