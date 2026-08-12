---
name: designing-haptics-and-multisensory-feedback
description: Use when vibration, force, sound, speech, visual animation, LEDs, or other sensory channels communicate state, urgency, confirmation, direction, or error across mobile, wearable, automotive, game, XR, or embedded interfaces.
---

# Designing Haptics and Multisensory Feedback

## Overview
Use sensory channels as a coordinated code. Critical meaning must survive unavailable, disabled, masked, or inaccessible channels; haptics and sound enrich certainty but should not create exclusive information islands.

## Parent Contract
**Required parent:** `routing-ui-work`.

Require environment, available hardware, accessibility needs, privacy/noise constraints, urgency, and whether the feedback is acknowledgement, progress, warning, navigation, success, or error.

## Decision Model
Assign each event a semantic priority before choosing sensation. **Acknowledgement** confirms input was received. **State change** communicates a durable transition. **Guidance** helps direction or timing. **Warning** requests attention. **Critical alarm** indicates immediate consequence. Do not use the same vibration or sound family for all five.

Build redundancy by meaning, not duplication. A critical error may combine visible message, accessible announcement, and haptic/audio cue, but each channel should expose enough context for the user to know what happened and what to do next. Color plus vibration without text/semantics is still ambiguous.

Respect environment. Sound may be masked in traffic, forbidden in quiet/shared spaces, or impossible for deaf users. Haptics may be unnoticed on a desk, unavailable on hardware, uncomfortable, or turned off. Visual animation may be missed peripherally or reduced for motion sensitivity. Route urgency to channels that fit both context and capability.

Haptic vocabulary should be small and learnable. Distinguish intensity, rhythm, duration, and spatiality only when users can reliably perceive the difference. Repetition and escalation need fatigue limits. Provide settings where strong feedback is optional, while preserving critical semantics through another channel.

## Evidence
Test with channels individually disabled, noisy/quiet contexts, reduced motion, screen reader, device vibration settings, different hardware strengths, and repeated exposure. Verify accessible status messages, not just physical sensation. For alarms, validate prioritization with realistic workload.

## Output Contract
Return a `multisensory-contract` with `event_semantics[]`, `channel_mapping[]`, `redundancy_rules[]`, `haptic_vocabulary[]`, `audio_policy`, `visual_feedback_policy`, `accessibility_alternatives[]`, `escalation_and_fatigue`, `user_settings`, and `channel-loss-tests[]`.

## Failure Traps
- Haptic-only critical state.
- Ten subtle vibration patterns users are expected to memorize.
- Success chime in a privacy-sensitive shared context.
- Repeated alarm vibration that becomes background noise.
- Motion feedback with no reduced-motion equivalent.
- Audio volume/intensity as the only representation of severity.
- Assuming all devices implement the same haptic strength.

Multisensory design is robust when removing any one channel does not remove the user’s ability to understand and act.