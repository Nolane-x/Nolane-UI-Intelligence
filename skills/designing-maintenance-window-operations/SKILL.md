---
name: designing-maintenance-window-operations
description: Use when this specialist's decision ownership is materially in scope. Own planned operational maintenance windows, including scope, schedule, suppression, approvals, runbook state, customer communication, extension, abort, and return-to-service verification.
---
# Designing Maintenance Window Operations

## Parent Contract

**Required parent:** `designing-incident-response-operations`.

Inherit the broader routing and decision boundary from this canonical parent; this specialist remains accountable only for the narrower ownership, failure topology, falsification criteria, and output contract defined below.

## Decision ownership

Own the lifecycle of planned service-impacting maintenance. Decide scope, start/end, timezone, affected components, alert suppression context, approvals, runbook linkage, communication, start authorization, extension, abort/rollback, and post-maintenance verification. Calendar scheduling alone does not capture operational consequence.

## Inputs and evidence

Require maintenance scope, component/service map, schedule/timezone, expected impact, runbook, owner, approvers, alert/suppression rules, customer communication, rollback plan, success criteria, and collision with other changes/incidents. Identify regulatory or blackout periods.

## Procedure

Show scope, expected impact, owner, exact time basis, runbook, rollback, and success criteria before approval. Detect overlapping maintenance, change freezes, or active incidents. Alert suppression must be bounded to known signals/components and have automatic expiry; never hide unrelated alerts. At start, verify prerequisites and current service state. During execution, track runbook/mitigations and remaining window. Extensions need explicit new end time and communication consequences. Completion requires post-maintenance health verification and re-enabling/expiring suppressions.

## Failure topology

Failures include timezone confusion, indefinite alert suppression, overlapping changes, maintenance marked complete when work ended but service not verified, window extensions with no customer update, and rollback unavailable. Another failure is treating planned impact as harmless and allowing a real incident to be masked as maintenance.

## Falsification

Reject if suppression can outlive the window without explicit extension; if unrelated alerts are hidden; if overlapping high-risk maintenance is not surfaced; if completion can occur before health verification; if time display is ambiguous across operator/customer zones; if active incident impact is automatically attributed to maintenance without evidence; or if rollback readiness is unknown at start.

## Output contract

Return a `maintenance-window-operations-contract` with: scope/components; schedule/timezone; expected impact; owner/approvals; runbook/rollback; conflict detection; suppression scope/expiry; start prerequisites; execution state; extension protocol; communication consequences; health verification; and completion/abort rules. Include one overrun and one unexpected-incident scenario.

## Handoffs

Runbook execution handles procedural steps, status-page/stakeholder communications handle notices, service health verifies return, and incident response takes over if unexpected impact becomes an incident.