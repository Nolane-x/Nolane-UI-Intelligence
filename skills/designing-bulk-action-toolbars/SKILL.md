---
name: designing-bulk-action-toolbars
description: Use when selection activates actions over many objects and the interface must make scope, eligibility, partial applicability, destructive consequences and selection persistence explicit.
---

# Designing Bulk Action Toolbars

## Parent Contract
**Required parent:** `engineering-rich-interactive-components`.

This faculty owns the action surface that appears when one or more objects are selected. Selection mechanics and individual action semantics remain separate.

## Decision Model
The toolbar must expose **scope before action**. Show selected count and, when relevant, the universe: “25 selected” differs from “All 8,240 matching items selected.” For cross-page or query-wide selection, distinguish explicitly between currently loaded rows and all matching records.

Compute action eligibility across the selection. If an action applies to only some items, choose deliberately among disable-with-reason, execute on eligible subset with clear summary, or require selection refinement. Silent partial execution is dangerous.

Appearance/disappearance should not destabilize the layout or cover selected items. Persistent placement may be preferable in data-heavy workflows; contextual replacement of a normal toolbar can work if users can still access selection controls and escape the mode.

Destructive bulk actions need consequence previews proportionate to scale, especially when objects differ in recoverability. Long-running operations need progress, cancellation where possible and a result summary that records successes/failures rather than pretending atomic completion.

## Failure Topology
- “Select all” means only the current page but users assume the entire result set.
- Delete is enabled for 100 items even though 20 are protected; execution silently skips them.
- Bulk toolbar covers pagination/filter context needed to understand scope.
- After action, selection remains on deleted IDs and later commands target stale objects.
- Confirmation repeats 500 item names instead of summarizing meaningful consequences.

## Falsification and Recovery
Test 1/2/1000 selections, cross-page select-all, mixed permissions, filtered results, partial failure, undoable and irreversible actions, keyboard selection and narrow viewport. The design fails if action scope cannot be restated precisely before commit.

Recover by centralizing selection scope, deriving eligibility per action, presenting subset consequences explicitly and reconciling selection after mutations.

## Output Contract
Return `bulk-action-toolbar-contract` with selection scope model, count/universe presentation, action eligibility matrix, placement/mode behavior, destructive confirmation handoff, long-running result handling, post-action selection reconciliation and scope tests.