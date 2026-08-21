---
name: auditing-token-migration-impact
description: Use when replacing, renaming, splitting, merging, or revaluing tokens and the actual consumer and rendered-state blast radius must be known before migration is accepted.
---

# Auditing Token Migration Impact

## Why This Audit Exists
Token changes propagate indirectly. A single semantic alias can affect hundreds of components, modes, packages, screenshots, and accessibility states. This skill owns the pre-change and post-change impact audit; it does not own the lifecycle policy that decides when an old token is deprecated.

## Parent Contract
**Required parent:** `architecting-design-tokens`.

The parent defines correct token architecture. This auditor proves what a proposed change will touch and whether observed effects match the declared migration intent.

## Impact Ledger
Build a ledger from changed token identity to inbound references, consuming components, product surfaces, modes, and runtime states. Classify effects as intended visual change, semantic migration without intended appearance change, tolerated degradation, or unexpected regression. Record indirect paths, not just direct text matches.

For splits and merges, preserve semantic ancestry: “A and B both become C” is not safe merely because current literals match. The audit asks whether consumers previously encoded different meaning or future divergence requirements.

## Prediction Before Change
State predictions before applying the migration: expected affected consumers, expected unchanged control group, modes at risk, and render states likely to shift. This prevents retrospective explanation of every diff as intended.

## Evidence Requirements
Evidence combines reference-graph queries, consumer inventory, before/after token traces, rendered comparisons for high-risk states, and control surfaces expected to remain stable. For dynamic themes, include at least one non-default mode. Evidence must identify the exact token revisions being compared.

## Characteristic Failure
Failure includes hidden consumers using generated aliases, unexpected mode inheritance, a renamed token accidentally captured from another namespace, visually silent semantic merges, and broad snapshot churn with no classification. Another failure is “zero search hits” treated as proof of zero usage while transforms or build products rewrite identifiers.

## Falsification
Falsification selects predicted-unchanged controls and verifies they remain unchanged; samples indirect consumers; and reverses the migration in a test branch to see whether attributed diffs disappear. If unexplained changes remain or known consumers are absent from the ledger, the audit is falsified.

## Recovery Strategy
Recovery pauses rollout, restores the last verified mapping, adds missing dependency paths to the impact model, and reclassifies affected consumers. If the migration changed meaning, route back to token architecture rather than widening expected snapshots.

## Output
Output: `token-migration-impact-contract` with change set, predicted blast radius, affected/unaffected evidence, unexplained diff queue, and acceptance status.

## Handoff, Sibling Boundary, delete-the-skill
Handoff lifecycle timing to token deprecation governance and implementation sequencing to design-system adoption migration. Sibling reference integrity can prove links are valid but not whether rendered/product impact is intended. The delete-the-skill test passes because no other owner predicts and reconciles migration blast radius.