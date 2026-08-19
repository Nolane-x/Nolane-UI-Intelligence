---
name: designing-geospatial-interfaces
description: Use when location, extent, distance or geographic relationships are primary to a task and the interface must coordinate map viewport, spatial selection, scale, projection, accuracy and non-map alternatives.
---

# Designing Geospatial Interfaces

## Parent Contract
**Required parent:** `designing-data-dense-interfaces`.

This faculty owns the geospatial workspace as a coherent interaction system. Marker clustering, layer management, map-list coordination and route comparison route to specialist children. It does not choose GIS algorithms, certify coordinates or replace domain cartographic expertise.

## Decision Boundary
A map is not decorative background. Define the geographic objects users reason about: points, paths, polygons, raster fields, administrative regions, live positions, search results or routes. Each object needs stable identity, source/provenance where material, coordinate reference assumptions and an interaction representation independent of the current pixel projection.

Viewport state includes center/extent, zoom/scale, bearing where supported and projection. Controls should preserve task context when fit-to-selection, search result, geolocation or layer change moves the view. Avoid automatic viewport jumps while users are manually inspecting a different area; offer a “return to live/result” path instead.

Location precision must be honest. A GPS position with 80 m uncertainty should not render as an exact pin without accuracy indication when precision affects decisions. Geocoded addresses, manually placed points and device positions can have different confidence/provenance. Do not let a crisp marker imply certainty the source lacks.

Spatial scale changes meaning. At low zoom, individual objects may need aggregation/generalization; at high zoom, labels/details can appear. Preserve semantic continuity across levels rather than swapping to unrelated representations. Scale bars and distance measurements should use domain-appropriate units and account for projection/geodesic semantics through the mapping engine.

Map interaction must have alternatives when the task is material: searchable list/table, coordinate entry, accessible result details or structured route steps. Keyboard panning/zooming alone is not equivalent to visually discovering an unlabeled polygon.

## Failure Topology
- Exact-looking pin hides a kilometer-scale location uncertainty.
- Search result automatically recenters every time live data refreshes, preventing manual inspection.
- Low-zoom markers overlap into an unreadable pile instead of aggregating.
- Selection is stored by screen position and points to the wrong feature after projection/zoom changes.
- Map is the only route to select a location, excluding nonvisual users.
- Projection distortion is ignored when measuring a domain where distance accuracy matters.

## Falsification and Recovery
Falsify at world/city/street scales, projection changes, uncertain positions, live updates, geolocation denied, keyboard/screen reader and list-to-map selection. Verify semantic feature IDs/coordinates survive viewport changes.

Recover by separating world data from viewport projection, showing accuracy/provenance, suppressing unwanted auto-follow, generalizing by scale and providing structured non-map access to material objects/actions.

## Output Contract
Return `geospatial-interface-contract` with geographic object model, viewport/projection state, accuracy/provenance, scale-dependent representation, navigation/selection semantics, live-follow behavior, units/measurement handoff, accessible alternatives and coordinate-identity tests.