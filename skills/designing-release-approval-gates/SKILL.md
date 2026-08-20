---
name: designing-release-approval-gates
description: Own software-release approval interfaces that bind reviewer decisions to immutable artifact, target, evidence, policy, expiry, and separation-of-duties constraints.
---
# Designing Release Approval Gates

## Decision ownership

Own approval before a release or deployment stage may proceed. Decide what artifact/target is being approved, evidence bundle, required reviewer roles, decision options, expiry/reapproval conditions, separation of duties, comments, and downstream effect. Generic approval workflows are a mechanism; this owner binds approval to immutable delivery state.

## Inputs and evidence

Require approval policy, artifact digest, target environment, test/security/change evidence, reviewer roles, quorum, expiry rules, source changes after approval, emergency override, and audit requirements. Identify whether one approval covers a release train, artifact, target, or exact deployment attempt.

## Procedure

Present artifact digest/version, target, relevant changes, required checks, and unresolved exceptions before the decision control. Approval must be scoped to immutable inputs; if artifact or material target changes, invalidate or require reapproval according to policy. Show who is eligible and who has already decided without pressuring reviewers through social color cues. Reject/request-changes must capture actionable rationale. Emergency bypass, if allowed, needs explicit authority and audit. Expired approvals remain historical but visibly inactive.

## Failure topology

Failures include approval attached to a mutable branch name, artifact rebuilt after approval, target changed after decision, self-approval violating separation of duties, old approval silently reused, and green checks summarized with no evidence access. Another failure is approving "the release" when the UI cannot state which exact artifact and environment that means.

## Falsification

Reject if approved inputs can mutate without invalidation; if artifact digest/target are absent; if an ineligible actor can approve; if expired approval appears active; if evidence cannot be opened; if emergency bypass lacks reason/authority; or if rejection rationale is lost when a new attempt is created.

## Output contract

Return a `release-approval-gates-contract` with: approval scope; immutable artifact/target binding; evidence bundle; reviewer eligibility/quorum; separation-of-duties rule; approve/reject/request-change states; expiry/invalidation; emergency override; audit fields; and downstream-unblock behavior. Include one rebuilt-artifact invalidation scenario.

## Handoffs

Build/artifact ownership provides immutable identity, deployment target selection supplies target, provenance provides attestations, and generic approvals render common decision mechanics.