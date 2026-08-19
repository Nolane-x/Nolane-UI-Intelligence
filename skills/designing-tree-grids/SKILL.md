---
name: designing-tree-grids
description: Use when hierarchical rows also expose aligned tabular columns and the interface must combine tree expansion with grid navigation, selection, editing and large-data behavior without collapsing hierarchy into a flat table.
---

# Designing Tree Grids

## Parent Contract
**Required parent:** `designing-data-dense-interfaces`.

This faculty owns hierarchical interactive tabular structures. A simple tree view and a flat editable grid are siblings with different focus/selection trade-offs.

## Decision Model
Identify the hierarchy-bearing column, usually the first logical column, and preserve depth/expand controls there while other columns remain aligned across levels. Row identity and parent-child relationships are semantic data, not indentation pixels.

Choose focus model carefully. A treegrid can navigate rows/cells with directional keys while expansion/collapse uses the hierarchy column or row-level commands. Define whether focus is cell-based or row-based, how Right/Left (or locale-equivalent) interact with expansion, and how users reach other columns without conflicting with hierarchy navigation.

Selection can target rows/objects independently of focus. Collapsing a parent may hide selected/focused descendants; define whether descendant selection persists and where focus moves. Editing cells in collapsed branches must not leave active editors in hidden content.

Lazy loading and virtualization require hierarchy-aware indices. `aria-rowindex`/set metadata or equivalent accessible structure must reflect logical position where applicable; recycling visible rows cannot erase tree level or ownership.

## Failure Topology
- Arrow keys simultaneously expand hierarchy and move cell focus with no predictable precedence.
- Indentation is the only hierarchy cue and disappears under zoom/low vision.
- Collapsing a row leaves focus on an invisible child.
- Sorting a numeric column reparents rows accidentally instead of sorting within allowed hierarchy.
- Virtualization announces wrong row level/count after branches expand.
- Editing child cell continues after parent collapse.

## Falsification and Recovery
Navigate cell/row focus, expand/collapse, multi-select, edit, lazy-load, sort, virtualize, zoom and screen-reader test. The contract fails if hierarchy ancestry and current focus cannot be recovered after structural changes.

Recover by separating hierarchy and grid actions, stable parent/row IDs, explicit collapse focus policy and hierarchy-aware virtualization/accessible metadata.

## Output Contract
Return `tree-grid-contract` with hierarchy column, focus/navigation model, expansion rules, selection/edit interaction, sort constraints, lazy loading, virtualization/accessibility metadata and structural tests.