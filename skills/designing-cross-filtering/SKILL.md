---
name: designing-cross-filtering
description: Use when selecting marks or regions in one analytical view filters or highlights peer views and the interface must distinguish selection, filtering, highlighting, scope and reset behavior across coordinated visualizations.
---

# Designing Cross Filtering

## Parent Contract
**Required parent:** `designing-data-visualization`.

This faculty owns coordinated analytical filtering across multiple views. It does not define each visualization’s encoding or the general table filter-builder UI.

## Decision Model
Separate **selection** from **filter application**. Clicking a bar may select it locally, highlight corresponding records elsewhere, or actually constrain the shared dataset. Those are different consequences and need distinct visual/state language. If cross-filtering is automatic, make the active global constraint persist after the pointer leaves the source chart.

Define filter scope. A selection can affect all dashboard views, only a linked group, or one downstream panel. Views that do not participate should not appear visually synchronized. When several source selections combine, state whether they are ANDed, ORed within a dimension, replaced by the latest selection, or represented as separate filter clauses.

Use stable semantic values rather than rendered mark indexes. Sorting, animation or aggregation can reorder marks; a filter for category `A` must remain `A`. Brush selections over continuous axes need an explicit inclusive/exclusive boundary and units.

Reset must be obvious and complete. Users should be able to clear one cross-filter at its source and all cross-filters globally. A dashboard that remains filtered after the source selection is offscreen needs a persistent scope summary.

Asynchronous coordinated views may update at different speeds. Indicate pending/stale panels where mismatch could affect interpretation rather than temporarily displaying a mixture of old and new scopes as if coherent.

## Failure Topology
- Hover highlight silently becomes a persistent filter after click with no state cue.
- One chart filters all peers while another only highlights, using identical selection styling.
- Multiple category selections are ANDed into an impossible empty set when users expect OR.
- A slow table shows old data while charts already reflect the new filter.
- Clearing a source selection leaves hidden derived filters active.
- Keyboard users can focus chart marks but cannot invoke or clear the same cross-filter.

## Falsification and Recovery
Falsify with single/multiple selections, brush ranges, mixed dimensions, asynchronous panel responses, source chart removal, keyboard interaction and global reset. Compare every participating view’s query scope at each state. Any interval where a panel appears current but uses a different scope is a failure.

Recover by centralizing cross-filter state, labeling scope/effect, distinguishing highlight from filter, grouping logical clauses explicitly and marking stale peers until synchronized.

## Output Contract
Return `cross-filtering-contract` with source interactions, semantic filter values, participating-view graph, combination logic, persistent active-state presentation, async synchronization, reset routes, accessibility equivalents and scope-parity tests.