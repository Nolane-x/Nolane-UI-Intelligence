---
name: designing-problem-list-management
description: Use when clinicians maintain a longitudinal problem list and must distinguish active, resolved, historical, suspected, duplicate, and entered-in-error problems while preserving coding, onset, evidence, and authorship.
---

# Designing Problem List Management

A problem list is a longitudinal clinical model, not a tag collection. Every change affects how future clinicians understand the patient's history, what appears in summaries, and which workflows may be triggered downstream.

## Parent Contract
**Required parent:** `designing-clinical-care-workflows`.

The parent owns care context. This skill owns the lifecycle and editing semantics of longitudinal clinical problems across encounters.

## Problem Identity
Bind each problem to a coded concept where the system supports it, while preserving clinician-entered wording when it carries useful specificity. Distinguish diagnosis code, free-text qualifier, onset, verification status, clinical status, recorder, source, and related encounter. Avoid using the display label as the sole identity because terminology can evolve.

Model states according to the clinical system: active, inactive, resolved, recurrence, remission, suspected/provisional, ruled out, entered-in-error, or historical where supported. Do not force every local ontology into these exact names; the key is that lifecycle state and certainty are separate dimensions.

## Editing and Duplicate Handling
Adding a similar problem should surface existing candidates before creating another entry, but similarity must not automatically merge clinically distinct conditions. Present code, laterality/site, onset, and status differences needed to decide. Merging or marking duplicate must preserve provenance and not erase the original authoring history.

Resolution requires effective time and may require rationale. Reopening a resolved problem should create a traceable state transition rather than deleting the resolution. Entered-in-error is not the same as resolved; it indicates the record itself should not be treated as a valid clinical problem.

## Longitudinal Context
Problem lists span encounters, yet encounter-specific evidence can justify changes. Show enough source context to understand why a state changed without turning the list into a full note viewer. If the product imports problems from external records, distinguish local adoption from merely observed external claims.

## Evidence
Test same-name problems with different codes, suspected versus confirmed states, resolution and recurrence, duplicate candidate handling, erroneous entry correction, external imported problems, and terminology display updates. Verify historical audit records after each edit.

Include concurrent edits and permission differences between viewers who can read versus curate the list.

## Failure Modes
- “Delete” removes a clinically meaningful history instead of recording entered-in-error.
- Resolved and ruled-out are visually equivalent.
- Similarity matching silently merges distinct diagnoses.
- External problem claims appear as locally verified diagnoses.
- Reopening erases the prior resolution date.
- A terminology rename breaks links to the underlying coded concept.

## Falsification
Create two superficially similar problems that differ in code/site, resolve one, and later reactivate it. Falsify if the UI merges them, loses the prior lifecycle, or cannot show which clinician made each transition.

## Recovery
Restore stable concept identity and revision history, separate clinical status from verification/certainty, require deliberate merge decisions, and treat erroneous entries as auditable corrections. If provenance is missing, display the uncertainty rather than attributing the problem to the current encounter.

## Handoff
Encounter-scoped evidence belongs to `designing-clinical-encounter-context`; handoff summaries may reference active/unresolved problems through `designing-clinical-handoff-summaries`; note finalization remains with `designing-clinical-note-signing`.

## Output Contract
Return a `problem-list-management-contract` with `problem_identity_fields`, `clinical_status_states[]`, `verification_states[]`, `duplicate_review_rules`, `resolution_recurrence_model`, `error_correction_semantics`, `external_source_boundary`, `audit_evidence[]`, `falsification_cases[]`, and `recovery_actions[]`.