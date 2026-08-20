---
name: designing-a-b-test-interpretation
description: Interpret UI A/B tests with attention to assignment, exposure, power, novelty, heterogeneous effects, metric tradeoffs, and practical significance rather than winner labels alone.
---

# Designing A/B test interpretation

An experiment result is evidence about a defined population, exposure, and metric—not proof that one design is universally better. Use this skill when UI variants are evaluated through randomized experiments.

## Decision ownership

Own interpretation criteria, practical-significance thresholds, segment analysis policy, multiple-metric handling, novelty and duration checks, and decision linkage. Decide what evidence is sufficient to ship, iterate, or run follow-up study.

## Inputs and evidence

Collect experiment design, randomization unit, sample size, exposure definition, guardrail metrics, primary metric, duration, confidence intervals, pre-experiment baseline, implementation differences, and data-quality checks. Identify peeking or early stopping.

## Procedure

Confirm assignment and exposure integrity before reading outcomes. Interpret effect sizes and uncertainty, not only p-values. Compare primary benefit against guardrails. Examine pre-specified segments where domain reasoning suggests heterogeneous effects, while avoiding post-hoc fishing for any positive subgroup.

Consider novelty, learning, and network effects when short experiments may not generalize. Distinguish statistical significance from product significance and quantify the decision threshold.

## Failure topology

Choosing the variant with a tiny statistically significant lift can ignore cost or user harm. Repeatedly slicing segments creates false discoveries. Another failure is treating non-significance as proof of equivalence when the experiment lacked power.

Instrumentation differences between variants can fabricate apparent effects.

## Falsification

Recompute conclusions under confidence intervals, practical thresholds, and guardrails. Check sample-ratio mismatch and exposure logging. Remove post-hoc segments and see whether the core decision still stands. Extend duration or run equivalence analysis when “no difference” is the claim.

## Output contract

Produce an `a-b-test-interpretation-contract` containing experiment integrity checks, effect estimates, uncertainty, practical thresholds, guardrails, pre-specified segments, novelty/duration considerations, and the decision with unresolved caveats.

## Handoffs

Use `designing-experiment-guardrail-metrics` for metric design, `designing-qualitative-quantitative-triangulation` for supporting research, `designing-design-hypothesis-ledgers` for experiment linkage, and analytics engineering for instrumentation defects.