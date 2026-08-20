---
name: designing-clinical-care-workflows
description: Use when a clinical product coordinates patient care across encounters, orders, medications, results, documentation, imaging, handoffs, and alerts where context mistakes can create safety risk.
---

# Designing Clinical Care Workflows

Clinical UI is a safety-bearing coordination system. It must preserve who the patient is, which encounter and care setting are active, what has been ordered or observed, who is accountable, and what remains unresolved across every transition.

## Parent Contract
**Required parent:** `designing-high-stakes-decisions`.

Inherit consequence-aware decision design, explicit uncertainty, and evidence gating. This skill specializes those obligations for longitudinal care where the same patient can have multiple encounters, orders, result states, medication histories, and responsible teams at once.

## Care Context Model
Declare the clinical context tuple that material actions depend on: patient identity, encounter/episode, location or care setting, responsible team, authoring clinician, effective time, and relevant status. Do not assume the visible chart header alone proves that every modal, side panel, or embedded viewer is bound to the same context.

Separate observations, orders, plans, and completed actions. A medication proposed in a draft note is not an active medication order; a result acknowledged by one clinician is not necessarily resolved for the care team. The interface should represent lifecycle and responsibility rather than flattening clinical events into a chronological feed.

Longitudinal history needs temporal semantics. Distinguish event time, documentation time, order time, specimen time, result time, and correction time where relevant. When data arrive late or are corrected, avoid reordering the record in ways that hide the provenance of the change.

Cross-module transitions must carry a bounded context contract. Moving from a result to an order, from an image to a note, or from handoff summary to problem list should preserve patient and encounter identity and disclose any change in scope. High-risk actions should reassert the context immediately before commit.

## Safety Evidence
Evidence must include wrong-patient resistance, encounter switching, stale tab/window behavior, corrected data, concurrent updates, cancelled orders, unresolved alerts, and partial service outages. Verify both rendered labels and backend-bound identifiers for consequential actions. A clinician correctly reading a banner is not evidence if the submit request references another patient or encounter.

Test representative care sequences rather than isolated screens: review abnormal result → inspect history → place follow-up order → document reasoning → hand off unresolved item. The evidence chain should show which state changed at each step and how accountability remained visible.

## Failure Classes
- Patient or encounter context drifts across modules.
- Draft, ordered, performed, resulted, acknowledged, and resolved states collapse into generic “done.”
- Corrected or late data overwrite historical meaning without provenance.
- Responsibility disappears after a handoff or service transition.
- A stale browser state permits action against superseded clinical data.
- Alert dismissal is mistaken for clinical resolution.

## Falsification
Open two patient charts and two encounters in alternating tabs. Perform a sequence that traverses results, orders, notes, and imaging. The workflow is falsified if any consequential action can be committed without an unambiguous patient/encounter binding, if state transitions cannot be reconstructed afterward, or if a correction erases the prior clinical fact without trace.

## Recovery
Stop the workflow at the context boundary, reload authoritative patient/encounter state, surface conflicting revisions, and require re-review before commit when clinically material data changed. Preserve failed drafts and reasoning without silently resubmitting. Unknown clinical state remains BLOCKED until verified.

## Handoff
Route patient identity to `designing-patient-identity-banners`, medications to medication specialists, diagnostic results to result specialists, imaging to radiology/measurement specialists, documentation to `designing-clinical-note-signing`, and interruption policy to `designing-clinical-alert-fatigue-controls`.

## Output Contract
Return a `clinical-care-workflows-contract` with `clinical_context_tuple`, `event_state_model`, `temporal_semantics`, `cross_module_handoffs[]`, `accountability_model`, `high_risk_reassertions[]`, `concurrency_rules`, `safety_evidence[]`, `falsification_cases[]`, and `recovery_actions[]`.