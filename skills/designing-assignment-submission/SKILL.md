---
name: designing-assignment-submission
description: Use when this specialist's decision ownership is materially in scope. Own learner assignment submission across draft files/text, requirements, deadline, versioning, upload state, final submit, late policy, receipt, resubmission, and instructor-visible artifact identity.
---
# Designing Assignment Submission

## Parent Contract

**Required parent:** `designing-digital-learning-experiences`.

Inherit the broader routing and decision boundary from this canonical parent; this specialist remains accountable only for the narrower ownership, failure topology, falsification criteria, and output contract defined below.

## Decision ownership

Own the lifecycle from preparing work to a durable submitted artifact. Decide draft versus submitted state, allowed artifact types, requirements, deadline/timezone, upload/save progress, final confirmation, receipt, late classification, resubmission/versioning, and withdrawal if allowed. Generic file upload does not own academic submission consequence.

## Inputs and evidence

Require assignment identity/version, instructions/requirements, allowed files/text/links, size/type limits, deadline/timezone, late policy, attempts/resubmission, draft autosave, plagiarism/integrity processing disclosure, grading workflow, and accessibility. Identify large file or flaky network cases.

## Procedure

Keep draft work separate from final submission. Show deadline and effective timezone, plus current late/on-time consequence before submit. Uploads must complete/verify before final submission; pending files cannot be represented as attached successfully. Final submit summarizes exact artifacts/text and locks or versions them according to policy, then returns a server-confirmed receipt with timestamp. Resubmission creates a new version while preserving earlier submissions and clearly states which version will be graded. If withdrawal is allowed, preserve history and policy consequence.

## Failure topology

Failures include upload thumbnail shown before bytes are complete, draft mistaken for submitted, submit race with pending file, timezone surprise, resubmission overwriting earlier artifact, receipt absent, and integrity processing undisclosed where policy requires notice. Another failure is a large file timing out exactly at deadline with no evidence of attempted upload/recovery.

## Falsification

Reject if learner cannot identify draft versus submitted; if final submit can include unverified upload; if deadline timezone is ambiguous; if no authoritative receipt/timestamp exists; if resubmission erases previous version; if instructor cannot trace graded artifact to submission version; or if upload failure recovery loses the draft state.

## Output contract

Return an `assignment-submission-contract` with: assignment/version; draft state; artifact requirements; upload/save states; deadline/timezone/late classification; final-submit summary; immutable submission version; receipt; resubmission/withdrawal; failure recovery; and grading linkage. Include one deadline-near upload failure.

## Handoffs

File uploaders handle byte transfer, rubric grading consumes submitted versions, gradebook consumes evaluation state, and academic integrity owns review findings rather than altering submission identity.