---
name: designing-medication-order-entry
description: Use when clinicians create medication orders and the interface must make drug, dose, route, frequency, timing, indication, duration, patient context, and safety constraints reviewable before commit.
---

# Designing Medication Order Entry

Medication entry is a structured prescribing decision, not a generic form. The interface must make clinically material parameters explicit, preserve terminology identity, and distinguish hard safety constraints from advisory guidance.

## Parent Contract
**Required parent:** `designing-clinical-care-workflows`.

The parent owns patient/encounter safety context. This skill owns the construction and review of a medication order before it enters the clinical order lifecycle.

## Medication Identity
Bind selection to a coded medication/concept and formulation rather than free-text display name alone. Make strength, form, and route compatibility visible during selection. Similar names and multiple strengths require disambiguation before the user reaches the final review state.

Structure the prescription into dose quantity, dose unit, route, frequency/timing, start, duration or stop condition, indication, and special instructions as required by the care setting. Defaults may reduce effort, but every default must have provenance and must remain visibly reviewable. Never let a preselected value hide because the field was auto-completed.

## Calculated and Conditional Dosing
Weight-based, renal, age, body-surface-area, infusion, and taper regimens require transparent calculation inputs and units. Show the source and timestamp of patient measurements used in the calculation when clinically material. If a required input is stale, missing, or ambiguous, block or escalate according to clinical policy rather than guessing.

Dose range checks, allergy checks, duplicate therapy, interaction warnings, and formulary constraints have different authority. Do not render every signal as the same red modal. High-severity blockers should be visually and behaviorally distinct from low-value advisories to reduce alert fatigue.

## Review Before Commit
Provide a concise prescription sentence or structured review that lets the prescriber verify patient, medication, strength/form, dose/unit, route, timing, duration, and indication. A final submit action should bind to the current order draft revision; if the underlying medication concept or patient context changed, require re-review.

## Evidence
Test look-alike medication names, multiple strengths, unusual units, decimal doses, pediatric/weight-based calculation, unavailable route, allergy alert, duplicate therapy, stale weight, and encounter change. Verify generated order payload against the rendered review summary.

Include keyboard-only entry, rapid repeated orders, and recovery from failed submission without duplicated order creation.

## Failure Modes
- Drug display name hides formulation or strength ambiguity.
- Dose unit changes after numeric entry without re-review.
- A default is silently committed because the field never appeared touched.
- Calculated dose lacks source measurement/time.
- Advisory and hard-stop alerts are visually indistinguishable.
- Submission retry creates duplicate medication orders.
- Patient/encounter switch leaves the draft active.

## Falsification
Prepare an order with a deliberately stale weight and then alter the patient context before submit. Falsify if the interface still allows silent commit, if the summary omits the calculated-dose provenance, or if the payload differs from what the prescriber reviewed.

## Recovery
Invalidate calculations whose inputs changed, preserve the draft, rebind to authoritative patient/encounter state only with deliberate user action, and require a new review step. For ambiguous medication identity or units, stop entry until the coded concept is resolved.

## Handoff
Medication history and discrepancies go to `designing-medication-reconciliation`; downstream lifecycle state goes to `designing-clinical-order-status`; interruption strategy for warnings coordinates with `designing-clinical-alert-fatigue-controls`.

## Output Contract
Return a `medication-order-entry-contract` with `medication_identity_model`, `prescription_fields[]`, `default_provenance`, `calculation_inputs[]`, `safety_signal_classes`, `review_summary`, `submission_idempotency`, `context_revalidation`, `evidence_cases[]`, and `recovery_actions[]`.