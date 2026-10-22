# Contributing

Thanks for helping. This project is a generated client with a small hand-written runtime, so most changes fall
into one of two places.

## Setup

```bash
uv sync
uv run pytest -m "not live"
```

Live tests start a real `opencode serve` and need the [OpenCode CLI](https://opencode.ai) on `PATH`. They make no
model calls and use a temporary data directory:

```bash
uv run pytest -m live
```

## Checks

CI runs all of these; run them before opening a pull request.

```bash
uv run ruff check .
uv run ruff format --check .
uv run pyright
uv run mypy
uv run python -m codegen --check
uv run pytest
```

## Layout

| Path | What it is | Edit by hand? |
| --- | --- | --- |
| `codegen/extract/` | Exports the OpenCode contract from `@opencode/protocol` | Yes |
| `spec/contract.json` | The exported contract | No, run the extractor |
| `codegen/*.py` | The Python code generator | Yes |
| `src/opencode/types/`, `src/opencode/resources/`, `src/opencode/_errors.py`, `api.md` | Generated code | No |
| `src/opencode/_*.py` (other) | Transport, retries, streaming, pagination, launcher | Yes |
| `tests/` | Tests | Yes |

## Updating to a new OpenCode version

The `Sync OpenCode spec` workflow does this nightly and opens a pull request. To do it locally:

```bash
cd codegen/extract
bun add --exact --ignore-scripts @opencode/protocol@<version> effect@<matching version>
bun run extract.ts
cd ../..
uv run python -m codegen
```

Then review the diff of `api.md` and update the README version table if the OpenCode minor version changed.

## Changing generated code

Change the generator in `codegen/`, run `uv run python -m codegen`, and commit both the generator change and the
regenerated files. Never edit generated files directly; CI will reject the change.

## Releases

Releases are automatic. Every merge to `main` that changes `src/`, `spec/` or `pyproject.toml` runs CI, picks the
next version from the merged commit subjects, publishes to PyPI and creates a GitHub release with generated notes.
Docs, tests and CI changes alone do not release.

Use [Conventional Commits](https://www.conventionalcommits.org/) subjects; with rebase merging, every commit lands
on `main` as written:

| Subject | Bump |
| --- | --- |
| `fix: handle empty cursor` | patch |
| `feat: add session.run helper` | minor |
| `feat!: rename Opencode.server` or a `BREAKING CHANGE:` footer | major (minor while below 1.0) |
| anything else (`chore:`, `refactor:`, ...) | patch |

The version comes from git tags (`hatch-vcs`); there is no version number to edit. To release without package
changes, run the Release workflow manually with **force**.
