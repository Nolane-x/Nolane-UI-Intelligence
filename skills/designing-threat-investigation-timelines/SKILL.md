---
name: designing-threat-investigation-timelines
description: Use when analysts must reconstruct a security sequence from heterogeneous event streams whose clocks, entities, confidence, and causal relationships may disagree.
---
# Designing Threat Investigation Timelines

## Parent Contract

**Required parent:** `designing-security-operations-workspaces`.

Inherit the broader routing and decision boundary from this canonical parent; this specialist remains accountable only for the narrower ownership, failure topology, falsification criteria, and output contract defined below.

## Decision ownership

Own temporal reconstruction for security investigations. Decide how events from endpoint, identity, network, cloud, email, and human notes are normalized into a timeline without pretending that timestamp order equals causality. This faculty owns time-window navigation, clock uncertainty, event grouping, causal annotations, gaps, and analyst-authored milestones. It does not own generic log viewing or the detection semantics that produced individual events.

## Inputs and evidence

Require source timestamps, ingestion timestamps, timezone and clock-drift characteristics, event identifiers, entity identities, confidence, deduplication keys, retention gaps, and representative attacks with concurrent benign activity. Include events that arrive late, sources with coarse timestamp precision, events replayed after reconnect, and manually entered observations. Record whether data sources can provide parent/child, session, trace, request, process, or authentication linkage that is stronger than time adjacency.

## Procedure

Maintain at least two temporal truths when needed: when the source says an event occurred and when the system observed it. Normalize display time but preserve original timestamp and precision. Visually distinguish directly observed events, inferred relationships, analyst hypotheses, and external notes. Let analysts compress repetitive noise without losing count, diversity, or first/last occurrence. Support reversible grouping by process tree, session, identity, host, or detector while preserving chronological orientation. Make gaps explicit when telemetry stops. Allow evidence pinning and named milestones such as initial access, privilege change, lateral movement, or containment, but never auto-label attack phases as certain when evidence is ambiguous.

## Failure topology

- Ingestion order is silently presented as event order.
- Two events one second apart are drawn as causally connected without supporting linkage.
- Clock skew makes a child process appear before its parent and the interface hides the inconsistency.
- Repetitive events are collapsed until analysts can no longer tell whether activity affected one or many entities.
- Manual notes look identical to machine-observed evidence.
- Timeline zoom drops low-volume but high-value events.
- Changing timezone or time window alters the apparent order of ambiguous timestamps without warning.

## Falsification

Use a scenario with clock skew, late-arriving events, repeated authentication attempts, concurrent benign activity, an analyst note, and a process lineage link that contradicts naive chronological ordering. The interface fails if users infer causality from placement alone, cannot recover original source time, or cannot tell whether a gap means inactivity versus missing telemetry.

## Output contract

Return `threat-investigation-timelines-contract` with timestamp model, precision/clock-skew treatment, event source encoding, grouping rules, causal-versus-temporal distinction, gap semantics, milestone behavior, analyst annotation model, zoom/aggregation policy, and reconstruction test scenarios.

## Handoffs

Entity-focused pivots route to `designing-security-entity-investigation`; cross-event inference routes to `designing-security-event-correlation`; case-preserved evidence routes to `designing-security-case-evidence-management`. Reuse generic time-series or log interaction only for navigation mechanics, never for security evidence semantics.