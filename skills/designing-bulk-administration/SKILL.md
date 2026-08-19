---
name: designing-bulk-administration
description: Use when administrators change many users, resources or policies at once and the interface must make selection universe, preview, partial eligibility, validation, execution progress, rollback and audit outcome explicit.
---

# Designing Bulk Administration

## Parent Contract
**Required parent:** `designing-organization-administration`.

This faculty owns high-impact multi-entity administrative changes. Generic bulk action presentation is inherited from `designing-bulk-action-toolbars`, but administrative consequence, validation and audit requirements are stronger here.

## Decision Boundary
Treat bulk administration as a **planned change set**, not “loop the single-item endpoint N times.” Capture target universe, action, per-target eligibility, resulting values, conflicts, dependencies and expected side effects before execution. Selection may be explicit IDs, all matching a query, group membership or imported list; the exact universe must be frozen or intentionally dynamic according to product semantics.

Provide a preflight phase for high-impact operations. Show counts of eligible, ineligible, unchanged and risky targets; sample or enumerate exceptions; reveal changes to ownership, access, billing seats, security policy or automation where material. Do not require users to inspect thousands of names when summary + exceptions is more informative.

Execution can be atomic, transactional by group or best-effort per target. The UI must match backend semantics. For best-effort runs, preserve per-item result and offer retry of failures without reapplying successes. For async jobs, provide durable job identity, progress by meaningful units and a route back after navigation.

Rollback must be claimed only when supported. If the system can restore prior values, define rollback scope/version conflicts. Otherwise provide compensating actions and exportable result history rather than a fake Undo.

## Failure Topology
- “All 5,420 users” is computed before filter changes but execution uses the new live query unexpectedly.
- Bulk role change includes last owners and locks organizations out.
- Progress reaches 100% sent requests while half are still processing downstream.
- Retry runs against all targets and duplicates successful side effects.
- UI advertises Undo for deletion that cannot actually be restored.
- Admin leaves the page and loses access to an hour-long job/results.

## Falsification and Recovery
Falsify with mixed eligibility, dynamic query changes, partial failures, concurrent edits, async job navigation, cancellation, retry and rollback conflict. Reconcile target snapshot and per-item results to audit events.

Recover by freezing/labeling scope, adding preflight and invariant checks, aligning progress with backend stages, retrying only failed IDs and representing irreversible/compensating recovery truthfully.

## Output Contract
Return `bulk-administration-contract` with target-universe semantics, preflight categories, invariant checks, execution atomicity, async job/progress, per-target result, retry/cancel/rollback policy, audit linkage and large-change tests.