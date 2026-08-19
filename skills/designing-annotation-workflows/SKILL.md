---
name: designing-annotation-workflows
description: Use when feedback must attach to a precise region, text range, frame, timestamp, coordinate, or structured field and remain recoverable as the underlying artifact changes.
---

# Designing Annotation Workflows

## Parent Contract
**Required parent:** `designing-comment-systems`.

This faculty owns spatial or semantic anchoring of collaborative feedback. A comment says something about an artifact; an annotation additionally answers exactly *where* in that artifact the statement applies. It does not own free-form discussion, version diffing, or review approval state.

## Decision Boundary
Choose an anchor representation that survives realistic edits. Pixel coordinates are acceptable for immutable images but fragile for responsive documents. Text annotations may need range identity plus surrounding context; video annotations may bind to timecode and region; design-canvas notes may bind to object IDs and local coordinates. The visible marker is only a projection of that canonical anchor.

Define what happens when the target moves, is edited, split, deleted, or replaced by a new version. An annotation can remain attached, become approximately relocated, be marked orphaned, or be intentionally migrated to a newer version. Silent reattachment to the wrong target is worse than an explicit orphan state because it changes the meaning of the feedback.

Creation should preserve the user's selected target while the composer opens. Marker density needs aggregation or filtering when many annotations overlap, but aggregation must not erase unresolved severity, author, or thread count. Resolved annotations can recede visually while remaining discoverable for audit and context.

## Failure Topology
- A text annotation stores DOM offsets and jumps to unrelated text after an edit.
- Image marker position is saved in viewport pixels and shifts after responsive resizing.
- Deleting an anchored object silently deletes the discussion with it.
- Hundreds of pins obscure the artifact and make the underlying work impossible to inspect.
- Opening a marker changes the current selection, so subsequent annotation attaches to the wrong target.
- Version change reuses the old coordinate on a materially different artifact and implies false continuity.

## Falsification and Recovery
Falsify with text inserted before an anchor, selected text deleted, canvas object renamed/moved, responsive image resizing, video trim, version replacement, overlapping notes, permission loss, keyboard-only marker traversal, and screen-reader navigation between annotations and targets. The design fails if a surviving annotation can no longer prove what it refers to or if an orphan is silently treated as a valid attachment.

Recover by using artifact-native stable IDs where available, supplementing fragile ranges with context fingerprints, storing canonical rather than viewport coordinates, declaring orphan/migration states, separating marker clustering from annotation identity, and preserving discussion independently of target deletion.

## Output Contract
Return `annotation-workflow-contract` with anchor types, canonical identity, creation/selection behavior, relocation strategy, orphan/version semantics, marker density rules, resolution visibility, permission behavior, accessible target-navigation model, and falsification cases.