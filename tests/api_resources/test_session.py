# File generated from our OpenAPI spec by Ferrule. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from opencode import Opencode, AsyncOpencode
from tests.utils import assert_matches_type
from opencode.types import (
    SessionDiffResponse,
    SessionActiveResponse,
    SessionContextResponse,
    SessionGenerateResponse,
)
from opencode.pagination import SyncCursorPage, AsyncCursorPage
from opencode.types.shared import (
    SessionInfo,
    SessionInboxUser,
    SessionStatsInfo,
    SessionTransferData,
    SessionInboxSynthetic,
    SessionInboxCompaction,
    SessionInterruptResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSession:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Opencode) -> None:
        session = client.session.create()
        assert_matches_type(SessionInfo, session, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Opencode) -> None:
        session = client.session.create(
            agent="agent",
            id="id",
            location={
                "directory": "string",
            },
            metadata={"foo": {}},
            model={
                "id": "string",
                "provider_id": "string",
                "variant": "string",
            },
            parent_id="parentID",
            permissions=[
                {
                    "action": "string",
                    "effect": "allow",
                    "resource": "string",
                }
            ],
            title="title",
        )
        assert_matches_type(SessionInfo, session, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Opencode) -> None:
        response = client.session.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = response.parse()
        assert_matches_type(SessionInfo, session, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Opencode) -> None:
        with client.session.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = response.parse()
            assert_matches_type(SessionInfo, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_update(self, client: Opencode) -> None:
        session = client.session.update(
            session_id="sessionID",
        )
        assert session is None

    @parametrize
    def test_method_update_with_all_params(self, client: Opencode) -> None:
        session = client.session.update(
            session_id="sessionID",
            archived=True,
            metadata={"foo": {}},
            permissions=[
                {
                    "action": "string",
                    "effect": "allow",
                    "resource": "string",
                }
            ],
            title="title",
        )
        assert session is None

    @parametrize
    def test_raw_response_update(self, client: Opencode) -> None:
        response = client.session.with_raw_response.update(
            session_id="sessionID",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = response.parse()
        assert session is None

    @parametrize
    def test_streaming_response_update(self, client: Opencode) -> None:
        with client.session.with_streaming_response.update(
            session_id="sessionID",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = response.parse()
            assert session is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Opencode) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            client.session.with_raw_response.update(
                session_id="",
            )

    @parametrize
    def test_method_list(self, client: Opencode) -> None:
        session = client.session.list()
        assert_matches_type(SyncCursorPage[SessionInfo], session, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Opencode) -> None:
        session = client.session.list(
            archived=True,
            cursor="cursor",
            directory="directory",
            limit=0,
            order="asc",
            parent_id="parentID",
            project="project",
            search="search",
            subpath="subpath",
        )
        assert_matches_type(SyncCursorPage[SessionInfo], session, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Opencode) -> None:
        response = client.session.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = response.parse()
        assert_matches_type(SyncCursorPage[SessionInfo], session, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Opencode) -> None:
        with client.session.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = response.parse()
            assert_matches_type(SyncCursorPage[SessionInfo], session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_active(self, client: Opencode) -> None:
        session = client.session.active()
        assert_matches_type(SessionActiveResponse, session, path=["response"])

    @parametrize
    def test_raw_response_active(self, client: Opencode) -> None:
        response = client.session.with_raw_response.active()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = response.parse()
        assert_matches_type(SessionActiveResponse, session, path=["response"])

    @parametrize
    def test_streaming_response_active(self, client: Opencode) -> None:
        with client.session.with_streaming_response.active() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = response.parse()
            assert_matches_type(SessionActiveResponse, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_background(self, client: Opencode) -> None:
        session = client.session.background(
            "sessionID",
        )
        assert session is None

    @parametrize
    def test_raw_response_background(self, client: Opencode) -> None:
        response = client.session.with_raw_response.background(
            "sessionID",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = response.parse()
        assert session is None

    @parametrize
    def test_streaming_response_background(self, client: Opencode) -> None:
        with client.session.with_streaming_response.background(
            "sessionID",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = response.parse()
            assert session is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_background(self, client: Opencode) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            client.session.with_raw_response.background(
                "",
            )

    @parametrize
    def test_method_command(self, client: Opencode) -> None:
        session = client.session.command(
            session_id="sessionID",
            name="name",
            text="text",
        )
        assert session is None

    @parametrize
    def test_method_command_with_all_params(self, client: Opencode) -> None:
        session = client.session.command(
            session_id="sessionID",
            name="name",
            text="text",
            agents=[
                {
                    "mention": {
                        "end": 0,
                        "start": 0,
                        "text": "string",
                    },
                    "name": "string",
                }
            ],
            delivery="steer",
            files=[
                {
                    "description": "string",
                    "mention": {
                        "end": 0,
                        "start": 0,
                        "text": "string",
                    },
                    "name": "string",
                    "uri": "string",
                }
            ],
            skills=[
                {
                    "id": "string",
                    "mention": {
                        "end": 0,
                        "start": 0,
                        "text": "string",
                    },
                }
            ],
        )
        assert session is None

    @parametrize
    def test_raw_response_command(self, client: Opencode) -> None:
        response = client.session.with_raw_response.command(
            session_id="sessionID",
            name="name",
            text="text",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = response.parse()
        assert session is None

    @parametrize
    def test_streaming_response_command(self, client: Opencode) -> None:
        with client.session.with_streaming_response.command(
            session_id="sessionID",
            name="name",
            text="text",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = response.parse()
            assert session is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_command(self, client: Opencode) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            client.session.with_raw_response.command(
                session_id="",
                name="name",
                text="text",
            )

    @parametrize
    def test_method_compact(self, client: Opencode) -> None:
        session = client.session.compact(
            session_id="sessionID",
        )
        assert_matches_type(SessionInboxCompaction, session, path=["response"])

    @parametrize
    def test_method_compact_with_all_params(self, client: Opencode) -> None:
        session = client.session.compact(
            session_id="sessionID",
            delivery="steer",
            id="id",
        )
        assert_matches_type(SessionInboxCompaction, session, path=["response"])

    @parametrize
    def test_raw_response_compact(self, client: Opencode) -> None:
        response = client.session.with_raw_response.compact(
            session_id="sessionID",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = response.parse()
        assert_matches_type(SessionInboxCompaction, session, path=["response"])

    @parametrize
    def test_streaming_response_compact(self, client: Opencode) -> None:
        with client.session.with_streaming_response.compact(
            session_id="sessionID",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = response.parse()
            assert_matches_type(SessionInboxCompaction, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_compact(self, client: Opencode) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            client.session.with_raw_response.compact(
                session_id="",
            )

    @parametrize
    def test_method_context(self, client: Opencode) -> None:
        session = client.session.context(
            "sessionID",
        )
        assert_matches_type(SessionContextResponse, session, path=["response"])

    @parametrize
    def test_raw_response_context(self, client: Opencode) -> None:
        response = client.session.with_raw_response.context(
            "sessionID",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = response.parse()
        assert_matches_type(SessionContextResponse, session, path=["response"])

    @parametrize
    def test_streaming_response_context(self, client: Opencode) -> None:
        with client.session.with_streaming_response.context(
            "sessionID",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = response.parse()
            assert_matches_type(SessionContextResponse, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_context(self, client: Opencode) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            client.session.with_raw_response.context(
                "",
            )

    @parametrize
    def test_method_diff(self, client: Opencode) -> None:
        session = client.session.diff(
            session_id="sessionID",
        )
        assert_matches_type(SessionDiffResponse, session, path=["response"])

    @parametrize
    def test_method_diff_with_all_params(self, client: Opencode) -> None:
        session = client.session.diff(
            session_id="sessionID",
            context=0,
            from_="from",
            to="to",
        )
        assert_matches_type(SessionDiffResponse, session, path=["response"])

    @parametrize
    def test_raw_response_diff(self, client: Opencode) -> None:
        response = client.session.with_raw_response.diff(
            session_id="sessionID",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = response.parse()
        assert_matches_type(SessionDiffResponse, session, path=["response"])

    @parametrize
    def test_streaming_response_diff(self, client: Opencode) -> None:
        with client.session.with_streaming_response.diff(
            session_id="sessionID",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = response.parse()
            assert_matches_type(SessionDiffResponse, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_diff(self, client: Opencode) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            client.session.with_raw_response.diff(
                session_id="",
            )

    @parametrize
    def test_method_environment(self, client: Opencode) -> None:
        session = client.session.environment(
            session_id="sessionID",
            variables={"foo": "string"},
        )
        assert session is None

    @parametrize
    def test_raw_response_environment(self, client: Opencode) -> None:
        response = client.session.with_raw_response.environment(
            session_id="sessionID",
            variables={"foo": "string"},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = response.parse()
        assert session is None

    @parametrize
    def test_streaming_response_environment(self, client: Opencode) -> None:
        with client.session.with_streaming_response.environment(
            session_id="sessionID",
            variables={"foo": "string"},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = response.parse()
            assert session is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_environment(self, client: Opencode) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            client.session.with_raw_response.environment(
                session_id="",
                variables={"foo": "string"},
            )

    @parametrize
    def test_method_export(self, client: Opencode) -> None:
        session = client.session.export(
            session_id="sessionID",
        )
        assert_matches_type(SessionTransferData, session, path=["response"])

    @parametrize
    def test_method_export_with_all_params(self, client: Opencode) -> None:
        session = client.session.export(
            session_id="sessionID",
            sanitize=True,
        )
        assert_matches_type(SessionTransferData, session, path=["response"])

    @parametrize
    def test_raw_response_export(self, client: Opencode) -> None:
        response = client.session.with_raw_response.export(
            session_id="sessionID",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = response.parse()
        assert_matches_type(SessionTransferData, session, path=["response"])

    @parametrize
    def test_streaming_response_export(self, client: Opencode) -> None:
        with client.session.with_streaming_response.export(
            session_id="sessionID",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = response.parse()
            assert_matches_type(SessionTransferData, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_export(self, client: Opencode) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            client.session.with_raw_response.export(
                session_id="",
            )

    @parametrize
    def test_method_fork(self, client: Opencode) -> None:
        session = client.session.fork(
            session_id="sessionID",
        )
        assert_matches_type(SessionInfo, session, path=["response"])

    @parametrize
    def test_method_fork_with_all_params(self, client: Opencode) -> None:
        session = client.session.fork(
            session_id="sessionID",
            before="before",
        )
        assert_matches_type(SessionInfo, session, path=["response"])

    @parametrize
    def test_raw_response_fork(self, client: Opencode) -> None:
        response = client.session.with_raw_response.fork(
            session_id="sessionID",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = response.parse()
        assert_matches_type(SessionInfo, session, path=["response"])

    @parametrize
    def test_streaming_response_fork(self, client: Opencode) -> None:
        with client.session.with_streaming_response.fork(
            session_id="sessionID",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = response.parse()
            assert_matches_type(SessionInfo, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_fork(self, client: Opencode) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            client.session.with_raw_response.fork(
                session_id="",
            )

    @parametrize
    def test_method_generate(self, client: Opencode) -> None:
        session = client.session.generate(
            session_id="sessionID",
            prompt="prompt",
        )
        assert_matches_type(SessionGenerateResponse, session, path=["response"])

    @parametrize
    def test_raw_response_generate(self, client: Opencode) -> None:
        response = client.session.with_raw_response.generate(
            session_id="sessionID",
            prompt="prompt",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = response.parse()
        assert_matches_type(SessionGenerateResponse, session, path=["response"])

    @parametrize
    def test_streaming_response_generate(self, client: Opencode) -> None:
        with client.session.with_streaming_response.generate(
            session_id="sessionID",
            prompt="prompt",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = response.parse()
            assert_matches_type(SessionGenerateResponse, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_generate(self, client: Opencode) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            client.session.with_raw_response.generate(
                session_id="",
                prompt="prompt",
            )

    @parametrize
    def test_method_get(self, client: Opencode) -> None:
        session = client.session.get(
            "sessionID",
        )
        assert_matches_type(SessionInfo, session, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Opencode) -> None:
        response = client.session.with_raw_response.get(
            "sessionID",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = response.parse()
        assert_matches_type(SessionInfo, session, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Opencode) -> None:
        with client.session.with_streaming_response.get(
            "sessionID",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = response.parse()
            assert_matches_type(SessionInfo, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Opencode) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            client.session.with_raw_response.get(
                "",
            )

    @parametrize
    def test_method_import_(self, client: Opencode) -> None:
        session = client.session.import_(
            info={
                "agent": "string",
                "cost": 0,
                "fork": {
                    "boundary": {
                        "message_id": "string",
                        "type": "before",
                    },
                    "session_id": "string",
                },
                "id": "string",
                "location": {
                    "directory": "string",
                },
                "metadata": {"foo": {}},
                "model": {
                    "id": "string",
                    "provider_id": "string",
                    "variant": "string",
                },
                "outcome": "succeeded",
                "parent_id": "string",
                "permissions": [
                    {
                        "action": "string",
                        "effect": "allow",
                        "resource": "string",
                    }
                ],
                "project_id": "string",
                "revert": {
                    "files": [
                        {
                            "additions": 0,
                            "deletions": 0,
                            "file": "string",
                            "patch": "string",
                            "status": "added",
                        }
                    ],
                    "message_id": "string",
                    "part_id": "string",
                    "snapshot": "string",
                },
                "subpath": "string",
                "time": {
                    "archived": 0,
                    "created": 0,
                    "idle": 0,
                    "updated": 0,
                    "viewed": 0,
                },
                "title": "string",
                "tokens": {
                    "cache": {
                        "read": 0,
                        "write": 0,
                    },
                    "input": 0,
                    "output": 0,
                    "reasoning": 0,
                },
            },
            messages=[{}],
        )
        assert_matches_type(SessionInfo, session, path=["response"])

    @parametrize
    def test_method_import__with_all_params(self, client: Opencode) -> None:
        session = client.session.import_(
            info={
                "agent": "string",
                "cost": 0,
                "fork": {
                    "boundary": {
                        "message_id": "string",
                        "type": "before",
                    },
                    "session_id": "string",
                },
                "id": "string",
                "location": {
                    "directory": "string",
                },
                "metadata": {"foo": {}},
                "model": {
                    "id": "string",
                    "provider_id": "string",
                    "variant": "string",
                },
                "outcome": "succeeded",
                "parent_id": "string",
                "permissions": [
                    {
                        "action": "string",
                        "effect": "allow",
                        "resource": "string",
                    }
                ],
                "project_id": "string",
                "revert": {
                    "files": [
                        {
                            "additions": 0,
                            "deletions": 0,
                            "file": "string",
                            "patch": "string",
                            "status": "added",
                        }
                    ],
                    "message_id": "string",
                    "part_id": "string",
                    "snapshot": "string",
                },
                "subpath": "string",
                "time": {
                    "archived": 0,
                    "created": 0,
                    "idle": 0,
                    "updated": 0,
                    "viewed": 0,
                },
                "title": "string",
                "tokens": {
                    "cache": {
                        "read": 0,
                        "write": 0,
                    },
                    "input": 0,
                    "output": 0,
                    "reasoning": 0,
                },
            },
            messages=[{}],
            location={
                "directory": "string",
            },
        )
        assert_matches_type(SessionInfo, session, path=["response"])

    @parametrize
    def test_raw_response_import_(self, client: Opencode) -> None:
        response = client.session.with_raw_response.import_(
            info={
                "agent": "string",
                "cost": 0,
                "fork": {
                    "boundary": {
                        "message_id": "string",
                        "type": "before",
                    },
                    "session_id": "string",
                },
                "id": "string",
                "location": {
                    "directory": "string",
                },
                "metadata": {"foo": {}},
                "model": {
                    "id": "string",
                    "provider_id": "string",
                    "variant": "string",
                },
                "outcome": "succeeded",
                "parent_id": "string",
                "permissions": [
                    {
                        "action": "string",
                        "effect": "allow",
                        "resource": "string",
                    }
                ],
                "project_id": "string",
                "revert": {
                    "files": [
                        {
                            "additions": 0,
                            "deletions": 0,
                            "file": "string",
                            "patch": "string",
                            "status": "added",
                        }
                    ],
                    "message_id": "string",
                    "part_id": "string",
                    "snapshot": "string",
                },
                "subpath": "string",
                "time": {
                    "archived": 0,
                    "created": 0,
                    "idle": 0,
                    "updated": 0,
                    "viewed": 0,
                },
                "title": "string",
                "tokens": {
                    "cache": {
                        "read": 0,
                        "write": 0,
                    },
                    "input": 0,
                    "output": 0,
                    "reasoning": 0,
                },
            },
            messages=[{}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = response.parse()
        assert_matches_type(SessionInfo, session, path=["response"])

    @parametrize
    def test_streaming_response_import_(self, client: Opencode) -> None:
        with client.session.with_streaming_response.import_(
            info={
                "agent": "string",
                "cost": 0,
                "fork": {
                    "boundary": {
                        "message_id": "string",
                        "type": "before",
                    },
                    "session_id": "string",
                },
                "id": "string",
                "location": {
                    "directory": "string",
                },
                "metadata": {"foo": {}},
                "model": {
                    "id": "string",
                    "provider_id": "string",
                    "variant": "string",
                },
                "outcome": "succeeded",
                "parent_id": "string",
                "permissions": [
                    {
                        "action": "string",
                        "effect": "allow",
                        "resource": "string",
                    }
                ],
                "project_id": "string",
                "revert": {
                    "files": [
                        {
                            "additions": 0,
                            "deletions": 0,
                            "file": "string",
                            "patch": "string",
                            "status": "added",
                        }
                    ],
                    "message_id": "string",
                    "part_id": "string",
                    "snapshot": "string",
                },
                "subpath": "string",
                "time": {
                    "archived": 0,
                    "created": 0,
                    "idle": 0,
                    "updated": 0,
                    "viewed": 0,
                },
                "title": "string",
                "tokens": {
                    "cache": {
                        "read": 0,
                        "write": 0,
                    },
                    "input": 0,
                    "output": 0,
                    "reasoning": 0,
                },
            },
            messages=[{}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = response.parse()
            assert_matches_type(SessionInfo, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_interrupt(self, client: Opencode) -> None:
        session = client.session.interrupt(
            session_id="sessionID",
        )
        assert_matches_type(SessionInterruptResponse, session, path=["response"])

    @parametrize
    def test_method_interrupt_with_all_params(self, client: Opencode) -> None:
        session = client.session.interrupt(
            session_id="sessionID",
            resume=True,
        )
        assert_matches_type(SessionInterruptResponse, session, path=["response"])

    @parametrize
    def test_raw_response_interrupt(self, client: Opencode) -> None:
        response = client.session.with_raw_response.interrupt(
            session_id="sessionID",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = response.parse()
        assert_matches_type(SessionInterruptResponse, session, path=["response"])

    @parametrize
    def test_streaming_response_interrupt(self, client: Opencode) -> None:
        with client.session.with_streaming_response.interrupt(
            session_id="sessionID",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = response.parse()
            assert_matches_type(SessionInterruptResponse, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_interrupt(self, client: Opencode) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            client.session.with_raw_response.interrupt(
                session_id="",
            )

    @pytest.mark.skip(reason="The mock server rejects integer query parameters typed through a $ref in anyOf.")
    @parametrize
    def test_method_log(self, client: Opencode) -> None:
        session = client.session.log(
            session_id="sessionID",
        )
        assert session is None

    @pytest.mark.skip(reason="The mock server rejects integer query parameters typed through a $ref in anyOf.")
    @parametrize
    def test_method_log_with_all_params(self, client: Opencode) -> None:
        session = client.session.log(
            session_id="sessionID",
            after=0,
            follow=True,
        )
        assert session is None

    @pytest.mark.skip(reason="The mock server rejects integer query parameters typed through a $ref in anyOf.")
    @parametrize
    def test_raw_response_log(self, client: Opencode) -> None:
        response = client.session.with_raw_response.log(
            session_id="sessionID",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = response.parse()
        assert session is None

    @pytest.mark.skip(reason="The mock server rejects integer query parameters typed through a $ref in anyOf.")
    @parametrize
    def test_streaming_response_log(self, client: Opencode) -> None:
        with client.session.with_streaming_response.log(
            session_id="sessionID",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = response.parse()
            assert session is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="The mock server rejects integer query parameters typed through a $ref in anyOf.")
    @parametrize
    def test_path_params_log(self, client: Opencode) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            client.session.with_raw_response.log(
                session_id="",
            )

    @parametrize
    def test_method_move(self, client: Opencode) -> None:
        session = client.session.move(
            session_id="sessionID",
            directory="directory",
        )
        assert session is None

    @parametrize
    def test_method_move_with_all_params(self, client: Opencode) -> None:
        session = client.session.move(
            session_id="sessionID",
            directory="directory",
            delivery="steer",
        )
        assert session is None

    @parametrize
    def test_raw_response_move(self, client: Opencode) -> None:
        response = client.session.with_raw_response.move(
            session_id="sessionID",
            directory="directory",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = response.parse()
        assert session is None

    @parametrize
    def test_streaming_response_move(self, client: Opencode) -> None:
        with client.session.with_streaming_response.move(
            session_id="sessionID",
            directory="directory",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = response.parse()
            assert session is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_move(self, client: Opencode) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            client.session.with_raw_response.move(
                session_id="",
                directory="directory",
            )

    @parametrize
    def test_method_prompt(self, client: Opencode) -> None:
        session = client.session.prompt(
            session_id="sessionID",
            text="text",
        )
        assert_matches_type(SessionInboxUser, session, path=["response"])

    @parametrize
    def test_method_prompt_with_all_params(self, client: Opencode) -> None:
        session = client.session.prompt(
            session_id="sessionID",
            text="text",
            agents=[
                {
                    "mention": {
                        "end": 0,
                        "start": 0,
                        "text": "string",
                    },
                    "name": "string",
                }
            ],
            delivery="steer",
            files=[
                {
                    "description": "string",
                    "mention": {
                        "end": 0,
                        "start": 0,
                        "text": "string",
                    },
                    "name": "string",
                    "uri": "string",
                }
            ],
            id="id",
            metadata={"foo": {}},
            resume=True,
            skills=[
                {
                    "id": "string",
                    "mention": {
                        "end": 0,
                        "start": 0,
                        "text": "string",
                    },
                }
            ],
        )
        assert_matches_type(SessionInboxUser, session, path=["response"])

    @parametrize
    def test_raw_response_prompt(self, client: Opencode) -> None:
        response = client.session.with_raw_response.prompt(
            session_id="sessionID",
            text="text",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = response.parse()
        assert_matches_type(SessionInboxUser, session, path=["response"])

    @parametrize
    def test_streaming_response_prompt(self, client: Opencode) -> None:
        with client.session.with_streaming_response.prompt(
            session_id="sessionID",
            text="text",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = response.parse()
            assert_matches_type(SessionInboxUser, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_prompt(self, client: Opencode) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            client.session.with_raw_response.prompt(
                session_id="",
                text="text",
            )

    @parametrize
    def test_method_remove(self, client: Opencode) -> None:
        session = client.session.remove(
            "sessionID",
        )
        assert session is None

    @parametrize
    def test_raw_response_remove(self, client: Opencode) -> None:
        response = client.session.with_raw_response.remove(
            "sessionID",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = response.parse()
        assert session is None

    @parametrize
    def test_streaming_response_remove(self, client: Opencode) -> None:
        with client.session.with_streaming_response.remove(
            "sessionID",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = response.parse()
            assert session is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_remove(self, client: Opencode) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            client.session.with_raw_response.remove(
                "",
            )

    @parametrize
    def test_method_shell(self, client: Opencode) -> None:
        session = client.session.shell(
            session_id="sessionID",
            command="command",
        )
        assert session is None

    @parametrize
    def test_method_shell_with_all_params(self, client: Opencode) -> None:
        session = client.session.shell(
            session_id="sessionID",
            command="command",
            id="id",
        )
        assert session is None

    @parametrize
    def test_raw_response_shell(self, client: Opencode) -> None:
        response = client.session.with_raw_response.shell(
            session_id="sessionID",
            command="command",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = response.parse()
        assert session is None

    @parametrize
    def test_streaming_response_shell(self, client: Opencode) -> None:
        with client.session.with_streaming_response.shell(
            session_id="sessionID",
            command="command",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = response.parse()
            assert session is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_shell(self, client: Opencode) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            client.session.with_raw_response.shell(
                session_id="",
                command="command",
            )

    @parametrize
    def test_method_skill(self, client: Opencode) -> None:
        session = client.session.skill(
            session_id="sessionID",
            id="id",
        )
        assert session is None

    @parametrize
    def test_method_skill_with_all_params(self, client: Opencode) -> None:
        session = client.session.skill(
            session_id="sessionID",
            id="id",
            resume=True,
        )
        assert session is None

    @parametrize
    def test_raw_response_skill(self, client: Opencode) -> None:
        response = client.session.with_raw_response.skill(
            session_id="sessionID",
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = response.parse()
        assert session is None

    @parametrize
    def test_streaming_response_skill(self, client: Opencode) -> None:
        with client.session.with_streaming_response.skill(
            session_id="sessionID",
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = response.parse()
            assert session is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_skill(self, client: Opencode) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            client.session.with_raw_response.skill(
                session_id="",
                id="id",
            )

    @parametrize
    def test_method_stats(self, client: Opencode) -> None:
        session = client.session.stats()
        assert_matches_type(SessionStatsInfo, session, path=["response"])

    @parametrize
    def test_method_stats_with_all_params(self, client: Opencode) -> None:
        session = client.session.stats(
            from_=0,
            project="project",
            timezone="timezone",
            to=0,
            tools="none",
        )
        assert_matches_type(SessionStatsInfo, session, path=["response"])

    @parametrize
    def test_raw_response_stats(self, client: Opencode) -> None:
        response = client.session.with_raw_response.stats()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = response.parse()
        assert_matches_type(SessionStatsInfo, session, path=["response"])

    @parametrize
    def test_streaming_response_stats(self, client: Opencode) -> None:
        with client.session.with_streaming_response.stats() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = response.parse()
            assert_matches_type(SessionStatsInfo, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_switch_agent(self, client: Opencode) -> None:
        session = client.session.switch_agent(
            session_id="sessionID",
            agent="agent",
        )
        assert session is None

    @parametrize
    def test_raw_response_switch_agent(self, client: Opencode) -> None:
        response = client.session.with_raw_response.switch_agent(
            session_id="sessionID",
            agent="agent",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = response.parse()
        assert session is None

    @parametrize
    def test_streaming_response_switch_agent(self, client: Opencode) -> None:
        with client.session.with_streaming_response.switch_agent(
            session_id="sessionID",
            agent="agent",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = response.parse()
            assert session is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_switch_agent(self, client: Opencode) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            client.session.with_raw_response.switch_agent(
                session_id="",
                agent="agent",
            )

    @parametrize
    def test_method_switch_model(self, client: Opencode) -> None:
        session = client.session.switch_model(
            session_id="sessionID",
            model={
                "id": "string",
                "provider_id": "string",
                "variant": "string",
            },
        )
        assert session is None

    @parametrize
    def test_raw_response_switch_model(self, client: Opencode) -> None:
        response = client.session.with_raw_response.switch_model(
            session_id="sessionID",
            model={
                "id": "string",
                "provider_id": "string",
                "variant": "string",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = response.parse()
        assert session is None

    @parametrize
    def test_streaming_response_switch_model(self, client: Opencode) -> None:
        with client.session.with_streaming_response.switch_model(
            session_id="sessionID",
            model={
                "id": "string",
                "provider_id": "string",
                "variant": "string",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = response.parse()
            assert session is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_switch_model(self, client: Opencode) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            client.session.with_raw_response.switch_model(
                session_id="",
                model={
                    "id": "string",
                    "provider_id": "string",
                    "variant": "string",
                },
            )

    @parametrize
    def test_method_synthetic(self, client: Opencode) -> None:
        session = client.session.synthetic(
            session_id="sessionID",
            text="text",
        )
        assert_matches_type(SessionInboxSynthetic, session, path=["response"])

    @parametrize
    def test_method_synthetic_with_all_params(self, client: Opencode) -> None:
        session = client.session.synthetic(
            session_id="sessionID",
            text="text",
            delivery="steer",
            description="description",
            id="id",
            metadata={"foo": {}},
            resume=True,
        )
        assert_matches_type(SessionInboxSynthetic, session, path=["response"])

    @parametrize
    def test_raw_response_synthetic(self, client: Opencode) -> None:
        response = client.session.with_raw_response.synthetic(
            session_id="sessionID",
            text="text",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = response.parse()
        assert_matches_type(SessionInboxSynthetic, session, path=["response"])

    @parametrize
    def test_streaming_response_synthetic(self, client: Opencode) -> None:
        with client.session.with_streaming_response.synthetic(
            session_id="sessionID",
            text="text",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = response.parse()
            assert_matches_type(SessionInboxSynthetic, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_synthetic(self, client: Opencode) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            client.session.with_raw_response.synthetic(
                session_id="",
                text="text",
            )

    @parametrize
    def test_method_view(self, client: Opencode) -> None:
        session = client.session.view(
            session_id="sessionID",
            idle=0,
        )
        assert session is None

    @parametrize
    def test_raw_response_view(self, client: Opencode) -> None:
        response = client.session.with_raw_response.view(
            session_id="sessionID",
            idle=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = response.parse()
        assert session is None

    @parametrize
    def test_streaming_response_view(self, client: Opencode) -> None:
        with client.session.with_streaming_response.view(
            session_id="sessionID",
            idle=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = response.parse()
            assert session is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_view(self, client: Opencode) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            client.session.with_raw_response.view(
                session_id="",
                idle=0,
            )

    @parametrize
    def test_method_wait(self, client: Opencode) -> None:
        session = client.session.wait(
            "sessionID",
        )
        assert session is None

    @parametrize
    def test_raw_response_wait(self, client: Opencode) -> None:
        response = client.session.with_raw_response.wait(
            "sessionID",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = response.parse()
        assert session is None

    @parametrize
    def test_streaming_response_wait(self, client: Opencode) -> None:
        with client.session.with_streaming_response.wait(
            "sessionID",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = response.parse()
            assert session is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_wait(self, client: Opencode) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            client.session.with_raw_response.wait(
                "",
            )


class TestAsyncSession:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncOpencode) -> None:
        session = await async_client.session.create()
        assert_matches_type(SessionInfo, session, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncOpencode) -> None:
        session = await async_client.session.create(
            agent="agent",
            id="id",
            location={
                "directory": "string",
            },
            metadata={"foo": {}},
            model={
                "id": "string",
                "provider_id": "string",
                "variant": "string",
            },
            parent_id="parentID",
            permissions=[
                {
                    "action": "string",
                    "effect": "allow",
                    "resource": "string",
                }
            ],
            title="title",
        )
        assert_matches_type(SessionInfo, session, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncOpencode) -> None:
        response = await async_client.session.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = await response.parse()
        assert_matches_type(SessionInfo, session, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncOpencode) -> None:
        async with async_client.session.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = await response.parse()
            assert_matches_type(SessionInfo, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_update(self, async_client: AsyncOpencode) -> None:
        session = await async_client.session.update(
            session_id="sessionID",
        )
        assert session is None

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncOpencode) -> None:
        session = await async_client.session.update(
            session_id="sessionID",
            archived=True,
            metadata={"foo": {}},
            permissions=[
                {
                    "action": "string",
                    "effect": "allow",
                    "resource": "string",
                }
            ],
            title="title",
        )
        assert session is None

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncOpencode) -> None:
        response = await async_client.session.with_raw_response.update(
            session_id="sessionID",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = await response.parse()
        assert session is None

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncOpencode) -> None:
        async with async_client.session.with_streaming_response.update(
            session_id="sessionID",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = await response.parse()
            assert session is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncOpencode) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            await async_client.session.with_raw_response.update(
                session_id="",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncOpencode) -> None:
        session = await async_client.session.list()
        assert_matches_type(AsyncCursorPage[SessionInfo], session, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncOpencode) -> None:
        session = await async_client.session.list(
            archived=True,
            cursor="cursor",
            directory="directory",
            limit=0,
            order="asc",
            parent_id="parentID",
            project="project",
            search="search",
            subpath="subpath",
        )
        assert_matches_type(AsyncCursorPage[SessionInfo], session, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncOpencode) -> None:
        response = await async_client.session.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = await response.parse()
        assert_matches_type(AsyncCursorPage[SessionInfo], session, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncOpencode) -> None:
        async with async_client.session.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = await response.parse()
            assert_matches_type(AsyncCursorPage[SessionInfo], session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_active(self, async_client: AsyncOpencode) -> None:
        session = await async_client.session.active()
        assert_matches_type(SessionActiveResponse, session, path=["response"])

    @parametrize
    async def test_raw_response_active(self, async_client: AsyncOpencode) -> None:
        response = await async_client.session.with_raw_response.active()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = await response.parse()
        assert_matches_type(SessionActiveResponse, session, path=["response"])

    @parametrize
    async def test_streaming_response_active(self, async_client: AsyncOpencode) -> None:
        async with async_client.session.with_streaming_response.active() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = await response.parse()
            assert_matches_type(SessionActiveResponse, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_background(self, async_client: AsyncOpencode) -> None:
        session = await async_client.session.background(
            "sessionID",
        )
        assert session is None

    @parametrize
    async def test_raw_response_background(self, async_client: AsyncOpencode) -> None:
        response = await async_client.session.with_raw_response.background(
            "sessionID",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = await response.parse()
        assert session is None

    @parametrize
    async def test_streaming_response_background(self, async_client: AsyncOpencode) -> None:
        async with async_client.session.with_streaming_response.background(
            "sessionID",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = await response.parse()
            assert session is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_background(self, async_client: AsyncOpencode) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            await async_client.session.with_raw_response.background(
                "",
            )

    @parametrize
    async def test_method_command(self, async_client: AsyncOpencode) -> None:
        session = await async_client.session.command(
            session_id="sessionID",
            name="name",
            text="text",
        )
        assert session is None

    @parametrize
    async def test_method_command_with_all_params(self, async_client: AsyncOpencode) -> None:
        session = await async_client.session.command(
            session_id="sessionID",
            name="name",
            text="text",
            agents=[
                {
                    "mention": {
                        "end": 0,
                        "start": 0,
                        "text": "string",
                    },
                    "name": "string",
                }
            ],
            delivery="steer",
            files=[
                {
                    "description": "string",
                    "mention": {
                        "end": 0,
                        "start": 0,
                        "text": "string",
                    },
                    "name": "string",
                    "uri": "string",
                }
            ],
            skills=[
                {
                    "id": "string",
                    "mention": {
                        "end": 0,
                        "start": 0,
                        "text": "string",
                    },
                }
            ],
        )
        assert session is None

    @parametrize
    async def test_raw_response_command(self, async_client: AsyncOpencode) -> None:
        response = await async_client.session.with_raw_response.command(
            session_id="sessionID",
            name="name",
            text="text",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = await response.parse()
        assert session is None

    @parametrize
    async def test_streaming_response_command(self, async_client: AsyncOpencode) -> None:
        async with async_client.session.with_streaming_response.command(
            session_id="sessionID",
            name="name",
            text="text",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = await response.parse()
            assert session is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_command(self, async_client: AsyncOpencode) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            await async_client.session.with_raw_response.command(
                session_id="",
                name="name",
                text="text",
            )

    @parametrize
    async def test_method_compact(self, async_client: AsyncOpencode) -> None:
        session = await async_client.session.compact(
            session_id="sessionID",
        )
        assert_matches_type(SessionInboxCompaction, session, path=["response"])

    @parametrize
    async def test_method_compact_with_all_params(self, async_client: AsyncOpencode) -> None:
        session = await async_client.session.compact(
            session_id="sessionID",
            delivery="steer",
            id="id",
        )
        assert_matches_type(SessionInboxCompaction, session, path=["response"])

    @parametrize
    async def test_raw_response_compact(self, async_client: AsyncOpencode) -> None:
        response = await async_client.session.with_raw_response.compact(
            session_id="sessionID",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = await response.parse()
        assert_matches_type(SessionInboxCompaction, session, path=["response"])

    @parametrize
    async def test_streaming_response_compact(self, async_client: AsyncOpencode) -> None:
        async with async_client.session.with_streaming_response.compact(
            session_id="sessionID",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = await response.parse()
            assert_matches_type(SessionInboxCompaction, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_compact(self, async_client: AsyncOpencode) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            await async_client.session.with_raw_response.compact(
                session_id="",
            )

    @parametrize
    async def test_method_context(self, async_client: AsyncOpencode) -> None:
        session = await async_client.session.context(
            "sessionID",
        )
        assert_matches_type(SessionContextResponse, session, path=["response"])

    @parametrize
    async def test_raw_response_context(self, async_client: AsyncOpencode) -> None:
        response = await async_client.session.with_raw_response.context(
            "sessionID",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = await response.parse()
        assert_matches_type(SessionContextResponse, session, path=["response"])

    @parametrize
    async def test_streaming_response_context(self, async_client: AsyncOpencode) -> None:
        async with async_client.session.with_streaming_response.context(
            "sessionID",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = await response.parse()
            assert_matches_type(SessionContextResponse, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_context(self, async_client: AsyncOpencode) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            await async_client.session.with_raw_response.context(
                "",
            )

    @parametrize
    async def test_method_diff(self, async_client: AsyncOpencode) -> None:
        session = await async_client.session.diff(
            session_id="sessionID",
        )
        assert_matches_type(SessionDiffResponse, session, path=["response"])

    @parametrize
    async def test_method_diff_with_all_params(self, async_client: AsyncOpencode) -> None:
        session = await async_client.session.diff(
            session_id="sessionID",
            context=0,
            from_="from",
            to="to",
        )
        assert_matches_type(SessionDiffResponse, session, path=["response"])

    @parametrize
    async def test_raw_response_diff(self, async_client: AsyncOpencode) -> None:
        response = await async_client.session.with_raw_response.diff(
            session_id="sessionID",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = await response.parse()
        assert_matches_type(SessionDiffResponse, session, path=["response"])

    @parametrize
    async def test_streaming_response_diff(self, async_client: AsyncOpencode) -> None:
        async with async_client.session.with_streaming_response.diff(
            session_id="sessionID",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = await response.parse()
            assert_matches_type(SessionDiffResponse, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_diff(self, async_client: AsyncOpencode) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            await async_client.session.with_raw_response.diff(
                session_id="",
            )

    @parametrize
    async def test_method_environment(self, async_client: AsyncOpencode) -> None:
        session = await async_client.session.environment(
            session_id="sessionID",
            variables={"foo": "string"},
        )
        assert session is None

    @parametrize
    async def test_raw_response_environment(self, async_client: AsyncOpencode) -> None:
        response = await async_client.session.with_raw_response.environment(
            session_id="sessionID",
            variables={"foo": "string"},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = await response.parse()
        assert session is None

    @parametrize
    async def test_streaming_response_environment(self, async_client: AsyncOpencode) -> None:
        async with async_client.session.with_streaming_response.environment(
            session_id="sessionID",
            variables={"foo": "string"},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = await response.parse()
            assert session is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_environment(self, async_client: AsyncOpencode) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            await async_client.session.with_raw_response.environment(
                session_id="",
                variables={"foo": "string"},
            )

    @parametrize
    async def test_method_export(self, async_client: AsyncOpencode) -> None:
        session = await async_client.session.export(
            session_id="sessionID",
        )
        assert_matches_type(SessionTransferData, session, path=["response"])

    @parametrize
    async def test_method_export_with_all_params(self, async_client: AsyncOpencode) -> None:
        session = await async_client.session.export(
            session_id="sessionID",
            sanitize=True,
        )
        assert_matches_type(SessionTransferData, session, path=["response"])

    @parametrize
    async def test_raw_response_export(self, async_client: AsyncOpencode) -> None:
        response = await async_client.session.with_raw_response.export(
            session_id="sessionID",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = await response.parse()
        assert_matches_type(SessionTransferData, session, path=["response"])

    @parametrize
    async def test_streaming_response_export(self, async_client: AsyncOpencode) -> None:
        async with async_client.session.with_streaming_response.export(
            session_id="sessionID",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = await response.parse()
            assert_matches_type(SessionTransferData, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_export(self, async_client: AsyncOpencode) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            await async_client.session.with_raw_response.export(
                session_id="",
            )

    @parametrize
    async def test_method_fork(self, async_client: AsyncOpencode) -> None:
        session = await async_client.session.fork(
            session_id="sessionID",
        )
        assert_matches_type(SessionInfo, session, path=["response"])

    @parametrize
    async def test_method_fork_with_all_params(self, async_client: AsyncOpencode) -> None:
        session = await async_client.session.fork(
            session_id="sessionID",
            before="before",
        )
        assert_matches_type(SessionInfo, session, path=["response"])

    @parametrize
    async def test_raw_response_fork(self, async_client: AsyncOpencode) -> None:
        response = await async_client.session.with_raw_response.fork(
            session_id="sessionID",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = await response.parse()
        assert_matches_type(SessionInfo, session, path=["response"])

    @parametrize
    async def test_streaming_response_fork(self, async_client: AsyncOpencode) -> None:
        async with async_client.session.with_streaming_response.fork(
            session_id="sessionID",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = await response.parse()
            assert_matches_type(SessionInfo, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_fork(self, async_client: AsyncOpencode) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            await async_client.session.with_raw_response.fork(
                session_id="",
            )

    @parametrize
    async def test_method_generate(self, async_client: AsyncOpencode) -> None:
        session = await async_client.session.generate(
            session_id="sessionID",
            prompt="prompt",
        )
        assert_matches_type(SessionGenerateResponse, session, path=["response"])

    @parametrize
    async def test_raw_response_generate(self, async_client: AsyncOpencode) -> None:
        response = await async_client.session.with_raw_response.generate(
            session_id="sessionID",
            prompt="prompt",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = await response.parse()
        assert_matches_type(SessionGenerateResponse, session, path=["response"])

    @parametrize
    async def test_streaming_response_generate(self, async_client: AsyncOpencode) -> None:
        async with async_client.session.with_streaming_response.generate(
            session_id="sessionID",
            prompt="prompt",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = await response.parse()
            assert_matches_type(SessionGenerateResponse, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_generate(self, async_client: AsyncOpencode) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            await async_client.session.with_raw_response.generate(
                session_id="",
                prompt="prompt",
            )

    @parametrize
    async def test_method_get(self, async_client: AsyncOpencode) -> None:
        session = await async_client.session.get(
            "sessionID",
        )
        assert_matches_type(SessionInfo, session, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncOpencode) -> None:
        response = await async_client.session.with_raw_response.get(
            "sessionID",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = await response.parse()
        assert_matches_type(SessionInfo, session, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncOpencode) -> None:
        async with async_client.session.with_streaming_response.get(
            "sessionID",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = await response.parse()
            assert_matches_type(SessionInfo, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncOpencode) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            await async_client.session.with_raw_response.get(
                "",
            )

    @parametrize
    async def test_method_import_(self, async_client: AsyncOpencode) -> None:
        session = await async_client.session.import_(
            info={
                "agent": "string",
                "cost": 0,
                "fork": {
                    "boundary": {
                        "message_id": "string",
                        "type": "before",
                    },
                    "session_id": "string",
                },
                "id": "string",
                "location": {
                    "directory": "string",
                },
                "metadata": {"foo": {}},
                "model": {
                    "id": "string",
                    "provider_id": "string",
                    "variant": "string",
                },
                "outcome": "succeeded",
                "parent_id": "string",
                "permissions": [
                    {
                        "action": "string",
                        "effect": "allow",
                        "resource": "string",
                    }
                ],
                "project_id": "string",
                "revert": {
                    "files": [
                        {
                            "additions": 0,
                            "deletions": 0,
                            "file": "string",
                            "patch": "string",
                            "status": "added",
                        }
                    ],
                    "message_id": "string",
                    "part_id": "string",
                    "snapshot": "string",
                },
                "subpath": "string",
                "time": {
                    "archived": 0,
                    "created": 0,
                    "idle": 0,
                    "updated": 0,
                    "viewed": 0,
                },
                "title": "string",
                "tokens": {
                    "cache": {
                        "read": 0,
                        "write": 0,
                    },
                    "input": 0,
                    "output": 0,
                    "reasoning": 0,
                },
            },
            messages=[{}],
        )
        assert_matches_type(SessionInfo, session, path=["response"])

    @parametrize
    async def test_method_import__with_all_params(self, async_client: AsyncOpencode) -> None:
        session = await async_client.session.import_(
            info={
                "agent": "string",
                "cost": 0,
                "fork": {
                    "boundary": {
                        "message_id": "string",
                        "type": "before",
                    },
                    "session_id": "string",
                },
                "id": "string",
                "location": {
                    "directory": "string",
                },
                "metadata": {"foo": {}},
                "model": {
                    "id": "string",
                    "provider_id": "string",
                    "variant": "string",
                },
                "outcome": "succeeded",
                "parent_id": "string",
                "permissions": [
                    {
                        "action": "string",
                        "effect": "allow",
                        "resource": "string",
                    }
                ],
                "project_id": "string",
                "revert": {
                    "files": [
                        {
                            "additions": 0,
                            "deletions": 0,
                            "file": "string",
                            "patch": "string",
                            "status": "added",
                        }
                    ],
                    "message_id": "string",
                    "part_id": "string",
                    "snapshot": "string",
                },
                "subpath": "string",
                "time": {
                    "archived": 0,
                    "created": 0,
                    "idle": 0,
                    "updated": 0,
                    "viewed": 0,
                },
                "title": "string",
                "tokens": {
                    "cache": {
                        "read": 0,
                        "write": 0,
                    },
                    "input": 0,
                    "output": 0,
                    "reasoning": 0,
                },
            },
            messages=[{}],
            location={
                "directory": "string",
            },
        )
        assert_matches_type(SessionInfo, session, path=["response"])

    @parametrize
    async def test_raw_response_import_(self, async_client: AsyncOpencode) -> None:
        response = await async_client.session.with_raw_response.import_(
            info={
                "agent": "string",
                "cost": 0,
                "fork": {
                    "boundary": {
                        "message_id": "string",
                        "type": "before",
                    },
                    "session_id": "string",
                },
                "id": "string",
                "location": {
                    "directory": "string",
                },
                "metadata": {"foo": {}},
                "model": {
                    "id": "string",
                    "provider_id": "string",
                    "variant": "string",
                },
                "outcome": "succeeded",
                "parent_id": "string",
                "permissions": [
                    {
                        "action": "string",
                        "effect": "allow",
                        "resource": "string",
                    }
                ],
                "project_id": "string",
                "revert": {
                    "files": [
                        {
                            "additions": 0,
                            "deletions": 0,
                            "file": "string",
                            "patch": "string",
                            "status": "added",
                        }
                    ],
                    "message_id": "string",
                    "part_id": "string",
                    "snapshot": "string",
                },
                "subpath": "string",
                "time": {
                    "archived": 0,
                    "created": 0,
                    "idle": 0,
                    "updated": 0,
                    "viewed": 0,
                },
                "title": "string",
                "tokens": {
                    "cache": {
                        "read": 0,
                        "write": 0,
                    },
                    "input": 0,
                    "output": 0,
                    "reasoning": 0,
                },
            },
            messages=[{}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = await response.parse()
        assert_matches_type(SessionInfo, session, path=["response"])

    @parametrize
    async def test_streaming_response_import_(self, async_client: AsyncOpencode) -> None:
        async with async_client.session.with_streaming_response.import_(
            info={
                "agent": "string",
                "cost": 0,
                "fork": {
                    "boundary": {
                        "message_id": "string",
                        "type": "before",
                    },
                    "session_id": "string",
                },
                "id": "string",
                "location": {
                    "directory": "string",
                },
                "metadata": {"foo": {}},
                "model": {
                    "id": "string",
                    "provider_id": "string",
                    "variant": "string",
                },
                "outcome": "succeeded",
                "parent_id": "string",
                "permissions": [
                    {
                        "action": "string",
                        "effect": "allow",
                        "resource": "string",
                    }
                ],
                "project_id": "string",
                "revert": {
                    "files": [
                        {
                            "additions": 0,
                            "deletions": 0,
                            "file": "string",
                            "patch": "string",
                            "status": "added",
                        }
                    ],
                    "message_id": "string",
                    "part_id": "string",
                    "snapshot": "string",
                },
                "subpath": "string",
                "time": {
                    "archived": 0,
                    "created": 0,
                    "idle": 0,
                    "updated": 0,
                    "viewed": 0,
                },
                "title": "string",
                "tokens": {
                    "cache": {
                        "read": 0,
                        "write": 0,
                    },
                    "input": 0,
                    "output": 0,
                    "reasoning": 0,
                },
            },
            messages=[{}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = await response.parse()
            assert_matches_type(SessionInfo, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_interrupt(self, async_client: AsyncOpencode) -> None:
        session = await async_client.session.interrupt(
            session_id="sessionID",
        )
        assert_matches_type(SessionInterruptResponse, session, path=["response"])

    @parametrize
    async def test_method_interrupt_with_all_params(self, async_client: AsyncOpencode) -> None:
        session = await async_client.session.interrupt(
            session_id="sessionID",
            resume=True,
        )
        assert_matches_type(SessionInterruptResponse, session, path=["response"])

    @parametrize
    async def test_raw_response_interrupt(self, async_client: AsyncOpencode) -> None:
        response = await async_client.session.with_raw_response.interrupt(
            session_id="sessionID",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = await response.parse()
        assert_matches_type(SessionInterruptResponse, session, path=["response"])

    @parametrize
    async def test_streaming_response_interrupt(self, async_client: AsyncOpencode) -> None:
        async with async_client.session.with_streaming_response.interrupt(
            session_id="sessionID",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = await response.parse()
            assert_matches_type(SessionInterruptResponse, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_interrupt(self, async_client: AsyncOpencode) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            await async_client.session.with_raw_response.interrupt(
                session_id="",
            )

    @pytest.mark.skip(reason="The mock server rejects integer query parameters typed through a $ref in anyOf.")
    @parametrize
    async def test_method_log(self, async_client: AsyncOpencode) -> None:
        session = await async_client.session.log(
            session_id="sessionID",
        )
        assert session is None

    @pytest.mark.skip(reason="The mock server rejects integer query parameters typed through a $ref in anyOf.")
    @parametrize
    async def test_method_log_with_all_params(self, async_client: AsyncOpencode) -> None:
        session = await async_client.session.log(
            session_id="sessionID",
            after=0,
            follow=True,
        )
        assert session is None

    @pytest.mark.skip(reason="The mock server rejects integer query parameters typed through a $ref in anyOf.")
    @parametrize
    async def test_raw_response_log(self, async_client: AsyncOpencode) -> None:
        response = await async_client.session.with_raw_response.log(
            session_id="sessionID",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = await response.parse()
        assert session is None

    @pytest.mark.skip(reason="The mock server rejects integer query parameters typed through a $ref in anyOf.")
    @parametrize
    async def test_streaming_response_log(self, async_client: AsyncOpencode) -> None:
        async with async_client.session.with_streaming_response.log(
            session_id="sessionID",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = await response.parse()
            assert session is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="The mock server rejects integer query parameters typed through a $ref in anyOf.")
    @parametrize
    async def test_path_params_log(self, async_client: AsyncOpencode) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            await async_client.session.with_raw_response.log(
                session_id="",
            )

    @parametrize
    async def test_method_move(self, async_client: AsyncOpencode) -> None:
        session = await async_client.session.move(
            session_id="sessionID",
            directory="directory",
        )
        assert session is None

    @parametrize
    async def test_method_move_with_all_params(self, async_client: AsyncOpencode) -> None:
        session = await async_client.session.move(
            session_id="sessionID",
            directory="directory",
            delivery="steer",
        )
        assert session is None

    @parametrize
    async def test_raw_response_move(self, async_client: AsyncOpencode) -> None:
        response = await async_client.session.with_raw_response.move(
            session_id="sessionID",
            directory="directory",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = await response.parse()
        assert session is None

    @parametrize
    async def test_streaming_response_move(self, async_client: AsyncOpencode) -> None:
        async with async_client.session.with_streaming_response.move(
            session_id="sessionID",
            directory="directory",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = await response.parse()
            assert session is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_move(self, async_client: AsyncOpencode) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            await async_client.session.with_raw_response.move(
                session_id="",
                directory="directory",
            )

    @parametrize
    async def test_method_prompt(self, async_client: AsyncOpencode) -> None:
        session = await async_client.session.prompt(
            session_id="sessionID",
            text="text",
        )
        assert_matches_type(SessionInboxUser, session, path=["response"])

    @parametrize
    async def test_method_prompt_with_all_params(self, async_client: AsyncOpencode) -> None:
        session = await async_client.session.prompt(
            session_id="sessionID",
            text="text",
            agents=[
                {
                    "mention": {
                        "end": 0,
                        "start": 0,
                        "text": "string",
                    },
                    "name": "string",
                }
            ],
            delivery="steer",
            files=[
                {
                    "description": "string",
                    "mention": {
                        "end": 0,
                        "start": 0,
                        "text": "string",
                    },
                    "name": "string",
                    "uri": "string",
                }
            ],
            id="id",
            metadata={"foo": {}},
            resume=True,
            skills=[
                {
                    "id": "string",
                    "mention": {
                        "end": 0,
                        "start": 0,
                        "text": "string",
                    },
                }
            ],
        )
        assert_matches_type(SessionInboxUser, session, path=["response"])

    @parametrize
    async def test_raw_response_prompt(self, async_client: AsyncOpencode) -> None:
        response = await async_client.session.with_raw_response.prompt(
            session_id="sessionID",
            text="text",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = await response.parse()
        assert_matches_type(SessionInboxUser, session, path=["response"])

    @parametrize
    async def test_streaming_response_prompt(self, async_client: AsyncOpencode) -> None:
        async with async_client.session.with_streaming_response.prompt(
            session_id="sessionID",
            text="text",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = await response.parse()
            assert_matches_type(SessionInboxUser, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_prompt(self, async_client: AsyncOpencode) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            await async_client.session.with_raw_response.prompt(
                session_id="",
                text="text",
            )

    @parametrize
    async def test_method_remove(self, async_client: AsyncOpencode) -> None:
        session = await async_client.session.remove(
            "sessionID",
        )
        assert session is None

    @parametrize
    async def test_raw_response_remove(self, async_client: AsyncOpencode) -> None:
        response = await async_client.session.with_raw_response.remove(
            "sessionID",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = await response.parse()
        assert session is None

    @parametrize
    async def test_streaming_response_remove(self, async_client: AsyncOpencode) -> None:
        async with async_client.session.with_streaming_response.remove(
            "sessionID",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = await response.parse()
            assert session is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_remove(self, async_client: AsyncOpencode) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            await async_client.session.with_raw_response.remove(
                "",
            )

    @parametrize
    async def test_method_shell(self, async_client: AsyncOpencode) -> None:
        session = await async_client.session.shell(
            session_id="sessionID",
            command="command",
        )
        assert session is None

    @parametrize
    async def test_method_shell_with_all_params(self, async_client: AsyncOpencode) -> None:
        session = await async_client.session.shell(
            session_id="sessionID",
            command="command",
            id="id",
        )
        assert session is None

    @parametrize
    async def test_raw_response_shell(self, async_client: AsyncOpencode) -> None:
        response = await async_client.session.with_raw_response.shell(
            session_id="sessionID",
            command="command",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = await response.parse()
        assert session is None

    @parametrize
    async def test_streaming_response_shell(self, async_client: AsyncOpencode) -> None:
        async with async_client.session.with_streaming_response.shell(
            session_id="sessionID",
            command="command",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = await response.parse()
            assert session is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_shell(self, async_client: AsyncOpencode) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            await async_client.session.with_raw_response.shell(
                session_id="",
                command="command",
            )

    @parametrize
    async def test_method_skill(self, async_client: AsyncOpencode) -> None:
        session = await async_client.session.skill(
            session_id="sessionID",
            id="id",
        )
        assert session is None

    @parametrize
    async def test_method_skill_with_all_params(self, async_client: AsyncOpencode) -> None:
        session = await async_client.session.skill(
            session_id="sessionID",
            id="id",
            resume=True,
        )
        assert session is None

    @parametrize
    async def test_raw_response_skill(self, async_client: AsyncOpencode) -> None:
        response = await async_client.session.with_raw_response.skill(
            session_id="sessionID",
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = await response.parse()
        assert session is None

    @parametrize
    async def test_streaming_response_skill(self, async_client: AsyncOpencode) -> None:
        async with async_client.session.with_streaming_response.skill(
            session_id="sessionID",
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = await response.parse()
            assert session is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_skill(self, async_client: AsyncOpencode) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            await async_client.session.with_raw_response.skill(
                session_id="",
                id="id",
            )

    @parametrize
    async def test_method_stats(self, async_client: AsyncOpencode) -> None:
        session = await async_client.session.stats()
        assert_matches_type(SessionStatsInfo, session, path=["response"])

    @parametrize
    async def test_method_stats_with_all_params(self, async_client: AsyncOpencode) -> None:
        session = await async_client.session.stats(
            from_=0,
            project="project",
            timezone="timezone",
            to=0,
            tools="none",
        )
        assert_matches_type(SessionStatsInfo, session, path=["response"])

    @parametrize
    async def test_raw_response_stats(self, async_client: AsyncOpencode) -> None:
        response = await async_client.session.with_raw_response.stats()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = await response.parse()
        assert_matches_type(SessionStatsInfo, session, path=["response"])

    @parametrize
    async def test_streaming_response_stats(self, async_client: AsyncOpencode) -> None:
        async with async_client.session.with_streaming_response.stats() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = await response.parse()
            assert_matches_type(SessionStatsInfo, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_switch_agent(self, async_client: AsyncOpencode) -> None:
        session = await async_client.session.switch_agent(
            session_id="sessionID",
            agent="agent",
        )
        assert session is None

    @parametrize
    async def test_raw_response_switch_agent(self, async_client: AsyncOpencode) -> None:
        response = await async_client.session.with_raw_response.switch_agent(
            session_id="sessionID",
            agent="agent",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = await response.parse()
        assert session is None

    @parametrize
    async def test_streaming_response_switch_agent(self, async_client: AsyncOpencode) -> None:
        async with async_client.session.with_streaming_response.switch_agent(
            session_id="sessionID",
            agent="agent",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = await response.parse()
            assert session is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_switch_agent(self, async_client: AsyncOpencode) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            await async_client.session.with_raw_response.switch_agent(
                session_id="",
                agent="agent",
            )

    @parametrize
    async def test_method_switch_model(self, async_client: AsyncOpencode) -> None:
        session = await async_client.session.switch_model(
            session_id="sessionID",
            model={
                "id": "string",
                "provider_id": "string",
                "variant": "string",
            },
        )
        assert session is None

    @parametrize
    async def test_raw_response_switch_model(self, async_client: AsyncOpencode) -> None:
        response = await async_client.session.with_raw_response.switch_model(
            session_id="sessionID",
            model={
                "id": "string",
                "provider_id": "string",
                "variant": "string",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = await response.parse()
        assert session is None

    @parametrize
    async def test_streaming_response_switch_model(self, async_client: AsyncOpencode) -> None:
        async with async_client.session.with_streaming_response.switch_model(
            session_id="sessionID",
            model={
                "id": "string",
                "provider_id": "string",
                "variant": "string",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = await response.parse()
            assert session is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_switch_model(self, async_client: AsyncOpencode) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            await async_client.session.with_raw_response.switch_model(
                session_id="",
                model={
                    "id": "string",
                    "provider_id": "string",
                    "variant": "string",
                },
            )

    @parametrize
    async def test_method_synthetic(self, async_client: AsyncOpencode) -> None:
        session = await async_client.session.synthetic(
            session_id="sessionID",
            text="text",
        )
        assert_matches_type(SessionInboxSynthetic, session, path=["response"])

    @parametrize
    async def test_method_synthetic_with_all_params(self, async_client: AsyncOpencode) -> None:
        session = await async_client.session.synthetic(
            session_id="sessionID",
            text="text",
            delivery="steer",
            description="description",
            id="id",
            metadata={"foo": {}},
            resume=True,
        )
        assert_matches_type(SessionInboxSynthetic, session, path=["response"])

    @parametrize
    async def test_raw_response_synthetic(self, async_client: AsyncOpencode) -> None:
        response = await async_client.session.with_raw_response.synthetic(
            session_id="sessionID",
            text="text",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = await response.parse()
        assert_matches_type(SessionInboxSynthetic, session, path=["response"])

    @parametrize
    async def test_streaming_response_synthetic(self, async_client: AsyncOpencode) -> None:
        async with async_client.session.with_streaming_response.synthetic(
            session_id="sessionID",
            text="text",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = await response.parse()
            assert_matches_type(SessionInboxSynthetic, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_synthetic(self, async_client: AsyncOpencode) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            await async_client.session.with_raw_response.synthetic(
                session_id="",
                text="text",
            )

    @parametrize
    async def test_method_view(self, async_client: AsyncOpencode) -> None:
        session = await async_client.session.view(
            session_id="sessionID",
            idle=0,
        )
        assert session is None

    @parametrize
    async def test_raw_response_view(self, async_client: AsyncOpencode) -> None:
        response = await async_client.session.with_raw_response.view(
            session_id="sessionID",
            idle=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = await response.parse()
        assert session is None

    @parametrize
    async def test_streaming_response_view(self, async_client: AsyncOpencode) -> None:
        async with async_client.session.with_streaming_response.view(
            session_id="sessionID",
            idle=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = await response.parse()
            assert session is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_view(self, async_client: AsyncOpencode) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            await async_client.session.with_raw_response.view(
                session_id="",
                idle=0,
            )

    @parametrize
    async def test_method_wait(self, async_client: AsyncOpencode) -> None:
        session = await async_client.session.wait(
            "sessionID",
        )
        assert session is None

    @parametrize
    async def test_raw_response_wait(self, async_client: AsyncOpencode) -> None:
        response = await async_client.session.with_raw_response.wait(
            "sessionID",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = await response.parse()
        assert session is None

    @parametrize
    async def test_streaming_response_wait(self, async_client: AsyncOpencode) -> None:
        async with async_client.session.with_streaming_response.wait(
            "sessionID",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = await response.parse()
            assert session is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_wait(self, async_client: AsyncOpencode) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            await async_client.session.with_raw_response.wait(
                "",
            )
