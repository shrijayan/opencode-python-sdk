"""MkDocs hook that generates the resource and type reference pages and fills version placeholders.

`opencode.types` holds ~640 generated models. One page per model would bloat the nav and one page for all of them
would be unusable, so this groups them by domain (the leading word of the class name, with events and session
messages split out) and writes one page per group. Pages are generated at build time from the source, so they
never drift from the code.
"""

from __future__ import annotations

import re
import ast
from typing import TYPE_CHECKING, Any
from pathlib import Path
from collections import defaultdict

if TYPE_CHECKING:
    from mkdocs.structure.files import Files

ROOT = Path(__file__).resolve().parents[2]
TYPES_SRC = ROOT / "src/opencode/types/_generated.py"
RESOURCES_DIR = ROOT / "src/opencode/resources"
TYPES_DIR = "reference/types"
MIN_GROUP = 4

GROUP_TITLES = {
    "Mcp": "MCP",
    "Pty": "PTY",
    "Rpc": "RPC",
    "Vcs": "VCS",
    "Tui": "TUI",
    "Persistent": "Persistent PTY",
    "Websearch": "Web search",
}


def _public_names() -> list[str]:
    tree = ast.parse(TYPES_SRC.read_text())
    names: list[str] = []
    for node in tree.body:
        if isinstance(node, ast.ClassDef):
            names.append(node.name)
        elif isinstance(node, ast.AnnAssign) and isinstance(node.target, ast.Name):
            names.append(node.target.id)
        elif isinstance(node, ast.Assign) and len(node.targets) == 1 and isinstance(node.targets[0], ast.Name):
            names.append(node.targets[0].id)
    return [n for n in names if not n.startswith("_") and n[0].isupper() and n != "__all__"]


def _group_of(name: str) -> str:
    if name.endswith("Event"):
        return "Events"
    words = re.findall(r"[A-Z][a-z0-9]*", name)
    if name.endswith("ErrorBody"):
        return "Error bodies"
    if words[0] == "Session" and len(words) > 1 and words[1] == "Message":
        return "Session messages"
    if words[0] == "Sessions":
        return "Session"
    return words[0]


def _slug(title: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", title.lower()).strip("-")


def type_groups() -> dict[str, list[str]]:
    raw: dict[str, list[str]] = defaultdict(list)
    for name in _public_names():
        raw[_group_of(name)].append(name)
    groups: dict[str, list[str]] = defaultdict(list)
    for key, names in raw.items():
        target = key if len(names) >= MIN_GROUP or key in {"Events", "Error bodies"} else "Miscellaneous"
        groups[GROUP_TITLES.get(target, target)].extend(names)
    return dict(sorted(groups.items(), key=lambda kv: (kv[0] == "Miscellaneous", kv[0].lower())))


def type_page(title: str, names: list[str]) -> str:
    lines = [f"# {title}", "", f"{len(names)} types. Import any of them from `opencode.types`.", ""]
    for name in sorted(names):
        lines += [
            f"::: opencode.types.{name}",
            "    options:",
            "      heading_level: 2",
            "      show_bases: false",
            "      show_signature: false",
            "      members_order: source",
            "",
        ]
    return "\n".join(lines)


def _types_index(groups: dict[str, list[str]]) -> str:
    total = sum(len(v) for v in groups.values())
    lines = [
        "# Types",
        "",
        f"`opencode.types` has {total} generated models, unions and aliases, one for every request, response and "
        "event in the OpenCode contract. They are grouped by domain below. Use search (++slash++) to jump to a "
        "type by name.",
        "",
        "| Group | Types | Examples |",
        "| --- | ---: | --- |",
    ]
    for title, names in groups.items():
        sample = ", ".join(f"`{n}`" for n in sorted(names)[:3])
        lines.append(f"| [{title}]({_slug(title)}.md) | {len(names)} | {sample} |")
    return "\n".join(lines) + "\n"


def resources_page() -> str:
    lines = [
        "# Resources",
        "",
        "Every resource is reachable as an attribute of the client, for example `client.session`. Each sync class "
        "below has an `Async` twin with the same methods, which return awaitables. The method list with HTTP routes "
        "is also in [api.md](https://github.com/shrijayan/opencode-python-sdk/blob/main/api.md).",
        "",
    ]
    for path in sorted(RESOURCES_DIR.glob("*.py")):
        if path.name.startswith("_"):
            continue
        tree = ast.parse(path.read_text())
        classes = [
            n.name
            for n in tree.body
            if isinstance(n, ast.ClassDef) and not n.name.startswith("Async") and n.name.endswith("Resource")
        ]
        for cls in classes:
            lines += [f"::: opencode.resources.{path.stem}.{cls}", "    options:", "      show_bases: false", ""]
    return "\n".join(lines)


_GROUPS: dict[str, list[str]] = {}


def on_config(config: Any) -> Any:
    _GROUPS.clear()
    _GROUPS.update(type_groups())
    for section in config["nav"]:
        if "API reference" not in section:
            continue
        for i, item in enumerate(section["API reference"]):
            if isinstance(item, dict) and "Types" in item:
                pages: list[Any] = [f"{TYPES_DIR}/index.md"]
                pages += [{title: f"{TYPES_DIR}/{_slug(title)}.md"} for title in _GROUPS]
                section["API reference"][i] = {"Types": pages}
    return config


def _read_constant(path: Path, name: str) -> str:
    match = re.search(rf'^{name}\s*=\s*"([^"]+)"', path.read_text(), re.M)
    return match.group(1) if match else "unknown"


def on_page_markdown(markdown: str, page: Any, config: Any, files: Files) -> str:
    """Fills ``{{ version }}`` and ``{{ api_version }}`` from the package source."""
    version = _read_constant(ROOT / "src/opencode/_version.py", "__version__")
    api_version = _read_constant(ROOT / "src/opencode/__init__.py", "API_VERSION")
    return markdown.replace("{{ version }}", version).replace("{{ api_version }}", api_version)


def on_files(files: Files, config: Any) -> Files:
    from mkdocs.structure.files import File

    def add(path: str, content: str) -> None:
        files.append(File.generated(config, path, content=content))

    add(f"{TYPES_DIR}/index.md", _types_index(_GROUPS))
    for title, names in _GROUPS.items():
        add(f"{TYPES_DIR}/{_slug(title)}.md", type_page(title, names))
    add("reference/resources.md", resources_page())
    return files


_PAGES: list[tuple[str, str, str]] = []


def on_page_content(html: str, page: Any, config: Any, files: Files) -> str:
    """Records hand-written pages for ``llms.txt``. Generated reference pages are left out: they are huge."""
    if not page.file.generated_by and page.file.src_uri.endswith(".md"):
        markdown = re.sub(
            r'^--8<-- "([^"]+)"$', lambda m: (ROOT / m.group(1)).read_text(), page.markdown or "", flags=re.M
        )
        _PAGES.append((page.title or page.file.src_uri, page.url, markdown))
    return html


def on_pre_build(config: Any) -> None:
    _PAGES.clear()


def on_post_build(config: Any) -> None:
    """Writes ``llms.txt`` (an index, per llmstxt.org) and ``llms-full.txt`` (every hand-written page)."""
    base = config["site_url"]
    site = Path(config["site_dir"])
    pages = sorted(_PAGES, key=lambda p: p[1])
    index = [
        f"# {config['site_name']}",
        "",
        f"> {config['site_description']} Install with `pip install opencode-python-sdk`; import as `opencode`.",
        "",
        "## Docs",
        "",
    ]
    index += [f"- [{title}]({base}{url})" for title, url, _ in pages]
    index += [
        "",
        "## Optional",
        "",
        f"- [Full docs as one file]({base}llms-full.txt)",
        "- [Method table with HTTP routes](https://github.com/shrijayan/opencode-python-sdk/blob/main/api.md)",
    ]
    (site / "llms.txt").write_text("\n".join(index) + "\n")
    full = [f"# {config['site_name']}\n\n> {config['site_description']}\n"]
    full += [f"\n---\n\nSource: {base}{url}\n\n{markdown.strip()}\n" for _, url, markdown in pages]
    (site / "llms-full.txt").write_text("".join(full))
