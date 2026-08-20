---
name: designing-pipeline-stage-visualization
description: Use when this specialist's decision ownership is materially in scope. Own visual representation of pipeline stages, dependencies, parallelism, fan-in/fan-out, skipped paths, gates, and current execution focus without reducing state to colored boxes.
---
# Designing Pipeline Stage Visualization

## Parent Contract

**Required parent:** `designing-software-delivery-pipelines`.

Inherit the broader routing and decision boundary from this canonical parent; this specialist remains accountable only for the narrower ownership, failure topology, falsification criteria, and output contract defined below.

## Decision ownership

Own how a pipeline run's execution structure is represented. Decide linear versus graph layout, parallel-group treatment, fan-in/fan-out, collapsed matrices, current/failed focus, skipped branches, gates, and navigation from overview to jobs. It does not decide stage semantics or execute jobs.

## Inputs and evidence

Require pipeline DAG, stage/job counts, parallel matrices, conditional branches, gate stages, typical run duration, failure frequency, and mobile/dense display requirements. Identify whether the DAG is stable across runs or dynamically generated.

## Procedure

Use the simplest structure that preserves causality. Linear pipelines should not be forced into a complex DAG; true parallel dependencies must not be flattened into a misleading list. Encode state with icon/text plus color, and distinguish queued, running, waiting, blocked, skipped, cancelled, failed, and successful. Collapsed parallel groups need aggregate counts and worst/member state disclosure. Selecting a failed stage should reveal upstream dependencies and logs without losing overview. Dynamic/skipped branches should explain why they did not run.

## Failure topology

Failures include all boxes looking equal despite different gating roles, skipped shown as success, matrix jobs exploding the page, connectors whose direction is unclear, current stage hidden off-screen, and a graph so zoomed out that labels vanish. Another failure is using animation to imply progress while no actual state event occurred.

## Falsification

Reject if users cannot distinguish blocked from queued; if a skipped conditional path has no reason; if one failed matrix member is hidden by an overall green group; if dependency direction is ambiguous; if navigating to logs loses the stage context; or if the overview cannot accommodate a representative high-parallelism pipeline without becoming unreadable.

## Output contract

Return a `pipeline-stage-visualization-contract` with: structural layout choice; stage state vocabulary; dependency direction; parallel-group aggregation; gate representation; skipped/conditional explanation; current/failure focus; overview-to-detail navigation; accessibility equivalents; and scale fallback. Include one fan-out/fan-in matrix example.

## Handoffs

CI job log navigation owns log detail, release approval gates own gated semantics, and software delivery pipelines own run/source/artifact identity. Generic graph visualization supplies mechanics only.