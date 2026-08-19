---
name: designing-pagination
description: Use when a large result set needs addressable pages, stable continuation, range context, and navigable state that can survive filtering, sorting, deep links, and accessibility use.
---

# Designing Pagination

## Parent Contract
**Required parent:** `designing-navigation`.

This faculty owns explicit page-addressable continuation. It does not decide result ranking or filtering semantics. Pagination is appropriate when users benefit from bounded chunks, resumable locations, deterministic URLs, or a clear sense of position within a finite or countable collection.

## Decision Boundary
Choose the pagination model from backend truth. Offset/page-number pagination can support stable page labels when ordering is sufficiently stable; cursor pagination may be more correct for changing datasets but cannot honestly promise arbitrary “page 37” jumps without additional indexing. The UI must not fabricate total counts or page numbers the data source cannot guarantee.

Preserve query context in navigation state: page, sort, filters, page size, and search terms should have deliberate URL/history semantics. Changing a filter usually invalidates the old page position; decide whether to reset to the first page or preserve an equivalent anchor. Returning from a detail page should restore the list position and page rather than starting over.

Page controls need useful targets, not every possible number. First/previous/next/last, a bounded number window, or a jump control can be combined according to scale. Disabled controls must remain understandable. Announce loaded page/range changes without stealing focus.

## Failure Topology
- UI renders page numbers for a cursor API and those numbers drift as records are inserted.
- Applying a filter leaves the user on page 12, which is now empty despite earlier matching results.
- Browser Back restores filters but not page position.
- Page-size changes silently reinterpret the current location and skip records.
- Tiny page-number targets become unusable at high zoom or on touch.
- A result count is shown as exact even though the backend only provides an estimate.

## Falsification and Recovery
Falsify with records inserted/deleted during browsing, deep links to later pages, filter/sort changes, page-size changes, browser history, return from a detail view, keyboard-only operation, screen reader announcements, and a backend with unknown total count. The design fails if page labels imply addressability the data source cannot preserve or if changing context causes silent record loss.

Recover by matching controls to the backend continuation model, encoding meaningful list state, resetting/re-anchoring on query changes, preserving return context, and labeling totals as approximate or unknown when necessary.

## Output Contract
Return `pagination-contract` with continuation model, addressability guarantees, URL/history state, query-change behavior, page-size semantics, control set, total-count authority, return-position policy, accessibility announcements, and dataset-mutation falsification cases.