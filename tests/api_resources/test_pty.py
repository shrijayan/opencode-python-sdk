# File generated from our OpenAPI spec by Ferrule. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from opencode import Opencode, AsyncOpencode
from tests.utils import assert_matches_type
from opencode.types import (
    PtyGetResponse,
    PtyListResponse,
    PtyCreateResponse,
    PtyUpdateResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPty:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Opencode) -> None:
        pty = client.pty.create()
        assert_matches_type(PtyCreateResponse, pty, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Opencode) -> None:
        pty = client.pty.create(
            args=["string"],
            command="command",
            cwd="cwd",
            env={"foo": "string"},
            location={
                "directory": "string",
            },
            title="title",
        )
        assert_matches_type(PtyCreateResponse, pty, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Opencode) -> None:
        response = client.pty.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pty = response.parse()
        assert_matches_type(PtyCreateResponse, pty, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Opencode) -> None:
        with client.pty.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pty = response.parse()
            assert_matches_type(PtyCreateResponse, pty, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_update(self, client: Opencode) -> None:
        pty = client.pty.update(
            pty_id={},
        )
        assert_matches_type(PtyUpdateResponse, pty, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Opencode) -> None:
        pty = client.pty.update(
            pty_id={},
            location={
                "directory": "string",
            },
            size={
                "cols": 0,
                "rows": 0,
            },
            title="title",
        )
        assert_matches_type(PtyUpdateResponse, pty, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Opencode) -> None:
        response = client.pty.with_raw_response.update(
            pty_id={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pty = response.parse()
        assert_matches_type(PtyUpdateResponse, pty, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Opencode) -> None:
        with client.pty.with_streaming_response.update(
            pty_id={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pty = response.parse()
            assert_matches_type(PtyUpdateResponse, pty, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Opencode) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `pty_id` but received ''"):
            client.pty.with_raw_response.update(
                pty_id="",
            )

    @parametrize
    def test_method_list(self, client: Opencode) -> None:
        pty = client.pty.list()
        assert_matches_type(PtyListResponse, pty, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Opencode) -> None:
        pty = client.pty.list(
            location={
                "directory": "string",
            },
        )
        assert_matches_type(PtyListResponse, pty, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Opencode) -> None:
        response = client.pty.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pty = response.parse()
        assert_matches_type(PtyListResponse, pty, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Opencode) -> None:
        with client.pty.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pty = response.parse()
            assert_matches_type(PtyListResponse, pty, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_get(self, client: Opencode) -> None:
        pty = client.pty.get(
            pty_id={},
        )
        assert_matches_type(PtyGetResponse, pty, path=["response"])

    @parametrize
    def test_method_get_with_all_params(self, client: Opencode) -> None:
        pty = client.pty.get(
            pty_id={},
            location={
                "directory": "string",
            },
        )
        assert_matches_type(PtyGetResponse, pty, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Opencode) -> None:
        response = client.pty.with_raw_response.get(
            pty_id={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pty = response.parse()
        assert_matches_type(PtyGetResponse, pty, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Opencode) -> None:
        with client.pty.with_streaming_response.get(
            pty_id={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pty = response.parse()
            assert_matches_type(PtyGetResponse, pty, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Opencode) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `pty_id` but received ''"):
            client.pty.with_raw_response.get(
                pty_id="",
            )

    @parametrize
    def test_method_remove(self, client: Opencode) -> None:
        pty = client.pty.remove(
            pty_id={},
        )
        assert pty is None

    @parametrize
    def test_method_remove_with_all_params(self, client: Opencode) -> None:
        pty = client.pty.remove(
            pty_id={},
            location={
                "directory": "string",
            },
        )
        assert pty is None

    @parametrize
    def test_raw_response_remove(self, client: Opencode) -> None:
        response = client.pty.with_raw_response.remove(
            pty_id={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pty = response.parse()
        assert pty is None

    @parametrize
    def test_streaming_response_remove(self, client: Opencode) -> None:
        with client.pty.with_streaming_response.remove(
            pty_id={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pty = response.parse()
            assert pty is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_remove(self, client: Opencode) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `pty_id` but received ''"):
            client.pty.with_raw_response.remove(
                pty_id="",
            )


class TestAsyncPty:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncOpencode) -> None:
        pty = await async_client.pty.create()
        assert_matches_type(PtyCreateResponse, pty, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncOpencode) -> None:
        pty = await async_client.pty.create(
            args=["string"],
            command="command",
            cwd="cwd",
            env={"foo": "string"},
            location={
                "directory": "string",
            },
            title="title",
        )
        assert_matches_type(PtyCreateResponse, pty, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncOpencode) -> None:
        response = await async_client.pty.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pty = await response.parse()
        assert_matches_type(PtyCreateResponse, pty, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncOpencode) -> None:
        async with async_client.pty.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pty = await response.parse()
            assert_matches_type(PtyCreateResponse, pty, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_update(self, async_client: AsyncOpencode) -> None:
        pty = await async_client.pty.update(
            pty_id={},
        )
        assert_matches_type(PtyUpdateResponse, pty, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncOpencode) -> None:
        pty = await async_client.pty.update(
            pty_id={},
            location={
                "directory": "string",
            },
            size={
                "cols": 0,
                "rows": 0,
            },
            title="title",
        )
        assert_matches_type(PtyUpdateResponse, pty, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncOpencode) -> None:
        response = await async_client.pty.with_raw_response.update(
            pty_id={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pty = await response.parse()
        assert_matches_type(PtyUpdateResponse, pty, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncOpencode) -> None:
        async with async_client.pty.with_streaming_response.update(
            pty_id={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pty = await response.parse()
            assert_matches_type(PtyUpdateResponse, pty, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncOpencode) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `pty_id` but received ''"):
            await async_client.pty.with_raw_response.update(
                pty_id="",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncOpencode) -> None:
        pty = await async_client.pty.list()
        assert_matches_type(PtyListResponse, pty, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncOpencode) -> None:
        pty = await async_client.pty.list(
            location={
                "directory": "string",
            },
        )
        assert_matches_type(PtyListResponse, pty, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncOpencode) -> None:
        response = await async_client.pty.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pty = await response.parse()
        assert_matches_type(PtyListResponse, pty, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncOpencode) -> None:
        async with async_client.pty.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pty = await response.parse()
            assert_matches_type(PtyListResponse, pty, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_get(self, async_client: AsyncOpencode) -> None:
        pty = await async_client.pty.get(
            pty_id={},
        )
        assert_matches_type(PtyGetResponse, pty, path=["response"])

    @parametrize
    async def test_method_get_with_all_params(self, async_client: AsyncOpencode) -> None:
        pty = await async_client.pty.get(
            pty_id={},
            location={
                "directory": "string",
            },
        )
        assert_matches_type(PtyGetResponse, pty, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncOpencode) -> None:
        response = await async_client.pty.with_raw_response.get(
            pty_id={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pty = await response.parse()
        assert_matches_type(PtyGetResponse, pty, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncOpencode) -> None:
        async with async_client.pty.with_streaming_response.get(
            pty_id={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pty = await response.parse()
            assert_matches_type(PtyGetResponse, pty, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncOpencode) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `pty_id` but received ''"):
            await async_client.pty.with_raw_response.get(
                pty_id="",
            )

    @parametrize
    async def test_method_remove(self, async_client: AsyncOpencode) -> None:
        pty = await async_client.pty.remove(
            pty_id={},
        )
        assert pty is None

    @parametrize
    async def test_method_remove_with_all_params(self, async_client: AsyncOpencode) -> None:
        pty = await async_client.pty.remove(
            pty_id={},
            location={
                "directory": "string",
            },
        )
        assert pty is None

    @parametrize
    async def test_raw_response_remove(self, async_client: AsyncOpencode) -> None:
        response = await async_client.pty.with_raw_response.remove(
            pty_id={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pty = await response.parse()
        assert pty is None

    @parametrize
    async def test_streaming_response_remove(self, async_client: AsyncOpencode) -> None:
        async with async_client.pty.with_streaming_response.remove(
            pty_id={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pty = await response.parse()
            assert pty is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_remove(self, async_client: AsyncOpencode) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `pty_id` but received ''"):
            await async_client.pty.with_raw_response.remove(
                pty_id="",
            )
