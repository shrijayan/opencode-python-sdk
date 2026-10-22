# Exceptions

See the [errors guide](../guides/errors.md) for the hierarchy and how to catch them.

## Base and status errors

::: opencode.OpencodeError
    options:
      heading_level: 3

::: opencode.APIError
    options:
      heading_level: 3

::: opencode.APIConnectionError
    options:
      heading_level: 3

::: opencode.APITimeoutError
    options:
      heading_level: 3

::: opencode.APIResponseValidationError
    options:
      heading_level: 3

::: opencode.APIStatusError
    options:
      heading_level: 3

::: opencode.BadRequestError
    options:
      heading_level: 3

::: opencode.AuthenticationError
    options:
      heading_level: 3

::: opencode.PermissionDeniedError
    options:
      heading_level: 3

::: opencode.NotFoundError
    options:
      heading_level: 3

::: opencode.ConflictError
    options:
      heading_level: 3

::: opencode.ContentTooLargeError
    options:
      heading_level: 3

::: opencode.UnprocessableEntityError
    options:
      heading_level: 3

::: opencode.RateLimitError
    options:
      heading_level: 3

::: opencode.InternalServerError
    options:
      heading_level: 3

::: opencode.NotImplementedServerError
    options:
      heading_level: 3

::: opencode.ServiceUnavailableError
    options:
      heading_level: 3

## Declared server errors

Raised when the server returns an error it declares in its contract. Each has a typed body on `.error`.

::: opencode.AgentNotFoundError
    options:
      heading_level: 3

::: opencode.CommandExecutionError
    options:
      heading_level: 3

::: opencode.CommandNotFoundError
    options:
      heading_level: 3

::: opencode.ForbiddenError
    options:
      heading_level: 3

::: opencode.FormAlreadySettledError
    options:
      heading_level: 3

::: opencode.FormInvalidAnswerError
    options:
      heading_level: 3

::: opencode.FormNotFoundError
    options:
      heading_level: 3

::: opencode.InstructionEntryValueTooLargeError
    options:
      heading_level: 3

::: opencode.IntegrationAttemptNotFoundError
    options:
      heading_level: 3

::: opencode.IntegrationMethodNotFoundError
    options:
      heading_level: 3

::: opencode.IntegrationNotFoundError
    options:
      heading_level: 3

::: opencode.InvalidCursorError
    options:
      heading_level: 3

::: opencode.InvalidRequestError
    options:
      heading_level: 3

::: opencode.LocationNotFoundError
    options:
      heading_level: 3

::: opencode.McpServerNotFoundError
    options:
      heading_level: 3

::: opencode.MessageNotFoundError
    options:
      heading_level: 3

::: opencode.PermissionNotFoundError
    options:
      heading_level: 3

::: opencode.PermissionSavedNotFoundError
    options:
      heading_level: 3

::: opencode.ProjectNotFoundError
    options:
      heading_level: 3

::: opencode.ProviderNotFoundError
    options:
      heading_level: 3

::: opencode.PtyNotFoundError
    options:
      heading_level: 3

::: opencode.RemoteFileNotFoundError
    options:
      heading_level: 3

::: opencode.RpcError
    options:
      heading_level: 3

::: opencode.RpcInternalError
    options:
      heading_level: 3

::: opencode.SessionBusyError
    options:
      heading_level: 3

::: opencode.SessionNotFoundError
    options:
      heading_level: 3

::: opencode.ShellNotFoundError
    options:
      heading_level: 3

::: opencode.SkillNotFoundError
    options:
      heading_level: 3

::: opencode.UnauthorizedError
    options:
      heading_level: 3

::: opencode.UnknownError
    options:
      heading_level: 3

::: opencode.VcsInitNotSupportedError
    options:
      heading_level: 3

::: opencode.WorktreeError
    options:
      heading_level: 3
