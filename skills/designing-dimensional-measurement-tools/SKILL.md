---
name: designing-dimensional-measurement-tools
description: Own precise 3D/CAD measurement of distance, angle, radius, diameter, area, volume, coordinates, clearances, and references with units, snap provenance, and persistent annotations.
---
# Designing Dimensional Measurement Tools

## Decision ownership

Own measurement interaction that interrogates model geometry without necessarily constraining it. Decide measurement type, reference picks, snapping, coordinate basis, units/precision, live preview, cumulative measurements, persistent annotations, tolerance, and relation to derived model properties. This differs from parametric dimensions that drive geometry.

## Inputs and evidence

Require model units/scale, geometry types, coordinate systems, snapping, precision/tolerance, measurement APIs, physical properties, section/isolation state, and export/annotation needs. Identify whether transformed/instanced geometry measurements use evaluated world geometry or source definition.

## Procedure

Make selected references explicit and highlight exact points/edges/faces used. Display measurement type, value, unit, precision, and coordinate/reference frame. Allow cycling candidate snap points when geometry overlaps. Distinguish minimum distance/clearance from point-to-point distance. Persistent measurements should track stable references and show broken/stale state if topology changes. Derived area/volume/mass values must state assumptions such as closed body and material density. Copy/export should retain units.

## Failure topology

Failures include measuring a hidden back vertex, unitless numbers, source-versus-instance coordinates mixed, persistent dimensions silently retargeting after topology edits, minimum distance confused with selected-point distance, and volume shown for non-closed geometry. Another failure is rounding enough to conceal tolerance violations.

## Falsification

Reject if users cannot identify the measured references; if units/reference frame are absent; if persistent measurement can silently bind to a different entity after edit; if invalid solid properties appear valid; if precision is insufficient for stated tolerance; or if instance transforms are ignored without disclosure.

## Output contract

Return a `dimensional-measurement-tools-contract` with: measurement types; reference selection/snapping; coordinate frame; units/precision; evaluated/source geometry rule; live preview; persistent reference identity; stale/broken state; derived-property assumptions; and copy/export representation. Include one topology-change invalidation case.

## Handoffs

3D snapping selects references, parametric constraints may convert measurements into driving dimensions, clash inspection uses clearance metrics, and annotations can publish persistent results.