---
name: designing-pointer-cancellation-accessibility
description: Use when press, drag, touch, or pointer gestures could trigger consequential actions before users have a reasonable opportunity to cancel an accidental down-event or movement.
---

# Designing Pointer Cancellation Accessibility

## Parent Contract
**Required parent:** `designing-pointer-touch-pen-input`.

This faculty owns when pointer actions commit: on down, on up, after movement, or through an explicit confirmation boundary. It focuses on error prevention for users with tremor, limited motor control, coarse touch, or accidental contact. It does not own the entire gesture vocabulary or drag-and-drop alternative path.

## Decision Boundary
Prefer activation on release for ordinary controls so users can move away before committing. Down-event activation requires a strong reason, such as an interaction whose semantics inherently begin on contact, and should still expose an abort path when possible. For press-and-hold, swipe, and drag gestures, define movement thresholds, cancellation zones, and what happens if the pointer leaves the target or the system interrupts the gesture.

High-consequence operations need stronger cancellation semantics than harmless navigation. A destructive action should not fire merely because a finger touched the wrong pixel during scrolling. Repeated controls in dense surfaces must prevent a down event intended for scrolling from becoming activation. Pen barrel buttons, mouse capture, and touch cancellation events should converge on the same committed-versus-aborted state model.

## Failure Topology
- An action fires on pointer-down and cannot be canceled by moving away before release.
- A list item activates while the user is attempting to scroll because movement threshold is too small.
- Dragging outside the window still commits to the last hovered target without explicit release context.
- Touch cancellation from an OS gesture leaves the interface in a half-pressed state.
- Destructive icon buttons commit earlier than ordinary buttons for implementation convenience.
- Pointer capture prevents users from escaping an interaction they did not intend to start.

## Falsification and Recovery
Test mouse, touch, pen, coarse pointers, tremor-like small movements, scroll starts, leaving/re-entering targets, OS interruptions, and lost pointer capture. The design fails if an accidental down event produces irreversible consequence before a user can withdraw, or if cancellation leaves the visual and underlying state inconsistent.

Recover by moving commit to release, adding movement/cancel thresholds, honoring pointer-cancel events, resetting provisional visuals, and routing high-impact operations through explicit confirmation or undo. Document true down-event exceptions rather than allowing them to spread as a component default.

## Output Contract
Return `pointer-cancellation-contract` with gesture commit point, provisional state, cancel thresholds/zones, pointer-cancel handling, scroll discrimination, high-consequence exceptions, reset behavior, and multi-input verification scenarios.
