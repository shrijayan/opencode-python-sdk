# File generated from our OpenAPI spec by Ferrule. See CONTRIBUTING.md for details.

from typing import Union
from typing_extensions import TypeAlias

from .rpc_event import RpcEvent
from .pty_exited_event import PtyExitedEvent
from .pty_created_event import PtyCreatedEvent
from .pty_deleted_event import PtyDeletedEvent
from .pty_updated_event import PtyUpdatedEvent
from .form_created_event import FormCreatedEvent
from .form_replied_event import FormRepliedEvent
from .session_idle_event import SessionIdleEvent
from .shell_exited_event import ShellExitedEvent
from .agent_updated_event import AgentUpdatedEvent
from .model_updated_event import ModelUpdatedEvent
from .session_moved_event import SessionMovedEvent
from .shell_created_event import ShellCreatedEvent
from .shell_deleted_event import ShellDeletedEvent
from .skill_updated_event import SkillUpdatedEvent
from .config_updated_event import ConfigUpdatedEvent
from .form_cancelled_event import FormCancelledEvent
from .plugin_updated_event import PluginUpdatedEvent
from .session_forked_event import SessionForkedEvent
from .session_viewed_event import SessionViewedEvent
from .tui_toast_show_event import TuiToastShowEvent
from .command_updated_event import CommandUpdatedEvent
from .project_updated_event import ProjectUpdatedEvent
from .session_created_event import SessionCreatedEvent
from .session_deleted_event import SessionDeletedEvent
from .session_renamed_event import SessionRenamedEvent
from .permission_asked_event import PermissionAskedEvent
from .provider_updated_event import ProviderUpdatedEvent
from .server_connected_event import ServerConnectedEvent
from .session_archived_event import SessionArchivedEvent
from .session_status_updated import SessionStatusUpdated
from .worktree_updated_event import WorktreeUpdatedEvent
from .location_shutdown_event import LocationShutdownEvent
from .reference_updated_event import ReferenceUpdatedEvent
from .session_synthetic_event import SessionSyntheticEvent
from .tui_prompt_append_event import TuiPromptAppendEvent
from .websearch_updated_event import WebsearchUpdatedEvent
from .worktree_resolved_event import WorktreeResolvedEvent
from .credential_updated_event import CredentialUpdatedEvent
from .filesystem_changed_event import FilesystemChangedEvent
from .mcp_status_changed_event import McpStatusChangedEvent
from .permission_replied_event import PermissionRepliedEvent
from .session_step_ended_event import SessionStepEndedEvent
from .session_text_delta_event import SessionTextDeltaEvent
from .session_text_ended_event import SessionTextEndedEvent
from .session_unarchived_event import SessionUnarchivedEvent
from .tui_session_select_event import TuiSessionSelectEvent
from .vcs_branch_updated_event import VcsBranchUpdatedEvent
from .credential_switched_event import CredentialSwitchedEvent
from .integration_updated_event import IntegrationUpdatedEvent
from .session_permissions_event import SessionPermissionsEvent
from .session_shell_ended_event import SessionShellEndedEvent
from .session_step_failed_event import SessionStepFailedEvent
from .session_tool_called_event import SessionToolCalledEvent
from .session_tool_failed_event import SessionToolFailedEvent
from .tui_command_execute_event import TuiCommandExecuteEvent
from .installation_updated_event import InstallationUpdatedEvent
from .models_dev_refreshed_event import ModelsDevRefreshedEvent
from .persistent_pty_added_event import PersistentPtyAddedEvent
from .session_step_started_event import SessionStepStartedEvent
from .session_text_started_event import SessionTextStartedEvent
from .session_tool_success_event import SessionToolSuccessEvent
from .mcp_resources_changed_event import McpResourcesChangedEvent
from .session_revert_staged_event import SessionRevertStagedEvent
from .session_shell_started_event import SessionShellStartedEvent
from .session_step_streamed_event import SessionStepStreamedEvent
from .session_tool_progress_event import SessionToolProgressEvent
from .session_usage_updated_event import SessionUsageUpdatedEvent
from .persistent_pty_removed_event import PersistentPtyRemovedEvent
from .session_agent_selected_event import SessionAgentSelectedEvent
from .session_inbox_enqueued_event import SessionInboxEnqueuedEvent
from .session_model_selected_event import SessionModelSelectedEvent
from .session_revert_cleared_event import SessionRevertClearedEvent
from .session_inbox_cancelled_event import SessionInboxCancelledEvent
from .session_inbox_delivered_event import SessionInboxDeliveredEvent
from .session_reasoning_delta_event import SessionReasoningDeltaEvent
from .session_reasoning_ended_event import SessionReasoningEndedEvent
from .session_retry_scheduled_event import SessionRetryScheduledEvent
from .session_skill_activated_event import SessionSkillActivatedEvent
from .session_compaction_delta_event import SessionCompactionDeltaEvent
from .session_compaction_ended_event import SessionCompactionEndedEvent
from .session_execution_failed_event import SessionExecutionFailedEvent
from .session_metadata_updated_event import SessionMetadataUpdatedEvent
from .session_revert_committed_event import SessionRevertCommittedEvent
from .session_tool_input_delta_event import SessionToolInputDeltaEvent
from .session_tool_input_ended_event import SessionToolInputEndedEvent
from .session_compaction_failed_event import SessionCompactionFailedEvent
from .session_execution_started_event import SessionExecutionStartedEvent
from .session_reasoning_started_event import SessionReasoningStartedEvent
from .session_compaction_started_event import SessionCompactionStartedEvent
from .session_tool_input_started_event import SessionToolInputStartedEvent
from .session_execution_succeeded_event import SessionExecutionSucceededEvent
from .session_instructions_updated_event import SessionInstructionsUpdatedEvent
from .installation_update_available_event import InstallationUpdateAvailableEvent
from .session_execution_interrupted_event import SessionExecutionInterruptedEvent
from .session_inbox_delivery_changed_event import SessionInboxDeliveryChangedEvent

__all__ = ["Event"]

Event: TypeAlias = Union[
    LocationShutdownEvent,
    ModelsDevRefreshedEvent,
    CredentialUpdatedEvent,
    CredentialSwitchedEvent,
    IntegrationUpdatedEvent,
    ProviderUpdatedEvent,
    ModelUpdatedEvent,
    AgentUpdatedEvent,
    SessionCreatedEvent,
    SessionAgentSelectedEvent,
    SessionModelSelectedEvent,
    SessionMovedEvent,
    SessionRenamedEvent,
    SessionMetadataUpdatedEvent,
    SessionPermissionsEvent,
    SessionViewedEvent,
    SessionArchivedEvent,
    SessionUnarchivedEvent,
    SessionUsageUpdatedEvent,
    SessionDeletedEvent,
    SessionForkedEvent,
    SessionInboxDeliveredEvent,
    SessionInboxEnqueuedEvent,
    SessionInboxCancelledEvent,
    SessionInboxDeliveryChangedEvent,
    SessionExecutionStartedEvent,
    SessionExecutionSucceededEvent,
    SessionExecutionFailedEvent,
    SessionExecutionInterruptedEvent,
    SessionInstructionsUpdatedEvent,
    SessionSyntheticEvent,
    SessionSkillActivatedEvent,
    SessionShellStartedEvent,
    SessionShellEndedEvent,
    SessionStepStartedEvent,
    SessionStepStreamedEvent,
    SessionStepEndedEvent,
    SessionStepFailedEvent,
    SessionTextStartedEvent,
    SessionTextDeltaEvent,
    SessionTextEndedEvent,
    SessionReasoningStartedEvent,
    SessionReasoningDeltaEvent,
    SessionReasoningEndedEvent,
    SessionToolInputStartedEvent,
    SessionToolInputDeltaEvent,
    SessionToolInputEndedEvent,
    SessionToolCalledEvent,
    SessionToolProgressEvent,
    SessionToolSuccessEvent,
    SessionToolFailedEvent,
    SessionRetryScheduledEvent,
    SessionCompactionStartedEvent,
    SessionCompactionDeltaEvent,
    SessionCompactionEndedEvent,
    SessionCompactionFailedEvent,
    SessionRevertStagedEvent,
    SessionRevertClearedEvent,
    SessionRevertCommittedEvent,
    FilesystemChangedEvent,
    ReferenceUpdatedEvent,
    PermissionAskedEvent,
    PermissionRepliedEvent,
    PluginUpdatedEvent,
    ProjectUpdatedEvent,
    WorktreeUpdatedEvent,
    WorktreeResolvedEvent,
    CommandUpdatedEvent,
    ConfigUpdatedEvent,
    SkillUpdatedEvent,
    PtyCreatedEvent,
    PtyUpdatedEvent,
    PtyExitedEvent,
    PtyDeletedEvent,
    PersistentPtyAddedEvent,
    PersistentPtyRemovedEvent,
    ShellCreatedEvent,
    ShellExitedEvent,
    ShellDeletedEvent,
    FormCreatedEvent,
    FormRepliedEvent,
    FormCancelledEvent,
    WebsearchUpdatedEvent,
    SessionStatusUpdated,
    SessionIdleEvent,
    TuiPromptAppendEvent,
    TuiCommandExecuteEvent,
    TuiToastShowEvent,
    TuiSessionSelectEvent,
    InstallationUpdatedEvent,
    InstallationUpdateAvailableEvent,
    VcsBranchUpdatedEvent,
    McpStatusChangedEvent,
    McpResourcesChangedEvent,
    RpcEvent,
    ServerConnectedEvent,
]
