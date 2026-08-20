---
name: designing-split-and-razor-editing
description: Use when this specialist's decision ownership is materially in scope. Own cutting media references at a time position across selected or targeted tracks, linked clips, grouped items, effects, markers, and protected tracks with clear scope and reversibility.
---
# Designing Split and Razor Editing

## Parent Contract

**Required parent:** `designing-nonlinear-media-editors`.

Inherit the broader routing and decision boundary from this canonical parent; this specialist remains accountable only for the narrower ownership, failure topology, falsification criteria, and output contract defined below.

## Decision ownership

Own creation of edit boundaries by splitting clips. Decide cut position, affected tracks/clips, playhead versus pointer basis, linked/grouped behavior, locked/protected exclusion, whether effects/keyframes are duplicated or partitioned, and how the new segments inherit identity. This is not destructive source cutting.

## Inputs and evidence

Require timebase, selected/target tracks, clip/link/group model, locks, transitions/effects/keyframes, marker relationships, nested clips, and history. Identify split-all-tracks versus split-selected workflows and audio sample versus video frame precision.

## Procedure

Before commit, show cut position and all affected clip intersections. A single-clip split uses explicit selection; split-all/targeted commands reveal which unlocked tracks participate. Linked/grouped items follow defined policy with temporary override. Track locks must block with visible reason. New segments retain source provenance and appropriate clip metadata while receiving distinct sequence identity. Effects/keyframes at the boundary need deterministic inheritance. Cutting through transitions should be blocked or explain resulting topology rather than silently corrupting the edit.

## Failure topology

Failures include razor cutting hidden tracks, linked audio left unsplit, locked track silently skipped but user believes all tracks split, duplicate keyframes/effects causing changed output, source media modified, and repeated click at same frame generating zero-length segments. Another failure is cutting a nested sequence while users think they are entering it.

## Falsification

Reject if affected track/clip scope is unknowable; if a lock skip is silent; if split changes source bytes; if linked behavior is inconsistent; if effect/keyframe inheritance cannot be predicted; if zero-length duplicate cuts are allowed; or if nested-sequence scope is ambiguous.

## Output contract

Return a `split-and-razor-editing-contract` with: cut position/basis; affected track/clip rule; lock handling; link/group policy; source preservation; new segment identity; metadata/effect/keyframe inheritance; transition/nested-sequence behavior; duplicate-cut guard; and undo. Include one split-targeted-tracks scenario.

## Handoffs

Track management supplies targets/locks, timeline supplies cut position, advanced trim handles subsequent gap/edge changes, and history preserves the split transaction.