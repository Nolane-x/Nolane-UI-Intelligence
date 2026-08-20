---
name: designing-government-application-journeys
description: Use when a government or civic service collects structured information over a multi-step application and must preserve progress, legal declarations, conditional sections, review, submission identity, and procedural clarity.
---

# Designing Government Application Journeys

A government application is a case-creation workflow. Good step design matters, but the deeper contract is that the applicant understands what they are applying for, what information is required, what has been saved, and what legal or procedural effect submission has.

## Parent Contract
**Required parent:** `designing-public-service-experiences`.

The parent owns the service outcome and policy context. This skill owns sequencing, section status, conditional content, review, declaration, and submission of a formal application.

## Application Structure
Organize by user-understandable topics rather than internal database tables. Separate applicant details, circumstances, evidence, declarations, and optional information according to the service. Conditional sections should be derived from explicit answers and remain inspectable from a review page so users can see why certain topics were or were not requested.

Progress should describe completed sections and remaining work, not promise an inaccurate percentage when branch length varies. A section can be “complete for now” while still subject to validation or evidence review; name that distinction if it matters.

## Save, Review, Submit
Persist answers at stable boundaries and expose save state. Before final submission, provide a review that groups answers meaningfully and offers targeted change links. Changing an answer should return the user to a coherent review state, not restart the journey or leave incompatible dependent data hidden.

Legal declarations, consent, and truthfulness statements belong close to submission and must be distinguishable from ordinary terms or informational text. The submit action should create one authoritative application/case identity and be protected against duplicate submission on retry.

## After Submission
Immediately show confirmed receipt state, reference identifier, what happens next, expected timing if authoritative, outstanding evidence/actions, and how to correct or report changes. “Application submitted” must not be visually conflated with benefit/service approval.

## Evidence
Test short and long branches, missing required information, dependent answer changes, saved return, session expiry, multi-device return if supported, failed submission after network timeout, duplicate click/retry, and change from review page. Verify server case identity and rendered confirmation.

## Failure Modes
- Progress percentage is misleading because conditional sections vary widely.
- Changing an upstream answer leaves incompatible hidden answers in the submitted payload.
- Review page hides conditional sections the user never encountered.
- Declaration is buried among generic checkboxes.
- Submission retry creates two cases.
- Confirmation omits the case/reference identity.
- A technical save failure is shown as if progress is safely stored.

## Falsification
Complete a branch, return to review, alter an upstream condition that should remove a later section, and submit after a simulated timeout. Falsify if stale hidden data remain, if the user cannot tell whether submission succeeded, or if retries create duplicate cases.

## Recovery
Recompute branch validity, explicitly remove or archive dependent answers, preserve a recoverable draft, and confirm submission against the authoritative case record before offering retry. If receipt state is uncertain, query by idempotency/application token rather than asking the user to resubmit blindly.

## Handoff
Evidence collection goes to `designing-service-evidence-upload`; long-lived draft identity to `designing-save-and-return-service-flows`; identity assurance to `designing-identity-proofing-service-flows`; status after submission to `designing-public-service-status-tracking`.

## Output Contract
Return a `government-application-journeys-contract` with `sections[]`, `branch_dependencies`, `progress_model`, `save_boundaries`, `review_model`, `declaration_requirements`, `submission_idempotency`, `confirmation_state`, `evidence_cases[]`, `falsification_cases[]`, and `recovery_actions[]`.