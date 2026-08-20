---
name: designing-portfolio-rollups
description: Own cross-project portfolio aggregation across outcomes, investments, milestones, dependencies, risks, capacity, and health without double-counting nested work or hiding incomparable project models.
---
# Designing Portfolio Rollups

## Decision ownership

Own the portfolio layer above projects. Decide project/group hierarchy, common rollup dimensions, aggregate health, investment/progress summaries, cross-project dependencies, shared risks, drill-down, and comparability limits. This owner must preserve the distinction between aggregation and normalization; not every project metric is safe to sum.

## Inputs and evidence

Require portfolio hierarchy, project membership rules, nested initiatives, common financial/capacity fields, health signals, milestone commitments, risk identities, cross-project dependencies, reporting audiences, and project types. Identify metrics that would double-count when parent initiatives already include child values.

## Procedure

Define stable portfolio entities and membership before building dashboards. Roll up only metrics with compatible units and clear aggregation rules; otherwise show distributions or project-level statuses. Deduplicate shared risks, milestones, or dependencies by identity. Preserve drill-down from every aggregate to contributing projects. Cross-project dependency views should reveal the owner on both sides. Health rollup must explain whether it is worst-child, weighted, threshold-based, or not aggregated. Provide a way to compare cohorts of similar projects rather than ranking incomparable initiatives on one score.

## Failure topology

Failures include double-counted budget/work, parent and child projects both appearing as independent totals, average health hiding one critical initiative, shared risk counted multiple times, portfolio charts with no drill-down, and ranking projects that use different estimation or lifecycle models. Another failure is stale closed projects remaining in active capacity totals.

## Falsification

Reject if a nested project causes totals to exceed known source values; if a shared cross-project risk appears as multiple independent portfolio risks; if an aggregate health status cannot explain its rule; if users cannot drill from a portfolio number to source projects; if incompatible estimate units are summed; or if archived projects influence active forecasts without explicit inclusion.

## Output contract

Return a `portfolio-rollups-contract` with: portfolio hierarchy; membership rules; metric aggregation whitelist; anti-double-counting rules; shared-identity deduplication; health aggregation policy; dependency rollup; cohort comparison; active/archived inclusion; drill-down links; and comparability warnings. Include one nested-initiative and one shared-risk example.

## Handoffs

Project health, milestones, risks, workload, and financial operations provide source evidence. Roadmaps may present portfolio timing, but this owner determines rollup truth and drill-down integrity.