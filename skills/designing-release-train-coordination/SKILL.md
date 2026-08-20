---
name: designing-release-train-coordination
description: Use when this specialist's decision ownership is materially in scope. Own coordination of multiple changes, services, artifacts, approvals, dependencies, cutoffs, and deployment waves into a shared scheduled release train.
---
# Designing Release Train Coordination

## Parent Contract

**Required parent:** `designing-software-delivery-pipelines`.

Inherit the broader routing and decision boundary from this canonical parent; this specialist remains accountable only for the narrower ownership, failure topology, falsification criteria, and output contract defined below.

## Decision ownership

Own the planning surface for a release containing multiple independently developed changes or services. Decide train membership, readiness, cutoff, dependency/order, owners, approvals, rollout waves, exceptions, and carryover. This owner does not replace each service's pipeline; it coordinates their shared release commitment.

## Inputs and evidence

Require release cadence, participating services/artifacts, change owners, dependency graph, readiness checks, cutoff policy, approvals, rollback compatibility, deployment order, communication deadlines, and exception rules. Identify whether train components can release independently after missing the cutoff.

## Procedure

Give the train a stable identity and target window. Show each member's artifact/change identity, readiness, owner, blockers, dependencies, and approval state. Cutoff should be explicit; changes added after cutoff require exception provenance. Dependency order should be visible without implying all components must deploy serially. Define go/no-go summary based on required members and allow optional/carryover classification. During execution, show wave progress and mixed component versions. After completion, record omitted/carried changes rather than rewriting original scope.

## Failure topology

Failures include release scope living in spreadsheets/chat, late changes silently joining, readiness reported at project rather than artifact level, dependency order hidden, optional components blocking the whole train, and omitted changes disappearing from history. Another failure is one failed component making the UI imply every service rolled back when they did not.

## Falsification

Reject if train membership at cutoff cannot be reconstructed; if a member lacks artifact/owner identity; if late addition has no exception record; if dependency/order cannot be inspected; if go/no-go cannot distinguish required from optional; or if post-release scope differs from planned scope with no carryover/omission history.

## Output contract

Return a `release-train-coordination-contract` with: train identity/window; membership; cutoff; required/optional classification; owner/artifact readiness; dependency/order; approvals; late-change exception; execution waves; per-member outcome; carryover/omission; and final scope record. Include one late addition and one failed optional member.

## Handoffs

Individual pipelines and artifacts provide readiness, release approvals provide gates, progressive delivery executes waves, and release notes consume actual final train scope.