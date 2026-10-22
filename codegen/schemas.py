"""Translates the contract's JSON Schemas into Python type declarations."""

from __future__ import annotations

import json
import re
from dataclasses import dataclass, field
from typing import Any

from .naming import BUILTIN_NAMES, MODEL_RESERVED, pascal, safe_identifier, snake

Schema = dict[str, Any]

UNKNOWN_TAG = "__unknown__"

# Names the generated types module imports. Generated declarations must not shadow them.
MODULE_RESERVED = frozenset(
    {
        "Annotated",
        "Any",
        "BaseModel",
        "ClassVar",
        "Discriminator",
        "Field",
        "Literal",
        "OpenEnum",
        "Tag",
        "TypeAlias",
        "discriminator",
        "is_none",
    }
)


@dataclass
class FieldDecl:
    name: str
    wire: str
    type: str
    required: bool
    nullable: bool
    doc: str | None
    literal_default: str | None = None
    """For a single-value literal (a union tag), the value to default to."""


@dataclass
class ClassDecl:
    name: str
    doc: str | None
    fields: list[FieldDecl]
    source: str
    unknown_for: str | None = None
    """Set on fallback classes generated for a union."""


@dataclass
class AliasDecl:
    name: str
    expr: str
    doc: str | None
    source: str
    deps: set[str] = field(default_factory=set)
    """Names of other aliases this one evaluates at import time."""


@dataclass
class TypeRef:
    expr: str
    nullable: bool = False
    aliases: set[str] = field(default_factory=set)
    """Aliases referenced by the expression; aliases are evaluated eagerly, so their order matters."""


class GenerationError(Exception):
    pass


def _canonical(value: Any) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"))


def _without_docs(value: Any) -> Any:
    if isinstance(value, dict):
        return {k: _without_docs(v) for k, v in value.items() if k not in ("description", "title", "examples")}
    if isinstance(value, list):
        return [_without_docs(v) for v in value]
    return value


def deduplicate(definitions: dict[str, Schema]) -> tuple[dict[str, Schema], dict[str, str]]:
    """Merges ``Name_N`` definitions into ``Name`` when they have the same shape.

    Effect numbers repeated identifiers per schema instance. Equal shapes collapse to one name; shapes that really
    differ keep their suffix.
    """
    renames: dict[str, str] = {}
    pattern = re.compile(r"^(.*)_(\d+)$")

    def rewrite(value: Any) -> Any:
        if isinstance(value, dict):
            result = {}
            for key, item in value.items():
                if key == "$ref" and isinstance(item, str):
                    name = item.removeprefix("#/$defs/")
                    while name in renames:
                        name = renames[name]
                    result[key] = f"#/$defs/{name}"
                else:
                    result[key] = rewrite(item)
            return result
        if isinstance(value, list):
            return [rewrite(item) for item in value]
        return value

    current = dict(definitions)
    while True:
        changed = False
        for name in sorted(current):
            match = pattern.match(name)
            if not match or match.group(1) not in current or name in renames:
                continue
            base = match.group(1)
            if _canonical(_without_docs(rewrite(current[name]))) == _canonical(_without_docs(rewrite(current[base]))):
                renames[name] = base
                changed = True
        if not changed:
            break
    merged = {name: rewrite(schema) for name, schema in current.items() if name not in renames}
    return merged, renames


def definition_python_name(key: str) -> str:
    """Maps a contract definition name to a Python class or alias name."""
    suffix = ""
    match = re.match(r"^(.*)_(\d+)$", key)
    if match:
        key, suffix = match.group(1), match.group(2)
    if key == "V2Event":
        name = "Event"
    elif key.startswith("V2Event."):
        name = pascal(key.removeprefix("V2Event.")) + "Event"
    elif key[:1].islower():
        name = pascal(key) + "Event"
    else:
        name = key
        if name.endswith("Encoded"):
            name = name.removesuffix("Encoded")
            if name.endswith("Error"):
                name += "Body"
        name = pascal(name)
    return name + suffix


class TypeRegistry:
    """Builds declarations on demand while walking schemas."""

    def __init__(self, definitions: dict[str, Schema]) -> None:
        self.definitions = definitions
        self.def_names: dict[str, str] = {}
        self.classes: dict[str, ClassDecl] = {}
        self.aliases: dict[str, AliasDecl] = {}
        self._inline_by_shape: dict[str, str] = {}
        self._taken: set[str] = set(MODULE_RESERVED)
        for key in sorted(definitions):
            name = definition_python_name(key)
            if name in self._taken:
                raise GenerationError(f"Definition {key!r} maps to taken Python name {name!r}")
            self._taken.add(name)
            self.def_names[key] = name
        self._building: set[str] = set()

    # -- schema helpers -------------------------------------------------------------------------------------

    def resolve(self, schema: Schema) -> Schema:
        seen: set[str] = set()
        while "$ref" in schema:
            key = schema["$ref"].removeprefix("#/$defs/")
            if key in seen:
                raise GenerationError(f"Reference cycle at {key}")
            seen.add(key)
            schema = self.definitions[key]
        return schema

    def is_null(self, schema: Schema) -> bool:
        return schema.get("type") == "null"

    def literal_values(self, schema: Schema) -> list[Any] | None:
        schema = self.resolve(schema)
        if "const" in schema:
            return [schema["const"]]
        if "enum" in schema:
            return list(schema["enum"])
        return None

    # -- declarations ---------------------------------------------------------------------------------------

    def ensure_definition(self, key: str) -> str:
        name = self.def_names[key]
        if name in self.classes or name in self.aliases or name in self._building:
            return name
        self._building.add(name)
        try:
            self._declare(name, self.definitions[key], source=f"#/$defs/{key}")
        finally:
            self._building.discard(name)
        return name

    def _declare(self, name: str, schema: Schema, *, source: str) -> None:
        doc = schema.get("description")
        options = schema.get("anyOf")
        if isinstance(options, list) and len(options) == 1 and self._is_object_model(options[0]):
            # A one-member union is just that member.
            schema = {**options[0], "description": doc or options[0].get("description")}
        if self._is_object_model(schema):
            self.classes[name] = self._class(name, schema, source=source, doc=doc)
            return
        union = self._discriminated_union(name, schema, source=source)
        if union is not None:
            self.aliases[name] = union
            return
        ref = self.type_of(schema, context=name)
        expr = ref.expr if not ref.nullable else f"{ref.expr} | None"
        self.aliases[name] = AliasDecl(name=name, expr=expr, doc=doc, source=source, deps=set(ref.aliases))

    def _is_object_model(self, schema: Schema) -> bool:
        if "allOf" in schema and "properties" not in schema:
            return False
        return schema.get("type") == "object" and bool(schema.get("properties"))

    def _class(self, name: str, schema: Schema, *, source: str, doc: str | None) -> ClassDecl:
        properties: dict[str, Schema] = schema.get("properties", {})
        required = set(schema.get("required", []))
        fields: list[FieldDecl] = []
        used: set[str] = set()
        for wire, prop in properties.items():
            if prop.get("not") == {}:
                continue  # never present
            attr = safe_identifier(snake(wire), reserved=MODEL_RESERVED)
            if attr in used:
                raise GenerationError(f"{name}: field {wire!r} collides with another field as {attr!r}")
            used.add(attr)
            ref = self.type_of(prop, context=f"{name}{pascal(wire)}")
            literal = self.literal_values(prop)
            literal_default = None
            if literal is not None and len(literal) == 1 and isinstance(literal[0], (str, bool, int)):
                literal_default = repr(literal[0])
            fields.append(
                FieldDecl(
                    name=attr,
                    wire=wire,
                    type=ref.expr,
                    required=wire in required,
                    nullable=ref.nullable,
                    doc=prop.get("description") or self._ref_description(prop),
                    literal_default=literal_default,
                )
            )
        return ClassDecl(name=name, doc=doc, fields=fields, source=source)

    def _ref_description(self, schema: Schema) -> str | None:
        for option in schema.get("anyOf", []):
            if isinstance(option, dict) and option.get("description"):
                return option["description"]
        return None

    def _inline_class(self, schema: Schema, context: str) -> str:
        """Declares an inline object as a class named after where it appears (``SessionInfoTime``).

        The same shape in the same place reuses one class, so a ``location`` query parameter shared by many
        endpoints becomes a single ``Location`` model.
        """
        shape = _canonical(_without_docs(schema))
        existing = self._inline_by_shape.get(f"{context}:{shape}")
        if existing is not None:
            return existing
        name = context
        if name in self._taken:
            index = 2
            while f"{context}{index}" in self._taken:
                index += 1
            name = f"{context}{index}"
        self._taken.add(name)
        self._inline_by_shape[f"{context}:{shape}"] = name
        self.classes[name] = self._class(name, schema, source=f"inline:{context}", doc=schema.get("description"))
        return name

    # -- unions ---------------------------------------------------------------------------------------------

    def _member_tags(self, member: Schema) -> dict[str, Any] | None:
        """Literal properties shared by every alternative of a member, or ``None`` if it is not an object."""
        resolved = self.resolve(member)
        options = resolved.get("anyOf")
        if options is not None:
            maps = [self._member_tags(option) for option in options]
            if any(item is None for item in maps):
                return None
            shared: dict[str, Any] = {}
            first = maps[0] or {}
            for key, value in first.items():
                if all(item is not None and item.get(key) == value for item in maps):
                    shared[key] = value
            return shared
        if resolved.get("type") != "object":
            return None
        tags: dict[str, Any] = {}
        for key, prop in resolved.get("properties", {}).items():
            if key not in resolved.get("required", []):
                continue
            values = self.literal_values(prop)
            if values is not None and len(values) == 1:
                tags[key] = values[0]
        return tags

    def _member_patterns(self, member: Schema, key: str) -> str | None:
        resolved = self.resolve(member)
        prop = resolved.get("properties", {}).get(key)
        if isinstance(prop, dict) and prop.get("type") == "string" and isinstance(prop.get("pattern"), str):
            return prop["pattern"]
        return None

    def _discriminated_union(self, name: str, schema: Schema, *, source: str) -> AliasDecl | None:
        options = [option for option in schema.get("anyOf", []) if not self.is_null(option)]
        nullable = len(options) != len(schema.get("anyOf", []))
        if len(options) < 2 or nullable:
            return None
        tag_maps = [self._member_tags(option) for option in options]
        if any(item is None for item in tag_maps):
            return None
        candidates: list[str] = []
        for key in {key for item in tag_maps if item for key in item}:
            values = [item.get(key) if item else None for item in tag_maps]
            patterns = [self._member_patterns(option, key) for option in options]
            known = [value for value in values if value is not None]
            if all(
                value is not None or pattern is not None for value, pattern in zip(values, patterns, strict=True)
            ) and len(set(map(_canonical, known))) == len(known):
                candidates.append(key)
        if not candidates:
            return None
        key = "type" if "type" in candidates else sorted(candidates)[0]

        members: list[str] = []
        tags: list[str] = []
        patterns: list[tuple[str, str]] = []
        deps: set[str] = set()
        for index, (option, tag_map) in enumerate(zip(options, tag_maps, strict=True)):
            tag_value = (tag_map or {}).get(key)
            member_context = (
                f"{name}{pascal(_tag_string(tag_value))}" if tag_value is not None else f"{name}Variant{index + 1}"
            )
            ref = self.type_of(option, context=member_context)
            deps |= ref.aliases
            value = (tag_map or {}).get(key)
            if value is None:
                pattern = self._member_patterns(option, key)
                assert pattern is not None
                tag = f"pattern:{pattern}"
                patterns.append((pattern, tag))
            else:
                tag = _tag_string(value)
                tags.append(tag)
            members.append(f"Annotated[{ref.expr}, Tag({tag!r})]")

        attribute = safe_identifier(snake(key), reserved=MODEL_RESERVED)
        unknown = f"Unknown{name}"
        if unknown in self._taken:
            raise GenerationError(f"Fallback name {unknown!r} is taken")
        self._taken.add(unknown)
        self.classes[unknown] = ClassDecl(
            name=unknown,
            doc=(
                f"A `{name}` variant this client version does not recognize.\n\n"
                "Newer OpenCode servers can add variants. The raw fields are kept and available as attributes "
                "and through `model_extra`."
            ),
            fields=[FieldDecl(name=attribute, wire=key, type="Any", required=False, nullable=True, doc=None)],
            source=f"unknown:{name}",
            unknown_for=name,
        )
        members.append(f"Annotated[{unknown}, Tag({UNKNOWN_TAG!r})]")
        pattern_arg = f", patterns={patterns!r}" if patterns else ""
        expr = (
            "Annotated[\n    "
            + "\n    | ".join(members)
            + f",\n    Discriminator(discriminator({key!r}, {attribute!r}, {tags!r}{pattern_arg})),\n]"
        )
        return AliasDecl(name=name, expr=expr, doc=schema.get("description"), source=source, deps=deps)

    # -- type expressions -----------------------------------------------------------------------------------

    def type_of(self, schema: Schema, *, context: str) -> TypeRef:
        """Returns the Python type expression for a schema. Nullability is reported separately."""
        if "$ref" in schema:
            key = schema["$ref"].removeprefix("#/$defs/")
            name = self.ensure_definition(key)
            return TypeRef(name, aliases={name} if name in self.aliases or name not in self.classes else set())

        if "anyOf" in schema or "oneOf" in schema:
            options = schema.get("anyOf") or schema.get("oneOf") or []
            non_null = [option for option in options if not self.is_null(option)]
            nullable = len(non_null) != len(options)
            if not non_null:
                return TypeRef("None", nullable=True)
            if len(non_null) == 1:
                inner = self.type_of(non_null[0], context=context)
                return TypeRef(inner.expr, nullable=nullable or inner.nullable, aliases=inner.aliases)
            literals = [self.literal_values(option) for option in non_null]
            if all(values is not None for values in literals):
                merged = [value for values in literals if values for value in values]
                return TypeRef(self._literal(merged), nullable=nullable)
            union_schema = {"anyOf": non_null}
            # An inline discriminated union gets a name so it can carry its fallback member.
            if all(self._member_tags(option) is not None for option in non_null):
                decl = self._discriminated_union(context, union_schema, source=f"inline:{context}")
                if decl is not None:
                    if context in self._taken:
                        raise GenerationError(f"Inline union name {context!r} is taken")
                    self._taken.add(context)
                    self.aliases[context] = decl
                    return TypeRef(context, nullable=nullable, aliases={context})
            inline_objects = [option for option in non_null if "$ref" not in option and option.get("properties")]
            parts = [
                self.type_of(
                    option,
                    # A lone object alternative takes the field's own name: `model: str | ConfigAgentModel`.
                    context=context
                    if len(inline_objects) == 1 and option is inline_objects[0]
                    else f"{context}Option{index + 1}",
                )
                for index, option in enumerate(non_null)
            ]
            exprs: list[str] = []
            aliases: set[str] = set()
            for part in parts:
                aliases |= part.aliases
                if part.expr not in exprs:
                    exprs.append(part.expr)
                nullable = nullable or part.nullable
            return TypeRef(" | ".join(exprs), nullable=nullable, aliases=aliases)

        if "allOf" in schema:
            merged: Schema = {k: v for k, v in schema.items() if k != "allOf"}
            for part in schema["allOf"]:
                resolved = self.resolve(part)
                if resolved.get("properties"):
                    merged.setdefault("properties", {}).update(resolved["properties"])
                    merged["required"] = sorted({*merged.get("required", []), *resolved.get("required", [])})
                merged.setdefault("type", resolved.get("type", "object"))
            return self.type_of(merged, context=context)

        if "const" in schema:
            return TypeRef(self._literal([schema["const"]]))
        if "enum" in schema:
            return TypeRef(self._literal(list(schema["enum"])))

        kind = schema.get("type")
        if isinstance(kind, list):
            options = [{**schema, "type": item} for item in kind]
            return self.type_of({"anyOf": options}, context=context)
        if kind == "string":
            if schema.get("format") == "binary" or schema.get("contentEncoding") == "base64":
                return TypeRef("bytes")
            return TypeRef("str")
        if kind == "integer":
            return TypeRef("int")
        if kind == "number":
            return TypeRef("float")
        if kind == "boolean":
            return TypeRef("bool")
        if kind == "null":
            return TypeRef("None", nullable=True)
        if kind == "array":
            items = schema.get("items")
            if items is None and schema.get("prefixItems"):
                items = {"anyOf": schema["prefixItems"]}
            if items is None or items == {}:
                return TypeRef("list[Any]")
            inner = self.type_of(items, context=f"{context}Item")
            expr = f"{inner.expr} | None" if inner.nullable else inner.expr
            return TypeRef(f"list[{expr}]", aliases=inner.aliases)
        if kind == "object" or "properties" in schema or "additionalProperties" in schema:
            if schema.get("properties"):
                return TypeRef(self._inline_class(schema, context))
            extra = schema.get("additionalProperties")
            if isinstance(extra, dict) and extra:
                inner = self.type_of(extra, context=f"{context}Value")
                expr = f"{inner.expr} | None" if inner.nullable else inner.expr
                return TypeRef(f"dict[str, {expr}]", aliases=inner.aliases)
            return TypeRef("dict[str, Any]")
        if "not" in schema:
            return TypeRef("Any")
        if not schema or set(schema) <= {"description", "title"}:
            return TypeRef("Any")
        raise GenerationError(f"Unsupported schema at {context}: {json.dumps(schema)[:300]}")

    def _literal(self, values: list[Any]) -> str:
        unique: list[Any] = []
        for value in values:
            if value not in unique:
                unique.append(value)
        literal = f"Literal[{', '.join(repr(value) for value in unique)}]"
        # Multi-member enums stay open at runtime so new server values do not fail validation.
        return literal if len(unique) == 1 else f"OpenEnum[{literal}]"


def _tag_string(value: Any) -> str:
    if isinstance(value, bool):
        return "true" if value else "false"
    return str(value)


def ensure_unique(names: list[str]) -> None:
    seen: set[str] = set()
    for name in names:
        if name in seen:
            raise GenerationError(f"Duplicate generated name {name!r}")
        if name in BUILTIN_NAMES:
            raise GenerationError(f"Generated name {name!r} shadows a Python builtin")
        seen.add(name)
