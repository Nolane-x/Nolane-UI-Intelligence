---
name: designing-review-feedback-workflows
description: Use when work moves through a structured feedback cycle and reviewers need to request changes, discuss findings, track addressed items, and hand the artifact back without conflating review with formal approval.
---

# Designing Review Feedback Workflows

## Parent Contract
**Required parent:** `designing-task-flows`.

This faculty owns the lifecycle of structured review feedback around a work artifact. It does not own multi-stage approval authority from Batch 001. A review may produce comments and change requests without granting or denying a formal release decision; the interface must preserve that distinction.

## Decision Architecture
Define review states from the collaboration process: not requested, requested, in review, feedback submitted, changes requested, author responding, ready for re-review, closed, or superseded by a newer revision. Do not use a single “Reviewed” state when unresolved findings still exist.

Feedback units need stable identity and disposition. A reviewer may raise a finding, the author may address it through a change, explain why no change is needed, or ask for clarification. “Resolve” should identify who can declare closure and whether reopening is possible. When a new revision invalidates prior feedback, mark findings as outdated/superseded rather than silently hiding them.

Review requests require scope: artifact/version, reviewers, due expectations if any, and what counts as completion. Parallel reviewers may disagree. Preserve each reviewer’s evidence instead of collapsing the first response into a global pass/fail. If formal approval follows review, hand off an explicit review summary rather than treating resolved comments as approval proof.

## Failure Topology
- All comments are resolved, so the product automatically marks the artifact approved even though no approver acted.
- Reviewer submits change requests against revision 3, then revision 4 appears and feedback remains visually attached as if current.
- Author can resolve every reviewer finding unilaterally even when policy requires reviewer confirmation.
- Two reviewers disagree but the interface reduces them to one green “review complete” state.
- Re-review starts with no indication which prior findings changed or remain open.
- Notification says “Review requested” but opens the latest artifact instead of the exact requested version.

## Falsification and Recovery
Falsify with parallel reviewers, reviewer removal, new artifact revision during review, reopened findings, author response without code/content change, formal approval following review, overdue review, permission revocation, and keyboard/screen-reader traversal of unresolved items. The design fails if review completion can be mistaken for approval or if feedback cannot be bound to the revision it evaluated.

Recover by version-binding review sessions, keeping reviewer-specific outcomes, defining finding disposition authority, marking superseded evidence, generating a structured handoff summary, and routing formal release decisions to approval owners.

## Output Contract
Return `review-feedback-workflow-contract` with review-session identity, version scope, reviewer set, lifecycle states, finding dispositions, resolution authority, re-review mechanics, disagreement representation, supersession behavior, approval handoff, accessibility navigation, and falsification cases.