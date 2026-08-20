---
name: designing-manufacturing-and-export-handoff
description: Own preparation of 3D/CAD models for downstream manufacturing or interchange, including target process, units, coordinate system, body selection, tolerances, validation, tessellation, metadata, and export evidence.
---
# Designing Manufacturing and Export Handoff

## Decision ownership

Own the boundary where an authored model becomes an artifact for manufacturing, fabrication, simulation, or external CAD interchange. Decide target/process profile, selected bodies/assemblies, units, coordinate/origin, orientation, tessellation/tolerance, metadata/BOM, validation, warnings, and handoff package. Generic export configuration does not own geometric/manufacturing readiness.

## Inputs and evidence

Require target format/process, model units, body/assembly state, coordinate requirements, tolerance, solid/manifold validity, material/BOM metadata, naming, layer conventions, mesh tessellation parameters, unresolved clashes, and recipient/tool constraints. Identify whether export is authoritative manufacturing data or merely visualization.

## Procedure

Select a named target profile rather than exposing undifferentiated format options. Preview included bodies/assemblies and exclude hidden construction/reference content intentionally. Make units, scale, origin, and orientation explicit. Run target-relevant validation: closed bodies, normals/manifold for mesh targets, unsupported features, minimum thickness if available, unresolved references, required metadata, and clash status where applicable. Tessellation settings should explain geometric tolerance, not only "quality high". Produce a manifest with source model revision and export settings; do not overwrite the source model to fit export constraints without a separate modeling action.

## Failure topology

Failures include millimeter/inch scale errors, wrong coordinate origin, hidden bodies omitted unexpectedly, construction geometry included, tessellation too coarse, invalid solids exported without warning, assembly metadata lost, and exported files detached from model revision/settings. Another failure is a successful export toast interpreted as manufacturability certification.

## Falsification

Reject if target units/orientation cannot be confirmed; if included body scope is ambiguous; if known target-invalid geometry is not surfaced; if tessellation tolerance has no meaningful unit/preview; if source model revision cannot be traced; or if the UI claims manufacturing correctness solely because file serialization succeeded.

## Output contract

Return a `manufacturing-and-export-handoff-contract` with: target process/format profile; source revision; included entities; units/scale; coordinate/orientation; geometry/tolerance settings; target validation findings; material/BOM metadata; unresolved-risk disclosure; export manifest; and destination artifact identity. Include one unit-mismatch safeguard scenario.

## Handoffs

Assembly/material owners provide product structure, clash/measurement owners provide readiness evidence, render export remains separate for imagery, and generic file/export skills handle destination/progress after the technical package is defined.