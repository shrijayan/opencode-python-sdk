# File generated from our OpenAPI spec by Ferrule. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from opencode import Opencode, AsyncOpencode
from tests.utils import assert_matches_type
from opencode.types import (
    SessionGetResponse,
    SessionDiffResponse,
    SessionForkResponse,
    SessionStatsResponse,
    SessionActiveResponse,
    SessionCreateResponse,
    SessionExportResponse,
    SessionImportResponse,
    SessionPromptResponse,
    SessionCompactResponse,
    SessionContextResponse,
    SessionSyntheticResponse,
)
from opencode.types.shared import (
    SessionInfo,
    SessionGenerateResponse,
    SessionInterruptResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSession:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Opencode) -> None:
        session = client.session.create()
        assert_matches_type(SessionCreateResponse, session, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Opencode) -> None:
        session = client.session.create(
            agent={},
            id={},
            location={},
            metadata={},
            model={},
            parent_id={},
            permissions={},
            title="title",
        )
        assert_matches_type(SessionCreateResponse, session, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Opencode) -> None:
        response = client.session.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = response.parse()
        assert_matches_type(SessionCreateResponse, session, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Opencode) -> None:
        with client.session.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = response.parse()
            assert_matches_type(SessionCreateResponse, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_update(self, client: Opencode) -> None:
        session = client.session.update(
            session_id={},
        )
        assert session is None

    @parametrize
    def test_method_update_with_all_params(self, client: Opencode) -> None:
        session = client.session.update(
            session_id={},
            archived=True,
            metadata={},
            permissions={},
            title="title",
        )
        assert session is None

    @parametrize
    def test_raw_response_update(self, client: Opencode) -> None:
        response = client.session.with_raw_response.update(
            session_id={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = response.parse()
        assert session is None

    @parametrize
    def test_streaming_response_update(self, client: Opencode) -> None:
        with client.session.with_streaming_response.update(
            session_id={},
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
        assert_matches_type(SessionInfo, session, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Opencode) -> None:
        session = client.session.list(
            archived=True,
            cursor={},
            directory={},
            limit=0,
            order="asc",
            parent_id={},
            project={},
            search="search",
            subpath={},
        )
        assert_matches_type(SessionInfo, session, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Opencode) -> None:
        response = client.session.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = response.parse()
        assert_matches_type(SessionInfo, session, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Opencode) -> None:
        with client.session.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = response.parse()
            assert_matches_type(SessionInfo, session, path=["response"])

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
            {},
        )
        assert session is None

    @parametrize
    def test_raw_response_background(self, client: Opencode) -> None:
        response = client.session.with_raw_response.background(
            {},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = response.parse()
        assert session is None

    @parametrize
    def test_streaming_response_background(self, client: Opencode) -> None:
        with client.session.with_streaming_response.background(
            {},
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
            session_id={},
            name="name",
            text="text",
        )
        assert session is None

    @parametrize
    def test_method_command_with_all_params(self, client: Opencode) -> None:
        session = client.session.command(
            session_id={},
            name="name",
            text="text",
            agents=[{}],
            delivery={},
            files=[{}],
            skills=[{}],
        )
        assert session is None

    @parametrize
    def test_raw_response_command(self, client: Opencode) -> None:
        response = client.session.with_raw_response.command(
            session_id={},
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
            session_id={},
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
            session_id={},
        )
        assert_matches_type(SessionCompactResponse, session, path=["response"])

    @parametrize
    def test_method_compact_with_all_params(self, client: Opencode) -> None:
        session = client.session.compact(
            session_id={},
            delivery={},
            id={},
        )
        assert_matches_type(SessionCompactResponse, session, path=["response"])

    @parametrize
    def test_raw_response_compact(self, client: Opencode) -> None:
        response = client.session.with_raw_response.compact(
            session_id={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = response.parse()
        assert_matches_type(SessionCompactResponse, session, path=["response"])

    @parametrize
    def test_streaming_response_compact(self, client: Opencode) -> None:
        with client.session.with_streaming_response.compact(
            session_id={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = response.parse()
            assert_matches_type(SessionCompactResponse, session, path=["response"])

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
            {},
        )
        assert_matches_type(SessionContextResponse, session, path=["response"])

    @parametrize
    def test_raw_response_context(self, client: Opencode) -> None:
        response = client.session.with_raw_response.context(
            {},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = response.parse()
        assert_matches_type(SessionContextResponse, session, path=["response"])

    @parametrize
    def test_streaming_response_context(self, client: Opencode) -> None:
        with client.session.with_streaming_response.context(
            {},
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
            session_id={},
        )
        assert_matches_type(SessionDiffResponse, session, path=["response"])

    @parametrize
    def test_method_diff_with_all_params(self, client: Opencode) -> None:
        session = client.session.diff(
            session_id={},
            context=0,
            from_={},
            to={},
        )
        assert_matches_type(SessionDiffResponse, session, path=["response"])

    @parametrize
    def test_raw_response_diff(self, client: Opencode) -> None:
        response = client.session.with_raw_response.diff(
            session_id={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = response.parse()
        assert_matches_type(SessionDiffResponse, session, path=["response"])

    @parametrize
    def test_streaming_response_diff(self, client: Opencode) -> None:
        with client.session.with_streaming_response.diff(
            session_id={},
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
            session_id={},
            variables={"foo": "string"},
        )
        assert session is None

    @parametrize
    def test_raw_response_environment(self, client: Opencode) -> None:
        response = client.session.with_raw_response.environment(
            session_id={},
            variables={"foo": "string"},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = response.parse()
        assert session is None

    @parametrize
    def test_streaming_response_environment(self, client: Opencode) -> None:
        with client.session.with_streaming_response.environment(
            session_id={},
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
            session_id={},
        )
        assert_matches_type(SessionExportResponse, session, path=["response"])

    @parametrize
    def test_method_export_with_all_params(self, client: Opencode) -> None:
        session = client.session.export(
            session_id={},
            sanitize=True,
        )
        assert_matches_type(SessionExportResponse, session, path=["response"])

    @parametrize
    def test_raw_response_export(self, client: Opencode) -> None:
        response = client.session.with_raw_response.export(
            session_id={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = response.parse()
        assert_matches_type(SessionExportResponse, session, path=["response"])

    @parametrize
    def test_streaming_response_export(self, client: Opencode) -> None:
        with client.session.with_streaming_response.export(
            session_id={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = response.parse()
            assert_matches_type(SessionExportResponse, session, path=["response"])

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
            session_id={},
        )
        assert_matches_type(SessionForkResponse, session, path=["response"])

    @parametrize
    def test_method_fork_with_all_params(self, client: Opencode) -> None:
        session = client.session.fork(
            session_id={},
            before={},
        )
        assert_matches_type(SessionForkResponse, session, path=["response"])

    @parametrize
    def test_raw_response_fork(self, client: Opencode) -> None:
        response = client.session.with_raw_response.fork(
            session_id={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = response.parse()
        assert_matches_type(SessionForkResponse, session, path=["response"])

    @parametrize
    def test_streaming_response_fork(self, client: Opencode) -> None:
        with client.session.with_streaming_response.fork(
            session_id={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = response.parse()
            assert_matches_type(SessionForkResponse, session, path=["response"])

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
            session_id={},
            prompt="prompt",
        )
        assert_matches_type(SessionGenerateResponse, session, path=["response"])

    @parametrize
    def test_raw_response_generate(self, client: Opencode) -> None:
        response = client.session.with_raw_response.generate(
            session_id={},
            prompt="prompt",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = response.parse()
        assert_matches_type(SessionGenerateResponse, session, path=["response"])

    @parametrize
    def test_streaming_response_generate(self, client: Opencode) -> None:
        with client.session.with_streaming_response.generate(
            session_id={},
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
            {},
        )
        assert_matches_type(SessionGetResponse, session, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Opencode) -> None:
        response = client.session.with_raw_response.get(
            {},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = response.parse()
        assert_matches_type(SessionGetResponse, session, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Opencode) -> None:
        with client.session.with_streaming_response.get(
            {},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = response.parse()
            assert_matches_type(SessionGetResponse, session, path=["response"])

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
            info={},
            messages=[{}],
        )
        assert_matches_type(SessionImportResponse, session, path=["response"])

    @parametrize
    def test_method_import__with_all_params(self, client: Opencode) -> None:
        session = client.session.import_(
            info={},
            messages=[{}],
            location={},
        )
        assert_matches_type(SessionImportResponse, session, path=["response"])

    @parametrize
    def test_raw_response_import_(self, client: Opencode) -> None:
        response = client.session.with_raw_response.import_(
            info={},
            messages=[{}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = response.parse()
        assert_matches_type(SessionImportResponse, session, path=["response"])

    @parametrize
    def test_streaming_response_import_(self, client: Opencode) -> None:
        with client.session.with_streaming_response.import_(
            info={},
            messages=[{}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = response.parse()
            assert_matches_type(SessionImportResponse, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_interrupt(self, client: Opencode) -> None:
        session = client.session.interrupt(
            session_id={},
        )
        assert_matches_type(SessionInterruptResponse, session, path=["response"])

    @parametrize
    def test_method_interrupt_with_all_params(self, client: Opencode) -> None:
        session = client.session.interrupt(
            session_id={},
            resume=True,
        )
        assert_matches_type(SessionInterruptResponse, session, path=["response"])

    @parametrize
    def test_raw_response_interrupt(self, client: Opencode) -> None:
        response = client.session.with_raw_response.interrupt(
            session_id={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = response.parse()
        assert_matches_type(SessionInterruptResponse, session, path=["response"])

    @parametrize
    def test_streaming_response_interrupt(self, client: Opencode) -> None:
        with client.session.with_streaming_response.interrupt(
            session_id={},
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

    @parametrize
    def test_method_log(self, client: Opencode) -> None:
        session = client.session.log(
            session_id={},
        )
        assert session is None

    @parametrize
    def test_method_log_with_all_params(self, client: Opencode) -> None:
        session = client.session.log(
            session_id={},
            after={},
            follow=True,
        )
        assert session is None

    @parametrize
    def test_raw_response_log(self, client: Opencode) -> None:
        response = client.session.with_raw_response.log(
            session_id={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = response.parse()
        assert session is None

    @parametrize
    def test_streaming_response_log(self, client: Opencode) -> None:
        with client.session.with_streaming_response.log(
            session_id={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = response.parse()
            assert session is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_log(self, client: Opencode) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            client.session.with_raw_response.log(
                session_id="",
            )

    @parametrize
    def test_method_move(self, client: Opencode) -> None:
        session = client.session.move(
            session_id={},
            directory={},
        )
        assert session is None

    @parametrize
    def test_method_move_with_all_params(self, client: Opencode) -> None:
        session = client.session.move(
            session_id={},
            directory={},
            delivery={},
        )
        assert session is None

    @parametrize
    def test_raw_response_move(self, client: Opencode) -> None:
        response = client.session.with_raw_response.move(
            session_id={},
            directory={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = response.parse()
        assert session is None

    @parametrize
    def test_streaming_response_move(self, client: Opencode) -> None:
        with client.session.with_streaming_response.move(
            session_id={},
            directory={},
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
                directory={},
            )

    @parametrize
    def test_method_prompt(self, client: Opencode) -> None:
        session = client.session.prompt(
            session_id={},
            text="text",
        )
        assert_matches_type(SessionPromptResponse, session, path=["response"])

    @parametrize
    def test_method_prompt_with_all_params(self, client: Opencode) -> None:
        session = client.session.prompt(
            session_id={},
            text="text",
            agents=[{}],
            delivery={},
            files=[{}],
            id={},
            metadata={"foo": {}},
            resume=True,
            skills=[{}],
        )
        assert_matches_type(SessionPromptResponse, session, path=["response"])

    @parametrize
    def test_raw_response_prompt(self, client: Opencode) -> None:
        response = client.session.with_raw_response.prompt(
            session_id={},
            text="text",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = response.parse()
        assert_matches_type(SessionPromptResponse, session, path=["response"])

    @parametrize
    def test_streaming_response_prompt(self, client: Opencode) -> None:
        with client.session.with_streaming_response.prompt(
            session_id={},
            text="text",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = response.parse()
            assert_matches_type(SessionPromptResponse, session, path=["response"])

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
            {},
        )
        assert session is None

    @parametrize
    def test_raw_response_remove(self, client: Opencode) -> None:
        response = client.session.with_raw_response.remove(
            {},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = response.parse()
        assert session is None

    @parametrize
    def test_streaming_response_remove(self, client: Opencode) -> None:
        with client.session.with_streaming_response.remove(
            {},
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
            session_id={},
            command="command",
        )
        assert session is None

    @parametrize
    def test_method_shell_with_all_params(self, client: Opencode) -> None:
        session = client.session.shell(
            session_id={},
            command="command",
            id={},
        )
        assert session is None

    @parametrize
    def test_raw_response_shell(self, client: Opencode) -> None:
        response = client.session.with_raw_response.shell(
            session_id={},
            command="command",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = response.parse()
        assert session is None

    @parametrize
    def test_streaming_response_shell(self, client: Opencode) -> None:
        with client.session.with_streaming_response.shell(
            session_id={},
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
            session_id={},
            id={},
        )
        assert session is None

    @parametrize
    def test_method_skill_with_all_params(self, client: Opencode) -> None:
        session = client.session.skill(
            session_id={},
            id={},
            resume=True,
        )
        assert session is None

    @parametrize
    def test_raw_response_skill(self, client: Opencode) -> None:
        response = client.session.with_raw_response.skill(
            session_id={},
            id={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = response.parse()
        assert session is None

    @parametrize
    def test_streaming_response_skill(self, client: Opencode) -> None:
        with client.session.with_streaming_response.skill(
            session_id={},
            id={},
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
                id={},
            )

    @parametrize
    def test_method_stats(self, client: Opencode) -> None:
        session = client.session.stats()
        assert_matches_type(SessionStatsResponse, session, path=["response"])

    @parametrize
    def test_method_stats_with_all_params(self, client: Opencode) -> None:
        session = client.session.stats(
            from_=0,
            project={},
            timezone="timezone",
            to=0,
            tools="none",
        )
        assert_matches_type(SessionStatsResponse, session, path=["response"])

    @parametrize
    def test_raw_response_stats(self, client: Opencode) -> None:
        response = client.session.with_raw_response.stats()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = response.parse()
        assert_matches_type(SessionStatsResponse, session, path=["response"])

    @parametrize
    def test_streaming_response_stats(self, client: Opencode) -> None:
        with client.session.with_streaming_response.stats() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = response.parse()
            assert_matches_type(SessionStatsResponse, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_switch_agent(self, client: Opencode) -> None:
        session = client.session.switch_agent(
            session_id={},
            agent={},
        )
        assert session is None

    @parametrize
    def test_raw_response_switch_agent(self, client: Opencode) -> None:
        response = client.session.with_raw_response.switch_agent(
            session_id={},
            agent={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = response.parse()
        assert session is None

    @parametrize
    def test_streaming_response_switch_agent(self, client: Opencode) -> None:
        with client.session.with_streaming_response.switch_agent(
            session_id={},
            agent={},
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
                agent={},
            )

    @parametrize
    def test_method_switch_model(self, client: Opencode) -> None:
        session = client.session.switch_model(
            session_id={},
            model={},
        )
        assert session is None

    @parametrize
    def test_raw_response_switch_model(self, client: Opencode) -> None:
        response = client.session.with_raw_response.switch_model(
            session_id={},
            model={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = response.parse()
        assert session is None

    @parametrize
    def test_streaming_response_switch_model(self, client: Opencode) -> None:
        with client.session.with_streaming_response.switch_model(
            session_id={},
            model={},
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
                model={},
            )

    @parametrize
    def test_method_synthetic(self, client: Opencode) -> None:
        session = client.session.synthetic(
            session_id={},
            text="text",
        )
        assert_matches_type(SessionSyntheticResponse, session, path=["response"])

    @parametrize
    def test_method_synthetic_with_all_params(self, client: Opencode) -> None:
        session = client.session.synthetic(
            session_id={},
            text="text",
            delivery={},
            description="description",
            id={},
            metadata={"foo": {}},
            resume=True,
        )
        assert_matches_type(SessionSyntheticResponse, session, path=["response"])

    @parametrize
    def test_raw_response_synthetic(self, client: Opencode) -> None:
        response = client.session.with_raw_response.synthetic(
            session_id={},
            text="text",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = response.parse()
        assert_matches_type(SessionSyntheticResponse, session, path=["response"])

    @parametrize
    def test_streaming_response_synthetic(self, client: Opencode) -> None:
        with client.session.with_streaming_response.synthetic(
            session_id={},
            text="text",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = response.parse()
            assert_matches_type(SessionSyntheticResponse, session, path=["response"])

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
            session_id={},
            idle=0,
        )
        assert session is None

    @parametrize
    def test_raw_response_view(self, client: Opencode) -> None:
        response = client.session.with_raw_response.view(
            session_id={},
            idle=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = response.parse()
        assert session is None

    @parametrize
    def test_streaming_response_view(self, client: Opencode) -> None:
        with client.session.with_streaming_response.view(
            session_id={},
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
            {},
        )
        assert session is None

    @parametrize
    def test_raw_response_wait(self, client: Opencode) -> None:
        response = client.session.with_raw_response.wait(
            {},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = response.parse()
        assert session is None

    @parametrize
    def test_streaming_response_wait(self, client: Opencode) -> None:
        with client.session.with_streaming_response.wait(
            {},
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
        assert_matches_type(SessionCreateResponse, session, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncOpencode) -> None:
        session = await async_client.session.create(
            agent={},
            id={},
            location={},
            metadata={},
            model={},
            parent_id={},
            permissions={},
            title="title",
        )
        assert_matches_type(SessionCreateResponse, session, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncOpencode) -> None:
        response = await async_client.session.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = await response.parse()
        assert_matches_type(SessionCreateResponse, session, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncOpencode) -> None:
        async with async_client.session.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = await response.parse()
            assert_matches_type(SessionCreateResponse, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_update(self, async_client: AsyncOpencode) -> None:
        session = await async_client.session.update(
            session_id={},
        )
        assert session is None

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncOpencode) -> None:
        session = await async_client.session.update(
            session_id={},
            archived=True,
            metadata={},
            permissions={},
            title="title",
        )
        assert session is None

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncOpencode) -> None:
        response = await async_client.session.with_raw_response.update(
            session_id={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = await response.parse()
        assert session is None

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncOpencode) -> None:
        async with async_client.session.with_streaming_response.update(
            session_id={},
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
        assert_matches_type(SessionInfo, session, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncOpencode) -> None:
        session = await async_client.session.list(
            archived=True,
            cursor={},
            directory={},
            limit=0,
            order="asc",
            parent_id={},
            project={},
            search="search",
            subpath={},
        )
        assert_matches_type(SessionInfo, session, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncOpencode) -> None:
        response = await async_client.session.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = await response.parse()
        assert_matches_type(SessionInfo, session, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncOpencode) -> None:
        async with async_client.session.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = await response.parse()
            assert_matches_type(SessionInfo, session, path=["response"])

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
            {},
        )
        assert session is None

    @parametrize
    async def test_raw_response_background(self, async_client: AsyncOpencode) -> None:
        response = await async_client.session.with_raw_response.background(
            {},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = await response.parse()
        assert session is None

    @parametrize
    async def test_streaming_response_background(self, async_client: AsyncOpencode) -> None:
        async with async_client.session.with_streaming_response.background(
            {},
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
            session_id={},
            name="name",
            text="text",
        )
        assert session is None

    @parametrize
    async def test_method_command_with_all_params(self, async_client: AsyncOpencode) -> None:
        session = await async_client.session.command(
            session_id={},
            name="name",
            text="text",
            agents=[{}],
            delivery={},
            files=[{}],
            skills=[{}],
        )
        assert session is None

    @parametrize
    async def test_raw_response_command(self, async_client: AsyncOpencode) -> None:
        response = await async_client.session.with_raw_response.command(
            session_id={},
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
            session_id={},
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
            session_id={},
        )
        assert_matches_type(SessionCompactResponse, session, path=["response"])

    @parametrize
    async def test_method_compact_with_all_params(self, async_client: AsyncOpencode) -> None:
        session = await async_client.session.compact(
            session_id={},
            delivery={},
            id={},
        )
        assert_matches_type(SessionCompactResponse, session, path=["response"])

    @parametrize
    async def test_raw_response_compact(self, async_client: AsyncOpencode) -> None:
        response = await async_client.session.with_raw_response.compact(
            session_id={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = await response.parse()
        assert_matches_type(SessionCompactResponse, session, path=["response"])

    @parametrize
    async def test_streaming_response_compact(self, async_client: AsyncOpencode) -> None:
        async with async_client.session.with_streaming_response.compact(
            session_id={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = await response.parse()
            assert_matches_type(SessionCompactResponse, session, path=["response"])

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
            {},
        )
        assert_matches_type(SessionContextResponse, session, path=["response"])

    @parametrize
    async def test_raw_response_context(self, async_client: AsyncOpencode) -> None:
        response = await async_client.session.with_raw_response.context(
            {},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = await response.parse()
        assert_matches_type(SessionContextResponse, session, path=["response"])

    @parametrize
    async def test_streaming_response_context(self, async_client: AsyncOpencode) -> None:
        async with async_client.session.with_streaming_response.context(
            {},
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
            session_id={},
        )
        assert_matches_type(SessionDiffResponse, session, path=["response"])

    @parametrize
    async def test_method_diff_with_all_params(self, async_client: AsyncOpencode) -> None:
        session = await async_client.session.diff(
            session_id={},
            context=0,
            from_={},
            to={},
        )
        assert_matches_type(SessionDiffResponse, session, path=["response"])

    @parametrize
    async def test_raw_response_diff(self, async_client: AsyncOpencode) -> None:
        response = await async_client.session.with_raw_response.diff(
            session_id={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = await response.parse()
        assert_matches_type(SessionDiffResponse, session, path=["response"])

    @parametrize
    async def test_streaming_response_diff(self, async_client: AsyncOpencode) -> None:
        async with async_client.session.with_streaming_response.diff(
            session_id={},
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
            session_id={},
            variables={"foo": "string"},
        )
        assert session is None

    @parametrize
    async def test_raw_response_environment(self, async_client: AsyncOpencode) -> None:
        response = await async_client.session.with_raw_response.environment(
            session_id={},
            variables={"foo": "string"},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = await response.parse()
        assert session is None

    @parametrize
    async def test_streaming_response_environment(self, async_client: AsyncOpencode) -> None:
        async with async_client.session.with_streaming_response.environment(
            session_id={},
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
            session_id={},
        )
        assert_matches_type(SessionExportResponse, session, path=["response"])

    @parametrize
    async def test_method_export_with_all_params(self, async_client: AsyncOpencode) -> None:
        session = await async_client.session.export(
            session_id={},
            sanitize=True,
        )
        assert_matches_type(SessionExportResponse, session, path=["response"])

    @parametrize
    async def test_raw_response_export(self, async_client: AsyncOpencode) -> None:
        response = await async_client.session.with_raw_response.export(
            session_id={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = await response.parse()
        assert_matches_type(SessionExportResponse, session, path=["response"])

    @parametrize
    async def test_streaming_response_export(self, async_client: AsyncOpencode) -> None:
        async with async_client.session.with_streaming_response.export(
            session_id={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = await response.parse()
            assert_matches_type(SessionExportResponse, session, path=["response"])

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
            session_id={},
        )
        assert_matches_type(SessionForkResponse, session, path=["response"])

    @parametrize
    async def test_method_fork_with_all_params(self, async_client: AsyncOpencode) -> None:
        session = await async_client.session.fork(
            session_id={},
            before={},
        )
        assert_matches_type(SessionForkResponse, session, path=["response"])

    @parametrize
    async def test_raw_response_fork(self, async_client: AsyncOpencode) -> None:
        response = await async_client.session.with_raw_response.fork(
            session_id={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = await response.parse()
        assert_matches_type(SessionForkResponse, session, path=["response"])

    @parametrize
    async def test_streaming_response_fork(self, async_client: AsyncOpencode) -> None:
        async with async_client.session.with_streaming_response.fork(
            session_id={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = await response.parse()
            assert_matches_type(SessionForkResponse, session, path=["response"])

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
            session_id={},
            prompt="prompt",
        )
        assert_matches_type(SessionGenerateResponse, session, path=["response"])

    @parametrize
    async def test_raw_response_generate(self, async_client: AsyncOpencode) -> None:
        response = await async_client.session.with_raw_response.generate(
            session_id={},
            prompt="prompt",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = await response.parse()
        assert_matches_type(SessionGenerateResponse, session, path=["response"])

    @parametrize
    async def test_streaming_response_generate(self, async_client: AsyncOpencode) -> None:
        async with async_client.session.with_streaming_response.generate(
            session_id={},
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
            {},
        )
        assert_matches_type(SessionGetResponse, session, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncOpencode) -> None:
        response = await async_client.session.with_raw_response.get(
            {},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = await response.parse()
        assert_matches_type(SessionGetResponse, session, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncOpencode) -> None:
        async with async_client.session.with_streaming_response.get(
            {},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = await response.parse()
            assert_matches_type(SessionGetResponse, session, path=["response"])

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
            info={},
            messages=[{}],
        )
        assert_matches_type(SessionImportResponse, session, path=["response"])

    @parametrize
    async def test_method_import__with_all_params(self, async_client: AsyncOpencode) -> None:
        session = await async_client.session.import_(
            info={},
            messages=[{}],
            location={},
        )
        assert_matches_type(SessionImportResponse, session, path=["response"])

    @parametrize
    async def test_raw_response_import_(self, async_client: AsyncOpencode) -> None:
        response = await async_client.session.with_raw_response.import_(
            info={},
            messages=[{}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = await response.parse()
        assert_matches_type(SessionImportResponse, session, path=["response"])

    @parametrize
    async def test_streaming_response_import_(self, async_client: AsyncOpencode) -> None:
        async with async_client.session.with_streaming_response.import_(
            info={},
            messages=[{}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = await response.parse()
            assert_matches_type(SessionImportResponse, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_interrupt(self, async_client: AsyncOpencode) -> None:
        session = await async_client.session.interrupt(
            session_id={},
        )
        assert_matches_type(SessionInterruptResponse, session, path=["response"])

    @parametrize
    async def test_method_interrupt_with_all_params(self, async_client: AsyncOpencode) -> None:
        session = await async_client.session.interrupt(
            session_id={},
            resume=True,
        )
        assert_matches_type(SessionInterruptResponse, session, path=["response"])

    @parametrize
    async def test_raw_response_interrupt(self, async_client: AsyncOpencode) -> None:
        response = await async_client.session.with_raw_response.interrupt(
            session_id={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = await response.parse()
        assert_matches_type(SessionInterruptResponse, session, path=["response"])

    @parametrize
    async def test_streaming_response_interrupt(self, async_client: AsyncOpencode) -> None:
        async with async_client.session.with_streaming_response.interrupt(
            session_id={},
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

    @parametrize
    async def test_method_log(self, async_client: AsyncOpencode) -> None:
        session = await async_client.session.log(
            session_id={},
        )
        assert session is None

    @parametrize
    async def test_method_log_with_all_params(self, async_client: AsyncOpencode) -> None:
        session = await async_client.session.log(
            session_id={},
            after={},
            follow=True,
        )
        assert session is None

    @parametrize
    async def test_raw_response_log(self, async_client: AsyncOpencode) -> None:
        response = await async_client.session.with_raw_response.log(
            session_id={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = await response.parse()
        assert session is None

    @parametrize
    async def test_streaming_response_log(self, async_client: AsyncOpencode) -> None:
        async with async_client.session.with_streaming_response.log(
            session_id={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = await response.parse()
            assert session is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_log(self, async_client: AsyncOpencode) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            await async_client.session.with_raw_response.log(
                session_id="",
            )

    @parametrize
    async def test_method_move(self, async_client: AsyncOpencode) -> None:
        session = await async_client.session.move(
            session_id={},
            directory={},
        )
        assert session is None

    @parametrize
    async def test_method_move_with_all_params(self, async_client: AsyncOpencode) -> None:
        session = await async_client.session.move(
            session_id={},
            directory={},
            delivery={},
        )
        assert session is None

    @parametrize
    async def test_raw_response_move(self, async_client: AsyncOpencode) -> None:
        response = await async_client.session.with_raw_response.move(
            session_id={},
            directory={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = await response.parse()
        assert session is None

    @parametrize
    async def test_streaming_response_move(self, async_client: AsyncOpencode) -> None:
        async with async_client.session.with_streaming_response.move(
            session_id={},
            directory={},
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
                directory={},
            )

    @parametrize
    async def test_method_prompt(self, async_client: AsyncOpencode) -> None:
        session = await async_client.session.prompt(
            session_id={},
            text="text",
        )
        assert_matches_type(SessionPromptResponse, session, path=["response"])

    @parametrize
    async def test_method_prompt_with_all_params(self, async_client: AsyncOpencode) -> None:
        session = await async_client.session.prompt(
            session_id={},
            text="text",
            agents=[{}],
            delivery={},
            files=[{}],
            id={},
            metadata={"foo": {}},
            resume=True,
            skills=[{}],
        )
        assert_matches_type(SessionPromptResponse, session, path=["response"])

    @parametrize
    async def test_raw_response_prompt(self, async_client: AsyncOpencode) -> None:
        response = await async_client.session.with_raw_response.prompt(
            session_id={},
            text="text",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = await response.parse()
        assert_matches_type(SessionPromptResponse, session, path=["response"])

    @parametrize
    async def test_streaming_response_prompt(self, async_client: AsyncOpencode) -> None:
        async with async_client.session.with_streaming_response.prompt(
            session_id={},
            text="text",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = await response.parse()
            assert_matches_type(SessionPromptResponse, session, path=["response"])

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
            {},
        )
        assert session is None

    @parametrize
    async def test_raw_response_remove(self, async_client: AsyncOpencode) -> None:
        response = await async_client.session.with_raw_response.remove(
            {},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = await response.parse()
        assert session is None

    @parametrize
    async def test_streaming_response_remove(self, async_client: AsyncOpencode) -> None:
        async with async_client.session.with_streaming_response.remove(
            {},
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
            session_id={},
            command="command",
        )
        assert session is None

    @parametrize
    async def test_method_shell_with_all_params(self, async_client: AsyncOpencode) -> None:
        session = await async_client.session.shell(
            session_id={},
            command="command",
            id={},
        )
        assert session is None

    @parametrize
    async def test_raw_response_shell(self, async_client: AsyncOpencode) -> None:
        response = await async_client.session.with_raw_response.shell(
            session_id={},
            command="command",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = await response.parse()
        assert session is None

    @parametrize
    async def test_streaming_response_shell(self, async_client: AsyncOpencode) -> None:
        async with async_client.session.with_streaming_response.shell(
            session_id={},
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
            session_id={},
            id={},
        )
        assert session is None

    @parametrize
    async def test_method_skill_with_all_params(self, async_client: AsyncOpencode) -> None:
        session = await async_client.session.skill(
            session_id={},
            id={},
            resume=True,
        )
        assert session is None

    @parametrize
    async def test_raw_response_skill(self, async_client: AsyncOpencode) -> None:
        response = await async_client.session.with_raw_response.skill(
            session_id={},
            id={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = await response.parse()
        assert session is None

    @parametrize
    async def test_streaming_response_skill(self, async_client: AsyncOpencode) -> None:
        async with async_client.session.with_streaming_response.skill(
            session_id={},
            id={},
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
                id={},
            )

    @parametrize
    async def test_method_stats(self, async_client: AsyncOpencode) -> None:
        session = await async_client.session.stats()
        assert_matches_type(SessionStatsResponse, session, path=["response"])

    @parametrize
    async def test_method_stats_with_all_params(self, async_client: AsyncOpencode) -> None:
        session = await async_client.session.stats(
            from_=0,
            project={},
            timezone="timezone",
            to=0,
            tools="none",
        )
        assert_matches_type(SessionStatsResponse, session, path=["response"])

    @parametrize
    async def test_raw_response_stats(self, async_client: AsyncOpencode) -> None:
        response = await async_client.session.with_raw_response.stats()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = await response.parse()
        assert_matches_type(SessionStatsResponse, session, path=["response"])

    @parametrize
    async def test_streaming_response_stats(self, async_client: AsyncOpencode) -> None:
        async with async_client.session.with_streaming_response.stats() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = await response.parse()
            assert_matches_type(SessionStatsResponse, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_switch_agent(self, async_client: AsyncOpencode) -> None:
        session = await async_client.session.switch_agent(
            session_id={},
            agent={},
        )
        assert session is None

    @parametrize
    async def test_raw_response_switch_agent(self, async_client: AsyncOpencode) -> None:
        response = await async_client.session.with_raw_response.switch_agent(
            session_id={},
            agent={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = await response.parse()
        assert session is None

    @parametrize
    async def test_streaming_response_switch_agent(self, async_client: AsyncOpencode) -> None:
        async with async_client.session.with_streaming_response.switch_agent(
            session_id={},
            agent={},
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
                agent={},
            )

    @parametrize
    async def test_method_switch_model(self, async_client: AsyncOpencode) -> None:
        session = await async_client.session.switch_model(
            session_id={},
            model={},
        )
        assert session is None

    @parametrize
    async def test_raw_response_switch_model(self, async_client: AsyncOpencode) -> None:
        response = await async_client.session.with_raw_response.switch_model(
            session_id={},
            model={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = await response.parse()
        assert session is None

    @parametrize
    async def test_streaming_response_switch_model(self, async_client: AsyncOpencode) -> None:
        async with async_client.session.with_streaming_response.switch_model(
            session_id={},
            model={},
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
                model={},
            )

    @parametrize
    async def test_method_synthetic(self, async_client: AsyncOpencode) -> None:
        session = await async_client.session.synthetic(
            session_id={},
            text="text",
        )
        assert_matches_type(SessionSyntheticResponse, session, path=["response"])

    @parametrize
    async def test_method_synthetic_with_all_params(self, async_client: AsyncOpencode) -> None:
        session = await async_client.session.synthetic(
            session_id={},
            text="text",
            delivery={},
            description="description",
            id={},
            metadata={"foo": {}},
            resume=True,
        )
        assert_matches_type(SessionSyntheticResponse, session, path=["response"])

    @parametrize
    async def test_raw_response_synthetic(self, async_client: AsyncOpencode) -> None:
        response = await async_client.session.with_raw_response.synthetic(
            session_id={},
            text="text",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = await response.parse()
        assert_matches_type(SessionSyntheticResponse, session, path=["response"])

    @parametrize
    async def test_streaming_response_synthetic(self, async_client: AsyncOpencode) -> None:
        async with async_client.session.with_streaming_response.synthetic(
            session_id={},
            text="text",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = await response.parse()
            assert_matches_type(SessionSyntheticResponse, session, path=["response"])

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
            session_id={},
            idle=0,
        )
        assert session is None

    @parametrize
    async def test_raw_response_view(self, async_client: AsyncOpencode) -> None:
        response = await async_client.session.with_raw_response.view(
            session_id={},
            idle=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = await response.parse()
        assert session is None

    @parametrize
    async def test_streaming_response_view(self, async_client: AsyncOpencode) -> None:
        async with async_client.session.with_streaming_response.view(
            session_id={},
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
            {},
        )
        assert session is None

    @parametrize
    async def test_raw_response_wait(self, async_client: AsyncOpencode) -> None:
        response = await async_client.session.with_raw_response.wait(
            {},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = await response.parse()
        assert session is None

    @parametrize
    async def test_streaming_response_wait(self, async_client: AsyncOpencode) -> None:
        async with async_client.session.with_streaming_response.wait(
            {},
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
