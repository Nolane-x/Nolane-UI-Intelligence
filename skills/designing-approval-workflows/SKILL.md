---
name: designing-approval-workflows
description: Use when an action or artifact requires one or more authorized decisions before taking effect and the interface must represent pending, approved, rejected, changes-requested, withdrawn and expired states with clear authority.
---

# Designing Approval Workflows

## Parent Contract
**Required parent:** `designing-task-flows`.

This faculty owns the approval decision lifecycle around a request. It does not define the organization’s policy for who is an approver or orchestrate complex multi-stage dependency graphs handled by `designing-multi-stage-approval`.

## Decision Boundary
Model approval as a stateful request bound to an exact subject revision and decision authority. Common states include draft, submitted, pending, approved, rejected, changes requested, withdrawn, expired and superseded. If the subject changes materially after submission, define whether approval is invalidated, partially retained or requires resubmission. Never display “Approved” for a version that was not actually reviewed.

Approvers need enough evidence to decide: subject summary, changed fields/diff, requester, rationale, policy context, conflicts, attachments and prior decisions where material. The UI should distinguish an approver’s **ability to decide** from their identity as a viewer; unauthorized users can inspect history without seeing active approve controls.

Decision actions require consequence clarity. “Reject” and “Request changes” are not synonyms: rejection may terminate the request, while changes requested can reopen editing and resubmission. Comments/rationale may be optional or mandatory by policy; the interface should enforce that policy without inventing it.

Withdrawal, expiration and delegation need temporal truth. A late approval after the request expired or was superseded must not resurrect obsolete state.

## Failure Topology
- Approved badge survives after the requester edits the approved amount.
- Users cannot tell whether “Reject” ends the workflow or returns it for revision.
- Approve button is visible to someone whose permission was revoked seconds earlier.
- A request expires but an open browser tab still allows stale approval.
- Decision history shows names but not which revision they reviewed.
- “Changes requested” removes prior rationale and the requester cannot tell what to fix.

## Falsification and Recovery
Falsify with edit-after-submit, permission revocation, withdrawal, expiration, resubmission, duplicate browser tabs and stale decisions. Bind every approval event to subject revision and policy snapshot where applicable. Any approval that can attach to the wrong version fails.

Recover by revision-binding requests, rechecking authorization at action time, separating reject/change-request states and invalidating stale decision controls immediately.

## Output Contract
Return `approval-workflow-contract` with subject/version identity, state machine, decision authority handoff, evidence packet, approve/reject/change/withdraw semantics, stale/expiry handling, rationale/history and revision-integrity tests.