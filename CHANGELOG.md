# Changelog

All notable changes to this project are documented here. The format follows
[Keep a Changelog](https://keepachangelog.com/en/1.1.0/) and the project uses
[semantic versioning](https://semver.org/).

## [0.1.0] - Unreleased

First release, generated from OpenCode 2.1.2.

### Added

- `Opencode` and `AsyncOpencode` clients covering all 142 operations of the OpenCode 2.1 server API.
- Typed pydantic models for every schema and 96 event types, with forward-compatible enums and union fallbacks.
- Typed exceptions for every error the server declares, plus status-based base classes.
- Cursor pagination, server-sent event streams, retries with backoff, and per-request options.
- `OpencodeServer` and `AsyncOpencodeServer` to run `opencode serve` as a child process.
- Contract extractor and code generator, with CI checks that generated code is current.
