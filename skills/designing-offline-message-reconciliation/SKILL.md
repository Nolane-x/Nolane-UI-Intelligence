---
name: designing-offline-message-reconciliation
description: Use when users compose or interact with messages while offline and the client must reconcile local echoes, sends, retries, edits, reactions, and remote events after connectivity returns without duplication or false delivery claims.
---

# Designing Offline Message Reconciliation

Offline messaging is a local transaction log that must later converge with shared conversation history. The UI should preserve user intent without pretending remote acceptance, ordering, or delivery occurred while disconnected.

## Parent Contract
**Required parent:** `designing-realtime-communication-systems`.

The parent owns realtime state planes. This skill owns local pending operations and their reconciliation with server-confirmed events after an offline interval.

## Local Operation Model
Assign stable local transaction identities to sends and other supported operations. Visible states should distinguish queued locally, sending/retrying, server accepted, rejected, and cancelled. A timestamp created on the device can aid orientation but must not be presented as authoritative server ordering.

Edits or reactions to local-unsent messages need dependency ordering. If a user writes message A, edits A, then sends reaction to a remote message while offline, replay should preserve causal dependencies and allow independent operations to succeed/fail separately.

## Reconciliation
On reconnect, fetch missing remote history before or alongside replay according to protocol. Membership or permission may have changed while offline. Revalidate authorization and encryption state before sending queued content. If the room no longer permits posting, preserve the draft/queued content for copy or retry elsewhere without transmitting it.

Deduplicate local echo against remote echo using transaction/event mapping. If the server transformed, rejected, or moderated content, replace the local optimistic representation with authoritative outcome while preserving a visible failure reason.

## Ordering and User Perception
Do not promise strict chronological placement based solely on local clock. When server order differs, transition gently and avoid messages visibly teleporting without explanation if the shift is material. For long offline periods, group reconciliation status so dozens of pending items do not create notification noise.

## Evidence
Test multiple queued sends, offline edit-before-send, deleted target reaction, room removal while offline, key/device change, local clock skew, duplicate reconnect, server timeout after acceptance, and app restart before reconnect. Verify exactly-once user-perceived message identity even when transport retries.

## Failure Modes
- Offline message shows ordinary sent state.
- Retry creates duplicate messages after ambiguous timeout.
- Permission change while offline is ignored.
- Local timestamps dictate canonical order after reconnect.
- Local edit is replayed before its base send exists.
- App restart loses the local queue while UI previously promised it was saved.

## Falsification
Queue several dependent operations, kill/restart the client, change room permissions remotely, then reconnect under clock skew. Falsify if duplicates appear, disallowed content transmits, or the UI cannot distinguish unsent local content from accepted history.

## Recovery
Rebuild queue from durable local transaction records, fetch authoritative membership/history, map local to remote IDs, replay only valid operations, and surface per-item rejection. Unknown acceptance after timeout should resolve by transaction lookup before retry.

## Handoff
Known missing remote ranges route to `designing-message-sync-gap-recovery`; encryption/key changes route to security owners; generic composer UX remains with `designing-message-composers`.

## Output Contract
Return an `offline-message-reconciliation-contract` with `local_operation_states[]`, `transaction_identity`, `dependency_order`, `reconnect_sequence`, `authorization_revalidation`, `echo_deduplication`, `ordering_policy`, `durable_queue_evidence[]`, `falsification_cases[]`, and `recovery_actions[]`.