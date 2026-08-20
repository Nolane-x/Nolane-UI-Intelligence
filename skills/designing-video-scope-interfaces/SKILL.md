---
name: designing-video-scope-interfaces
description: Use when this specialist's decision ownership is materially in scope. Own waveform, parade, vectorscope, histogram, gamut, and related video measurement scopes with signal context, scale, target overlays, persistence, and correspondence to viewed output.
---
# Designing Video Scope Interfaces

## Parent Contract

**Required parent:** `designing-nonlinear-media-editors`.

Inherit the broader routing and decision boundary from this canonical parent; this specialist remains accountable only for the narrower ownership, failure topology, falsification criteria, and output contract defined below.

## Decision ownership

Own analytical scopes used to measure video signals during grading/editing. Decide scope type, scale/units, luma/chroma/channel mode, graticules/targets, source versus output pipeline point, persistence, zoom, overlays, and synchronization with displayed frame. This is measurement, not decorative data visualization.

## Inputs and evidence

Require frame signal, color space/transfer, processing pipeline, scope algorithms, scale standards, HDR/SDR targets, channel modes, legal/safe ranges if applicable, frame update cadence, and performance. Identify whether scopes see pre-grade, post-grade, or display-referred signal.

## Procedure

Label each scope and its scale/context. The viewer and scope should be synchronized to the same frame and known pipeline stage. Waveform/parade axes must reveal signal levels; vectorscope shows target/graticule semantics; histogram discloses channel/luma mode. HDR workflows need appropriate scale rather than reusing SDR labels. Freeze/compare can be useful but must state when a scope is not live. Scope updates may decimate for performance but should not lag enough to mislead interactive grading.

## Failure topology

Failures include scopes measuring a different pipeline stage than viewer, unlabeled 0-100 values with unknown units, HDR signal clipped into SDR scale, frozen scope appearing live, frame lag during rapid scrubbing, and target graticules used outside their color-space assumptions. Another failure is auto-scaling that makes over-range signal look normal.

## Falsification

Reject if scope pipeline stage cannot be identified; if scale/unit/transfer context is absent; if scope and viewer frame can diverge without cue; if HDR uses inappropriate SDR scale; if frozen state is hidden; or if auto-ranging conceals out-of-range values.

## Output contract

Return a `video-scope-interfaces-contract` with: scope types; pipeline tap point; frame synchronization; scale/units; color context; channel modes; graticules/targets; live/frozen state; update latency; HDR/SDR behavior; and out-of-range representation. Include one mismatched-pipeline scenario.

## Handoffs

Color grading consumes scope evidence, playback/timeline supplies frame position, render/export supplies output color context, and generic data-viz provides rendering mechanics only.