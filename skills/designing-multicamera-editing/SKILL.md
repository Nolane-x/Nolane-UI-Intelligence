---
name: designing-multicamera-editing
description: Use when this specialist's decision ownership is materially in scope. Own synchronized multi-angle editing across source grouping, sync basis, angle naming, live/after-the-fact cuts, audio-follow policy, missing cameras, and preservation of source timing.
---
# Designing Multicamera Editing

## Parent Contract

**Required parent:** `designing-nonlinear-media-editors`.

Inherit the broader routing and decision boundary from this canonical parent; this specialist remains accountable only for the narrower ownership, failure topology, falsification criteria, and output contract defined below.

## Decision ownership

Own editorial switching among synchronized camera/audio sources. Decide multicam group identity, synchronization method, angle grid, naming, active angle, cut creation, trim, audio switching/follow rules, missing/offline angles, and relation between multicam sequence and underlying sources.

## Inputs and evidence

Require source clips, camera/timecode metadata, audio waveforms or sync markers, frame rates, sync algorithm/result confidence, angle names, preferred/master audio, offline state, sequence timebase, and editing shortcuts. Identify drift or incomplete overlap.

## Procedure

Build a multicam group with explicit sync basis—timecode, audio, marker, manual offset—and allow verification/correction before editorial cuts. Angle viewer should preserve camera identity and current availability. Live switching creates sequence edits at playhead with clear active angle; after-the-fact changes should switch an existing segment without altering synchronization. Audio-follow policy must be independent and explicit: switch with video, fixed master audio, or manually selected. Offline/missing angles remain as labeled unavailable slots rather than shifting camera numbers.

## Failure topology

Failures include wrong sync silently accepted, camera numbering changes when a source goes offline, video switch unexpectedly switching audio, angle change shifting clip timing, mixed frame-rate drift, and multicam edits impossible to trace back to source. Another failure is angle grid latency causing the user to cut based on stale frames.

## Falsification

Reject if sync method/confidence cannot be inspected; if unavailable angle renumbers others; if audio-follow behavior is unknown; if switching angle can alter synchronized timing; if source lineage is lost; or if monitoring latency exceeds the defined cut-preview tolerance without a warning.

## Output contract

Return a `multicamera-editing-contract` with: group/source identity; sync method/offset/confidence; angle naming/order; active/offline state; cut/switch semantics; audio-follow policy; mixed-frame-rate treatment; source lineage; monitoring latency; and resync/correction behavior. Include one offline-angle and one master-audio scenario.

## Handoffs

Ingest supplies source metadata, timeline represents resulting cuts, audio mixing handles mix state, relink handles missing cameras, and playback monitoring displays synchronized angles.