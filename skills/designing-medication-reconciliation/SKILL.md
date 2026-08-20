---
name: designing-medication-reconciliation
description: Use when clinicians compare medication lists across sources or transitions of care and must resolve continuation, discontinuation, duplication, uncertainty, and source disagreement without losing provenance.
---

# Designing Medication Reconciliation

Medication reconciliation is comparison under uncertainty. The interface must help clinicians determine what the patient was taking, what is currently ordered, what should continue, and why discrepancies exist across source lists.

## Parent Contract
**Required parent:** `designing-clinical-care-workflows`.

The parent establishes patient/encounter context. This skill owns side-by-side or structured reconciliation among medication sources and the resulting resolution record.

## Source-Aware Medication State
Each medication claim needs provenance: patient-reported, pharmacy/imported, prior encounter, active inpatient order, external record, clinician-entered history, or another authoritative source. Do not merge identical-looking medications before preserving source, status, timing, and confidence.

Normalize enough to compare medication concept, formulation, dose, unit, route, frequency, and schedule while retaining the raw source expression for audit. Similarity should produce a candidate match, not automatic equivalence. “Metoprolol 50 mg daily” and an order with different formulation or schedule may be clinically distinct.

## Discrepancy Decisions
Model outcomes such as continue, stop, replace, hold, unable to verify, duplicate, changed dose, changed frequency, and not currently taking. Require rationale according to policy for clinically material changes. Avoid a single checkbox that simultaneously confirms history and generates a new order without making that effect explicit.

Reconciliation should account for transitions: admission, transfer, discharge, and specialist handoff may have different target lists. The interface must state which list will become authoritative after completion and what downstream orders or discharge instructions will be created.

## Uncertainty and Completion
A reconciliation can be incomplete. Missing patient history, unavailable external source, or uncertain dose should remain visible as unresolved rather than forcing all rows into resolved states to unlock a “complete” button. Completion claims need explicit coverage boundaries.

## Evidence
Use datasets containing duplicates, conflicting doses, inactive historical medications, PRN versus scheduled use, patient-reported supplements, unknown strength, external-source delays, and a medication intentionally held. Verify the resulting medication list and generated orders against each row's decision and provenance.

Test interrupted reconciliation, partial save, second clinician review, and data arriving after the process began.

## Failure Modes
- Source lists are merged so provenance disappears.
- Similar medication names are automatically treated as the same therapy.
- “Continue” generates an order without showing that consequence.
- Unverified medications are forced into active/inactive binary states.
- Late external data silently alters a completed reconciliation.
- Completion badge implies full coverage despite unavailable sources.

## Falsification
Give reviewers two sources with one subtle formulation mismatch and one unknown-dose medication. Falsify if the UI encourages blind matching, requires false certainty to finish, or cannot show how each resolution changed the target list.

## Recovery
Restore source-level rows, mark candidate matches rather than confirmed equivalence, preserve unresolved states, and make downstream order effects previewable. If new source data arrive, create a review delta instead of silently rewriting the reconciliation result.

## Handoff
New medication ordering goes to `designing-medication-order-entry`; handoff summaries may surface unresolved discrepancies through `designing-clinical-handoff-summaries`; order lifecycle states belong to `designing-clinical-order-status`.

## Output Contract
Return a `medication-reconciliation-contract` with `source_types[]`, `normalized_comparison_fields`, `candidate_match_rules`, `discrepancy_outcomes[]`, `downstream_effects`, `unresolved_state_model`, `completion_boundary`, `late_data_policy`, `evidence_cases[]`, and `recovery_actions[]`.