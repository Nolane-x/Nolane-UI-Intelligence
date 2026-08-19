---
name: designing-range-selection
description: Use when users select contiguous spans in ordered lists, grids, timelines or text-like object collections and the interface must preserve anchor, extent and ordering semantics under sorting, filtering and direction reversal.
---

# Designing Range Selection

## Parent Contract
**Required parent:** `designing-multi-selection-models`.

This specialist owns contiguous selection between an anchor and an extent. It does not define general additive selection or geometric lasso.

## Decision Model
A range needs an **anchor identity** and a current **extent identity** evaluated in a declared ordering. Shift-click/Shift-arrow typically expands or contracts relative to that anchor. Reversing direction past the anchor should produce a predictable range, not accumulate old items.

Define what ordering means. In a sorted table, the range is usually visual/current order, not original database order. In a timeline, it may be time order. In a tree, “contiguous” can mean visible flattened order and collapsing nodes can hide selected descendants. Document the product interpretation.

Filtering/sorting while a range exists can invalidate spatial continuity. Preserve membership IDs if that is the selection model, but reset or relocate the range anchor only by explicit policy. A stale anchor pointing to a hidden/deleted item makes the next Shift selection surprising.

Grid ranges add two-dimensional bounds: rectangular cell regions, full rows/columns or irregular additive ranges. Clarify whether range extension preserves a rectangle and which cell is active for keyboard operations.

## Failure Topology
- Shift-select after sorting uses pre-sort indices and selects unrelated rows.
- Reversing direction keeps old selected items instead of shrinking the range.
- Anchor is deleted but remains implicit, so next range starts from nowhere visible.
- Range selection in a tree includes hidden collapsed descendants unexpectedly.
- Grid range has no clear active cell for paste or keyboard editing.

## Falsification and Recovery
Create ranges forward/backward, cross the anchor, sort/filter, delete anchor, collapse hierarchy, page/virtualize, and use keyboard only. Log anchor/extent IDs and resulting membership after every event. Any result dependent on stale array index rather than declared order fails.

Recover by keying anchor to semantic identity, recalculating against current ordering, resetting visibly when the anchor becomes invalid and separating rectangular grid range from general multi-selection.

## Output Contract
Return `range-selection-contract` with order definition, anchor/extent identity, extension/reversal behavior, modifier interaction, invalid-anchor policy, hierarchy/grid rules, visible feedback and sequence tests.