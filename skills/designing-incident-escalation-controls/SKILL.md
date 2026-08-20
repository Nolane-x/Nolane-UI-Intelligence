---
name: designing-incident-escalation-controls
description: Own incident escalation across responder tiers, leadership, vendors, specialist teams, and regulatory pathways with explicit triggers, acknowledgement, timeout, and fallback.
---
# Designing Incident Escalation Controls

## Decision ownership

Own escalation as a controlled coordination action. Decide eligible targets, trigger/rationale, urgency, acknowledgement, retry/fallback, timeout, role authority, and whether escalation changes incident severity or merely adds support. Generic notifications send messages; this owner governs the operational state of requesting additional authority or expertise.

## Inputs and evidence

Require escalation policies, on-call rosters, specialist teams, vendor contacts, severity triggers, acknowledgement SLAs, leadership/regulatory paths, permissions, and fallback chains. Identify external escalations that may disclose sensitive incident information.

## Procedure

Present escalation targets by role/purpose rather than a raw contact list. Before sending, show current incident context that will be shared and allow minimal necessary redaction for external parties. Record initiator, target, reason, urgency, channel, sent time, acknowledgement deadline, and outcome. Pending escalation remains visible until acknowledged or explicitly cancelled. Timeouts should suggest the next defined fallback rather than silently retrying forever. Escalation must not automatically alter severity unless policy says so; show any consequence separately.

## Failure topology

Failures include paging the wrong team from stale roster data, escalation disappearing after send, no indication whether anyone acknowledged, leaking internal data to vendors, repeated pages with no fallback logic, and severity changing implicitly because leadership was notified. Another failure is making escalation so hidden that responders improvise personal messages outside the incident record.

## Falsification

Reject if a sent escalation has no tracked acknowledgement state; if timeout/fallback is undefined; if external recipients receive undisclosed sensitive context; if stale roster identity cannot be detected; if escalation can change severity invisibly; or if cancellation leaves recipients believing the request is active with no follow-up.

## Output contract

Return an `incident-escalation-controls-contract` with: escalation targets/roles; trigger/rationale; shared-context preview; privacy/redaction; sent/pending/acknowledged/failed/cancelled states; acknowledgement deadline; fallback chain; consequence on severity/roles; and audit history. Include one unacknowledged vendor escalation.

## Handoffs

Responder roles and on-call handoffs provide current contacts, severity policy may require escalation, stakeholder communications handle broader audiences, and generic notification systems carry delivery transport.