---
name: governing-token-extension-boundaries
description: Use when a token format permits vendor or tool-specific extensions and portability must be preserved without pretending proprietary metadata is universally understood.
---

# Governing Token Extension Boundaries

## Overview
Extension namespaces let tools add useful metadata without changing a shared token core. They also create portability traps: one exporter may require metadata another consumer ignores. This skill owns which information may live in extensions, how namespaces are versioned, and what happens when an extension is unavailable.

## Parent Contract
**Required parent:** `architecting-design-tokens`.

The parent owns canonical token semantics. An extension may enrich those semantics but must not secretly become the only place a required canonical meaning exists.

## Boundary Decisions
Classify extension data as advisory, reconstructable, loss-tolerant, or behavior-critical. Advisory metadata may disappear safely. Behavior-critical data requires either a core representation, a declared portability ceiling, or an explicit compatibility gate. Namespace ownership and version must be unambiguous so two vendors cannot collide on the same key.

A consumer that does not understand an extension needs a defined posture: preserve opaque data, ignore with warning, degrade through a documented fallback, or reject. Silent reinterpretation is never acceptable.

## Invariants
The canonical token remains valid when advisory extensions are stripped. Unknown extensions cannot change the meaning of core fields. Extension versions are identifiable. Round trips do not erase opaque data when preservation is promised. A critical extension dependency is surfaced before a consumer claims compatibility.

## Evidence
Evidence combines stripped-extension tests, unknown-namespace fixtures, round-trip preservation checks, version mismatch tests, and at least one consumer lacking the extension. Record which rendered or tooling behaviors degrade and which remain invariant.

## Failure Patterns
Failure appears as a theme that only works in one design tool, a proprietary gradient/shadow definition with no canonical fallback, an exporter that discards unknown metadata, namespace collisions, or an extension version change that silently alters interpretation. Another failure is marketing “portable tokens” while essential behavior depends on private metadata.

## Falsification
Falsification removes each extension namespace in isolation, feeds a future/unknown version to current consumers, and round-trips through an extension-unaware tool. If required meaning disappears without a blocked state or if opaque preservation was promised but data is lost, the boundary contract is disproved.

## Recovery
Recovery moves essential semantics into the shared representation when possible, otherwise raises the compatibility requirement and marks unsupported consumers explicitly. Preserve unknown metadata during repair. Version incompatible changes instead of teaching parsers to guess.

## Output and Handoff
Output: `token-extension-boundaries-contract`, containing namespace owners, version rules, criticality class, unknown-extension behavior, fallback/degradation policy, and portability claims. Handoff standard-core modeling changes to the parent; handoff consumer adapters to implementation integration.

## Sibling Boundary and delete-the-skill
Type conformance validates known value shapes; it cannot govern unknown vendor namespaces. Reference integrity governs graph edges, not extension portability. The delete-the-skill test passes because a fully typed, valid token graph can still become non-portable through hidden extension dependencies.