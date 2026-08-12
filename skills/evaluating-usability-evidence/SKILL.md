---
name: evaluating-usability-evidence
description: Use when a UI recommendation cites user research, telemetry, experiments, expert review, benchmarks, surveys, anecdotes, or prior product data and the strength or transferability of that evidence affects the decision.
---

# Evaluating Usability Evidence

## Overview
Evidence earns influence through fit, not through the label “research.” This skill judges whether an observation supports the exact UI claim being made and how far that claim may travel.

## Parent Contract
**Required parent:** `routing-ui-work`.

Require the proposed decision and its supporting evidence. If no decision claim exists, return a framing gap rather than grading a pile of research artifacts.

## Decision Model
Evaluate six dimensions. **Provenance:** who collected the evidence and under what incentives. **Method fit:** whether the method can answer the claim — preference survey versus task performance, telemetry versus causal explanation, expert review versus user behavior. **Sample fit:** whether participants represent relevant expertise, accessibility needs, environment, and risk context. **Task realism:** whether data, timing, consequences, device, and interruptions resemble actual use. **Signal quality:** repeated pattern, effect magnitude, critical severity, confounds, missing data. **Transferability:** how much platform, workflow, population, or product change separates evidence from the new decision.

Separate absence of evidence from evidence of absence. A clean automated audit does not prove cognitive accessibility. No support tickets may mean low feature use. A preference win can coexist with worse error rates. A statistically precise metric can still measure the wrong outcome.

Weight severe repeated failures differently from minor taste disagreement. For high-risk tasks, a single credible critical failure can justify redesign even when the sample is small; it does not justify estimating population prevalence.

## Evidence
Create a trace from each recommendation to the observation supporting it. Preserve raw count or study context when available, uncertainty, alternative explanations, and contradictory evidence. Do not manufacture confidence scores from arbitrary numerics; use qualitative confidence with reasons unless the study design supports quantitative inference.

## Output Contract
Return a `usability-evidence-assessment` with `decision_claim`, `evidence_items[] {type, provenance, method_fit, sample_fit, task_fit, signal, transferability}`, `contradictions[]`, `unsupported_inferences[]`, `confidence`, `claim_bounds`, `additional_evidence_needed[]`, and `decision_effect`.

## Failure Traps
- “Users said” with no participant/task context.
- Treating telemetry correlation as causal explanation.
- Generalizing internal designer preference to customers.
- Discounting accessibility findings because they affect a minority sample.
- Converting a small qualitative study into population percentages.
- Ignoring evidence that contradicts the favored design.
- Giving precise confidence numbers unsupported by the research design.

The strongest output often narrows a claim rather than strengthening it.