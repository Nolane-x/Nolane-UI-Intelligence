---
name: designing-keyframe-animation-editing
description: Own time-varying parameter authoring through keyframes, interpolation, curves, tangents, temporal/value snapping, selection, copy/paste, retiming, and property-to-timeline linkage.
---
# Designing Keyframe Animation Editing

## Decision ownership

Own authoring of parameter changes over time. Decide keyframe identity, property channels, value/time, interpolation, bezier/tangent controls, curve versus dope-sheet views, selection, copy/paste, retiming, snapping, and distinction between current value and animated value. This owner applies to media-effect/property animation, not generic UI motion.

## Inputs and evidence

Require animatable properties/units, sequence timebase, interpolation types, curve representation, property ranges, expression/modifier support, clip/local versus sequence/global time, nested sequence behavior, and undo. Identify properties where linear interpolation is invalid or clamped.

## Procedure

Show whether a property is static, animated, or driven elsewhere. Adding a keyframe captures property value at an explicit time basis. Keyframe markers in inspector and timeline/curve editor must synchronize selection. Interpolation type needs readable semantics and tangent handles that reveal weighted/broken/unified state where supported. Moving keys shows time/value deltas and collision behavior. Copy/paste states whether times are absolute, relative to playhead, or normalized. Retiming a clip should define whether contained keyframes stretch, stay source-relative, or stay sequence-relative.

## Failure topology

Failures include editing a property value and accidentally creating/removing a keyframe, clip-local versus sequence time confusion, hidden interpolation causing overshoot, duplicate keys at same time, retiming leaving animation desynchronized, and curve values using unlabeled units. Another failure is a keyframe icon that changes color but gives no textual static/animated state.

## Falsification

Reject if users cannot know whether a property is animated; if keyframe time basis is ambiguous; if timeline and curve selections disagree; if interpolation/tangent state cannot be inspected; if paste/retime semantics are hidden; if duplicate-time keys produce undefined result; or if value units/ranges are missing.

## Output contract

Return a `keyframe-animation-editing-contract` with: property/channel identity; static/animated state; time basis; keyframe value/unit; interpolation/tangents; timeline/curve synchronization; move/collision; snapping; copy/paste; retiming behavior; and nested-sequence rules. Include one clip-retime animation scenario.

## Handoffs

Timeline snapping supplies time targets, audio automation handles specialized audio envelopes, color grading may animate grading parameters, and generic numeric editors provide value entry.