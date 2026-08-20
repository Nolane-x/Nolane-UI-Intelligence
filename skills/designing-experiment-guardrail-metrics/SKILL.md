---
name: designing-experiment-guardrail-metrics
description: Design guardrail metrics that reveal whether a UI experiment improves its target outcome by shifting cost, error, accessibility, trust, or burden elsewhere.
---

# Designing experiment guardrail metrics

Optimization can move harm into metrics nobody watches. Use this skill when experiments target conversion, engagement, speed, retention, or task completion and need constraints that protect broader product quality.

## Decision ownership

Own guardrail selection, directionality, acceptable degradation thresholds, alerting, analysis windows, and decision rules when primary and guardrail metrics conflict. Decide which guardrails are universal versus experiment-specific.

## Inputs and evidence

Collect the intervention mechanism, expected behavior change, known risks, support/contact rates, errors, cancellations, refunds, accessibility telemetry where appropriate, latency, downstream retention, and business constraints. Identify ways users could achieve the primary metric through coercion or accidental action.

## Procedure

Choose a small set of guardrails causally adjacent to likely harm. Define thresholds before launch. Include system health and user-quality metrics where relevant. For funnel experiments, monitor downstream reversal or complaint signals rather than only immediate completion.

Use qualitative or audit-based guardrails for harms that telemetry cannot capture reliably. Keep guardrails interpretable; a composite “quality score” may obscure which risk moved.

## Failure topology

Too many guardrails make every result inconclusive. Generic guardrails can miss intervention-specific harms. Another failure is monitoring guardrails but shipping despite meaningful degradation because the primary metric “won.”

Rare severe harms may disappear in averages.

## Falsification

Construct plausible harmful mechanisms and verify at least one guardrail would detect each. Simulate primary lift with threshold-level guardrail degradation and ensure decision policy is clear. Inspect distributions and tail events where averages hide severity.

## Output contract

Produce an `experiment-guardrail-metrics-contract` defining primary mechanism, risk hypotheses, guardrails, measurement windows, thresholds, rare-event treatment, conflict decision rules, and instrumentation validation.

## Handoffs

Use `designing-a-b-test-interpretation` for results, trust/high-stakes skills for severe harms, `designing-task-success-measures` for usability outcomes, and `designing-design-hypothesis-ledgers` for pre-registration.