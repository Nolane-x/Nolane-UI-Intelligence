---
name: designing-tree-views
description: Use when hierarchical objects must be browsed or selected in a compact expandable tree and the design must separate focus, selection, expansion, hierarchy and multi-select operations.
---

# Designing Tree Views

## Parent Contract
**Required parent:** `engineering-rich-interactive-components`.

This faculty owns hierarchical tree-view interaction such as file explorers, layer trees and category browsers. Treegrids and general navigation architecture are separate owners.

## Decision Boundary
A tree item has multiple independent dimensions: hierarchy level, expanded/collapsed, focus, selected/not selected, optional checked/stateful metadata and availability. Do not collapse focus and selection unless the product intentionally uses selection-follows-focus and that convention fits the task.

Keyboard navigation should respect hierarchical geometry: Up/Down traverse visible items; expansion/collapse and parent/child movement follow the chosen platform/ARIA pattern; Home/End and typeahead can accelerate large trees. Multi-select trees require explicit range/additive selection semantics and strong visual distinction between focus and selected items.

Expansion is not selection. Clicking a disclosure icon can expand without changing the active object; clicking the row may select. Define hit regions so users can predict whether they are navigating hierarchy or choosing an object.

Large trees need lazy loading and virtualization. Loading children must preserve the parent’s expanded intent, announce busy/error state, and not scramble focus when nodes arrive. Stable semantic node IDs are mandatory if rows are recycled.

## Failure Topology
- Moving keyboard focus edits/opens every item because selection follows focus accidentally.
- Clicking disclosure also changes selection and destroys a multi-selection.
- Virtualized rows reuse DOM identity and screen reader/focus jumps to another node.
- Loading child nodes inserts above the focused row and loses orientation.
- Indentation alone communicates hierarchy, failing at high zoom or low vision.
- Recursive nesting becomes so deep that labels have no usable width.

## Falsification and Recovery
Test keyboard traversal, single/multi-select, collapse a branch containing selected/focused descendants, lazy-load success/error, deep hierarchy, typeahead, virtualization, RTL and screen reader. The design fails if a node’s focus/selection/expansion state cannot be independently recovered after structural updates.

Recover by stabilizing node identity, separating disclosure from selection, preserving hidden descendant selection according to explicit policy, and moving excessively complex structures to search/breadcrumb/detail views.

## Output Contract
Return `tree-view-contract` with node model, focus vs selection policy, expansion semantics, pointer/keyboard map, multi-select rules, lazy loading, virtualization identity, hierarchy cues, accessibility roles/states and structural tests.