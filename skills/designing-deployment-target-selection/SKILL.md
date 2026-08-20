---
name: designing-deployment-target-selection
description: Own selection and verification of deployment environments, regions, clusters, tenants, or scopes with identity, health, permissions, compatibility, and consequence preview.
---
# Designing Deployment Target Selection

## Decision ownership

Own the operator decision of where software will be deployed. Decide target taxonomy, disambiguation, environment/region/cluster hierarchy, current version/health context, permission eligibility, compatibility checks, multi-target selection, and confirmation. Environment management defines targets; this skill governs choosing them safely for a deployment.

## Inputs and evidence

Require target inventory, stable IDs, environment type, region/cluster/tenant metadata, current deployed version, health, maintenance/freeze/lock state, permissions, artifact compatibility, and rollout policy. Identify dangerous naming collisions such as two clusters with the same display name in different accounts.

## Procedure

Display target identity with enough hierarchy to disambiguate—account/project, environment, region, cluster—not just a friendly name. Show current version and material health/freeze/lock conditions before selection. Filter incompatible or unauthorized targets while explaining why. Multi-target selection should preview total blast radius and rollout ordering. Production or sensitive targets need explicit environment cues that survive theme/color limitations. Preserve recently used targets cautiously; never auto-select a production target merely because it was last used.

## Failure topology

Failures include deploying to the wrong similarly named environment, hidden current-version differences, stale inventory, production represented only by red color, unauthorized targets appearing selectable until final failure, and multi-region selection with no scope summary. Another failure is defaults carrying from staging to production unexpectedly.

## Falsification

Reject if two same-named targets cannot be distinguished before selection; if current version/lock state is unknown; if production sensitivity depends only on color; if an incompatible artifact can be committed to a target with no preflight warning; if multi-target blast radius is not summarized; or if a previous selection silently persists across environment context changes.

## Output contract

Return a `deployment-target-selection-contract` containing: target hierarchy/identity; selection/search; current version/health; compatibility checks; permission filtering; lock/freeze visibility; sensitive-target cues; multi-target scope/order; default persistence rules; and confirmation payload. Include one same-name cross-account target scenario.

## Handoffs

Environment management owns target metadata, rollout specialists govern deployment progression after selection, locks/freezes can block selection/commit, and high-stakes decisions control sensitive consequences.