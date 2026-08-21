---
name: designing-rotary-controller-focus-navigation
description: Use when an automotive HMI is navigated with a rotary controller, knob, touchpad-dial hybrid, or detented hardware and focus movement must map rotation, push, tilt, back, acceleration, and region transitions into predictable low-glance interaction.
---

# Designing Rotary Controller Focus Navigation

## Rotary input is not a mouse wheel
A rotary controller provides ordered, often detented input that users operate by feel. Mapping it directly to visual scroll can separate focus from action context and force visual search. This skill owns how rotation and associated hardware commands move focus, enter regions, activate controls, and accelerate through long collections.

## Parent Contract
**Required parent:** `designing-high-stakes-decisions`.

The parent provides high-stakes conservative interaction principles. This specialist begins when physical rotary input is a primary driver-facing modality.

## Control vocabulary
Define semantics for clockwise/counterclockwise detent, press/select, back, tilt/directional movement if hardware supports it, long-press, and acceleration. The decision owner is whether rotation changes focus, changes a focused value, or scrolls a container in each interaction state. Do not make the same rotation unexpectedly switch between these meanings without a clear mode cue.

For value adjustment, use an explicit edit mode or direct-manipulation convention that prevents accidental changes during navigation. Returning from adjustment should restore navigation semantics predictably.

## Focus order and regions
Rotary navigation needs a stable linear or region-aware order even when layout is spatial. Group controls into predictable sequences aligned with visual hierarchy. Crossing from navigation rail to content region should have clear entry/exit behavior. Disabled and unavailable controls are skipped according to declared rules rather than trapping the dial.

Long lists may use acceleration after sustained rotation, but focus should remain visually traceable. Detent count and selection movement need a stable mapping; missing or duplicated steps undermine eyes-off operation.

## Low-glance feedback
The focused target must be immediately recognizable, and value-adjust mode should be distinguishable from navigation. Pair tactile detents with visible movement; do not require reading tiny labels to know where the controller is operating. Audio cues may supplement but not replace visible focus.

## Evidence
Evidence includes hardware-event traces, detent-to-focus mapping, region transitions, edit-mode entry/exit, acceleration behavior, disabled-item handling, and driving-state restrictions. Test on representative physical hardware where possible because emulator key presses do not reproduce detent cadence and hybrid controls faithfully.

## Failure modes
Characteristic Failure includes rotation scrolling while focus stays offscreen, accidental value changes during navigation, skipped/duplicated detents, acceleration outrunning visible context, focus trapped in disabled regions, and inconsistent Back/press behavior across similar controls. Another failure is focus order that follows DOM/layout implementation rather than driver task hierarchy.

## Falsification
Rotate rapidly and slowly, reverse direction, enter/exit value edit repeatedly, disable intermediate controls, change layout mode, and transition driving state while the controller is active. The contract fails if one detent produces ambiguous movement, if focus becomes invisible, if a value changes outside declared edit semantics, or if lockout state can be bypassed through hardware navigation.

## Recovery
On lost focus, return to the nearest valid semantic target in the current region and preserve prior region memory. On ambiguous edit/navigation mode, default to navigation without committing a value change. Repair the command-state model rather than adding device-specific timing hacks.

## Output and Handoff
Output: `rotary-controller-focus-navigation-contract`, containing hardware command semantics, focus order, region transitions, edit modes, acceleration, lockout integration, and evidence. Handoff availability to driving-state lockouts and role-based access to driver/passenger authority splits.

## Sibling Boundary and delete-the-skill
Sibling directional focus graphs serve general D-pad/remote geometry; rotary navigation owns ordered detent semantics and value-edit mode. The delete-the-skill test passes because a rotary controller requires a tactile, mode-aware focus contract that cannot be safely inferred from pointer or arrow-key navigation.