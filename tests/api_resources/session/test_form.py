# File generated from our OpenAPI spec by Ferrule. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from opencode import Opencode, AsyncOpencode
from tests.utils import assert_matches_type
from opencode.types.shared import FormInfo, FormDetail
from opencode.types.session import FormListResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestForm:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Opencode) -> None:
        form = client.session.form.create(
            session_id="sessionID",
            fields=[
                {
                    "custom": True,
                    "default": "string",
                    "description": "string",
                    "format": "email",
                    "hidden": True,
                    "key": "string",
                    "maxLength": 0,
                    "minLength": 0,
                    "options": [
                        {
                            "description": "string",
                            "label": "string",
                            "value": "string",
                        }
                    ],
                    "pattern": "string",
                    "placeholder": "string",
                    "required": True,
                    "title": "string",
                    "type": "string",
                    "when": [
                        {
                            "key": "string",
                            "op": "eq",
                            "value": "string",
                        }
                    ],
                }
            ],
            title="title",
        )
        assert_matches_type(FormInfo, form, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Opencode) -> None:
        form = client.session.form.create(
            session_id="sessionID",
            fields=[
                {
                    "custom": True,
                    "default": "string",
                    "description": "string",
                    "format": "email",
                    "hidden": True,
                    "key": "string",
                    "maxLength": 0,
                    "minLength": 0,
                    "options": [
                        {
                            "description": "string",
                            "label": "string",
                            "value": "string",
                        }
                    ],
                    "pattern": "string",
                    "placeholder": "string",
                    "required": True,
                    "title": "string",
                    "type": "string",
                    "when": [
                        {
                            "key": "string",
                            "op": "eq",
                            "value": "string",
                        }
                    ],
                }
            ],
            title="title",
            id="id",
            metadata={"foo": {}},
        )
        assert_matches_type(FormInfo, form, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Opencode) -> None:
        response = client.session.form.with_raw_response.create(
            session_id="sessionID",
            fields=[
                {
                    "custom": True,
                    "default": "string",
                    "description": "string",
                    "format": "email",
                    "hidden": True,
                    "key": "string",
                    "maxLength": 0,
                    "minLength": 0,
                    "options": [
                        {
                            "description": "string",
                            "label": "string",
                            "value": "string",
                        }
                    ],
                    "pattern": "string",
                    "placeholder": "string",
                    "required": True,
                    "title": "string",
                    "type": "string",
                    "when": [
                        {
                            "key": "string",
                            "op": "eq",
                            "value": "string",
                        }
                    ],
                }
            ],
            title="title",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        form = response.parse()
        assert_matches_type(FormInfo, form, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Opencode) -> None:
        with client.session.form.with_streaming_response.create(
            session_id="sessionID",
            fields=[
                {
                    "custom": True,
                    "default": "string",
                    "description": "string",
                    "format": "email",
                    "hidden": True,
                    "key": "string",
                    "maxLength": 0,
                    "minLength": 0,
                    "options": [
                        {
                            "description": "string",
                            "label": "string",
                            "value": "string",
                        }
                    ],
                    "pattern": "string",
                    "placeholder": "string",
                    "required": True,
                    "title": "string",
                    "type": "string",
                    "when": [
                        {
                            "key": "string",
                            "op": "eq",
                            "value": "string",
                        }
                    ],
                }
            ],
            title="title",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            form = response.parse()
            assert_matches_type(FormInfo, form, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: Opencode) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            client.session.form.with_raw_response.create(
                session_id="",
                fields=[
                    {
                        "custom": True,
                        "default": "string",
                        "description": "string",
                        "format": "email",
                        "hidden": True,
                        "key": "string",
                        "maxLength": 0,
                        "minLength": 0,
                        "options": [
                            {
                                "description": "string",
                                "label": "string",
                                "value": "string",
                            }
                        ],
                        "pattern": "string",
                        "placeholder": "string",
                        "required": True,
                        "title": "string",
                        "type": "string",
                        "when": [
                            {
                                "key": "string",
                                "op": "eq",
                                "value": "string",
                            }
                        ],
                    }
                ],
                title="title",
            )

    @parametrize
    def test_method_list(self, client: Opencode) -> None:
        form = client.session.form.list(
            "sessionID",
        )
        assert_matches_type(FormListResponse, form, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Opencode) -> None:
        response = client.session.form.with_raw_response.list(
            "sessionID",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        form = response.parse()
        assert_matches_type(FormListResponse, form, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Opencode) -> None:
        with client.session.form.with_streaming_response.list(
            "sessionID",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            form = response.parse()
            assert_matches_type(FormListResponse, form, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Opencode) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            client.session.form.with_raw_response.list(
                "",
            )

    @parametrize
    def test_method_cancel(self, client: Opencode) -> None:
        form = client.session.form.cancel(
            form_id="formID",
            session_id="sessionID",
        )
        assert form is None

    @parametrize
    def test_method_cancel_with_all_params(self, client: Opencode) -> None:
        form = client.session.form.cancel(
            form_id="formID",
            session_id="sessionID",
            message="message",
        )
        assert form is None

    @parametrize
    def test_raw_response_cancel(self, client: Opencode) -> None:
        response = client.session.form.with_raw_response.cancel(
            form_id="formID",
            session_id="sessionID",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        form = response.parse()
        assert form is None

    @parametrize
    def test_streaming_response_cancel(self, client: Opencode) -> None:
        with client.session.form.with_streaming_response.cancel(
            form_id="formID",
            session_id="sessionID",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            form = response.parse()
            assert form is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_cancel(self, client: Opencode) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            client.session.form.with_raw_response.cancel(
                form_id="formID",
                session_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `form_id` but received ''"):
            client.session.form.with_raw_response.cancel(
                form_id="",
                session_id="sessionID",
            )

    @parametrize
    def test_method_get(self, client: Opencode) -> None:
        form = client.session.form.get(
            form_id="formID",
            session_id="sessionID",
        )
        assert_matches_type(FormDetail, form, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Opencode) -> None:
        response = client.session.form.with_raw_response.get(
            form_id="formID",
            session_id="sessionID",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        form = response.parse()
        assert_matches_type(FormDetail, form, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Opencode) -> None:
        with client.session.form.with_streaming_response.get(
            form_id="formID",
            session_id="sessionID",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            form = response.parse()
            assert_matches_type(FormDetail, form, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Opencode) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            client.session.form.with_raw_response.get(
                form_id="formID",
                session_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `form_id` but received ''"):
            client.session.form.with_raw_response.get(
                form_id="",
                session_id="sessionID",
            )

    @parametrize
    def test_method_reply(self, client: Opencode) -> None:
        form = client.session.form.reply(
            form_id="formID",
            session_id="sessionID",
            answer={"foo": "string"},
        )
        assert form is None

    @parametrize
    def test_raw_response_reply(self, client: Opencode) -> None:
        response = client.session.form.with_raw_response.reply(
            form_id="formID",
            session_id="sessionID",
            answer={"foo": "string"},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        form = response.parse()
        assert form is None

    @parametrize
    def test_streaming_response_reply(self, client: Opencode) -> None:
        with client.session.form.with_streaming_response.reply(
            form_id="formID",
            session_id="sessionID",
            answer={"foo": "string"},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            form = response.parse()
            assert form is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_reply(self, client: Opencode) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            client.session.form.with_raw_response.reply(
                form_id="formID",
                session_id="",
                answer={"foo": "string"},
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `form_id` but received ''"):
            client.session.form.with_raw_response.reply(
                form_id="",
                session_id="sessionID",
                answer={"foo": "string"},
            )


class TestAsyncForm:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncOpencode) -> None:
        form = await async_client.session.form.create(
            session_id="sessionID",
            fields=[
                {
                    "custom": True,
                    "default": "string",
                    "description": "string",
                    "format": "email",
                    "hidden": True,
                    "key": "string",
                    "maxLength": 0,
                    "minLength": 0,
                    "options": [
                        {
                            "description": "string",
                            "label": "string",
                            "value": "string",
                        }
                    ],
                    "pattern": "string",
                    "placeholder": "string",
                    "required": True,
                    "title": "string",
                    "type": "string",
                    "when": [
                        {
                            "key": "string",
                            "op": "eq",
                            "value": "string",
                        }
                    ],
                }
            ],
            title="title",
        )
        assert_matches_type(FormInfo, form, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncOpencode) -> None:
        form = await async_client.session.form.create(
            session_id="sessionID",
            fields=[
                {
                    "custom": True,
                    "default": "string",
                    "description": "string",
                    "format": "email",
                    "hidden": True,
                    "key": "string",
                    "maxLength": 0,
                    "minLength": 0,
                    "options": [
                        {
                            "description": "string",
                            "label": "string",
                            "value": "string",
                        }
                    ],
                    "pattern": "string",
                    "placeholder": "string",
                    "required": True,
                    "title": "string",
                    "type": "string",
                    "when": [
                        {
                            "key": "string",
                            "op": "eq",
                            "value": "string",
                        }
                    ],
                }
            ],
            title="title",
            id="id",
            metadata={"foo": {}},
        )
        assert_matches_type(FormInfo, form, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncOpencode) -> None:
        response = await async_client.session.form.with_raw_response.create(
            session_id="sessionID",
            fields=[
                {
                    "custom": True,
                    "default": "string",
                    "description": "string",
                    "format": "email",
                    "hidden": True,
                    "key": "string",
                    "maxLength": 0,
                    "minLength": 0,
                    "options": [
                        {
                            "description": "string",
                            "label": "string",
                            "value": "string",
                        }
                    ],
                    "pattern": "string",
                    "placeholder": "string",
                    "required": True,
                    "title": "string",
                    "type": "string",
                    "when": [
                        {
                            "key": "string",
                            "op": "eq",
                            "value": "string",
                        }
                    ],
                }
            ],
            title="title",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        form = await response.parse()
        assert_matches_type(FormInfo, form, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncOpencode) -> None:
        async with async_client.session.form.with_streaming_response.create(
            session_id="sessionID",
            fields=[
                {
                    "custom": True,
                    "default": "string",
                    "description": "string",
                    "format": "email",
                    "hidden": True,
                    "key": "string",
                    "maxLength": 0,
                    "minLength": 0,
                    "options": [
                        {
                            "description": "string",
                            "label": "string",
                            "value": "string",
                        }
                    ],
                    "pattern": "string",
                    "placeholder": "string",
                    "required": True,
                    "title": "string",
                    "type": "string",
                    "when": [
                        {
                            "key": "string",
                            "op": "eq",
                            "value": "string",
                        }
                    ],
                }
            ],
            title="title",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            form = await response.parse()
            assert_matches_type(FormInfo, form, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncOpencode) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            await async_client.session.form.with_raw_response.create(
                session_id="",
                fields=[
                    {
                        "custom": True,
                        "default": "string",
                        "description": "string",
                        "format": "email",
                        "hidden": True,
                        "key": "string",
                        "maxLength": 0,
                        "minLength": 0,
                        "options": [
                            {
                                "description": "string",
                                "label": "string",
                                "value": "string",
                            }
                        ],
                        "pattern": "string",
                        "placeholder": "string",
                        "required": True,
                        "title": "string",
                        "type": "string",
                        "when": [
                            {
                                "key": "string",
                                "op": "eq",
                                "value": "string",
                            }
                        ],
                    }
                ],
                title="title",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncOpencode) -> None:
        form = await async_client.session.form.list(
            "sessionID",
        )
        assert_matches_type(FormListResponse, form, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncOpencode) -> None:
        response = await async_client.session.form.with_raw_response.list(
            "sessionID",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        form = await response.parse()
        assert_matches_type(FormListResponse, form, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncOpencode) -> None:
        async with async_client.session.form.with_streaming_response.list(
            "sessionID",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            form = await response.parse()
            assert_matches_type(FormListResponse, form, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncOpencode) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            await async_client.session.form.with_raw_response.list(
                "",
            )

    @parametrize
    async def test_method_cancel(self, async_client: AsyncOpencode) -> None:
        form = await async_client.session.form.cancel(
            form_id="formID",
            session_id="sessionID",
        )
        assert form is None

    @parametrize
    async def test_method_cancel_with_all_params(self, async_client: AsyncOpencode) -> None:
        form = await async_client.session.form.cancel(
            form_id="formID",
            session_id="sessionID",
            message="message",
        )
        assert form is None

    @parametrize
    async def test_raw_response_cancel(self, async_client: AsyncOpencode) -> None:
        response = await async_client.session.form.with_raw_response.cancel(
            form_id="formID",
            session_id="sessionID",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        form = await response.parse()
        assert form is None

    @parametrize
    async def test_streaming_response_cancel(self, async_client: AsyncOpencode) -> None:
        async with async_client.session.form.with_streaming_response.cancel(
            form_id="formID",
            session_id="sessionID",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            form = await response.parse()
            assert form is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_cancel(self, async_client: AsyncOpencode) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            await async_client.session.form.with_raw_response.cancel(
                form_id="formID",
                session_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `form_id` but received ''"):
            await async_client.session.form.with_raw_response.cancel(
                form_id="",
                session_id="sessionID",
            )

    @parametrize
    async def test_method_get(self, async_client: AsyncOpencode) -> None:
        form = await async_client.session.form.get(
            form_id="formID",
            session_id="sessionID",
        )
        assert_matches_type(FormDetail, form, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncOpencode) -> None:
        response = await async_client.session.form.with_raw_response.get(
            form_id="formID",
            session_id="sessionID",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        form = await response.parse()
        assert_matches_type(FormDetail, form, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncOpencode) -> None:
        async with async_client.session.form.with_streaming_response.get(
            form_id="formID",
            session_id="sessionID",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            form = await response.parse()
            assert_matches_type(FormDetail, form, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncOpencode) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            await async_client.session.form.with_raw_response.get(
                form_id="formID",
                session_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `form_id` but received ''"):
            await async_client.session.form.with_raw_response.get(
                form_id="",
                session_id="sessionID",
            )

    @parametrize
    async def test_method_reply(self, async_client: AsyncOpencode) -> None:
        form = await async_client.session.form.reply(
            form_id="formID",
            session_id="sessionID",
            answer={"foo": "string"},
        )
        assert form is None

    @parametrize
    async def test_raw_response_reply(self, async_client: AsyncOpencode) -> None:
        response = await async_client.session.form.with_raw_response.reply(
            form_id="formID",
            session_id="sessionID",
            answer={"foo": "string"},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        form = await response.parse()
        assert form is None

    @parametrize
    async def test_streaming_response_reply(self, async_client: AsyncOpencode) -> None:
        async with async_client.session.form.with_streaming_response.reply(
            form_id="formID",
            session_id="sessionID",
            answer={"foo": "string"},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            form = await response.parse()
            assert form is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_reply(self, async_client: AsyncOpencode) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            await async_client.session.form.with_raw_response.reply(
                form_id="formID",
                session_id="",
                answer={"foo": "string"},
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `form_id` but received ''"):
            await async_client.session.form.with_raw_response.reply(
                form_id="",
                session_id="sessionID",
                answer={"foo": "string"},
            )
