---
name: designing-editable-data-grids
description: Use when tabular data supports in-cell or row editing and the design must coordinate grid navigation, edit mode, selection, validation, paste/fill operations, virtualization and transactional save behavior.
---

# Designing Editable Data Grids

## Parent Contract
**Required parent:** `designing-data-dense-interfaces`.

This faculty owns the editing layer of an interactive grid. General grid navigation, cell editing details, sorting/filtering and backend transactions may route to sibling owners.

## Decision Model
Separate **navigation mode** from **edit mode**. Arrow keys that move among cells should not unexpectedly move the caret inside an editor, and text-editing keys should not trigger grid shortcuts while a field is active. Define clear entry/exit: Enter/F2/type-to-replace, click/double click or explicit editor activation, then commit/cancel with predictable keys.

Choose transaction granularity. Cell-level optimistic saves support speed but can produce partial rows; row-level commit supports validation dependencies; batch edit supports spreadsheet workflows. The UI must expose pending, failed and conflicted states at the granularity actually used.

Selection can coexist with editing but must be visually distinct. Multi-cell selection, copy/paste and fill handle operations require schema-aware parsing and a preview/error policy for partial invalid data. Never silently truncate a pasted matrix.

Virtualization must preserve editor identity. Scrolling an edited row out of the rendered window cannot destroy a draft without policy. If editing pins the row in memory, bound that behavior for large datasets.

## Failure Topology
- Arrow key intended for text caret moves to another cell and commits unexpectedly.
- Sorting while editing relocates the row and the draft attaches to the wrong record.
- Paste applies valid cells and silently drops invalid ones.
- Virtualization unmounts the editor and loses the draft.
- Pending save looks identical to committed data.
- Screen reader receives hundreds of tabbable controls instead of managed grid navigation.

## Falsification and Recovery
Edit while sorting/filtering, scroll out/in, paste multi-cell data, trigger cross-field validation, lose network, receive external changes, use keyboard/screen reader and large datasets. The contract fails if draft identity follows row position rather than stable record/field identity.

Recover by stabilizing IDs, separating navigation/edit state machines, selecting explicit transaction granularity and making partial failures/conflicts first-class.

## Output Contract
Return `editable-data-grid-contract` with navigation/edit modes, activation/commit keys, transaction granularity, selection interaction, paste/fill policy, virtualization draft retention, async/conflict states, accessibility model and adversarial tests.