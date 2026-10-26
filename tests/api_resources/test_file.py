# File generated from our OpenAPI spec by Ferrule. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from opencode import Opencode, AsyncOpencode
from tests.utils import assert_matches_type
from opencode.types import FileFindResponse, FileListResponse, FileWriteResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestFile:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Opencode) -> None:
        file = client.file.list()
        assert_matches_type(FileListResponse, file, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Opencode) -> None:
        file = client.file.list(
            location={
                "directory": "string",
            },
            path="path",
        )
        assert_matches_type(FileListResponse, file, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Opencode) -> None:
        response = client.file.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = response.parse()
        assert_matches_type(FileListResponse, file, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Opencode) -> None:
        with client.file.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = response.parse()
            assert_matches_type(FileListResponse, file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_find(self, client: Opencode) -> None:
        file = client.file.find(
            query="query",
        )
        assert_matches_type(FileFindResponse, file, path=["response"])

    @parametrize
    def test_method_find_with_all_params(self, client: Opencode) -> None:
        file = client.file.find(
            query="query",
            limit=0,
            location={
                "directory": "string",
            },
            type="file",
        )
        assert_matches_type(FileFindResponse, file, path=["response"])

    @parametrize
    def test_raw_response_find(self, client: Opencode) -> None:
        response = client.file.with_raw_response.find(
            query="query",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = response.parse()
        assert_matches_type(FileFindResponse, file, path=["response"])

    @parametrize
    def test_streaming_response_find(self, client: Opencode) -> None:
        with client.file.with_streaming_response.find(
            query="query",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = response.parse()
            assert_matches_type(FileFindResponse, file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_read(self, client: Opencode) -> None:
        file = client.file.read(
            path="path",
        )
        assert file is None

    @parametrize
    def test_method_read_with_all_params(self, client: Opencode) -> None:
        file = client.file.read(
            path="path",
            location={
                "directory": "string",
            },
        )
        assert file is None

    @parametrize
    def test_raw_response_read(self, client: Opencode) -> None:
        response = client.file.with_raw_response.read(
            path="path",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = response.parse()
        assert file is None

    @parametrize
    def test_streaming_response_read(self, client: Opencode) -> None:
        with client.file.with_streaming_response.read(
            path="path",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = response.parse()
            assert file is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_read(self, client: Opencode) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path` but received ''"):
            client.file.with_raw_response.read(
                path="",
            )

    @parametrize
    def test_method_write(self, client: Opencode) -> None:
        file = client.file.write(
            body=b"raw file contents",
            path="path",
        )
        assert_matches_type(FileWriteResponse, file, path=["response"])

    @parametrize
    def test_method_write_with_all_params(self, client: Opencode) -> None:
        file = client.file.write(
            body=b"raw file contents",
            path="path",
            location={
                "directory": "string",
            },
        )
        assert_matches_type(FileWriteResponse, file, path=["response"])

    @parametrize
    def test_raw_response_write(self, client: Opencode) -> None:
        response = client.file.with_raw_response.write(
            body=b"raw file contents",
            path="path",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = response.parse()
        assert_matches_type(FileWriteResponse, file, path=["response"])

    @parametrize
    def test_streaming_response_write(self, client: Opencode) -> None:
        with client.file.with_streaming_response.write(
            body=b"raw file contents",
            path="path",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = response.parse()
            assert_matches_type(FileWriteResponse, file, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncFile:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_list(self, async_client: AsyncOpencode) -> None:
        file = await async_client.file.list()
        assert_matches_type(FileListResponse, file, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncOpencode) -> None:
        file = await async_client.file.list(
            location={
                "directory": "string",
            },
            path="path",
        )
        assert_matches_type(FileListResponse, file, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncOpencode) -> None:
        response = await async_client.file.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = await response.parse()
        assert_matches_type(FileListResponse, file, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncOpencode) -> None:
        async with async_client.file.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = await response.parse()
            assert_matches_type(FileListResponse, file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_find(self, async_client: AsyncOpencode) -> None:
        file = await async_client.file.find(
            query="query",
        )
        assert_matches_type(FileFindResponse, file, path=["response"])

    @parametrize
    async def test_method_find_with_all_params(self, async_client: AsyncOpencode) -> None:
        file = await async_client.file.find(
            query="query",
            limit=0,
            location={
                "directory": "string",
            },
            type="file",
        )
        assert_matches_type(FileFindResponse, file, path=["response"])

    @parametrize
    async def test_raw_response_find(self, async_client: AsyncOpencode) -> None:
        response = await async_client.file.with_raw_response.find(
            query="query",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = await response.parse()
        assert_matches_type(FileFindResponse, file, path=["response"])

    @parametrize
    async def test_streaming_response_find(self, async_client: AsyncOpencode) -> None:
        async with async_client.file.with_streaming_response.find(
            query="query",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = await response.parse()
            assert_matches_type(FileFindResponse, file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_read(self, async_client: AsyncOpencode) -> None:
        file = await async_client.file.read(
            path="path",
        )
        assert file is None

    @parametrize
    async def test_method_read_with_all_params(self, async_client: AsyncOpencode) -> None:
        file = await async_client.file.read(
            path="path",
            location={
                "directory": "string",
            },
        )
        assert file is None

    @parametrize
    async def test_raw_response_read(self, async_client: AsyncOpencode) -> None:
        response = await async_client.file.with_raw_response.read(
            path="path",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = await response.parse()
        assert file is None

    @parametrize
    async def test_streaming_response_read(self, async_client: AsyncOpencode) -> None:
        async with async_client.file.with_streaming_response.read(
            path="path",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = await response.parse()
            assert file is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_read(self, async_client: AsyncOpencode) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path` but received ''"):
            await async_client.file.with_raw_response.read(
                path="",
            )

    @parametrize
    async def test_method_write(self, async_client: AsyncOpencode) -> None:
        file = await async_client.file.write(
            body=b"raw file contents",
            path="path",
        )
        assert_matches_type(FileWriteResponse, file, path=["response"])

    @parametrize
    async def test_method_write_with_all_params(self, async_client: AsyncOpencode) -> None:
        file = await async_client.file.write(
            body=b"raw file contents",
            path="path",
            location={
                "directory": "string",
            },
        )
        assert_matches_type(FileWriteResponse, file, path=["response"])

    @parametrize
    async def test_raw_response_write(self, async_client: AsyncOpencode) -> None:
        response = await async_client.file.with_raw_response.write(
            body=b"raw file contents",
            path="path",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = await response.parse()
        assert_matches_type(FileWriteResponse, file, path=["response"])

    @parametrize
    async def test_streaming_response_write(self, async_client: AsyncOpencode) -> None:
        async with async_client.file.with_streaming_response.write(
            body=b"raw file contents",
            path="path",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = await response.parse()
            assert_matches_type(FileWriteResponse, file, path=["response"])

        assert cast(Any, response.is_closed) is True
