---
name: designing-inline-editing
description: Use when displayed content becomes editable in place and the interaction must define entry, draft state, commit/cancel, validation, focus, concurrency and escape from edit mode without destabilizing surrounding content.
---

# Designing Inline Editing

## Parent Contract
**Required parent:** `engineering-rich-interactive-components`.

This faculty owns the transition between read and edit modes for a local value. It does not define the domain validation itself or large multi-field editing workflows.

## Decision Boundary
Inline editing is appropriate when context matters and the edit is small enough that moving to a dedicated form would add friction. Make editability discoverable through affordance, focus, command or consistent direct interaction; do not rely on an invisible double-click convention as the only route.

Maintain three states: displayed committed value, draft edit value and any external authoritative update. Define entry via click, Enter/F2, explicit edit control or domain convention. Define commit via Enter, blur, explicit save or combination; multiline fields often cannot use Enter as commit. Escape should usually cancel the draft, but not if Escape is already consumed by a nested picker without staged behavior.

Blur-to-save is convenient but risky when validation fails, focus moves to a related popup, or the user merely clicks away to inspect something. If the edit has material consequences, explicit commit may be safer.

Concurrent updates need policy. If the backing value changes while the user has a draft, do not overwrite the draft silently; surface conflict or preserve the local edit with provenance.

## Failure Topology
- Clicking anywhere outside commits an accidental half-edit.
- A date-picker popup causes blur and saves before the user chooses a date.
- Invalid value collapses back to read mode, losing error context.
- External update replaces the draft while typing.
- Layout width changes between read/edit, moving adjacent controls under the pointer.
- Screen reader is not told that a static label became an input.

## Falsification and Recovery
Test keyboard/pointer entry, nested popups, invalid input, Escape, navigation away, external update, slow save, failed save and repeated edits. The contract fails if draft vs committed value becomes ambiguous or focus leaves edit mode without a defined outcome.

Recover by making commit boundaries explicit, keeping invalid drafts visible, treating nested overlays as part of the edit session and introducing conflict state for concurrent change.

## Output Contract
Return `inline-editing-contract` with eligibility/affordance, entry triggers, read/draft/authoritative state model, commit/cancel matrix, blur policy, nested-overlay focus, validation/async/concurrency behavior and edit-session tests.