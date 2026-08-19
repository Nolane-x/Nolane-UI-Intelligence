---
name: designing-dialog-systems
description: Use when a product needs modal or nonmodal dialog tasks and must consistently define modality, initial/final focus, action hierarchy, nested dialogs, validation and dismissal consequences.
---

# Designing Dialog Systems

## Parent Contract
**Required parent:** `engineering-rich-interactive-components`.

This faculty owns dialog interaction architecture. Motion belongs to `designing-modal-presentation-motion`; high-stakes action safety and form validation remain downstream/peer obligations.

## Decision Boundary
Choose modal only when the task requires a bounded interruption or prevents safe interaction with background context. Nonmodal dialogs/panels are preferable when users need to inspect or manipulate the underlying workspace concurrently. Do not use modal dialogs as generic containers for every small form.

A modal contract includes inert background, labelled dialog container, trapped tab sequence, predictable Escape/cancel policy and focus restoration. Initial focus depends on task: first field for data entry, a safe action for short confirmations, or a heading/static element when focusing a control would scroll meaningful content out of view. Never select a destructive primary action merely because it is visually prominent.

Action hierarchy should reflect consequences: primary completion, cancel/back, destructive alternative, secondary helpers. Validation keeps the dialog open and moves/explains errors without resetting entered state. Async submission must prevent duplicate commits while retaining a route to cancel when cancellation is genuinely possible.

Nested modal dialogs are a warning sign. If unavoidable, preserve a stack with one active modality owner and restore focus one level at a time.

## Failure Topology
- Modal visuals appear but background remains focusable/interactable.
- Initial focus lands on Delete, so pressing Enter accidentally confirms destruction.
- Escape discards unsaved complex work with no policy.
- Validation closes/reopens the dialog and loses fields.
- Nested dialogs produce multiple focus traps fighting each other.
- Closing restores focus to a trigger that no longer exists.

## Falsification and Recovery
Tab/Shift+Tab, screen reader landmarks, Escape, outside click, validation, async submit, trigger removal, nested overlay and browser back. The design fails if more than one modal context is operable or if focus can disappear into inert content.

Recover by simplifying task boundaries, promoting long workflows to pages/panels, centralizing modal stack ownership, selecting safe initial focus and defining explicit close/discard consequences.

## Output Contract
Return `dialog-system-contract` with modal/nonmodal rationale, labelled structure, initial/final focus, action hierarchy, dismissal/discard matrix, validation/async behavior, nested-dialog policy, overlay relationships and accessibility verification.