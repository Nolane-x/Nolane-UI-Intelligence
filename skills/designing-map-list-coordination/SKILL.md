---
name: designing-map-list-coordination
description: Use when the same geographic results appear in a map and list/table and the interface must coordinate selection, hover/focus, viewport filtering, sorting and responsive mode without creating two competing sources of truth.
---

# Designing Map and List Coordination

## Parent Contract
**Required parent:** `designing-geospatial-interfaces`.

This faculty owns linked map/list representations of the same result set. It does not define list search/filtering or marker clustering themselves.

## Decision Model
Establish one result model with stable IDs. Map markers/features and list rows are projections of those records; selection on either surface updates shared selection, not two loosely synchronized copies. Distinguish selected record, focused/hovered record and records merely within the current viewport.

Decide whether viewport changes filter the list. “Search this area” is a user command with clear scope; continuously filtering the list on every pan can make results vanish while users compare. If automatic viewport filtering is justified, show a persistent `Map area` filter and provide a way to detach/list all results.

Sorting often differs: list may sort by relevance, price or name while map is spatial. Avoid implying top-list order corresponds to geographic priority. Distance sort needs a declared origin. Selecting a list item may pan/zoom the map only enough to reveal it, not reset the entire context unless requested.

Hover coupling can help pointer users but must not become the only identification path. Keyboard focus on a list row can highlight its marker; map feature activation should move or expose corresponding list context without stealing focus unpredictably.

Responsive layouts may show map and list side by side on desktop but one at a time on mobile. Shared filters/selection must survive switching modes; the hidden surface should not reset state.

## Failure Topology
- Panning one pixel refilters the list and users lose the row they were reading.
- Clicking a list item zooms aggressively and destroys comparison context.
- Marker selection and list selection use separate states and highlight different records after refresh.
- Mobile switching from List to Map resets filters/selection.
- Hover synchronizes surfaces but keyboard focus does not.
- “2 km away” sort uses device location while map visually centers somewhere else with no origin disclosure.

## Falsification and Recovery
Falsify with pan/zoom, explicit vs automatic viewport filter, list sorting, selection from both surfaces, refresh/reorder, keyboard focus and mobile mode switching. Assert map/list selected IDs and filter scope remain consistent.

Recover by centralizing result/selection state, making viewport filtering explicit, minimizing auto-pan, preserving state across presentation modes and exposing distance/filter origin.

## Output Contract
Return `map-list-coordination-contract` with shared result identity, selection/focus coupling, viewport-filter policy, list sort/origin, pan/zoom response, responsive modes, clustering handoff, accessibility behavior and cross-surface parity tests.