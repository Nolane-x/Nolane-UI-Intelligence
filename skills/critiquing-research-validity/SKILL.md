---
name: critiquing-research-validity
description: Use when UI decisions cite interviews, usability studies, surveys, analytics, experiments, preference tests, expert review, standards, benchmarks, prior product evidence, or research-saturation claims that need independent validity review.
---

# Critiquing Research Validity

## Overview
Challenge whether the evidence supports the exact design claim and whether the claim has outrun its method, sample, task, source authority, or freshness. More research artifacts do not automatically mean stronger evidence.

## Parent Contract
**Required parent:** `challenging-ui-designs`.

**May modify:** false. Review source ledger, research plan/evidence assessment, decision record, atlas/saturation record, and cited results. Do not replace a weak study with your own intuition.

## Decision Model
For each consequential claim trace **claim → evidence → method → sample/context → inference**. Method fit asks whether the evidence can answer the question: preference is not error rate; telemetry is not causal explanation; expert review is not representative user behavior; automated accessibility is not comprehension evidence. Sample fit asks whether participant expertise, disability, environment, locale, and risk role match the target. Task fit asks whether scenario/data/consequence reflect real use.

Check source authority and status. Normative Recommendation, regulatory guidance, platform HIG, empirical toolkit, design system, and community heuristic are not interchangeable. Draft status and version date remain visible. For current high-drift platform/AI guidance, stale evidence is a finding.

Review contradictions rather than cherry-picking. A decision should acknowledge credible opposing evidence and explain scope. Small qualitative research can reveal severe defects but should not become population percentages. Absence of complaints is not proof of absence, especially when feature usage is low.

For saturation, verify all five dimensions: breadth, depth, contradictions, novelty final wave, freshness. SATURATED is time-bounded and must reopen on recorded triggers.

## Evidence
Cite study/source identifiers, participant/task context, raw observations or result summaries, authority/status, dates, and the unsupported inference. State what additional evidence would falsify or support the claim rather than simply saying “more research needed.”

## Output Contract
Return a `finding-set` with `may_modify:false`, `artifact_revision`, `findings[] {finding_id, severity, claim, evidence_problem, source_or_study, user_decision_impact, falsifier, recommended_research, required_reverification}`, `unsupported_inferences[]`, `stale_sources[]`, `contradictions_ignored[]`, and `release_recommendation`.

## Failure Traps
- Five internal votes generalized to all customers.
- Analytics correlation narrated as causation.
- Community design trend treated as normative guidance.
- Draft standard described as current conformance requirement.
- Sample-size critique used to dismiss a credible catastrophic error.
- Research critic proposing a preferred UI instead of evaluating evidence.
- Saturation accepted because source count is large.

The reviewer protects decision quality by narrowing claims to what the evidence can actually carry.