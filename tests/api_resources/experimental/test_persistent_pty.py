# File generated from our OpenAPI spec by Ferrule. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from opencode import Opencode, AsyncOpencode
from tests.utils import assert_matches_type
from opencode.types.shared import (
    PersistentPtyInfo,
    PersistentPtySnapshot,
    PtyTicketConnectToken,
)
from opencode.types.experimental import (
    PersistentPtyListResponse,
    PersistentPtyReadResponse,
    PersistentPtyHandoffResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPersistentPty:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Opencode) -> None:
        persistent_pty = client.experimental.persistent_pty.create(
            session_id="sessionID",
            args=["string"],
            env={"foo": "string"},
            title="title",
        )
        assert_matches_type(PersistentPtyInfo, persistent_pty, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Opencode) -> None:
        persistent_pty = client.experimental.persistent_pty.create(
            session_id="sessionID",
            args=["string"],
            env={"foo": "string"},
            title="title",
            command="command",
            cwd="cwd",
            size={
                "cols": 0,
                "rows": 0,
            },
        )
        assert_matches_type(PersistentPtyInfo, persistent_pty, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Opencode) -> None:
        response = client.experimental.persistent_pty.with_raw_response.create(
            session_id="sessionID",
            args=["string"],
            env={"foo": "string"},
            title="title",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        persistent_pty = response.parse()
        assert_matches_type(PersistentPtyInfo, persistent_pty, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Opencode) -> None:
        with client.experimental.persistent_pty.with_streaming_response.create(
            session_id="sessionID",
            args=["string"],
            env={"foo": "string"},
            title="title",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            persistent_pty = response.parse()
            assert_matches_type(PersistentPtyInfo, persistent_pty, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: Opencode) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            client.experimental.persistent_pty.with_raw_response.create(
                session_id="",
                args=["string"],
                env={"foo": "string"},
                title="title",
            )

    @parametrize
    def test_method_update(self, client: Opencode) -> None:
        persistent_pty = client.experimental.persistent_pty.update(
            pty_id="ptyID",
            size={
                "cols": 0,
                "rows": 0,
            },
        )
        assert_matches_type(PersistentPtyInfo, persistent_pty, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Opencode) -> None:
        persistent_pty = client.experimental.persistent_pty.update(
            pty_id="ptyID",
            size={
                "cols": 0,
                "rows": 0,
            },
            attachment_id="attachmentID",
        )
        assert_matches_type(PersistentPtyInfo, persistent_pty, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Opencode) -> None:
        response = client.experimental.persistent_pty.with_raw_response.update(
            pty_id="ptyID",
            size={
                "cols": 0,
                "rows": 0,
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        persistent_pty = response.parse()
        assert_matches_type(PersistentPtyInfo, persistent_pty, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Opencode) -> None:
        with client.experimental.persistent_pty.with_streaming_response.update(
            pty_id="ptyID",
            size={
                "cols": 0,
                "rows": 0,
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            persistent_pty = response.parse()
            assert_matches_type(PersistentPtyInfo, persistent_pty, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Opencode) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `pty_id` but received ''"):
            client.experimental.persistent_pty.with_raw_response.update(
                pty_id="",
                size={
                    "cols": 0,
                    "rows": 0,
                },
            )

    @parametrize
    def test_method_list(self, client: Opencode) -> None:
        persistent_pty = client.experimental.persistent_pty.list(
            "sessionID",
        )
        assert_matches_type(PersistentPtyListResponse, persistent_pty, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Opencode) -> None:
        response = client.experimental.persistent_pty.with_raw_response.list(
            "sessionID",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        persistent_pty = response.parse()
        assert_matches_type(PersistentPtyListResponse, persistent_pty, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Opencode) -> None:
        with client.experimental.persistent_pty.with_streaming_response.list(
            "sessionID",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            persistent_pty = response.parse()
            assert_matches_type(PersistentPtyListResponse, persistent_pty, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Opencode) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            client.experimental.persistent_pty.with_raw_response.list(
                "",
            )

    @parametrize
    def test_method_connect_token(self, client: Opencode) -> None:
        persistent_pty = client.experimental.persistent_pty.connect_token(
            pty_id="ptyID",
        )
        assert_matches_type(PtyTicketConnectToken, persistent_pty, path=["response"])

    @parametrize
    def test_method_connect_token_with_all_params(self, client: Opencode) -> None:
        persistent_pty = client.experimental.persistent_pty.connect_token(
            pty_id="ptyID",
            x_opencode_ticket="x-opencode-ticket",
        )
        assert_matches_type(PtyTicketConnectToken, persistent_pty, path=["response"])

    @parametrize
    def test_raw_response_connect_token(self, client: Opencode) -> None:
        response = client.experimental.persistent_pty.with_raw_response.connect_token(
            pty_id="ptyID",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        persistent_pty = response.parse()
        assert_matches_type(PtyTicketConnectToken, persistent_pty, path=["response"])

    @parametrize
    def test_streaming_response_connect_token(self, client: Opencode) -> None:
        with client.experimental.persistent_pty.with_streaming_response.connect_token(
            pty_id="ptyID",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            persistent_pty = response.parse()
            assert_matches_type(PtyTicketConnectToken, persistent_pty, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_connect_token(self, client: Opencode) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `pty_id` but received ''"):
            client.experimental.persistent_pty.with_raw_response.connect_token(
                pty_id="",
            )

    @parametrize
    def test_method_get(self, client: Opencode) -> None:
        persistent_pty = client.experimental.persistent_pty.get(
            "ptyID",
        )
        assert_matches_type(PersistentPtyInfo, persistent_pty, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Opencode) -> None:
        response = client.experimental.persistent_pty.with_raw_response.get(
            "ptyID",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        persistent_pty = response.parse()
        assert_matches_type(PersistentPtyInfo, persistent_pty, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Opencode) -> None:
        with client.experimental.persistent_pty.with_streaming_response.get(
            "ptyID",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            persistent_pty = response.parse()
            assert_matches_type(PersistentPtyInfo, persistent_pty, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Opencode) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `pty_id` but received ''"):
            client.experimental.persistent_pty.with_raw_response.get(
                "",
            )

    @parametrize
    def test_method_handoff(self, client: Opencode) -> None:
        persistent_pty = client.experimental.persistent_pty.handoff()
        assert_matches_type(PersistentPtyHandoffResponse, persistent_pty, path=["response"])

    @parametrize
    def test_raw_response_handoff(self, client: Opencode) -> None:
        response = client.experimental.persistent_pty.with_raw_response.handoff()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        persistent_pty = response.parse()
        assert_matches_type(PersistentPtyHandoffResponse, persistent_pty, path=["response"])

    @parametrize
    def test_streaming_response_handoff(self, client: Opencode) -> None:
        with client.experimental.persistent_pty.with_streaming_response.handoff() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            persistent_pty = response.parse()
            assert_matches_type(PersistentPtyHandoffResponse, persistent_pty, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_read(self, client: Opencode) -> None:
        persistent_pty = client.experimental.persistent_pty.read(
            session_id="sessionID",
        )
        assert_matches_type(PersistentPtyReadResponse, persistent_pty, path=["response"])

    @parametrize
    def test_method_read_with_all_params(self, client: Opencode) -> None:
        persistent_pty = client.experimental.persistent_pty.read(
            session_id="sessionID",
            lines=0,
        )
        assert_matches_type(PersistentPtyReadResponse, persistent_pty, path=["response"])

    @parametrize
    def test_raw_response_read(self, client: Opencode) -> None:
        response = client.experimental.persistent_pty.with_raw_response.read(
            session_id="sessionID",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        persistent_pty = response.parse()
        assert_matches_type(PersistentPtyReadResponse, persistent_pty, path=["response"])

    @parametrize
    def test_streaming_response_read(self, client: Opencode) -> None:
        with client.experimental.persistent_pty.with_streaming_response.read(
            session_id="sessionID",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            persistent_pty = response.parse()
            assert_matches_type(PersistentPtyReadResponse, persistent_pty, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_read(self, client: Opencode) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            client.experimental.persistent_pty.with_raw_response.read(
                session_id="",
            )

    @parametrize
    def test_method_remove(self, client: Opencode) -> None:
        persistent_pty = client.experimental.persistent_pty.remove(
            "ptyID",
        )
        assert persistent_pty is None

    @parametrize
    def test_raw_response_remove(self, client: Opencode) -> None:
        response = client.experimental.persistent_pty.with_raw_response.remove(
            "ptyID",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        persistent_pty = response.parse()
        assert persistent_pty is None

    @parametrize
    def test_streaming_response_remove(self, client: Opencode) -> None:
        with client.experimental.persistent_pty.with_streaming_response.remove(
            "ptyID",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            persistent_pty = response.parse()
            assert persistent_pty is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_remove(self, client: Opencode) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `pty_id` but received ''"):
            client.experimental.persistent_pty.with_raw_response.remove(
                "",
            )

    @parametrize
    def test_method_shutdown(self, client: Opencode) -> None:
        persistent_pty = client.experimental.persistent_pty.shutdown()
        assert persistent_pty is None

    @parametrize
    def test_raw_response_shutdown(self, client: Opencode) -> None:
        response = client.experimental.persistent_pty.with_raw_response.shutdown()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        persistent_pty = response.parse()
        assert persistent_pty is None

    @parametrize
    def test_streaming_response_shutdown(self, client: Opencode) -> None:
        with client.experimental.persistent_pty.with_streaming_response.shutdown() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            persistent_pty = response.parse()
            assert persistent_pty is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_snapshot(self, client: Opencode) -> None:
        persistent_pty = client.experimental.persistent_pty.snapshot(
            "ptyID",
        )
        assert_matches_type(PersistentPtySnapshot, persistent_pty, path=["response"])

    @parametrize
    def test_raw_response_snapshot(self, client: Opencode) -> None:
        response = client.experimental.persistent_pty.with_raw_response.snapshot(
            "ptyID",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        persistent_pty = response.parse()
        assert_matches_type(PersistentPtySnapshot, persistent_pty, path=["response"])

    @parametrize
    def test_streaming_response_snapshot(self, client: Opencode) -> None:
        with client.experimental.persistent_pty.with_streaming_response.snapshot(
            "ptyID",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            persistent_pty = response.parse()
            assert_matches_type(PersistentPtySnapshot, persistent_pty, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_snapshot(self, client: Opencode) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `pty_id` but received ''"):
            client.experimental.persistent_pty.with_raw_response.snapshot(
                "",
            )


class TestAsyncPersistentPty:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncOpencode) -> None:
        persistent_pty = await async_client.experimental.persistent_pty.create(
            session_id="sessionID",
            args=["string"],
            env={"foo": "string"},
            title="title",
        )
        assert_matches_type(PersistentPtyInfo, persistent_pty, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncOpencode) -> None:
        persistent_pty = await async_client.experimental.persistent_pty.create(
            session_id="sessionID",
            args=["string"],
            env={"foo": "string"},
            title="title",
            command="command",
            cwd="cwd",
            size={
                "cols": 0,
                "rows": 0,
            },
        )
        assert_matches_type(PersistentPtyInfo, persistent_pty, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncOpencode) -> None:
        response = await async_client.experimental.persistent_pty.with_raw_response.create(
            session_id="sessionID",
            args=["string"],
            env={"foo": "string"},
            title="title",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        persistent_pty = await response.parse()
        assert_matches_type(PersistentPtyInfo, persistent_pty, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncOpencode) -> None:
        async with async_client.experimental.persistent_pty.with_streaming_response.create(
            session_id="sessionID",
            args=["string"],
            env={"foo": "string"},
            title="title",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            persistent_pty = await response.parse()
            assert_matches_type(PersistentPtyInfo, persistent_pty, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncOpencode) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            await async_client.experimental.persistent_pty.with_raw_response.create(
                session_id="",
                args=["string"],
                env={"foo": "string"},
                title="title",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncOpencode) -> None:
        persistent_pty = await async_client.experimental.persistent_pty.update(
            pty_id="ptyID",
            size={
                "cols": 0,
                "rows": 0,
            },
        )
        assert_matches_type(PersistentPtyInfo, persistent_pty, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncOpencode) -> None:
        persistent_pty = await async_client.experimental.persistent_pty.update(
            pty_id="ptyID",
            size={
                "cols": 0,
                "rows": 0,
            },
            attachment_id="attachmentID",
        )
        assert_matches_type(PersistentPtyInfo, persistent_pty, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncOpencode) -> None:
        response = await async_client.experimental.persistent_pty.with_raw_response.update(
            pty_id="ptyID",
            size={
                "cols": 0,
                "rows": 0,
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        persistent_pty = await response.parse()
        assert_matches_type(PersistentPtyInfo, persistent_pty, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncOpencode) -> None:
        async with async_client.experimental.persistent_pty.with_streaming_response.update(
            pty_id="ptyID",
            size={
                "cols": 0,
                "rows": 0,
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            persistent_pty = await response.parse()
            assert_matches_type(PersistentPtyInfo, persistent_pty, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncOpencode) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `pty_id` but received ''"):
            await async_client.experimental.persistent_pty.with_raw_response.update(
                pty_id="",
                size={
                    "cols": 0,
                    "rows": 0,
                },
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncOpencode) -> None:
        persistent_pty = await async_client.experimental.persistent_pty.list(
            "sessionID",
        )
        assert_matches_type(PersistentPtyListResponse, persistent_pty, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncOpencode) -> None:
        response = await async_client.experimental.persistent_pty.with_raw_response.list(
            "sessionID",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        persistent_pty = await response.parse()
        assert_matches_type(PersistentPtyListResponse, persistent_pty, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncOpencode) -> None:
        async with async_client.experimental.persistent_pty.with_streaming_response.list(
            "sessionID",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            persistent_pty = await response.parse()
            assert_matches_type(PersistentPtyListResponse, persistent_pty, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncOpencode) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            await async_client.experimental.persistent_pty.with_raw_response.list(
                "",
            )

    @parametrize
    async def test_method_connect_token(self, async_client: AsyncOpencode) -> None:
        persistent_pty = await async_client.experimental.persistent_pty.connect_token(
            pty_id="ptyID",
        )
        assert_matches_type(PtyTicketConnectToken, persistent_pty, path=["response"])

    @parametrize
    async def test_method_connect_token_with_all_params(self, async_client: AsyncOpencode) -> None:
        persistent_pty = await async_client.experimental.persistent_pty.connect_token(
            pty_id="ptyID",
            x_opencode_ticket="x-opencode-ticket",
        )
        assert_matches_type(PtyTicketConnectToken, persistent_pty, path=["response"])

    @parametrize
    async def test_raw_response_connect_token(self, async_client: AsyncOpencode) -> None:
        response = await async_client.experimental.persistent_pty.with_raw_response.connect_token(
            pty_id="ptyID",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        persistent_pty = await response.parse()
        assert_matches_type(PtyTicketConnectToken, persistent_pty, path=["response"])

    @parametrize
    async def test_streaming_response_connect_token(self, async_client: AsyncOpencode) -> None:
        async with async_client.experimental.persistent_pty.with_streaming_response.connect_token(
            pty_id="ptyID",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            persistent_pty = await response.parse()
            assert_matches_type(PtyTicketConnectToken, persistent_pty, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_connect_token(self, async_client: AsyncOpencode) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `pty_id` but received ''"):
            await async_client.experimental.persistent_pty.with_raw_response.connect_token(
                pty_id="",
            )

    @parametrize
    async def test_method_get(self, async_client: AsyncOpencode) -> None:
        persistent_pty = await async_client.experimental.persistent_pty.get(
            "ptyID",
        )
        assert_matches_type(PersistentPtyInfo, persistent_pty, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncOpencode) -> None:
        response = await async_client.experimental.persistent_pty.with_raw_response.get(
            "ptyID",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        persistent_pty = await response.parse()
        assert_matches_type(PersistentPtyInfo, persistent_pty, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncOpencode) -> None:
        async with async_client.experimental.persistent_pty.with_streaming_response.get(
            "ptyID",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            persistent_pty = await response.parse()
            assert_matches_type(PersistentPtyInfo, persistent_pty, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncOpencode) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `pty_id` but received ''"):
            await async_client.experimental.persistent_pty.with_raw_response.get(
                "",
            )

    @parametrize
    async def test_method_handoff(self, async_client: AsyncOpencode) -> None:
        persistent_pty = await async_client.experimental.persistent_pty.handoff()
        assert_matches_type(PersistentPtyHandoffResponse, persistent_pty, path=["response"])

    @parametrize
    async def test_raw_response_handoff(self, async_client: AsyncOpencode) -> None:
        response = await async_client.experimental.persistent_pty.with_raw_response.handoff()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        persistent_pty = await response.parse()
        assert_matches_type(PersistentPtyHandoffResponse, persistent_pty, path=["response"])

    @parametrize
    async def test_streaming_response_handoff(self, async_client: AsyncOpencode) -> None:
        async with async_client.experimental.persistent_pty.with_streaming_response.handoff() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            persistent_pty = await response.parse()
            assert_matches_type(PersistentPtyHandoffResponse, persistent_pty, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_read(self, async_client: AsyncOpencode) -> None:
        persistent_pty = await async_client.experimental.persistent_pty.read(
            session_id="sessionID",
        )
        assert_matches_type(PersistentPtyReadResponse, persistent_pty, path=["response"])

    @parametrize
    async def test_method_read_with_all_params(self, async_client: AsyncOpencode) -> None:
        persistent_pty = await async_client.experimental.persistent_pty.read(
            session_id="sessionID",
            lines=0,
        )
        assert_matches_type(PersistentPtyReadResponse, persistent_pty, path=["response"])

    @parametrize
    async def test_raw_response_read(self, async_client: AsyncOpencode) -> None:
        response = await async_client.experimental.persistent_pty.with_raw_response.read(
            session_id="sessionID",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        persistent_pty = await response.parse()
        assert_matches_type(PersistentPtyReadResponse, persistent_pty, path=["response"])

    @parametrize
    async def test_streaming_response_read(self, async_client: AsyncOpencode) -> None:
        async with async_client.experimental.persistent_pty.with_streaming_response.read(
            session_id="sessionID",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            persistent_pty = await response.parse()
            assert_matches_type(PersistentPtyReadResponse, persistent_pty, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_read(self, async_client: AsyncOpencode) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            await async_client.experimental.persistent_pty.with_raw_response.read(
                session_id="",
            )

    @parametrize
    async def test_method_remove(self, async_client: AsyncOpencode) -> None:
        persistent_pty = await async_client.experimental.persistent_pty.remove(
            "ptyID",
        )
        assert persistent_pty is None

    @parametrize
    async def test_raw_response_remove(self, async_client: AsyncOpencode) -> None:
        response = await async_client.experimental.persistent_pty.with_raw_response.remove(
            "ptyID",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        persistent_pty = await response.parse()
        assert persistent_pty is None

    @parametrize
    async def test_streaming_response_remove(self, async_client: AsyncOpencode) -> None:
        async with async_client.experimental.persistent_pty.with_streaming_response.remove(
            "ptyID",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            persistent_pty = await response.parse()
            assert persistent_pty is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_remove(self, async_client: AsyncOpencode) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `pty_id` but received ''"):
            await async_client.experimental.persistent_pty.with_raw_response.remove(
                "",
            )

    @parametrize
    async def test_method_shutdown(self, async_client: AsyncOpencode) -> None:
        persistent_pty = await async_client.experimental.persistent_pty.shutdown()
        assert persistent_pty is None

    @parametrize
    async def test_raw_response_shutdown(self, async_client: AsyncOpencode) -> None:
        response = await async_client.experimental.persistent_pty.with_raw_response.shutdown()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        persistent_pty = await response.parse()
        assert persistent_pty is None

    @parametrize
    async def test_streaming_response_shutdown(self, async_client: AsyncOpencode) -> None:
        async with async_client.experimental.persistent_pty.with_streaming_response.shutdown() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            persistent_pty = await response.parse()
            assert persistent_pty is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_snapshot(self, async_client: AsyncOpencode) -> None:
        persistent_pty = await async_client.experimental.persistent_pty.snapshot(
            "ptyID",
        )
        assert_matches_type(PersistentPtySnapshot, persistent_pty, path=["response"])

    @parametrize
    async def test_raw_response_snapshot(self, async_client: AsyncOpencode) -> None:
        response = await async_client.experimental.persistent_pty.with_raw_response.snapshot(
            "ptyID",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        persistent_pty = await response.parse()
        assert_matches_type(PersistentPtySnapshot, persistent_pty, path=["response"])

    @parametrize
    async def test_streaming_response_snapshot(self, async_client: AsyncOpencode) -> None:
        async with async_client.experimental.persistent_pty.with_streaming_response.snapshot(
            "ptyID",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            persistent_pty = await response.parse()
            assert_matches_type(PersistentPtySnapshot, persistent_pty, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_snapshot(self, async_client: AsyncOpencode) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `pty_id` but received ''"):
            await async_client.experimental.persistent_pty.with_raw_response.snapshot(
                "",
            )
