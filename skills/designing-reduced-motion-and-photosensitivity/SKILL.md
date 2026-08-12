---
name: designing-reduced-motion-and-photosensitivity
description: Use when a UI uses animation, parallax, zoom, scrolling effects, flashes, rapid transitions, camera movement, ambient motion, game effects, XR locomotion, or any visual change that can cause vestibular discomfort, distraction, or photosensitive risk.
---

# Designing Reduced Motion and Photosensitivity

## Overview
Motion is optional presentation unless the task fundamentally depends on temporal/spatial change. Preserve meaning and operability when motion is reduced, avoid hazardous flashing, and design camera/viewport movement with particular care in games and XR.

## Parent Contract
**Required parent:** `designing-accessible-interfaces`.

Require motion inventory, semantic purpose, frequency, duration, user control, reduced-motion platform setting, flashing content, and any camera/locomotion behavior. Coordinate with `designing-motion` but this specialist owns safety and accessible alternatives.

## Decision Model
Classify motion by purpose: orientation/state continuity, feedback, attention, spatial explanation, decoration, ambient atmosphere, or camera/locomotion. For every effect ask what information disappears if motion is removed. If nothing disappears, reduced mode may disable it. If meaning depends on transition, provide a non-motion state cue or shortened/faded alternative that preserves the information.

Avoid large-field scale/zoom/parallax tied tightly to scroll or pointer where it can trigger vestibular discomfort. User-initiated small motion can still be problematic if unavoidable. Respect platform reduced-motion preference by default and provide in-product controls for motion-heavy domains when valuable.

Photosensitivity requires strict handling of flashes, contrast changes, repetitive patterns, and large high-intensity regions. Do not use an animation preview as the only validation; measure relevant frequency/area thresholds with appropriate tools and standards when shipping potentially flashing content.

Games and XR need camera-specific alternatives: reduced shake, stable horizon, teleport/snap turn options, vignette or comfort mode where platform/domain supports it, and the ability to disable nonessential screen effects. Do not hide essential enemy/objective cues solely inside motion.

## Evidence
Inventory CSS/animation/video/game effects, test `prefers-reduced-motion` or platform equivalents, inspect state meaning with all nonessential animation removed, run flashing-content analysis where applicable, test scroll/parallax, camera movement, transitions, and motion controls. Include users with vestibular sensitivity where the product is motion-intensive.

## Output Contract
Return a `motion-safety-contract` with `motion_inventory[]`, `purpose_classification`, `reduced_motion_mapping[]`, `meaning_preservation[]`, `flashing_risk_controls[]`, `camera_locomotion_alternatives[]`, `user_settings`, `platform_preference_behavior`, and `motion_safety_tests[]`.

## Failure Traps
- Reduced motion only shortens animation from 600ms to 300ms while preserving large zoom.
- Navigation understanding depends on parallax trajectory.
- Flashing warning effect added because red color felt insufficient.
- XR camera moves the user without comfort options.
- Motion setting exists but resets every session.
- Essential state only visible during an animation that ends.
- “No one complained” used as evidence of photosensitive safety.

Reduced motion is a semantic alternate rendering of the same task, not a degraded mode.