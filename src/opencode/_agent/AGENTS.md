# Using opencode 0.0.1

Instructions for coding agents writing code that uses the `opencode` package.

- Read `SKILL.md` next to this file first: install, authentication (`OPENCODE_PASSWORD`), one example per resource and error handling, for this exact version.
- Look up method signatures and types in `api.md` (https://github.com//blob/main/api.md); every request and response type is importable from `opencode.types`.
- Construct one `Opencode` (or `AsyncOpencode`) and reuse it; do not pass secrets in code.
- Catch `opencode.APIError` subclasses rather than `httpx` errors; retries and timeouts are already built in.
- Do not edit generated files of the SDK; they are regenerated from the API spec.
