# File generated from our OpenAPI spec by Ferrule. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from opencode import Opencode, AsyncOpencode
from tests.utils import assert_matches_type
from opencode.types.session.instructions import EntryListResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestEntry:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Opencode) -> None:
        entry = client.session.instructions.entry.list(
            "sessionID",
        )
        assert_matches_type(EntryListResponse, entry, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Opencode) -> None:
        response = client.session.instructions.entry.with_raw_response.list(
            "sessionID",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        entry = response.parse()
        assert_matches_type(EntryListResponse, entry, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Opencode) -> None:
        with client.session.instructions.entry.with_streaming_response.list(
            "sessionID",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            entry = response.parse()
            assert_matches_type(EntryListResponse, entry, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Opencode) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            client.session.instructions.entry.with_raw_response.list(
                "",
            )

    @parametrize
    def test_method_put(self, client: Opencode) -> None:
        entry = client.session.instructions.entry.put(
            key="key",
            session_id="sessionID",
            value={},
        )
        assert entry is None

    @parametrize
    def test_raw_response_put(self, client: Opencode) -> None:
        response = client.session.instructions.entry.with_raw_response.put(
            key="key",
            session_id="sessionID",
            value={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        entry = response.parse()
        assert entry is None

    @parametrize
    def test_streaming_response_put(self, client: Opencode) -> None:
        with client.session.instructions.entry.with_streaming_response.put(
            key="key",
            session_id="sessionID",
            value={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            entry = response.parse()
            assert entry is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_put(self, client: Opencode) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            client.session.instructions.entry.with_raw_response.put(
                key="key",
                session_id="",
                value={},
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `key` but received ''"):
            client.session.instructions.entry.with_raw_response.put(
                key="",
                session_id="sessionID",
                value={},
            )

    @parametrize
    def test_method_remove(self, client: Opencode) -> None:
        entry = client.session.instructions.entry.remove(
            key="key",
            session_id="sessionID",
        )
        assert entry is None

    @parametrize
    def test_raw_response_remove(self, client: Opencode) -> None:
        response = client.session.instructions.entry.with_raw_response.remove(
            key="key",
            session_id="sessionID",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        entry = response.parse()
        assert entry is None

    @parametrize
    def test_streaming_response_remove(self, client: Opencode) -> None:
        with client.session.instructions.entry.with_streaming_response.remove(
            key="key",
            session_id="sessionID",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            entry = response.parse()
            assert entry is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_remove(self, client: Opencode) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            client.session.instructions.entry.with_raw_response.remove(
                key="key",
                session_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `key` but received ''"):
            client.session.instructions.entry.with_raw_response.remove(
                key="",
                session_id="sessionID",
            )


class TestAsyncEntry:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_list(self, async_client: AsyncOpencode) -> None:
        entry = await async_client.session.instructions.entry.list(
            "sessionID",
        )
        assert_matches_type(EntryListResponse, entry, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncOpencode) -> None:
        response = await async_client.session.instructions.entry.with_raw_response.list(
            "sessionID",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        entry = await response.parse()
        assert_matches_type(EntryListResponse, entry, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncOpencode) -> None:
        async with async_client.session.instructions.entry.with_streaming_response.list(
            "sessionID",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            entry = await response.parse()
            assert_matches_type(EntryListResponse, entry, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncOpencode) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            await async_client.session.instructions.entry.with_raw_response.list(
                "",
            )

    @parametrize
    async def test_method_put(self, async_client: AsyncOpencode) -> None:
        entry = await async_client.session.instructions.entry.put(
            key="key",
            session_id="sessionID",
            value={},
        )
        assert entry is None

    @parametrize
    async def test_raw_response_put(self, async_client: AsyncOpencode) -> None:
        response = await async_client.session.instructions.entry.with_raw_response.put(
            key="key",
            session_id="sessionID",
            value={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        entry = await response.parse()
        assert entry is None

    @parametrize
    async def test_streaming_response_put(self, async_client: AsyncOpencode) -> None:
        async with async_client.session.instructions.entry.with_streaming_response.put(
            key="key",
            session_id="sessionID",
            value={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            entry = await response.parse()
            assert entry is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_put(self, async_client: AsyncOpencode) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            await async_client.session.instructions.entry.with_raw_response.put(
                key="key",
                session_id="",
                value={},
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `key` but received ''"):
            await async_client.session.instructions.entry.with_raw_response.put(
                key="",
                session_id="sessionID",
                value={},
            )

    @parametrize
    async def test_method_remove(self, async_client: AsyncOpencode) -> None:
        entry = await async_client.session.instructions.entry.remove(
            key="key",
            session_id="sessionID",
        )
        assert entry is None

    @parametrize
    async def test_raw_response_remove(self, async_client: AsyncOpencode) -> None:
        response = await async_client.session.instructions.entry.with_raw_response.remove(
            key="key",
            session_id="sessionID",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        entry = await response.parse()
        assert entry is None

    @parametrize
    async def test_streaming_response_remove(self, async_client: AsyncOpencode) -> None:
        async with async_client.session.instructions.entry.with_streaming_response.remove(
            key="key",
            session_id="sessionID",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            entry = await response.parse()
            assert entry is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_remove(self, async_client: AsyncOpencode) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            await async_client.session.instructions.entry.with_raw_response.remove(
                key="key",
                session_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `key` but received ''"):
            await async_client.session.instructions.entry.with_raw_response.remove(
                key="",
                session_id="sessionID",
            )
