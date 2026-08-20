---
name: designing-3d-annotation-and-markup
description: Own model-attached 3D notes, callouts, dimensions, issue pins, sketches, viewpoints, and review markup with stable references, visibility scope, authorship, and broken-reference handling.
---
# Designing 3D Annotation and Markup

## Decision ownership

Own review/communication annotations bound to 3D geometry or viewpoints. Decide annotation types, anchor/reference identity, screen/world orientation, visibility, author/status, viewpoint capture, issue linkage, replies, and what happens when referenced geometry changes. This owner differs from parametric dimensions because markup communicates rather than drives geometry.

## Inputs and evidence

Require model entity IDs, topology-reference stability, annotation types, collaboration/review workflow, camera/view state, layer/visibility, permissions, status lifecycle, export formats, and version history. Identify face/edge references likely to break after topology edits.

## Procedure

Anchor annotations to stable semantic entities when possible; if a face/edge reference is fragile, record geometric context and expose broken/stale state rather than silently retargeting. Pins/callouts should remain discoverable from both model and issue list. Capture optional viewpoint/section state so reviewers can reproduce context. Visibility filters by author/status/type must never make unresolved critical issues disappear without an active-filter cue. Replies/status changes keep attribution. Freehand markup may be view-specific and should say so. Export should preserve author, status, reference, and view when the target format supports it.

## Failure topology

Failures include annotations floating after geometry edits, a pin silently attaching to a different face, issue filters hiding unresolved blockers, view-specific scribbles appearing meaningful from another angle, comments detached from model version, and export flattening markup with no authorship. Another failure is annotation clutter making geometry impossible to inspect.

## Falsification

Reject if broken references can silently retarget; if an annotation cannot reveal author/status/model version; if opening a viewpoint cannot restore sufficient context; if active filters can hide unresolved items without disclosure; if freehand markup scope is ambiguous; or if issue list and viewport disagree on annotation identity.

## Output contract

Return a `3d-annotation-and-markup-contract` with: annotation taxonomy; anchor identity; fragile-reference handling; author/status; viewpoint/section capture; visibility/filtering; replies; version binding; clutter/aggregation; export metadata; and broken-reference recovery. Include one topology-change broken-pin case.

## Handoffs

Review feedback/comment systems provide discussion mechanics, camera views capture context, dimensional measurement supplies numeric references, and graph/history skills support version comparison.