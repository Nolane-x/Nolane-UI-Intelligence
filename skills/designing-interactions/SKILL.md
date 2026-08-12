---
name: designing-interactions
description: Use when a UI contains meaningful controls, direct manipulation, selection, asynchronous behavior, feedback, shortcuts, destructive actions, or modality-specific interaction.
---

# Designing Interactions

## Overview
Interaction design specifies what users can do, how they know they can do it, what happens during the action, and how they recover. Visual affordance and behavioral semantics must agree.

## Parent Contract
**Required parent:** `routing-ui-work`.

Use user/task model, flow model, and component semantics when available.

## Interaction contract per action
For every critical action specify:
- trigger/control and user-recognizable label
- allowed input modalities
- preconditions/permissions
- visible affordance
- focus/selection relationship
- immediate feedback (< action acceptance)
- in-progress behavior
- success behavior
- error/partial behavior
- cancellation/undo
- repeated activation behavior
- resulting focus/location

## Affordance integrity
Interactive things must look interactive in their context; non-interactive things must not borrow control styling without a reason. Hover-only affordance is insufficient for touch/keyboard. A decorative card with hover elevation can falsely imply the entire card is clickable.

## Feedback timing
Match feedback to latency:
- immediate local state for accepted input
- progress/working state when delay is perceptible
- resumable/background status for long jobs
- optimistic update only when failure can be reconciled truthfully

Do not show success before the product has crossed the relevant commit boundary.

## Selection, focus, hover, and activation
These are different states. Keyboard focus is not selection. Hover is not confirmation. Pressed is not persistent active state. Define them separately and ensure visual treatment remains distinguishable where coexistence matters.

## Direct manipulation
For drag/drop, resize, canvas, reordering, or gestures define:
- grab affordance and target
- valid/invalid drop zones
- preview
- constraints/snap behavior
- keyboard or alternate path where accessibility requires it
- cancellation
- undo
- offscreen/scroll behavior

## Shortcuts
Shortcuts accelerate discoverable actions; they must not be the only path unless the product is explicitly a keyboard-native expert tool and the contract permits it. Avoid collisions with platform/browser conventions.

## Destructive actions
Choose between inline undo, confirm-on-commit, staged deletion, typed confirmation, or other friction according to consequence, reversibility, frequency, and target ambiguity. More friction is not automatically safer.

## Output: `interaction-contract`
Return `actions`, `modality_matrix`, `focus_model`, `selection_model`, `feedback_timing`, `async_behavior`, `direct_manipulation_rules`, `shortcuts`, `destructive_policy`, and `interaction_invariants`.

## Common failures
- Loading spinner with controls still accepting duplicate destructive input.
- Focus disappearing after modal close or list deletion.
- Whole rows clickable while containing nested buttons with unclear activation target.
- Tooltip as the only place an essential instruction exists.
