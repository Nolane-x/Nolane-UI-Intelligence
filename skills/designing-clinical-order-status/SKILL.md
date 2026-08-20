---
name: designing-clinical-order-status
description: Use when clinical orders move through draft, signed, transmitted, accepted, scheduled, performed, resulted, cancelled, discontinued, or failed states and users need exact lifecycle and responsibility rather than a generic completion badge.
---

# Designing Clinical Order Status

Clinical order status is a workflow contract across people and systems. “Ordered,” “in progress,” and “done” are too coarse when a laboratory, imaging, medication, referral, or procedure order may be signed, transmitted, accepted, scheduled, collected, performed, resulted, corrected, cancelled, or rejected at different times.

## Parent Contract
**Required parent:** `designing-clinical-care-workflows`.

The parent owns the care workflow and clinical context. This skill owns the state machine, status evidence, transition visibility, responsibility, and recovery behavior for clinical orders after or around commit.

## State Machine
Define order states from actual backend and operational semantics rather than inventing UI-only labels. Separate authoring state from execution state. A signed medication order may be active immediately, while a diagnostic order may still await transmission or scheduling. If multiple systems contribute state, preserve source and timestamp for each transition.

Distinguish terminal from reversible states. Cancelled, discontinued, expired, completed, and entered-in-error have different meanings and audit consequences. Avoid a single “closed” label when downstream care depends on why the order stopped.

State should expose actor/responsibility where clinically material: who placed the order, who owns the next step, which service accepted it, and whether a result or follow-up is pending. If responsibility is unknown, state that explicitly rather than implying ownership from department labels.

## Pending and Failure Semantics
Transmission failure, scheduling delay, specimen not collected, patient no-show, rejected order, and technical result failure are operationally distinct. Surface the failure nearest the blocked transition and provide recovery aligned with clinical policy. Retrying must be idempotent or clearly create a replacement order with lineage to the original.

A result arriving does not automatically mean the care workflow is resolved. Keep result status, acknowledgement, and follow-up separate from execution completion.

## Evidence
Create orders that succeed, fail before transmission, are accepted then cancelled, are replaced, are performed without result, receive corrected result, and become stale while the user remains on screen. Verify every status against authoritative event history and rendered labels. Include concurrent changes from another clinician or service.

## Failure Modes
- A generic spinner represents several clinically distinct pending states.
- “Completed” is shown before result or required follow-up exists.
- Cancel and discontinue are conflated.
- Transmission failure looks like a successful signed order.
- Retry creates an unlinked duplicate.
- Status changes without showing who or what system changed it.
- Old cached state permits an action that is no longer valid.

## Falsification
Simulate an order that is signed locally but rejected downstream. Falsify if the clinician sees only “ordered” or if recovery produces a duplicate without lineage. Then cancel an accepted order from another session; falsify if the stale page continues to present incompatible controls.

## Recovery
Reload authoritative event history, transition the UI into a conflict-aware state, preserve the original order identifier and audit trail, and require deliberate replacement when needed. Do not collapse an unknown downstream response into success.

## Handoff
Order construction belongs to `designing-medication-order-entry` or the relevant domain owner; diagnostic result interpretation routes to result specialists; unresolved transitions may appear in `designing-clinical-handoff-summaries`.

## Output Contract
Return a `clinical-order-status-contract` with `order_states[]`, `transition_sources[]`, `terminal_state_semantics`, `responsibility_model`, `pending_failure_states[]`, `idempotency_or_replacement_rules`, `result_followup_boundary`, `evidence_cases[]`, `falsification_cases[]`, and `recovery_actions[]`.