---
name: designing-target-size-and-spacing
description: Use when touch or pointer actions are dense, mobile, motor-sensitive, or high consequence and target geometry must support accurate activation without accidental neighbors.
---

# Designing Target Size and Spacing

## Parent Contract
**Required parent:** `designing-pointer-touch-pen-input`.

This faculty owns the activation geometry around interactive targets: effective hit area, spacing from competing targets, edge placement, and exceptions for inline or platform-native controls. It does not decide the visual size of every icon; a visually compact affordance can have a larger hit area when that does not create overlap or ambiguity.

## Decision Boundary
Classify controls by frequency, consequence, input context, and neighboring density. Primary touch actions, destructive controls, map markers, small icon buttons, and dense toolbars require different tradeoffs. Define the effective interactive region, not just the painted glyph. Invisible expansion must stop before it steals events from adjacent controls or makes overlapping targets resolve unpredictably.

Spacing can compensate when a control cannot grow because it is embedded in text or a dense specialized surface. Edge controls need particular attention because device bezels, browser gestures, and one-handed reach alter practical accuracy. Hover cannot be required to reveal the only usable hit target on touch hardware. Pen input may tolerate finer precision, but the design should not silently assume a pen when finger use remains allowed.

## Failure Topology
- A 16px icon is also the entire hit target on a phone.
- Invisible hit areas overlap, so tapping between two icons activates an arbitrary neighbor.
- Destructive and benign actions are packed together with identical geometry.
- An edge-aligned control conflicts with system back/home gestures.
- A dense toolbar passes desktop mouse testing but produces frequent touch misfires.
- Responsive compression shrinks spacing without changing the interaction model.

## Falsification and Recovery
Measure rendered hit regions and test with finger, mouse, coarse pointer emulation, zoom, and small devices. Include rapid repeated actions and controls near edges. The design fails if users can easily activate an adjacent consequence while aiming at the intended target, or if a target's operable area is materially smaller than its visual affordance suggests.

Recover by expanding hit regions, redistributing spacing, separating dangerous actions, changing responsive grouping, or moving infrequent controls behind deliberate disclosure. Where density is intrinsic, provide alternative keyboard/command paths rather than pretending precision is universal.

## Output Contract
Return `target-size-spacing-contract` with target classes, effective hit geometry, minimum spacing logic, overlap prohibition, edge/system-gesture constraints, responsive rules, dangerous-neighbor policy, and coarse-pointer verification cases.
