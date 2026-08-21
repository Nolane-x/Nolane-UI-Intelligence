---
name: governing-token-deprecation-lifecycles
description: Use when an obsolete design token needs a replacement path, warning interval, consumer migration signal, and defensible removal gate without indefinite compatibility debt.
---

# Governing Token Deprecation Lifecycles

## Lifecycle Purpose
Deprecation is a state machine, not a comment that says “old.” This skill owns the transition from supported token to deprecated token to removed token, including replacement mapping, warning behavior, deadlines, exceptions, and proof that removal will not orphan consumers.

## Parent Contract
**Required parent:** `architecting-design-tokens`.

The parent may decide a token no longer belongs in the architecture. This specialist determines how that decision propagates safely through consumers over time.

## States and Gates
Use explicit states such as `active`, `deprecated-with-replacement`, `deprecated-without-equivalent`, `removal-candidate`, and `removed`. Every transition has evidence. A replacement mapping states whether it preserves semantics, intentionally changes semantics, or requires manual judgment. A deadline without consumer visibility is not a lifecycle.

The decision to remove requires both time/policy conditions and usage evidence. “Deprecated for six months” cannot substitute for knowing whether supported consumers still rely on the token.

## Consumer Signals
Warnings should identify the old token, supported replacement or migration guidance, affected package/version, and removal horizon. Generated code and transformed aliases need signals too; otherwise human-readable deprecation markers miss real use.

## Evidence
Evidence includes reference/usage inventories over time, warning telemetry or build findings, migration completion by supported consumer class, replacement semantic review, and a final negative-usage scan tied to the release candidate. Preserve exceptions with owner and expiry.

## Failure Modes
Failure includes permanent deprecation with no removal criteria, removal while generated consumers still reference the token, automatic replacement that changes meaning, warnings that cannot identify call sites, and a token resurrected by an old package after apparent cleanup.

## Falsification
Falsification installs a supported old consumer against the proposed removal, scans generated outputs, exercises non-default modes, and checks that warnings lead to a valid migration path. Any supported consumer that breaks without a declared exception disproves readiness for removal.

## Recovery
Recovery returns the token to the last support state, restores compatibility only within the declared window, and updates the migration evidence. If there is no semantic replacement, expose that explicitly and require a design decision rather than inventing an alias.

## Output
Output: `token-deprecation-lifecycles-contract` containing state, replacement semantics, warning channel, deadline, consumer coverage, exceptions, and removal evidence.

## Handoff and Sibling Boundary
Handoff blast-radius discovery to token migration impact auditing and coordinated product rollout to design-system breaking-change rollout. The sibling does not own lifecycle authority.

## delete-the-skill test
Remove this skill and token architecture can still label something obsolete, but no owner remains for the temporal support/removal contract, warning interval, or evidence-bound removal gate. That material gap proves independent ownership.