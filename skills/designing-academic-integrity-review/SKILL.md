---
name: designing-academic-integrity-review
description: Own evidence-sensitive review of potential academic integrity concerns, including detector limitations, source comparison, case state, learner response, reviewer decisions, privacy, and appeal provenance.
---
# Designing Academic Integrity Review

## Decision ownership

Own the interface for reviewing possible integrity violations without treating automated similarity or anomaly signals as guilt. Decide alert/evidence presentation, source comparison, case state, reviewer assignment, confidence/limitations, learner response, decision, sanction linkage, appeal, and privacy. This owner is governance-oriented and must resist detector overclaiming.

## Inputs and evidence

Require submission/version, detector outputs, matched sources or behavioral evidence, detector confidence/limitations, policy, learner identity, reviewer roles, prior case state where permitted, response/appeal process, and retention/privacy rules. Identify false-positive classes and evidence that cannot legally or ethically be surfaced to all reviewers.

## Procedure

Present automated findings as signals with method/version and limitations, not verdicts. Link every similarity/anomaly to inspectable evidence and exact submission version. Allow reviewer notes that distinguish observation from inference. Case lifecycle may include triage, evidence review, learner response requested, decision pending, resolved, appealed. Decisions require policy basis and rationale. Protect sensitive information and avoid showing unrelated prior history where policy forbids it. Appeals preserve original decision/evidence and append new review rather than overwriting.

## Failure topology

Failures include a percentage labeled plagiarism, AI-detector score treated as proof, matched passages without source context, submission version mismatch, learner response buried, reviewer decision with no policy rationale, and appeals overwriting the original case. Another failure is exposing allegation status broadly to instructors/peers without need.

## Falsification

Reject if automated detector output is framed as conclusive without policy/evidence basis; if evidence cannot link to exact submission version; if reviewer cannot record uncertainty; if learner response/appeal state is absent where process requires it; if decision rationale/policy is missing; or if sensitive case data exceeds authorized scope.

## Output contract

Return an `academic-integrity-review-contract` with: case/submission identity; signal source/method/version; limitations; evidence/source comparison; reviewer observations/inferences; lifecycle; learner response; decision/policy rationale; sanction handoff; appeal history; and privacy/retention. Include one high-similarity legitimate-source scenario.

## Handoffs

Assignment submission supplies immutable artifact, grading remains separate until policy links outcomes, case/evidence management may provide generic workflow, and security-style anomaly tools do not replace academic policy judgment.