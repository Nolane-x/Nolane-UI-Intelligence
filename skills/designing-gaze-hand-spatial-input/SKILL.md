---
name: designing-gaze-hand-spatial-input
description: Use when spatial or XR interfaces use eye/gaze targeting, hand gestures, pinch, indirect pointing, dwell, reach, or mixed spatial input where intent, comfort, occlusion, and target placement matter.
---

# Designing Gaze and Hand Spatial Input

## Overview
Gaze is excellent for indicating interest and dangerous as an automatic commitment signal. Separate attention from intent, then design hand or other confirmation so spatial interaction remains comfortable, private, and resistant to accidental activation.

## Parent Contract
**Required parent:** `routing-ui-work`.

Require headset/platform conventions, interaction distance, field of view, seated/standing context, hand tracking capability, accessibility scope, and whether gaze data is exposed or private. Coordinate with `designing-spatial-xr-interfaces` for spatial placement.

## Decision Model
Treat gaze as a candidate-target channel. Define target acquisition tolerance, visual response, and whether selection requires pinch, dwell, button, voice, or another signal. Dwell activation is appropriate only when intentional waiting is distinguishable from reading; repeated short dwell creates Midas-touch errors and fatigue.

Place frequent interactive targets in a comfortable visual and reach envelope. Avoid requiring neck rotation, extreme peripheral search, prolonged arm elevation, or precise mid-air tracing for routine tasks. Scale interactive regions for spatial uncertainty and distance. Handle occlusion: hands, windows, 3D content, and overlapping depth layers can block or confuse targeting.

Gestures need discoverability and feedback at three moments: readiness/tracking, recognized intent, and committed action. A system that only responds after the final pinch leaves users unsure whether tracking failed. Preserve alternatives for people who cannot perform a gesture or maintain gaze stability.

Privacy is unusual in gaze systems. Never expose or visualize raw gaze trails casually; focus-like highlighting should follow platform privacy conventions rather than imply surveillance.

## Evidence
Test seated and standing postures, different reach/body ranges, target depth/scale, hand occlusion, tremor, one-hand use, dwell duration, accidental gaze, loss of tracking, alternative input, and comfort over sustained use. Platform HIG is necessary but not proof of task comfort.

## Output Contract
Return a `spatial-input-contract` with `targeting_model`, `intent_confirmation`, `target_geometry`, `comfortable_envelope`, `dwell_policy`, `gesture_vocabulary[]`, `tracking_feedback`, `occlusion_rules`, `privacy_rules`, `alternative_inputs[]`, and `comfort_tests[]`.

## Failure Traps
- Gaze-to-activate everywhere.
- Tiny targets floating at arbitrary depths.
- Persistent arm-raised controls for frequent tasks.
- No feedback until a gesture fully succeeds.
- Gesture-only operation with no accessible alternative.
- Decorative depth that causes targeting overlap.
- Recording or showing gaze data without clear necessity and privacy treatment.

Spatial input should feel like intention made visible, not the system guessing that every glance is a command.