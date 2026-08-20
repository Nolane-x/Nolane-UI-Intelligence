---
name: designing-composition-boundaries
description: Decide which behavior belongs inside a shared component and which should be assembled through composition so abstractions stay coherent across divergent use cases.
---

# Designing composition boundaries

Shared components often become bloated because every product-specific arrangement is pulled into the core. Use this skill when deciding whether a new capability should be intrinsic, composed from primitives, wrapped by a product layer, or represented as a separate compound component.

## Decision ownership

Own the boundary between core responsibility and composition. Decide which invariants the component must guarantee, which regions or behaviors may be supplied by consumers, and what dependencies a composed child may assume about its parent context.

## Inputs and evidence

Collect current use cases, requested variants, wrapper patterns, duplicated orchestration code, accessibility relationships, state ownership, and lifecycle coupling. Identify which requested behaviors co-vary and which appear only in one product workflow.

Inspect whether consumer composition can preserve focus, labeling, error handling, and responsive behavior without reaching into internals.

## Procedure

State the component’s invariant purpose in one sentence. Capabilities required to satisfy that purpose across consumers belong near the core; workflow-specific ordering, extra content, or business logic usually belongs outside. Introduce compound components when children need shared state/context but remain independently meaningful.

Design composition seams deliberately: slots, child components, render regions, context providers, or adapter props should expose semantic roles, not raw DOM positions. Define what happens when optional pieces are absent or reordered.

Prefer a small primitive plus documented compositions over a monolith with dozens of conditional branches when use cases are structurally distinct.

## Failure topology

Over-centralization turns a component into a product framework and multiplies conditional props. Under-centralization forces every consumer to reimplement accessibility or interaction invariants. Another failure is fake composition: consumers can inject arbitrary markup but must know private DOM ordering or CSS selectors to make it work.

Composition can also fragment analytics or state if ownership is not explicit.

## Falsification

Implement two structurally different consumers using the proposed boundary. If either must access private internals, the seam is insufficient. Remove an optional composed region and test state, focus, and labeling. Attempt to change internal DOM order without changing semantic roles; public compositions should survive.

Count product-specific conditions in the shared core after adding the capability. Growth indicates misplaced ownership.

## Output contract

Produce a `composition-boundaries-contract` with core invariants, composition seams, shared-state ownership, required semantic relationships, optional-region behavior, prohibited internal dependencies, representative compositions, and criteria for promoting or extracting capabilities.

## Handoffs

Use `designing-component-api-governance` for prop/event surfaces, `designing-slot-and-part-contracts` for named regions, `designing-variant-prop-taxonomies` for finite semantic variants, and `governing-design-system-evolution` when moving established responsibility across boundaries.