---
name: governing-component-slot-contracts
description: Use when a component exposes named insertion points and allowed content, cardinality, ordering, ownership, and invalid compositions need explicit enforcement.
---

# Governing Component Slot Contracts

## Composition Problem
Slots are more than holes in markup. A component that accepts arbitrary content in arbitrary regions can lose semantics, focus order, layout guarantees, or accessibility relationships. This skill owns the content contract for each exposed insertion point.

## Parent Contract
**Required parent:** `architecting-component-systems`.

The parent defines component composition strategy. This specialist governs named slot obligations after composition is allowed.

## Slot Schema
For every slot define semantic purpose, required/optional status, cardinality, accepted content class, ownership of spacing/semantics, ordering relative to other slots, and whether slotted content participates in focus or labeling. Distinguish content slots from render-prop behavior and from public anatomy parts.

A slot that accepts “anything” still needs boundary rules when the host component makes assumptions. For example, an action slot may permit one or more controls but forbid nested navigation if the host claims dialog semantics.

## Valid and Invalid States
Model missing required content, too many children, incompatible interactive descendants, nested landmark conflicts, and asynchronous slot replacement. Invalid composition should fail early or degrade predictably; it must not silently corrupt host semantics.

## Evidence
Evidence uses valid/invalid fixture families, accessibility-tree inspection, focus traversal, layout stress with long/localized content, and consumer examples that prove the slot can be used without reaching private structure. Test portal and conditional rendering if a slot may move across DOM ownership boundaries.

## Failure Modes
Failure includes two primary actions inserted into a single-primary slot, interactive content nested inside an interactive host, a title slot omitted while the host still advertises a labeled-dialog requirement, slot content stealing spacing authority, or reorderable slots producing incorrect reading order.

## Falsification
Falsification deliberately supplies boundary compositions: zero, one, many, wrong semantic type, very long content, conditional removal, and nested focusable content. If the host still appears plausible while violating declared semantics or focus ownership, the slot contract is insufficient.

## Recovery
Recovery rejects or normalizes invalid content at the slot boundary, clarifies ownership, and provides a separate composition primitive when the requested use case is legitimately different. Do not widen a slot until it accepts arbitrary structure just to accommodate one exception.

## Output
Output: `component-slot-contracts-contract`, a per-slot schema with semantics, cardinality, content constraints, invalid-state handling, and validation evidence.

## Handoff
Handoff stable part identity to anatomy governance and state combinations to component-state contracts. Product-specific content decisions remain outside this skill.

## Sibling Boundary and delete-the-skill
Anatomy says what a region is; this skill says what a consumer may put there and under which invariants. Removing it leaves composition legality and host/child authority without an owner, satisfying the delete-the-skill test.