---
name: designing-public-service-status-tracking
description: Use when applicants need to follow a public-service case after submission and distinguish receipt, evidence review, human assessment, decision, payment or fulfillment, outstanding actions, delays, and completed outcomes.
---

# Designing Public Service Status Tracking

Service status should explain what is happening to a case and what, if anything, the person must do. A linear progress tracker is misleading when public-service processing includes parallel evidence checks, human review, external dependencies, and decisions that may reopen work.

## Parent Contract
**Required parent:** `designing-public-service-experiences`.

The parent owns the end-to-end service. This skill owns the post-submission status model, milestones, outstanding user actions, expected timing, and delay/recovery communication.

## Status Model
Derive user-facing statuses from authoritative case states, but translate internal workflow codes into meaningful outcomes. Distinguish received, awaiting evidence, evidence received, under review, waiting on another organization, decision made, fulfillment/payment in progress, completed, paused, withdrawn, and unable-to-progress where relevant.

Do not use “in progress” as a catch-all. The user should know whether the service is actively reviewing the case, waiting on them, or waiting on an external dependency. When exact timing is not known, show a bounded expectation or explain the source of uncertainty rather than inventing a date.

## Outstanding Actions
Place required user action ahead of passive milestones. Each action should state what is needed, due date if authoritative, how to complete it, and consequence of not acting. A green timeline with a small hidden evidence request is a serious failure.

## History and Decisions
Preserve a history of material status changes, messages, evidence requests, and decisions. If a status regresses because new information reopened assessment, explain the transition instead of making the tracker jump backward without reason. Decision details should link to entitlement/refusal explanation and review/appeal routes where applicable.

## Evidence
Simulate submission, evidence request, upload, external dependency delay, decision, fulfillment, and a reopened case. Verify the same case identifier and authoritative timestamps throughout. Test notification links, stale cached status, revoked/changed identity credentials, and users with multiple simultaneous applications.

## Failure Modes
- A linear tracker implies processing sequence that does not exist.
- “In progress” hides that the service is waiting on the applicant.
- Estimated completion date is presented as a guarantee.
- New evidence request is visually secondary to decorative milestones.
- Reopened assessment looks like data corruption.
- Users with multiple cases cannot tell which status they are viewing.
- Browser cache shows old status after a decision changed.

## Falsification
Create a case that is waiting on the applicant and another waiting on an external agency but map both to the same internal broad state. Falsify if the UI cannot express the operational difference or does not surface the applicant's required action.

## Recovery
Map internal states to user-meaningful reasons, elevate outstanding actions, bind status to fresh case evidence, and preserve transition history. If timing is uncertain, communicate the uncertainty and next checkpoint rather than promising a fictional completion date.

## Handoff
Decision reasoning routes to `designing-benefit-entitlement-explanations`; new evidence to `designing-service-evidence-upload`; post-decision circumstance changes to `designing-public-service-change-reporting`.

## Output Contract
Return a `public-service-status-tracking-contract` with `user_status_states[]`, `case_identity`, `outstanding_actions[]`, `timing_semantics`, `dependency_states[]`, `status_history`, `reopen_rules`, `freshness_evidence`, `falsification_cases[]`, and `recovery_actions[]`.