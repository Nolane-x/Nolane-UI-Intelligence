---
name: governing-token-type-conformance
description: Use when token producers and consumers must agree on value types, composite shapes, units, and coercion rules so interchange does not silently change semantics.
---

# Governing Token Type Conformance

## Overview
Design-token interchange fails when a value that looks serializable is not semantically compatible with the declared token type. This skill owns type conformance across authoring, storage, transformation, and consumption: declared type, inferred type, unit domain, composite field shape, and whether coercion is legal.

## Parent Contract
**Required parent:** `architecting-design-tokens`.

The parent chooses token semantics and layers. This skill protects the boundary where those semantics become typed data consumed by tools and platforms.

## Type Lattice
Treat each token as `(declared-type, value-shape, unit, reference-target-type, consumer-capabilities)`. Decisions include whether aliases may cross compatible subtypes, whether numbers without units are accepted, how colors preserve color-space information, and how composite values expose required versus optional fields.

Never use “the renderer accepted it” as proof of conformance. A browser accepting a string does not mean another exporter, native client, or transformation pipeline will preserve the same meaning.

## Conformance Invariants
- references resolve to a value compatible with the source token's contract;
- composite members are validated independently and as a whole;
- transforms that narrow precision or gamut are explicit;
- unsupported types fail with diagnostics rather than stringification;
- a unit conversion preserves dimension, not merely numeric magnitude.

## Evidence
Evidence should include schema validation, cross-consumer round trips, examples at type boundaries, precision/gamut loss reports, and negative fixtures for illegal coercions. Capture both serialized and interpreted values because two consumers can parse the same JSON into different runtime semantics.

## Failure Topology
Failure includes a duration interpreted as a length, color channels clamped without notice, shadow composites losing spread, dimension aliases crossing incompatible units, font-weight strings coerced differently, or a token whose declared type no longer matches its referenced target after refactoring. Silent coercion is more severe than a hard error because it produces plausible but false UI.

## Falsification
Falsification sends boundary values through every supported transform, changes a referenced token to an incompatible type, removes optional composite fields, and round-trips values through at least two consumers. The skill is falsified if incompatible data reaches rendering without a typed warning or if round-trip meaning changes while validation remains green.

## Recovery
Recovery identifies the first boundary where type meaning diverged, restores a canonical typed representation, and adds an explicit adapter only when loss is accepted. Do not mutate the source type solely to satisfy one weak consumer; isolate the consumer limitation and document the degradation.

## Output and Handoff
Output: `token-type-conformance-contract`, covering type declarations, compatible aliases, unit policy, composite validation, coercion prohibition/allowance, and degradation evidence. Handoff visual token choices to the parent and platform-specific serialization to adapters.

## Sibling Boundary and delete-the-skill
Reference integrity proves a target exists; it does not prove the target's type is compatible. Extension governance owns vendor metadata, not core value shape. The delete-the-skill test passes because valid references can still transport semantically invalid typed values.