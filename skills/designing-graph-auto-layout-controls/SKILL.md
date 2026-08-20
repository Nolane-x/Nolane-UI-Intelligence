---
name: designing-graph-auto-layout-controls
description: Use when this specialist's decision ownership is materially in scope. Own user control over automatic graph arrangement, including scope, preview, constraints, pinned objects, determinism, and recovery from disruptive layout changes.
---
# Designing Graph Auto-Layout Controls

## Parent Contract

**Required parent:** `designing-diagramming-and-node-graph-editors`.

Inherit the broader routing and decision boundary from this canonical parent; this specialist remains accountable only for the narrower ownership, failure topology, falsification criteria, and output contract defined below.

## Decision ownership

Own the product-facing contract for algorithmic node arrangement. Decide when auto-layout is offered, which graph scope it affects, how direction/spacing/algorithm presets are expressed, how pinned positions and containers constrain the result, whether users preview before commit, and how the operation remains reversible. The underlying layout algorithm can be implemented elsewhere; this owner governs its interaction and trust model.

## Inputs and evidence

Require graph families and sizes, available layout algorithms, runtime cost, whether coordinates themselves carry meaning, pin/lock semantics, container and lane constraints, expected manual arrangement, collaboration behavior, and frequency of incremental graph change. Identify layouts where deterministic reproduction matters for reviews, diffs, or team communication.

## Procedure

Define scope before controls: selected nodes, current subgraph, container, connected component, or whole graph. Whole-graph relayout should never be the accidental default on a mature hand-arranged diagram. Expose a small set of meaningful goals—hierarchical direction, compactness, flow orientation, separation—rather than raw algorithm jargon unless users are experts. Show a preview or ghost layout for disruptive operations and make pinned/locked nodes visibly invariant. Specify what happens to manual bendpoints, annotations, and viewport focus. Long-running layout needs progress/cancel and an approximation path. After commit, preserve an undo boundary that restores both positions and relevant routing state.

## Failure topology

Failures include a single toolbar click destroying hours of manual organization, layout controls whose names do not predict outcomes, pinned nodes drifting, nested containers being violated, collaborative users seeing inconsistent arrangements, or non-deterministic layouts making diffs meaningless. Another failure is recomputing the entire graph after every small edit, causing constant visual churn.

## Falsification

Reject if users cannot know the affected scope before running layout; if pinned elements move; if cancelling a preview mutates the saved graph; if repeated layout with identical inputs yields materially different arrangements where reproducibility is required; if large graphs block interaction with no cancel path; or if undo restores node positions but leaves edge routes/viewport in an incoherent state.

## Output contract

Return a `graph-auto-layout-controls-contract` containing: available goals/presets; scope selector; constraints and pins; preview semantics; expected runtime classes; progress/cancel behavior; deterministic guarantees; edge-routing order; annotation handling; collaboration synchronization; commit/undo boundary; and the fallback when layout cannot satisfy all constraints.

## Handoffs

Coordinate with `designing-edge-routing-and-bendpoints`, `designing-subgraph-and-container-models`, and formal diagram owners that impose direction or lane constraints. Generic background-task progress handles long computation, while undo/redo history provides mechanism-level recovery under this skill's atomic layout transaction.