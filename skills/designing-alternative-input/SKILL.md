---
name: designing-alternative-input
description: Use when a UI must remain fully operable through keyboard-only, switch control, assistive pointer, voice access, scanning, head tracking, or other input paths that cannot rely on the primary gesture or precision device.
---

# Designing Alternative Input

## Overview
Alternative input is complete task reachability, not a checkbox that every control can technically receive focus. Design traversal, grouping, activation, manipulation, timing, and recovery for users who cannot use the primary motor path.

## Parent Contract
**Required parent:** `routing-ui-work`.

Require task-flow critical actions, semantic component model, primary modalities, platform accessibility services, and any custom canvas or gesture surfaces. Coordinate with root accessibility obligations.

## Decision Model
Map the full workflow to a modality-independent action vocabulary: navigate, focus/select, activate, adjust value, move/reorder, reveal context, dismiss/cancel, submit/commit, undo/recover. For each action specify at least one path available to the alternative modalities in scope.

Optimize traversal cost. A switch user scanning 200 individual table cells experiences a fundamentally different interface from a pointer user. Use semantic grouping, region navigation, composite-widget patterns, shortcuts, and skip mechanisms so repeated operation does not become physically exhausting. Preserve predictable order and clear current location.

Custom canvases are high risk. Shapes, nodes, timelines, maps, and game-like editors need semantic mirrors or command surfaces that expose selection and actions without pixel-perfect pointing. A screen reader may need a structured list/tree representation; a switch user may need focusable groups and move commands; voice access needs stable accessible names.

Time requirements must accommodate slower input. Avoid transient controls and timeouts that expire before scanning or speech activation. If a time limit is essential, expose extension or alternate completion where allowed.

## Evidence
Test representative end-to-end tasks using actual keyboard/switch/voice-access or platform emulation, not tab-stop counts. Measure number of traversal actions, dead ends, inaccessible custom regions, focus loss, timing failures, and whether every destructive/recovery action remains reachable.

## Output Contract
Return an `alternative-input-contract` with `action_vocabulary[]`, `modality_paths{}`, `navigation_groups[]`, `custom_surface_equivalents[]`, `timing_accommodations[]`, `stable_names[]`, `focus_and_selection_rules`, `recovery_paths[]`, and `end_to_end_tests[]`.

## Failure Traps
- Every element focusable but the workflow requires hundreds of steps.
- Custom canvas with no semantic or command representation.
- Drag alternatives missing for keyboard/switch users.
- Tooltip or hover as the only action label.
- Timeouts that reset a scanning user.
- Voice-access targets with duplicate or unstable names.
- Focus disappearing after dynamic updates.

Parity means equal ability to accomplish the task, not identical mechanics.

## V6 Alternative Input Protocol
Model a **switch-scan topology** for sequential/group scanning: order, grouping, dwell/activation timing, back/cancel, and recovery from overshoot. Provide **dwell input fallback** where clicking/pressing is unavailable, with consequence-sensitive dwell or confirmation rather than one global timer.

Ensure a **voice-free action path** for products that otherwise rely on speech; noise, privacy, speech impairment, and context can make voice unavailable. Preserve **remapping persistence** for custom keys/switches/gestures across sessions and devices where meaningful. Tune **fatigue-aware timing** for long scanning/dwell sessions and allow pauses without losing place.

### Falsification
Complete core tasks using only switch scanning or configured alternative input, then introduce fatigue/overshoot and restart. If the user is trapped or remapping disappears, the interface fails.

### Recovery
Reduce scan depth, add grouping/direct shortcuts, restore mappings, and provide a reliable cancel/escape route independent of the failed input.
