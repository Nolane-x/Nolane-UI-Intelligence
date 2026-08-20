---
name: designing-mobile-gesture-navigation-conflicts
description: Use when app gestures compete with operating-system back/home/edge gestures, scroll, pull-to-refresh, sheets, carousels, maps, canvases, or assistive gestures on touch devices.
---

# Designing Mobile Gesture Navigation Conflicts

## Parent Contract

**Required parent:** `designing-mobile-native-application-shells`.

This specialist owns arbitration between application touch gestures and higher-authority system/navigation gestures. It complements generic pointer/touch design by focusing on gesture arenas where multiple recognizers can plausibly claim the same movement and where a wrong winner changes navigation or loses work.

## Gesture arena model

List every recognizer active in the region: OS edge-back/home, app interactive back, vertical/horizontal scroll, nested scroll, pull-to-refresh, drawer reveal, sheet drag, carousel swipe, map/canvas pan, item drag, text selection, zoom, accessibility gestures, and product-specific interactions. For each pair, define initiation zones, direction/velocity thresholds, priority, simultaneous recognition, failure/cancellation behavior and accessible alternative.

System gestures generally outrank product convenience. Avoid placing high-frequency custom gestures in protected edge/home regions unless the platform explicitly defines coexistence. A visual affordance near an edge is not evidence that touch should start there. Increase target geometry inward or provide an explicit control rather than requiring users to disable/defeat OS navigation.

Distinguish gesture **recognition** from **commit**. Interactive transitions such as back or sheet dismissal need a progress phase and a cancellation path that restores state exactly. A child carousel may temporarily win horizontal movement only after direction is clear; before then the parent scroll/navigation system should not mutate. Nested scroll containers need handoff at extents rather than simultaneous fighting.

Gesture arbitration also depends on content state. A map or canvas may consume pan while in manipulation mode but yield it when a modal editor is open. An unsaved full-screen editor may allow system back gesture to begin yet intercept commit with a save/discard decision. Make state-dependent changes visible enough that users can predict them.

## Evidence

Collect platform gesture guidance, recognizer logs, touch traces from real devices, left/right handed use where relevant, screen sizes, nested scroll cases, accessibility services, stylus behavior if supported, and representative high-density edge controls. Slow-motion/video evidence can reveal recognizer switching and snap-back defects hidden by screenshots.

## Failure topology

Failures include a carousel that blocks OS back; an edge drawer that opens while the app begins a back transition; a nested sheet that steals vertical scroll before the inner list reaches its extent; a drag gesture that accidentally navigates away; and cancellation that restores the screen visually but leaves focus/selection/draft state changed.

Another failure is a threshold arms race: making app gestures require increasingly aggressive motion to avoid conflicts, producing fatigue and discoverability problems instead of resolving ownership.

## Falsification

Perform ambiguous diagonal/slow/fast gestures from protected edges, inside nested scrollables, on draggable items and while sheets/maps/canvases are active. Cancel interactive transitions at multiple progress points. Enable representative accessibility navigation. The contract fails if two surfaces move for one intention, system navigation becomes unreliable, state mutates on canceled recognition, or an essential command lacks a non-gesture path.

## Recovery

Simplify the gesture arena: remove low-value custom gestures, move initiation zones, use explicit handles/controls, defer recognition until direction is unambiguous, and define one mutation owner. Restore complete semantic state on cancellation. Do not fix systemic competition by globally disabling platform gestures unless the product context has exceptional, well-evidenced justification.

## Output contract

Return a `mobile-gesture-navigation-conflicts-contract` with recognizer inventory, conflict matrix, priority/threshold rules, protected zones, simultaneous-recognition exceptions, progress/commit/cancel semantics, nested-scroll handoffs, state-dependent modes, accessible alternatives, and physical-device test scenarios.

## Handoffs

Use generic pointer/touch owners for individual gesture mechanics, native stack owners for back semantics, drawer/sheet and carousel owners for component behavior, safe-area integration for protected edges, and accessibility modality owners when system assistive gestures constrain the arena.