---
name: designing-track-and-layer-management
description: Use when this specialist's decision ownership is materially in scope. Own video/audio/subtitle/data track organization, targeting, patching, mute/solo/lock, hierarchy, role, ordering, visibility, routing, and safe bulk track operations.
---
# Designing Track and Layer Management

## Parent Contract

**Required parent:** `designing-nonlinear-media-editors`.

Inherit the broader routing and decision boundary from this canonical parent; this specialist remains accountable only for the narrower ownership, failure topology, falsification criteria, and output contract defined below.

## Decision ownership

Own persistent track/layer semantics in a media timeline. Decide track type, order, name/role, visibility/mute/solo, lock, record/target/patch state, audio routing links, subtitle/data distinction, creation/deletion, and multi-track selection. This owner prevents header toggles from becoming an unexplained wall of icons.

## Inputs and evidence

Require track types, compositing order, audio routing, source patching model, target-track behavior, subtitle support, effect tracks/buses if present, maximum track counts, shortcut conventions, and deletion consequences. Identify products where audio/video track order has different semantic direction.

## Procedure

Give each track clear type, name, index/role, and independent state. Separate visibility from lock and playback mute from editorial targeting. When source patch/record targeting matters, show source-to-destination mapping and warn if an edit will omit a source channel. Solo semantics need additive/exclusive behavior and a visible global "some tracks soloed" state. Track deletion previews affected clips/effects and whether media is removed from sequence only. Reordering must make compositing/routing consequence clear. Large projects require compact grouping/folders while preserving critical active states.

## Failure topology

Failures include wrong track targeted for insert, mute mistaken for disabled edit, hidden locks causing failed edits, solo state making output silent with no global cue, deleting a track silently deleting content, and track order reversed between audio/video expectations without explanation. Another failure is source channel patching hidden until after audio channels are lost from an edit.

## Falsification

Reject if target/mute/lock/visibility states are visually confusable; if an insert can discard source channels without pre-edit cue; if track deletion lacks content-count consequence; if global playback is changed by hidden solo state; if reordering consequence is unclear; or if collapsed track groups conceal active/locked/solo states.

## Output contract

Return a `track-and-layer-management-contract` with: track taxonomy/order; name/role; visibility/mute/solo/lock; target/patch semantics; source mapping; grouping; creation/deletion; reorder consequences; audio routing links; subtitle/data handling; and compact-state indicators. Include one missing-source-channel patch case.

## Handoffs

Audio mixing owns gain/pan/bus behavior, timeline/edit operations consume targeting, subtitles own caption content, and generic list reordering supplies mechanics only.