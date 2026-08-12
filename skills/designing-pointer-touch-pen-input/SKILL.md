---
name: designing-pointer-touch-pen-input
description: Use when a UI accepts mouse, trackpad, touch, stylus, or other direct pointing input and target size, hover, precision, gestures, cancellation, palm rejection, or input switching materially affects operation.
---

# Designing Pointer, Touch, and Pen Input

## Overview
Direct input modalities share coordinates but not capability. Mouse precision and hover, finger occlusion and coarse targeting, trackpad gestures, and pen precision/pressure must not be collapsed into one pointer assumption.

## Parent Contract
**Required parent:** `routing-ui-work`.

Require device classes, input modalities, target environment, and applicable accessibility target. When multiple inputs can coexist, preserve state across modality switches.

## Decision Model
For every interactive target define visual affordance, hit geometry, spacing, activation event, cancellation path, and feedback. Use the coarsest realistic input to set minimum operability; precision-only affordances must have alternatives. Never depend on hover for essential labels, content, or actions because touch and many assistive contexts have none.

Separate preview from commit. Pointer-down can provide pressed feedback, but consequential activation usually commits on an event that permits cancellation when the pointer moves away. For touch, account for finger occlusion, edge reach, system gestures, scrolling conflicts, and accidental double activation. For pen, decide whether pressure, tilt, barrel button, hover, and palm rejection are enhancements or essential semantics. If essential, provide an equivalent for devices without them when the product promises cross-input support.

Gestures need a vocabulary and ownership model. Pinch, swipe, rotate, long-press, and edge gestures can conflict with platform or accessibility behavior. Custom gestures require discoverable alternatives. Drag interactions route to the dedicated drag skill.

Input switching must preserve selection/focus where reasonable: touching a canvas should not destroy keyboard selection; moving a mouse after stylus use should not unexpectedly change tool mode.

## Evidence
Inspect actual CSS/device target geometry, pointer cancellation, coarse-pointer layouts, touch scrolling, pen behavior when supported, zoom, orientation, and platform conventions. WCAG target/gesture rules are evidence obligations on applicable web surfaces, not approximate aesthetic suggestions.

## Output Contract
Return a `direct-input-contract` with `target_rules[]`, `activation_and_cancel`, `hover_policy`, `touch_reach_and_occlusion`, `gesture_map[]`, `pen_capabilities`, `concurrent_input_rules[]`, `system_gesture_conflicts[]`, `alternatives[]`, and `runtime_tests[]`.

## Failure Traps
- Desktop hover menu copied to touch unchanged.
- Tiny icon hit targets because the SVG is visually small.
- Destructive action firing on pointer-down.
- Long-press as the only way to discover a function.
- Stylus-specific control silently missing for mouse/touch users.
- Input switch resetting selection or mode.
- Enlarged hit areas that overlap neighboring controls and create ambiguity.

Choose interaction geometry from capability and consequence, not from visual density alone.