---
name: designing-clinical-encounter-context
description: Use when a patient's record contains multiple encounters, episodes, locations, or care settings and clinical actions must be explicitly bound to the correct active context.
---

# Designing Clinical Encounter Context

Patient identity answers who. Encounter context answers which episode of care. Confusing the two can place an otherwise correct order, note, or result acknowledgment into the wrong hospitalization, visit, or service context.

## Parent Contract
**Required parent:** `designing-clinical-care-workflows`.

The parent owns the cross-clinical workflow. This skill owns encounter selection, visibility, transitions, and binding for actions whose meaning depends on episode, location, service, or care setting.

## Encounter Model
Represent encounter identity with more than a human label. Maintain stable identifiers plus clinically meaningful descriptors: visit type, admission/discharge state, service, location, attending/responsible team, start/end time, and episode relationship when available. Avoid using “current” as a permanent property; currentness is relative to user intent and system time.

Different modules may legitimately use different context scopes. A longitudinal problem list spans encounters, while an inpatient medication order may require the active admission. Make the scope visible so clinicians can tell whether they are reviewing lifetime history, this admission, this visit, or a specific procedure encounter.

## Transition Rules
When a user changes encounters, decide which selections reset, which data re-query, which drafts stay bound to their original encounter, and which panels must close. Do not carry a draft order into a new encounter merely because the patient did not change. If a note is intentionally cross-encounter, state that explicitly and preserve provenance.

Encounter state can change server-side: discharge, transfer, merge, cancellation, or corrected visit classification. Revalidate before consequential commit when a stale encounter could invalidate the action. Show a meaningful blocked state instead of converting every mismatch into a generic network error.

## Temporal Orientation
Past and future encounters need clear visual treatment. When reviewing historical records, avoid placing current-action controls adjacent to old encounter data without a context cue. A clinician should not need to infer from timestamps alone that they are charting into a closed visit.

## Evidence
Test admitted, discharged, transferred, outpatient, emergency, historical, and future scheduled encounters. Open one patient with multiple overlapping episodes, then navigate longitudinal history while placing an encounter-bound action. Verify action payload, audit record, and displayed context agree.

Test direct links into an old encounter, browser refresh, duplicate tabs, server-side discharge while the screen is open, and insufficient permission for a specific encounter.

## Failure Modes
- Patient banner remains correct while encounter binding silently changes.
- Longitudinal view makes an encounter-specific action appear global.
- A discharged encounter still accepts a new active order without review.
- Switching encounter keeps a stale draft bound to the wrong episode.
- Location transfer is mistaken for a new encounter or vice versa.
- Direct link resolves to “latest encounter” instead of the referenced one.

## Falsification
Open a historical encounter, navigate to a longitudinal module, then initiate an encounter-bound order. Falsify if the user cannot predict which encounter receives the action or if the system silently redirects to another encounter without disclosure.

## Recovery
Lock the action to an explicit encounter identifier, surface scope in the action surface, revalidate encounter state, and require deliberate rebinding when context changes. Preserve drafts with their original encounter metadata so recovery cannot attach them accidentally to a new episode.

## Handoff
Patient-level identity stays with `designing-patient-identity-banners`; order lifecycle belongs to `designing-clinical-order-status`; note finalization belongs to `designing-clinical-note-signing`.

## Output Contract
Return a `clinical-encounter-context-contract` with `encounter_identity_fields`, `scope_classes[]`, `module_scope_map`, `transition_rules`, `draft_binding_policy`, `server_state_revalidation`, `historical_context_treatment`, `evidence_cases[]`, `falsification_cases[]`, and `recovery_actions[]`.