---
name: designing-cell-editing
description: Use when a grid or spreadsheet cell can be edited and the interface must distinguish cell navigation, direct edit, formula/value display, commit movement, validation and editing of content longer than the visible cell.
---

# Designing Cell Editing

## Parent Contract
**Required parent:** `designing-spreadsheet-interfaces`.

This faculty owns one cell’s edit session. It does not own multi-cell grid navigation, formula semantics or transaction persistence beyond the edit boundary.

## Decision Model
Separate **selected/active cell** from **editing cell**. Typing while a cell is active may replace its content; Enter/F2/double click may enter edit preserving existing content; clicking into a formula bar may edit the same draft through another surface. Both editors must share one draft, caret and commit/cancel state.

Define movement after commit. Enter, Tab and arrow behavior varies by spreadsheet convention and product setting; never let an arrow intended to move the text caret commit unless edit mode explicitly hands it back to grid navigation. Multiline text needs a deliberate newline chord because Enter may otherwise commit.

Display value and underlying content can differ: formatted dates, percentages, lookup labels and formulas may render a result while editing reveals source expression. Make the transition intelligible and avoid geometry shifts that hide neighboring context.

Invalid input can be blocked, accepted with error marker, or normalized depending on schema. Keep the draft visible when correction is required; do not silently restore the old value on blur and make users wonder whether save succeeded.

## Failure Topology
- Arrow key exits edit while the user moves the caret through a long formula.
- Formula bar and in-cell editor maintain separate drafts and overwrite each other.
- Double-click starts editing but text selection gesture also changes grid range.
- Cell value is truncated; edit overlay clips the remaining content with no expansion.
- Invalid blur silently discards the draft.
- Virtualization scroll unmounts the active editor and commits accidentally.

## Falsification and Recovery
Edit long text/formulas, use Home/End/arrows, paste, IME composition, invalid values, scroll, resize column, switch to formula bar, press Escape/Enter/Tab and use screen reader. The contract fails if active cell, draft, caret and committed value cannot be named separately.

Recover by centralizing edit-session state, making navigation/edit mode transitions explicit, retaining invalid drafts and pinning the active editor semantically through virtualization.

## Output Contract
Return `cell-editing-contract` with edit entry modes, shared draft/caret, in-cell/formula-bar surfaces, key handoff, commit/cancel/move behavior, validation, overflow editor geometry, virtualization policy and edit tests.