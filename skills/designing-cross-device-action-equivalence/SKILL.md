---
name: designing-cross-device-action-equivalence
description: Use when the same product operation must remain understandable and reachable across multiple devices, input modalities, form factors, remote controls, companion surfaces, or handoff contexts.
---

# Designing Cross-Device Action Equivalence

## Overview
Cross-device consistency does not mean identical controls. A desktop shortcut, touch gesture, remote-control button, voice command, and wearable action can all express the same user intent while requiring different mechanics and affordances. The invariant is the operation’s meaning, consequence, state transition, and recovery—not pixel geometry or gesture shape. This skill prevents platform adaptation from fragmenting the user’s mental model or forcing one device’s interaction grammar onto another.

## Parent Contract
**Required parent:** `routing-ui-work`.

Consume the canonical task model, platform surfaces, input modalities, action/state contracts, accessibility requirements, and platform conventions. If there is no shared operation across surfaces, do not route this skill merely because a product has several clients.

## Decision Model
### 1. Define canonical operations before triggers
Create an operation vocabulary such as select, activate, confirm, cancel, back, navigate, zoom, scrub, move, reorder, submit, undo, share, or dismiss. Record preconditions, effect, reversibility, risk, and state result independently of any device-specific gesture.

### 2. Map operation to device-native triggers
For each target surface, choose native triggers that fit its precision, reach, focus model, physical controls, viewing distance, and platform convention. Touch can use direct manipulation while TV uses directional focus; desktop may add keyboard commands; voice can expose an equivalent intent. Equivalence does not require every device to expose every optimization, but critical operations must remain reachable.

### 3. Preserve semantic and consequence parity
The same named action should not have a materially different consequence on another device without explicit contextual reason. Keep confirmation policy, destructive severity, ownership, and undo semantics aligned. If a small surface intentionally offers a reduced operation, label the limitation instead of pretending parity.

### 4. Preserve transfer learning without freezing innovation
Reuse stable labels, command concepts, state names, and information architecture where they aid recognition. Allow device-specific shortcuts and direct manipulation when they improve performance. Avoid changing both label and interaction mechanism simultaneously unless the platform convention is stronger than learned product behavior.

### 5. Model handoff and concurrent control
When work moves between devices, define what state transfers, what remains local, what happens to in-progress input, which device currently owns focus/control, and how conflicts are resolved. A remote action must identify the target device or object before a consequential operation.

### 6. Verify alternatives and discoverability
Powerful gestures, shortcuts, hardware buttons, and voice commands need an discoverable equivalent when required by accessibility or novice use. Test operation coverage as a matrix: `canonical action × platform × modality × state × risk`.

## Evidence
ISO/IEC 4933:2026 establishes a current published framework for unifying input actions across devices. Use it as authority that cross-device action consistency is a distinct UI concern, while deriving project-specific mappings from platform guidance, observed user behavior, accessibility requirements, and task evidence. Record each target platform’s authoritative conventions separately; one standard cannot make a gesture universally appropriate.

## Output Contract
Produce a `cross-device-action-contract` containing: canonical action vocabulary; semantic preconditions/effects; platform-specific triggers; alternative access paths; naming consistency; destructive/confirmation parity; handoff and target-binding rules; focus/control ownership; reduced-capability declarations; discoverability plan; action-coverage matrix; conflict resolution; and verification scenarios for switching devices without relearning task meaning.

## Failure Traps
- Copying mobile gestures to desktop or TV in the name of consistency.
- Using the same label for actions whose consequences differ materially by device.
- Hiding essential operations behind gesture-only or hardware-only paths.
- Treating visual similarity as interaction equivalence.
- Dropping undo or confirmation on a compact client because there is less space.
- Letting a companion device issue an ambiguous destructive action without showing its target.
- Reordering navigation and renaming core actions on every surface with no task reason.
- Assuming cross-device parity means feature parity when a device cannot safely support an operation.

The design succeeds when users can transfer their understanding of *what the product does* while each device remains native in *how the action is performed*.

## V6 Cross-Device Action Continuity
Keep **action identity continuity** across web/mobile/desktop/watch/TV: the same named action should have the same consequence even if the interaction differs. Record **device-capability delta** for camera, biometrics, files, pointer, haptics, background execution, screen size, or secure hardware.

Use a durable **handoff token** for transferring object/task/version/context, not just a generic URL. Define **partial-action transfer** when a task begins on one device and must finish on another. Add a **duplicate-execution guard** so handoff/retry does not run the same payment/send/delete/agent command twice.

### Falsification
Start a task on device A, disconnect, continue on B, then resume A. If state/consequence diverges or duplicates, equivalence is false.

### Recovery
Reconcile authoritative action state, invalidate stale handoff tokens, and present the user with the exact completed/pending scope before continuing.
