---
name: designing-postmortem-authoring
description: Use when this specialist's decision ownership is materially in scope. Own evidence-linked incident postmortem creation from timeline, impact, contributing conditions, response decisions, learning, and corrective actions without turning the artifact into blame or a generic document template.
---
# Designing Postmortem Authoring

## Parent Contract

**Required parent:** `designing-incident-response-operations`.

Inherit the broader routing and decision boundary from this canonical parent; this specialist remains accountable only for the narrower ownership, failure topology, falsification criteria, and output contract defined below.

## Decision ownership

Own the structured retrospective artifact after an incident. Decide how timeline/evidence are imported, how impact and detection are summarized, how contributing conditions differ from simplistic root cause, how response effectiveness is assessed, and how lessons turn into owned follow-up actions. Rich-text editing is implementation support; this owner governs incident-learning semantics.

## Inputs and evidence

Require incident timeline, confirmed impact, severity changes, mitigations/results, hypotheses, communications, recovery criteria, responder roles, relevant changes, and organization postmortem policy. Identify required review, privacy/redaction, and publication scope.

## Procedure

Seed the postmortem from canonical incident evidence but require human synthesis. Preserve links back to source events rather than copying unsupported claims. Structure analysis around impact, detection, contributing conditions, response, recovery, communication, and what made the system more or less resilient. Avoid mandatory single-root-cause fields when causality is multi-factor. Distinguish factual timeline from interpretation. Corrective actions need owner, intended risk reduction, target horizon, and verification; vague "improve monitoring" is not sufficient. Support redacted/public variants without diverging the underlying factual record.

## Failure topology

Failures include timeline transcription with no analysis, blame-oriented person attribution, a forced single root cause, action items detached from findings, unsupported hindsight certainty, public redaction changing factual claims, and postmortems that remain drafts indefinitely. Another failure is auto-generated prose that sounds complete while responders have not reviewed causality.

## Falsification

Reject if a key causal claim has no linked evidence; if people are named as causes where system/process conditions are the actionable level; if corrective actions cannot trace to a finding/risk; if redacted and internal versions contradict on core facts; if the document hides uncertainty present during investigation; or if publication can occur without required reviewer acknowledgement.

## Output contract

Return a `postmortem-authoring-contract` with: evidence import; factual timeline link; impact/detection sections; contributing-condition model; response/recovery analysis; communication review; uncertainty handling; action-item schema; reviewer/publish state; redaction strategy; and source traceability. Include one multi-factor causal example.

## Handoffs

Timeline, hypothesis/evidence, mitigation, communications, and service health provide source records. Postmortem action follow-up owns execution after publication, while general content/publishing skills provide document mechanics.