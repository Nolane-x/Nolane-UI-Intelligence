---
name: designing-object-grouping-and-locking
description: Use when editor objects can be grouped, nested or locked and the interface must distinguish structural grouping, selection scope, edit isolation and manipulation locks from permissions or visibility.
---

# Designing Object Grouping and Locking

## Parent Contract
**Required parent:** `designing-editor-canvas-workspaces`.

This faculty owns object-structure grouping and local manipulation locks. Authorization/permissions, layer hierarchy and general selection are separate concerns.

## Decision Boundary
A group creates a structural relationship among objects: selection and transforms may operate on the group while children retain identity. Define entry/isolation behavior for editing children, nested groups, ungrouping, and how property inspectors represent mixed/group properties.

Locking means “protect from ordinary manipulation in this workspace,” not “user lacks permission.” A locked object may remain visible/selectable for inspection, may be skipped by hit testing, or may require an explicit unlock command. Choose one model and communicate it. Do not make lock a security boundary.

Grouping and layering interact. Moving a group in hierarchy should preserve child order; ungrouping needs a deterministic destination/order. Hidden/locked descendants should not unexpectedly become editable because the group is selected.

Multi-selection can become a group, but avoid auto-grouping merely to perform a bulk transform if the user did not request persistent structure. Temporary transform sets and actual groups are different product objects.

## Failure Topology
- Locked item cannot be selected, so users cannot discover why it will not move.
- Lock icon implies permission/security and users assume collaborators cannot edit it.
- Ungrouping dumps children at the top of the layer stack.
- Double-click enters nested groups inconsistently and users lose selection context.
- Group transform changes hidden locked child despite a policy that says locked means immutable.
- Undo merges a temporary multi-transform with permanent grouping unexpectedly.

## Falsification and Recovery
Test nested groups, lock/unlock, selection through locked items, group transform, hidden descendants, reorder, ungroup, copy/paste and undo. The contract fails if structural state cannot be reconstructed from hierarchy + visible indicators.

Recover by separating group identity from temporary selection, defining lock as local manipulation policy, exposing lock reason/state, and preserving hierarchy positions on group/ungroup.

## Output Contract
Return `object-group-lock-contract` with group structure, selection/edit-isolation behavior, nesting, lock semantics/hit testing, transform policy, hierarchy preservation, permission disclaimer, undo behavior and structural tests.