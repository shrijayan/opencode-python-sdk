# File generated from our OpenAPI spec by Ferrule. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["McpOAuthConfig"]


class McpOAuthConfig(  # type: ignore[call-arg]
    TypedDict,
    total=False,
    extra_items=object,  # pyright: ignore[reportGeneralTypeIssues]
):
    auth_server_metadata_url: str

    callback_port: int

    client_id: str

    client_secret: str

    redirect_uri: str

    scope: str
