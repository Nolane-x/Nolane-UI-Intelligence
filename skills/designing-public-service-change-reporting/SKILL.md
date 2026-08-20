---
name: designing-public-service-change-reporting
description: Use when people must report changed circumstances after applying for or receiving a public service and the interface must establish what changed, when it became effective, which case is affected, supporting evidence, and confirmation of impact processing.
---

# Designing Public Service Change Reporting

Reporting a change is not editing a profile. A changed address, income, household member, health status, employment, bank detail, or care circumstance can alter an existing case or entitlement from a specific effective date and may require reassessment.

## Parent Contract
**Required parent:** `designing-public-service-experiences`.

The parent owns the service relationship. This skill owns post-application change events, effective time, case binding, evidence, acknowledgement, and resulting reassessment status.

## Change Event Model
Represent a change as an event with type, old state where appropriate, new state, effective date, reporter, affected person/case, evidence requirements, and processing status. Avoid mutating the current profile first and trying to infer later what changed.

Different change types can have different policy consequences and deadlines. Ask only questions relevant to the selected change while explaining whether multiple simultaneous changes can be reported together. If one event affects several linked benefits/services, show which will be notified and which require separate action.

## Effective Date and History
Effective date often matters more than submission date. Make the distinction explicit and support corrections if the user entered the wrong date. Preserve prior state and earlier change reports so reassessment can be audited. Do not overwrite an existing address/income record without keeping the event history when the service requires it.

## Confirmation and Impact
After submission, confirm the reported facts, case/reference, date received, and what happens next. Distinguish “change received” from “entitlement recalculated.” If immediate recalculation is available, bind it to an authoritative decision revision; otherwise expose pending reassessment and any interim obligations.

## Evidence
Test future-dated and backdated changes, multiple simultaneous changes, corrected change report, evidence-required change, report affecting several cases, failed submission, duplicate retry, and a change made while another reassessment is pending. Verify event history and downstream case state.

## Failure Modes
- The UI edits profile fields without creating a traceable change event.
- Submission date is silently used as effective date.
- Users cannot tell which service/case received the change.
- “Change submitted” looks like a confirmed new award amount.
- Duplicate retries create multiple conflicting change events.
- A correction deletes the original reported event.
- Cross-service impact is implied without authoritative routing evidence.

## Falsification
Report a backdated change, interrupt submission, retry, and then correct the effective date. Falsify if the system creates duplicate events, loses the original history, or displays a recalculated entitlement before the decision engine/caseworker confirms it.

## Recovery
Bind changes to stable event IDs, preserve original and corrected revisions, distinguish receipt from reassessment, and show affected cases explicitly. If cross-service propagation is uncertain, tell the user which services still require separate reporting.

## Handoff
Evidence collection goes to `designing-service-evidence-upload`; decision explanation after reassessment to `designing-benefit-entitlement-explanations`; progress and outstanding action to `designing-public-service-status-tracking`.

## Output Contract
Return a `public-service-change-reporting-contract` with `change_event_schema`, `effective_date_rules`, `affected_case_mapping`, `multi_change_policy`, `evidence_requirements`, `submission_idempotency`, `reassessment_states[]`, `correction_history`, `evidence_cases[]`, and `recovery_actions[]`.