---
name: designing-list-insertion-removal-motion
description: Use when items enter or leave an ordered collection and motion must preserve object identity, reading position and causal understanding without delaying the collection’s authoritative state.
---

# Designing List Insertion and Removal Motion

## Parent Contract
**Required parent:** `designing-motion`.

This faculty owns the temporal treatment of structural membership changes in lists, feeds, queues, tables and repeated cards. It does not decide sorting policy, data retention, undo semantics or whether an item is allowed to be removed.

## Decision Boundary
The core problem is **continuity of identity under structural change**. A new item may be inserted at the user’s action point, at a sorted position, or at a remote-update position. A removed item may disappear immediately from the authoritative model while its former space collapses visually. Motion should help users answer “what changed?” without making stale content look live.

Classify insertion source: direct creation, optimistic creation, server-confirmed creation, remote collaborator update, pagination/prepend, or restored item. The motion should reflect causality, not merely animate every DOM mount. Initial page render is not automatically an insertion event.

For removal, distinguish committed deletion from pending removal and filtering. A filter hiding 200 rows should not play 200 deletion animations. A destructive item can visually exit after commit while its region becomes noninteractive immediately. If undo is offered, the animation may preserve spatial memory but must not imply the item still exists in the active dataset.

Reflow nearby items carefully. Users often track a row or card by position; large cascades can destroy that reference. Preserve scroll anchor when prepending content and avoid shifting the target under the pointer during an action.

## Failure Topology
- Every re-render is mistaken for insertion and the list flickers continuously.
- A deleted row remains clickable during its fade-out.
- Sorting and insertion animations combine so the new item appears to teleport twice.
- Prepending a feed moves the viewport, losing the article being read.
- Bulk filter changes animate hundreds of exits and stall the main thread.
- Optimistic insertion celebrates success before validation later removes the item.

## Falsification and Recovery
Test create-success, create-failure, remote insert, sort-after-insert, delete/undo, bulk filter, prepend while scrolled, virtualized recycling and rapid repeated updates. Track semantic item IDs rather than DOM nodes. If a user cannot identify the changed item or the animation preserves an obsolete interaction target, the design fails.

Recover by reducing motion to the changed object, anchoring the viewport, suppressing transitions for bulk transformations, and binding transitions to lifecycle events instead of mount/unmount accidents.

## Output Contract
Return `list-membership-motion-contract` containing event classes, identity keys, insertion/removal treatment, reflow policy, interaction cutoff, scroll-anchor behavior, optimistic/undo branches, bulk-change suppression and verification fixtures.