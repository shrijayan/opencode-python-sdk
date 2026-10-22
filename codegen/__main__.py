"""Generates the OpenCode Python client from ``spec/contract.json``.

Usage::

    uv run python -m codegen           # regenerate
    uv run python -m codegen --check   # fail if generated files are stale
"""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
import tempfile
from pathlib import Path

from .operations import build_operations, build_resources
from .render import (
    error_classes,
    render_api_md,
    render_errors,
    render_resource_module,
    render_resources_init,
    render_types,
    render_types_init,
)
from .schemas import TypeRegistry, deduplicate

ROOT = Path(__file__).resolve().parent.parent
CONTRACT = ROOT / "spec" / "contract.json"
PACKAGE = ROOT / "src" / "opencode"
MANIFEST = PACKAGE / ".generated.json"


def generate() -> dict[str, str]:
    """Returns ``{relative path: source}`` for every generated file."""
    contract = json.loads(CONTRACT.read_text())
    version: str = contract["opencodeVersion"]
    definitions, renames = deduplicate(contract["definitions"])
    contract["groups"] = _rewrite_refs(contract["groups"], renames)

    registry = TypeRegistry(definitions)
    for key in sorted(definitions):
        registry.ensure_definition(key)
    operations = build_operations(contract, registry)
    resources = build_resources(operations)
    errors = error_classes(operations, registry)

    files: dict[str, str] = {
        "src/opencode/types/_generated.py": render_types(registry, version),
        "src/opencode/types/__init__.py": render_types_init(registry, version),
        "src/opencode/_errors.py": render_errors(errors, version),
        "src/opencode/resources/__init__.py": render_resources_init(resources, version),
        "api.md": render_api_md(resources, version),
    }
    for name, resource in resources.items():
        files[f"src/opencode/resources/{name}.py"] = render_resource_module(resource, registry, errors, version)

    error_names = [entry["class"] for entry in errors.values() if not entry["is_base"]]
    init = (ROOT / "src/opencode/__init__.py").read_text()
    init = _replace_region(
        init, "error-imports", ["from ._errors import (", *[f"    {name}," for name in error_names], ")"]
    )
    init = _replace_region(init, "error-exports", [f"{name!r}," for name in error_names])
    init = _replace_region(
        init,
        "api-version",
        [f"API_VERSION = {version!r}", '"""The OpenCode server version this client was generated from."""'],
    )
    files["src/opencode/__init__.py"] = init
    return files


def _replace_region(source: str, name: str, lines: list[str]) -> str:
    """Replaces the lines between ``# <generated:name>`` and ``# </generated:name>``, keeping their indentation."""
    start_marker, end_marker = f"# <generated:{name}>", f"# </generated:{name}>"
    start = source.index(start_marker)
    end = source.index(end_marker)
    indent = source[source.rfind("\n", 0, start) + 1 : start]
    body = "".join(f"{indent}{line}\n" for line in lines)
    return source[: start + len(start_marker)] + "\n" + body + indent + source[end:]


def _rewrite_refs(value: object, renames: dict[str, str]) -> object:
    if isinstance(value, dict):
        result: dict[str, object] = {}
        for key, item in value.items():
            if key == "$ref" and isinstance(item, str):
                name = item.removeprefix("#/$defs/")
                while name in renames:
                    name = renames[name]
                result[key] = f"#/$defs/{name}"
            else:
                result[key] = _rewrite_refs(item, renames)
        return result
    if isinstance(value, list):
        return [_rewrite_refs(item, renames) for item in value]
    return value


def _format(directory: Path) -> None:
    python_files = [str(path) for path in directory.rglob("*.py")]
    if not python_files:
        return
    ruff = [sys.executable, "-m", "ruff"]
    config = ["--config", str(ROOT / "pyproject.toml")]
    subprocess.run([*ruff, "check", "--fix-only", "--quiet", *config, *python_files], check=True, cwd=ROOT)
    subprocess.run([*ruff, "format", "--quiet", *config, *python_files], check=True, cwd=ROOT)


def main() -> int:
    parser = argparse.ArgumentParser(prog="python -m codegen", description=__doc__)
    parser.add_argument("--check", action="store_true", help="exit with status 1 if generated files are out of date")
    args = parser.parse_args()

    files = generate()
    with tempfile.TemporaryDirectory() as tmp:
        staging = Path(tmp)
        for relative, source in files.items():
            target = staging / relative
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text(source)
        _format(staging)
        rendered = {relative: (staging / relative).read_text() for relative in files}

    previous = set(json.loads(MANIFEST.read_text())) if MANIFEST.exists() else set()
    stale = sorted(previous - set(rendered))
    changed = [
        relative
        for relative, source in rendered.items()
        if not (ROOT / relative).exists() or (ROOT / relative).read_text() != source
    ]

    if args.check:
        if changed or stale:
            for relative in [*changed, *stale]:
                print(f"out of date: {relative}")
            print("Run `uv run python -m codegen` and commit the result.")
            return 1
        print("Generated files are up to date.")
        return 0

    for relative in stale:
        (ROOT / relative).unlink(missing_ok=True)
    for relative, source in rendered.items():
        target = ROOT / relative
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(source)
    MANIFEST.write_text(json.dumps(sorted(rendered), indent=2) + "\n")
    print(f"Generated {len(rendered)} files ({len(changed)} changed, {len(stale)} removed).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
