---
name: designing-offline-degraded-experiences
description: Use when connectivity, services, permissions, sensors, peripherals, models, or dependencies may be unavailable and the UI must distinguish cached, stale, queued, limited, conflicted, or unrecoverable operation.
---

# Designing Offline and Degraded Experiences

## Overview
Degraded mode is a capability contract. Tell users what data they are seeing, what they can still do, what will be queued, and what requires reconnection — without pretending stale or local state is authoritative.

## Parent Contract
**Required parent:** `routing-ui-work`.

Require dependency graph, cache/data freshness, operations safe to queue/replay, conflict model, security/permission behavior, and recovery. Do not define offline support as “show a banner” if no operation semantics exist.

## Decision Model
Classify each function as available offline, locally editable/queued, read-only cached, unavailable, or unsafe. The classification may differ by data freshness and risk. Viewing yesterday’s article cache is acceptable; displaying stale clinical values as current is not.

Represent data provenance: live, cached-at timestamp, locally modified, queued, syncing, conflicted, rejected. Avoid one generic cloud icon. When users edit offline, preserve stable local identity and a durable queue. On reconnect, reconcile using domain semantics — last-write-wins is not a universal strategy. Show conflicts only when automatic merge cannot preserve intent, and present enough context to resolve them.

Service degradation can be partial. If search is down but saved data works, keep the usable path. If an AI model is unavailable, expose manual workflow if promised rather than disabling unrelated product functions. Permission or peripheral loss has its own recovery steps.

Security can tighten offline. Sensitive cached content may need local encryption or no offline storage; session expiry may prevent opening data even if cached. State those boundaries clearly.

## Evidence
Test cold start offline, network loss mid-read/edit/commit, queued actions across restart, reconnect order, clock/freshness, concurrent server edits, conflict resolution, revoked permissions, service-specific outage, cache eviction, accessibility, and high-risk stale data. Verify backend replay/idempotency with UI semantics.

## Output Contract
Return a `degraded-mode-contract` with `dependency_states[]`, `capability_matrix`, `data_freshness_rules`, `offline_edit_model`, `queue_semantics`, `reconnect_sequence`, `conflict_policy`, `security_constraints`, `manual_fallbacks[]`, `user_messaging`, and `degraded_tests[]`.

## Failure Traps
- “Offline” banner while actions still fail unpredictably.
- Stale data displayed without timestamp/source state.
- Queued destructive actions replayed twice.
- Silent last-write-wins after offline edit.
- Entire application disabled because one dependency is down.
- AI outage blocking a manual feature that does not need AI.
- Cached sensitive data exposed after session/account change.

Degraded UI is trustworthy when users can predict what will happen before they act.