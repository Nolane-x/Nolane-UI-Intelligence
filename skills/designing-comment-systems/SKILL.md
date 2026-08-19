---
name: designing-comment-systems
description: Use when users discuss an artifact, record, document, or work item through persistent comments and the interface must coordinate identity, ordering, resolution, editing, deletion, permissions, and object context.
---

# Designing Comment Systems

## Parent Contract
**Required parent:** `designing-collaboration-and-presence`.

This faculty owns persistent commentary attached to a collaborative object. It does not own free-form chat chronology or formal approval decisions. Comments should remain anchored to the artifact/work item they discuss and preserve enough authorship/history to support durable collaboration.

## Decision Boundary
Define comment scope: whole object, section, version, field, selected text, or other anchor. Whole-object comments form a discussion stream; anchored annotations require the annotation specialist. Establish ordering—chronological, threaded, or resolved/open groups—and whether replies form bounded threads.

Editing and deletion need provenance. A user may edit their comment, but products with accountability needs can show an edited marker or retain audit evidence outside the visible UI. Deletion can remove content, leave a tombstone, or be restricted after replies; choose according to domain and policy rather than treating comments as ephemeral text.

Resolution is not deletion. A resolved comment records that a discussion or requested change is considered closed and should be reopenable when work changes. Permission changes must affect compose/edit/delete controls immediately. Mentions and notifications delegate to their dedicated owners but keep comment identity for deep linking.

## Failure Topology
- Resolving a comment hides it permanently and destroys review history.
- Editing silently changes a comment others already acted on with no “edited” evidence where accountability matters.
- Deleted parent removes replies that still contain useful decisions.
- Comment composer remains enabled after the user loses edit/comment permission.
- Deep links open the document but not the referenced comment location.
- Sorting by newest-first makes reply chronology visually ambiguous.

## Falsification and Recovery
Falsify with comment edit after replies, deletion of a parent, permission revocation, resolution/reopen, hundreds of resolved comments, object/version change, deep links, keyboard/screen-reader navigation, and mention notification opening the exact comment. The design fails if comment identity/history cannot survive routine collaboration changes or if “resolved” is indistinguishable from “gone.”

Recover by using stable comment IDs, explicit open/resolved state, bounded edit/delete policy, tombstones where reply context requires them, current-permission enforcement, deep-linkable anchors, and separate audit retention where the domain requires accountability.

## Output Contract
Return `comment-system-contract` with scope/anchor class, ordering/thread model, comment identity, compose/edit/delete authority, edited/tombstone policy, resolution/reopen lifecycle, deep-link behavior, permission updates, notification/mention handoffs, accessibility semantics, and falsification cases.