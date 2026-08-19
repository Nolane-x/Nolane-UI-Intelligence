---
name: designing-external-display-handoffs
description: Use when content moves or extends onto a projector, monitor, presentation display, secondary screen, or dedicated audience view and the product must separate presenter controls from what appears externally.
---

# Designing External Display Handoffs

## Parent Contract
**Required parent:** `designing-device-integration-interfaces`.

This faculty owns multi-display presentation state. It does not own casting media specifically. The app may mirror, extend, or create a distinct audience surface, and users need to know which content appears on which physical display before exposing sensitive or unfinished material.

## Decision Boundary
Define display modes: mirrored app, dedicated presentation, presenter view plus audience view, or detached workspace. Identify displays with human labels/geometry without assuming physical left/right is stable. Before sending sensitive content, show target and preview where practical. Presenter notes, controls, notifications, or private windows must remain on the intended private display.

Handle attach/detach, resolution/DPI changes, orientation, sleep, and primary-display changes dynamically. When the external display disappears, return the audience surface safely to the local app rather than losing controls offscreen. Fullscreen and pointer focus across screens need explicit ownership.

## Failure Topology
- Presenter notes appear on the projector because display roles swap silently.
- External monitor disconnects and the control window remains positioned offscreen.
- A newly connected display is auto-selected for sensitive content without confirmation.
- Audience view shows system notifications or private overlays from the presenter surface.
- Resolution change crops the primary presentation controls.
- Keyboard focus moves to an invisible audience window and traps input.

## Falsification and Recovery
Test one/two/multiple displays, connect/disconnect during presentation, role swap, resolution/orientation change, sleep/wake, fullscreen, notifications, app restart, and pointer/keyboard focus. The design fails if users cannot know which physical display is receiving private versus audience content.

Recover by explicit display roles, target preview/confirmation, separate presenter/audience window content, safe offscreen-window recovery, and re-evaluation on topology changes. Do not infer privacy from physical monitor position.

## Output Contract
Return `external-display-handoff-contract` with display discovery/roles, target selection, presenter/audience separation, privacy rules, attach/detach recovery, geometry/resolution behavior, focus/fullscreen policy, and multi-display verification cases.
