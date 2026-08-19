---
name: designing-multi-selection-models
description: Use when users can act on more than one object and the interface must define selection membership, focus, additive/toggle behavior, persistence, scope and action consequences across pointer, keyboard and touch.
---

# Designing Multi-Selection Models

## Parent Contract
**Required parent:** `designing-pointer-touch-pen-input`.

This faculty owns the abstract selection set and its interaction semantics. Range selection, lasso geometry and bulk action presentation are sibling concerns.

## Decision Boundary
Define selection as a set of stable object IDs, not highlighted DOM rows. Keep **focus/current object**, **selection membership**, **hover**, and **active drag source** distinct. A focused item can be unselected; a selected set can persist while focus moves for inspection.

Choose interaction conventions that match platform/task: click/tap replace selection; modifier-click may toggle/add; checkboxes can provide explicit multi-select on touch or enterprise tables; a dedicated “Select” mode may be appropriate on mobile where modifier keys are absent. Do not import desktop modifier semantics blindly into touch.

Selection scope must survive or intentionally react to filtering, pagination, hierarchy and data refresh. If selected objects become hidden by a filter, decide whether they remain selected and make hidden-selection count visible before actions. Remote deletion or permission loss must remove/mark affected IDs rather than leaving ghost membership.

Selection should have a clear escape route: click empty space, Escape, explicit Clear, back from selection mode, or task-specific behavior. Avoid accidental clearing when users interact with controls inside selected items.

## Failure Topology
- Focus highlight is used as selection, so arrow navigation changes bulk-action targets.
- Clicking a checkbox and clicking a row follow conflicting toggle rules.
- Filter hides selected records but bulk delete still affects them with no scope warning.
- Touch has no way to add to selection without long-press guesswork.
- A selected item deleted remotely remains counted and actions fail later.
- Clicking a button inside a row clears the entire selection before the action executes.

## Falsification and Recovery
Test pointer modifiers, keyboard navigation, touch selection mode, controls inside rows, filtering, pagination, remote deletion, selection across hierarchy and undo. The contract fails if the selected ID set cannot be stated deterministically after each event.

Recover by centralizing selection state, separating focus/current from membership, making hidden selections explicit and choosing one platform-appropriate additive mechanism per modality.

## Output Contract
Return `multi-selection-contract` with selection identity model, focus distinction, replace/add/toggle events by modality, scope across filtering/paging, hidden/stale membership policy, clear-selection routes and event-sequence tests.