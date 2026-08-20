---
name: designing-builder-data-binding
description: Use when a visual builder binds interface properties or repeated structures to runtime data and must expose source, type, scope, null/loading/error behavior, transformations, write-back, and preview truth.
---

# Designing Builder Data Binding

## Parent Contract

**Required parent:** `designing-visual-application-builders`.

This specialist owns how authored UI connects to data. It does not design database/query systems themselves. The builder must make data scope and runtime uncertainty concrete enough that authors can reason about what value appears, why it appears, and what happens when the source is absent, delayed, malformed or mutable.

## Binding model

Represent each binding as a typed path from a named source/context to an interface target, optionally through explicit transformations. Show the current context chain: page inputs, route params, authenticated user, query/result, repeated-item variable, component property, local state, derived expression. Avoid magic names that resolve differently depending on where a component is moved.

Type compatibility should be checked at authoring time where possible. Binding a list to text, nullable timestamp to required date field, or untrusted rich HTML to a content region needs explicit conversion or validation. Expression editors should preserve source provenance and distinguish deterministic transformations from side-effecting actions.

Every data-bound view needs non-happy states. Loading, empty, null/missing, permission denied, stale, error and partial data may be different. Let authors preview those states without editing production data. Sample data should be labeled and separated from runtime evidence so a polished preview cannot be mistaken for real query success.

Repeated collections introduce item identity. Use stable keys from domain data, not visual index, when reorder/update semantics require continuity. Expose the item context to nested components and interactions without leaking it outside the repeat scope. Pagination/virtualization must not change identity.

Two-way/write-back bindings are a higher-risk class. Show target, mutation authority, validation, optimistic state and rollback. Do not make a property look like a passive binding if user input triggers persistence.

## Evidence

Inspect data/query schemas, expression runtime, component property types, network/error traces, sample/production separation, repeated collection behavior and exported runtime code. Test nulls, permission changes, stale cache, partial responses and schema evolution.

## Failure topology

Failures include a binding picker that shows only field names without scope; moving a component and silently rebinding to a different `item`; sample data masking a missing production source; list indices used as identities; null rendered as `undefined`; and write-back mutations firing during editor preview.

Another failure is invisible transformation debt: a long expression hides business logic in a property field with no provenance or testability.

## Falsification

Move bound components across scopes, change source schemas, inject null/loading/error/partial values, reorder repeated items, switch preview identities/permissions and test a write-back rollback. The contract is falsified if the author cannot trace a rendered value to source, if binding meaning changes silently after reparenting, if preview causes unintended side effects, or if unsupported data states produce misleading UI.

## Recovery

Make data context explicit, migrate ambiguous names to qualified bindings, introduce typed transformation steps, add state-specific authoring previews and convert side-effecting bindings into explicit actions. Preserve broken bindings as diagnosable references after schema changes instead of dropping them and substituting empty literals.

## Output contract

Return a `builder-data-binding-contract` with source/context model, target types, expression/transform rules, repeated-item identity, loading/null/empty/error states, sample-data policy, preview isolation, write-back semantics, schema-change behavior and runtime parity tests.

## Handoffs

Use query/data-product owners for source semantics, conditional visibility for state-driven presence, interaction wiring for mutations, component authoring for exposed data properties, and design-code handoff when builder binding expressions need implementation equivalents.