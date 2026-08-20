---
name: designing-deployment-failure-diagnosis
description: Use when this specialist's decision ownership is materially in scope. Own post-failure diagnostic synthesis for deployments across stage/job errors, target state, logs, health, version distribution, configuration drift, and recommended next inspection without pretending to automate root cause.
---
# Designing Deployment Failure Diagnosis

## Parent Contract

**Required parent:** `designing-software-delivery-pipelines`.

Inherit the broader routing and decision boundary from this canonical parent; this specialist remains accountable only for the narrower ownership, failure topology, falsification criteria, and output contract defined below.

## Decision ownership

Own the operator-facing diagnostic workspace after a deployment does not complete as intended. Decide failure summary, failing scope, last successful stage, artifact/target identity, evidence aggregation, version distribution, likely investigation branches, and links to retry/rollback/incident escalation. It does not assert root cause unless evidence supports it.

## Inputs and evidence

Require deployment attempt, artifact, target(s), pipeline/job results, logs, rollout state, health signals, config drift, target events, time correlation, previous successful deployment, and retry/rollback availability. Identify partial failures where some targets changed successfully.

## Procedure

Start with what is known: operation, artifact, target scope, failure time, stage, and partial-success state. Present the most relevant evidence groups—job error/annotation, target events, health degradation, version distribution, drift—not an undifferentiated dashboard. Show previous known-good deployment for comparison. Offer investigation branches as evidence queries, not confident diagnoses. Retry should state scope and whether it reuses artifact/state; rollback should show compatibility. Escalation to incident response should carry the diagnostic bundle.

## Failure topology

Failures include generic "deployment failed", retry as the only action, partial rollout hidden, logs disconnected from target context, plausible-sounding root cause generated from one error line, and rollback offered without state compatibility. Another failure is losing evidence when a retry starts and replaces the failed attempt view.

## Falsification

Reject if failure scope/artifact/target are unknown; if partial success cannot be identified; if suggested cause is presented as fact without evidence; if retry scope is ambiguous; if previous attempt evidence is overwritten by retry; if health/version distribution cannot verify whether production changed; or if incident escalation loses diagnostic links.

## Output contract

Return a `deployment-failure-diagnosis-contract` with: attempt/artifact/target identity; failure stage/time; partial-success state; evidence groups; previous-known-good comparison; investigation branches with confidence; retry semantics; rollback eligibility link; incident-escalation payload; and preserved attempt history. Include one 3-of-10 targets failed scenario.

## Handoffs

CI logs, environment diff/drift, rollout/rollback, and health evidence feed diagnosis. Incident response owns broader operational impact once the failure becomes an active incident.