---
name: designing-incident-hypothesis-evidence-logs
description: Use when this specialist's decision ownership is materially in scope. Own explicit incident reasoning records that separate hypotheses from facts, attach supporting and contradicting evidence, track confidence, and preserve rejected explanations.
---
# Designing Incident Hypothesis Evidence Logs

## Parent Contract

**Required parent:** `designing-incident-response-operations`.

Inherit the broader routing and decision boundary from this canonical parent; this specialist remains accountable only for the narrower ownership, failure topology, falsification criteria, and output contract defined below.

## Decision ownership

Own the reasoning ledger used to investigate causes and impact during an incident. Decide how hypotheses are stated, linked to evidence, assigned confidence/status, tested, contradicted, merged, rejected, and promoted to confirmed findings. This owner guards against chat-driven memory and premature root-cause certainty.

## Inputs and evidence

Require observability evidence types, timeline events, recent changes, service topology, responder observations, query links, experiment results, and incident scope. Determine whether hypotheses can concern root cause, blast radius, mitigation effect, or secondary symptoms and label those categories.

## Procedure

Capture hypotheses as falsifiable statements with owner or proposer, creation time, predicted observations, and current confidence. Attach evidence as supporting, contradicting, or contextual; do not merely paste links without interpretation. Preserve competing hypotheses side by side. When evidence changes confidence, record the reason. Rejected hypotheses remain visible in a collapsed/history state so teams do not repeat disproven work. Only promote a hypothesis to confirmed when the organization-defined evidence threshold is met; otherwise communicate uncertainty.

## Failure topology

Failures include speculative chat lines becoming "root cause", evidence links with no claimed relationship, confidence changed arbitrarily, rejected ideas deleted, confirmation bias showing only supporting evidence, and one hypothesis mixing several independent claims. Another failure is over-formalizing reasoning so responders stop recording hypotheses at all.

## Falsification

Reject if a confirmed finding has no inspectable supporting evidence; if contradictory evidence cannot be attached; if rejected hypotheses disappear entirely; if confidence can change with no reason; if a hypothesis cannot state what observation would disprove it; or if creating a hypothesis requires enough fields to discourage rapid capture during active response.

## Output contract

Return an `incident-hypothesis-evidence-logs-contract` with: hypothesis categories; statement format; predicted/falsifying observations; proposer/time; confidence/status; supporting/contradicting evidence links; change rationale; merge/split/reject behavior; confirmation threshold; and historical visibility. Include one disproven and one competing-hypothesis example.

## Handoffs

Timeline capture supplies chronology, dependency impact analysis supplies structural evidence, mitigation tracking can test effect hypotheses, and postmortem authoring consumes confirmed/rejected reasoning without rewriting uncertainty.