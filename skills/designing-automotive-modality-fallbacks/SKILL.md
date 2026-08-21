---
name: designing-automotive-modality-fallbacks
description: Use when an automotive task can use touch, rotary, steering-wheel controls, voice, physical switches, audio, haptics, or display channels and the UI must provide safe fallback when one modality is unavailable, unreliable, inappropriate, or restricted by driving state.
---

# Designing Automotive Modality Fallbacks

## No modality is universally available or safe
Automotive HMIs often distribute one task across touch, hardware, speech, sound, haptics, cluster, center display, and personal devices. Noise can degrade voice, gloves can reduce touch accuracy, a display may fail, steering-wheel controls may be limited, and driving-state policy may restrict visual interaction. This skill owns the fallback hierarchy that preserves essential task capability without pretending one modality can always substitute for another.

## Parent Contract
**Required parent:** `designing-high-stakes-decisions`.

The parent provides high-stakes authority and conservative degradation principles. This specialist begins when one user goal has multiple modality paths or when the primary modality can become unavailable.

## Capability and task mapping
Model modalities by the tasks they can safely support, not by feature parity. Record input availability, output availability, environmental constraints, driver/passenger role, task demand, confirmation needs, and failure detection. The decision owner is the fallback path for each essential task under each relevant degradation state.

A voice alternative is not automatically equivalent to touch. It may increase cognitive load, expose private content to passengers, fail in noise, or be unsuitable for precise value selection. A physical control may support coarse adjustment but not detailed configuration. Define what each fallback can and cannot preserve.

## Essential versus deferrable tasks
Separate essential driving/vehicle operations from convenience tasks. Essential operations should have robust fallback or clear safe-state behavior. A deferrable media or account task may simply be postponed until parked or until a capable surface returns. Do not overload degraded modalities with complex workflows just to claim functional parity.

## Feedback continuity
When input modality changes, preserve clear confirmation through an available output channel. If the center display is unavailable, a steering-wheel action may need cluster or audio confirmation. If audio is muted or failed, critical warning semantics require visual/haptic alternatives according to governing requirements. Avoid silent commands when the user cannot verify whether the vehicle accepted them.

## Detection and transition
Fallback begins only when modality loss or restriction is known with sufficient confidence. Show degraded mode when it affects task capability. Preserve partial user input when switching paths, but revalidate command semantics and authority; a parked touch flow should not automatically continue as a complex voice flow after the vehicle starts moving.

## Evidence
Evidence includes modality capability matrix, environmental/degradation triggers, task fallback paths, driver/passenger distinctions, confirmation channels, and failed-modality simulations. Test noisy voice, touch unavailable, display failure/degraded display, hardware-control-only operation, and a driving-state transition during a multimodal task.

## Failure modes
Characteristic Failure includes treating voice as a universal safe substitute, fallback commands with no feedback channel, essential tasks becoming unreachable after one display fails, touch-only recovery from touch failure, passenger-private content read aloud during voice fallback, and degraded mode continuing a task whose demand is no longer appropriate.

## Falsification
Disable each primary modality in turn, combine two failures, add cabin noise, change driving state mid-task, and test privacy-sensitive content with passengers present. The contract fails if an essential task has no safe path or safe state, if a fallback preserves functionality by increasing unacceptable demand, or if confirmation cannot be obtained through an available channel.

## Recovery
Restore the strongest available safe modality, migrate only still-valid task state, and communicate any lost capability. If no adequate modality exists, enter a conservative deferred or safe-state outcome rather than simulating success. When the primary channel returns, reconcile actual vehicle state before restoring the original flow.

## Output and Handoff
Output: `automotive-modality-fallbacks-contract`, containing modality capabilities, task criticality, fallback hierarchy, transition rules, feedback channels, privacy constraints, and evidence. Handoff action availability to driving-state lockouts and driver/passenger role to authority splits.

## Sibling Boundary and delete-the-skill
Sibling vehicle-state-dependent controls own semantic changes in a control; this skill owns continuity when an entire interaction or feedback channel is unavailable. The delete-the-skill test passes because without a modality fallback owner, multimodal automotive systems look redundant in normal operation but fail unpredictably when the primary channel disappears.