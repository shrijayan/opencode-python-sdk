# API reference

Generated from the OpenCode 2.1.2 contract. Every method exists on both `Opencode` and `AsyncOpencode`;
async methods return awaitables, async list methods return `AsyncPaginator`, and async streams return
`AsyncStream`. Types live in `opencode.types`.

## `client.agent`

| Method | HTTP | Returns | Summary |
| --- | --- | --- | --- |
| `list()` | `GET /api/agent` | `AgentListResponse` | List agents |
| `get(agent_id)` | `GET /api/agent/:agentID` | `AgentGetResponse` | Get agent |

## `client.command`

| Method | HTTP | Returns | Summary |
| --- | --- | --- | --- |
| `list()` | `GET /api/command` | `CommandListResponse` | List commands |

## `client.config`

| Method | HTTP | Returns | Summary |
| --- | --- | --- | --- |
| `get()` | `GET /api/config` | `list[ConfigEntry]` | Get configuration |
| `shells()` | `GET /api/config/shell` | `list[ConfigShellOption]` | List available shells |
| `update()` | `PATCH /api/experimental/config` | `None` | Update global configuration *(experimental)* |

## `client.credential`

| Method | HTTP | Returns | Summary |
| --- | --- | --- | --- |
| `list()` | `GET /api/credential` | `list[CredentialEntry]` | List credentials |
| `create()` | `POST /api/credential` | `CredentialEntry` | Create credential |
| `update(credential_id)` | `PATCH /api/credential/:credentialID` | `None` | Update credential |
| `activate(credential_id)` | `POST /api/credential/:credentialID/activate` | `None` | Activate credential |
| `remove(credential_id)` | `DELETE /api/credential/:credentialID` | `None` | Remove credential |

## `client.debug.location`

| Method | HTTP | Returns | Summary |
| --- | --- | --- | --- |
| `list()` | `GET /api/debug/location` | `list[LocationPublicRef]` | List loaded locations |
| `evict()` | `DELETE /api/debug/location` | `None` | Evict a loaded location |

## `client.event`

| Method | HTTP | Returns | Summary |
| --- | --- | --- | --- |
| `subscribe()` | `GET /api/event` | `Stream[Event]` | Subscribe to events |

## `client.experimental.persistent_pty`

| Method | HTTP | Returns | Summary |
| --- | --- | --- | --- |
| `read(session_id)` | `GET /api/experimental/session/:sessionID/terminal/read` | `PersistentPtyReadResult &#124; None` | Read the session's most recently controlled terminal *(experimental)* |
| `list(session_id)` | `GET /api/experimental/session/:sessionID/terminal` | `list[PersistentPtyInfo]` |  *(experimental)* |
| `create(session_id)` | `POST /api/experimental/session/:sessionID/terminal` | `PersistentPtyInfo` |  *(experimental)* |
| `shutdown()` | `POST /api/experimental/persistent-pty/shutdown` | `None` |  *(experimental)* |
| `handoff()` | `POST /api/experimental/persistent-pty/handoff` | `ExperimentalPersistentPtyHandoffResponse` |  *(experimental)* |
| `get(pty_id)` | `GET /api/experimental/persistent-pty/:ptyID` | `PersistentPtyInfo` |  *(experimental)* |
| `update(pty_id)` | `PUT /api/experimental/persistent-pty/:ptyID` | `PersistentPtyInfo` |  *(experimental)* |
| `snapshot(pty_id)` | `GET /api/experimental/persistent-pty/:ptyID/snapshot` | `PersistentPtySnapshot` |  *(experimental)* |
| `remove(pty_id)` | `DELETE /api/experimental/persistent-pty/:ptyID` | `None` |  *(experimental)* |
| `connect_token(pty_id)` | `POST /api/experimental/persistent-pty/:ptyID/connect-token` | `PtyTicketConnectToken` |  *(experimental)* |

## `client.file`

| Method | HTTP | Returns | Summary |
| --- | --- | --- | --- |
| `read(path)` | `GET /api/fs/read/*` | `bytes` | Read file |
| `list()` | `GET /api/fs/list` | `FileListResponse` | List directory |
| `find()` | `GET /api/fs/find` | `FileFindResponse` | Find files |
| `write()` | `POST /api/experimental/fs/write` | `FileWriteResponse` | Write file *(experimental)* |

## `client.form`

| Method | HTTP | Returns | Summary |
| --- | --- | --- | --- |
| `list()` | `GET /api/form` | `FormListResponse` | List pending forms |

## `client.generate`

| Method | HTTP | Returns | Summary |
| --- | --- | --- | --- |
| `text()` | `POST /api/experimental/generate` | `GenerateTextResponseData` | Generate text *(experimental)* |

## `client.integration`

| Method | HTTP | Returns | Summary |
| --- | --- | --- | --- |
| `list()` | `GET /api/integration` | `IntegrationListResponse` | List integrations |
| `get(integration_id)` | `GET /api/integration/:integrationID` | `IntegrationGetResponse` | Get integration |

## `client.integration.wellknown`

| Method | HTTP | Returns | Summary |
| --- | --- | --- | --- |
| `add()` | `POST /api/experimental/integration/wellknown` | `None` | Add wellknown integration *(experimental)* |

## `client.integration.connect`

| Method | HTTP | Returns | Summary |
| --- | --- | --- | --- |
| `key(integration_id)` | `POST /api/integration/:integrationID/connect/key` | `None` | Connect with key |
| `external(integration_id)` | `POST /api/integration/:integrationID/connect/external` | `None` | Connect with external credentials |

## `client.integration.oauth`

| Method | HTTP | Returns | Summary |
| --- | --- | --- | --- |
| `connect(integration_id)` | `POST /api/integration/:integrationID/connect/oauth` | `IntegrationOauthConnectResponse` | Begin OAuth connection |
| `status(integration_id, attempt_id)` | `GET /api/integration/:integrationID/connect/oauth/:attemptID` | `IntegrationOauthStatusResponse` | Get OAuth attempt status |
| `complete(integration_id, attempt_id)` | `POST /api/integration/:integrationID/connect/oauth/:attemptID/complete` | `None` | Complete OAuth connection |
| `cancel(integration_id, attempt_id)` | `DELETE /api/integration/:integrationID/connect/oauth/:attemptID` | `None` | Cancel OAuth connection |

## `client.integration.command`

| Method | HTTP | Returns | Summary |
| --- | --- | --- | --- |
| `connect(integration_id)` | `POST /api/integration/:integrationID/connect/command` | `IntegrationCommandConnectResponse` | Begin command connection |
| `status(integration_id, attempt_id)` | `GET /api/integration/:integrationID/connect/command/:attemptID` | `IntegrationCommandStatusResponse` | Get command attempt status |
| `cancel(integration_id, attempt_id)` | `DELETE /api/integration/:integrationID/connect/command/:attemptID` | `None` | Cancel command connection |

## `client.location`

| Method | HTTP | Returns | Summary |
| --- | --- | --- | --- |
| `get()` | `GET /api/location` | `LocationPublicInfo` | Get location |
| `reload()` | `POST /api/location/reload` | `None` | Reload configuration |

## `client.mcp`

| Method | HTTP | Returns | Summary |
| --- | --- | --- | --- |
| `list()` | `GET /api/mcp` | `McpListResponse` | List MCP servers |
| `add(server)` | `PUT /api/experimental/mcp/:server` | `None` | Add MCP server *(experimental)* |
| `remove(server)` | `DELETE /api/experimental/mcp/:server` | `None` | Remove MCP server *(experimental)* |
| `connect(server)` | `POST /api/experimental/mcp/:server/connect` | `None` | Connect MCP server *(experimental)* |
| `disconnect(server)` | `POST /api/experimental/mcp/:server/disconnect` | `None` | Disconnect MCP server *(experimental)* |

## `client.mcp.resource`

| Method | HTTP | Returns | Summary |
| --- | --- | --- | --- |
| `catalog()` | `GET /api/mcp/resource` | `McpResourceCatalogResponse` | List MCP resources |

## `client.message`

| Method | HTTP | Returns | Summary |
| --- | --- | --- | --- |
| `list(session_id)` | `GET /api/session/:sessionID/message` | `SyncCursorPage[SessionMessageInfo]` | Get session messages |

## `client.migration.v1`

| Method | HTTP | Returns | Summary |
| --- | --- | --- | --- |
| `status()` | `GET /api/experimental/migration/v1` | `MigrationV1StatusResponseOption1 &#124; MigrationV1StatusResponseOption2 &#124; MigrationV1StatusResponseOption3` | Get V1 migration status *(experimental)* |

## `client.model`

| Method | HTTP | Returns | Summary |
| --- | --- | --- | --- |
| `list()` | `GET /api/model` | `ModelListResponse` | List models |
| `default()` | `GET /api/model/default` | `ModelDefaultResponse` | Get default model |

## `client.permission`

| Method | HTTP | Returns | Summary |
| --- | --- | --- | --- |
| `create(session_id)` | `POST /api/session/:sessionID/permission` | `PermissionCreateResponse` | Create permission request |
| `list(session_id)` | `GET /api/session/:sessionID/permission` | `list[PermissionRequest]` | List session permission requests |
| `get(session_id, request_id)` | `GET /api/session/:sessionID/permission/:requestID` | `PermissionRequest` | Get permission request |
| `reply(session_id, request_id)` | `POST /api/session/:sessionID/permission/:requestID/reply` | `None` | Reply to pending permission request |

## `client.permission.request_`

| Method | HTTP | Returns | Summary |
| --- | --- | --- | --- |
| `list()` | `GET /api/permission/request` | `PermissionRequestListResponse` | List pending permission requests |

## `client.permission.saved`

| Method | HTTP | Returns | Summary |
| --- | --- | --- | --- |
| `list()` | `GET /api/permission/saved` | `list[PermissionSavedInfo]` | List saved permissions |
| `update(id)` | `PATCH /api/permission/saved/:id` | `PermissionSavedInfo` | Update saved permission |
| `remove(id)` | `DELETE /api/permission/saved/:id` | `None` | Remove saved permission |

## `client.plugin`

| Method | HTTP | Returns | Summary |
| --- | --- | --- | --- |
| `list()` | `GET /api/plugin` | `PluginListResponse` | List plugins |
| `check()` | `POST /api/plugin/check` | `PluginCheckResponse` | Check plugin updates |
| `update()` | `POST /api/plugin/update` | `None` | Update plugins |

## `client.project`

| Method | HTTP | Returns | Summary |
| --- | --- | --- | --- |
| `list()` | `GET /api/project` | `list[Project]` | List projects |
| `update(project_id)` | `PATCH /api/project/:projectID` | `Project` | Update project |

## `client.provider`

| Method | HTTP | Returns | Summary |
| --- | --- | --- | --- |
| `list()` | `GET /api/provider` | `ProviderListResponse` | List providers |
| `get(provider_id)` | `GET /api/provider/:providerID` | `ProviderGetResponse` | Get provider |

## `client.pty`

| Method | HTTP | Returns | Summary |
| --- | --- | --- | --- |
| `list()` | `GET /api/pty` | `PtyListResponse` | List PTY sessions |
| `create()` | `POST /api/pty` | `PtyCreateResponse` | Create PTY session |
| `get(pty_id)` | `GET /api/pty/:ptyID` | `PtyGetResponse` | Get PTY session |
| `update(pty_id)` | `PUT /api/pty/:ptyID` | `PtyUpdateResponse` | Update PTY session |
| `remove(pty_id)` | `DELETE /api/pty/:ptyID` | `None` | Remove PTY session |

## `client.pty.connect`

| Method | HTTP | Returns | Summary |
| --- | --- | --- | --- |
| `token(pty_id)` | `POST /api/pty/:ptyID/connect-token` | `PtyConnectTokenResponse` | Create PTY WebSocket token |

## `client.reference`

| Method | HTTP | Returns | Summary |
| --- | --- | --- | --- |
| `list()` | `GET /api/reference` | `ReferenceListResponse` | List references |

## `client.rpc`

| Method | HTTP | Returns | Summary |
| --- | --- | --- | --- |
| `call(rpc_id, method)` | `POST /api/rpc/:rpcID/:method` | `RpcOutput` | Call a plugin RPC |

## `client.server`

| Method | HTTP | Returns | Summary |
| --- | --- | --- | --- |
| `info()` | `GET /api/info` | `ServerInfo` | Get server info |
| `pair()` | `POST /api/pair` | `PairingCode` | Create pairing code |
| `connect(code)` | `GET /auth/connect/:code` | `PairingSession` | Redeem pairing code |

## `client.session`

| Method | HTTP | Returns | Summary |
| --- | --- | --- | --- |
| `list()` | `GET /api/session` | `SyncCursorPage[SessionInfo]` | List sessions |
| `stats()` | `GET /api/experimental/session/stats` | `SessionStatsInfo` | Get session statistics *(experimental)* |
| `create()` | `POST /api/session` | `SessionInfo` | Create session |
| `import_()` | `POST /api/experimental/session/import` | `SessionInfo` | Import session *(experimental)* |
| `export(session_id)` | `GET /api/experimental/session/:sessionID/export` | `SessionTransferData` | Export session *(experimental)* |
| `active()` | `GET /api/session/active` | `dict[str, Any]` | List active sessions |
| `get(session_id)` | `GET /api/session/:sessionID` | `SessionInfo` | Get session |
| `remove(session_id)` | `DELETE /api/session/:sessionID` | `None` | Delete session |
| `fork(session_id)` | `POST /api/session/:sessionID/fork` | `SessionInfo` | Fork session |
| `switch_agent(session_id)` | `POST /api/session/:sessionID/agent` | `None` | Switch session agent |
| `switch_model(session_id)` | `POST /api/session/:sessionID/model` | `None` | Switch session model |
| `update(session_id)` | `PATCH /api/session/:sessionID` | `None` | Update session |
| `move(session_id)` | `POST /api/session/:sessionID/move` | `None` | Move session |
| `prompt(session_id)` | `POST /api/session/:sessionID/prompt` | `SessionInboxUser` | Send message |
| `command(session_id)` | `POST /api/session/:sessionID/command` | `None` | Run command |
| `skill(session_id)` | `POST /api/experimental/session/:sessionID/skill` | `None` | Activate skill *(experimental)* |
| `synthetic(session_id)` | `POST /api/session/:sessionID/synthetic` | `SessionInboxSynthetic` | Add synthetic message |
| `shell(session_id)` | `POST /api/session/:sessionID/shell` | `None` | Run shell command |
| `compact(session_id)` | `POST /api/session/:sessionID/compact` | `SessionInboxCompaction` | Compact session |
| `wait(session_id)` | `POST /api/experimental/session/:sessionID/wait` | `None` | Wait for session *(experimental)* |
| `context(session_id)` | `GET /api/session/:sessionID/context` | `list[SessionMessageInfo]` | Get session context |
| `diff(session_id)` | `GET /api/session/:sessionID/diff` | `list[FileDiffInfo]` | Diff session turns |
| `generate(session_id)` | `POST /api/session/:sessionID/generate` | `SessionGenerateResponseData` | Generate text from session context |
| `log(session_id)` | `GET /api/experimental/session/:sessionID/log` | `Stream[SessionLogItem]` | Read the session log *(experimental)* |
| `interrupt(session_id)` | `POST /api/session/:sessionID/interrupt` | `SessionInterruptResponse` | Interrupt session execution |
| `background(session_id)` | `POST /api/session/:sessionID/background` | `None` | Background blocking session tools |
| `environment(session_id)` | `PUT /api/session/:sessionID/environment` | `None` | Set session environment |
| `view(session_id)` | `POST /api/session/:sessionID/view` | `None` | View session |

## `client.session.revert`

| Method | HTTP | Returns | Summary |
| --- | --- | --- | --- |
| `stage(session_id)` | `POST /api/session/:sessionID/revert/stage` | `SessionRevert` | Stage session revert |
| `clear(session_id)` | `DELETE /api/session/:sessionID/revert` | `None` | Clear staged revert |
| `commit(session_id)` | `POST /api/session/:sessionID/revert/commit` | `None` | Commit staged revert |

## `client.session.inbox`

| Method | HTTP | Returns | Summary |
| --- | --- | --- | --- |
| `list(session_id)` | `GET /api/session/:sessionID/inbox` | `list[SessionInboxInfo]` | List session inbox |
| `cancel(session_id, inbox_id)` | `DELETE /api/session/:sessionID/inbox/:inboxID` | `None` | Cancel inbox input |
| `update(session_id, inbox_id)` | `PATCH /api/session/:sessionID/inbox/:inboxID` | `None` | Update inbox item |

## `client.session.instructions.entry`

| Method | HTTP | Returns | Summary |
| --- | --- | --- | --- |
| `list(session_id)` | `GET /api/experimental/session/:sessionID/instructions/entries` | `list[InstructionEntryInfo]` | List instruction entries *(experimental)* |
| `put(session_id, key)` | `PUT /api/experimental/session/:sessionID/instructions/entries/:key` | `None` | Put instruction entry *(experimental)* |
| `remove(session_id, key)` | `DELETE /api/experimental/session/:sessionID/instructions/entries/:key` | `None` | Remove instruction entry *(experimental)* |

## `client.session.message`

| Method | HTTP | Returns | Summary |
| --- | --- | --- | --- |
| `get(session_id, message_id)` | `GET /api/session/:sessionID/message/:messageID` | `SessionMessageInfo` | Get session message |

## `client.session.form`

| Method | HTTP | Returns | Summary |
| --- | --- | --- | --- |
| `list(session_id)` | `GET /api/session/:sessionID/form` | `list[FormInfo]` | List session forms |
| `create(session_id)` | `POST /api/session/:sessionID/form` | `FormInfo` | Create session form |
| `get(session_id, form_id)` | `GET /api/session/:sessionID/form/:formID` | `FormDetail` | Get session form |
| `reply(session_id, form_id)` | `POST /api/session/:sessionID/form/:formID/reply` | `None` | Reply to form |
| `cancel(session_id, form_id)` | `DELETE /api/session/:sessionID/form/:formID` | `None` | Cancel form |

## `client.shell`

| Method | HTTP | Returns | Summary |
| --- | --- | --- | --- |
| `list()` | `GET /api/shell` | `ShellListResponse` | List running shell commands |
| `create()` | `POST /api/shell` | `ShellCreateResponse` | Run shell command |
| `get(id)` | `GET /api/shell/:id` | `ShellGetResponse` | Get shell command |
| `output(id)` | `GET /api/shell/:id/output` | `ShellOutputResponse` | Read shell output |
| `remove(id)` | `DELETE /api/shell/:id` | `None` | Remove shell command |

## `client.skill`

| Method | HTTP | Returns | Summary |
| --- | --- | --- | --- |
| `list()` | `GET /api/skill` | `SkillListResponse` | List skills |

## `client.vcs`

| Method | HTTP | Returns | Summary |
| --- | --- | --- | --- |
| `init()` | `POST /api/vcs/init` | `None` | Initialize VCS repository |
| `get()` | `GET /api/vcs` | `VcsGetResponse` | VCS info |
| `base()` | `GET /api/vcs/base` | `VcsBaseResponse` | VCS review base |
| `status()` | `GET /api/vcs/status` | `VcsStatusResponse` | VCS status |
| `diff()` | `GET /api/vcs/diff` | `VcsDiffResponse` | VCS diff |

## `client.vcs.branch`

| Method | HTTP | Returns | Summary |
| --- | --- | --- | --- |
| `list()` | `GET /api/vcs/branch` | `VcsBranchListResponse` | VCS branches |

## `client.voice`

| Method | HTTP | Returns | Summary |
| --- | --- | --- | --- |
| `session()` | `POST /api/experimental/voice/session` | `VoiceSessionResponseData` | Create voice session *(experimental)* |

## `client.websearch`

| Method | HTTP | Returns | Summary |
| --- | --- | --- | --- |
| `providers()` | `GET /api/websearch/provider` | `WebsearchProvidersResponse` | List web search providers |
| `query()` | `POST /api/websearch` | `WebsearchQueryResponse` | Search the web |

## `client.worktree`

| Method | HTTP | Returns | Summary |
| --- | --- | --- | --- |
| `list()` | `GET /api/worktree` | `WorktreeList` | List worktrees |
| `create()` | `POST /api/worktree` | `WorktreeInfo` | Create worktree |
| `remove()` | `DELETE /api/worktree` | `None` | Remove worktree |
| `refresh()` | `POST /api/worktree/refresh` | `None` | Refresh worktrees |
