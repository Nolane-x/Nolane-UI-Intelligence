---
name: designing-map-layer-management
description: Use when users enable, order, style or inspect multiple geospatial layers and the interface must expose visibility, scale availability, legend, source, opacity, ordering and loading/error state.
---

# Designing Map Layer Management

## Parent Contract
**Required parent:** `designing-geospatial-interfaces`.

This faculty owns the interaction model for map layers. It does not define cartographic styling algorithms, data licensing or the content of domain datasets.

## Decision Boundary
A layer has identity, type, visibility, draw order, scale/zoom range, data source/freshness, legend, loading/error status and optional style/opacity controls. Separate **not visible because toggled off** from **not visible at this scale**, **not loaded**, **filtered empty** and **permission unavailable**. A blank map should not make users guess which condition applies.

Layer order matters when geometry overlaps. If users can reorder, preview/announce the stacking consequence and keep basemap/reference layers constrained when necessary. Do not let drag reorder visually imply that a raster overlay can become an interactive point layer if their capabilities differ.

Legends belong to the active styling and filter state. If thresholds/categories change, update the legend from the same style configuration; stale legends are analytical defects. Complex layers may expose sublayers/categories but deep nested controls can overwhelm the map—use grouping/search and persistent active-state summaries.

Scale visibility should be discoverable. A disabled layer checkbox may mean permission, unsupported scale or loading; use explanatory state and optionally offer “zoom to visible range.” Expensive layers need progressive loading/cancel and indication of stale tiles/features where material.

Source/provenance is especially important for regulatory, scientific or emergency maps. Provide metadata/detail routes without cluttering primary layer controls.

## Failure Topology
- Layer is checked but nothing appears because current zoom is outside its range with no explanation.
- Legend colors no longer match features after filter/style change.
- Reordering an overlay hides labels/critical boundaries unexpectedly.
- Failed network tiles look identical to an intentionally empty dataset.
- Ten nested layer groups require dozens of clicks to understand what is active.
- User assumes a layer is current although source timestamp is days old.

## Falsification and Recovery
Falsify with many layers, conflicting draw order, zoom limits, loading failures, filter/style changes, stale data, permission loss and saved layer state. Reconcile active legend and rendered feature scope to layer configuration.

Recover by first-class layer state, scale explanations, constrained ordering, configuration-derived legends, provenance/freshness metadata and manageable grouping/search.

## Output Contract
Return `map-layer-management-contract` with layer state schema, visibility/scale rules, ordering constraints, legend binding, style/opacity controls, loading/error/freshness, provenance, persistence and render-config parity tests.