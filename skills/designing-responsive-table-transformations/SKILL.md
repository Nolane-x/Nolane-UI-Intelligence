---
name: designing-responsive-table-transformations
description: Transform tabular data for constrained widths without destroying comparison, row identity, headers, actions, or accessible relationships.
---

# Designing responsive table transformations

Tables encode relationships through two-dimensional alignment. On narrow surfaces, simply stacking every cell into cards can destroy the comparison task that justified a table. Use this skill when data tables must remain useful under constrained space.

## Decision ownership

Own which table properties may adapt: column priority, horizontal scrolling, pinned identity columns, disclosure of secondary fields, row-to-card transformation, action placement, and summary views. Decide when preserving the actual table is more important than avoiding horizontal scroll.

## Inputs and evidence

Collect comparison tasks, essential columns, column widths under localization, sortable/filterable state, row actions, selection, grouped headers, sticky regions, assistive-technology requirements, and device use. Identify whether users compare across rows, inspect one record at a time, or perform batch actions.

## Procedure

Classify columns by identity, comparison value, and secondary detail. Preserve the dimensions needed for the dominant task. Horizontal scrolling can be correct when alignment matters; provide pinned row identity or clear scroll affordance rather than hiding columns arbitrarily.

If transforming rows into cards, repeat labels explicitly and preserve sorting, selection, and actions. Do not simulate a table visually while removing header-cell relationships needed by assistive technology. For column disclosure, make hidden active sort/filter state visible.

Test dense data and long values, not a five-row demo.

## Failure topology

Card transformations increase vertical length and eliminate cross-row scanning. Hidden columns can contain active filters or important exception states. Horizontal scroll without row identity causes users to lose which record they are reading.

A responsive table may also duplicate controls or change selection semantics between modes.

## Falsification

Give users actual comparison and batch-edit tasks at narrow widths. Test keyboard and screen-reader navigation, long values, many rows, pinned columns, active sort/filter, and selection across a state change. Resize while horizontally scrolled and ensure context is recoverable.

If the chosen transformation makes the primary analytical task substantially slower, it fails even if every value remains technically reachable.

## Output contract

Produce a `responsive-table-transformations-contract` with task model, column priority, chosen transformation per state, scroll/pinning behavior, hidden-state signaling, selection/action parity, accessibility semantics, and performance/usability evidence.

## Handoffs

Use data-grid specialist skills for full grid behavior, `designing-responsive-priority-collapse` for secondary columns, `designing-responsive-density-shifts` for row density, and `verifying-responsive-state-parity` for state retention.