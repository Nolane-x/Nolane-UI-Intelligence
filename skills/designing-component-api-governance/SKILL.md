---
name: designing-component-api-governance
description: Govern component APIs so capabilities remain composable and evolvable without accumulating contradictory props, hidden state coupling, or implementation leaks.
---

# Designing component API governance

Component APIs are product contracts. Use this skill when props, events, slots, variants, imperative handles, or composition patterns are being added to a shared component and local convenience may create long-term system debt.

## Decision ownership

Own API admissibility, semantic naming, controlled/uncontrolled boundaries, event contracts, extension points, and compatibility review. Decide whether a need belongs in the component, in composition, in a lower-level primitive, or only in a product wrapper.

## Inputs and evidence

Collect real consumer use cases, existing props and combinations, runtime state model, accessibility behavior, escape-hatch usage, wrapper components, issue history, and implementation constraints across supported frameworks/platforms. Inspect props that are mutually exclusive, conditional, or only meaningful together.

Record requests rejected in the past and whether consumers solved them by unsafe overrides.

## Procedure

Model the component’s conceptual state before adding API. Prefer APIs that expose intent rather than internal mechanics. Make invalid combinations unrepresentable where practical, or document and validate them explicitly. Keep controlled and uncontrolled modes behaviorally equivalent except for state ownership.

Use composition when consumer content or structure is genuinely open-ended. Use props when the system owns a finite semantic choice. Define event ordering, cancellation, and data payload stability. Treat accessibility semantics and keyboard behavior as part of the API contract.

Review every new prop against future combinatorial cost; ten booleans are rarely ten independent decisions.

## Failure topology

Boolean prop proliferation creates impossible state combinations. Implementation-leaking props freeze DOM or rendering strategy. Another failure is “escape hatch first”: a broad className/style/render callback bypasses system guarantees because the real capability was never modeled.

Controlled/uncontrolled drift can cause state races, and event callbacks without ordering guarantees lead consumers to depend on accidental timing.

## Falsification

Enumerate meaningful prop combinations and identify contradictions. Build at least three unlike consumer examples; if each requires bespoke conditionals inside the component, the abstraction may be wrong. Refactor the internal structure hypothetically and see which public props would break despite unchanged semantics.

Test keyboard, accessibility tree, and event ordering across controlled and uncontrolled use.

## Output contract

Produce a `component-api-governance-contract` containing component state model, public API inventory, prop/slot/event semantics, invalid-combination rules, controlled-state policy, extension boundaries, accessibility guarantees, compatibility classification, and examples showing supported composition patterns.

## Handoffs

Use `designing-composition-boundaries` for wrapper-versus-core ownership, `designing-slot-and-part-contracts` for structural extension, `designing-variant-prop-taxonomies` for variant modeling, and `designing-design-system-versioning` when changing established APIs.