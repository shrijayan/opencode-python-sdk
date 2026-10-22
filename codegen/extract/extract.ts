/**
 * Exports the OpenCode client contract as JSON for the Python code generator.
 *
 * The contract is read from `ClientApi`, the Effect HttpApi published in `@opencode/protocol`.
 * It is the same source the official TypeScript client is generated from, and this script
 * follows the rules of OpenCode's `httpapi-codegen` so names and shapes match across languages:
 *
 * - group names come from `groupNames`, and WebSocket-only endpoints are omitted;
 * - client paths come from the OpenAPI identifier with the group prefix removed;
 * - path, query, header and struct payload fields flatten into one input list;
 * - a success body of exactly `{ data: A }` is marked for unwrapping;
 * - query fields are described by their decoded type, everything else by its wire encoding.
 *
 * Usage: bun run extract.ts [--out ../../spec/contract.json]
 */
import { mkdir, readFile, writeFile } from "node:fs/promises"
import { dirname, join } from "node:path"
import { fileURLToPath } from "node:url"
import { Context, Schema, SchemaAST, SchemaRepresentation } from "effect"
import { HttpApi, HttpApiSchema, OpenApi } from "effect/http-api"
import { ClientApi, groupNames, promiseOmitEndpoints } from "@opencode/protocol/client"

type JsonSchema = { readonly [key: string]: unknown }
type Source = "params" | "query" | "headers" | "payload" | "wildcard"
type InputField = { name: string; source: Source; optional: boolean; schema: JsonSchema }

const here = dirname(fileURLToPath(import.meta.url))
const outIndex = process.argv.indexOf("--out")
const out = outIndex >= 0 ? process.argv[outIndex + 1]! : join(here, "..", "..", "spec", "contract.json")

const readVersion = async (name: string) =>
  (JSON.parse(await readFile(join(here, "node_modules", name, "package.json"), "utf8")) as { version: string }).version

// Every schema is registered as a root and compiled at the end into one multi-document,
// so shared and anonymous definitions get one stable name across all operations.
const roots: Schema.Top[] = []

/** Registers a schema and returns a placeholder that is replaced by its JSON Schema (wire form). */
function jsonSchema(schema: Schema.Top): JsonSchema {
  roots.push(schema)
  return { $root: roots.length - 1 }
}

function isStruct(schema: Schema.Top) {
  const ast = Schema.toType(schema).ast
  return SchemaAST.isObjects(ast) && ast.indexSignatures.length === 0
}

function structFields(schema: Schema.Top | undefined, source: Source, owner: string): InputField[] {
  if (schema === undefined) return []
  const decoded = Schema.toType(schema).ast
  if (!SchemaAST.isObjects(decoded) || decoded.indexSignatures.length > 0) {
    throw new Error(`Input schema must be a struct: ${owner}.${source}`)
  }
  // Query values travel as strings, so describe them by their decoded type. Everything else is JSON on the wire.
  const described = source === "query" ? decoded : schema.ast
  if (!SchemaAST.isObjects(described)) throw new Error(`Input schema must be a struct: ${owner}.${source}`)
  return decoded.propertySignatures.map((field) => {
    if (typeof field.name !== "string") throw new Error(`Input field must have a string name: ${owner}.${source}`)
    const wire = described.propertySignatures.find((candidate) => candidate.name === field.name)
    if (wire === undefined) throw new Error(`Missing wire field ${field.name}: ${owner}.${source}`)
    return {
      name: field.name,
      source,
      optional: SchemaAST.isOptional(field.type),
      schema: jsonSchema(Schema.make<Schema.Top>(wire.type)),
    }
  })
}

/** Mirrors httpapi-codegen: drop a leading "v2" and everything up to the group's own name. */
function clientEndpointPath(group: string, name: string): string[] {
  const parts = name.split(".")
  if (parts[0] === "v2") parts.shift()
  const index = parts.lastIndexOf(group.slice(group.lastIndexOf(".") + 1))
  const result = index < 0 ? parts : parts.slice(index + 1)
  if (result.length === 0 || result.some((part) => part.length === 0)) {
    throw new Error(`Client endpoint path must contain non-empty names: ${name}`)
  }
  return result
}

function isDataEnvelope(schema: Schema.Top) {
  const ast = Schema.toType(schema).ast
  return (
    SchemaAST.isObjects(ast) &&
    ast.indexSignatures.length === 0 &&
    ast.propertySignatures.length === 1 &&
    ast.propertySignatures[0]?.name === "data"
  )
}

function errorTag(schema: Schema.Top): string | undefined {
  const ast = Schema.toType(schema).ast
  const fields = SchemaAST.isDeclaration(ast) ? ast.typeParameters[0] : ast
  if (fields === undefined || !SchemaAST.isObjects(fields)) return undefined
  const tag = fields.propertySignatures.find((field) => field.name === "_tag")?.type
  return tag !== undefined && SchemaAST.isLiteral(tag) && typeof tag.literal === "string" ? tag.literal : undefined
}

const resolveStatus = SchemaAST.resolveAt<number>("httpApiStatus")
const resolveEncoding = SchemaAST.resolveAt<{ readonly _tag: string }>("~httpApiEncoding")
const isBinary = (schema: Schema.Top) => (resolveEncoding(schema.ast)?._tag ?? "Json") === "Uint8Array"

type StreamSchema = Schema.Top & { readonly _tag: "StreamSse" | "StreamUint8Array"; readonly events: Schema.Top }
const isStream = (schema: Schema.Top): schema is StreamSchema =>
  "_tag" in schema && (schema._tag === "StreamSse" || schema._tag === "StreamUint8Array")

const groups = new Map<string, { name: string; sourceGroup: string; endpoints: unknown[] }>()

HttpApi.reflect(ClientApi, {
  onGroup() {},
  onEndpoint({ endpoint, errors, group }) {
    if (promiseOmitEndpoints.has(endpoint.identifier)) return
    const groupName = (groupNames as Record<string, string>)[group.identifier] ?? group.identifier
    const identifier = Context.getOrElse(endpoint.annotations, OpenApi.Identifier, () =>
      group.topLevel ? endpoint.identifier : `${group.identifier}.${endpoint.identifier}`,
    )
    const clientPath = clientEndpointPath(group.identifier, identifier)
    const owner = `${groupName}.${clientPath.join(".")}`

    const successes = Array.from(endpoint.success)
    if (successes.length > 1) throw new Error(`Multiple success schemas: ${owner}`)
    const success = successes[0] ?? HttpApiSchema.NoContent
    const payloads = Array.from(endpoint.payload.values()).flatMap(({ schemas }) => schemas)
    if (payloads.length > 1) throw new Error(`Multiple payload schemas: ${owner}`)
    const payload = payloads[0]
    const opaque = payload !== undefined && !isStruct(payload)

    const input: InputField[] = [
      ...structFields(endpoint.params?.schema, "params", owner),
      ...structFields(endpoint.query?.schema, "query", owner),
      ...structFields(endpoint.headers?.schema, "headers", owner),
      ...(payload === undefined
        ? []
        : opaque
          ? [{ name: "payload", source: "payload" as const, optional: false, schema: jsonSchema(payload) }]
          : structFields(payload, "payload", owner)),
    ]
    const seen = new Set<string>()
    for (const field of input) {
      if (seen.has(field.name)) throw new Error(`Input field collision: ${owner}.${field.name}`)
      seen.add(field.name)
    }
    if (endpoint.path.includes("*")) {
      if (endpoint.path.indexOf("*") !== endpoint.path.length - 1) throw new Error(`Unsupported wildcard: ${owner}`)
      const name = seen.has("path") ? "wildcard" : "path"
      input.push({ name, source: "wildcard", optional: false, schema: { type: "string" } })
    }

    let successInfo: Record<string, unknown>
    if (isStream(success)) {
      if (success._tag !== "StreamSse") throw new Error(`Unsupported byte stream: ${owner}`)
      const events = success.events.ast
      const data = SchemaAST.isObjects(events)
        ? events.propertySignatures.find((field) => field.name === "data")?.type
        : undefined
      if (data === undefined) throw new Error(`Invalid SSE schema: ${owner}`)
      // Each SSE `data` line is JSON text. Drop that outer string encoding to describe the JSON value itself.
      const value = SchemaAST.replaceEncoding(data, undefined)
      successInfo = { kind: "stream", status: 200, schema: jsonSchema(Schema.make<Schema.Top>(value)) }
    } else if (HttpApiSchema.isNoContent(success.ast)) {
      successInfo = { kind: "void", status: resolveStatus(success.ast) ?? 204 }
    } else if (isBinary(success)) {
      successInfo = { kind: "binary", status: resolveStatus(success.ast) ?? 200 }
    } else {
      successInfo = {
        kind: "value",
        status: resolveStatus(success.ast) ?? 200,
        unwrapData: isDataEnvelope(success),
        schema: jsonSchema(success),
      }
    }

    const declared = Array.from(errors)
      .sort(([a], [b]) => a - b)
      .flatMap(([status, schemas]) =>
        schemas.map((schema) => ({ status, tag: errorTag(schema), schema: jsonSchema(schema) })),
      )

    const entry = groups.get(groupName) ?? { name: groupName, sourceGroup: group.identifier, endpoints: [] }
    if (entry.sourceGroup !== group.identifier) throw new Error(`Client group name collision: ${groupName}`)
    entry.endpoints.push({
      clientPath,
      operationId: identifier,
      method: endpoint.method,
      path: endpoint.path,
      summary: Context.getOrUndefined(endpoint.annotations, OpenApi.Summary),
      description: Context.getOrUndefined(endpoint.annotations, OpenApi.Description),
      deprecated: Context.getOrUndefined(endpoint.annotations, OpenApi.Deprecated) === true,
      input,
      payload: payload === undefined ? undefined : { mode: isBinary(payload) ? "binary" : opaque ? "opaque" : "struct" },
      success: successInfo,
      errors: declared,
    })
    groups.set(groupName, entry)
  },
})

if (roots.length === 0) throw new Error("No schemas found")
const compiled = SchemaRepresentation.toJsonSchemaMultiDocument(
  SchemaRepresentation.toRepresentations(
    roots.map((schema) => Schema.toCodecJson(schema).ast) as [SchemaAST.AST, ...SchemaAST.AST[]],
  ),
) as { schemas: ReadonlyArray<JsonSchema>; definitions?: Record<string, JsonSchema> }

function resolveRoots(value: unknown): unknown {
  if (Array.isArray(value)) return value.map(resolveRoots)
  if (value === null || typeof value !== "object") return value
  const record = value as Record<string, unknown>
  if (typeof record.$root === "number") return compiled.schemas[record.$root]
  return Object.fromEntries(Object.entries(record).map(([key, item]) => [key, resolveRoots(item)]))
}

const definitions = compiled.definitions ?? {}
const document = {
  generator: "opencode-python-sdk codegen/extract",
  opencodeVersion: await readVersion("@opencode/protocol"),
  effectVersion: await readVersion("effect"),
  groups: resolveRoots([...groups.values()].map(({ name, endpoints }) => ({ name, endpoints }))) as Array<{
    name: string
    endpoints: unknown[]
  }>,
  definitions: Object.fromEntries(Object.entries(definitions).sort(([a], [b]) => a.localeCompare(b))),
}

await mkdir(dirname(out), { recursive: true })
await writeFile(out, `${JSON.stringify(document, null, 2)}\n`)
const operations = document.groups.reduce((total, group) => total + group.endpoints.length, 0)
console.log(
  `Wrote ${out}: OpenCode ${document.opencodeVersion}, ${operations} operations, ${Object.keys(definitions).length} definitions`,
)
