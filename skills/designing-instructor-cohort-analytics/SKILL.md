---
name: designing-instructor-cohort-analytics
description: Use when this specialist's decision ownership is materially in scope. Own instructor-facing learning analytics across participation, progress, assessment distributions, item difficulty, disengagement signals, subgroup comparison, privacy, uncertainty, and actionable drill-down.
---
# Designing Instructor Cohort Analytics

## Parent Contract

**Required parent:** `designing-digital-learning-experiences`.

Inherit the broader routing and decision boundary from this canonical parent; this specialist remains accountable only for the narrower ownership, failure topology, falsification criteria, and output contract defined below.

## Decision ownership

Own aggregate learning evidence for instructors or program operators. Decide cohort definition, participation/progress/assessment metrics, distribution, item analysis, trend, subgroup filtering, alert thresholds, drill-down, missing-data disclosure, and privacy. This owner must prevent analytics from turning weak engagement proxies into claims about ability or motivation.

## Inputs and evidence

Require cohort/enrollment, progress, attempts, grades, activity timestamps, content/item identities, demographic/accommodation data only if authorized, metric definitions, data completeness, privacy thresholds, and course version. Identify learners with missing/offline data and small subgroups at re-identification risk.

## Procedure

Start from explicit metric definitions and cohort denominator. Show distributions and ranges before relying on averages. Separate engagement evidence (activity, submissions) from performance/mastery evidence. Item analysis can reveal difficulty/discrimination or common errors where statistically justified, with sample size. Subgroup comparisons require privacy thresholds and contextual caution; suppress tiny cells. Every alert—stalled, low participation, high failure—should drill to evidence and support a pedagogical action without labeling the learner as deficient. Course/version changes must segment incompatible data.

## Failure topology

Failures include average grade without distribution, inactivity interpreted as disengagement despite offline work, tiny subgroup dashboards exposing individuals, leaderboard-like ranking, missing data treated as zero, and model-generated risk labels with no definition. Another failure is comparing assessments across changed course versions as if identical.

## Falsification

Reject if denominator/sample size is hidden; if missing data is treated as negative performance; if engagement proxy is labeled motivation/mastery; if small subgroup privacy rules are absent; if an alert cannot explain its metric threshold; or if incompatible course/assessment versions are pooled without disclosure.

## Output contract

Return an `instructor-cohort-analytics-contract` with: cohort definition; metric definitions; denominators/completeness; distributions; engagement/performance separation; item analysis/sample size; subgroup privacy thresholds; alerts/drill-down; version segmentation; and limits on inference. Include one small-subgroup suppression case.

## Handoffs

Progress, gradebook, assessments, and submissions provide source evidence; data visualization renders it; privacy-sensitive interfaces govern authorization; interventions remain instructor decisions outside the metric itself.