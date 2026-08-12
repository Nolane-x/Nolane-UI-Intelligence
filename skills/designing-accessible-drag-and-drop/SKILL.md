---
name: designing-accessible-drag-and-drop
description: Use when users move, reorder, group, resize, connect, schedule, upload, or manipulate objects through dragging and an equivalent operation must remain available to people who cannot perform precise drag gestures.
---

# Designing Accessible Drag and Drop

## Overview
Drag is a spatial accelerator, not permission to make spatial dexterity mandatory. Preserve the mental model of moving an object while offering equivalent select–move–place operations across keyboard, single pointer, switch, and screen-reader contexts.

## Parent Contract
**Required parent:** `routing-ui-work`.

Require object semantics, valid destinations, ordering/grouping rules, input modalities, and consequence of an incorrect drop. If drag is purely decorative or physics-like and not functional, do not invent unnecessary alternate commands.

## Decision Model
Model drag as explicit states: idle object, selected/lifted, valid destinations available, candidate destination, committed move, cancelled move. The same state machine should back pointer drag and alternatives. Provide a non-drag path appropriate to the domain: Move to… command, position controls, up/down actions, destination picker, cut/paste, keyboard lift-and-drop, or structured reorder list.

Communicate what can move and where it can go without relying solely on animation. During operation, expose current object, original position, valid destination, proposed result, and invalid reason. For screen readers use concise state announcements; avoid narrating every pixel. For keyboard/gamepad, focus navigation while “holding” an object must be deterministic and cancellable.

Handle scrolling and virtualization. Auto-scroll must not run away from the pointer; dropping outside the viewport must not lose the object. Preserve original state until commit so Escape/cancel is reliable. For consequential moves, show outcome or undo rather than inserting a generic confirmation before every reorder.

## Evidence
Test with mouse/touch, keyboard-only, screen reader when applicable, coarse pointer, zoom, virtualized lists, long lists requiring scroll, invalid destinations, cancellation, and undo. On WCAG-governed web work, dragging functionality must have an applicable single-pointer non-drag alternative unless an exception truly applies.

## Output Contract
Return a `drag-drop-contract` with `objects[]`, `destinations[]`, `state_machine`, `pointer_drag_path`, `non_drag_paths[]`, `focus_and_announcement_rules`, `scroll_virtualization_rules`, `invalid_state_feedback`, `cancel_and_undo`, and `verification_matrix[]`.

## Failure Traps
- “Keyboard accessible” meaning users can focus the draggable object but cannot move it.
- Alternative buttons that change semantics or cannot reach all destinations.
- Position conveyed only through color or motion.
- Live-region spam on every movement.
- Auto-scroll that traps the user.
- Dropping commits before the user can cancel.
- Reordering controls visually hidden until hover with no other discovery path.

The alternate path must be functionally equivalent, not a second-class approximation.