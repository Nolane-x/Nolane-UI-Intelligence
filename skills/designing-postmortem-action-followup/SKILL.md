---
name: designing-postmortem-action-followup
description: Use when this specialist's decision ownership is materially in scope. Own corrective-action lifecycle after an incident, including risk linkage, ownership, due horizon, verification of risk reduction, deferral, supersession, and closure evidence.
---
# Designing Postmortem Action Followup

## Parent Contract

**Required parent:** `designing-incident-response-operations`.

Inherit the broader routing and decision boundary from this canonical parent; this specialist remains accountable only for the narrower ownership, failure topology, falsification criteria, and output contract defined below.

## Decision ownership

Own what happens after corrective actions leave the postmortem. Decide how actions link to findings/risks, move into project systems, retain incident provenance, receive owner and target horizon, get reviewed, are deferred/superseded, and prove effectiveness before closure. A closed task is not automatically a closed incident risk.

## Inputs and evidence

Require published postmortem findings, action items, risk/severity, owners, work-management integration, due-date policy, verification criteria, dependency links, and review cadence. Identify actions that are exploratory versus committed remediation.

## Procedure

Create follow-up items with immutable incident/finding linkage and explicit intended risk reduction. Assign accountable owner and horizon, but allow planning systems to refine implementation tasks underneath. Track state separately from verification: implemented, measuring, effective, ineffective, deferred, superseded. When an action is deferred or dropped, require rationale and risk acceptance/alternative. Periodic review should prioritize overdue high-risk actions and actions lacking verification. Closing should capture evidence that the intended control or resilience improvement exists and, where possible, behaves as expected.

## Failure topology

Failures include action items copied into a tracker with lost incident context, completion based on merged code rather than risk outcome, endless due-date pushing, deferred actions disappearing, duplicate remediation across incidents, and metrics that reward closing tickets rather than reducing recurrence risk.

## Falsification

Reject if an action cannot trace to its incident finding; if implementation automatically marks the risk mitigated; if defer/cancel has no rationale; if overdue high-impact actions are indistinguishable from low-priority housekeeping; if duplicate actions cannot be linked/superseded; or if closure lacks stated verification evidence.

## Output contract

Return a `postmortem-action-followup-contract` with: incident/finding provenance; intended risk reduction; owner; target horizon; planning integration; lifecycle states; verification criteria/evidence; defer/cancel/supersede rationale; duplicate linking; review prioritization; and closure rule. Include one implemented-but-ineffective action case.

## Handoffs

Project/work management executes remediation, risk registers track accepted residual risk, postmortem authoring creates the source finding, and reliability experiments may verify whether a control improved resilience.