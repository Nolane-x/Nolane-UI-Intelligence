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

## V6 Interaction Mechanics Protocol
For every material control, create an **input-to-state transition table** across keyboard, pointer, touch, pen, remote, voice, gaze, or alternative input that the task profile enables. Record precondition, trigger, preview/pressed state, commit event, cancellation, resulting state, focus destination, and announcement. The same semantic action may have different physical gestures, but it must not acquire contradictory meaning.

Perform an **acquisition-cost check** using target size, distance, repetition frequency, motor precision, edge placement, and consequence. Tiny targets used once in an expert desktop are different from tiny destructive targets in a repeated touch workflow. Model an **interruption-and-cancel path** for drag, long-running command, modal editing, streaming agent output, and any gesture with a pre-commit phase.

If the interface changes local state before server confirmation, define **optimistic-action rollback**: what is speculative, how conflicts appear, whether inverse action is safe, and how focus/selection survives rollback. For tools with modes—draw/select, edit/view, live/simulate—run a **mode-visibility probe**: a user arriving mid-session must be able to infer the current mode before taking a consequential action.

### Falsification
Trigger the same action through every supported input, interrupt at each intermediate state, double-trigger under latency, and switch mode without moving focus. A mismatch in commit semantics, cancellation, or visible mode falsifies the interaction contract.

### Recovery
Repair the transition model rather than adding one-off event handlers. Collapse ambiguous gestures, add explicit mode/status feedback, or defer optimistic updates when rollback cannot preserve product truth.
