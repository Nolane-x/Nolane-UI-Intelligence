---
name: designing-nonlinear-media-editors
description: Use when this specialist's decision ownership is materially in scope. Own the interaction architecture for nonlinear audio/video editing where source media, timeline state, tracks, edits, effects, review, proxies, and export must remain coherent and reversible.
---
# Designing Nonlinear Media Editors

## Parent Contract

**Required parent:** `designing-editor-canvas-workspaces`.

Inherit the broader routing and decision boundary from this canonical parent; this specialist remains accountable only for the narrower ownership, failure topology, falsification criteria, and output contract defined below.

## Decision ownership

Own the top-level authoring contract for timeline-based media editing. Decide how source media, bins, timelines/sequences, playhead, tracks/layers, selection, edit modes, effects/automation, review markers, offline media, proxies, history, and export relate. This owner explicitly differs from playback: the central question is how edits transform authored sequence state without destroying source media or user intent.

## Inputs and evidence

Require media types/codecs, sequence model, timebase/frame rate, track types, source/record paradigms, editing operations, proxy/offline behavior, effects, audio/video sync, collaboration/review, hardware/performance constraints, and export targets. Inspect long projects with hundreds of clips, nested sequences, missing media, mixed frame rates, and multi-channel audio—not only a short social clip.

## Procedure

Establish immutable or source-preserving media identity and a separate sequence/timeline representation. Make current sequence, playhead timecode, selection, active tracks, edit mode, snapping, and trim context continuously recoverable. Edits should affect sequence references unless a destructive source operation is explicitly invoked. Track targeting/patching must be clear before insert/overwrite-style operations. Provide a coherent history transaction model for compound edits. Offline/proxy state cannot masquerade as source quality. Review markers/comments must bind to stable timeline/media positions under edit semantics. Export should consume the actual sequence state and render dependencies, not a stale playback preview.

## Failure topology

Failures include source files accidentally altered, clip versus timeline selection ambiguity, hidden track targeting causing media to land on the wrong tracks, mixed frame-rate timecode errors, proxies mistaken for final-resolution source, ripple edits shifting unrelated content, and nested sequence changes appearing unexplained. Another failure is a gorgeous timeline that cannot explain why output differs from what the editor previewed.

## Falsification

Reject if users cannot identify current sequence/edit mode/target tracks before a consequential edit; if source and sequence edits are conflated; if offline/proxy state can look fully online; if undo cannot restore a compound edit coherently; if timebase is hidden when timecode/frame precision matters; or if export can render a materially different state than the currently committed sequence without warning.

## Output contract

Return a `nonlinear-media-editors-contract` containing: source-versus-sequence identity; sequence/timebase; playhead/selection/edit modes; track targeting; source preservation; history transaction rules; proxy/offline state; nested media behavior; review marker identity; preview-versus-export consistency; and performance/degraded modes. Include one mixed-frame-rate and one offline-source scenario.

## Handoffs

Delegate ingest/bins, timelines, tracks, trimming, razor, advanced trim semantics, snapping, transitions, keyframes, multicamera, audio mixing/automation, grading/scopes, subtitles, relink, proxies, markers, and render queues to dedicated owners. Batch 003 playback skills remain viewing/monitoring dependencies only.