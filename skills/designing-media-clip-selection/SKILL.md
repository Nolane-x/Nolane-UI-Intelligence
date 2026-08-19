---
name: designing-media-clip-selection
description: Use when users select an in/out time range from media for sharing, export, annotation, highlights, or downstream editing and the interface must preserve range semantics and preview accuracy.
---

# Designing Media Clip Selection

## Parent Contract
**Required parent:** `designing-media-playback-experiences`.

This faculty owns temporal range selection, not ordinary single-position seeking. It defines start/end handles, minimum/maximum duration, frame/keyframe precision, playback preview, and what exported/shared range semantics mean.

## Decision Boundary
Maintain three temporal concepts: current playhead, clip start, and clip end. Users should be able to adjust boundaries without confusing the playhead with a handle. Decide whether handles snap to frames, keyframes, chapters, words, or coarse seconds according to media type and output capability. If backend export can only cut at keyframes, do not present frame-perfect handles unless the system will re-encode accurately.

Preview should make the selected range obvious and offer a way to play just the clip. Define inclusive/exclusive endpoint semantics so displayed duration matches export. For live/DVR content, selected range may expire; warn before boundaries fall outside the available window. Keyboard and screen-reader users need independent start/end adjustment with understandable time values.

## Failure Topology
- Dragging the start handle moves the playhead and loses the previous preview position unpredictably.
- UI shows frame-level precision but exported clip starts seconds earlier due to keyframe constraints.
- Start can move after end and silently swaps handles without explanation.
- Duration label disagrees with exported media because endpoint rules differ.
- Touch handles overlap and cannot be selected independently on short clips.
- A live-window clip becomes invalid while the user is naming/exporting it.

## Falsification and Recovery
Test short/long ranges, minimum boundary, crossing handles, keyboard adjustment, touch overlap, preview loop, exact export comparison, codec/keyframe constraints, and live-window expiry. The design fails if the selected visual range cannot predict the produced clip.

Recover by aligning UI precision with output precision, keeping start/end/playhead separate, constraining invalid ranges visibly, providing zoom/coarse-fine adjustment for close handles, and surfacing expiry before output. Verify the actual rendered/exported artifact.

## Output Contract
Return `media-clip-selection-contract` with temporal range model, handle interaction, precision/snap authority, duration/end semantics, preview behavior, validity constraints, live-window rules, and output-fidelity verification cases.
