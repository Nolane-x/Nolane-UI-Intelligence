---
name: designing-benefit-entitlement-explanations
description: Use when a public service must explain an award, entitlement amount, duration, reduction, refusal, suspension, or change and users need to understand the governing factors and available correction or review routes.
---

# Designing Benefit Entitlement Explanations

An entitlement result is consequential. The interface should help a person understand what was decided, the effective period, the key inputs/rules that affected the result, and what they can do if facts are wrong or they disagree.

## Parent Contract
**Required parent:** `designing-public-service-experiences`.

The parent owns the service journey. This skill owns explanation of formal entitlement outcomes after policy has been applied; it does not author the policy or independently calculate awards.

## Decision Anatomy
Present the decision before the calculation detail: awarded/refused/suspended/changed, effective date or period, amount/frequency where applicable, and any conditions. Then expose the material factors used—income period, household composition, contribution record, disability assessment, residency status, caps, deductions, overpayments, or other domain-specific inputs.

A calculation explanation should reconcile to the displayed result. Group additions, reductions, disregards, and caps according to the actual policy model. Avoid decorative “breakdowns” that omit a hidden adjustment and therefore do not sum to the final amount.

## Uncertainty and Human Judgement
Some decisions include discretionary or assessed components. Distinguish rule-derived amounts from human assessment and state what evidence was considered where policy allows. Do not make algorithmic certainty claims simply because the result was produced by software.

## Correction, Review, Appeal
Separate “my information is wrong” from “I disagree with the decision.” The first may route to correction/change reporting; the second may route to reconsideration, review, or appeal. Make deadlines, evidence requirements, and decision references visible when authoritative.

## Evidence
Use known decisions with multiple adjustments, zero award, partial award, changed circumstances, retroactive effect, refusal, and manual assessment. Verify the explanation reconciles exactly to authoritative decision data and that links open the correct case/decision revision.

Test plain-language comprehension without removing legally material distinctions. Include screen reader, print/PDF if official notices use it, and multilingual content expansion.

## Failure Modes
- Amount is prominent but effective period is hidden.
- Breakdown does not mathematically reconcile to final award.
- Human assessment is presented as an automatic rule result.
- Refusal copy cites a generic reason while the authoritative decision is more specific.
- Correction and appeal routes are merged into one confusing contact link.
- Deadline is shown without timezone/date basis or authoritative source.
- A later revised decision silently replaces the earlier explanation.

## Falsification
Choose a decision with two reductions and one cap. Falsify if users cannot reproduce the displayed award from the explanation. Then revise one underlying fact; falsify if the UI cannot distinguish the superseded decision from the new one.

## Recovery
Bind explanations to immutable decision revisions, expose all material adjustments, reconcile totals, and separate correction from challenge routes. When the system lacks enough reason data, state that limitation and direct to the authoritative decision notice rather than inventing rationale.

## Handoff
Pre-application likely eligibility belongs to `designing-service-eligibility-checkers`; changed facts after decision route to `designing-public-service-change-reporting`; case progression stays with `designing-public-service-status-tracking`.

## Output Contract
Return a `benefit-entitlement-explanations-contract` with `decision_identity`, `outcome_summary`, `effective_period`, `material_factors[]`, `calculation_reconciliation`, `judgement_boundary`, `correction_route`, `review_appeal_route`, `decision_revision_history`, `evidence_cases[]`, and `recovery_actions[]`.