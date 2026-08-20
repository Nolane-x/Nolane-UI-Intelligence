---
name: designing-canary-rollouts
description: Own staged canary rollout interfaces where a small traffic or instance cohort receives a new version, is observed against criteria, then advances, pauses, or rolls back.
---
# Designing Canary Rollouts

## Decision ownership

Own canary-specific progression. Decide cohort size/selection, baseline comparison, observation window, success/failure criteria, manual versus automatic advance, pause, rollback, and visibility of mixed versions. It does not define deployment transport or monitoring metrics themselves.

## Inputs and evidence

Require target topology, canary cohort mechanism, traffic/instance percentages, baseline version, health/business metrics, error budgets, observation duration, automation policy, rollback capability, and maximum blast radius. Identify whether cohort selection is random, region-based, tenant-based, or instance-based.

## Procedure

Before start, show exact canary scope and baseline version. Define advance criteria and observation window up front; do not let a green moment imply success. During rollout, show cohort size, version distribution, metric comparison, missing telemetry, and elapsed observation. Automatic advance needs a visible countdown/criteria and a pause path. Failed criteria should state whether rollout pauses or rolls back. Mixed-version state must remain visible until all targets converge or the rollout is abandoned.

## Failure topology

Failures include canary scope larger than expected, metrics compared across mismatched cohorts, automatic advance with missing telemetry, one short healthy sample triggering progression, rollback appearing complete while mixed versions remain, and operators unable to pause automation. Another failure is describing "10%" without identifying what denominator it represents.

## Falsification

Reject if canary denominator/cohort is ambiguous; if advance can occur with missing required signals; if observation duration is not visible; if baseline comparison uses a materially different population without disclosure; if pause cannot stop pending advance; or if rollback completion hides remaining new-version instances.

## Output contract

Return a `canary-rollouts-contract` with: cohort definition; baseline; rollout steps; required signals; observation windows; comparison method; automatic/manual advance; pause; failure action; rollback verification; version-distribution display; and completion criteria. Include one missing-telemetry automatic-advance case.

## Handoffs

Deployment target selection defines scope, progressive delivery may coordinate broader stages, rollback handles recovery mechanics, and service/metrics exploration provide evidence without owning canary policy.