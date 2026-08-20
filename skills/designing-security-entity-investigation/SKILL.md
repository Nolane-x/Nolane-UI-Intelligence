---
name: designing-security-entity-investigation
description: Use when analysts pivot around users, hosts, processes, domains, IPs, applications, or cloud resources and must preserve identity resolution, provenance, history, and relationship confidence.
---
# Designing Security Entity Investigation

## Parent Contract

**Required parent:** `designing-security-operations-workspaces`.

Inherit the broader routing and decision boundary from this canonical parent; this specialist remains accountable only for the narrower ownership, failure topology, falsification criteria, and output contract defined below.

## Decision ownership

Own the investigative surface for one security entity and the pivots that radiate from it. Decide how identities from multiple telemetry sources are reconciled, how aliases and historical identities are shown, which behaviors form the entity baseline, and how related entities are ranked without overstating weak associations. This faculty is about entity truth and pivot safety; it does not own full attack-path visualization or generic asset inventory administration.

## Inputs and evidence

Require stable and unstable identifiers for each entity type, source systems, tenant/account boundaries, hostname or username reuse rules, cloud resource lifecycle, process ancestry, address reassignment behavior, enrichment sources, criticality labels, owner information, and event history. Collect examples where a username exists in multiple directories, an IP is reassigned, a cloud instance is recreated with the same name, a process hash appears on many hosts, or an external domain has conflicting reputation sources.

## Procedure

Start with identity confidence. Display the canonical entity and every alias or source-specific identifier that materially affects matching. Separate current attributes from historical attributes so an analyst does not apply today's owner or IP to yesterday's event. Build a behavior summary from inspectable time ranges and data sources; do not hide source coverage. Rank related entities by relationship type—authentication, process parentage, network communication, shared credential, shared artifact, administrative ownership—rather than one generic “related” list. Every pivot should carry the originating evidence and selected time window. Provide explicit comparison between baseline behavior and the investigation window while acknowledging sparse data.

## Failure topology

- A hostname is treated as permanent identity after the underlying device was reimaged or replaced.
- IP address relationships imply machine identity in DHCP/NAT environments.
- Reputation or enrichment badges appear authoritative despite stale or conflicting sources.
- Related entities are sorted by an unexplained score and weak coincidence looks causal.
- Historical events display current owner, department, or privilege state as if it existed at event time.
- Pivots reset the time window and make behavior appear unrelated.
- Entity pages hide which telemetry sources are absent.

## Falsification

Test identity reuse, a reassigned IP, a renamed user, a short-lived cloud resource, multiple matching process hashes, and enrichment with conflicting verdicts. Ask analysts to state exactly which object they believe they are investigating and why two records are considered the same or different entity. The design fails if identity confidence or temporal validity cannot be inspected, or if a pivot loses its originating evidence.

## Output contract

Return `security-entity-investigation-contract` with entity identity schema, alias/history treatment, temporal attribute rules, source coverage, relationship taxonomy, pivot-context preservation, baseline comparison model, enrichment provenance, and entity-resolution verification cases.

## Handoffs

Path-level relationship exploration routes to `designing-attack-path-visualization`; event ordering routes to `designing-threat-investigation-timelines`; IOC lookup routes to `designing-indicator-of-compromise-search`; account-specific anomaly interpretation routes to `designing-authentication-anomaly-review`. Generic entity tables and graphs remain subordinate to this identity contract.