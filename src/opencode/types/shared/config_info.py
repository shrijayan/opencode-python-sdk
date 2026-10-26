# File generated from our OpenAPI spec by Ferrule. See CONTRIBUTING.md for details.

from typing import TYPE_CHECKING, Dict, List, Union, Optional
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .config_agent import ConfigAgent
from .config_command import ConfigCommand
from .config_warming import ConfigWarming
from .config_provider import ConfigProvider
from .config_worktree import ConfigWorktree
from .mcp_local_config import McpLocalConfig
from .config_lsp_server import ConfigLSPServer
from .mcp_remote_config import McpRemoteConfig
from .permission_ruleset import PermissionRuleset
from .config_plugin_entry import ConfigPluginEntry
from .config_reference_git import ConfigReferenceGit
from .config_formatter_entry import ConfigFormatterEntry
from .config_reference_local import ConfigReferenceLocal
from .config_web_search_info import ConfigWebSearchInfo

__all__ = [
    "ConfigInfo",
    "Compaction",
    "CompactionKeep",
    "Enterprise",
    "Experimental",
    "ExperimentalPolicy",
    "Lsp",
    "Mcp",
    "McpServers",
    "McpTimeout",
    "Media",
    "MediaImage",
    "Model",
    "Plugin",
    "Policy",
    "References",
    "ToolOutput",
    "Warming",
    "Watcher",
    "Websearch",
]


class CompactionKeep(BaseModel):
    tokens: Optional[int] = None

    if TYPE_CHECKING:
        # Some versions of Pydantic <2.8.0 have a bug and don’t allow assigning a
        # value to this field, so for compatibility we avoid doing it at runtime.
        __pydantic_extra__: Dict[str, object] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]

        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...
    else:
        __pydantic_extra__: Dict[str, object]


class Compaction(BaseModel):
    auto: Optional[bool] = None

    buffer: Optional[int] = None

    keep: Optional[CompactionKeep] = None

    if TYPE_CHECKING:
        # Some versions of Pydantic <2.8.0 have a bug and don’t allow assigning a
        # value to this field, so for compatibility we avoid doing it at runtime.
        __pydantic_extra__: Dict[str, object] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]

        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...
    else:
        __pydantic_extra__: Dict[str, object]


class Enterprise(BaseModel):
    url: Optional[str] = None

    if TYPE_CHECKING:
        # Some versions of Pydantic <2.8.0 have a bug and don’t allow assigning a
        # value to this field, so for compatibility we avoid doing it at runtime.
        __pydantic_extra__: Dict[str, object] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]

        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...
    else:
        __pydantic_extra__: Dict[str, object]


class ExperimentalPolicy(BaseModel):
    action: Literal["provider.use", "tool.use", "integration.use"]

    effect: Literal["allow", "deny"]

    resource: str

    if TYPE_CHECKING:
        # Some versions of Pydantic <2.8.0 have a bug and don’t allow assigning a
        # value to this field, so for compatibility we avoid doing it at runtime.
        __pydantic_extra__: Dict[str, object] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]

        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...
    else:
        __pydantic_extra__: Dict[str, object]


class Experimental(BaseModel):
    location_idle_timeout: Union[Literal[False], str, None] = None

    policies: Optional[List[ExperimentalPolicy]] = None

    portable_shell_scanner: Optional[bool] = None

    subagent_depth: Optional[int] = None

    todo: Optional[bool] = None

    if TYPE_CHECKING:
        # Some versions of Pydantic <2.8.0 have a bug and don’t allow assigning a
        # value to this field, so for compatibility we avoid doing it at runtime.
        __pydantic_extra__: Dict[str, object] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]

        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...
    else:
        __pydantic_extra__: Dict[str, object]


class Lsp(BaseModel):
    disabled: Literal[True]

    if TYPE_CHECKING:
        # Some versions of Pydantic <2.8.0 have a bug and don’t allow assigning a
        # value to this field, so for compatibility we avoid doing it at runtime.
        __pydantic_extra__: Dict[str, object] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]

        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...
    else:
        __pydantic_extra__: Dict[str, object]


McpServers: TypeAlias = Union[McpLocalConfig, McpRemoteConfig]


class McpTimeout(BaseModel):
    catalog: Optional[int] = None

    execution: Optional[int] = None

    startup: Optional[int] = None

    if TYPE_CHECKING:
        # Some versions of Pydantic <2.8.0 have a bug and don’t allow assigning a
        # value to this field, so for compatibility we avoid doing it at runtime.
        __pydantic_extra__: Dict[str, object] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]

        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...
    else:
        __pydantic_extra__: Dict[str, object]


class Mcp(BaseModel):
    servers: Optional[Dict[str, McpServers]] = None

    timeout: Optional[McpTimeout] = None

    if TYPE_CHECKING:
        # Some versions of Pydantic <2.8.0 have a bug and don’t allow assigning a
        # value to this field, so for compatibility we avoid doing it at runtime.
        __pydantic_extra__: Dict[str, object] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]

        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...
    else:
        __pydantic_extra__: Dict[str, object]


class MediaImage(BaseModel):
    auto_resize: Optional[bool] = None

    max_base64_bytes: Optional[int] = None

    max_height: Optional[int] = None

    max_width: Optional[int] = None

    if TYPE_CHECKING:
        # Some versions of Pydantic <2.8.0 have a bug and don’t allow assigning a
        # value to this field, so for compatibility we avoid doing it at runtime.
        __pydantic_extra__: Dict[str, object] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]

        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...
    else:
        __pydantic_extra__: Dict[str, object]


class Media(BaseModel):
    image: Optional[MediaImage] = None

    if TYPE_CHECKING:
        # Some versions of Pydantic <2.8.0 have a bug and don’t allow assigning a
        # value to this field, so for compatibility we avoid doing it at runtime.
        __pydantic_extra__: Dict[str, object] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]

        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...
    else:
        __pydantic_extra__: Dict[str, object]


class Model(BaseModel):
    model: str

    provider_id: str = FieldInfo(alias="providerID")

    variant: Optional[str] = None

    if TYPE_CHECKING:
        # Some versions of Pydantic <2.8.0 have a bug and don’t allow assigning a
        # value to this field, so for compatibility we avoid doing it at runtime.
        __pydantic_extra__: Dict[str, object] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]

        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...
    else:
        __pydantic_extra__: Dict[str, object]


Plugin: TypeAlias = Union[str, ConfigPluginEntry]


class Policy(BaseModel):
    action: Literal["provider.use", "tool.use", "integration.use"]

    effect: Literal["allow", "deny"]

    resource: str

    if TYPE_CHECKING:
        # Some versions of Pydantic <2.8.0 have a bug and don’t allow assigning a
        # value to this field, so for compatibility we avoid doing it at runtime.
        __pydantic_extra__: Dict[str, object] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]

        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...
    else:
        __pydantic_extra__: Dict[str, object]


References: TypeAlias = Union[str, ConfigReferenceGit, ConfigReferenceLocal]


class ToolOutput(BaseModel):
    max_bytes: Optional[int] = None

    max_lines: Optional[int] = None

    if TYPE_CHECKING:
        # Some versions of Pydantic <2.8.0 have a bug and don’t allow assigning a
        # value to this field, so for compatibility we avoid doing it at runtime.
        __pydantic_extra__: Dict[str, object] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]

        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...
    else:
        __pydantic_extra__: Dict[str, object]


Warming: TypeAlias = Union[bool, ConfigWarming]


class Watcher(BaseModel):
    ignore: Optional[List[str]] = None

    if TYPE_CHECKING:
        # Some versions of Pydantic <2.8.0 have a bug and don’t allow assigning a
        # value to this field, so for compatibility we avoid doing it at runtime.
        __pydantic_extra__: Dict[str, object] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]

        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...
    else:
        __pydantic_extra__: Dict[str, object]


Websearch: TypeAlias = Union[Literal[False], ConfigWebSearchInfo]


class ConfigInfo(BaseModel):
    agents: Optional[Dict[str, ConfigAgent]] = None

    commands: Optional[Dict[str, ConfigCommand]] = None

    compaction: Optional[Compaction] = None

    default_agent: Optional[str] = None

    enterprise: Optional[Enterprise] = None

    experimental: Optional[Experimental] = None

    formatter: Union[bool, Dict[str, ConfigFormatterEntry], None] = None

    instructions: Optional[List[str]] = None

    lsp: Union[bool, Dict[str, Union[Lsp, ConfigLSPServer]], None] = None

    mcp: Optional[Mcp] = None

    media: Optional[Media] = None

    model: Union[str, Model, None] = None

    permissions: Optional[PermissionRuleset] = None

    plugins: Optional[List[Plugin]] = None

    policies: Optional[List[Policy]] = None

    providers: Optional[Dict[str, ConfigProvider]] = None

    references: Optional[Dict[str, References]] = None

    share: Optional[Literal["manual", "auto", "disabled"]] = None

    shell: Optional[str] = None

    skills: Optional[List[str]] = None

    snapshots: Optional[bool] = None

    tool_output: Optional[ToolOutput] = None

    update: Optional[Literal["disable", "notify", "auto"]] = None

    username: Optional[str] = None

    warming: Optional[Warming] = None

    watcher: Optional[Watcher] = None

    websearch: Optional[Websearch] = None

    worktree: Optional[ConfigWorktree] = None

    if TYPE_CHECKING:
        # Some versions of Pydantic <2.8.0 have a bug and don’t allow assigning a
        # value to this field, so for compatibility we avoid doing it at runtime.
        __pydantic_extra__: Dict[str, object] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]

        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...
    else:
        __pydantic_extra__: Dict[str, object]
