---
name: designing-drawer-and-sheet-motion
description: Use when edge drawers or sheets move between hidden, partial and expanded positions and the motion must coordinate drag physics, detents, scroll handoff and dismissal without losing state truth.
---

# Designing Drawer and Sheet Motion

## Parent Contract
**Required parent:** `designing-motion`.

This faculty owns motion across drawer/sheet positions. Component anatomy, content hierarchy and modality are separate decisions.

## Decision Model
Name the positional state machine before choosing easing: `closed`, optional `peek`, one or more semantic detents, `expanded`, and `dragging`. A detent must exist because it supports a useful task state—not because three snap points look sophisticated. On release, choose the next state from position, velocity, direction, platform conventions and destructive consequences.

For directly draggable sheets, the surface should track the gesture with minimal perceived latency. Apply resistance only beyond meaningful bounds; excessive rubber-banding makes precise placement impossible. When content inside the sheet scrolls, define ownership of vertical movement: at scroll top a downward gesture may transfer to sheet dismissal, while internal scrolling should not constantly tug the sheet.

Programmatic transitions and gesture transitions must converge on the same state model. If a keyboard command expands the sheet, it should land on the same detent as a gesture. Rotation, viewport resize and virtual keyboard appearance can invalidate pixel heights; preserve semantic detent intent rather than stale coordinates.

## Failure Topology
- Velocity alone dismisses a sheet containing unsaved work with no safety boundary.
- Scroll and sheet drag fight for the same gesture.
- The surface snaps to pixel positions that become wrong after keyboard/viewport changes.
- Releasing near a detent chooses different outcomes depending on frame rate.
- Background content parallax distracts from the active sheet or causes motion sickness.

## Falsification
Drag slowly/quickly across thresholds, reverse direction before release, begin from internal scroll positions, rotate/resize, open the keyboard, interrupt with system navigation, use keyboard/assistive alternatives and reduced motion. The final state must be deterministic from declared rules, not animation timing accidents.

## Recovery
Reduce detents to task-relevant states, separate scroll ownership, use semantic sizing, clamp destructive dismissal behind confirmation/recovery, and replace ornamental background movement with stable context.

## Output Contract
Return `drawer-sheet-motion-contract` with positional states, detent rationale, gesture mapping, release decision function, scroll handoff, viewport adaptation, interruption/cancellation, accessibility alternative and reduced-motion behavior.