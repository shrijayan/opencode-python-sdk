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

## Documentation

The site in `docs/` is built with MkDocs Material and mkdocstrings. The API reference is generated from docstrings
at build time by `docs/hooks/types_reference.py`.

```bash
uv sync --group docs
uv run mkdocs serve
uv run mkdocs build --strict
```

### Docs must keep up with the code

A change to the public API is not done until the docs cover it. CI enforces this:

| Check | Where | Fails when |
| --- | --- | --- |
| `tests/test_docs_coverage.py` | `pytest` job | A resource, method, `opencode.__all__` name or `opencode.types` model is not in the reference; an exported class or one of its public methods has no docstring; a resource group is missing from `docs/guides/index.md`; a guide mentions a method or type that does not exist |
| ruff `D1` rules | Lint job | A public function in a public module has no docstring |
| `mkdocs build --strict` | Docs workflow | A link or cross-reference is broken |

Each failure names what is missing and the file to change. In practice:

- **New endpoint or resource group** (from a spec sync): resource and type pages are generated from the code, so
  they appear on their own. Add a row for a new group to `docs/guides/index.md`.
- **New hand-written class or function exported from `opencode`**: give it a docstring and add a `::: opencode.Name`
  directive to the right page in `docs/reference/`.
- **Renamed or removed API**: update every guide that mentions it.

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
