---
name: designing-foldable-large-screen-interfaces
description: Use when a mobile or tablet interface must adapt across large displays, split-screen, multiwindow, folding postures, hinges, book/tabletop modes, or major width changes that alter information relationships.
---

# Designing Foldable and Large-Screen Interfaces

## Overview
Large and folding screens change task topology, not just component width. Use additional space to reveal relationships, parallelize context, and preserve continuity across posture changes without turning the UI into empty margins.

## Parent Contract
**Required parent:** `routing-ui-work`.

Require supported window classes/postures, orientation and split-screen expectations, hinge/occlusion information where available, input modalities, and the phone/tablet task model. Coordinate with general responsive layout rather than duplicating breakpoints.

## Decision Model
Choose an adaptation strategy per region: **reflow** changes arrangement, **reveal** adds useful simultaneous content, **relocate** moves controls for reach/context, **replace** uses a platform-appropriate presentation, and **persist** deliberately keeps structure stable. Do not make every width transition a proportional scale.

Identify pane relationships. Master/detail, list/editor, canvas/inspector, media/queue, and navigation/content can coexist when it reduces navigation and memory load. Define when panes split, merge, overlay, or remain independently scrollable. Preserve selected object and scroll/focus context as panes appear or disappear.

Treat hinges and folds as environmental boundaries. Avoid placing primary controls, text, or critical drag targets across occluded or uncomfortable regions. Tabletop posture can create upper display/lower controls; book posture may favor dual panes. Do not assume portrait orientation or a single full-screen window.

Reach and input vary. Large touch screens need reachable controls and reasonable target spacing; keyboard/pointer may coexist. Dragging across panes must retain alternatives. External keyboard should not break mobile touch affordances.

## Evidence
Test compact, medium, expanded windows; split-screen; rotation; fold/unfold continuity; hinge/occlusion; tabletop/book postures when supported; external keyboard/pointer; long content; and process recreation where runtime emulation is limited. Verify state continuity rather than screenshot fit only.

## Output Contract
Return a `large-screen-contract` with `window_classes[]`, `postures[]`, `adaptation_by_region[]`, `pane_relationships[]`, `hinge_rules`, `state_continuity`, `reach_and_input_rules`, `orientation_policy`, `multiwindow_rules`, and `transition_tests[]`.

## Failure Traps
- Centering a phone-width column on a huge canvas without a reason.
- Filling space with decorative cards instead of useful simultaneous context.
- Duplicating the same information in two panes after expansion.
- Losing selection when folding/unfolding.
- Critical controls behind or spanning a hinge.
- Portrait-only logic on resizable windows.
- Treating tablet as a single fixed breakpoint.

The design should remain one coherent task as the device changes shape.