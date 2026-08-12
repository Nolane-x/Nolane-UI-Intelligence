---
name: designing-gamepad-remote-focus
description: Use when a TV, console, game, kiosk, spatial, or couch-distance interface uses D-pad, directional remote, controller, or focus-based navigation instead of free pointer targeting.
---

# Designing Gamepad and Remote Focus

## Overview
Directional navigation is a graph problem. The user should be able to predict where focus moves, see it from a distance, escape every region, and return to the correct context after overlays or navigation.

## Parent Contract
**Required parent:** `routing-ui-work`.

Require screen geometry, control grouping, remote/controller input map, viewing distance, scroll behavior, and modal layers. Do not assume visual proximity automatically gives the correct directional edge.

## Decision Model
Construct focus regions and explicit directional relationships. Within regular grids, spatial inference may work; across asymmetrical layouts, carousels, rails, drawers, and overlays, define intended transitions. Every region needs entry point, internal traversal, exit edges, and a recovery target when the previously focused item disappears.

Separate **focus** from **selection/activation**. Focus tells where an action would apply; selected state tells what is chosen or active. Their styling and semantics must remain distinguishable. At 10-foot distance or fast gameplay, focus indicator needs sufficient scale, contrast, and motion restraint to be recognized without masking content.

Scrolling follows focus without disorienting jumps. Keep a predictable amount of context visible, preserve row/column intent when moving between uneven collections, and remember focus when returning from details. Long holds/repeat acceleration need bounds so users do not overshoot.

Overlays create local focus scopes. Opening moves focus to a sensible target; Back/Escape closes or steps back according to platform convention; closing returns to the triggering locus. Never leave focus behind a modal or on an unmounted element.

## Evidence
Test only with the actual remote/gamepad model for complete workflows, rapid repeats, nested rails, scroll boundaries, empty/disabled items, overlays, Back behavior, and focus restoration. Test distance legibility and relevant accessibility settings rather than relying on a mouse-driven browser demo.

## Output Contract
Return a `directional-focus-contract` with `regions[]`, `focus_graph`, `default_entry`, `selection_semantics`, `repeat_behavior`, `scroll_follow_rules`, `overlay_scope_rules`, `back_escape_rules`, `focus_memory`, `missing_item_recovery`, and `controller_tests[]`.

## Failure Traps
- Nearest-neighbor focus jumping diagonally to a surprising control.
- Focus and selected state using the same visual treatment.
- Modal close button unreachable by D-pad.
- Carousel focus that moves offscreen while scroll lags.
- Returning from details to the top of the page instead of the triggering item.
- Tiny desktop focus rings viewed from across a room.
- Pointer-only hover states leaking into controller UX.

A directional interface feels “obvious” only after its focus graph has been deliberately designed.