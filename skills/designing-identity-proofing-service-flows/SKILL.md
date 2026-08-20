---
name: designing-identity-proofing-service-flows
description: Use when a public service must establish that a person is who they claim to be at a required assurance level while providing understandable alternatives, failure recovery, privacy boundaries, and separation from general account login.
---

# Designing Identity Proofing Service Flows

Identity proofing is evidence-based assurance for a service decision. It is different from authentication: logging into an account proves control of credentials, while proofing establishes a governed relationship between a person and claimed identity attributes.

## Parent Contract
**Required parent:** `designing-public-service-experiences`.

The parent owns the service. This skill owns assurance-level choice, evidence steps, matching outcomes, alternative routes, and recovery when automated proofing cannot establish identity.

## Assurance Contract
State what level of assurance the service requires and why. Collect only evidence necessary for that assurance and service risk. A low-risk status check should not inherit the most intrusive proofing flow merely because the platform can request it.

Separate evidence acquisition, evidence validation, attribute matching, liveness or possession checks where used, and final assurance decision. A technically valid document can still fail matching; a failed automated match does not prove fraud. Use neutral language that distinguishes inability to verify from evidence of deception.

## Alternatives and Inclusion
Automated routes can exclude people without conventional documents, stable credit history, modern devices, addresses, or biometric capability. Provide policy-approved alternatives such as in-person, postal, knowledge/document review, assisted service, or lower-assurance route when possible. Do not present alternative proofing as a hidden exception reached only after repeated failure.

## Privacy and Device Safety
Explain sensitive capture before camera/document access. Minimize retention of raw evidence, avoid exposing document images in histories or shared contexts, and make abandonment/logout clear. Device capability failure should not be worded as identity failure.

## Evidence
Test successful proofing, document capture failure, valid document but mismatch, name variation, address change, inaccessible camera, unsupported device, user without standard evidence, manual review, session expiry, and return after partial completion. Verify server assurance state rather than relying on front-end progress.

## Failure Modes
- Authentication success is shown as identity-proofing success.
- Automated mismatch is worded as suspected fraud.
- High-assurance evidence is requested for a low-risk service without justification.
- Alternative proofing appears only after an inaccessible route fails repeatedly.
- Camera/device failure consumes proofing attempts.
- Sensitive document thumbnails persist after the session.
- Manual-review state is shown as generic “pending” with no expectation.

## Falsification
Use a user whose identity is legitimate but whose automated match fails due to a known data variation. Falsify if the design dead-ends or implies wrongdoing rather than routing to an alternative review. Then disable the camera; falsify if technical failure changes the person's identity-assurance status.

## Recovery
Reset technical failures without penalizing assurance, expose alternative routes early, preserve completed verified steps where policy permits, and separate “not verified yet” from “verification failed.” Escalate policy ambiguity instead of inventing acceptance criteria.

## Handoff
Account authentication uses `designing-authentication-and-passkeys`; assisted completion routes to `designing-assisted-digital-handoffs`; document evidence capture coordinates with `designing-service-evidence-upload` but identity proofing remains a distinct assurance decision.

## Output Contract
Return an `identity-proofing-service-flows-contract` with `required_assurance`, `proofing_steps[]`, `evidence_types[]`, `matching_states`, `technical_failure_boundary`, `alternative_routes[]`, `privacy_retention`, `manual_review_state`, `evidence_cases[]`, and `recovery_actions[]`.