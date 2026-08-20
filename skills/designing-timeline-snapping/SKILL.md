---
name: designing-timeline-snapping
description: Own temporal snapping among playhead, clip edges, markers, beats, keyframes, frames, samples, and guides with priority, tolerance, target feedback, and temporary override.
---
# Designing Timeline Snapping

## Decision ownership

Own precision alignment in media timelines. Decide eligible temporal targets, frame/sample quantization, snap priority, tolerance as zoom changes, target highlighting, magnetic behavior, temporary disable, and conflict among multiple candidates. This differs from 3D or generic snapping because timebase and media semantics determine valid positions.

## Inputs and evidence

Require sequence timebase, audio sample precision, clip edges, playhead, markers, beats/grid, keyframes, edit operations, zoom scale, shortcut conventions, and performance. Identify operations that must remain frame-bound versus those supporting subframe/sample precision.

## Procedure

Expose active snapping globally and provide a quick temporary override. When a dragged edit approaches a target, highlight the exact target and show type/time. Snap tolerance should be screen-space stable but never leap across large temporal distance at low zoom without clear feedback. Define priority/cycling when playhead, marker, and clip edge coincide. Respect operation precision: video edges may frame-snap while audio/keyframes can use finer resolution. Snapping should not change track or edit mode and must release cleanly when modifier is held.

## Failure topology

Failures include snapping to a hidden marker, low zoom causing huge temporal jumps, target feedback lagging behind committed position, audio forced unnecessarily to video frames, multiple coincident targets causing jitter, and temporary disable remaining stuck. Another failure is a magnetic feel with no way to know what was snapped to.

## Falsification

Reject if committed time differs from indicated target; if target type/time cannot be identified; if low-zoom tolerance creates unreasonable jumps; if hidden/disabled target classes still attract edits; if precision rules conflict with media type; or if temporary override state persists beyond the gesture.

## Output contract

Return a `timeline-snapping-contract` with: target taxonomy; precision/timebase; priority/cycling; tolerance versus zoom; target highlight/time label; global state; temporary override; hidden-target policy; coincident-target handling; and commit guarantee. Include one coincident marker/playhead/edge case.

## Handoffs

Trim/split/keyframe operations invoke snapping, timeline supplies temporal geometry, marker owner defines marker semantics, and audio automation may require sample/subframe precision.