# File generated from our OpenAPI spec by Ferrule. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from opencode import Opencode, AsyncOpencode
from tests.utils import assert_matches_type
from opencode.types import (
    VcGetResponse,
    VcBaseResponse,
    VcDiffResponse,
    VcStatusResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestVcs:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_base(self, client: Opencode) -> None:
        vc = client.vcs.base()
        assert_matches_type(VcBaseResponse, vc, path=["response"])

    @parametrize
    def test_method_base_with_all_params(self, client: Opencode) -> None:
        vc = client.vcs.base(
            location={
                "directory": "string",
            },
        )
        assert_matches_type(VcBaseResponse, vc, path=["response"])

    @parametrize
    def test_raw_response_base(self, client: Opencode) -> None:
        response = client.vcs.with_raw_response.base()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        vc = response.parse()
        assert_matches_type(VcBaseResponse, vc, path=["response"])

    @parametrize
    def test_streaming_response_base(self, client: Opencode) -> None:
        with client.vcs.with_streaming_response.base() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            vc = response.parse()
            assert_matches_type(VcBaseResponse, vc, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_diff(self, client: Opencode) -> None:
        vc = client.vcs.diff(
            mode={},
        )
        assert_matches_type(VcDiffResponse, vc, path=["response"])

    @parametrize
    def test_method_diff_with_all_params(self, client: Opencode) -> None:
        vc = client.vcs.diff(
            mode={},
            base="base",
            context=0,
            location={
                "directory": "string",
            },
        )
        assert_matches_type(VcDiffResponse, vc, path=["response"])

    @parametrize
    def test_raw_response_diff(self, client: Opencode) -> None:
        response = client.vcs.with_raw_response.diff(
            mode={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        vc = response.parse()
        assert_matches_type(VcDiffResponse, vc, path=["response"])

    @parametrize
    def test_streaming_response_diff(self, client: Opencode) -> None:
        with client.vcs.with_streaming_response.diff(
            mode={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            vc = response.parse()
            assert_matches_type(VcDiffResponse, vc, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_get(self, client: Opencode) -> None:
        vc = client.vcs.get()
        assert_matches_type(VcGetResponse, vc, path=["response"])

    @parametrize
    def test_method_get_with_all_params(self, client: Opencode) -> None:
        vc = client.vcs.get(
            location={
                "directory": "string",
            },
        )
        assert_matches_type(VcGetResponse, vc, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Opencode) -> None:
        response = client.vcs.with_raw_response.get()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        vc = response.parse()
        assert_matches_type(VcGetResponse, vc, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Opencode) -> None:
        with client.vcs.with_streaming_response.get() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            vc = response.parse()
            assert_matches_type(VcGetResponse, vc, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_init(self, client: Opencode) -> None:
        vc = client.vcs.init()
        assert vc is None

    @parametrize
    def test_method_init_with_all_params(self, client: Opencode) -> None:
        vc = client.vcs.init(
            location={
                "directory": "string",
            },
            provider="provider",
        )
        assert vc is None

    @parametrize
    def test_raw_response_init(self, client: Opencode) -> None:
        response = client.vcs.with_raw_response.init()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        vc = response.parse()
        assert vc is None

    @parametrize
    def test_streaming_response_init(self, client: Opencode) -> None:
        with client.vcs.with_streaming_response.init() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            vc = response.parse()
            assert vc is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_status(self, client: Opencode) -> None:
        vc = client.vcs.status()
        assert_matches_type(VcStatusResponse, vc, path=["response"])

    @parametrize
    def test_method_status_with_all_params(self, client: Opencode) -> None:
        vc = client.vcs.status(
            location={
                "directory": "string",
            },
        )
        assert_matches_type(VcStatusResponse, vc, path=["response"])

    @parametrize
    def test_raw_response_status(self, client: Opencode) -> None:
        response = client.vcs.with_raw_response.status()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        vc = response.parse()
        assert_matches_type(VcStatusResponse, vc, path=["response"])

    @parametrize
    def test_streaming_response_status(self, client: Opencode) -> None:
        with client.vcs.with_streaming_response.status() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            vc = response.parse()
            assert_matches_type(VcStatusResponse, vc, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncVcs:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_base(self, async_client: AsyncOpencode) -> None:
        vc = await async_client.vcs.base()
        assert_matches_type(VcBaseResponse, vc, path=["response"])

    @parametrize
    async def test_method_base_with_all_params(self, async_client: AsyncOpencode) -> None:
        vc = await async_client.vcs.base(
            location={
                "directory": "string",
            },
        )
        assert_matches_type(VcBaseResponse, vc, path=["response"])

    @parametrize
    async def test_raw_response_base(self, async_client: AsyncOpencode) -> None:
        response = await async_client.vcs.with_raw_response.base()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        vc = await response.parse()
        assert_matches_type(VcBaseResponse, vc, path=["response"])

    @parametrize
    async def test_streaming_response_base(self, async_client: AsyncOpencode) -> None:
        async with async_client.vcs.with_streaming_response.base() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            vc = await response.parse()
            assert_matches_type(VcBaseResponse, vc, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_diff(self, async_client: AsyncOpencode) -> None:
        vc = await async_client.vcs.diff(
            mode={},
        )
        assert_matches_type(VcDiffResponse, vc, path=["response"])

    @parametrize
    async def test_method_diff_with_all_params(self, async_client: AsyncOpencode) -> None:
        vc = await async_client.vcs.diff(
            mode={},
            base="base",
            context=0,
            location={
                "directory": "string",
            },
        )
        assert_matches_type(VcDiffResponse, vc, path=["response"])

    @parametrize
    async def test_raw_response_diff(self, async_client: AsyncOpencode) -> None:
        response = await async_client.vcs.with_raw_response.diff(
            mode={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        vc = await response.parse()
        assert_matches_type(VcDiffResponse, vc, path=["response"])

    @parametrize
    async def test_streaming_response_diff(self, async_client: AsyncOpencode) -> None:
        async with async_client.vcs.with_streaming_response.diff(
            mode={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            vc = await response.parse()
            assert_matches_type(VcDiffResponse, vc, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_get(self, async_client: AsyncOpencode) -> None:
        vc = await async_client.vcs.get()
        assert_matches_type(VcGetResponse, vc, path=["response"])

    @parametrize
    async def test_method_get_with_all_params(self, async_client: AsyncOpencode) -> None:
        vc = await async_client.vcs.get(
            location={
                "directory": "string",
            },
        )
        assert_matches_type(VcGetResponse, vc, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncOpencode) -> None:
        response = await async_client.vcs.with_raw_response.get()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        vc = await response.parse()
        assert_matches_type(VcGetResponse, vc, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncOpencode) -> None:
        async with async_client.vcs.with_streaming_response.get() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            vc = await response.parse()
            assert_matches_type(VcGetResponse, vc, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_init(self, async_client: AsyncOpencode) -> None:
        vc = await async_client.vcs.init()
        assert vc is None

    @parametrize
    async def test_method_init_with_all_params(self, async_client: AsyncOpencode) -> None:
        vc = await async_client.vcs.init(
            location={
                "directory": "string",
            },
            provider="provider",
        )
        assert vc is None

    @parametrize
    async def test_raw_response_init(self, async_client: AsyncOpencode) -> None:
        response = await async_client.vcs.with_raw_response.init()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        vc = await response.parse()
        assert vc is None

    @parametrize
    async def test_streaming_response_init(self, async_client: AsyncOpencode) -> None:
        async with async_client.vcs.with_streaming_response.init() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            vc = await response.parse()
            assert vc is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_status(self, async_client: AsyncOpencode) -> None:
        vc = await async_client.vcs.status()
        assert_matches_type(VcStatusResponse, vc, path=["response"])

    @parametrize
    async def test_method_status_with_all_params(self, async_client: AsyncOpencode) -> None:
        vc = await async_client.vcs.status(
            location={
                "directory": "string",
            },
        )
        assert_matches_type(VcStatusResponse, vc, path=["response"])

    @parametrize
    async def test_raw_response_status(self, async_client: AsyncOpencode) -> None:
        response = await async_client.vcs.with_raw_response.status()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        vc = await response.parse()
        assert_matches_type(VcStatusResponse, vc, path=["response"])

    @parametrize
    async def test_streaming_response_status(self, async_client: AsyncOpencode) -> None:
        async with async_client.vcs.with_streaming_response.status() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            vc = await response.parse()
            assert_matches_type(VcStatusResponse, vc, path=["response"])

        assert cast(Any, response.is_closed) is True
