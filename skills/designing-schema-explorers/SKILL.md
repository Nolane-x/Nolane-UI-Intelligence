---
name: designing-schema-explorers
description: Use when developers inspect structured schemas, types, fields, relationships, constraints, and evolution and the interface must preserve graph context, provenance, search, deprecation, and large-schema navigation.
---

# Designing Schema Explorers

## Parent Contract
**Required parent:** `designing-data-dense-interfaces`.

This faculty owns read-oriented exploration of structured data or API schemas. It does not own free-form query construction or schema editing/migration. The central challenge is helping users reason about a large graph of types and relationships without flattening everything into an unreadable tree.

## Decision Architecture
Identify the schema model: relational tables, GraphQL types, JSON Schema/OpenAPI models, event schemas, protobuf messages, or domain entities. Present structure using concepts native to that model—fields, type, nullability/requiredness, cardinality, enum constraints, indexes, keys, references, inheritance, or composition. Do not normalize away distinctions that affect runtime behavior.

Support multiple navigation paths: search by type/field, follow relationship links, inspect incoming references, browse namespaces/domains, and preserve breadcrumb/back history. Large schemas need progressive loading and stable expansion state. A user following six relationships should be able to understand the path they took and return without losing context.

Provenance and evolution are material. Show source service/package, version or revision when known, deprecated fields, replacement guidance, and whether a schema is generated, inferred, or authoritative. Examples can aid comprehension but must be labeled as examples rather than constraints. When comparing revisions, hand off to diff/history owners rather than overloading the primary explorer.

## Failure Topology
- Explorer renders a 5,000-node tree expanded by default and becomes unusable.
- Relation navigation changes the current type but provides no path back to the originating field.
- Required and nullable semantics are visually collapsed into one “optional” badge despite different runtime meaning.
- Deprecated field is shown identically to current fields and users build new integrations against it.
- Inferred sample schema is presented as authoritative contract.
- Search result names a field but omits containing type/namespace, producing ambiguous duplicates.

## Falsification and Recovery
Falsify with thousands of types, duplicate field names across namespaces, cyclic relationships, deprecated/replacement fields, partial/inferred schemas, permission-restricted namespaces, keyboard/screen-reader traversal, deep-link to a field, and schema refresh while a user has nodes expanded. The design fails if users cannot identify the authority and containing context of a schema element or recover their relationship-navigation path.

Recover by model-native semantics, lazy hierarchical/graph navigation, contextual search results, stable history/breadcrumbs, explicit provenance/version/deprecation, permission-safe placeholders, and bounded refresh that preserves valid navigation state.

## Output Contract
Return `schema-explorer-contract` with schema model, element semantics, browse/search/navigation paths, relationship traversal, provenance/version, deprecation representation, lazy-loading strategy, deep-link identity, permission handling, accessibility model, and falsification cases.