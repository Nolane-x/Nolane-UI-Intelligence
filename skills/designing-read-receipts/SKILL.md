---
name: designing-read-receipts
description: Use when a messaging product exposes seen/read evidence and must define what counts as read, whose state is visible, privacy preferences, group aggregation, and uncertainty without coercive false precision.
---

# Designing Read Receipts

## Parent Contract
**Required parent:** `designing-chat-interfaces`.

This faculty owns recipient-consumption evidence after message delivery. It does not infer comprehension, agreement, or response obligation from a read event. The product must treat read state as a bounded observation whose collection and disclosure may be disabled or unavailable.

## Decision Boundary
Define the read event from observable behavior: message crossed a visibility threshold while conversation was active, user explicitly marked read, or service received another defined signal. Merely opening a route is often insufficient when unread messages remain below the viewport. Likewise, background prefetch must never mark content read.

In groups, individual avatars can become noise and privacy leakage. Decide whether to show aggregate counts, a details popover, “seen by all,” or no per-person state above a participant threshold. If read receipts are optional, explain reciprocal or asymmetric consequences according to product policy; do not secretly keep displaying others’ status after a user disables their own if the policy promises reciprocity.

Read evidence can arrive late or never arrive. Never substitute delivery with read. If participants leave, block, or lose access, preserve historical semantics only to the extent allowed by privacy policy.

## Failure Topology
- Conversation opening marks hundreds of below-fold messages read.
- Read state is collected from a background tab with no actual viewing.
- Group chat displays a wall of avatars that obscures message content.
- Disabling read receipts changes nothing in disclosure behavior.
- “Read” is used by workflow logic as proof the user understood a critical instruction.
- Delayed receipt arrives after a message is deleted and creates a confusing orphan state.

## Falsification and Recovery
Falsify with conversation opened at top while unread messages are below, background tab, multiple devices, receipt disabled, large groups, blocked participant, message deletion, screen reader navigation, and delayed/out-of-order receipt events. The design fails if read status can be generated without a defined consumption signal or if it claims knowledge of understanding rather than observed state.

Recover by grounding read transitions in explicit visibility/user signals, honoring privacy settings, separating delivery/read semantics, aggregating large-group evidence, and keeping workflow obligations independent of read receipts.

## Output Contract
Return `read-receipt-contract` with qualifying read signal, viewport/activity requirements, multi-device reconciliation, privacy preference semantics, group aggregation thresholds, delivery separation, delayed/deleted-message handling, disclosure limits, accessibility presentation, and falsification cases.