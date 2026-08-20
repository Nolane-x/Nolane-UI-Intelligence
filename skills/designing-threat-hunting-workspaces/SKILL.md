---
name: designing-threat-hunting-workspaces
description: Use when analysts conduct hypothesis-driven security hunts across telemetry and need reproducible queries, evidence notebooks, scope control, comparison, and promotion of findings without confusing exploration with confirmed detection.
---
# Designing Threat Hunting Workspaces

## Decision ownership

Own the workspace for hypothesis-driven security exploration. Decide how a hunt records its question, scope, assumptions, data coverage, queries, pivots, intermediate observations, exclusions, saved evidence, and conclusions so exploratory work is reproducible rather than a trail of lost browser tabs. This faculty does not author production detection rules and does not replace the specific search, entity, timeline, or network owners used during a hunt. It owns the continuity between those tools.

## Inputs and evidence

Require hunt hypothesis, target behaviors, relevant tactics or business risks, time range, populations, data sources, schema availability, query languages, sampling limits, baseline periods, expected benign explanations, saved-query model, collaboration requirements, and promotion paths into detections or cases. Include hunts that find nothing, hunts with incomplete telemetry, hunts that branch into competing hypotheses, and hunts whose original query becomes invalid after schema changes. Capture which steps are exploratory transformations versus evidence-preserving selections.

## Procedure

Start every hunt with a falsifiable statement and explicit scope: what behavior would support or weaken the hypothesis, which populations and time windows are included, and what telemetry gaps limit inference. Make each query or transformation part of a navigable notebook-like sequence with inputs, outputs, execution time, result counts, and schema/version context. Preserve branches when analysts pursue alternate explanations; do not force one linear path. Support pinning representative evidence while keeping the query that produced it. Provide lightweight comparison between baseline and suspect populations, but surface sample-size and coverage caveats. When a hunt produces reusable logic, promote a bounded artifact into detection-rule authoring rather than silently converting the exploratory query into production monitoring.

## Failure topology

- The workspace saves only the final query, losing the reasoning and prior pivots that made it meaningful.
- A no-result hunt is called “clean” despite missing telemetry for the relevant population.
- Analysts edit a saved query in place and cannot reproduce the historical hunt.
- Exploratory exclusions become permanent detection suppressions without review.
- Branching hypotheses are flattened into one narrative and contradictory evidence disappears.
- Pinned evidence lacks the exact query/time range that selected it.
- Result counts are compared across different populations or retention windows as if directly comparable.

## Falsification

Run a hunt with two competing hypotheses, one missing data source, a schema change midway, a baseline comparison, and a promising query that is later promoted toward detection. The design fails if a second analyst cannot replay the path, determine what data was absent, recover historical query versions, or distinguish exploratory evidence from a validated production detector.

## Output contract

Return `threat-hunting-workspaces-contract` containing hypothesis schema, scope and coverage ledger, reproducible query history, branching model, evidence pinning, baseline comparison constraints, collaboration state, null-result semantics, promotion boundary, and replay verification scenarios.

## Handoffs

Specific searches route to `designing-indicator-of-compromise-search`, entity analysis to `designing-security-entity-investigation`, timeline work to `designing-threat-investigation-timelines`, and reusable monitoring logic to `designing-detection-rule-authoring` plus `designing-detection-rule-testing`. Durable findings can be promoted to `designing-security-case-evidence-management`.