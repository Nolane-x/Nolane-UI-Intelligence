---
name: designing-edit-markers-and-review-notes
description: Use when this specialist's decision ownership is materially in scope. Own editorial markers, ranges, review notes, approvals, status, authorship, color/type, attachment, timeline anchoring, and behavior as edits shift sequence time.
---
# Designing Edit Markers and Review Notes

## Parent Contract

**Required parent:** `designing-nonlinear-media-editors`.

Inherit the broader routing and decision boundary from this canonical parent; this specialist remains accountable only for the narrower ownership, failure topology, falsification criteria, and output contract defined below.

## Decision ownership

Own time-bound editorial annotations used for navigation and review. Decide point versus range markers, sequence versus clip/source anchoring, category/color, author, comments/replies, status, assignment, attachments, review-version context, and what happens when timeline edits move content. This owner differs from generic comments because temporal identity is central.

## Inputs and evidence

Require sequence/clip identities, timebase, marker types, review workflow, collaboration, external review imports, edit operations, version history, permissions, and export/share needs. Determine whether notes should follow content or stay at absolute sequence time.

## Procedure

When creating a marker/note, make anchor type explicit: sequence time, clip/source frame, selected range, or asset. Content-following notes should move with the referenced clip under ripple edits; sequence-time notes should not. Show marker category/status/author in a compact timeline lane and richer list. Clicking a note navigates and previews the referenced frame/range. Review comments imported from another cut need version binding and stale/repositioned handling. Resolve/approve changes preserve history; filters disclose hidden unresolved notes.

## Failure topology

Failures include notes drifting to unrelated content after edits, external review timecode applied to wrong version, resolved notes disappearing with no history, filters hiding blockers, duplicate markers after import, and color-only categories. Another failure is an annotation jumping when clip speed/retime changes with no anchor policy.

## Falsification

Reject if anchor type cannot be identified; if timeline edits can move a note contrary to its anchoring semantics without cue; if review version is unknown; if unresolved notes can be hidden without active-filter disclosure; if resolution erases discussion; or if retime behavior is undefined.

## Output contract

Return an `edit-markers-and-review-notes-contract` with: marker/note identity; point/range; anchor type; timecode/source reference; author/category/status; assignment/replies; version binding; edit/retime movement policy; import/dedup; navigation preview; filters; and history. Include one ripple-edit and one stale-review-version scenario.

## Handoffs

Timeline provides temporal geometry, collaboration/comments provide discussion mechanics, version history provides cut identity, and render/export may include or exclude markers under explicit review outputs.