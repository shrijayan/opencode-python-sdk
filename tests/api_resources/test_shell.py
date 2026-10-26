# File generated from our OpenAPI spec by Ferrule. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from opencode import Opencode, AsyncOpencode
from tests.utils import assert_matches_type
from opencode.types import (
    ShellGetResponse,
    ShellListResponse,
    ShellCreateResponse,
    ShellOutputResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestShell:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Opencode) -> None:
        shell = client.shell.create(
            command="command",
        )
        assert_matches_type(ShellCreateResponse, shell, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Opencode) -> None:
        shell = client.shell.create(
            command="command",
            api_timeout=0,
            cwd="cwd",
            location={
                "directory": "string",
            },
            metadata={"foo": {}},
        )
        assert_matches_type(ShellCreateResponse, shell, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Opencode) -> None:
        response = client.shell.with_raw_response.create(
            command="command",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        shell = response.parse()
        assert_matches_type(ShellCreateResponse, shell, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Opencode) -> None:
        with client.shell.with_streaming_response.create(
            command="command",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            shell = response.parse()
            assert_matches_type(ShellCreateResponse, shell, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_list(self, client: Opencode) -> None:
        shell = client.shell.list()
        assert_matches_type(ShellListResponse, shell, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Opencode) -> None:
        shell = client.shell.list(
            location={
                "directory": "string",
            },
        )
        assert_matches_type(ShellListResponse, shell, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Opencode) -> None:
        response = client.shell.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        shell = response.parse()
        assert_matches_type(ShellListResponse, shell, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Opencode) -> None:
        with client.shell.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            shell = response.parse()
            assert_matches_type(ShellListResponse, shell, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_get(self, client: Opencode) -> None:
        shell = client.shell.get(
            id={},
        )
        assert_matches_type(ShellGetResponse, shell, path=["response"])

    @parametrize
    def test_method_get_with_all_params(self, client: Opencode) -> None:
        shell = client.shell.get(
            id={},
            location={
                "directory": "string",
            },
        )
        assert_matches_type(ShellGetResponse, shell, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Opencode) -> None:
        response = client.shell.with_raw_response.get(
            id={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        shell = response.parse()
        assert_matches_type(ShellGetResponse, shell, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Opencode) -> None:
        with client.shell.with_streaming_response.get(
            id={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            shell = response.parse()
            assert_matches_type(ShellGetResponse, shell, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Opencode) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.shell.with_raw_response.get(
                id="",
            )

    @parametrize
    def test_method_output(self, client: Opencode) -> None:
        shell = client.shell.output(
            id={},
        )
        assert_matches_type(ShellOutputResponse, shell, path=["response"])

    @parametrize
    def test_method_output_with_all_params(self, client: Opencode) -> None:
        shell = client.shell.output(
            id={},
            cursor=0,
            limit=0,
            location={
                "directory": "string",
            },
        )
        assert_matches_type(ShellOutputResponse, shell, path=["response"])

    @parametrize
    def test_raw_response_output(self, client: Opencode) -> None:
        response = client.shell.with_raw_response.output(
            id={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        shell = response.parse()
        assert_matches_type(ShellOutputResponse, shell, path=["response"])

    @parametrize
    def test_streaming_response_output(self, client: Opencode) -> None:
        with client.shell.with_streaming_response.output(
            id={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            shell = response.parse()
            assert_matches_type(ShellOutputResponse, shell, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_output(self, client: Opencode) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.shell.with_raw_response.output(
                id="",
            )

    @parametrize
    def test_method_remove(self, client: Opencode) -> None:
        shell = client.shell.remove(
            id={},
        )
        assert shell is None

    @parametrize
    def test_method_remove_with_all_params(self, client: Opencode) -> None:
        shell = client.shell.remove(
            id={},
            location={
                "directory": "string",
            },
        )
        assert shell is None

    @parametrize
    def test_raw_response_remove(self, client: Opencode) -> None:
        response = client.shell.with_raw_response.remove(
            id={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        shell = response.parse()
        assert shell is None

    @parametrize
    def test_streaming_response_remove(self, client: Opencode) -> None:
        with client.shell.with_streaming_response.remove(
            id={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            shell = response.parse()
            assert shell is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_remove(self, client: Opencode) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.shell.with_raw_response.remove(
                id="",
            )


class TestAsyncShell:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncOpencode) -> None:
        shell = await async_client.shell.create(
            command="command",
        )
        assert_matches_type(ShellCreateResponse, shell, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncOpencode) -> None:
        shell = await async_client.shell.create(
            command="command",
            api_timeout=0,
            cwd="cwd",
            location={
                "directory": "string",
            },
            metadata={"foo": {}},
        )
        assert_matches_type(ShellCreateResponse, shell, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncOpencode) -> None:
        response = await async_client.shell.with_raw_response.create(
            command="command",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        shell = await response.parse()
        assert_matches_type(ShellCreateResponse, shell, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncOpencode) -> None:
        async with async_client.shell.with_streaming_response.create(
            command="command",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            shell = await response.parse()
            assert_matches_type(ShellCreateResponse, shell, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_list(self, async_client: AsyncOpencode) -> None:
        shell = await async_client.shell.list()
        assert_matches_type(ShellListResponse, shell, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncOpencode) -> None:
        shell = await async_client.shell.list(
            location={
                "directory": "string",
            },
        )
        assert_matches_type(ShellListResponse, shell, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncOpencode) -> None:
        response = await async_client.shell.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        shell = await response.parse()
        assert_matches_type(ShellListResponse, shell, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncOpencode) -> None:
        async with async_client.shell.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            shell = await response.parse()
            assert_matches_type(ShellListResponse, shell, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_get(self, async_client: AsyncOpencode) -> None:
        shell = await async_client.shell.get(
            id={},
        )
        assert_matches_type(ShellGetResponse, shell, path=["response"])

    @parametrize
    async def test_method_get_with_all_params(self, async_client: AsyncOpencode) -> None:
        shell = await async_client.shell.get(
            id={},
            location={
                "directory": "string",
            },
        )
        assert_matches_type(ShellGetResponse, shell, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncOpencode) -> None:
        response = await async_client.shell.with_raw_response.get(
            id={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        shell = await response.parse()
        assert_matches_type(ShellGetResponse, shell, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncOpencode) -> None:
        async with async_client.shell.with_streaming_response.get(
            id={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            shell = await response.parse()
            assert_matches_type(ShellGetResponse, shell, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncOpencode) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.shell.with_raw_response.get(
                id="",
            )

    @parametrize
    async def test_method_output(self, async_client: AsyncOpencode) -> None:
        shell = await async_client.shell.output(
            id={},
        )
        assert_matches_type(ShellOutputResponse, shell, path=["response"])

    @parametrize
    async def test_method_output_with_all_params(self, async_client: AsyncOpencode) -> None:
        shell = await async_client.shell.output(
            id={},
            cursor=0,
            limit=0,
            location={
                "directory": "string",
            },
        )
        assert_matches_type(ShellOutputResponse, shell, path=["response"])

    @parametrize
    async def test_raw_response_output(self, async_client: AsyncOpencode) -> None:
        response = await async_client.shell.with_raw_response.output(
            id={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        shell = await response.parse()
        assert_matches_type(ShellOutputResponse, shell, path=["response"])

    @parametrize
    async def test_streaming_response_output(self, async_client: AsyncOpencode) -> None:
        async with async_client.shell.with_streaming_response.output(
            id={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            shell = await response.parse()
            assert_matches_type(ShellOutputResponse, shell, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_output(self, async_client: AsyncOpencode) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.shell.with_raw_response.output(
                id="",
            )

    @parametrize
    async def test_method_remove(self, async_client: AsyncOpencode) -> None:
        shell = await async_client.shell.remove(
            id={},
        )
        assert shell is None

    @parametrize
    async def test_method_remove_with_all_params(self, async_client: AsyncOpencode) -> None:
        shell = await async_client.shell.remove(
            id={},
            location={
                "directory": "string",
            },
        )
        assert shell is None

    @parametrize
    async def test_raw_response_remove(self, async_client: AsyncOpencode) -> None:
        response = await async_client.shell.with_raw_response.remove(
            id={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        shell = await response.parse()
        assert shell is None

    @parametrize
    async def test_streaming_response_remove(self, async_client: AsyncOpencode) -> None:
        async with async_client.shell.with_streaming_response.remove(
            id={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            shell = await response.parse()
            assert shell is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_remove(self, async_client: AsyncOpencode) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.shell.with_raw_response.remove(
                id="",
            )
