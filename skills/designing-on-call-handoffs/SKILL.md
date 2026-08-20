---
name: designing-on-call-handoffs
description: Use when this specialist's decision ownership is materially in scope. Own continuity across responder shift changes, including active incidents, pending alerts, role transfer, unresolved hypotheses, mitigation state, and acknowledgement by the incoming responder.
---
# Designing On-Call Handoffs

## Parent Contract

**Required parent:** `designing-incident-response-operations`.

Inherit the broader routing and decision boundary from this canonical parent; this specialist remains accountable only for the narrower ownership, failure topology, falsification criteria, and output contract defined below.

## Decision ownership

Own the transfer of operational responsibility between on-call responders or shifts. Decide handoff contents, active/pending work, acknowledgement, role transfer, time boundary, fallback if incoming responder does not accept, and how context is summarized without losing evidence. This is broader than changing an assignee because operational continuity and latent risk matter.

## Inputs and evidence

Require on-call schedule, active incident/alert state, role assignments, pending escalations, ongoing mitigations, maintenance windows, open hypotheses, recent changes, handoff timing, and acknowledgement policy. Identify services with overlapping rotations or follow-the-sun handoffs.

## Procedure

Generate a handoff packet from live operational state, then require human review before sending. Separate "must act", "watch closely", and "context" so critical pending work is not buried. Include active incidents with current objective, severity, role, mitigations, next checks, and communication deadlines. Pending alerts/escalations and maintenance events need explicit status. Incoming responder acknowledgement should transfer responsibility only when accepted; until then, outgoing ownership remains visible or a fallback is invoked. Preserve the handoff record for later incident reconstruction.

## Failure topology

Failures include copy/paste handoff notes detached from current state, incoming responder assumed active before acknowledging, open mitigations omitted, communication deadlines lost at shift change, duplicate owners during follow-the-sun transitions, and sensitive information shared beyond the incoming scope. Another failure is an excessively long handoff that hides the few urgent items.

## Falsification

Reject if a critical active incident can be omitted from generated handoff; if responsibility changes before acknowledgement; if pending communication/escalation deadlines are invisible; if current mitigation status differs from the handoff with no freshness cue; if no fallback exists when the incoming responder is unavailable; or if handoff history cannot identify effective transfer time.

## Output contract

Return an `on-call-handoffs-contract` with: handoff scope; priority classes; active-incident summary; alert/escalation/maintenance inclusion; freshness; outgoing/incoming roles; acknowledgement state; effective transfer time; fallback; privacy scope; and retained handoff record. Include one unacknowledged shift transfer.

## Handoffs

Responder-role assignment performs incident role transfer, escalation handles unavailable incoming coverage, war-room collaboration supports live context, and incident timeline records effective responsibility changes.