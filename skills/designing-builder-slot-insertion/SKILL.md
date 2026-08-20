---
name: designing-builder-slot-insertion
description: Use when reusable builder components expose bounded insertion regions and authors must understand legal child types, ordering, defaults, nesting, empty state, drop targets, and ownership of inserted content.
---

# Designing Builder Slot Insertion

## Parent Contract

**Required parent:** `designing-visual-application-builders`.

Slots are not generic drag-and-drop zones. This skill owns the contract for inserting authored content into component-defined regions while preserving structural validity and clear ownership between the component definition and the instance's supplied children.

## Slot semantics

Give every slot a stable identity and purpose: label, accepted child capabilities/types, cardinality, ordering semantics, default/fallback content, whether nested slots are allowed, and whether the component can constrain layout around supplied content. A visual empty rectangle is not a sufficient API.

Clarify ownership. Slot **definition** belongs to the component; inserted **content** commonly belongs to the instance/context. Editing the component must not accidentally absorb instance content into its default. Editing an inserted child should preserve awareness that its surrounding layout may be controlled by the slot. If fallback content appears only when empty, distinguish it from real inserted content in hierarchy and selection.

Insertion needs valid target feedback before commit. Overlapping nested slots, invisible slots, conditional branches and responsive transformations can produce several geometrically plausible targets. Use semantic highlighting and destination labels rather than nearest-rectangle heuristics. Keyboard/non-pointer insertion requires an equivalent target-selection flow.

Moving content between slots is a reparenting operation and may change inherited styles, data context, focus/order semantics and event scope. Preview or warn when those effects are material. Prevent cycles: a component cannot be inserted into a slot in a way that creates recursive structure unless the product explicitly supports bounded recursion with safeguards.

## Evidence

Use component schema, accepted-child constraints, nested instances, empty/fallback states, responsive layouts, data/context inheritance and accessibility reading order. Test with ambiguous overlapping slots and structures that are visually identical but semantically accept different content.

## Failure topology

Failures include dropping into the nearest visual container even though it is not an exposed slot; treating fallback nodes as editable instance children; reparenting content and silently losing data context; allowing an invalid child that crashes runtime later; and nested slots whose highlights make it impossible to know which component will own the inserted object.

A subtle failure is slot leakage: deleting a component definition removes instance-authored content because the storage model failed to distinguish slot ownership.

## Falsification

Insert, reorder and move several child types across nested/conditional/responsive slots using pointer and keyboard paths. Empty/refill slots, edit fallback content, change component definitions and delete/recreate instances. The contract is falsified if destination ownership is ambiguous before drop, if invalid structures can be committed without explicit escape hatch, if instance content is lost by definition edits, or if runtime order differs from the authored slot order.

## Recovery

Reconstruct slot ownership from stable IDs and separate definition/fallback from instance payload. Add explicit accepted-content validation and target disambiguation. If a historical document contains invalid children, quarantine them with a visible repair state rather than silently moving them to another container.

## Output contract

Return a `builder-slot-insertion-contract` containing slot identities, accepted content/cardinality, ownership model, fallback semantics, drop/keyboard targeting, nested-slot disambiguation, reparenting effects, recursion policy, invalid-state recovery and verification scenarios.

## Handoffs

Use component authoring to define exposed regions, instance overrides for local component differences, canvas/hierarchy synchronization for target representation, data binding for context changes, layout constraints for spatial behavior and accessibility/order owners when slot order changes semantic reading/focus.