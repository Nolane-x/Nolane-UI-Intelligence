---
name: designing-proxy-media-workflows
description: Use when this specialist's decision ownership is materially in scope. Own creation, attachment, selection, regeneration, quality indication, and export safeguards for lower-cost proxy media linked to high-resolution source.
---
# Designing Proxy Media Workflows

## Parent Contract

**Required parent:** `designing-nonlinear-media-editors`.

Inherit the broader routing and decision boundary from this canonical parent; this specialist remains accountable only for the narrower ownership, failure topology, falsification criteria, and output contract defined below.

## Decision ownership

Own performance-oriented derivative media used during editing. Decide proxy preset, generation state, source linkage, attachment verification, toggle/automatic use, quality indicator, stale proxy detection, regeneration, missing proxy, and final-export source policy. This owner ensures proxies accelerate editing without confusing editorial source truth.

## Inputs and evidence

Require source media identity, proxy codec/resolution/frame rate/audio, generation jobs, checksums/timecode, link metadata, storage location, playback performance, export pipeline, color transforms, and multicamera needs. Identify proxies that differ in color/metadata enough to affect review.

## Procedure

Create proxies as explicit derivatives of immutable source identity. Generation shows queued/progress/failed/ready per clip. Attachment verifies duration/timecode/frame-rate compatibility. When proxy playback is active, provide a recoverable quality/source indicator without obstructing editing. Automatic switching based on performance must not change timeline semantics. If source changes/relinks, detect stale proxy and require regeneration or validated reattachment. Final render/export defaults to source or defined high-quality media and blocks/warns if only proxy exists when target quality requires source.

## Failure topology

Failures include exporting proxy resolution accidentally, wrong proxy attached to a clip, stale proxy after source replacement, color mismatch mistaken for source grade, automatic proxy use hidden, and missing proxies reported as missing source. Another failure is bulk generation with no storage-cost or failure visibility.

## Falsification

Reject if proxy cannot trace to source; if active proxy use is unknowable; if compatibility is not verified; if final high-quality export can silently use proxy contrary to policy; if source relink fails to invalidate stale proxy; or if proxy failure makes source appear offline.

## Output contract

Return a `proxy-media-workflows-contract` with: source/proxy identity; preset; generation lifecycle; compatibility checks; storage; active-use indicator; automatic-switch policy; stale detection; relink/regeneration; quality/color caveats; and final-export source rule. Include one stale-proxy after relink scenario.

## Handoffs

Ingest creates source, relink manages source recovery, playback/render uses selected media tier, and background-task/file storage owners manage generation/storage progress.