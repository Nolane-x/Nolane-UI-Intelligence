---
name: designing-editing-timelines
description: Use when this specialist's decision ownership is materially in scope. Own timeline navigation and sequence representation across playhead, time ruler, zoom, selections, edit points, clip boundaries, gaps, linked media, and long-project orientation.
---
# Designing Editing Timelines

## Parent Contract

**Required parent:** `designing-nonlinear-media-editors`.

Inherit the broader routing and decision boundary from this canonical parent; this specialist remains accountable only for the narrower ownership, failure topology, falsification criteria, and output contract defined below.

## Decision ownership

Own the timeline as the primary spatial-temporal authoring surface. Decide time ruler/timecode, playhead, clip geometry, gaps, edit-point selection, clip selection, range selection, zoom/scroll, track header alignment, nested sequence cues, linked audio/video representation, and long-timeline overview. This owner does not define each edit operation.

## Inputs and evidence

Require sequence timebase/frame rate, duration range, track count/types, clip model, linked items, nested sequences, transition/effect indicators, markers, waveform/thumbnail availability, input mappings, and performance limits. Test both frame-level precision and hour-long navigation.

## Procedure

Keep timebase and playhead time recoverable. Timeline zoom should preserve the user's temporal anchor—typically playhead or pointer—not jump unpredictably. Distinguish clip body, edge/edit point, gap, range, and playhead interactions through hit areas and feedback. Track headers remain aligned during vertical scroll. Linked audio/video should show relationship without making independent edits impossible. At low zoom, simplify thumbnails/waveforms before losing clip boundaries and important markers. Provide fit-sequence, fit-selection, and return-to-playhead commands. Virtualization must preserve selection and edit-point identity.

## Failure topology

Failures include selecting a clip when the user intended an edit point, zoom moving the target away, playhead hidden after horizontal navigation, track headers desynchronized, tiny gaps invisible, linked clips moving unexpectedly, and nested sequences indistinguishable from source clips. Another failure is high-density thumbnails consuming performance while essential frame precision lags.

## Falsification

Reject if clip/edit-point/gap hit targets are ambiguous at supported zoom; if zoom cannot preserve a meaningful anchor; if playhead time is unknowable; if track headers drift from content; if hidden micro-gaps can change output with no cue; or if virtualization loses active selection/trim state.

## Output contract

Return an `editing-timelines-contract` with: ruler/timebase; playhead; temporal anchoring; selection entities; clip/gap/edit-point geometry; zoom/scroll; track-header sync; linked-media cues; nested sequence representation; low/high zoom detail policy; navigation commands; and virtualization identity. Include one hour-long and one frame-precision scenario.

## Handoffs

Track management owns track state, trimming/razor/advanced edit owners consume edit points, snapping governs temporal alignment, markers provide annotations, and playback controls monitor the committed sequence.