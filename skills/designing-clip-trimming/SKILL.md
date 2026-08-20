---
name: designing-clip-trimming
description: Use when this specialist's decision ownership is materially in scope. Own simple clip in/out trimming with source-handle limits, frame/sample precision, linked media, preview, slip prevention, snapping, and source-preserving semantics.
---
# Designing Clip Trimming

## Parent Contract

**Required parent:** `designing-nonlinear-media-editors`.

Inherit the broader routing and decision boundary from this canonical parent; this specialist remains accountable only for the narrower ownership, failure topology, falsification criteria, and output contract defined below.

## Decision ownership

Own adjustment of a clip's timeline start/end while keeping its content anchored according to basic trim semantics. Decide edge handles, source available handles, frame/sample precision, preview, linked audio/video behavior, snapping, numeric trim, and limit feedback. Advanced ripple/roll/slip/slide semantics are delegated separately.

## Inputs and evidence

Require clip source in/out, timeline in/out, timebase, source duration, linked media, speed changes, transitions, snapping, handles, and undo model. Identify audio sample precision versus video frame precision and source clips with insufficient handles.

## Procedure

Highlight the exact clip edge and show proposed timecode/delta during drag. Prevent dragging beyond available source or sequence limits and communicate the limiting cause. Provide edit preview near the boundary where frame-level content matters. Linked media should trim together by default only under explicit link semantics, with modifier/unlink path. Snapping targets should be visible and not steal trim unexpectedly. Numeric entry must state whether value is new duration, edge timecode, or delta. Trimming a clip under a transition should expose handle consequences before the transition breaks.

## Failure topology

Failures include dragging the wrong edge, hidden source-handle limit, linked audio remaining untrimmed unexpectedly, transition disappearing because handles ran out, numeric field interpreted in wrong unit, and trim preview showing stale frame. Another failure is pointer precision too small at low timeline zoom with no zoom-to-edit assistance.

## Falsification

Reject if active edge cannot be identified; if proposed source/timeline time is hidden; if trim can exceed source handles silently; if linked-media scope is ambiguous; if transition impact is discovered only after commit; or if basic trim accidentally changes internal source content position as a slip.

## Output contract

Return a `clip-trimming-contract` with: selected edge; source/timeline in-out; handle limits; time precision; preview; linked-media behavior; snapping; numeric-entry semantics; transition interaction; low-zoom assistance; and undo boundary. Include one insufficient-handle transition case.

## Handoffs

Advanced trim semantics owns ripple/roll/slip/slide, snapping supplies temporal targets, timeline supplies hit geometry, and playback preview verifies boundary content.