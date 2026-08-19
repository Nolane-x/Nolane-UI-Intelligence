---
name: designing-accessible-data-table-navigation
description: Use when tabular relationships, sorting, selection, virtualization, grouped headers, or inline actions must remain understandable and operable through nonvisual and keyboard navigation.
---

# Designing Accessible Data Table Navigation

## Parent Contract
**Required parent:** `designing-accessible-interfaces`.

This faculty owns accessibility semantics and navigation for true data tables. It does not redesign generic table visuals or spreadsheet editing. The core question is whether row/column relationships, header scope, stateful operations, and focus behavior remain coherent when a user cannot rely on visual alignment.

## Decision Boundary
Confirm that the content is actually tabular before adopting table/grid semantics. Define row and column headers, multi-level header relationships, captions or contextual names, sortable-state exposure, selected-row semantics, and how inline controls are reached. Native table navigation may be preferable for read-mostly data; a keyboard-managed grid pattern is justified only when cell-level interaction requires application-style movement.

Virtualization must not create a fictitious row universe. Expose meaningful position/count information when rows are windowed, and preserve focus when a recycled DOM cell receives new data. Sticky visual headers do not replace semantic header associations. Responsive transformations into cards or stacked rows must preserve labels for every value.

## Failure Topology
- Layout tables use data-table semantics and create meaningless row/column announcements.
- Visual headers are built with generic divs and values lose their field names nonvisually.
- Sorting changes rows but does not expose the active sort key/direction.
- Virtualized recycling makes screen readers announce stale cell content or wrong row positions.
- Every inline action becomes a tab stop in hundreds of rows with no efficient row navigation.
- Mobile card transformation drops column labels because visual position formerly carried the meaning.

## Falsification and Recovery
Navigate representative tables with screen-reader table commands, keyboard-only sorting/selection/actions, high zoom, virtualization, grouped headers, empty states, and responsive transformations. The design fails if a value cannot be associated with its header, if state changes are silent, or if focus identity changes when scrolling virtualized data.

Recover by restoring native structural semantics where possible, explicitly modeling headers and sort/selection states, choosing a justified grid interaction model, stabilizing virtual row identity, and adding labels to responsive representations. Test large datasets, not only demo rows.

## Output Contract
Return `accessible-data-table-contract` with table/grid eligibility, header relationships, caption/context naming, sorting/selection semantics, inline-action navigation, virtualization identity rules, responsive transformation obligations, and assistive verification cases.
