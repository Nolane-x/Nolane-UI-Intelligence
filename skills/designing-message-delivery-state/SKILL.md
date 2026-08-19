---
name: designing-message-delivery-state
description: Use when outgoing messages transition through local, queued, sending, server-accepted, failed, and retried states and the UI must preserve message identity without duplicates or false delivery claims.
---

# Designing Message Delivery State

## Parent Contract
**Required parent:** `designing-chat-interfaces`.

This faculty owns the transport-facing lifecycle of an outgoing message. It does not own whether recipients have read the message. “Sent,” “delivered,” and “read” are separate evidence levels and must not be collapsed into one optimistic checkmark.

## Decision Boundary
Give each locally created message a stable client operation ID before network submission. Render optimistic messages only if their provisional state is visible enough to recover from failure. When the server returns canonical identity/time/order, reconcile the existing bubble rather than inserting a duplicate.

Define evidence labels from the service contract: local draft, queued offline, sending, server accepted, delivered to recipient device/service if such evidence truly exists, failed retryable, failed terminal. Avoid presenting “Delivered” when the backend only acknowledges storage. Reordered acknowledgements must update the correct operation, not whichever bubble is currently last.

Retry must preserve message identity and content unless the user edits before resending. If a timeout leaves server outcome unknown, check status or use idempotent submission rather than creating a second message. Offline queue state should be visually distinct from server acceptance so users can choose to cancel before reconnect.

## Failure Topology
- Optimistic send appears final, then vanishes after failure with no recovery path.
- Retry creates a duplicate because the original server acceptance arrived late.
- UI calls server acknowledgement “Delivered” though no recipient-delivery evidence exists.
- Offline queued messages are indistinguishable from sent messages.
- Message timestamps reorder when server time replaces client time and break conversation reading.
- Failure icon is shown but has no accessible explanation or retry affordance.

## Falsification and Recovery
Falsify with offline send, timeout after server commit, out-of-order acknowledgements, reconnect replay, retry, duplicate client events, edited-before-retry content, multiple devices, and service-level delivery evidence unavailable. The design fails if one user intent can become multiple canonical messages or if a status label claims more transport evidence than the system possesses.

Recover by using stable operation/idempotency IDs, reconciling optimistic and canonical records, defining an evidence ladder for status labels, representing queued/unknown states honestly, and making retries status-aware.

## Output Contract
Return `message-delivery-state-contract` with message operation identity, provisional/canonical reconciliation, transport state machine, evidence semantics, offline queue behavior, timeout/unknown handling, retry/idempotency rules, timestamp/order reconciliation, accessibility status, and falsification cases.