"""Builds the resource tree and method signatures from contract endpoints."""

from __future__ import annotations

import re
from dataclasses import dataclass, field
from typing import Any

from .naming import pascal, safe_identifier, snake
from .schemas import GenerationError, Schema, TypeRegistry

RESERVED_PARAMS = frozenset({"self", "extra_headers", "extra_query", "extra_body", "timeout"})
RESOURCE_RESERVED = frozenset({"with_options", "close", "request", "stream", "page"})


@dataclass
class Param:
    name: str
    wire: str
    source: str
    type: str
    required: bool
    nullable: bool
    doc: str | None


@dataclass
class ErrorInfo:
    status: int
    tag: str | None
    schema: Schema


@dataclass
class Operation:
    group: str
    client_path: list[str]
    method_name: str
    http_method: str
    path: str
    operation_id: str
    summary: str | None
    description: str | None
    deprecated: bool
    experimental: bool
    params: list[Param]
    payload_mode: str | None
    kind: str
    """``json``, ``void``, ``binary``, ``stream`` or ``page``."""
    return_type: str
    response_type: str | None
    unwrap: bool
    errors: list[ErrorInfo]

    @property
    def path_params(self) -> list[Param]:
        return [param for param in self.params if param.source in ("params", "wildcard")]

    @property
    def keyword_params(self) -> list[Param]:
        return [param for param in self.params if param.source not in ("params", "wildcard")]


@dataclass
class Resource:
    name: str
    """Attribute name on the parent (``session``, ``revert``)."""
    class_name: str
    path: list[str]
    operations: list[Operation] = field(default_factory=list)
    children: dict[str, Resource] = field(default_factory=dict)


def _is_page(registry: TypeRegistry, schema: Schema, params: list[Param]) -> Schema | None:
    """Returns the item schema when a response is a cursor page: ``{data: [...], cursor: {next, previous}}``."""
    resolved = registry.resolve(schema)
    properties = resolved.get("properties", {})
    if set(properties) != {"data", "cursor"} or not any(param.wire == "cursor" for param in params):
        return None
    cursor = registry.resolve(properties["cursor"])
    if set(cursor.get("properties", {})) != {"next", "previous"}:
        return None
    data = registry.resolve(properties["data"])
    if data.get("type") != "array":
        return None
    return data.get("items", {})


def build_operations(contract: dict[str, Any], registry: TypeRegistry) -> list[Operation]:
    operations: list[Operation] = []
    for group in contract["groups"]:
        for endpoint in group["endpoints"]:
            operations.append(_operation(group["name"], endpoint, registry))
    return operations


def _operation(group: str, endpoint: dict[str, Any], registry: TypeRegistry) -> Operation:
    client_path: list[str] = endpoint["clientPath"]
    context = pascal(group) + "".join(pascal(part) for part in client_path)
    method_name = safe_identifier(snake(client_path[-1]), reserved=RESOURCE_RESERVED)

    params: list[Param] = []
    used: set[str] = set()
    for item in endpoint["input"]:
        name = safe_identifier(snake(item["name"]), reserved=RESERVED_PARAMS)
        if name in used:
            raise GenerationError(f"{endpoint['operationId']}: parameter {item['name']!r} collides as {name!r}")
        used.add(name)
        ref = registry.type_of(
            item["schema"],
            context=pascal(item["name"]) if item["source"] == "query" else f"{context}{pascal(item['name'])}",
        )
        params.append(
            Param(
                name=name,
                wire=item["name"],
                source=item["source"],
                type=ref.expr,
                required=not item["optional"],
                nullable=ref.nullable,
                doc=item["schema"].get("description") or registry._ref_description(item["schema"]),
            )
        )

    success = endpoint["success"]
    kind: str = success["kind"]
    unwrap = bool(success.get("unwrapData"))
    response_type: str | None = None
    if kind == "void":
        return_type = "None"
    elif kind == "binary":
        return_type = "bytes"
    elif kind == "stream":
        item = registry.type_of(success["schema"], context=f"{context}Event")
        return_type = item.expr if not item.nullable else f"{item.expr} | None"
        response_type = return_type
    else:
        schema: Schema = success["schema"]
        page_item = None if unwrap else _is_page(registry, schema, params)
        if page_item is not None:
            kind = "page"
            item = registry.type_of(page_item, context=f"{context}Item")
            response = registry.type_of(schema, context=f"{context}Response")
            return_type = item.expr
            response_type = response.expr
        else:
            target = schema
            target_context = f"{context}Response"
            if unwrap:
                if "$ref" in schema:
                    # Match the name the data field already got when its definition was declared.
                    target_context = registry.def_names[schema["$ref"].removeprefix("#/$defs/")] + "Data"
                target = registry.resolve(schema)["properties"]["data"]
            ref = registry.type_of(target, context=target_context)
            return_type = ref.expr if not ref.nullable else f"{ref.expr} | None"
            response_type = return_type
        if kind == "value":
            kind = "json"

    path: str = endpoint["path"]
    return Operation(
        group=group,
        client_path=client_path,
        method_name=method_name,
        http_method=endpoint["method"],
        path=path,
        operation_id=endpoint["operationId"],
        summary=endpoint.get("summary"),
        description=endpoint.get("description"),
        deprecated=bool(endpoint.get("deprecated")),
        experimental="/experimental/" in path or endpoint["operationId"].startswith("experimental."),
        params=params,
        payload_mode=(endpoint.get("payload") or {}).get("mode"),
        kind=kind,
        return_type=return_type,
        response_type=response_type,
        unwrap=unwrap,
        errors=[
            ErrorInfo(status=error["status"], tag=error.get("tag"), schema=error["schema"])
            for error in endpoint["errors"]
        ],
    )


def build_resources(operations: list[Operation]) -> dict[str, Resource]:
    roots: dict[str, Resource] = {}
    for operation in operations:
        group = safe_identifier(snake(operation.group), reserved=RESOURCE_RESERVED)
        root = roots.setdefault(group, Resource(name=group, class_name=pascal(operation.group), path=[operation.group]))
        node = root
        for part in operation.client_path[:-1]:
            child_name = safe_identifier(snake(part), reserved=RESOURCE_RESERVED)
            if child_name not in node.children:
                node.children[child_name] = Resource(
                    name=child_name, class_name=node.class_name + pascal(part), path=[*node.path, part]
                )
            node = node.children[child_name]
        if any(existing.method_name == operation.method_name for existing in node.operations):
            raise GenerationError(f"Duplicate method {operation.method_name} on {node.class_name}")
        if operation.method_name in node.children:
            raise GenerationError(f"Method {operation.method_name} collides with a sub-resource on {node.class_name}")
        node.operations.append(operation)
    return roots


def python_path(operation: Operation) -> str:
    """Builds the f-string body for an endpoint path such as ``/api/session/:sessionID``."""
    by_wire = {param.wire: param for param in operation.params if param.source == "params"}

    def replace(match: re.Match[str]) -> str:
        wire = match.group(1)
        if wire not in by_wire:
            raise GenerationError(f"{operation.operation_id}: missing path parameter {wire}")
        return "{encode_path_segment(" + by_wire[wire].name + ")}"

    path = re.sub(r":([A-Za-z_][A-Za-z0-9_]*)", replace, operation.path)
    if path.endswith("*"):
        wildcard = next(param for param in operation.params if param.source == "wildcard")
        path = path[:-1] + "{encode_path(" + wildcard.name + ")}"
    return path
