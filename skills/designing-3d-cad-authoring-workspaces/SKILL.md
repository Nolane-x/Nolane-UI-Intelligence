---
name: designing-3d-cad-authoring-workspaces
description: Own the interaction architecture for 3D/CAD authoring where scene hierarchy, spatial selection, modeling state, constraints, assemblies, materials, inspection, and export must remain coherent.
---
# Designing 3D CAD Authoring Workspaces

## Decision ownership

Own the top-level spatial-authoring contract for 3D modeling and CAD workspaces. Decide how viewport, scene hierarchy, properties, modeling mode, selection, transform context, dimensions/constraints, materials, assemblies, inspection, and output coexist. This owner does not define every modeling operation; it ensures 3D state has one understandable authority rather than being spread across disconnected panels and hidden modes.

## Inputs and evidence

Require model/entity taxonomy, coordinate system, units, scene size, modeling paradigms (mesh, solid, parametric, assembly), expected object count, selection modes, camera/view needs, constraints, materials, rendering, export/manufacturing targets, history, and device/input modalities. Inspect representative dense assemblies and precision-edit workflows, not only single-object demo scenes.

## Procedure

Establish stable model identity independent of viewport representation. Make world/local/reference coordinate context visible whenever transforms or dimensions depend on it. Separate navigation from geometry editing and expose current modeling/selection mode persistently. Keep scene hierarchy and viewport selection synchronized. Properties should distinguish geometric definition, transform, material/appearance, metadata, and derived measurements. High-consequence modeling operations need preview/recoverability appropriate to the history model. At scale, support isolation, layers/collections, sectioning, and search without losing the path back to full context. Export/manufacturing readiness must draw from actual model validity, units, and target requirements rather than a generic Download action.

## Failure topology

Failures include users editing in the wrong coordinate system, navigation gestures mutating geometry, hidden edit modes, scene tree and viewport selection diverging, dimensions shown without unit context, assembly instances mistaken for unique geometry, and rendered appearance obscuring topology/selection. Another failure is exporting a visually correct model with invalid scale, missing bodies, or target-incompatible geometry.

## Falsification

Reject if a user cannot state current selection and modeling mode before an edit; if world/local transform context is hidden; if navigation can accidentally commit geometry changes; if the same model entity has inconsistent identity between hierarchy and viewport; if scale/units cannot be verified before export; or if destructive operations cannot be recovered according to the product's history contract.

## Output contract

Return a `3d-cad-authoring-workspaces-contract` containing: model/entity taxonomy; coordinate/unit model; viewport-navigation/edit separation; selection/mode state; scene hierarchy; property domains; history/preview rules; isolation/layers; precision context; assembly/instance semantics; validation/readiness; and export/manufacturing handoff. Include one dense assembly and one precision modeling scenario.

## Handoffs

Delegate scene hierarchy, viewport navigation, camera views, 3D snapping, layers, mesh modes, modeling operations, measurements, constraints, assemblies, materials, lighting, UVs, annotations, sections, clash inspection, rendering, and manufacturing/export to dedicated owners. Generic canvas/transform/snapping skills supply lower-level interaction mechanics only.