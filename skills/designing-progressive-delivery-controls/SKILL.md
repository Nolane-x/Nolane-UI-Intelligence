---
name: designing-progressive-delivery-controls
description: Own multi-step progressive delivery across cohorts, regions, percentages, or stages with explicit progression policy, evidence gates, holds, aborts, and mixed-version state.
---
# Designing Progressive Delivery Controls

## Decision ownership

Own rollout plans that advance through multiple scopes rather than one deployment action. Decide step sequence, cohort/percentage definitions, evidence gates, automatic/manual progression, hold duration, pause/abort, stage edits, and visibility of current version distribution. Canary is one specialized pattern; this owner coordinates arbitrary staged rollout plans.

## Inputs and evidence

Require rollout stages, target partitions, traffic/instance denominators, promotion criteria, observation signals, maximum concurrent stages, automatic progression policy, rollback scope, maintenance/freeze constraints, and version inventory. Determine whether stage definitions are immutable once rollout starts.

## Procedure

Present the entire rollout plan before start with scope and expected progression. Highlight current stage, completed stages, pending gates, and remaining blast radius. Every percentage needs a denominator and partition rule. Automatic advancement must be conditioned on explicit evidence and time windows, with visible pause/override. Editing future stages during an active rollout should show whether approval is invalidated. Failure should distinguish pause-for-investigation, rollback-current-stage, and rollback-entire-rollout. Completion requires version convergence or an explicit accepted mixed-state outcome.

## Failure topology

Failures include percentages without denominator, future stages hidden until they happen, automatic advance with stale signals, plan edits silently changing approved scope, pause that does not stop scheduled progression, and completion while old versions remain unexpectedly. Another failure is rolling back only the newest cohort while UI implies the whole deployment reverted.

## Falsification

Reject if the full blast-radius plan cannot be reviewed before start; if automatic progression ignores missing/stale evidence; if pause has ambiguous effect; if changing a future stage does not surface approval consequences; if rollback scope is unclear; or if version distribution cannot confirm rollout completion.

## Output contract

Return a `progressive-delivery-controls-contract` with: ordered stages; partition/denominator; evidence gates; observation windows; automatic/manual progression; pause/hold; active-plan edit policy; failure/abort options; rollback scope; version-distribution view; and completion criteria. Include one mid-rollout plan-change case.

## Handoffs

Canary and blue-green owners provide specialized stage semantics, approvals govern scope changes, rollback owns restoration mechanics, and target selection validates partitions.