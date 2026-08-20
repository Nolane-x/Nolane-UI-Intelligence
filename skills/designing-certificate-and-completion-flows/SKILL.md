---
name: designing-certificate-and-completion-flows
description: Own course/program completion verification and credential issuance, including requirement proof, pending states, identity, name corrections, issuance, download/share, revocation, expiry, and verification links.
---
# Designing Certificate and Completion Flows

## Decision ownership

Own the boundary from satisfying educational requirements to issuing a completion record or credential. Decide eligibility check, pending grading, manual review, learner identity/name, issue date, credential ID, expiry if any, corrections, revocation, download/share, and third-party verification. A celebratory UI cannot substitute for canonical completion evidence.

## Inputs and evidence

Require course/program identity/version, completion requirements, grade/mastery thresholds, pending evaluations, learner identity, credential template, issuer, credential ID scheme, issue/expiry policy, verification endpoint, revocation/correction process, and privacy. Identify credentials requiring manual or external approval.

## Procedure

Evaluate eligibility from canonical curriculum/progress/grade state and show unmet or pending requirements. If all requirements are met but issuance is asynchronous/manual, distinguish "eligible" from "issued". Confirm credential display name through an authorized identity path without exposing unnecessary identity data. Issued credentials carry immutable ID, issuer, program/version, issue date, and verification. Corrections create a traceable reissue/update; revocation remains externally verifiable. Download/share should not expose private grades unless explicitly included.

## Failure topology

Failures include certificate offered while grading pending, completion triggered by percentage alone, typo correction creating duplicate valid credentials, revoked credential link still verifying as active, share cards leaking private performance, and learner name editable without identity policy. Another failure is a downloadable PDF with no verifiable credential identity.

## Falsification

Reject if eligibility cannot enumerate requirements; if pending evaluation is treated as complete; if issued credential lacks stable ID/issuer/program identity; if correction/revocation history is absent; if verification status can diverge from displayed active state; or if sharing reveals data beyond the credential contract.

## Output contract

Return a `certificate-and-completion-flows-contract` with: requirement eligibility; pending/manual-review states; learner display identity; issuer/program/version; credential ID; issue/expiry; download/share; verification; correction/reissue; revocation; and privacy fields. Include one pending-grade and one corrected-name scenario.

## Handoffs

Curriculum/progress/gradebook provide eligibility evidence, data export/file download handles artifacts, and identity/privacy owners govern learner naming and share scope.