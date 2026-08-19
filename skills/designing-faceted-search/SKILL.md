---
name: designing-faceted-search
description: Use when users narrow a result universe through structured facets and the interface must preserve query semantics, counts, multi-select logic, dependencies, and reversible refinement.
---

# Designing Faceted Search

## Parent Contract
**Required parent:** `designing-search`.

This faculty owns refinement of an existing search/browse universe through structured dimensions. It is not a generic filter-builder for arbitrary analytical predicates; facets are discoverable values derived from the result domain and must communicate how each selection changes that universe.

## Decision Model
Define facet semantics before controls. Within a facet, multiple values may be ORed (“red or blue”) or ANDed (“has Wi‑Fi and parking”); across facets they are often ANDed, but domain rules can differ. The UI must not leave this logic to guesswork when it materially changes results.

Counts need a declared basis: current result set, result set with this facet excluded, approximate index count, or unavailable. Showing `Color: Red (18)` after Red is selected can be misleading if the count calculation includes or excludes the selection inconsistently. Disabled zero-count options may aid understanding, but hiding them can be better when the value space is enormous; choose intentionally.

Selections must remain visible outside collapsed panels, especially on mobile. Chips, a summary row, or persistent selected-count cues should support rapid removal. If one facet changes available values in another, update without silently deleting a still-valid selection. Query state should be shareable/restorable when the product promises navigable search URLs.

## Failure Topology
- Multi-select uses OR in one facet and AND in another with identical control treatment.
- Counts are stale or computed from a different scope than the visible results.
- Mobile filter sheet closes and users cannot see that five filters remain active.
- Selecting a parent category silently deletes a compatible child selection.
- Facet values reorder on every count update, destroying spatial memory.
- Clearing search terms unexpectedly clears all structured facets without a stated reset model.

## Falsification and Recovery
Falsify with multi-select values, dependent facets, zero-result combinations, rapidly changing counts, back/forward navigation, saved URLs, mobile sheet interaction, keyboard/screen-reader use, and an index that only provides approximate counts. The design fails if the same visible selections can map to ambiguous boolean logic or if active refinement becomes invisible.

Recover by specifying boolean semantics, defining count scope and approximation, persisting visible active selections, stabilizing value order, separating query reset from facet reset, and serializing a canonical refinement state.

## Output Contract
Return `faceted-search-contract` with facet dimensions, within/across-facet logic, value/count authority, dependency behavior, active-selection representation, reset semantics, ordering, responsive presentation, URL persistence, accessibility behavior, and falsification combinations.