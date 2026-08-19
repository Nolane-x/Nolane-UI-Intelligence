---
name: designing-property-inspectors
description: Use when a professional interface exposes properties of the current selection and must handle mixed values, multi-edit, dependencies, live preview, invalid state and selection changes without losing causal clarity.
---

# Designing Property Inspectors

## Parent Contract
**Required parent:** `designing-editor-canvas-workspaces`.

This specialist owns selection-bound property editing. It does not define the domain property schema itself or the primary selection model.

## Decision Boundary
The inspector is a projection of current selection state, not a static settings form. For each property define applicability, value, editability, inheritance/source, mixed state across multi-selection, validation and whether changes preview live or commit explicitly.

Mixed values require a first-class representation. Blank is ambiguous: it can mean empty, unavailable, inherited or different values. Show mixed state distinctly and define what happens when the user enters a value—usually applying that value to all eligible selected objects, with scope made clear.

Selection can change while a field is focused. Decide whether an uncommitted edit commits to the old selection, cancels, blocks selection change, or follows a transactional editing model. Never silently apply half-typed input to the newly selected object.

Property dependencies need visibility. If enabling A reveals B or changes B’s valid range, preserve causal grouping and explain disabled/inherited state. Long inspectors need sections/search without hiding current validation errors.

## Failure Topology
- Mixed values render as empty, so users overwrite data accidentally.
- Typing in a field then clicking another object applies the text to the new selection.
- Multi-edit changes hidden ineligible objects partially with no scope report.
- Live preview fires expensive operations on every keystroke without cancellation.
- Inherited/locked values look merely disabled and users cannot discover the source.
- Inspector scroll position jumps to top on every selection update.

## Falsification and Recovery
Test single/multi-selection, mixed/inherited/locked states, selection change mid-edit, invalid input, undo, rapid live preview, partial applicability and large inspectors. The contract fails if the user cannot predict which objects and properties a commit will mutate.

Recover by modeling property provenance explicitly, separating draft from committed value, preserving inspector state where semantic sections persist and showing an edit-scope summary for multi-edit.

## Output Contract
Return `property-inspector-contract` with selection binding, property state algebra, mixed/inherited treatment, draft/commit policy, multi-edit scope, dependency rules, live-preview cancellation, validation/undo handoff and selection-change tests.