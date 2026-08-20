---
name: designing-deployment-rollback
description: Own software deployment rollback decisions and verification, including target scope, rollback candidate, compatibility, data/schema constraints, staged reversal, and confirmation of restored service.
---
# Designing Deployment Rollback

## Decision ownership

Own the UX for reverting a deployment to a prior software state. Decide rollback target, candidate version, scope, compatibility, irreversible data/schema warnings, staged versus immediate reversal, action authority, and verification that the old version is actually restored and healthy. Undo metaphors are insufficient because deployment rollback may be partial or unsafe.

## Inputs and evidence

Require deployment history, current/previous artifact digests, target/version distribution, migration/schema changes, feature/data compatibility, rollback capability, active traffic, health metrics, permissions, and rollback policy. Identify cases where forward-fix is safer than reversal.

## Procedure

Show current and proposed rollback versions, exact target scope, and reason. Preflight known incompatibilities, especially schema/data or external side effects. If rollback is unsafe, do not present it as a normal enabled button; explain constraints and alternatives. During reversal, show progress by target/version distribution. A command success is not completion—verify restored version and service health. Partial rollback must remain visibly partial. Record actor, trigger, evidence, and outcome for release/postmortem history.

## Failure topology

Failures include one-click rollback with unknown target, reverting binaries against incompatible schema, rollback marked complete on job success, residual new-version instances hidden, accidental rollback of unrelated regions, and no record of why reversal occurred. Another failure is presenting rollback as always safer than forward remediation.

## Falsification

Reject if artifact/target scope is ambiguous; if known incompatible migrations are not surfaced; if rollback completion lacks version-distribution and health verification; if partial failure is reported as success; if authority/consequence is absent for production rollback; or if prior version availability/retention is unknown.

## Output contract

Return a `deployment-rollback-contract` with: current/candidate versions; target scope; trigger/rationale; compatibility preflight; irreversible constraints; authority/confirmation; rollback steps; partial-failure state; version-distribution verification; health verification; audit record; and forward-fix alternative state. Include one schema-incompatible rollback scenario.

## Handoffs

Artifact history supplies candidates, target selection defines scope, health/metrics verify recovery, and incident mitigation may initiate rollback during an outage.