---
name: designing-realtime-communication-systems
description: Use when a communication product combines rooms or channels, live message synchronization, offline recovery, encryption state, calls, screen sharing, and moderation and must preserve shared state across devices and participants.
---

# Designing Realtime Communication Systems

Realtime communication is a distributed state system presented as conversation. The interface must help users distinguish what is local, what is sent, what is synchronized, what is encrypted, who is present, and which moderation or call state is authoritative when networks and devices disagree.

## Parent Contract
**Required parent:** `designing-collaboration-and-presence`.

Inherit generic collaboration identity and presence. This skill owns communication-system orchestration across membership, message replication, offline periods, encryption, live media sessions, and moderation. It does not replace the existing `designing-chat-interfaces` owner for ordinary composer/thread mechanics.

## Shared State Planes
Separate durable conversation history, ephemeral presence/typing, membership and permissions, device/encryption trust, and live-call state. These planes have different latency and consistency expectations. A participant can be present in a room while message history is still syncing; a message can be locally echoed while not yet accepted by the server; a call can continue while room membership changes.

Model visible state from event identity and causal ordering rather than arrival order alone. Where the protocol supports local echoes, retries, edits, redactions, reactions, and remote echoes, keep one user-perceived message identity across those transitions.

## Connectivity and Recovery
Declare behavior for connected, reconnecting, offline, partially synchronized, and degraded media states. Reconnection should not produce duplicate messages, resurrect redacted content, or reorder history silently. If the client knows a history gap exists, show that bounded uncertainty instead of presenting a seamless complete transcript.

## Trust and Safety
Encryption, device trust, membership authorization, and moderation are distinct. A secure transport badge does not prove every participant is verified; a moderator removing a message does not mean local caches instantly vanish. Surface the guarantee the system actually provides and route specialized decisions to their owners.

## Evidence
Test two accounts on multiple devices across network partition, clock skew, message retry, membership change, key/device change, live call, screen share, moderation action, and reconnect. Capture event IDs and server state alongside rendered UI. A smooth demo on one browser is not sufficient evidence.

## Failure Modes
- Local echo appears permanently sent when the server rejected it.
- Presence is treated as durable membership truth.
- Reconnect duplicates or reorders user-perceived messages.
- Encryption badge implies identity verification that never occurred.
- A call participant remains actionable after losing room permission.
- History gaps are hidden as if synchronization were complete.

## Falsification
Partition one device, send/edit/redact messages elsewhere, change membership, then reconnect. Falsify if the recovering client cannot converge without duplicate or stale-visible state, or if it claims complete history while a known gap remains.

## Recovery
Reconcile by stable event identity, expose bounded sync state, revalidate membership and device trust before consequential actions, and separate durable history from ephemeral presence. Unknown remote state remains visible as syncing/unknown until authoritative evidence arrives.

## Handoff
Membership routes to `designing-room-channel-membership`; gaps and offline state to sync specialists; encryption to encryption/key verification owners; calls/screenshare/moderation to their specialist owners. Generic message composition remains outside this owner.

## Output Contract
Return a `realtime-communication-systems-contract` with `state_planes[]`, `event_identity_model`, `consistency_expectations`, `connectivity_states[]`, `reconciliation_policy`, `trust_boundaries`, `live_media_links`, `moderation_links`, `evidence_cases[]`, `falsification_cases[]`, and `recovery_actions[]`.