---
name: modeling-perception-and-motor-control
description: Use when UI success depends on seeing, hearing, targeting, reaching, holding, dragging, timing, precision, distance, motion, small displays, glare, tremor, fatigue, or mixed input capabilities.
---

# Modeling Perception and Motor Control

## Overview
Translate human sensing and movement constraints into geometry, timing, feedback, and alternative-input requirements. A control is not operable merely because its hit box exists.

## Parent Contract
**Required parent:** `routing-ui-work`.

Require platform surface, input modalities, viewing conditions, and accessibility target. If the physical environment is unknown but materially changes interaction — car, kiosk, headset, wearable — expose the uncertainty.

## Decision Model
For every high-frequency or consequential control model: acquisition distance, target size, spacing from competing targets, precision requirement, dwell/hold duration, movement direction, repetition, and feedback latency. Separate visual bounds from interactive bounds. Small visual affordances may have larger hit areas, but overlapping or surprising hit areas create new errors.

Model perception beyond nominal contrast. Consider viewing distance, pixel density, magnification, glare, peripheral versus focal attention, color-vision independence, temporal change, and whether information survives dark/high-contrast/forced-color contexts. For auditory or haptic information, ask whether the channel is available in the environment and whether equivalent meaning exists elsewhere.

Avoid gesture essentialism. Multi-finger, path-dependent, drag, motion, or precision gestures need an alternative when capability or applicable accessibility guidance requires it. Concurrent inputs must not corrupt state: switching from pen to keyboard or touch to mouse should preserve selection, focus, and action meaning.

Timing is part of motor accessibility. Short timeouts, tiny transient controls, double-click requirements, accidental activation on pointer-down, and immediate destructive consequences create avoidable motor error.

## Evidence
Use actual target geometry, device/input tests, keyboard/switch paths, zoom/forced-color checks, WCAG input-modality obligations where applicable, platform ergonomics, and realistic environment tests. Record the weakest supported modality rather than only the primary demo path.

## Output Contract
Return a `perceptual-motor-envelope` with `viewing_conditions[]`, `input_capabilities[]`, `target_constraints[]`, `precision_risks[]`, `timing_constraints[]`, `channel_redundancy[]`, `gesture_alternatives[]`, `concurrent_input_rules[]`, and `evidence_requirements[]`.

## Failure Traps
- Using visual size as the only measure of target operability.
- Hover-only discovery on touch or gaze systems.
- Dragging as the only way to reorder or move.
- Color, sound, or haptics as the only carrier of critical meaning.
- Designing at one zoom level or one viewing distance.
- Focus state that disappears when switching input mode.
- Treating accidental activation as user carelessness instead of interaction design failure.

Model the real action envelope first; decorative micro-interaction comes later.