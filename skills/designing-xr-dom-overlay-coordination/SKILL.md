---
name: designing-xr-dom-overlay-coordination
description: Use when an XR experience combines immersive spatial content with conventional DOM or 2D overlay UI and must coordinate input, focus, visibility, lifecycle, safe areas, modality, and state without letting the two interface layers contradict each other.
---

# Designing XR DOM Overlay Coordination

Hybrid XR interfaces often have two UI systems: immersive spatial content and conventional DOM overlays. They differ in rendering, input routing, accessibility support, lifecycle, and coordinate space. Coordination must make them one product state rather than two competing control surfaces.

## Parent Contract
**Required parent:** `designing-spatial-xr-interfaces`.

The parent owns immersive spatial composition. This skill owns the seam between immersive content and DOM/2D overlay surfaces; generic web layout remains with existing responsive/component owners.

## Layer Authority
Declare which actions belong in immersive space, which belong in overlay, and which can appear in both. Avoid duplicate controls that can drift—for example, an immersive mute button and overlay mute button showing different state. If both exist, bind them to one authoritative action/state model.

## Input and Focus
DOM overlay may capture pointer/touch while immersive scene expects controller/hand events. Define hit routing, prevent click-through into the scene, and provide a clear exit from overlay focus back to immersive input. Keyboard and screen-reader focus should remain coherent when overlay opens; immersive focus indicators should not continue implying control simultaneously.

## Lifecycle
Handle entering/exiting immersive session, browser chrome changes, overlay availability, permission prompts, orientation change, and session interruption. If the platform does not support overlay for a capability, do not silently remove essential controls on entering XR; provide spatial equivalents or block the mode.

## Safe Area and Legibility
Overlay may compete with headset view cutouts, system affordances, or mobile browser controls in handheld AR. Respect platform safe regions and ensure overlay does not cover safety/permission prompts. Spatial state behind the overlay may need dimming or interaction pause so users know which layer owns input.

## Accessibility Boundary
DOM can offer stronger conventional accessibility than some immersive surfaces. Use that advantage deliberately, but do not claim the immersive task is fully accessible because an unrelated overlay menu is. Ensure equivalent essential actions where possible and document unsupported immersive requirements.

## Evidence
Test overlay open/close during XR, pointer/touch/controller input, keyboard focus, screen reader where supported, session enter/exit, permission prompt, orientation change, unsupported overlay platform, duplicated control synchronization, and browser back.

## Failure Modes
- Tap on overlay also activates immersive object behind it.
- Overlay and spatial duplicate controls disagree on state.
- Keyboard focus remains trapped when overlay closes.
- Entering immersive mode removes the only accessible exit control.
- System permission prompt is obscured by custom overlay.
- Overlay visibility persists after XR session ends with stale state.

## Falsification
Open an overlay above an active spatial control, change the same setting from both layers, then exit/re-enter the immersive session. Falsify if click-through occurs, states diverge, or focus/controls become unreachable.

## Recovery
Centralize action state, enforce input-layer capture, restore focus explicitly, reconcile session lifecycle, and provide fallback controls before entering unsupported modes. If overlay capability is unknown, feature-detect and gate rather than assuming.

## Handoff
Spatial panel placement remains with `designing-world-space-panel-placement`; generic DOM accessibility/layout use existing web owners; immersive interaction remains with ray/near-far/gaze-hand owners.

## Output Contract
Return an `xr-dom-overlay-coordination-contract` with `layer_ownership`, `duplicate_action_binding`, `input_routing`, `focus_transfer`, `session_lifecycle`, `safe_area_rules`, `accessibility_boundary`, `fallback_capabilities`, `evidence_cases[]`, `falsification_cases[]`, and `recovery_actions[]`.