---
name: designing-security-operations-workspaces
description: Use when analysts must detect, investigate, contain, and hand off security events across high-volume telemetry without losing evidence provenance, risk context, or operational control.
---
# Designing Security Operations Workspaces

## Parent Contract

**Required parent:** `designing-security-centers`.

Inherit the broader routing and decision boundary from this canonical parent; this specialist remains accountable only for the narrower ownership, failure topology, falsification criteria, and output contract defined below.

## Decision ownership

Own the top-level interaction architecture for a security operations center workspace. Decide how alerts, entities, timelines, evidence, cases, actions, automation, and analyst notes coexist without collapsing into one undifferentiated dashboard. This faculty owns operational context continuity: an analyst moving from an alert to a user, host, process, network session, or case must retain why the transition happened and what evidence justified it. It does not define detection logic, endpoint containment semantics, or vulnerability scoring; specialist children own those decisions.

## Inputs and evidence

Require the security operating model, analyst roles and authority, alert volume and latency, data-source coverage, entity identifiers, case workflow, evidence-retention constraints, automation boundaries, escalation policy, destructive-response permissions, and representative investigations from benign to severe. Inspect false-positive-heavy queues, partial telemetry, delayed events, duplicated identities, cross-tenant boundaries, and incidents that span endpoint, identity, email, and network systems. Treat timestamps, source systems, confidence, and evidence lineage as first-class data.

## Procedure

Model the workspace around investigation state rather than product modules. Define a stable investigation context containing trigger, scope, working hypotheses, entities, time window, evidence set, actions taken, and unresolved questions. Establish navigation between queue, entity, timeline, graph, raw events, and case surfaces while preserving filters and provenance. Separate observation from intervention: containment, block, disable, isolate, or revoke actions must have stronger authority cues than search and exploration. Design evidence pinning and comparison so analysts can preserve important facts before changing the time window or query. Make uncertainty visible; absence of telemetry must not look like evidence of absence. Provide keyboard-dense workflows, fast pivots, and explicit handoff state for shift changes.

## Failure topology

- The workspace optimizes chart density but forces analysts to reconstruct investigation context after every pivot.
- Entity names appear identical across data sources even when identifiers or tenants differ.
- Automated enrichment is displayed as fact without source, freshness, or confidence.
- Destructive response controls sit beside harmless filters with no authority separation.
- Time-window changes silently discard pinned evidence or alter counts used in a decision.
- Case notes and raw evidence drift apart, making later audit impossible.
- Missing telemetry is rendered as zero activity.

## Falsification

Run a multi-source investigation beginning with a noisy alert, pivot through identity and endpoint data, change time windows, pin evidence, create a case, perform a simulated containment action, then hand the work to another analyst. Fail the design if the second analyst cannot reconstruct why each pivot and action occurred, if source ambiguity can change the apparent entity, or if an action can be executed without seeing scope, authority, and expected blast radius.

## Output contract

Return `security-operations-workspaces-contract` containing workspace regions, investigation-context model, evidence lineage rules, entity identity policy, observation-versus-response separation, pivot/navigation semantics, case synchronization, uncertainty treatment, analyst handoff state, and representative verification scenarios.

## Handoffs

Delegate queue mechanics to `designing-security-alert-triage`, temporal reconstruction to `designing-threat-investigation-timelines`, entity pivots to `designing-security-entity-investigation`, response controls to dedicated containment skills, and cross-shift continuity to `designing-security-operations-handoffs`. Reuse generic audit, search, graph, data-dense, permissions, and high-stakes decision faculties only for their lower-level mechanics.