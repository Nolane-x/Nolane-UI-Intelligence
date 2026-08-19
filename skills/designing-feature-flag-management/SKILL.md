---
name: designing-feature-flag-management
description: Use when operators control runtime feature exposure and the interface must represent flag identity, targeting, environment, rollout percentage, precedence, evaluation evidence, scheduling, kill-switch risk, and cleanup.
---

# Designing Feature Flag Management

## Parent Contract
**Required parent:** `designing-high-stakes-decisions`.

This faculty owns operational control of feature exposure. It does not own deployment environments generally or experimentation statistics. A feature flag can change behavior for real users immediately, so the UI must make targeting and effective evaluation understandable before mutation.

## Decision Architecture
Give every flag stable identity, purpose, owner, type, lifecycle, and environment scope. Boolean, multivariate, percentage rollout, user/group targeting, prerequisite, and kill-switch flags have different evaluation semantics. Do not collapse them into one toggle when rule precedence determines who actually receives which value.

Before saving a rule change, show an effective targeting summary: environment, audiences, exclusions, rollout allocation, prerequisites, fallback/default, and estimated affected population when the backend can provide it. A 10% rollout is ambiguous without a stable bucketing key and eligible population. Scheduling future changes requires explicit timezone and current-rule interaction.

Operational safety includes history, rollback, stale-rule detection, and cleanup. Turning a flag “off” may not restore old behavior if code no longer contains the fallback path. A kill switch deserves rapid access but also strong identity/context so operators do not disable the wrong service feature. Flags that are fully launched should eventually be retired; the UI can surface age/ownership debt without automatically deleting code-bound controls.

## Failure Topology
- One toggle hides layered targeting rules and operators think “on” means everyone receives the feature.
- Production flag is edited while the page visually resembles staging and environment context is subtle.
- Percentage rollout rebuckets users after a rule edit and exposes a different cohort unexpectedly.
- Scheduled launch uses browser timezone and fires at the wrong business time.
- Rollback control restores a prior flag rule but code deployment removed the old branch, so behavior cannot actually revert.
- Temporary flag remains for years with no owner or cleanup signal.

## Falsification and Recovery
Falsify with multi-environment flags, prerequisites, exclusion cohorts, percentage changes, user-level override, scheduled rollout, stale browser edit, emergency kill switch, missing owner, and code path no longer supporting a prior variant. The design fails if an operator cannot explain effective evaluation for a representative user before committing a rule change or if environment identity can be overlooked.

Recover by exposing rule precedence and environment prominently, using stable bucketing semantics, previewing effective audiences, versioning mutations, recording ownership/history, distinguishing flag rollback from code rollback, and surfacing lifecycle debt.

## Output Contract
Return `feature-flag-management-contract` with flag type/identity, environment scope, targeting rule precedence, rollout/bucketing semantics, audience preview, scheduling, mutation history/versioning, emergency controls, rollback limits, ownership/cleanup policy, and falsification cases.