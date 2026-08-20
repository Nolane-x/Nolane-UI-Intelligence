---
name: designing-builder-layout-constraint-editing
description: Use when a visual builder edits flex/grid/constraints, intrinsic sizing, absolute anchors, min/max, gaps, alignment, aspect, and parent-child layout relationships without reducing responsive layout to x/y coordinates.
---

# Designing Builder Layout Constraint Editing

## Parent Contract

**Required parent:** `designing-visual-application-builders`.

This faculty owns how authors manipulate layout **rules** in a visual environment. Generic composition decides desired relationships; this skill makes those relationships editable and inspectable in a system where the rendered position is usually a consequence of parent and child constraints rather than a stored pixel coordinate.

## Constraint reasoning

For a selected object, expose both the value and its controlling relationship. Width may be fixed, content-sized, fill/flex, grid-track-derived, percentage, viewport/container-relative or bounded by min/max. Position may come from normal flow, grid area, alignment, margin/gap, absolute anchors or transform. A drag interaction must map intentionally into one of these rules; it must not silently convert an intrinsic/flex child to absolute positioning simply because direct manipulation is convenient.

Clarify parent versus child ownership. Grid columns and gap belong to the container; an item's span/alignment may belong to the child. Flex distribution can involve both. Inspector navigation should let authors jump to the controlling parent without losing selection context. Mixed selections must not display a fake single value when constraints differ semantically.

Direct manipulation needs predictive feedback. Resizing a fill item might change flex basis, max width or sibling allocation depending on the product's model. Show which rule will be authored before commit. Snapping/guides may visualize geometry but should not imply permanent constraint relationships unless a constraint is actually created.

Handle conflicting/overconstrained systems explicitly. Absolute left+right+width, grid placement plus manual translation, fixed height plus content overflow, or min greater than max need diagnostics rather than arbitrary solver outcomes. Preserve content-driven behavior as a first-class choice; builders otherwise tend to freeze every observed size.

## Evidence

Use actual runtime layout engine, exported styles/code, nested flex/grid/absolute examples, long/localized content, reusable components in several parent sizes, min/max/aspect cases and continuous resize. Compare visual manipulation with resulting authored rule diff.

## Failure topology

Failures include dragging an item and accidentally switching it to absolute; inspector showing `320px` while actual width is grid-derived; resizing a child when the necessary fix is parent track definition; hidden min/max constraints making handles appear broken; and builder-generated wrappers changing layout semantics between editor and runtime.

## Falsification

Manipulate nested flex and grid layouts, resize containers continuously, insert long content, change sibling counts, move components between parents, switch breakpoints and inspect exported rules. The contract is falsified if the author cannot predict what rule a drag/resize will change, if runtime position differs because inspector hid the controlling constraint, or if responsive/intrinsic behavior is lost without an explicit conversion.

## Recovery

Restore semantic layout modes, surface controlling parents and constraint provenance, remove accidental fixed/absolute values, and offer conversions with previewed diffs. For legacy overconstraint, show the conflicting rules and let the author choose authority rather than silently deleting one.

## Output contract

Return a `builder-layout-constraint-editing-contract` containing supported layout modes, sizing semantics, parent/child ownership, direct-manipulation mapping, conversion rules, conflict diagnostics, intrinsic-content policy, multi-selection behavior, runtime/export parity and stress scenarios.

## Handoffs

Use responsive breakpoint authoring for range-specific rules, generic composition for intended hierarchy, snapping/manipulation owners for input mechanics, style provenance for inherited layout properties and component authoring for reusable layout APIs.