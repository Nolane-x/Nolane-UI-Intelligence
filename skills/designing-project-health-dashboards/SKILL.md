---
name: designing-project-health-dashboards
description: Use when this specialist's decision ownership is materially in scope. Own evidence-derived project health summaries that combine milestones, blockers, schedule, scope, capacity, risk, and change without collapsing status into a manual traffic light.
---
# Designing Project Health Dashboards

## Parent Contract

**Required parent:** `designing-project-and-work-management`.

Inherit the broader routing and decision boundary from this canonical parent; this specialist remains accountable only for the narrower ownership, failure topology, falsification criteria, and output contract defined below.

## Decision ownership

Own the project-health overview and its derivation. Decide which signals represent delivery health, how manual judgment coexists with evidence, how stale data is treated, what constitutes risk versus current failure, and how every summary can drill into contributing work. This owner does not redefine milestone, risk, dependency, or workload semantics.

## Inputs and evidence

Require project goals, milestone state, critical dependencies, overdue work, scope changes, workload/capacity, risk register, update cadence, manual status reports, and audience. Identify which metrics are comparable across project types and which would create false standardization.

## Procedure

Build health from a compact set of explainable signals: milestone risk, critical blockers, schedule variance, unresolved high-impact risks, scope change, and optionally capacity or quality evidence. Show evidence freshness. If a manual health label is allowed, keep it visibly distinct from derived indicators and capture rationale when it conflicts. Each warning must drill to source items or calculations. Trend recent change—improving, worsening, stable—where evidence supports it, but avoid pseudo-precision. Portfolio contexts should compare common signals while preserving project-specific notes.

## Failure topology

Failures include green-by-default dashboards, manual status overriding severe evidence invisibly, stale metrics, vanity completion percentages, red warnings with no drill-down, and one universal health score that treats dissimilar projects as comparable. Another failure is double-counting the same blocked dependency through several correlated indicators and exaggerating risk.

## Falsification

Reject if a critical blocked milestone can coexist with an unexplained green overall state; if the source of a warning cannot be opened; if stale data appears current; if manual and derived health conflict with no visible rationale; if an aggregate score cannot explain its factors; or if a filtered view makes the project look healthier without declaring scope.

## Output contract

Return a `project-health-dashboards-contract` with: health signal set; derivation rules; manual-judgment policy; freshness thresholds; trend behavior; drill-down mappings; conflict explanation; filtered-scope treatment; portfolio comparability limits; and no-data/insufficient-evidence state. Include one derived/manual conflict case.

## Handoffs

Consume milestone, dependency, workload, risk, scope-change, and status evidence from their owners. Data visualization chooses chart mechanics, while this skill decides which health claims are legitimate.