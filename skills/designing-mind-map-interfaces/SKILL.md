---
name: designing-mind-map-interfaces
description: Use when this specialist's decision ownership is materially in scope. Own rapid hierarchical idea expansion, branch navigation, folding, reordering, and focus mechanics for mind-map style knowledge structures.
---
# Designing Mind-Map Interfaces

## Parent Contract

**Required parent:** `designing-diagramming-and-node-graph-editors`.

Inherit the broader routing and decision boundary from this canonical parent; this specialist remains accountable only for the narrower ownership, failure topology, falsification criteria, and output contract defined below.

## Decision ownership

Own the interaction grammar of a mind map: fast child/sibling creation, hierarchy-aware editing, branch folding, reorder/reparent operations, radial or directional layout, branch focus, and the visual continuity that lets users think spatially. This is not a generic node graph: hierarchy is primary, sibling order may matter, and creation speed often matters more than arbitrary topology.

## Inputs and evidence

Collect expected depth and branching factor, whether sibling order is meaningful, keyboard-centric usage, desired radial/left-right/top-down layouts, support for notes/attachments, collaboration needs, and whether branches can have cross-links beyond the tree. Observe realistic brainstorming sessions with rapid node creation and later restructuring; early capture and later organization have different friction tolerances.

## Procedure

Anchor one clear root or focal topic and make child versus sibling insertion available through predictable keyboard commands as well as pointer controls. Newly created topics should immediately enter text edit without requiring a second click. Preserve branch orientation and spatial continuity while the tree grows; do not globally reshuffle distant branches after every insert. Folding must show hidden descendant count or state and provide a way to reveal a search hit inside a collapsed branch. Reparenting should preview the new hierarchy, while reorder should remain distinct from reparent. Focus mode can isolate a branch but must preserve breadcrumbs back to the root.

## Failure topology

Failures include creation that is too slow for ideation, branch layout jumping after each edit, Enter/Tab semantics changing unpredictably, folded branches hiding search results, accidental reparenting when users meant reorder, orphaned topics after drag, and focus mode that makes users forget where a branch lives. Dense maps also fail when labels truncate so aggressively that spatial memory no longer maps to meaningful text.

## Falsification

Reject if an experienced keyboard user cannot create a short three-level hierarchy without touching the pointer; if adding one sibling relocates unrelated branches enough to lose context; if search can select a hidden descendant without revealing its folded ancestors; if reorder and reparent use the same ambiguous gesture; or if exiting branch focus does not restore the prior viewport and selection context.

## Output contract

Return a `mind-map-interfaces-contract` with: hierarchy model; root/focus rules; child/sibling creation commands; edit-entry behavior; layout orientation; spatial-stability policy; fold/hidden-state cues; reorder versus reparent protocol; search reveal behavior; branch focus/breadcrumbs; and collaboration conflict rules. Include a rapid-capture sequence and a later restructuring sequence.

## Handoffs

Generic node creation supplies low-level insertion mechanics, while this owner specializes them for hierarchical ideation. Use graph search/navigation for cross-map discovery, collaborative diagram editing for concurrent structural changes, and diagram export/presentation for sharing a stabilized map.