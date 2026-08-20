---
name: designing-graph-diff-and-history
description: Own semantic comparison and historical review of graph structure, distinguishing meaningful node/edge changes from incidental layout movement.
---
# Designing Graph Diff and History

## Decision ownership

Own temporal comparison for graphs. Decide how added, removed, retyped, reconnected, renamed, regrouped, and materially moved entities are represented; how layout-only churn is separated from semantic change; how users navigate between versions; and how structural identity survives renames or position changes. Generic text diff is insufficient because topology is the primary artifact.

## Inputs and evidence

Require stable IDs or identity matching rules, version model, change events if available, whether layout coordinates are semantic, collaboration attribution, edge/container identity, expected version distance, and restoration permissions. Determine whether comparison is snapshot-to-snapshot, event replay, or both.

## Procedure

Classify changes before visualization: semantic entity change, relationship change, container membership change, property change, and layout-only change. Default to the semantic layer while allowing layout diffs when coordinates matter. Preserve a common spatial anchor where possible so unchanged regions stay fixed across versions. Removed entities need ghost/tombstone representation or a dedicated side; added entities need provenance. For rewired edges, show old and new endpoints explicitly rather than treating the edge as delete-plus-add if identity is known. Provide change filtering, attribution, and step-through history. Restore actions must state whether they revert one object, a subgraph, or the entire version.

## Failure topology

Failures include every node appearing changed after auto-layout, renamed nodes being treated as delete/add, edge rewires impossible to perceive, removed structure disappearing completely, diff colors colliding with status colors, and restore controls that silently revert unrelated concurrent work. History can also fail when attribution is attached to screen positions instead of stable entities.

## Falsification

Reject if running auto-layout alone produces a semantic diff flood; if a known stable-ID rename is shown as deletion/addition; if users cannot identify both endpoints of a rewired relationship; if removed nodes have no inspectable prior state; if change colors are indistinguishable under high-contrast/low-vision modes; or if a partial restore cannot preview collateral changes.

## Output contract

Return a `graph-diff-and-history-contract` containing: identity strategy; change taxonomy; semantic-versus-layout default; unchanged-region anchoring; added/removed/rewired representations; attribution; version navigation; filters; replay behavior; restore scopes; conflict safeguards; and accessible textual diff equivalent. Include an auto-layout-only comparison and an edge-rewire comparison.

## Handoffs

Use generic version history for storage/revision navigation, but keep graph-semantic diff logic here. Coordinate with layout controls to classify coordinate churn, collaboration for attribution, and validation for showing whether historical changes introduced or resolved findings.