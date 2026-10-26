# Shared Types

```python
from opencode.types import (
    AbsolutePath,
    AgentColor,
    AgentID,
    AgentInfo,
    AgentUpdatedEvent,
    CommandInfo,
    CommandUpdatedEvent,
    ConfigAgent,
    ConfigCommand,
    ConfigDirectory,
    ConfigDocument,
    ConfigEntry,
    ConfigFormatterEntry,
    ConfigInfo,
    ConfigLSPServer,
    ConfigModel,
    ConfigModelCapabilities,
    ConfigModelCost,
    ConfigModelReasoning,
    ConfigModelSettings,
    ConfigPluginEntry,
    ConfigProvider,
    ConfigProviderSettings,
    ConfigReferenceGit,
    ConfigReferenceLocal,
    ConfigShellOption,
    ConfigUpdatedEvent,
    ConfigWarming,
    ConfigWebSearchInfo,
    ConfigWorktree,
    ConnectionCredentialInfo,
    ConnectionEnvInfo,
    ConnectionInfo,
    ConnectionStatus,
    CredentialEntry,
    CredentialExternal,
    CredentialID,
    CredentialKey,
    CredentialOAuth,
    CredentialSwitchedEvent,
    CredentialUpdatedEvent,
    CredentialValue,
    Event,
    EventID,
    EventSeq,
    EventVersion,
    EventVersion10,
    FileDiffInfo,
    FileSystemEntry,
    FileSystemWrite,
    FilesystemChangedEvent,
    FormAnswer,
    FormBooleanField,
    FormCancelledEvent,
    FormCreatedEvent,
    FormDetail,
    FormExternalField,
    FormField,
    FormFields,
    FormFields1,
    FormFields2,
    FormFields3,
    FormID,
    FormInfo,
    FormIntegerField,
    FormMetadata,
    FormMultiselectField,
    FormNumberField,
    FormOption,
    FormRepliedEvent,
    FormState,
    FormStringField,
    FormValue,
    FormWhen,
    InstallationUpdateAvailableEvent,
    InstallationUpdatedEvent,
    InstructionEntryInfo,
    InstructionEntryKey,
    InstructionEntrySnapshot,
    InstructionHash,
    IntegrationAttempt,
    IntegrationAttemptID,
    IntegrationAttemptStatus,
    IntegrationCommandAttempt,
    IntegrationCommandAttemptStatus,
    IntegrationCommandMethod,
    IntegrationEnvMethod,
    IntegrationExternalMethod,
    IntegrationID,
    IntegrationInfo,
    IntegrationKeyMethod,
    IntegrationMethod,
    IntegrationMethodID,
    IntegrationOAuthMethod,
    IntegrationUpdatedEvent,
    LocationPublicInfo,
    LocationPublicRef,
    LocationRef,
    LocationShutdownEvent,
    McpLocalConfig,
    McpOAuthConfig,
    McpProtocol,
    McpRemoteConfig,
    McpResource,
    McpResourceCatalog,
    McpResourceTemplate,
    McpResourcesChangedEvent,
    McpServer,
    McpStatusChangedEvent,
    McpStatusConnected,
    McpStatusDisabled,
    McpStatusFailed,
    McpStatusNeedsAuth,
    McpStatusPending,
    ModelCacheFormat,
    ModelCapabilities,
    ModelCompatibility,
    ModelCost,
    ModelInfo,
    ModelMaxTokensField,
    ModelReasoningField,
    ModelRef,
    ModelSettings,
    ModelUpdatedEvent,
    ModelVariant,
    ModelsDevRefreshedEvent,
    MoneyUSD,
    MoneyUSDPerMillionTokens,
    PairingCode,
    PairingSession,
    PermissionAskedEvent,
    PermissionEffect,
    PermissionID,
    PermissionRepliedEvent,
    PermissionReply,
    PermissionRequest,
    PermissionRule,
    PermissionRuleset,
    PermissionSavedID,
    PermissionSavedInfo,
    PermissionSource,
    PersistentPtyAddedEvent,
    PersistentPtyHandoff,
    PersistentPtyInfo,
    PersistentPtyReadLines,
    PersistentPtyReadResult,
    PersistentPtyRemovedEvent,
    PersistentPtySnapshot,
    PluginFeatures,
    PluginInfo,
    PluginSource,
    PluginState,
    PluginUpdatedEvent,
    Project,
    ProjectCommands,
    ProjectIcon,
    ProjectID,
    ProjectTime,
    ProjectUpdatedEvent,
    ProjectVcs,
    PromptAgentAttachment,
    PromptBase64,
    PromptFileAttachment,
    PromptFileSource,
    PromptInputFileAttachment,
    PromptInputSkillAttachment,
    PromptMention,
    PromptSkillAttachment,
    ProviderCompaction,
    ProviderCompatibility,
    ProviderEncoding,
    ProviderID,
    ProviderInfo,
    ProviderRequest,
    ProviderSettings,
    ProviderTransport,
    ProviderUpdatedEvent,
    Pty,
    PtyCreatedEvent,
    PtyDeletedEvent,
    PtyExitedEvent,
    PtyID,
    PtyTicketConnectToken,
    PtyUpdatedEvent,
    ReferenceGitSource,
    ReferenceInfo,
    ReferenceLocalSource,
    ReferenceSource,
    ReferenceUpdatedEvent,
    RelativePath,
    RpcEvent,
    RpcOutput,
    ServerConnectedEvent,
    ServerInfo,
    SessionAgentSelectedEvent,
    SessionArchivedEvent,
    SessionCompactionDeltaEvent,
    SessionCompactionEndedEvent,
    SessionCompactionFailedEvent,
    SessionCompactionStartedEvent,
    SessionCreatedEvent,
    SessionDeletedEvent,
    SessionExecutionFailedEvent,
    SessionExecutionInterruptedEvent,
    SessionExecutionStartedEvent,
    SessionExecutionSucceededEvent,
    SessionForkBoundary,
    SessionForkedEvent,
    SessionID,
    SessionID1,
    SessionIdleEvent,
    SessionInboxCancelledEvent,
    SessionInboxCompaction,
    SessionInboxCompactionPayload,
    SessionInboxDeliveredEvent,
    SessionInboxDelivery,
    SessionInboxDeliveryChangedEvent,
    SessionInboxEnqueuedEvent,
    SessionInboxInfo,
    SessionInboxItem,
    SessionInboxMove,
    SessionInboxMovePayload,
    SessionInboxMovePayload1,
    SessionInboxSynthetic,
    SessionInboxSyntheticPayload,
    SessionInboxUser,
    SessionInboxUserPayload,
    SessionInfo,
    SessionInstructionsUpdatedEvent,
    SessionInterruptResponse,
    SessionMessageAgentSelected,
    SessionMessageAssistant,
    SessionMessageAssistantReasoning,
    SessionMessageAssistantRetry,
    SessionMessageAssistantText,
    SessionMessageAssistantTool,
    SessionMessageCompaction,
    SessionMessageCompactionCompleted,
    SessionMessageCompactionFailed,
    SessionMessageCompactionRunning,
    SessionMessageID,
    SessionMessageIdle,
    SessionMessageInfo,
    SessionMessageLocationSwitched,
    SessionMessageModelSelected,
    SessionMessageNative,
    SessionMessageNative1,
    SessionMessageNative10,
    SessionMessageNative11,
    SessionMessageNative12,
    SessionMessageNative2,
    SessionMessageNative3,
    SessionMessageNative4,
    SessionMessageNative5,
    SessionMessageNative6,
    SessionMessageNative7,
    SessionMessageNative8,
    SessionMessageNative9,
    SessionMessageShell,
    SessionMessageSkill,
    SessionMessageSynthetic,
    SessionMessageSystem,
    SessionMessageToolStateCompleted,
    SessionMessageToolStateError,
    SessionMessageToolStateRunning,
    SessionMessageToolStateStreaming,
    SessionMessageUser,
    SessionMessagesResponse,
    SessionMetadata,
    SessionMetadataUpdatedEvent,
    SessionModelSelectedEvent,
    SessionMovedEvent,
    SessionPermissionsEvent,
    SessionReasoningDeltaEvent,
    SessionReasoningEndedEvent,
    SessionReasoningStartedEvent,
    SessionRenamedEvent,
    SessionRetryScheduledEvent,
    SessionRevert,
    SessionRevertClearedEvent,
    SessionRevertCommittedEvent,
    SessionRevertStagedEvent,
    SessionShellEndedEvent,
    SessionShellStartedEvent,
    SessionSkillActivatedEvent,
    SessionStatsActivity,
    SessionStatsInfo,
    SessionStatsModelUsage,
    SessionStatsToolTotals,
    SessionStatsToolUsage,
    SessionStatsTools,
    SessionStatus,
    SessionStatusUpdated,
    SessionStepEndedEvent,
    SessionStepFailedEvent,
    SessionStepStartedEvent,
    SessionStepStreamedEvent,
    SessionStructuredError,
    SessionSyntheticEvent,
    SessionTextDeltaEvent,
    SessionTextEndedEvent,
    SessionTextStartedEvent,
    SessionToolCalledEvent,
    SessionToolFailedEvent,
    SessionToolInputDeltaEvent,
    SessionToolInputEndedEvent,
    SessionToolInputStartedEvent,
    SessionToolProgressEvent,
    SessionToolSuccessEvent,
    SessionTransferData,
    SessionUnarchivedEvent,
    SessionUsageUpdatedEvent,
    SessionViewedEvent,
    SessionsCursor,
    SessionsResponse,
    ShellCreatedEvent,
    ShellDeletedEvent,
    ShellExitedEvent,
    ShellID,
    ShellInfo,
    SkillID,
    SkillInfo,
    SkillName,
    SkillUpdatedEvent,
    SnapshotID,
    TokenUsageInfo,
    ToolContent,
    ToolFileContent,
    ToolTextContent,
    TuiCommandExecuteEvent,
    TuiPromptAppendEvent,
    TuiSessionSelectEvent,
    TuiToastShowEvent,
    VcsBase,
    VcsBranch,
    VcsBranchList,
    VcsBranchUpdatedEvent,
    VcsFileStatus,
    VcsInfo,
    VcsMode,
    VoiceTransport,
    VoiceTransportInput,
    VoiceWebRTCTransport,
    VoiceWebRTCTransportInput,
    VoiceWebSocketTransport,
    VoiceWebSocketTransportInput,
    WebSearchID,
    WebSearchProvider,
    WebSearchResponse,
    WebSearchResult,
    WebsearchUpdatedEvent,
    WorkspaceID,
    WorktreeDirectory,
    WorktreeInfo,
    WorktreeList,
    WorktreeResolvedEvent,
    WorktreeUpdatedEvent,
)
```

# Agent

Types:

```python
from opencode.types import AgentListResponse, AgentGetResponse
```

Methods:

- <code title="get /api/agent">client.agent.<a href="./src/opencode/resources/agent.py">list</a>(\*\*<a href="src/opencode/types/agent_list_params.py">params</a>) -> <a href="./src/opencode/types/agent_list_response.py">AgentListResponse</a></code>
- <code title="get /api/agent/{agentID}">client.agent.<a href="./src/opencode/resources/agent.py">get</a>(agent_id, \*\*<a href="src/opencode/types/agent_get_params.py">params</a>) -> <a href="./src/opencode/types/agent_get_response.py">AgentGetResponse</a></code>

# Command

Types:

```python
from opencode.types import CommandListResponse
```

Methods:

- <code title="get /api/command">client.command.<a href="./src/opencode/resources/command.py">list</a>(\*\*<a href="src/opencode/types/command_list_params.py">params</a>) -> <a href="./src/opencode/types/command_list_response.py">CommandListResponse</a></code>

# Config

Types:

```python
from opencode.types import ConfigGetResponse, ConfigShellsResponse
```

Methods:

- <code title="patch /api/experimental/config">client.config.<a href="./src/opencode/resources/config.py">update</a>(\*\*<a href="src/opencode/types/config_update_params.py">params</a>) -> None</code>
- <code title="get /api/config">client.config.<a href="./src/opencode/resources/config.py">get</a>(\*\*<a href="src/opencode/types/config_get_params.py">params</a>) -> <a href="./src/opencode/types/config_get_response.py">ConfigGetResponse</a></code>
- <code title="get /api/config/shell">client.config.<a href="./src/opencode/resources/config.py">shells</a>() -> <a href="./src/opencode/types/config_shells_response.py">ConfigShellsResponse</a></code>

# Credential

Types:

```python
from opencode.types import CredentialListResponse
```

Methods:

- <code title="post /api/credential">client.credential.<a href="./src/opencode/resources/credential.py">create</a>(\*\*<a href="src/opencode/types/credential_create_params.py">params</a>) -> <a href="./src/opencode/types/shared/credential_entry.py">CredentialEntry</a></code>
- <code title="patch /api/credential/{credentialID}">client.credential.<a href="./src/opencode/resources/credential.py">update</a>(credential_id, \*\*<a href="src/opencode/types/credential_update_params.py">params</a>) -> None</code>
- <code title="get /api/credential">client.credential.<a href="./src/opencode/resources/credential.py">list</a>() -> <a href="./src/opencode/types/credential_list_response.py">CredentialListResponse</a></code>
- <code title="post /api/credential/{credentialID}/activate">client.credential.<a href="./src/opencode/resources/credential.py">activate</a>(credential_id) -> None</code>
- <code title="delete /api/credential/{credentialID}">client.credential.<a href="./src/opencode/resources/credential.py">remove</a>(credential_id) -> None</code>

# Debug

## Location

Types:

```python
from opencode.types.debug import LocationListResponse
```

Methods:

- <code title="get /api/debug/location">client.debug.location.<a href="./src/opencode/resources/debug/location.py">list</a>() -> <a href="./src/opencode/types/debug/location_list_response.py">LocationListResponse</a></code>
- <code title="delete /api/debug/location">client.debug.location.<a href="./src/opencode/resources/debug/location.py">evict</a>(\*\*<a href="src/opencode/types/debug/location_evict_params.py">params</a>) -> None</code>

# Event

Methods:

- <code title="get /api/event">client.event.<a href="./src/opencode/resources/event.py">subscribe</a>() -> <a href="./src/opencode/types/shared/event.py">Event</a></code>

# Experimental

## PersistentPty

Types:

```python
from opencode.types.experimental import (
    PersistentPtyListResponse,
    PersistentPtyHandoffResponse,
    PersistentPtyReadResponse,
)
```

Methods:

- <code title="post /api/experimental/session/{sessionID}/terminal">client.experimental.persistent_pty.<a href="./src/opencode/resources/experimental/persistent_pty.py">create</a>(session_id, \*\*<a href="src/opencode/types/experimental/persistent_pty_create_params.py">params</a>) -> <a href="./src/opencode/types/shared/persistent_pty_info.py">PersistentPtyInfo</a></code>
- <code title="put /api/experimental/persistent-pty/{ptyID}">client.experimental.persistent_pty.<a href="./src/opencode/resources/experimental/persistent_pty.py">update</a>(pty_id, \*\*<a href="src/opencode/types/experimental/persistent_pty_update_params.py">params</a>) -> <a href="./src/opencode/types/shared/persistent_pty_info.py">PersistentPtyInfo</a></code>
- <code title="get /api/experimental/session/{sessionID}/terminal">client.experimental.persistent_pty.<a href="./src/opencode/resources/experimental/persistent_pty.py">list</a>(session_id) -> <a href="./src/opencode/types/experimental/persistent_pty_list_response.py">PersistentPtyListResponse</a></code>
- <code title="post /api/experimental/persistent-pty/{ptyID}/connect-token">client.experimental.persistent_pty.<a href="./src/opencode/resources/experimental/persistent_pty.py">connect_token</a>(pty_id) -> <a href="./src/opencode/types/shared/pty_ticket_connect_token.py">PtyTicketConnectToken</a></code>
- <code title="get /api/experimental/persistent-pty/{ptyID}">client.experimental.persistent_pty.<a href="./src/opencode/resources/experimental/persistent_pty.py">get</a>(pty_id) -> <a href="./src/opencode/types/shared/persistent_pty_info.py">PersistentPtyInfo</a></code>
- <code title="post /api/experimental/persistent-pty/handoff">client.experimental.persistent_pty.<a href="./src/opencode/resources/experimental/persistent_pty.py">handoff</a>() -> <a href="./src/opencode/types/experimental/persistent_pty_handoff_response.py">PersistentPtyHandoffResponse</a></code>
- <code title="get /api/experimental/session/{sessionID}/terminal/read">client.experimental.persistent_pty.<a href="./src/opencode/resources/experimental/persistent_pty.py">read</a>(session_id, \*\*<a href="src/opencode/types/experimental/persistent_pty_read_params.py">params</a>) -> <a href="./src/opencode/types/experimental/persistent_pty_read_response.py">PersistentPtyReadResponse</a></code>
- <code title="delete /api/experimental/persistent-pty/{ptyID}">client.experimental.persistent_pty.<a href="./src/opencode/resources/experimental/persistent_pty.py">remove</a>(pty_id) -> None</code>
- <code title="post /api/experimental/persistent-pty/shutdown">client.experimental.persistent_pty.<a href="./src/opencode/resources/experimental/persistent_pty.py">shutdown</a>() -> None</code>
- <code title="get /api/experimental/persistent-pty/{ptyID}/snapshot">client.experimental.persistent_pty.<a href="./src/opencode/resources/experimental/persistent_pty.py">snapshot</a>(pty_id) -> <a href="./src/opencode/types/shared/persistent_pty_snapshot.py">PersistentPtySnapshot</a></code>

# File

Types:

```python
from opencode.types import FileListResponse, FileFindResponse, FileWriteResponse
```

Methods:

- <code title="get /api/fs/list">client.file.<a href="./src/opencode/resources/file.py">list</a>(\*\*<a href="src/opencode/types/file_list_params.py">params</a>) -> <a href="./src/opencode/types/file_list_response.py">FileListResponse</a></code>
- <code title="get /api/fs/find">client.file.<a href="./src/opencode/resources/file.py">find</a>(\*\*<a href="src/opencode/types/file_find_params.py">params</a>) -> <a href="./src/opencode/types/file_find_response.py">FileFindResponse</a></code>
- <code title="get /api/fs/read/{path}">client.file.<a href="./src/opencode/resources/file.py">read</a>(path, \*\*<a href="src/opencode/types/file_read_params.py">params</a>) -> None</code>
- <code title="post /api/experimental/fs/write">client.file.<a href="./src/opencode/resources/file.py">write</a>(\*\*<a href="src/opencode/types/file_write_params.py">params</a>) -> <a href="./src/opencode/types/file_write_response.py">FileWriteResponse</a></code>

# Form

Types:

```python
from opencode.types import FormListResponse
```

Methods:

- <code title="get /api/form">client.form.<a href="./src/opencode/resources/form.py">list</a>(\*\*<a href="src/opencode/types/form_list_params.py">params</a>) -> <a href="./src/opencode/types/form_list_response.py">FormListResponse</a></code>

# Generate

Types:

```python
from opencode.types import GenerateTextResponse
```

Methods:

- <code title="post /api/experimental/generate">client.generate.<a href="./src/opencode/resources/generate.py">text</a>(\*\*<a href="src/opencode/types/generate_text_params.py">params</a>) -> <a href="./src/opencode/types/generate_text_response.py">GenerateTextResponse</a></code>

# Integration

Types:

```python
from opencode.types import IntegrationListResponse, IntegrationGetResponse
```

Methods:

- <code title="get /api/integration">client.integration.<a href="./src/opencode/resources/integration/integration.py">list</a>(\*\*<a href="src/opencode/types/integration_list_params.py">params</a>) -> <a href="./src/opencode/types/integration_list_response.py">IntegrationListResponse</a></code>
- <code title="get /api/integration/{integrationID}">client.integration.<a href="./src/opencode/resources/integration/integration.py">get</a>(integration_id, \*\*<a href="src/opencode/types/integration_get_params.py">params</a>) -> <a href="./src/opencode/types/integration_get_response.py">IntegrationGetResponse</a></code>

## Wellknown

Methods:

- <code title="post /api/experimental/integration/wellknown">client.integration.wellknown.<a href="./src/opencode/resources/integration/wellknown.py">add</a>(\*\*<a href="src/opencode/types/integration/wellknown_add_params.py">params</a>) -> None</code>

## Connect

Methods:

- <code title="post /api/integration/{integrationID}/connect/external">client.integration.connect.<a href="./src/opencode/resources/integration/connect.py">external</a>(integration_id, \*\*<a href="src/opencode/types/integration/connect_external_params.py">params</a>) -> None</code>
- <code title="post /api/integration/{integrationID}/connect/key">client.integration.connect.<a href="./src/opencode/resources/integration/connect.py">key</a>(integration_id, \*\*<a href="src/opencode/types/integration/connect_key_params.py">params</a>) -> None</code>

## Oauth

Types:

```python
from opencode.types.integration import OauthConnectResponse, OauthStatusResponse
```

Methods:

- <code title="delete /api/integration/{integrationID}/connect/oauth/{attemptID}">client.integration.oauth.<a href="./src/opencode/resources/integration/oauth.py">cancel</a>(attempt_id, \*, integration_id, \*\*<a href="src/opencode/types/integration/oauth_cancel_params.py">params</a>) -> None</code>
- <code title="post /api/integration/{integrationID}/connect/oauth/{attemptID}/complete">client.integration.oauth.<a href="./src/opencode/resources/integration/oauth.py">complete</a>(attempt_id, \*, integration_id, \*\*<a href="src/opencode/types/integration/oauth_complete_params.py">params</a>) -> None</code>
- <code title="post /api/integration/{integrationID}/connect/oauth">client.integration.oauth.<a href="./src/opencode/resources/integration/oauth.py">connect</a>(integration_id, \*\*<a href="src/opencode/types/integration/oauth_connect_params.py">params</a>) -> <a href="./src/opencode/types/integration/oauth_connect_response.py">OauthConnectResponse</a></code>
- <code title="get /api/integration/{integrationID}/connect/oauth/{attemptID}">client.integration.oauth.<a href="./src/opencode/resources/integration/oauth.py">status</a>(attempt_id, \*, integration_id, \*\*<a href="src/opencode/types/integration/oauth_status_params.py">params</a>) -> <a href="./src/opencode/types/integration/oauth_status_response.py">OauthStatusResponse</a></code>

## Command

Types:

```python
from opencode.types.integration import CommandConnectResponse, CommandStatusResponse
```

Methods:

- <code title="delete /api/integration/{integrationID}/connect/command/{attemptID}">client.integration.command.<a href="./src/opencode/resources/integration/command.py">cancel</a>(attempt_id, \*, integration_id, \*\*<a href="src/opencode/types/integration/command_cancel_params.py">params</a>) -> None</code>
- <code title="post /api/integration/{integrationID}/connect/command">client.integration.command.<a href="./src/opencode/resources/integration/command.py">connect</a>(integration_id, \*\*<a href="src/opencode/types/integration/command_connect_params.py">params</a>) -> <a href="./src/opencode/types/integration/command_connect_response.py">CommandConnectResponse</a></code>
- <code title="get /api/integration/{integrationID}/connect/command/{attemptID}">client.integration.command.<a href="./src/opencode/resources/integration/command.py">status</a>(attempt_id, \*, integration_id, \*\*<a href="src/opencode/types/integration/command_status_params.py">params</a>) -> <a href="./src/opencode/types/integration/command_status_response.py">CommandStatusResponse</a></code>

# Location

Methods:

- <code title="get /api/location">client.location.<a href="./src/opencode/resources/location.py">get</a>(\*\*<a href="src/opencode/types/location_get_params.py">params</a>) -> <a href="./src/opencode/types/shared/location_public_info.py">LocationPublicInfo</a></code>
- <code title="post /api/location/reload">client.location.<a href="./src/opencode/resources/location.py">reload</a>() -> None</code>

# Mcp

Types:

```python
from opencode.types import McpListResponse
```

Methods:

- <code title="get /api/mcp">client.mcp.<a href="./src/opencode/resources/mcp/mcp.py">list</a>(\*\*<a href="src/opencode/types/mcp_list_params.py">params</a>) -> <a href="./src/opencode/types/mcp_list_response.py">McpListResponse</a></code>
- <code title="put /api/experimental/mcp/{server}">client.mcp.<a href="./src/opencode/resources/mcp/mcp.py">add</a>(server, \*\*<a href="src/opencode/types/mcp_add_params.py">params</a>) -> None</code>
- <code title="post /api/experimental/mcp/{server}/connect">client.mcp.<a href="./src/opencode/resources/mcp/mcp.py">connect</a>(server, \*\*<a href="src/opencode/types/mcp_connect_params.py">params</a>) -> None</code>
- <code title="post /api/experimental/mcp/{server}/disconnect">client.mcp.<a href="./src/opencode/resources/mcp/mcp.py">disconnect</a>(server, \*\*<a href="src/opencode/types/mcp_disconnect_params.py">params</a>) -> None</code>
- <code title="delete /api/experimental/mcp/{server}">client.mcp.<a href="./src/opencode/resources/mcp/mcp.py">remove</a>(server, \*\*<a href="src/opencode/types/mcp_remove_params.py">params</a>) -> None</code>

## Resource

Types:

```python
from opencode.types.mcp import ResourceCatalogResponse
```

Methods:

- <code title="get /api/mcp/resource">client.mcp.resource.<a href="./src/opencode/resources/mcp/resource.py">catalog</a>(\*\*<a href="src/opencode/types/mcp/resource_catalog_params.py">params</a>) -> <a href="./src/opencode/types/mcp/resource_catalog_response.py">ResourceCatalogResponse</a></code>

# Message

Methods:

- <code title="get /api/session/{sessionID}/message">client.message.<a href="./src/opencode/resources/message.py">list</a>(session_id, \*\*<a href="src/opencode/types/message_list_params.py">params</a>) -> <a href="./src/opencode/types/shared/session_message_info.py">SessionMessageInfo</a></code>

# Migration

## V1

Types:

```python
from opencode.types.migration import V1StatusResponse
```

Methods:

- <code title="get /api/experimental/migration/v1">client.migration.v1.<a href="./src/opencode/resources/migration/v1.py">status</a>() -> <a href="./src/opencode/types/migration/v1_status_response.py">V1StatusResponse</a></code>

# Model

Types:

```python
from opencode.types import ModelListResponse, ModelDefaultResponse
```

Methods:

- <code title="get /api/model">client.model.<a href="./src/opencode/resources/model.py">list</a>(\*\*<a href="src/opencode/types/model_list_params.py">params</a>) -> <a href="./src/opencode/types/model_list_response.py">ModelListResponse</a></code>
- <code title="get /api/model/default">client.model.<a href="./src/opencode/resources/model.py">default</a>(\*\*<a href="src/opencode/types/model_default_params.py">params</a>) -> <a href="./src/opencode/types/model_default_response.py">ModelDefaultResponse</a></code>

# Permission

Types:

```python
from opencode.types import PermissionCreateResponse, PermissionListResponse
```

Methods:

- <code title="post /api/session/{sessionID}/permission">client.permission.<a href="./src/opencode/resources/permission/permission.py">create</a>(session_id, \*\*<a href="src/opencode/types/permission_create_params.py">params</a>) -> <a href="./src/opencode/types/permission_create_response.py">PermissionCreateResponse</a></code>
- <code title="get /api/session/{sessionID}/permission">client.permission.<a href="./src/opencode/resources/permission/permission.py">list</a>(session_id) -> <a href="./src/opencode/types/permission_list_response.py">PermissionListResponse</a></code>
- <code title="get /api/session/{sessionID}/permission/{requestID}">client.permission.<a href="./src/opencode/resources/permission/permission.py">get</a>(request_id, \*, session_id) -> <a href="./src/opencode/types/shared/permission_request.py">PermissionRequest</a></code>
- <code title="post /api/session/{sessionID}/permission/{requestID}/reply">client.permission.<a href="./src/opencode/resources/permission/permission.py">reply</a>(request_id, \*, session_id, \*\*<a href="src/opencode/types/permission_reply_params.py">params</a>) -> None</code>

## Request

Types:

```python
from opencode.types.permission import RequestListResponse
```

Methods:

- <code title="get /api/permission/request">client.permission.request.<a href="./src/opencode/resources/permission/request.py">list</a>(\*\*<a href="src/opencode/types/permission/request_list_params.py">params</a>) -> <a href="./src/opencode/types/permission/request_list_response.py">RequestListResponse</a></code>

## Saved

Types:

```python
from opencode.types.permission import SavedListResponse
```

Methods:

- <code title="patch /api/permission/saved/{id}">client.permission.saved.<a href="./src/opencode/resources/permission/saved.py">update</a>(id, \*\*<a href="src/opencode/types/permission/saved_update_params.py">params</a>) -> <a href="./src/opencode/types/shared/permission_saved_info.py">PermissionSavedInfo</a></code>
- <code title="get /api/permission/saved">client.permission.saved.<a href="./src/opencode/resources/permission/saved.py">list</a>(\*\*<a href="src/opencode/types/permission/saved_list_params.py">params</a>) -> <a href="./src/opencode/types/permission/saved_list_response.py">SavedListResponse</a></code>
- <code title="delete /api/permission/saved/{id}">client.permission.saved.<a href="./src/opencode/resources/permission/saved.py">remove</a>(id) -> None</code>

# Plugin

Types:

```python
from opencode.types import PluginListResponse, PluginCheckResponse
```

Methods:

- <code title="post /api/plugin/update">client.plugin.<a href="./src/opencode/resources/plugin.py">update</a>(\*\*<a href="src/opencode/types/plugin_update_params.py">params</a>) -> None</code>
- <code title="get /api/plugin">client.plugin.<a href="./src/opencode/resources/plugin.py">list</a>(\*\*<a href="src/opencode/types/plugin_list_params.py">params</a>) -> <a href="./src/opencode/types/plugin_list_response.py">PluginListResponse</a></code>
- <code title="post /api/plugin/check">client.plugin.<a href="./src/opencode/resources/plugin.py">check</a>(\*\*<a href="src/opencode/types/plugin_check_params.py">params</a>) -> <a href="./src/opencode/types/plugin_check_response.py">PluginCheckResponse</a></code>

# Project

Types:

```python
from opencode.types import ProjectListResponse
```

Methods:

- <code title="patch /api/project/{projectID}">client.project.<a href="./src/opencode/resources/project.py">update</a>(project_id, \*\*<a href="src/opencode/types/project_update_params.py">params</a>) -> <a href="./src/opencode/types/shared/project.py">Project</a></code>
- <code title="get /api/project">client.project.<a href="./src/opencode/resources/project.py">list</a>(\*\*<a href="src/opencode/types/project_list_params.py">params</a>) -> <a href="./src/opencode/types/project_list_response.py">ProjectListResponse</a></code>

# Provider

Types:

```python
from opencode.types import ProviderListResponse, ProviderGetResponse
```

Methods:

- <code title="get /api/provider">client.provider.<a href="./src/opencode/resources/provider.py">list</a>(\*\*<a href="src/opencode/types/provider_list_params.py">params</a>) -> <a href="./src/opencode/types/provider_list_response.py">ProviderListResponse</a></code>
- <code title="get /api/provider/{providerID}">client.provider.<a href="./src/opencode/resources/provider.py">get</a>(provider_id, \*\*<a href="src/opencode/types/provider_get_params.py">params</a>) -> <a href="./src/opencode/types/provider_get_response.py">ProviderGetResponse</a></code>

# Pty

Types:

```python
from opencode.types import PtyCreateResponse, PtyUpdateResponse, PtyListResponse, PtyGetResponse
```

Methods:

- <code title="post /api/pty">client.pty.<a href="./src/opencode/resources/pty/pty.py">create</a>(\*\*<a href="src/opencode/types/pty_create_params.py">params</a>) -> <a href="./src/opencode/types/pty_create_response.py">PtyCreateResponse</a></code>
- <code title="put /api/pty/{ptyID}">client.pty.<a href="./src/opencode/resources/pty/pty.py">update</a>(pty_id, \*\*<a href="src/opencode/types/pty_update_params.py">params</a>) -> <a href="./src/opencode/types/pty_update_response.py">PtyUpdateResponse</a></code>
- <code title="get /api/pty">client.pty.<a href="./src/opencode/resources/pty/pty.py">list</a>(\*\*<a href="src/opencode/types/pty_list_params.py">params</a>) -> <a href="./src/opencode/types/pty_list_response.py">PtyListResponse</a></code>
- <code title="get /api/pty/{ptyID}">client.pty.<a href="./src/opencode/resources/pty/pty.py">get</a>(pty_id, \*\*<a href="src/opencode/types/pty_get_params.py">params</a>) -> <a href="./src/opencode/types/pty_get_response.py">PtyGetResponse</a></code>
- <code title="delete /api/pty/{ptyID}">client.pty.<a href="./src/opencode/resources/pty/pty.py">remove</a>(pty_id, \*\*<a href="src/opencode/types/pty_remove_params.py">params</a>) -> None</code>

## Connect

Types:

```python
from opencode.types.pty import ConnectTokenResponse
```

Methods:

- <code title="post /api/pty/{ptyID}/connect-token">client.pty.connect.<a href="./src/opencode/resources/pty/connect.py">token</a>(pty_id, \*\*<a href="src/opencode/types/pty/connect_token_params.py">params</a>) -> <a href="./src/opencode/types/pty/connect_token_response.py">ConnectTokenResponse</a></code>

# Reference

Types:

```python
from opencode.types import ReferenceListResponse
```

Methods:

- <code title="get /api/reference">client.reference.<a href="./src/opencode/resources/reference.py">list</a>(\*\*<a href="src/opencode/types/reference_list_params.py">params</a>) -> <a href="./src/opencode/types/reference_list_response.py">ReferenceListResponse</a></code>

# Rpc

Methods:

- <code title="post /api/rpc/{rpcID}/{method}">client.rpc.<a href="./src/opencode/resources/rpc.py">call</a>(method, \*, rpc_id, \*\*<a href="src/opencode/types/rpc_call_params.py">params</a>) -> <a href="./src/opencode/types/shared/rpc_output.py">RpcOutput</a></code>

# Server

Methods:

- <code title="get /auth/connect/{code}">client.server.<a href="./src/opencode/resources/server.py">connect</a>(code) -> <a href="./src/opencode/types/shared/pairing_session.py">PairingSession</a></code>
- <code title="get /api/info">client.server.<a href="./src/opencode/resources/server.py">info</a>() -> <a href="./src/opencode/types/shared/server_info.py">ServerInfo</a></code>
- <code title="post /api/pair">client.server.<a href="./src/opencode/resources/server.py">pair</a>() -> <a href="./src/opencode/types/shared/pairing_code.py">PairingCode</a></code>

# Session

Types:

```python
from opencode.types import SessionActiveResponse, SessionContextResponse, SessionDiffResponse, SessionGenerateResponse
```

Methods:

- <code title="post /api/session">client.session.<a href="./src/opencode/resources/session/session.py">create</a>(\*\*<a href="src/opencode/types/session_create_params.py">params</a>) -> <a href="./src/opencode/types/shared/session_info.py">SessionInfo</a></code>
- <code title="patch /api/session/{sessionID}">client.session.<a href="./src/opencode/resources/session/session.py">update</a>(session_id, \*\*<a href="src/opencode/types/session_update_params.py">params</a>) -> None</code>
- <code title="get /api/session">client.session.<a href="./src/opencode/resources/session/session.py">list</a>(\*\*<a href="src/opencode/types/session_list_params.py">params</a>) -> <a href="./src/opencode/types/shared/session_info.py">SessionInfo</a></code>
- <code title="get /api/session/active">client.session.<a href="./src/opencode/resources/session/session.py">active</a>() -> <a href="./src/opencode/types/session_active_response.py">SessionActiveResponse</a></code>
- <code title="post /api/session/{sessionID}/background">client.session.<a href="./src/opencode/resources/session/session.py">background</a>(session_id) -> None</code>
- <code title="post /api/session/{sessionID}/command">client.session.<a href="./src/opencode/resources/session/session.py">command</a>(session_id, \*\*<a href="src/opencode/types/session_command_params.py">params</a>) -> None</code>
- <code title="post /api/session/{sessionID}/compact">client.session.<a href="./src/opencode/resources/session/session.py">compact</a>(session_id, \*\*<a href="src/opencode/types/session_compact_params.py">params</a>) -> <a href="./src/opencode/types/shared/session_inbox_compaction.py">SessionInboxCompaction</a></code>
- <code title="get /api/session/{sessionID}/context">client.session.<a href="./src/opencode/resources/session/session.py">context</a>(session_id) -> <a href="./src/opencode/types/session_context_response.py">SessionContextResponse</a></code>
- <code title="get /api/session/{sessionID}/diff">client.session.<a href="./src/opencode/resources/session/session.py">diff</a>(session_id, \*\*<a href="src/opencode/types/session_diff_params.py">params</a>) -> <a href="./src/opencode/types/session_diff_response.py">SessionDiffResponse</a></code>
- <code title="put /api/session/{sessionID}/environment">client.session.<a href="./src/opencode/resources/session/session.py">environment</a>(session_id, \*\*<a href="src/opencode/types/session_environment_params.py">params</a>) -> None</code>
- <code title="get /api/experimental/session/{sessionID}/export">client.session.<a href="./src/opencode/resources/session/session.py">export</a>(session_id, \*\*<a href="src/opencode/types/session_export_params.py">params</a>) -> <a href="./src/opencode/types/shared/session_transfer_data.py">SessionTransferData</a></code>
- <code title="post /api/session/{sessionID}/fork">client.session.<a href="./src/opencode/resources/session/session.py">fork</a>(session_id, \*\*<a href="src/opencode/types/session_fork_params.py">params</a>) -> <a href="./src/opencode/types/shared/session_info.py">SessionInfo</a></code>
- <code title="post /api/session/{sessionID}/generate">client.session.<a href="./src/opencode/resources/session/session.py">generate</a>(session_id, \*\*<a href="src/opencode/types/session_generate_params.py">params</a>) -> <a href="./src/opencode/types/session_generate_response.py">SessionGenerateResponse</a></code>
- <code title="get /api/session/{sessionID}">client.session.<a href="./src/opencode/resources/session/session.py">get</a>(session_id) -> <a href="./src/opencode/types/shared/session_info.py">SessionInfo</a></code>
- <code title="post /api/experimental/session/import">client.session.<a href="./src/opencode/resources/session/session.py">import_</a>(\*\*<a href="src/opencode/types/session_import__params.py">params</a>) -> <a href="./src/opencode/types/shared/session_info.py">SessionInfo</a></code>
- <code title="post /api/session/{sessionID}/interrupt">client.session.<a href="./src/opencode/resources/session/session.py">interrupt</a>(session_id, \*\*<a href="src/opencode/types/session_interrupt_params.py">params</a>) -> <a href="./src/opencode/types/shared/session_interrupt_response.py">SessionInterruptResponse</a></code>
- <code title="get /api/experimental/session/{sessionID}/log">client.session.<a href="./src/opencode/resources/session/session.py">log</a>(session_id, \*\*<a href="src/opencode/types/session_log_params.py">params</a>) -> None</code>
- <code title="post /api/session/{sessionID}/move">client.session.<a href="./src/opencode/resources/session/session.py">move</a>(session_id, \*\*<a href="src/opencode/types/session_move_params.py">params</a>) -> None</code>
- <code title="post /api/session/{sessionID}/prompt">client.session.<a href="./src/opencode/resources/session/session.py">prompt</a>(session_id, \*\*<a href="src/opencode/types/session_prompt_params.py">params</a>) -> <a href="./src/opencode/types/shared/session_inbox_user.py">SessionInboxUser</a></code>
- <code title="delete /api/session/{sessionID}">client.session.<a href="./src/opencode/resources/session/session.py">remove</a>(session_id) -> None</code>
- <code title="post /api/session/{sessionID}/shell">client.session.<a href="./src/opencode/resources/session/session.py">shell</a>(session_id, \*\*<a href="src/opencode/types/session_shell_params.py">params</a>) -> None</code>
- <code title="post /api/experimental/session/{sessionID}/skill">client.session.<a href="./src/opencode/resources/session/session.py">skill</a>(session_id, \*\*<a href="src/opencode/types/session_skill_params.py">params</a>) -> None</code>
- <code title="get /api/experimental/session/stats">client.session.<a href="./src/opencode/resources/session/session.py">stats</a>(\*\*<a href="src/opencode/types/session_stats_params.py">params</a>) -> <a href="./src/opencode/types/shared/session_stats_info.py">SessionStatsInfo</a></code>
- <code title="post /api/session/{sessionID}/agent">client.session.<a href="./src/opencode/resources/session/session.py">switch_agent</a>(session_id, \*\*<a href="src/opencode/types/session_switch_agent_params.py">params</a>) -> None</code>
- <code title="post /api/session/{sessionID}/model">client.session.<a href="./src/opencode/resources/session/session.py">switch_model</a>(session_id, \*\*<a href="src/opencode/types/session_switch_model_params.py">params</a>) -> None</code>
- <code title="post /api/session/{sessionID}/synthetic">client.session.<a href="./src/opencode/resources/session/session.py">synthetic</a>(session_id, \*\*<a href="src/opencode/types/session_synthetic_params.py">params</a>) -> <a href="./src/opencode/types/shared/session_inbox_synthetic.py">SessionInboxSynthetic</a></code>
- <code title="post /api/session/{sessionID}/view">client.session.<a href="./src/opencode/resources/session/session.py">view</a>(session_id, \*\*<a href="src/opencode/types/session_view_params.py">params</a>) -> None</code>
- <code title="post /api/experimental/session/{sessionID}/wait">client.session.<a href="./src/opencode/resources/session/session.py">wait</a>(session_id) -> None</code>

## Revert

Methods:

- <code title="delete /api/session/{sessionID}/revert">client.session.revert.<a href="./src/opencode/resources/session/revert.py">clear</a>(session_id) -> None</code>
- <code title="post /api/session/{sessionID}/revert/commit">client.session.revert.<a href="./src/opencode/resources/session/revert.py">commit</a>(session_id) -> None</code>
- <code title="post /api/session/{sessionID}/revert/stage">client.session.revert.<a href="./src/opencode/resources/session/revert.py">stage</a>(session_id, \*\*<a href="src/opencode/types/session/revert_stage_params.py">params</a>) -> <a href="./src/opencode/types/shared/session_revert.py">SessionRevert</a></code>

## Inbox

Types:

```python
from opencode.types.session import InboxListResponse
```

Methods:

- <code title="patch /api/session/{sessionID}/inbox/{inboxID}">client.session.inbox.<a href="./src/opencode/resources/session/inbox.py">update</a>(inbox_id, \*, session_id, \*\*<a href="src/opencode/types/session/inbox_update_params.py">params</a>) -> None</code>
- <code title="get /api/session/{sessionID}/inbox">client.session.inbox.<a href="./src/opencode/resources/session/inbox.py">list</a>(session_id) -> <a href="./src/opencode/types/session/inbox_list_response.py">InboxListResponse</a></code>
- <code title="delete /api/session/{sessionID}/inbox/{inboxID}">client.session.inbox.<a href="./src/opencode/resources/session/inbox.py">cancel</a>(inbox_id, \*, session_id) -> None</code>

## Instructions

### Entry

Types:

```python
from opencode.types.session.instructions import EntryListResponse
```

Methods:

- <code title="get /api/experimental/session/{sessionID}/instructions/entries">client.session.instructions.entry.<a href="./src/opencode/resources/session/instructions/entry.py">list</a>(session_id) -> <a href="./src/opencode/types/session/instructions/entry_list_response.py">EntryListResponse</a></code>
- <code title="put /api/experimental/session/{sessionID}/instructions/entries/{key}">client.session.instructions.entry.<a href="./src/opencode/resources/session/instructions/entry.py">put</a>(key, \*, session_id, \*\*<a href="src/opencode/types/session/instructions/entry_put_params.py">params</a>) -> None</code>
- <code title="delete /api/experimental/session/{sessionID}/instructions/entries/{key}">client.session.instructions.entry.<a href="./src/opencode/resources/session/instructions/entry.py">remove</a>(key, \*, session_id) -> None</code>

## Message

Methods:

- <code title="get /api/session/{sessionID}/message/{messageID}">client.session.message.<a href="./src/opencode/resources/session/message.py">get</a>(message_id, \*, session_id) -> <a href="./src/opencode/types/shared/session_message_info.py">SessionMessageInfo</a></code>

## Form

Types:

```python
from opencode.types.session import FormListResponse
```

Methods:

- <code title="post /api/session/{sessionID}/form">client.session.form.<a href="./src/opencode/resources/session/form.py">create</a>(session_id, \*\*<a href="src/opencode/types/session/form_create_params.py">params</a>) -> <a href="./src/opencode/types/shared/form_info.py">FormInfo</a></code>
- <code title="get /api/session/{sessionID}/form">client.session.form.<a href="./src/opencode/resources/session/form.py">list</a>(session_id) -> <a href="./src/opencode/types/session/form_list_response.py">FormListResponse</a></code>
- <code title="delete /api/session/{sessionID}/form/{formID}">client.session.form.<a href="./src/opencode/resources/session/form.py">cancel</a>(form_id, \*, session_id, \*\*<a href="src/opencode/types/session/form_cancel_params.py">params</a>) -> None</code>
- <code title="get /api/session/{sessionID}/form/{formID}">client.session.form.<a href="./src/opencode/resources/session/form.py">get</a>(form_id, \*, session_id) -> <a href="./src/opencode/types/shared/form_detail.py">FormDetail</a></code>
- <code title="post /api/session/{sessionID}/form/{formID}/reply">client.session.form.<a href="./src/opencode/resources/session/form.py">reply</a>(form_id, \*, session_id, \*\*<a href="src/opencode/types/session/form_reply_params.py">params</a>) -> None</code>

# Shell

Types:

```python
from opencode.types import ShellCreateResponse, ShellListResponse, ShellGetResponse, ShellOutputResponse
```

Methods:

- <code title="post /api/shell">client.shell.<a href="./src/opencode/resources/shell.py">create</a>(\*\*<a href="src/opencode/types/shell_create_params.py">params</a>) -> <a href="./src/opencode/types/shell_create_response.py">ShellCreateResponse</a></code>
- <code title="get /api/shell">client.shell.<a href="./src/opencode/resources/shell.py">list</a>(\*\*<a href="src/opencode/types/shell_list_params.py">params</a>) -> <a href="./src/opencode/types/shell_list_response.py">ShellListResponse</a></code>
- <code title="get /api/shell/{id}">client.shell.<a href="./src/opencode/resources/shell.py">get</a>(id, \*\*<a href="src/opencode/types/shell_get_params.py">params</a>) -> <a href="./src/opencode/types/shell_get_response.py">ShellGetResponse</a></code>
- <code title="get /api/shell/{id}/output">client.shell.<a href="./src/opencode/resources/shell.py">output</a>(id, \*\*<a href="src/opencode/types/shell_output_params.py">params</a>) -> <a href="./src/opencode/types/shell_output_response.py">ShellOutputResponse</a></code>
- <code title="delete /api/shell/{id}">client.shell.<a href="./src/opencode/resources/shell.py">remove</a>(id, \*\*<a href="src/opencode/types/shell_remove_params.py">params</a>) -> None</code>

# Skill

Types:

```python
from opencode.types import SkillListResponse
```

Methods:

- <code title="get /api/skill">client.skill.<a href="./src/opencode/resources/skill.py">list</a>(\*\*<a href="src/opencode/types/skill_list_params.py">params</a>) -> <a href="./src/opencode/types/skill_list_response.py">SkillListResponse</a></code>

# Vcs

Types:

```python
from opencode.types import VcBaseResponse, VcDiffResponse, VcGetResponse, VcStatusResponse
```

Methods:

- <code title="get /api/vcs/base">client.vcs.<a href="./src/opencode/resources/vcs/vcs.py">base</a>(\*\*<a href="src/opencode/types/vc_base_params.py">params</a>) -> <a href="./src/opencode/types/vc_base_response.py">VcBaseResponse</a></code>
- <code title="get /api/vcs/diff">client.vcs.<a href="./src/opencode/resources/vcs/vcs.py">diff</a>(\*\*<a href="src/opencode/types/vc_diff_params.py">params</a>) -> <a href="./src/opencode/types/vc_diff_response.py">VcDiffResponse</a></code>
- <code title="get /api/vcs">client.vcs.<a href="./src/opencode/resources/vcs/vcs.py">get</a>(\*\*<a href="src/opencode/types/vc_get_params.py">params</a>) -> <a href="./src/opencode/types/vc_get_response.py">VcGetResponse</a></code>
- <code title="post /api/vcs/init">client.vcs.<a href="./src/opencode/resources/vcs/vcs.py">init</a>(\*\*<a href="src/opencode/types/vc_init_params.py">params</a>) -> None</code>
- <code title="get /api/vcs/status">client.vcs.<a href="./src/opencode/resources/vcs/vcs.py">status</a>(\*\*<a href="src/opencode/types/vc_status_params.py">params</a>) -> <a href="./src/opencode/types/vc_status_response.py">VcStatusResponse</a></code>

## Branch

Types:

```python
from opencode.types.vcs import BranchListResponse
```

Methods:

- <code title="get /api/vcs/branch">client.vcs.branch.<a href="./src/opencode/resources/vcs/branch.py">list</a>(\*\*<a href="src/opencode/types/vcs/branch_list_params.py">params</a>) -> <a href="./src/opencode/types/vcs/branch_list_response.py">BranchListResponse</a></code>

# Voice

Types:

```python
from opencode.types import VoiceSessionResponse
```

Methods:

- <code title="post /api/experimental/voice/session">client.voice.<a href="./src/opencode/resources/voice.py">session</a>(\*\*<a href="src/opencode/types/voice_session_params.py">params</a>) -> <a href="./src/opencode/types/voice_session_response.py">VoiceSessionResponse</a></code>

# Websearch

Types:

```python
from opencode.types import WebsearchProvidersResponse, WebsearchQueryResponse
```

Methods:

- <code title="get /api/websearch/provider">client.websearch.<a href="./src/opencode/resources/websearch.py">providers</a>(\*\*<a href="src/opencode/types/websearch_providers_params.py">params</a>) -> <a href="./src/opencode/types/websearch_providers_response.py">WebsearchProvidersResponse</a></code>
- <code title="post /api/websearch">client.websearch.<a href="./src/opencode/resources/websearch.py">query</a>(\*\*<a href="src/opencode/types/websearch_query_params.py">params</a>) -> <a href="./src/opencode/types/websearch_query_response.py">WebsearchQueryResponse</a></code>

# Worktree

Methods:

- <code title="post /api/worktree">client.worktree.<a href="./src/opencode/resources/worktree.py">create</a>(\*\*<a href="src/opencode/types/worktree_create_params.py">params</a>) -> <a href="./src/opencode/types/shared/worktree_info.py">WorktreeInfo</a></code>
- <code title="get /api/worktree">client.worktree.<a href="./src/opencode/resources/worktree.py">list</a>(\*\*<a href="src/opencode/types/worktree_list_params.py">params</a>) -> <a href="./src/opencode/types/shared/worktree_list.py">WorktreeList</a></code>
- <code title="post /api/worktree/refresh">client.worktree.<a href="./src/opencode/resources/worktree.py">refresh</a>(\*\*<a href="src/opencode/types/worktree_refresh_params.py">params</a>) -> None</code>
- <code title="delete /api/worktree">client.worktree.<a href="./src/opencode/resources/worktree.py">remove</a>(\*\*<a href="src/opencode/types/worktree_remove_params.py">params</a>) -> None</code>
