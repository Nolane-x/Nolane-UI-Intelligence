---
name: designing-menu-entry-exit-motion
description: Use when menus or submenus need entry and exit motion that preserves anchor/context, supports rapid keyboard and pointer traversal, and never delays command access.
---

# Designing Menu Entry and Exit Motion

## Parent Contract
**Required parent:** `designing-motion`. Menu semantics, command organization and keyboard behavior remain owned by interaction/component faculties.

## Decision Boundary
Menu motion explains **where a command surface came from and where it goes**. It must be subordinate to immediate command access. Opening a menu is not a theatrical page transition: users often open, scan, traverse submenus and dismiss within a fraction of a second.

Anchor the motion to the trigger or parent item when spatially meaningful. Small opacity/scale/translation can communicate attachment, but the transform origin must follow actual placement after collision detection. If a menu flips above its trigger near the viewport edge, an origin still animating from below is contradictory.

Submenus require special care. Directional motion may reinforce hierarchy, but pointer intent corridors and keyboard arrow traversal matter more than animation. Do not close a parent because the pointer briefly crosses the gap while the submenu is animating. Opening/closing durations should not make diagonal traversal impossible.

Exit can be shorter than entry, especially for dismissal or command execution. However, the surface must become noninteractive at the semantic dismissal boundary even if a visual fade continues; ghost menu items must not receive clicks. Focus restoration or transfer happens according to the menu contract, not at `animationend`.

Reduced motion can use near-instant opacity or direct appearance. Motion should never encode which item is selected or checked without a persistent state cue.

## Failure Topology
- A 300–500 ms entrance makes repeated command use feel sluggish.
- Transform origin ignores collision flipping and visually detaches the menu from its trigger.
- An exiting menu still intercepts pointer events.
- Submenu animation competes with pointer intent and causes accidental closure.
- Keyboard users must wait for transitions before focus can move.
- Nested menus accumulate different easings and feel like unrelated libraries.

## Falsification and Recovery
Open/close repeatedly, traverse nested menus quickly by pointer and keyboard, place triggers at every viewport edge, resize while open, invoke a command during entry, press Escape immediately, and test reduced motion. If animation changes command reachability or focus timing, it fails.

Recover by decoupling semantic open/close from visual animation, using placement-aware origins, shortening travel, and removing submenu translation where it harms traversal.

## Output Contract
Return `menu-motion-contract` with anchor/origin rule, placement adaptation, entry/exit timing, submenu hierarchy treatment, semantic-vs-visual dismissal boundary, pointer/focus interaction, reduced-motion mode and edge-placement tests.