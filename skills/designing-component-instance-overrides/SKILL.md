---
name: designing-component-instance-overrides
description: Use when visual-builder component instances need bounded local differences while preserving definition linkage, update behavior, nested ownership, reset, detach, and conflict visibility.
---

# Designing Component Instance Overrides

## Parent Contract

**Required parent:** `designing-visual-application-builders`.

This owner decides how instances diverge from reusable component definitions without becoming accidental copies. It does not design the reusable component itself. Its core responsibility is to preserve a legible relationship between definition state, instance-specific intent and future definition updates.

## Override model

Define which dimensions are overridable: content/text, child slot content, properties/variants, token/style values, visibility, data binding, interactions, nested instance choices or layout constraints. “Everything is editable” is not a neutral policy; it destroys the guarantee that a component update can propagate safely. Conversely, forbidding meaningful content/variant changes turns reuse into duplication.

Store overrides as intent against stable definition identities, not serialized snapshots of every resolved value. When the definition changes, recompute the instance and apply still-valid overrides. If an overridden target is removed/renamed/restructured, surface an orphan/conflict rather than silently retargeting by tree position.

Expose override provenance at the point of editing. Authors need to know whether a value is definition-owned, inherited, locally overridden, data-bound or changed by a nested instance. Provide reset at appropriate scopes: one property, one subtree, all overrides, or selected classes—not a single destructive reset button.

Detach is a structural boundary. Explain that detaching converts linked instance semantics into local authored structure and which future updates will stop. Allow undo and, where possible, preserve a reference to origin for inspection without pretending it remains update-linked.

Nested instances require compositional ownership. A parent instance override should not flatten or steal the child component's internal override model. Define how slots and exposed properties cross component boundaries.

## Evidence

Use real component schema revisions, nested components, variants, responsive changes, data-bound content and collaboration. Test updates that add/remove/rename fields or children, not just style tweaks. Inspect diff/provenance after definition changes.

## Failure topology

Failures include storing full resolved snapshots so every instance appears overridden; definition updates wiping intentional local content; stale overrides targeting the wrong child after reorder; reset removing data bindings; detach occurring implicitly when an unsupported edit is attempted; and nested overrides that cannot identify which component definition owns the property.

## Falsification

Create several instances with different override types, then evolve the definition structurally and visually. Rename/delete targets, change variants, nest another component, undo, collaborate and reset selectively. The contract is falsified if linkage status cannot be explained, if a definition update silently changes the meaning of an override, if reset scope is unpredictable, or if an unsupported mutation secretly detaches/copies structure.

## Recovery

Rebind overrides to stable semantic IDs, classify orphaned overrides explicitly, and require conscious resolution when definition evolution invalidates intent. Convert snapshot-style overrides to sparse intent where possible. If an instance has drifted beyond meaningful linkage, offer a deliberate detach or new-definition extraction rather than continuing a fictional relationship.

## Output contract

Return a `component-instance-overrides-contract` containing overridable dimensions, storage model, definition-update reconciliation, orphan/conflict behavior, nested ownership, reset scopes, detach semantics, provenance UI, collaboration rules and migration/falsification scenarios.

## Handoffs

Use builder component authoring for definition APIs, slot insertion for exposed child regions, style inheritance for cascade provenance, data-binding owners for bound values, and design-system component API owners when reusable definitions are shared beyond one builder project.