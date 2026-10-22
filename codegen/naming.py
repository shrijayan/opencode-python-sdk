"""Name conversion rules shared by the generator."""

from __future__ import annotations

import builtins
import keyword
import re

import pydantic

_WORD_SPLIT = re.compile(r"[^0-9A-Za-z]+")
_ACRONYM_BOUNDARY = re.compile(r"([A-Z]+)([A-Z][a-z])")
_CASE_BOUNDARY = re.compile(r"([a-z0-9])([A-Z])")

PYTHON_RESERVED = frozenset(keyword.kwlist) | frozenset(keyword.softkwlist) - {"_", "type", "match", "case"}
"""Names that cannot be used as identifiers. Soft keywords other than these are fine as names."""

MODEL_RESERVED = frozenset(name for name in dir(pydantic.BaseModel) if not name.startswith("__")) | {
    "to_dict",
    "to_json",
}
"""Attribute names that would shadow ``pydantic.BaseModel`` or :class:`opencode.BaseModel` members."""

BUILTIN_NAMES = frozenset(dir(builtins))


def pascal(name: str) -> str:
    """``session.message.user`` -> ``SessionMessageUser``; inner capitals are kept (``persistentPty`` -> ``PersistentPty``)."""
    parts = [part for part in _WORD_SPLIT.split(name) if part]
    return "".join(part[0].upper() + part[1:] for part in parts)


def snake(name: str) -> str:
    """``parentID`` -> ``parent_id``, ``x-opencode-ticket`` -> ``x_opencode_ticket``, ``_tag`` -> ``tag``."""
    value = _WORD_SPLIT.sub("_", name)
    value = _ACRONYM_BOUNDARY.sub(r"\1_\2", value)
    value = _CASE_BOUNDARY.sub(r"\1_\2", value)
    value = re.sub(r"_+", "_", value).strip("_").lower()
    if not value:
        raise ValueError(f"Cannot derive a Python name from {name!r}")
    if value[0].isdigit():
        value = f"n{value}"
    return value


def safe_identifier(name: str, *, reserved: frozenset[str] = frozenset()) -> str:
    """Appends ``_`` until the name is not a keyword or one of ``reserved``."""
    while name in PYTHON_RESERVED or name in reserved:
        name = f"{name}_"
    return name


def docstring(text: str | None, indent: str) -> str | None:
    """Formats text as a triple-quoted docstring body, or returns ``None`` when there is nothing to say."""
    if text is None:
        return None
    text = text.strip()
    if not text:
        return None
    text = text.replace("\\", "\\\\").replace('"""', '\\"\\"\\"')
    if text.endswith('"'):
        text += " "
    lines = text.splitlines()
    if len(lines) == 1:
        return f'{indent}"""{lines[0]}"""'
    body = "\n".join(f"{indent}{line}".rstrip() for line in lines[1:])
    return f'{indent}"""{lines[0]}\n{body}\n{indent}"""'
