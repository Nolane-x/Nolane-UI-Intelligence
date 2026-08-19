---
name: designing-virtualized-grids
description: Use when a large grid renders only a moving window of rows or columns and the interface must preserve logical identity, focus, selection, scrolling, measurements and accessibility despite DOM recycling.
---

# Designing Virtualized Grids

## Parent Contract
**Required parent:** `designing-data-dense-interfaces`.

This specialist owns user-facing consequences of row/column virtualization. It does not choose the virtualization library or performance implementation authority.

## Decision Boundary
Virtualization is an implementation strategy that must not leak as broken semantics. Model the dataset in logical coordinates independent of mounted DOM. Focus, selection, editing, errors and scroll-to-item all bind to stable record/column IDs or indices from the authoritative model, never the recycled element instance.

Dynamic row heights complicate scroll position. If heights are estimated then measured, preserve the user’s visual anchor while corrections occur. Prepending or expanding rows above the viewport should not make the reading target jump. Column virtualization must coordinate pinned columns and horizontal focus navigation.

Keyboard navigation can request an offscreen cell; the system should scroll/mount it and then establish focus deterministically. Screen reader support may require exposing row/column counts/indices and careful managed focus; do not create thousands of hidden DOM rows just to look accessible if that destroys performance.

Editing is a retention boundary. Decide whether the active edit pins its row, commits/cancels before unmount, or uses a portal/overlay tied to semantic coordinates. Silent draft loss is unacceptable.

## Failure Topology
- Recycled row keeps selected CSS and visually selects a different record.
- PageDown changes logical focus but DOM focus stays on the recycled old node.
- Dynamic height measurement jumps the viewport after image/content load.
- Screen reader announces “row 5 of 20” although dataset has 100,000 rows.
- Editing row scrolls out and draft disappears.
- Find/jump cannot focus a far item because it is not mounted yet.

## Falsification and Recovery
Scroll rapidly, select/edit, jump to distant records, resize dynamic rows, prepend data, pin columns, screen-reader navigate and mutate dataset while offscreen. The contract fails if semantic state follows DOM reuse rather than logical identity.

Recover by centralizing logical state, anchor-preserving measurement correction, deterministic scroll-then-focus, explicit edit retention and accurate accessible index/count metadata.

## Output Contract
Return `virtualized-grid-contract` with logical identity model, render window, scroll-anchor policy, dynamic measurement, offscreen focus/navigation, selection/edit retention, pinned-region coordination, accessibility metadata and recycling tests.