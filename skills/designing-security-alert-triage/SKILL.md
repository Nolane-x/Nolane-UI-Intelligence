---
name: designing-security-alert-triage
description: Use when analysts must prioritize and disposition high-volume security alerts while preserving severity, confidence, asset criticality, duplication, and investigation context.
---
# Designing Security Alert Triage

## Parent Contract

**Required parent:** `designing-security-operations-workspaces`.

Inherit the broader routing and decision boundary from this canonical parent; this specialist remains accountable only for the narrower ownership, failure topology, falsification criteria, and output contract defined below.

## Decision ownership

Own the decision surface that turns an incoming alert stream into ordered analyst work. This faculty decides which signals determine priority, how duplicate or correlated alerts are represented, what minimum evidence is visible before opening an investigation, and how analysts record dispositions such as benign, expected, suspicious, duplicate, escalated, or unresolved. It does not own the detection rule that emitted the alert or the full investigation that follows triage.

## Inputs and evidence

Require alert schema, source/detector identity, severity model, confidence model, asset and identity criticality, tenant or business scope, suppression rules, correlation identifiers, alert age, SLA expectations, historical false-positive rates, and the actual dispositions analysts use. Collect realistic bursts: hundreds of identical alerts, one severe alert hidden among low-risk noise, delayed telemetry, reopened alerts, and alerts whose severity conflicts with asset criticality. Include examples where the detector is high confidence but impact is low and vice versa.

## Procedure

Define priority as an inspectable composition rather than a mysterious score. Show the few factors that materially changed ordering—severity, confidence, blast radius, privileged identity, crown-jewel asset, exploitability, recency, or active spread. Separate queue sorting from analyst ownership so assignment does not silently imply severity. Represent correlated families without hiding child evidence; analysts need to understand whether a group is one incident, repeated attempts, or merely similar signatures. Design disposition as a structured decision with rationale and optional evidence references, not a colored checkbox. Preserve queue position and filters when opening and returning from an alert. Make stale, superseded, duplicate, suppressed, and reopened states explicit.

## Failure topology

- A single opaque “risk score” decides order but analysts cannot explain why.
- Duplicate collapsing hides a child alert that affected a different high-value asset.
- Severity color becomes the only priority cue and is inaccessible or misleading.
- Closing an alert erases the rationale needed to tune detections later.
- Assignment, acknowledgment, investigation, and resolution are conflated into one status.
- Refreshing the queue moves the item being read and destroys analyst orientation.
- Alert age is hidden, so a critical but stale item appears equivalent to an active event.

## Falsification

Feed the interface a burst containing duplicates, conflicting severity and asset criticality, reopened alerts, one privileged-account event, and late-arriving enrichment. Ask analysts to explain why the top five are ordered as shown and to disposition several without opening full cases. The design fails if priority cannot be explained, if grouped alerts conceal materially different scope, or if a disposition cannot later be audited back to evidence and rationale.

## Output contract

Return `security-alert-triage-contract` containing priority factors, queue ordering semantics, grouping/correlation behavior, alert lifecycle states, disposition taxonomy, analyst assignment rules, evidence shown at triage depth, stale/reopened handling, accessibility requirements, and triage verification cases.

## Handoffs

Escalated work routes to `designing-security-operations-workspaces` and investigation specialists. Correlation logic routes to `designing-security-event-correlation`; detector quality routes to detection-rule owners; case lifecycle routes to `designing-security-case-evidence-management`. Generic work-queue and triage faculties may supply interaction primitives but cannot replace security-specific risk and evidence semantics.