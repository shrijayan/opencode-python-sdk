# Copyright 2026 Ferrule contributors
# SPDX-License-Identifier: Apache-2.0
# Copied from https://github.com/shrijayan/ferrule/blob/ea62784146f05b4f15ccdf269f30f6fcf7b98c60/scripts/opencode/config_models.py
# Modified by The Ferrule Authors: Json is a TypeAlias, for Python 3.10.
"""Name every schema of the opencode spec as a model in its stainless.yml.

The opencode SDK exports each ``$defs`` entry of ``spec/contract.json`` from ``opencode.types``
under the name its own generator gave it (``Agent.Info`` -> ``AgentInfo``,
``Session.NotFoundErrorEncoded`` -> ``SessionNotFoundErrorBody``, ``session.created`` ->
``SessionCreatedEvent``). ``models:`` is how a stainless.yml keeps such names, so this script
writes one model per component schema, under ``$shared``, keyed by that name in snake case, and
the ``custom_casings`` that spell the keys back as the SDK does (``ConfigLSPServer``,
``MoneyUSD``). Both go between marker comments, so a new spec is applied by running it again;
the rest of the config is left as written, except that a method of an endpoint whose ``data``
the SDK returns (``x-opencode-unwrap-data``) gets ``unwrap_response: data``.

``apply`` is pure and deterministic; only ``main`` touches files. See ADR 0015.
"""

from __future__ import annotations

import re
import json
import argparse
from typing import Any, TypeAlias, cast
from pathlib import Path

Json: TypeAlias = dict[str, Any]

MODELS_BEGIN = "  # <ferrule:models> written by scripts/opencode/config_models.py"
MODELS_END = "  # </ferrule:models>"
CASINGS_BEGIN = "# <ferrule:casings> written by scripts/opencode/config_models.py"
CASINGS_END = "# </ferrule:casings>"
SCHEMAS_PREFIX = "#/components/schemas/"

# Words Stainless spells upper-case in class names unless custom_casings says otherwise
# (crates/converter/src/extensions/casings.rs DEFAULT_INITIALISMS).
DEFAULT_INITIALISMS = frozenset(
    {
        "3ds", "ach", "acl", "ai", "api", "ats", "cpu", "crm", "db", "dns", "e2e", "eeoc", "gb",
        "gpu", "hd", "hris", "html", "http", "https", "id", "ip", "iso", "jsonl", "kb", "kyb",
        "kyc", "lfs", "mb", "mp3", "mp4", "nft", "saml", "sdk", "sku", "sms", "ss", "ssh", "sso",
        "url",
    }
)  # fmt: skip

_WORD_SPLIT = re.compile(r"[^0-9A-Za-z]+")
_ACRONYM_BOUNDARY = re.compile(r"([A-Z]+)([A-Z][a-z])")
_CASE_BOUNDARY = re.compile(r"([a-z0-9])([A-Z])")
_NUMBERED = re.compile(r"^(.*)_(\d+)$")


class ModelsError(ValueError):
    """Raised when two schemas get one name, or the config has no place for the models."""


def pascal(name: str) -> str:
    """``session.message.user`` -> ``SessionMessageUser``, inner capitals kept."""
    return "".join(part[0].upper() + part[1:] for part in _WORD_SPLIT.split(name) if part)


def words(name: str) -> list[str]:
    """``ConfigLSPServer`` -> ``["Config", "LSP", "Server"]``, as the SDK splits names."""
    spaced = _CASE_BOUNDARY.sub(r"\1 \2", _ACRONYM_BOUNDARY.sub(r"\1 \2", name))
    return [w for w in _WORD_SPLIT.split(spaced.replace(" ", "_")) if w]


def python_name(key: str) -> str:
    """Return the class or alias name the SDK's generator gives the definition ``key``."""
    suffix = ""
    numbered = _NUMBERED.match(key)
    if numbered:
        key, suffix = numbered.group(1), numbered.group(2)
    if key == "V2Event":
        name = "Event"
    elif key.startswith("V2Event."):
        name = pascal(key.removeprefix("V2Event.")) + "Event"
    elif key[:1].islower():
        name = pascal(key) + "Event"
    else:
        name = key.removesuffix("Encoded")
        if key.endswith("Encoded") and name.endswith("Error"):
            name += "Body"
        name = pascal(name)
    return name + suffix


def _ref_counts(node: object, counts: dict[str, int]) -> dict[str, int]:
    """Count the ``$ref`` to each component schema under ``node``."""
    if isinstance(node, dict):
        ref = cast("Json", node).get("$ref")
        if isinstance(ref, str) and ref.startswith(SCHEMAS_PREFIX):
            name = ref.removeprefix(SCHEMAS_PREFIX)
            counts[name] = counts.get(name, 0) + 1
        for value in cast("Json", node).values():
            _ref_counts(value, counts)
    elif isinstance(node, list):
        for value in cast("list[object]", node):
            _ref_counts(value, counts)
    return counts


def envelopes(spec: Json) -> set[str]:
    """Return the schemas used only as the response of an endpoint whose ``data`` is returned.

    Those are not part of the API once unwrapped, and their names are the ones the unwrapped
    types get (``GenerateTextResponse``), so they are no models.
    """
    as_envelope: dict[str, int] = {}
    for item in cast("Json", spec.get("paths", {})).values():
        for op in cast("Json", item).values():
            if isinstance(op, dict) and cast("Json", op).get("x-opencode-unwrap-data"):
                content = cast("Json", op).get("responses", {}).get("200", {}).get("content", {})
                schema = content.get("application/json", {}).get("schema", {})
                ref = schema.get("$ref", "")
                if ref.startswith(SCHEMAS_PREFIX):
                    name = ref.removeprefix(SCHEMAS_PREFIX)
                    as_envelope[name] = as_envelope.get(name, 0) + 1
    everywhere = _ref_counts(spec, {})
    return {name for name, n in as_envelope.items() if everywhere.get(name) == n}


def model_entries(spec: Json) -> list[tuple[str, str]]:
    """``(model key, schema name)`` for every component schema but the envelopes, by key."""
    schemas = cast("Json", spec.get("components", {})).get("schemas", {})
    skip = envelopes(spec)
    entries: dict[str, str] = {}
    for schema in sorted(cast("Json", schemas)):
        if schema in skip:
            continue
        key = "_".join(w.lower() for w in words(python_name(schema)))
        if key in entries:
            msg = f"{schema} and {entries[key]} are both named {key}"
            raise ModelsError(msg)
        entries[key] = schema
    return sorted(entries.items())


def default_spelling(word: str) -> str:
    """How Stainless spells ``word`` (lower case) in a class name without custom casings."""
    return word.upper() if word in DEFAULT_INITIALISMS else word[:1].upper() + word[1:]


def casings(spec: Json) -> dict[str, Json]:
    """Return the ``custom_casings`` spelling every model key as the SDK names its schema."""
    wanted: dict[str, str] = {}
    for _, schema in model_entries(spec):
        for word in words(python_name(schema)):
            low = word.lower()
            if wanted.setdefault(low, word) != word:
                msg = f"{low} is spelled both {wanted[low]} and {word}"
                raise ModelsError(msg)
    out: dict[str, Json] = {}
    for low, word in sorted(wanted.items()):
        if word == default_spelling(low):
            continue
        if word == low.upper():
            out[low] = {"initialism": True}
        elif word == low[:1].upper() + low[1:]:
            out[low] = {"initialism": False}
        else:
            out[low] = {"pascal": word}
    return out


def models_block(spec: Json) -> str:
    """Return the ``$shared`` resource with every model, between its markers."""
    lines = [MODELS_BEGIN, "  $shared:", "    models:"]
    lines += [f'      {key}: "{SCHEMAS_PREFIX}{schema}"' for key, schema in model_entries(spec)]
    return "\n".join([*lines, MODELS_END])


def casings_block(spec: Json) -> str:
    """Return the top-level ``custom_casings``, between its markers."""
    lines = [CASINGS_BEGIN, "custom_casings:"]
    for word, casing in casings(spec).items():
        (field, value), *_ = casing.items()
        lines.append(f"  {word}: {{ {field}: {json.dumps(value)} }}")
    return "\n".join([*lines, CASINGS_END])


def _replace(text: str, markers: tuple[str, str], block: str, anchor: str, *, after: bool) -> str:
    begin, end = markers
    if begin in text:
        head, rest = text.split(begin, 1)
        if end not in rest:
            msg = f"{begin.strip()} has no {end.strip()}"
            raise ModelsError(msg)
        return head + block + rest.split(end, 1)[1]
    if anchor not in text:
        msg = f"the config has no {anchor.strip()!r} line"
        raise ModelsError(msg)
    placed = anchor + block + "\n" if after else "\n" + block + anchor
    return text.replace(anchor, placed, 1)


_METHOD_LINE = re.compile(
    r"^(?P<indent> +)(?P<name>\w+): (?P<verb>get|post|put|patch|delete) (?P<path>\S+)$",
    re.MULTILINE,
)


def unwrapped(spec: Json) -> set[str]:
    """Return the ``verb path`` endpoints whose ``data`` the SDK returns."""
    found: set[str] = set()
    for path, item in cast("Json", spec.get("paths", {})).items():
        for verb, op in cast("Json", item).items():
            if isinstance(op, dict) and cast("Json", op).get("x-opencode-unwrap-data"):
                found.add(f"{verb} {path}")
    return found


def unwrap_methods(config: str, spec: Json) -> str:
    """Write each method of an unwrapped endpoint as ``{endpoint, unwrap_response: data}``."""
    wanted = unwrapped(spec)

    def rewrite(m: re.Match[str]) -> str:
        endpoint = f"{m['verb']} {m['path']}"
        if endpoint not in wanted or m["name"] == "endpoint":
            return m.group(0)
        pad = m["indent"] + "  "
        return f"{m['indent']}{m['name']}:\n{pad}endpoint: {endpoint}\n{pad}unwrap_response: data"

    return _METHOD_LINE.sub(rewrite, config)


def apply(config: str, spec: Json) -> str:
    """``config`` with its models, casings and unwrapped methods rewritten for ``spec``."""
    models = models_block(spec)
    text = _replace(config, (MODELS_BEGIN, MODELS_END), models, "\nresources:\n", after=True)
    casing = casings_block(spec)
    text = _replace(text, (CASINGS_BEGIN, CASINGS_END), casing, "\nreadme:\n", after=False)
    return unwrap_methods(text, spec)


def main(argv: list[str] | None = None) -> int:
    """Rewrite the models and casings of a stainless.yml from an OpenAPI document."""
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0] if __doc__ else None)
    parser.add_argument("spec", type=Path)
    parser.add_argument("config", type=Path)
    args = parser.parse_args(argv)
    config = cast("Path", args.config)
    spec = json.loads(cast("Path", args.spec).read_text(encoding="utf-8"))
    config.write_text(apply(config.read_text(encoding="utf-8"), spec), encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
