---
name: designing-blue-green-rollouts
description: Own blue-green deployment switching between parallel environments, including active/inactive identity, synchronization, traffic cutover, smoke verification, fallback, and stale-environment cleanup.
---
# Designing Blue-Green Rollouts

## Decision ownership

Own blue-green specific deployment state. Decide how active versus candidate environment is identified, how version/config/data compatibility is compared, how cutover is previewed, what verifies success, how fallback works, and when the inactive environment may be retired. This owner prevents color labels from becoming the only environment identity.

## Inputs and evidence

Require paired environments, current active side, candidate version, configuration/data/schema compatibility, traffic switch mechanism, health checks, session/state implications, rollback window, and cleanup policy. Identify whether names blue/green are stable or swap roles per release.

## Procedure

Represent environments with stable IDs and explicit role labels: active, candidate, previous—not color alone. Before cutover, show version/config differences and unmet readiness checks. Traffic switch should state expected scope and whether sessions/connections drain. After cutover, enter verification state while the previous environment remains available for fallback according to policy. A fallback control must state whether data/schema changes make reversal unsafe. Cleanup/repurpose of the old side should be a separate later action, not an automatic consequence of successful switch.

## Failure topology

Failures include users confusing blue/green names after roles swap, cutover with configuration drift, fallback offered despite irreversible schema changes, old environment destroyed too early, and traffic shown as fully switched while connections remain. Another failure is only using green/blue color, which is inaccessible and semantically weak.

## Falsification

Reject if users cannot identify current active side without color; if cutover can proceed with unresolved critical drift hidden; if fallback safety is unknown; if verification completion automatically deletes the old side; if residual traffic is not visible; or if a role swap changes labels so historical logs become ambiguous.

## Output contract

Return a `blue-green-rollouts-contract` containing: stable environment identities; active/candidate/previous roles; readiness diff; cutover scope; connection/session handling; verification window; fallback conditions; irreversible-change warnings; residual-traffic state; and old-environment cleanup policy. Include one unsafe-fallback scenario.

## Handoffs

Environment diff/drift owners provide readiness evidence, target selection identifies the pair, rollback handles fallback execution, and release approvals may gate cutover.