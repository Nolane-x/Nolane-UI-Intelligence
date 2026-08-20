---
name: designing-alert-triage-workspaces
description: Use when this specialist's decision ownership is materially in scope. Own high-noise operational alert review, deduplication, grouping, acknowledgement, suppression context, and promotion into an incident without hiding uncertainty.
---
# Designing Alert Triage Workspaces

## Parent Contract

**Required parent:** `designing-incident-response-operations`.

Inherit the broader routing and decision boundary from this canonical parent; this specialist remains accountable only for the narrower ownership, failure topology, falsification criteria, and output contract defined below.

## Decision ownership

Own the responder-facing surface that turns raw alerts into an actionable queue. Decide grouping/deduplication, priority evidence, acknowledgement, ownership, correlation context, suppression visibility, alert aging, and the threshold for promoting a cluster to an incident. This owner does not decide detector logic; it makes detector outputs reviewable without pretending every alert is independently meaningful.

## Inputs and evidence

Require alert schema, source/detector identity, service/entity links, severity/confidence, dedup keys, firing/resolved timestamps, suppression rules, historical recurrence, on-call ownership, and incident-linking behavior. Measure realistic burst rates and repeated flapping patterns, not average alert volume.

## Procedure

Group only when the grouping rule is inspectable and reversible. Preserve count, first/last seen, member diversity, and representative severity so aggregation does not conceal one critical member. Distinguish firing, recovering, resolved, acknowledged, suppressed, and stale states. Acknowledgement must mean a responder has taken ownership, not that the condition is fixed. Surface suppression source and expiry. Promotion to incident should carry selected alerts and current context forward instead of requiring copy/paste. Provide fast filters by service, source, owner, and time while keeping active filter scope obvious.

## Failure topology

Failures include alert floods sorted only by newest, groups that hide critical outliers, acknowledgement treated as resolution, suppressed alerts disappearing completely, flapping alerts generating repeated incidents, and stale alerts remaining visually active. Another failure is a triage queue whose severity color is trusted even when confidence/source quality differ materially.

## Falsification

Reject if a grouped alert can contain a higher-severity member with no cue; if responders cannot identify why an alert is suppressed; if acknowledging removes it from all shared visibility; if promotion to incident loses member alerts/evidence; if duplicate alerts cannot be collapsed without deleting source identity; or if resolved alerts remain indistinguishable from firing ones in a burst.

## Output contract

Return an `alert-triage-workspaces-contract` with: alert state model; grouping/dedup rules; member/outlier disclosure; acknowledgement semantics; owner assignment; suppression visibility/expiry; confidence/source cues; flapping treatment; filters; stale handling; and incident-promotion payload. Include one burst and one suppressed-critical-alert scenario.

## Handoffs

Use incident severity declaration only after operational impact is assessed, service health for current system evidence, and security alert triage for threat-specific semantics. Generic work queues provide list mechanics but not alert-state meaning.