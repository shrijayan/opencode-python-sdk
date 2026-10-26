# Copyright 2026 Ferrule contributors
# SPDX-License-Identifier: Apache-2.0
# Copied from https://github.com/shrijayan/ferrule/blob/ea62784146f05b4f15ccdf269f30f6fcf7b98c60/scripts/opencode/contract_to_openapi.py
# Modified by The Ferrule Authors: Json is a TypeAlias, for Python 3.10.
"""Convert the opencode SDK's ``spec/contract.json`` into an OpenAPI 3.1 document.

``contract.json`` is exported from the Effect ``HttpApi`` definitions in ``@opencode/protocol``.
It lists groups of endpoints and a ``$defs`` table of JSON Schemas. This module maps:

- each group to an OpenAPI tag,
- each endpoint to an operation (``:name`` and ``*`` path segments become ``{name}``),
- ``params``/``query``/``headers``/``wildcard`` inputs to parameters,
- ``payload`` inputs to a JSON (``struct``) or octet-stream (``binary``) request body,
- ``value``/``void``/``stream``/``binary`` successes and tagged errors to responses,
- ``$defs`` to ``components.schemas``, with Effect's ``Struct`` + ``Record`` intersection and
  ``NonEmptyArray`` written in the plain form generators read.

``convert`` is pure and deterministic; only ``main`` touches files. See ADR 0015.
"""

from __future__ import annotations

import sys
import json
import argparse
from typing import Any, cast
from pathlib import Path
from typing_extensions import TypeAlias

Json: TypeAlias = dict[str, Any]

DEFS_PREFIX = "#/$defs/"
COMPONENTS_PREFIX = "#/components/schemas/"
SOURCE_TO_LOCATION = {"params": "path", "wildcard": "path", "query": "query", "headers": "header"}


class ContractError(ValueError):
    """Raised when ``contract.json`` has a shape this converter does not know."""


def rewrite_refs(node: object) -> object:
    """Return ``node`` with every ``#/$defs/`` reference pointed at ``components.schemas``."""
    if isinstance(node, dict):
        out: Json = {}
        for key, value in cast("Json", node).items():
            if key == "$schema":
                continue
            if key == "$ref" and isinstance(value, str) and value.startswith(DEFS_PREFIX):
                out[key] = COMPONENTS_PREFIX + value.removeprefix(DEFS_PREFIX)
            else:
                out[key] = rewrite_refs(value)
        return fold_non_empty_array(fold_record(out))
    if isinstance(node, list):
        return [rewrite_refs(item) for item in cast("list[object]", node)]
    return node


def fold_non_empty_array(schema: Json) -> Json:
    """Drop the ``prefixItems`` of Effect's ``NonEmptyArray``: its one entry repeats ``items``.

    ``minItems: 1`` already says the array is not empty; generators that read only ``items``
    (Forge) otherwise see no item type. A real tuple (``prefixItems`` that differ) is kept.
    """
    prefix = schema.get("prefixItems")
    if (
        schema.get("type") != "array"
        or not isinstance(prefix, list)
        or cast("list[object]", prefix) != [schema.get("items")]
    ):
        return schema
    return {key: value for key, value in schema.items() if key != "prefixItems"}


def _is_record(member: object) -> bool:
    return isinstance(member, dict) and set(cast("Json", member)) == {
        "type",
        "additionalProperties",
    }


def fold_record(schema: Json) -> Json:
    """Fold Effect's ``Struct`` + ``Record`` intersection into one object schema.

    Effect encodes ``Schema.Struct({...}, Schema.Record(...))`` as an object whose ``allOf``
    holds only ``{"type": "object", "additionalProperties": X}``. That is the same schema as the
    object with ``additionalProperties: X``, which generators handle without an ``allOf``.
    """
    members = schema.get("allOf")
    if (
        schema.get("type") != "object"
        or "additionalProperties" in schema
        or not isinstance(members, list)
        or len(cast("list[object]", members)) != 1
        or not _is_record(cast("list[object]", members)[0])
    ):
        return schema
    record = cast("list[Json]", members)[0]
    folded = {key: value for key, value in schema.items() if key != "allOf"}
    folded["additionalProperties"] = record["additionalProperties"]
    return folded


def convert_path(path: str) -> str:
    """Turn ``/a/:id/b/*`` into the OpenAPI template ``/a/{id}/b/{path}``."""
    segments: list[str] = []
    for segment in path.split("/"):
        if segment.startswith(":"):
            segments.append("{" + segment[1:] + "}")
        elif segment == "*":
            segments.append("{path}")
        else:
            segments.append(segment)
    return "/".join(segments)


def _is_object(schema: Json) -> bool:
    if schema.get("type") == "object":
        return True
    variants = cast("list[Json]", schema.get("anyOf", []))
    return any(variant.get("type") == "object" for variant in variants)


def _parameter(item: Json) -> Json:
    location = SOURCE_TO_LOCATION[item["source"]]
    schema = cast("Json", rewrite_refs(item["schema"]))
    param: Json = {
        "name": item["name"],
        "in": location,
        "required": location == "path" or not item["optional"],
        "schema": schema,
    }
    if location == "query" and _is_object(schema):
        # Forge covers only ``form`` style; nested keys are encoded by query_settings.
        param["style"] = "form"
        param["explode"] = True
    return param


def _request_body(endpoint: Json, payload: list[Json]) -> Json | None:
    if not payload:
        return None
    mode = cast("Json", endpoint.get("payload") or {}).get("mode", "struct")
    if mode == "binary":
        content: Json = {"application/octet-stream": {"schema": {"type": "string", "format": "binary"}}}
        return {"required": True, "content": content}
    if mode != "struct":
        msg = f"{endpoint['operationId']}: unknown payload mode {mode!r}"
        raise ContractError(msg)
    properties = {item["name"]: rewrite_refs(item["schema"]) for item in payload}
    required = [item["name"] for item in payload if not item["optional"]]
    schema: Json = {"type": "object", "properties": properties}
    if required:
        schema["required"] = required
    return {"required": bool(required), "content": {"application/json": {"schema": schema}}}


def _success(endpoint: Json) -> tuple[str, Json]:
    success = cast("Json", endpoint["success"])
    status = str(success["status"])
    kind = success["kind"]
    description = endpoint.get("summary") or "Success"
    response: Json = {"description": description}
    if kind == "void":
        return status, response
    if kind == "value":
        media = "application/json"
        schema = rewrite_refs(success["schema"])
    elif kind == "stream":
        media = "text/event-stream"
        schema = rewrite_refs(success["schema"])
    elif kind == "binary":
        media = "application/octet-stream"
        schema = {"type": "string", "format": "binary"}
    else:
        msg = f"{endpoint['operationId']}: unknown success kind {kind!r}"
        raise ContractError(msg)
    response["content"] = {media: {"schema": schema}}
    return status, response


def _errors(endpoint: Json) -> dict[str, Json]:
    by_status: dict[str, list[Json]] = {}
    for error in cast("list[Json]", endpoint["errors"]):
        by_status.setdefault(str(error["status"]), []).append(error)
    responses: dict[str, Json] = {}
    for status in sorted(by_status):
        errors = by_status[status]
        schemas = [rewrite_refs(error["schema"]) for error in errors]
        schema = schemas[0] if len(schemas) == 1 else {"anyOf": schemas}
        responses[status] = {
            "description": ", ".join(error["tag"] for error in errors),
            "content": {"application/json": {"schema": schema}},
        }
    return responses


def convert_endpoint(group: str, endpoint: Json) -> Json:
    """Map one contract endpoint to an OpenAPI operation object."""
    inputs = cast("list[Json]", endpoint["input"])
    for item in inputs:
        if item["source"] not in SOURCE_TO_LOCATION and item["source"] != "payload":
            msg = f"{endpoint['operationId']}: unknown input source {item['source']!r}"
            raise ContractError(msg)
    operation: Json = {"operationId": endpoint["operationId"], "tags": [group]}
    for key in ("summary", "description"):
        if endpoint.get(key):
            operation[key] = endpoint[key]
    if endpoint["deprecated"]:
        operation["deprecated"] = True
    parameters = [_parameter(item) for item in inputs if item["source"] != "payload"]
    if parameters:
        operation["parameters"] = parameters
    body = _request_body(endpoint, [item for item in inputs if item["source"] == "payload"])
    if body is not None:
        operation["requestBody"] = body
    status, success = _success(endpoint)
    operation["responses"] = {status: success, **_errors(endpoint)}
    operation["x-opencode-client-path"] = list(endpoint["clientPath"])
    if cast("Json", endpoint["success"]).get("unwrapData"):
        # The SDK returns the `data` of this envelope (config_models.py: `unwrap_response`).
        operation["x-opencode-unwrap-data"] = True
    return operation


def convert(contract: Json) -> Json:
    """Convert a parsed ``contract.json`` into an OpenAPI 3.1 document."""
    paths: dict[str, Json] = {}
    tags: list[Json] = []
    for group in cast("list[Json]", contract["groups"]):
        name = group["name"]
        tags.append({"name": name})
        for endpoint in cast("list[Json]", group["endpoints"]):
            method = str(endpoint["method"]).lower()
            item = paths.setdefault(convert_path(endpoint["path"]), {})
            if method in item:
                msg = f"duplicate operation {endpoint['method']} {endpoint['path']}"
                raise ContractError(msg)
            item[method] = convert_endpoint(name, endpoint)
    definitions = cast("Json", contract["definitions"])
    schemas = {name: rewrite_refs(definitions[name]) for name in sorted(definitions)}
    return {
        "openapi": "3.1.0",
        "info": {
            "title": "OpenCode",
            "version": contract["opencodeVersion"],
            "x-contract-generator": contract["generator"],
        },
        "tags": tags,
        "paths": {path: paths[path] for path in sorted(paths)},
        "components": {"schemas": schemas},
    }


def dumps(document: Json) -> str:
    """Serialise ``document`` the same way every time."""
    return json.dumps(document, indent=2, ensure_ascii=False) + "\n"


def main(argv: list[str] | None = None) -> int:
    """Read ``contract.json`` and write the OpenAPI document."""
    parser = argparse.ArgumentParser(description="Convert contract.json to OpenAPI 3.1.")
    parser.add_argument("contract", type=Path)
    parser.add_argument("output", type=Path)
    args = parser.parse_args(argv)
    contract_path = cast("Path", args.contract)
    output_path = cast("Path", args.output)
    try:
        document = convert(json.loads(contract_path.read_text(encoding="utf-8")))
    except (ContractError, KeyError) as exc:
        sys.stderr.write(f"error: {contract_path}: {exc}\n")
        return 1
    output_path.write_text(dumps(document), encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
