# Guide index

Every resource group on the client, and where it is documented. Every group has a reference
entry; the common ones also have a guide. CI fails if a group on the client is missing from this table
(see `tests/test_docs_coverage.py`).

| Group | What it covers | Guide | Reference |
| --- | --- | --- | --- |
| `client.agent` | List and inspect agents | - | [`AgentResource`](../reference/resources.md#opencode.resources.agent.AgentResource) |
| `client.command` | List slash commands | - | [`CommandResource`](../reference/resources.md#opencode.resources.command.CommandResource) |
| `client.config` | Read and update configuration | - | [`ConfigResource`](../reference/resources.md#opencode.resources.config.ConfigResource) |
| `client.credential` | Manage provider credentials | - | [`CredentialResource`](../reference/resources.md#opencode.resources.credential.CredentialResource) |
| `client.debug` | Inspect loaded locations | - | [`DebugResource`](../reference/resources.md#opencode.resources.debug.DebugResource) |
| `client.event` | Subscribe to server events | [Guide](events.md) | [`EventResource`](../reference/resources.md#opencode.resources.event.EventResource) |
| `client.experimental` | Experimental endpoints, such as persistent terminals | - | [`ExperimentalResource`](../reference/resources.md#opencode.resources.experimental.ExperimentalResource) |
| `client.file` | Read, list, find and write files | - | [`FileResource`](../reference/resources.md#opencode.resources.file.FileResource) |
| `client.form` | List pending forms | - | [`FormResource`](../reference/resources.md#opencode.resources.form.FormResource) |
| `client.generate` | One-off text generation | - | [`GenerateResource`](../reference/resources.md#opencode.resources.generate.GenerateResource) |
| `client.integration` | Connect and manage integrations | - | [`IntegrationResource`](../reference/resources.md#opencode.resources.integration.IntegrationResource) |
| `client.location` | Project locations the server knows | - | [`LocationResource`](../reference/resources.md#opencode.resources.location.LocationResource) |
| `client.mcp` | MCP servers and their resources | - | [`McpResource`](../reference/resources.md#opencode.resources.mcp.McpResource) |
| `client.message` | Read session messages | [Guide](sessions.md) | [`MessageResource`](../reference/resources.md#opencode.resources.message.MessageResource) |
| `client.migration` | Data migrations | - | [`MigrationResource`](../reference/resources.md#opencode.resources.migration.MigrationResource) |
| `client.model` | List models | - | [`ModelResource`](../reference/resources.md#opencode.resources.model.ModelResource) |
| `client.permission` | Answer and manage permission requests | - | [`PermissionResource`](../reference/resources.md#opencode.resources.permission.PermissionResource) |
| `client.plugin` | List plugins | - | [`PluginResource`](../reference/resources.md#opencode.resources.plugin.PluginResource) |
| `client.project` | Projects | - | [`ProjectResource`](../reference/resources.md#opencode.resources.project.ProjectResource) |
| `client.provider` | Model providers | - | [`ProviderResource`](../reference/resources.md#opencode.resources.provider.ProviderResource) |
| `client.pty` | Terminals | [Interactive terminals](terminals.md) | [`PtyResource`](../reference/resources.md#opencode.resources.pty.PtyResource) |
| `client.reference` | References | - | [`ReferenceResource`](../reference/resources.md#opencode.resources.reference.ReferenceResource) |
| `client.rpc` | Plugin RPC | - | [`RpcResource`](../reference/resources.md#opencode.resources.rpc.RpcResource) |
| `client.server` | Server info and health | - | [`ServerResource`](../reference/resources.md#opencode.resources.server.ServerResource) |
| `client.session` | Sessions, prompts and their sub-resources | [Guide](sessions.md) | [`SessionResource`](../reference/resources.md#opencode.resources.session.SessionResource) |
| `client.shell` | Shells | - | [`ShellResource`](../reference/resources.md#opencode.resources.shell.ShellResource) |
| `client.skill` | Skills | - | [`SkillResource`](../reference/resources.md#opencode.resources.skill.SkillResource) |
| `client.vcs` | Version control status and branches | - | [`VcsResource`](../reference/resources.md#opencode.resources.vcs.VcsResource) |
| `client.voice` | Voice input | - | [`VoiceResource`](../reference/resources.md#opencode.resources.voice.VoiceResource) |
| `client.websearch` | Web search | - | [`WebsearchResource`](../reference/resources.md#opencode.resources.websearch.WebsearchResource) |
| `client.worktree` | Git worktrees | - | [`WorktreeResource`](../reference/resources.md#opencode.resources.worktree.WorktreeResource) |
