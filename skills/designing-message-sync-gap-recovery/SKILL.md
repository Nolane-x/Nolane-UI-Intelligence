---
name: designing-message-sync-gap-recovery
description: Use when a realtime timeline knows that some events are missing or out of range and the interface must represent, fetch, stitch, and verify the gap without presenting incomplete history as complete conversation.
---

# Designing Message Sync Gap Recovery

A synchronization gap is known missing history between two trusted boundaries. Hiding it behind a spinner or seamlessly concatenating uncertain pages can make users believe they have read a complete conversation when they have not.

## Parent Contract
**Required parent:** `designing-realtime-communication-systems`.

The parent owns distributed communication state. This skill owns detection, representation, backfill, stitching, and failure recovery for bounded history gaps.

## Gap Identity
Represent a gap using the protocol's pagination/token/event boundaries where available. Distinguish “older history not yet loaded” from “server says events exist but retrieval failed,” “history unavailable due to retention,” and “history inaccessible due to permission/encryption.” These states demand different copy and recovery.

When backfilling, anchor visible scroll position and existing event identity. Do not jump the user unpredictably or duplicate boundary events. Newly fetched events can include edits, redactions, membership changes, or reactions that alter already-rendered state; apply them causally rather than appending everything as new messages.

## Completeness Semantics
A timeline may have multiple gaps. Make search, unread markers, jump-to-event, and thread references aware of incomplete ranges. If search excludes missing history, say so. If a referenced event is inside an unrecoverable gap, show that boundary rather than inventing “message deleted.”

## Evidence
Create synthetic event ranges with one or more missing intervals, duplicate boundary events, edits/redactions inside the gap, encrypted events with unavailable keys, retention-expired history, and a pagination token failure. Verify reconstructed event sequence against canonical server history.

Test scrolling during backfill, reconnect during recovery, and switching rooms before the fetch completes.

## Failure Modes
- Gap is represented as ordinary loading forever.
- Backfill duplicates boundary messages.
- Scroll jumps and causes users to lose reading position.
- Missing event referenced by a reply is labeled deleted without evidence.
- Search claims no results while an unrecovered gap exists.
- Events inside backfill are appended by arrival time instead of causal timeline order.

## Falsification
Remove a known event range containing one edit and one membership event, then recover it while the user is scrolled at the boundary. Falsify if sequence differs from server history, duplicate events appear, or the UI ever claims the timeline is complete before recovery succeeds.

## Recovery
Persist explicit gap boundaries, retry with fresh pagination authority, merge by stable event identity, and update derived state after backfill. If retention or permissions make recovery impossible, convert the gap into an explicit unavailable range rather than silently closing it.

## Handoff
Whole-device offline reconciliation belongs to `designing-offline-message-reconciliation`; encryption failures inside a gap route to `designing-end-to-end-encryption-state` and key owners.

## Output Contract
Return a `message-sync-gap-recovery-contract` with `gap_states[]`, `boundary_identity`, `backfill_merge_rules`, `scroll_anchor_policy`, `causal_update_rules`, `search_unread_semantics`, `unrecoverable_gap_states[]`, `evidence_cases[]`, `falsification_cases[]`, and `recovery_actions[]`.