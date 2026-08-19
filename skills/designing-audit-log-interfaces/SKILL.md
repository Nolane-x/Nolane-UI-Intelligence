---
name: designing-audit-log-interfaces
description: Use when users inspect tamper-resistant or accountability-oriented event history and the interface must preserve actor, action, target, time, source, before/after evidence and filtering without rewriting history as friendly activity feed copy.
---

# Designing Audit Log Interfaces

## Parent Contract
**Required parent:** `designing-data-dense-interfaces`.

This faculty owns exploration and presentation of audit events. It does not guarantee cryptographic immutability, retention compliance or legal admissibility; those claims require system and policy evidence.

## Decision Boundary
An audit event should preserve stable identifiers and structured fields: event ID, actor/principal, action, target/resource, occurred/recorded timestamps where distinct, source/session/IP/device when lawful and useful, result, relevant before/after or changed fields, and correlation/request IDs. Human-readable text is a projection of those fields, not the only record.

Chronology and time semantics matter. Use explicit timezone, precise timestamps on demand and stable ordering for events with equal times. Delayed ingestion should not silently place an event as though it was observed earlier; expose occurrence vs receipt when it changes interpretation.

Filtering/search should support investigations: actor, action type, resource, outcome, date range, correlation ID and domain fields. Applied filters must remain visible. Pagination/export should preserve a stable query snapshot when evidence is expected to be reproducible; a live-growing log can otherwise shift pages while the user investigates.

Sensitive audit data requires scoped access and masking without pretending redacted fields never existed. If an actor is deleted, preserve historical actor identity according to policy rather than replacing all old events with “Unknown” if a durable audit identifier is allowed.

Before/after diffs should show semantic changes, not enormous raw JSON blobs by default. However, friendly summaries cannot omit material changed fields.

## Failure Topology
- Activity feed says “Alice updated settings” but does not identify which settings changed.
- Sorting uses local formatted timestamp strings and misorders cross-timezone events.
- Live events shift pagination so an investigator sees duplicates/misses records.
- Deleted users erase actor attribution from old events.
- Export does not record filters/timezone/query snapshot and cannot reproduce the view.
- Redaction hides the fact that a protected value changed at all.

## Falsification and Recovery
Falsify with same-timestamp events, delayed ingestion, deleted actors, permission-scoped fields, live arrival during paging, export/reimport and before/after multi-field changes. Verify every displayed narrative can be traced to structured event fields.

Recover by treating structured audit events as authority, separating occurred/recorded time, snapshotting investigative queries and presenting semantic diffs with explicit redaction markers.

## Output Contract
Return `audit-log-interface-contract` with event schema projection, actor/target identity, temporal ordering, filter/search model, live/snapshot policy, sensitive-field treatment, semantic diff, export context, accessibility and reproducibility tests.