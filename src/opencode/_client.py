# File generated from our OpenAPI spec by Ferrule. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
import base64
from typing import TYPE_CHECKING, Any, Mapping
from typing_extensions import Self, override

import httpx

from . import _exceptions
from ._qs import Querystring
from ._types import (
    Omit,
    Timeout,
    NotGiven,
    Transport,
    ProxiesTypes,
    RequestOptions,
    not_given,
)
from ._utils import (
    is_given,
    is_mapping_t,
    get_async_library,
)
from ._compat import cached_property
from ._version import __version__
from ._streaming import Stream as Stream, AsyncStream as AsyncStream
from ._exceptions import APIStatusError
from ._base_client import (
    DEFAULT_MAX_RETRIES,
    SyncAPIClient,
    AsyncAPIClient,
)

if TYPE_CHECKING:
    from .resources import (
        mcp,
        pty,
        rpc,
        vcs,
        file,
        form,
        agent,
        debug,
        event,
        model,
        shell,
        skill,
        voice,
        config,
        plugin,
        server,
        command,
        message,
        project,
        session,
        generate,
        location,
        provider,
        worktree,
        migration,
        reference,
        websearch,
        credential,
        permission,
        integration,
        experimental,
    )
    from .resources.rpc import RpcResource, AsyncRpcResource
    from .resources.file import FileResource, AsyncFileResource
    from .resources.form import FormResource, AsyncFormResource
    from .resources.agent import AgentResource, AsyncAgentResource
    from .resources.event import EventResource, AsyncEventResource
    from .resources.model import ModelResource, AsyncModelResource
    from .resources.shell import ShellResource, AsyncShellResource
    from .resources.skill import SkillResource, AsyncSkillResource
    from .resources.voice import VoiceResource, AsyncVoiceResource
    from .resources.config import ConfigResource, AsyncConfigResource
    from .resources.plugin import PluginResource, AsyncPluginResource
    from .resources.server import ServerResource, AsyncServerResource
    from .resources.command import CommandResource, AsyncCommandResource
    from .resources.mcp.mcp import McpResource, AsyncMcpResource
    from .resources.message import MessageResource, AsyncMessageResource
    from .resources.project import ProjectResource, AsyncProjectResource
    from .resources.pty.pty import PtyResource, AsyncPtyResource
    from .resources.vcs.vcs import VcsResource, AsyncVcsResource
    from .resources.generate import GenerateResource, AsyncGenerateResource
    from .resources.location import LocationResource, AsyncLocationResource
    from .resources.provider import ProviderResource, AsyncProviderResource
    from .resources.worktree import WorktreeResource, AsyncWorktreeResource
    from .resources.reference import ReferenceResource, AsyncReferenceResource
    from .resources.websearch import WebsearchResource, AsyncWebsearchResource
    from .resources.credential import CredentialResource, AsyncCredentialResource
    from .resources.debug.debug import DebugResource, AsyncDebugResource
    from .resources.session.session import SessionResource, AsyncSessionResource
    from .resources.migration.migration import MigrationResource, AsyncMigrationResource
    from .resources.permission.permission import PermissionResource, AsyncPermissionResource
    from .resources.integration.integration import IntegrationResource, AsyncIntegrationResource
    from .resources.experimental.experimental import ExperimentalResource, AsyncExperimentalResource

__all__ = [
    "Timeout",
    "Transport",
    "ProxiesTypes",
    "RequestOptions",
    "Opencode",
    "AsyncOpencode",
    "Client",
    "AsyncClient",
]


class Opencode(SyncAPIClient):
    # client options
    username: str | None
    password: str | None

    def __init__(
        self,
        *,
        username: str | None = None,
        password: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#client) for more details.
        http_client: httpx.Client | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new synchronous Opencode client instance.

        This automatically infers the `password` argument from the `OPENCODE_PASSWORD` environment variable if it is not provided.
        """
        if username is None:
            username = "opencode"
        self.username = username

        if password is None:
            password = os.environ.get("OPENCODE_PASSWORD")
        self.password = password

        if base_url is None:
            base_url = os.environ.get("OPENCODE_BASE_URL")
        if base_url is None:
            base_url = f"http://127.0.0.1:4096"

        custom_headers_env = os.environ.get("OPENCODE_CUSTOM_HEADERS")
        if custom_headers_env is not None:
            parsed: dict[str, str] = {}
            for line in custom_headers_env.split("\n"):
                colon = line.find(":")
                if colon >= 0:
                    parsed[line[:colon].strip()] = line[colon + 1 :].strip()
            default_headers = {**parsed, **(default_headers if is_mapping_t(default_headers) else {})}

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

    @cached_property
    def agent(self) -> AgentResource:
        from .resources.agent import AgentResource

        return AgentResource(self)

    @cached_property
    def command(self) -> CommandResource:
        from .resources.command import CommandResource

        return CommandResource(self)

    @cached_property
    def config(self) -> ConfigResource:
        from .resources.config import ConfigResource

        return ConfigResource(self)

    @cached_property
    def credential(self) -> CredentialResource:
        from .resources.credential import CredentialResource

        return CredentialResource(self)

    @cached_property
    def debug(self) -> DebugResource:
        from .resources.debug import DebugResource

        return DebugResource(self)

    @cached_property
    def event(self) -> EventResource:
        from .resources.event import EventResource

        return EventResource(self)

    @cached_property
    def experimental(self) -> ExperimentalResource:
        from .resources.experimental import ExperimentalResource

        return ExperimentalResource(self)

    @cached_property
    def file(self) -> FileResource:
        from .resources.file import FileResource

        return FileResource(self)

    @cached_property
    def form(self) -> FormResource:
        from .resources.form import FormResource

        return FormResource(self)

    @cached_property
    def generate(self) -> GenerateResource:
        from .resources.generate import GenerateResource

        return GenerateResource(self)

    @cached_property
    def integration(self) -> IntegrationResource:
        from .resources.integration import IntegrationResource

        return IntegrationResource(self)

    @cached_property
    def location(self) -> LocationResource:
        from .resources.location import LocationResource

        return LocationResource(self)

    @cached_property
    def mcp(self) -> McpResource:
        from .resources.mcp import McpResource

        return McpResource(self)

    @cached_property
    def message(self) -> MessageResource:
        from .resources.message import MessageResource

        return MessageResource(self)

    @cached_property
    def migration(self) -> MigrationResource:
        from .resources.migration import MigrationResource

        return MigrationResource(self)

    @cached_property
    def model(self) -> ModelResource:
        from .resources.model import ModelResource

        return ModelResource(self)

    @cached_property
    def permission(self) -> PermissionResource:
        from .resources.permission import PermissionResource

        return PermissionResource(self)

    @cached_property
    def plugin(self) -> PluginResource:
        from .resources.plugin import PluginResource

        return PluginResource(self)

    @cached_property
    def project(self) -> ProjectResource:
        from .resources.project import ProjectResource

        return ProjectResource(self)

    @cached_property
    def provider(self) -> ProviderResource:
        from .resources.provider import ProviderResource

        return ProviderResource(self)

    @cached_property
    def pty(self) -> PtyResource:
        from .resources.pty import PtyResource

        return PtyResource(self)

    @cached_property
    def reference(self) -> ReferenceResource:
        from .resources.reference import ReferenceResource

        return ReferenceResource(self)

    @cached_property
    def rpc(self) -> RpcResource:
        from .resources.rpc import RpcResource

        return RpcResource(self)

    @cached_property
    def server(self) -> ServerResource:
        from .resources.server import ServerResource

        return ServerResource(self)

    @cached_property
    def session(self) -> SessionResource:
        from .resources.session import SessionResource

        return SessionResource(self)

    @cached_property
    def shell(self) -> ShellResource:
        from .resources.shell import ShellResource

        return ShellResource(self)

    @cached_property
    def skill(self) -> SkillResource:
        from .resources.skill import SkillResource

        return SkillResource(self)

    @cached_property
    def vcs(self) -> VcsResource:
        from .resources.vcs import VcsResource

        return VcsResource(self)

    @cached_property
    def voice(self) -> VoiceResource:
        from .resources.voice import VoiceResource

        return VoiceResource(self)

    @cached_property
    def websearch(self) -> WebsearchResource:
        from .resources.websearch import WebsearchResource

        return WebsearchResource(self)

    @cached_property
    def worktree(self) -> WorktreeResource:
        from .resources.worktree import WorktreeResource

        return WorktreeResource(self)

    @cached_property
    def with_raw_response(self) -> OpencodeWithRawResponse:
        return OpencodeWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> OpencodeWithStreamedResponse:
        return OpencodeWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="repeat")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        if self.username is None or self.password is None:
            return {}
        credentials = f"{self.username}:{self.password}".encode("ascii")
        header = f"Basic {base64.b64encode(credentials).decode('ascii')}"
        return {"Authorization": header}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": "false",
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        username: str | None = None,
        password: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        http_client: httpx.Client | None = None,
        max_retries: int | NotGiven = not_given,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            username=username or self.username,
            password=password or self.password,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class AsyncOpencode(AsyncAPIClient):
    # client options
    username: str | None
    password: str | None

    def __init__(
        self,
        *,
        username: str | None = None,
        password: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultAsyncHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#asyncclient) for more details.
        http_client: httpx.AsyncClient | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new async AsyncOpencode client instance.

        This automatically infers the `password` argument from the `OPENCODE_PASSWORD` environment variable if it is not provided.
        """
        if username is None:
            username = "opencode"
        self.username = username

        if password is None:
            password = os.environ.get("OPENCODE_PASSWORD")
        self.password = password

        if base_url is None:
            base_url = os.environ.get("OPENCODE_BASE_URL")
        if base_url is None:
            base_url = f"http://127.0.0.1:4096"

        custom_headers_env = os.environ.get("OPENCODE_CUSTOM_HEADERS")
        if custom_headers_env is not None:
            parsed: dict[str, str] = {}
            for line in custom_headers_env.split("\n"):
                colon = line.find(":")
                if colon >= 0:
                    parsed[line[:colon].strip()] = line[colon + 1 :].strip()
            default_headers = {**parsed, **(default_headers if is_mapping_t(default_headers) else {})}

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

    @cached_property
    def agent(self) -> AsyncAgentResource:
        from .resources.agent import AsyncAgentResource

        return AsyncAgentResource(self)

    @cached_property
    def command(self) -> AsyncCommandResource:
        from .resources.command import AsyncCommandResource

        return AsyncCommandResource(self)

    @cached_property
    def config(self) -> AsyncConfigResource:
        from .resources.config import AsyncConfigResource

        return AsyncConfigResource(self)

    @cached_property
    def credential(self) -> AsyncCredentialResource:
        from .resources.credential import AsyncCredentialResource

        return AsyncCredentialResource(self)

    @cached_property
    def debug(self) -> AsyncDebugResource:
        from .resources.debug import AsyncDebugResource

        return AsyncDebugResource(self)

    @cached_property
    def event(self) -> AsyncEventResource:
        from .resources.event import AsyncEventResource

        return AsyncEventResource(self)

    @cached_property
    def experimental(self) -> AsyncExperimentalResource:
        from .resources.experimental import AsyncExperimentalResource

        return AsyncExperimentalResource(self)

    @cached_property
    def file(self) -> AsyncFileResource:
        from .resources.file import AsyncFileResource

        return AsyncFileResource(self)

    @cached_property
    def form(self) -> AsyncFormResource:
        from .resources.form import AsyncFormResource

        return AsyncFormResource(self)

    @cached_property
    def generate(self) -> AsyncGenerateResource:
        from .resources.generate import AsyncGenerateResource

        return AsyncGenerateResource(self)

    @cached_property
    def integration(self) -> AsyncIntegrationResource:
        from .resources.integration import AsyncIntegrationResource

        return AsyncIntegrationResource(self)

    @cached_property
    def location(self) -> AsyncLocationResource:
        from .resources.location import AsyncLocationResource

        return AsyncLocationResource(self)

    @cached_property
    def mcp(self) -> AsyncMcpResource:
        from .resources.mcp import AsyncMcpResource

        return AsyncMcpResource(self)

    @cached_property
    def message(self) -> AsyncMessageResource:
        from .resources.message import AsyncMessageResource

        return AsyncMessageResource(self)

    @cached_property
    def migration(self) -> AsyncMigrationResource:
        from .resources.migration import AsyncMigrationResource

        return AsyncMigrationResource(self)

    @cached_property
    def model(self) -> AsyncModelResource:
        from .resources.model import AsyncModelResource

        return AsyncModelResource(self)

    @cached_property
    def permission(self) -> AsyncPermissionResource:
        from .resources.permission import AsyncPermissionResource

        return AsyncPermissionResource(self)

    @cached_property
    def plugin(self) -> AsyncPluginResource:
        from .resources.plugin import AsyncPluginResource

        return AsyncPluginResource(self)

    @cached_property
    def project(self) -> AsyncProjectResource:
        from .resources.project import AsyncProjectResource

        return AsyncProjectResource(self)

    @cached_property
    def provider(self) -> AsyncProviderResource:
        from .resources.provider import AsyncProviderResource

        return AsyncProviderResource(self)

    @cached_property
    def pty(self) -> AsyncPtyResource:
        from .resources.pty import AsyncPtyResource

        return AsyncPtyResource(self)

    @cached_property
    def reference(self) -> AsyncReferenceResource:
        from .resources.reference import AsyncReferenceResource

        return AsyncReferenceResource(self)

    @cached_property
    def rpc(self) -> AsyncRpcResource:
        from .resources.rpc import AsyncRpcResource

        return AsyncRpcResource(self)

    @cached_property
    def server(self) -> AsyncServerResource:
        from .resources.server import AsyncServerResource

        return AsyncServerResource(self)

    @cached_property
    def session(self) -> AsyncSessionResource:
        from .resources.session import AsyncSessionResource

        return AsyncSessionResource(self)

    @cached_property
    def shell(self) -> AsyncShellResource:
        from .resources.shell import AsyncShellResource

        return AsyncShellResource(self)

    @cached_property
    def skill(self) -> AsyncSkillResource:
        from .resources.skill import AsyncSkillResource

        return AsyncSkillResource(self)

    @cached_property
    def vcs(self) -> AsyncVcsResource:
        from .resources.vcs import AsyncVcsResource

        return AsyncVcsResource(self)

    @cached_property
    def voice(self) -> AsyncVoiceResource:
        from .resources.voice import AsyncVoiceResource

        return AsyncVoiceResource(self)

    @cached_property
    def websearch(self) -> AsyncWebsearchResource:
        from .resources.websearch import AsyncWebsearchResource

        return AsyncWebsearchResource(self)

    @cached_property
    def worktree(self) -> AsyncWorktreeResource:
        from .resources.worktree import AsyncWorktreeResource

        return AsyncWorktreeResource(self)

    @cached_property
    def with_raw_response(self) -> AsyncOpencodeWithRawResponse:
        return AsyncOpencodeWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncOpencodeWithStreamedResponse:
        return AsyncOpencodeWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="repeat")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        if self.username is None or self.password is None:
            return {}
        credentials = f"{self.username}:{self.password}".encode("ascii")
        header = f"Basic {base64.b64encode(credentials).decode('ascii')}"
        return {"Authorization": header}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": f"async:{get_async_library()}",
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        username: str | None = None,
        password: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        http_client: httpx.AsyncClient | None = None,
        max_retries: int | NotGiven = not_given,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            username=username or self.username,
            password=password or self.password,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class OpencodeWithRawResponse:
    _client: Opencode

    def __init__(self, client: Opencode) -> None:
        self._client = client

    @cached_property
    def agent(self) -> agent.AgentResourceWithRawResponse:
        from .resources.agent import AgentResourceWithRawResponse

        return AgentResourceWithRawResponse(self._client.agent)

    @cached_property
    def command(self) -> command.CommandResourceWithRawResponse:
        from .resources.command import CommandResourceWithRawResponse

        return CommandResourceWithRawResponse(self._client.command)

    @cached_property
    def config(self) -> config.ConfigResourceWithRawResponse:
        from .resources.config import ConfigResourceWithRawResponse

        return ConfigResourceWithRawResponse(self._client.config)

    @cached_property
    def credential(self) -> credential.CredentialResourceWithRawResponse:
        from .resources.credential import CredentialResourceWithRawResponse

        return CredentialResourceWithRawResponse(self._client.credential)

    @cached_property
    def debug(self) -> debug.DebugResourceWithRawResponse:
        from .resources.debug import DebugResourceWithRawResponse

        return DebugResourceWithRawResponse(self._client.debug)

    @cached_property
    def event(self) -> event.EventResourceWithRawResponse:
        from .resources.event import EventResourceWithRawResponse

        return EventResourceWithRawResponse(self._client.event)

    @cached_property
    def experimental(self) -> experimental.ExperimentalResourceWithRawResponse:
        from .resources.experimental import ExperimentalResourceWithRawResponse

        return ExperimentalResourceWithRawResponse(self._client.experimental)

    @cached_property
    def file(self) -> file.FileResourceWithRawResponse:
        from .resources.file import FileResourceWithRawResponse

        return FileResourceWithRawResponse(self._client.file)

    @cached_property
    def form(self) -> form.FormResourceWithRawResponse:
        from .resources.form import FormResourceWithRawResponse

        return FormResourceWithRawResponse(self._client.form)

    @cached_property
    def generate(self) -> generate.GenerateResourceWithRawResponse:
        from .resources.generate import GenerateResourceWithRawResponse

        return GenerateResourceWithRawResponse(self._client.generate)

    @cached_property
    def integration(self) -> integration.IntegrationResourceWithRawResponse:
        from .resources.integration import IntegrationResourceWithRawResponse

        return IntegrationResourceWithRawResponse(self._client.integration)

    @cached_property
    def location(self) -> location.LocationResourceWithRawResponse:
        from .resources.location import LocationResourceWithRawResponse

        return LocationResourceWithRawResponse(self._client.location)

    @cached_property
    def mcp(self) -> mcp.McpResourceWithRawResponse:
        from .resources.mcp import McpResourceWithRawResponse

        return McpResourceWithRawResponse(self._client.mcp)

    @cached_property
    def message(self) -> message.MessageResourceWithRawResponse:
        from .resources.message import MessageResourceWithRawResponse

        return MessageResourceWithRawResponse(self._client.message)

    @cached_property
    def migration(self) -> migration.MigrationResourceWithRawResponse:
        from .resources.migration import MigrationResourceWithRawResponse

        return MigrationResourceWithRawResponse(self._client.migration)

    @cached_property
    def model(self) -> model.ModelResourceWithRawResponse:
        from .resources.model import ModelResourceWithRawResponse

        return ModelResourceWithRawResponse(self._client.model)

    @cached_property
    def permission(self) -> permission.PermissionResourceWithRawResponse:
        from .resources.permission import PermissionResourceWithRawResponse

        return PermissionResourceWithRawResponse(self._client.permission)

    @cached_property
    def plugin(self) -> plugin.PluginResourceWithRawResponse:
        from .resources.plugin import PluginResourceWithRawResponse

        return PluginResourceWithRawResponse(self._client.plugin)

    @cached_property
    def project(self) -> project.ProjectResourceWithRawResponse:
        from .resources.project import ProjectResourceWithRawResponse

        return ProjectResourceWithRawResponse(self._client.project)

    @cached_property
    def provider(self) -> provider.ProviderResourceWithRawResponse:
        from .resources.provider import ProviderResourceWithRawResponse

        return ProviderResourceWithRawResponse(self._client.provider)

    @cached_property
    def pty(self) -> pty.PtyResourceWithRawResponse:
        from .resources.pty import PtyResourceWithRawResponse

        return PtyResourceWithRawResponse(self._client.pty)

    @cached_property
    def reference(self) -> reference.ReferenceResourceWithRawResponse:
        from .resources.reference import ReferenceResourceWithRawResponse

        return ReferenceResourceWithRawResponse(self._client.reference)

    @cached_property
    def rpc(self) -> rpc.RpcResourceWithRawResponse:
        from .resources.rpc import RpcResourceWithRawResponse

        return RpcResourceWithRawResponse(self._client.rpc)

    @cached_property
    def server(self) -> server.ServerResourceWithRawResponse:
        from .resources.server import ServerResourceWithRawResponse

        return ServerResourceWithRawResponse(self._client.server)

    @cached_property
    def session(self) -> session.SessionResourceWithRawResponse:
        from .resources.session import SessionResourceWithRawResponse

        return SessionResourceWithRawResponse(self._client.session)

    @cached_property
    def shell(self) -> shell.ShellResourceWithRawResponse:
        from .resources.shell import ShellResourceWithRawResponse

        return ShellResourceWithRawResponse(self._client.shell)

    @cached_property
    def skill(self) -> skill.SkillResourceWithRawResponse:
        from .resources.skill import SkillResourceWithRawResponse

        return SkillResourceWithRawResponse(self._client.skill)

    @cached_property
    def vcs(self) -> vcs.VcsResourceWithRawResponse:
        from .resources.vcs import VcsResourceWithRawResponse

        return VcsResourceWithRawResponse(self._client.vcs)

    @cached_property
    def voice(self) -> voice.VoiceResourceWithRawResponse:
        from .resources.voice import VoiceResourceWithRawResponse

        return VoiceResourceWithRawResponse(self._client.voice)

    @cached_property
    def websearch(self) -> websearch.WebsearchResourceWithRawResponse:
        from .resources.websearch import WebsearchResourceWithRawResponse

        return WebsearchResourceWithRawResponse(self._client.websearch)

    @cached_property
    def worktree(self) -> worktree.WorktreeResourceWithRawResponse:
        from .resources.worktree import WorktreeResourceWithRawResponse

        return WorktreeResourceWithRawResponse(self._client.worktree)


class AsyncOpencodeWithRawResponse:
    _client: AsyncOpencode

    def __init__(self, client: AsyncOpencode) -> None:
        self._client = client

    @cached_property
    def agent(self) -> agent.AsyncAgentResourceWithRawResponse:
        from .resources.agent import AsyncAgentResourceWithRawResponse

        return AsyncAgentResourceWithRawResponse(self._client.agent)

    @cached_property
    def command(self) -> command.AsyncCommandResourceWithRawResponse:
        from .resources.command import AsyncCommandResourceWithRawResponse

        return AsyncCommandResourceWithRawResponse(self._client.command)

    @cached_property
    def config(self) -> config.AsyncConfigResourceWithRawResponse:
        from .resources.config import AsyncConfigResourceWithRawResponse

        return AsyncConfigResourceWithRawResponse(self._client.config)

    @cached_property
    def credential(self) -> credential.AsyncCredentialResourceWithRawResponse:
        from .resources.credential import AsyncCredentialResourceWithRawResponse

        return AsyncCredentialResourceWithRawResponse(self._client.credential)

    @cached_property
    def debug(self) -> debug.AsyncDebugResourceWithRawResponse:
        from .resources.debug import AsyncDebugResourceWithRawResponse

        return AsyncDebugResourceWithRawResponse(self._client.debug)

    @cached_property
    def event(self) -> event.AsyncEventResourceWithRawResponse:
        from .resources.event import AsyncEventResourceWithRawResponse

        return AsyncEventResourceWithRawResponse(self._client.event)

    @cached_property
    def experimental(self) -> experimental.AsyncExperimentalResourceWithRawResponse:
        from .resources.experimental import AsyncExperimentalResourceWithRawResponse

        return AsyncExperimentalResourceWithRawResponse(self._client.experimental)

    @cached_property
    def file(self) -> file.AsyncFileResourceWithRawResponse:
        from .resources.file import AsyncFileResourceWithRawResponse

        return AsyncFileResourceWithRawResponse(self._client.file)

    @cached_property
    def form(self) -> form.AsyncFormResourceWithRawResponse:
        from .resources.form import AsyncFormResourceWithRawResponse

        return AsyncFormResourceWithRawResponse(self._client.form)

    @cached_property
    def generate(self) -> generate.AsyncGenerateResourceWithRawResponse:
        from .resources.generate import AsyncGenerateResourceWithRawResponse

        return AsyncGenerateResourceWithRawResponse(self._client.generate)

    @cached_property
    def integration(self) -> integration.AsyncIntegrationResourceWithRawResponse:
        from .resources.integration import AsyncIntegrationResourceWithRawResponse

        return AsyncIntegrationResourceWithRawResponse(self._client.integration)

    @cached_property
    def location(self) -> location.AsyncLocationResourceWithRawResponse:
        from .resources.location import AsyncLocationResourceWithRawResponse

        return AsyncLocationResourceWithRawResponse(self._client.location)

    @cached_property
    def mcp(self) -> mcp.AsyncMcpResourceWithRawResponse:
        from .resources.mcp import AsyncMcpResourceWithRawResponse

        return AsyncMcpResourceWithRawResponse(self._client.mcp)

    @cached_property
    def message(self) -> message.AsyncMessageResourceWithRawResponse:
        from .resources.message import AsyncMessageResourceWithRawResponse

        return AsyncMessageResourceWithRawResponse(self._client.message)

    @cached_property
    def migration(self) -> migration.AsyncMigrationResourceWithRawResponse:
        from .resources.migration import AsyncMigrationResourceWithRawResponse

        return AsyncMigrationResourceWithRawResponse(self._client.migration)

    @cached_property
    def model(self) -> model.AsyncModelResourceWithRawResponse:
        from .resources.model import AsyncModelResourceWithRawResponse

        return AsyncModelResourceWithRawResponse(self._client.model)

    @cached_property
    def permission(self) -> permission.AsyncPermissionResourceWithRawResponse:
        from .resources.permission import AsyncPermissionResourceWithRawResponse

        return AsyncPermissionResourceWithRawResponse(self._client.permission)

    @cached_property
    def plugin(self) -> plugin.AsyncPluginResourceWithRawResponse:
        from .resources.plugin import AsyncPluginResourceWithRawResponse

        return AsyncPluginResourceWithRawResponse(self._client.plugin)

    @cached_property
    def project(self) -> project.AsyncProjectResourceWithRawResponse:
        from .resources.project import AsyncProjectResourceWithRawResponse

        return AsyncProjectResourceWithRawResponse(self._client.project)

    @cached_property
    def provider(self) -> provider.AsyncProviderResourceWithRawResponse:
        from .resources.provider import AsyncProviderResourceWithRawResponse

        return AsyncProviderResourceWithRawResponse(self._client.provider)

    @cached_property
    def pty(self) -> pty.AsyncPtyResourceWithRawResponse:
        from .resources.pty import AsyncPtyResourceWithRawResponse

        return AsyncPtyResourceWithRawResponse(self._client.pty)

    @cached_property
    def reference(self) -> reference.AsyncReferenceResourceWithRawResponse:
        from .resources.reference import AsyncReferenceResourceWithRawResponse

        return AsyncReferenceResourceWithRawResponse(self._client.reference)

    @cached_property
    def rpc(self) -> rpc.AsyncRpcResourceWithRawResponse:
        from .resources.rpc import AsyncRpcResourceWithRawResponse

        return AsyncRpcResourceWithRawResponse(self._client.rpc)

    @cached_property
    def server(self) -> server.AsyncServerResourceWithRawResponse:
        from .resources.server import AsyncServerResourceWithRawResponse

        return AsyncServerResourceWithRawResponse(self._client.server)

    @cached_property
    def session(self) -> session.AsyncSessionResourceWithRawResponse:
        from .resources.session import AsyncSessionResourceWithRawResponse

        return AsyncSessionResourceWithRawResponse(self._client.session)

    @cached_property
    def shell(self) -> shell.AsyncShellResourceWithRawResponse:
        from .resources.shell import AsyncShellResourceWithRawResponse

        return AsyncShellResourceWithRawResponse(self._client.shell)

    @cached_property
    def skill(self) -> skill.AsyncSkillResourceWithRawResponse:
        from .resources.skill import AsyncSkillResourceWithRawResponse

        return AsyncSkillResourceWithRawResponse(self._client.skill)

    @cached_property
    def vcs(self) -> vcs.AsyncVcsResourceWithRawResponse:
        from .resources.vcs import AsyncVcsResourceWithRawResponse

        return AsyncVcsResourceWithRawResponse(self._client.vcs)

    @cached_property
    def voice(self) -> voice.AsyncVoiceResourceWithRawResponse:
        from .resources.voice import AsyncVoiceResourceWithRawResponse

        return AsyncVoiceResourceWithRawResponse(self._client.voice)

    @cached_property
    def websearch(self) -> websearch.AsyncWebsearchResourceWithRawResponse:
        from .resources.websearch import AsyncWebsearchResourceWithRawResponse

        return AsyncWebsearchResourceWithRawResponse(self._client.websearch)

    @cached_property
    def worktree(self) -> worktree.AsyncWorktreeResourceWithRawResponse:
        from .resources.worktree import AsyncWorktreeResourceWithRawResponse

        return AsyncWorktreeResourceWithRawResponse(self._client.worktree)


class OpencodeWithStreamedResponse:
    _client: Opencode

    def __init__(self, client: Opencode) -> None:
        self._client = client

    @cached_property
    def agent(self) -> agent.AgentResourceWithStreamingResponse:
        from .resources.agent import AgentResourceWithStreamingResponse

        return AgentResourceWithStreamingResponse(self._client.agent)

    @cached_property
    def command(self) -> command.CommandResourceWithStreamingResponse:
        from .resources.command import CommandResourceWithStreamingResponse

        return CommandResourceWithStreamingResponse(self._client.command)

    @cached_property
    def config(self) -> config.ConfigResourceWithStreamingResponse:
        from .resources.config import ConfigResourceWithStreamingResponse

        return ConfigResourceWithStreamingResponse(self._client.config)

    @cached_property
    def credential(self) -> credential.CredentialResourceWithStreamingResponse:
        from .resources.credential import CredentialResourceWithStreamingResponse

        return CredentialResourceWithStreamingResponse(self._client.credential)

    @cached_property
    def debug(self) -> debug.DebugResourceWithStreamingResponse:
        from .resources.debug import DebugResourceWithStreamingResponse

        return DebugResourceWithStreamingResponse(self._client.debug)

    @cached_property
    def event(self) -> event.EventResourceWithStreamingResponse:
        from .resources.event import EventResourceWithStreamingResponse

        return EventResourceWithStreamingResponse(self._client.event)

    @cached_property
    def experimental(self) -> experimental.ExperimentalResourceWithStreamingResponse:
        from .resources.experimental import ExperimentalResourceWithStreamingResponse

        return ExperimentalResourceWithStreamingResponse(self._client.experimental)

    @cached_property
    def file(self) -> file.FileResourceWithStreamingResponse:
        from .resources.file import FileResourceWithStreamingResponse

        return FileResourceWithStreamingResponse(self._client.file)

    @cached_property
    def form(self) -> form.FormResourceWithStreamingResponse:
        from .resources.form import FormResourceWithStreamingResponse

        return FormResourceWithStreamingResponse(self._client.form)

    @cached_property
    def generate(self) -> generate.GenerateResourceWithStreamingResponse:
        from .resources.generate import GenerateResourceWithStreamingResponse

        return GenerateResourceWithStreamingResponse(self._client.generate)

    @cached_property
    def integration(self) -> integration.IntegrationResourceWithStreamingResponse:
        from .resources.integration import IntegrationResourceWithStreamingResponse

        return IntegrationResourceWithStreamingResponse(self._client.integration)

    @cached_property
    def location(self) -> location.LocationResourceWithStreamingResponse:
        from .resources.location import LocationResourceWithStreamingResponse

        return LocationResourceWithStreamingResponse(self._client.location)

    @cached_property
    def mcp(self) -> mcp.McpResourceWithStreamingResponse:
        from .resources.mcp import McpResourceWithStreamingResponse

        return McpResourceWithStreamingResponse(self._client.mcp)

    @cached_property
    def message(self) -> message.MessageResourceWithStreamingResponse:
        from .resources.message import MessageResourceWithStreamingResponse

        return MessageResourceWithStreamingResponse(self._client.message)

    @cached_property
    def migration(self) -> migration.MigrationResourceWithStreamingResponse:
        from .resources.migration import MigrationResourceWithStreamingResponse

        return MigrationResourceWithStreamingResponse(self._client.migration)

    @cached_property
    def model(self) -> model.ModelResourceWithStreamingResponse:
        from .resources.model import ModelResourceWithStreamingResponse

        return ModelResourceWithStreamingResponse(self._client.model)

    @cached_property
    def permission(self) -> permission.PermissionResourceWithStreamingResponse:
        from .resources.permission import PermissionResourceWithStreamingResponse

        return PermissionResourceWithStreamingResponse(self._client.permission)

    @cached_property
    def plugin(self) -> plugin.PluginResourceWithStreamingResponse:
        from .resources.plugin import PluginResourceWithStreamingResponse

        return PluginResourceWithStreamingResponse(self._client.plugin)

    @cached_property
    def project(self) -> project.ProjectResourceWithStreamingResponse:
        from .resources.project import ProjectResourceWithStreamingResponse

        return ProjectResourceWithStreamingResponse(self._client.project)

    @cached_property
    def provider(self) -> provider.ProviderResourceWithStreamingResponse:
        from .resources.provider import ProviderResourceWithStreamingResponse

        return ProviderResourceWithStreamingResponse(self._client.provider)

    @cached_property
    def pty(self) -> pty.PtyResourceWithStreamingResponse:
        from .resources.pty import PtyResourceWithStreamingResponse

        return PtyResourceWithStreamingResponse(self._client.pty)

    @cached_property
    def reference(self) -> reference.ReferenceResourceWithStreamingResponse:
        from .resources.reference import ReferenceResourceWithStreamingResponse

        return ReferenceResourceWithStreamingResponse(self._client.reference)

    @cached_property
    def rpc(self) -> rpc.RpcResourceWithStreamingResponse:
        from .resources.rpc import RpcResourceWithStreamingResponse

        return RpcResourceWithStreamingResponse(self._client.rpc)

    @cached_property
    def server(self) -> server.ServerResourceWithStreamingResponse:
        from .resources.server import ServerResourceWithStreamingResponse

        return ServerResourceWithStreamingResponse(self._client.server)

    @cached_property
    def session(self) -> session.SessionResourceWithStreamingResponse:
        from .resources.session import SessionResourceWithStreamingResponse

        return SessionResourceWithStreamingResponse(self._client.session)

    @cached_property
    def shell(self) -> shell.ShellResourceWithStreamingResponse:
        from .resources.shell import ShellResourceWithStreamingResponse

        return ShellResourceWithStreamingResponse(self._client.shell)

    @cached_property
    def skill(self) -> skill.SkillResourceWithStreamingResponse:
        from .resources.skill import SkillResourceWithStreamingResponse

        return SkillResourceWithStreamingResponse(self._client.skill)

    @cached_property
    def vcs(self) -> vcs.VcsResourceWithStreamingResponse:
        from .resources.vcs import VcsResourceWithStreamingResponse

        return VcsResourceWithStreamingResponse(self._client.vcs)

    @cached_property
    def voice(self) -> voice.VoiceResourceWithStreamingResponse:
        from .resources.voice import VoiceResourceWithStreamingResponse

        return VoiceResourceWithStreamingResponse(self._client.voice)

    @cached_property
    def websearch(self) -> websearch.WebsearchResourceWithStreamingResponse:
        from .resources.websearch import WebsearchResourceWithStreamingResponse

        return WebsearchResourceWithStreamingResponse(self._client.websearch)

    @cached_property
    def worktree(self) -> worktree.WorktreeResourceWithStreamingResponse:
        from .resources.worktree import WorktreeResourceWithStreamingResponse

        return WorktreeResourceWithStreamingResponse(self._client.worktree)


class AsyncOpencodeWithStreamedResponse:
    _client: AsyncOpencode

    def __init__(self, client: AsyncOpencode) -> None:
        self._client = client

    @cached_property
    def agent(self) -> agent.AsyncAgentResourceWithStreamingResponse:
        from .resources.agent import AsyncAgentResourceWithStreamingResponse

        return AsyncAgentResourceWithStreamingResponse(self._client.agent)

    @cached_property
    def command(self) -> command.AsyncCommandResourceWithStreamingResponse:
        from .resources.command import AsyncCommandResourceWithStreamingResponse

        return AsyncCommandResourceWithStreamingResponse(self._client.command)

    @cached_property
    def config(self) -> config.AsyncConfigResourceWithStreamingResponse:
        from .resources.config import AsyncConfigResourceWithStreamingResponse

        return AsyncConfigResourceWithStreamingResponse(self._client.config)

    @cached_property
    def credential(self) -> credential.AsyncCredentialResourceWithStreamingResponse:
        from .resources.credential import AsyncCredentialResourceWithStreamingResponse

        return AsyncCredentialResourceWithStreamingResponse(self._client.credential)

    @cached_property
    def debug(self) -> debug.AsyncDebugResourceWithStreamingResponse:
        from .resources.debug import AsyncDebugResourceWithStreamingResponse

        return AsyncDebugResourceWithStreamingResponse(self._client.debug)

    @cached_property
    def event(self) -> event.AsyncEventResourceWithStreamingResponse:
        from .resources.event import AsyncEventResourceWithStreamingResponse

        return AsyncEventResourceWithStreamingResponse(self._client.event)

    @cached_property
    def experimental(self) -> experimental.AsyncExperimentalResourceWithStreamingResponse:
        from .resources.experimental import AsyncExperimentalResourceWithStreamingResponse

        return AsyncExperimentalResourceWithStreamingResponse(self._client.experimental)

    @cached_property
    def file(self) -> file.AsyncFileResourceWithStreamingResponse:
        from .resources.file import AsyncFileResourceWithStreamingResponse

        return AsyncFileResourceWithStreamingResponse(self._client.file)

    @cached_property
    def form(self) -> form.AsyncFormResourceWithStreamingResponse:
        from .resources.form import AsyncFormResourceWithStreamingResponse

        return AsyncFormResourceWithStreamingResponse(self._client.form)

    @cached_property
    def generate(self) -> generate.AsyncGenerateResourceWithStreamingResponse:
        from .resources.generate import AsyncGenerateResourceWithStreamingResponse

        return AsyncGenerateResourceWithStreamingResponse(self._client.generate)

    @cached_property
    def integration(self) -> integration.AsyncIntegrationResourceWithStreamingResponse:
        from .resources.integration import AsyncIntegrationResourceWithStreamingResponse

        return AsyncIntegrationResourceWithStreamingResponse(self._client.integration)

    @cached_property
    def location(self) -> location.AsyncLocationResourceWithStreamingResponse:
        from .resources.location import AsyncLocationResourceWithStreamingResponse

        return AsyncLocationResourceWithStreamingResponse(self._client.location)

    @cached_property
    def mcp(self) -> mcp.AsyncMcpResourceWithStreamingResponse:
        from .resources.mcp import AsyncMcpResourceWithStreamingResponse

        return AsyncMcpResourceWithStreamingResponse(self._client.mcp)

    @cached_property
    def message(self) -> message.AsyncMessageResourceWithStreamingResponse:
        from .resources.message import AsyncMessageResourceWithStreamingResponse

        return AsyncMessageResourceWithStreamingResponse(self._client.message)

    @cached_property
    def migration(self) -> migration.AsyncMigrationResourceWithStreamingResponse:
        from .resources.migration import AsyncMigrationResourceWithStreamingResponse

        return AsyncMigrationResourceWithStreamingResponse(self._client.migration)

    @cached_property
    def model(self) -> model.AsyncModelResourceWithStreamingResponse:
        from .resources.model import AsyncModelResourceWithStreamingResponse

        return AsyncModelResourceWithStreamingResponse(self._client.model)

    @cached_property
    def permission(self) -> permission.AsyncPermissionResourceWithStreamingResponse:
        from .resources.permission import AsyncPermissionResourceWithStreamingResponse

        return AsyncPermissionResourceWithStreamingResponse(self._client.permission)

    @cached_property
    def plugin(self) -> plugin.AsyncPluginResourceWithStreamingResponse:
        from .resources.plugin import AsyncPluginResourceWithStreamingResponse

        return AsyncPluginResourceWithStreamingResponse(self._client.plugin)

    @cached_property
    def project(self) -> project.AsyncProjectResourceWithStreamingResponse:
        from .resources.project import AsyncProjectResourceWithStreamingResponse

        return AsyncProjectResourceWithStreamingResponse(self._client.project)

    @cached_property
    def provider(self) -> provider.AsyncProviderResourceWithStreamingResponse:
        from .resources.provider import AsyncProviderResourceWithStreamingResponse

        return AsyncProviderResourceWithStreamingResponse(self._client.provider)

    @cached_property
    def pty(self) -> pty.AsyncPtyResourceWithStreamingResponse:
        from .resources.pty import AsyncPtyResourceWithStreamingResponse

        return AsyncPtyResourceWithStreamingResponse(self._client.pty)

    @cached_property
    def reference(self) -> reference.AsyncReferenceResourceWithStreamingResponse:
        from .resources.reference import AsyncReferenceResourceWithStreamingResponse

        return AsyncReferenceResourceWithStreamingResponse(self._client.reference)

    @cached_property
    def rpc(self) -> rpc.AsyncRpcResourceWithStreamingResponse:
        from .resources.rpc import AsyncRpcResourceWithStreamingResponse

        return AsyncRpcResourceWithStreamingResponse(self._client.rpc)

    @cached_property
    def server(self) -> server.AsyncServerResourceWithStreamingResponse:
        from .resources.server import AsyncServerResourceWithStreamingResponse

        return AsyncServerResourceWithStreamingResponse(self._client.server)

    @cached_property
    def session(self) -> session.AsyncSessionResourceWithStreamingResponse:
        from .resources.session import AsyncSessionResourceWithStreamingResponse

        return AsyncSessionResourceWithStreamingResponse(self._client.session)

    @cached_property
    def shell(self) -> shell.AsyncShellResourceWithStreamingResponse:
        from .resources.shell import AsyncShellResourceWithStreamingResponse

        return AsyncShellResourceWithStreamingResponse(self._client.shell)

    @cached_property
    def skill(self) -> skill.AsyncSkillResourceWithStreamingResponse:
        from .resources.skill import AsyncSkillResourceWithStreamingResponse

        return AsyncSkillResourceWithStreamingResponse(self._client.skill)

    @cached_property
    def vcs(self) -> vcs.AsyncVcsResourceWithStreamingResponse:
        from .resources.vcs import AsyncVcsResourceWithStreamingResponse

        return AsyncVcsResourceWithStreamingResponse(self._client.vcs)

    @cached_property
    def voice(self) -> voice.AsyncVoiceResourceWithStreamingResponse:
        from .resources.voice import AsyncVoiceResourceWithStreamingResponse

        return AsyncVoiceResourceWithStreamingResponse(self._client.voice)

    @cached_property
    def websearch(self) -> websearch.AsyncWebsearchResourceWithStreamingResponse:
        from .resources.websearch import AsyncWebsearchResourceWithStreamingResponse

        return AsyncWebsearchResourceWithStreamingResponse(self._client.websearch)

    @cached_property
    def worktree(self) -> worktree.AsyncWorktreeResourceWithStreamingResponse:
        from .resources.worktree import AsyncWorktreeResourceWithStreamingResponse

        return AsyncWorktreeResourceWithStreamingResponse(self._client.worktree)


Client = Opencode

AsyncClient = AsyncOpencode
