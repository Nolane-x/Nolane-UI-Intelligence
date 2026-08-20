---
name: designing-ray-pointer-interaction
description: Use when XR interfaces use controller, hand, head, or other projected rays to target distant spatial UI and must manage hit testing, target priority, depth, occlusion, hover, commit, and loss of tracking without duplicating gaze-hand input ownership.
---

# Designing Ray Pointer Interaction

A ray pointer converts orientation into distant targeting. Its failure modes are geometric and stateful: the ray can intersect the wrong surface, pass through occluders, jitter across adjacent targets, or remain visually active after tracking confidence drops.

## Parent Contract
**Required parent:** `designing-spatial-xr-interfaces`.

The parent owns spatial XR composition. Existing `designing-gaze-hand-spatial-input` owns gaze/hand intent arbitration broadly. This skill narrows to projected-ray targeting mechanics for distant UI, especially hit testing, visual feedback, and commit stability.

## Decision ownership

This skill owns the decision boundary from ray-source confidence to a committed distant target: which intersections are eligible, how depth and interaction layers establish priority, how much stabilization or angular tolerance is allowed, when press captures a target, and when tracking or occlusion must cancel rather than guess. General gaze/hand intent arbitration remains with its broader owner; this skill is accountable for making projected-ray acquisition and commit deterministic enough that the same scene geometry cannot silently select a different object as tracking noise changes.

## Ray State Model
Separate source tracking, ray availability, candidate intersection, hover/aim state, press/commit state, drag/capture state, and cancelled/lost tracking. A visible line is not evidence that a valid target exists. Hide or downgrade the ray when tracking is too uncertain to support precise interaction.

Define origin and direction for each input source. Controller rays may originate from a grip/aim pose; hand rays may use a synthesized pose; head rays need stronger commit separation because orientation follows looking. Do not mix these origins invisibly across devices.

## Hit Testing and Priority
Resolve intersections in spatial order while honoring interaction layers. A nearer decorative mesh should not unexpectedly steal input from an intended panel if it is non-interactive; conversely, an occluding physical surface should block a distant control when the scene semantics require it. Define whether transparent or passthrough surfaces participate in hit tests.

Targets need angular size and depth-aware tolerance. Excessive magnetism can activate the wrong adjacent control; no tolerance can make distant targeting unusable. Keep hover stabilization bounded and disclose target capture through visual feedback.

## Commit and Drag
Separate aim from commit. During press/drag, capture the intended target so small wrist motion does not retarget midway unless the interaction explicitly supports transfer. On release, apply cancellation rules based on gesture semantics rather than firing whichever object the ray currently intersects.

## Evidence
Test near-overlapping surfaces, transparent layers, moving targets, small distant controls, tremor/noise, tracking dropout, controller recenter, drag across depth, and two rays/hands. Verify the selected object identity against scene hit-test logs.

## Failure Modes
- Decorative geometry intercepts the ray invisibly.
- Hover jumps rapidly between adjacent depth layers.
- Tracking loss leaves a frozen ray implying control.
- Press begins on one target and releases action on another unintentionally.
- Large hidden hit volumes make the wrong target feel “sticky.”
- Ray remains active through an occluder that should block interaction.

## Falsification
Place two interactive panels close in angle but different in depth behind an occluding object, then add tracking noise. Falsify if the wrong panel receives commit, if the UI cannot explain target priority, or if tracking loss still produces activation.

## Recovery
Recompute hit layers, shrink or reshape interaction volumes, add bounded stabilization, capture target through commit, and cancel on confidence loss. If scene semantics cannot determine whether an occluder should block input, mark the interaction rule unresolved instead of choosing by render order.

## Handoff
Near/far mode switching routes to `designing-xr-near-far-interaction-transitions`; panel geometry to `designing-world-space-panel-placement`; generic gaze/hand confirmation remains with `designing-gaze-hand-spatial-input`.

## Output Contract
Return a `ray-pointer-interaction-contract` with `ray_sources[]`, `tracking_states`, `hit_test_layers`, `target_priority`, `angular_tolerance`, `hover_stabilization`, `commit_capture_rules`, `occlusion_policy`, `evidence_cases[]`, `falsification_cases[]`, and `recovery_actions[]`.