---
name: designing-clinical-handoff-summaries
description: Use when responsibility for patient care transfers between clinicians, teams, shifts, units, or settings and the interface must surface active problems, pending work, contingency plans, and accountability without creating a stale shadow chart.
---

# Designing Clinical Handoff Summaries

A handoff summary is a responsibility-transfer artifact, not a miniature electronic record. It should expose what the receiving clinician must know and do, while preserving links to authoritative source data and making staleness visible.

## Parent Contract
**Required parent:** `designing-clinical-care-workflows`.

The parent owns longitudinal care coordination. This skill owns the bounded summary used when clinical responsibility changes hands.

## Handoff Content Model
Separate stable context from active work. Stable context may include patient identity, care setting, major active problems, allergies or precautions when policy requires. Active work includes pending orders/results, unresolved medication discrepancies, expected events, contingency plans, tasks, escalation conditions, and named responsibility.

Do not duplicate large portions of the chart into editable free text. When a field can be linked to a governed source, show the current source state and optionally the handoff author's interpretation. Preserve the distinction so the summary cannot silently become a competing system of record.

## Accountability
Every actionable handoff item should identify owner or receiving role, expected time/condition, status, and what counts as completion. “Follow labs” is weak; a handoff should make clear which result, when expected, what state remains pending, and who is watching it. If ownership is unassigned, treat that as a visible risk state.

Acknowledgement of a handoff means receipt, not completion of all items. Track acceptance separately from task resolution. For shift changes, record when responsibility transferred and which items remained open at that boundary.

## Freshness and Change
A handoff can stale quickly. Bind source-derived items to timestamps/revisions and flag material changes after the summary was authored. Avoid presenting old copied values as current. If a result arrives or an order is cancelled, update the linked state while retaining what the sender knew at handoff time when audit is important.

## Evidence
Simulate a shift handoff with pending imaging, abnormal lab follow-up, medication discrepancy, and contingency instruction. Change one source item after the handoff and verify the receiver can distinguish authored statement from current state. Test partial acceptance, unassigned item, patient transfer, and unavailable source module.

## Failure Modes
- Handoff text becomes a stale duplicate of the chart.
- Receipt is shown as task completion.
- Pending work lacks owner or expected condition.
- Source updates silently rewrite what the sender originally communicated.
- Important uncertainty is summarized into false certainty.
- The summary includes every chart detail and buries actionable risk.

## Falsification
Give the receiver a summary containing one stale source-derived value and one unresolved task with no owner. Falsify if the UI makes the stale value look current or permits the handoff to appear fully safe despite unassigned responsibility.

## Recovery
Restore links to authoritative source items, label authored interpretation separately, expose freshness and revision deltas, and require ownership for material pending work according to policy. If the source cannot be reached, mark that evidence unavailable instead of freezing an old value without warning.

## Handoff
Pending order state uses `designing-clinical-order-status`; medication discrepancies use `designing-medication-reconciliation`; results use lab/abnormality owners; this skill synthesizes responsibility transfer without taking over their domain logic.

## Output Contract
Return a `clinical-handoff-summaries-contract` with `stable_context`, `active_work_items[]`, `source_links[]`, `authored_interpretation_boundary`, `responsibility_fields`, `receipt_vs_resolution`, `freshness_rules`, `change_after_handoff_behavior`, `evidence_cases[]`, and `recovery_actions[]`.