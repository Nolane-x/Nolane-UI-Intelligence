---
name: designing-section-and-cut-planes
description: Own non-destructive section/cut-plane inspection in 3D models, including plane definition, orientation, multiple sections, cap display, scope, clipping direction, persistence, and measurement context.
---
# Designing Section and Cut Planes

## Decision ownership

Own visual inspection by clipping or sectioning model geometry without altering source solids. Decide section-plane creation, coordinate/reference, direction, offset, multiple-plane combination, affected scope, cap/hatch display, persistence, naming, and distinction from destructive geometry cuts.

## Inputs and evidence

Require model coordinate system, section implementation, object/layer scope, multiple-plane limits, cap/material behavior, measurement support, saved-view linkage, export support, and performance constraints. Identify whether section is purely visual or can generate section curves/documents.

## Procedure

Represent the active plane visibly with orientation and clipping side. Plane movement supports numeric offset and snapping/reference alignment. Multiple active planes need a manageable list and clear combination semantics. Sectioned-away geometry should remain present in hierarchy and searchable. Cap/hatch is display state and must not imply new solid geometry unless explicitly generated. Measurements and annotations taken in section mode should record that context. Saving a view may optionally capture active sections under explicit scope.

## Failure topology

Failures include users thinking clipped geometry was deleted, clipping direction reversed unexpectedly, hidden active section planes causing missing objects, multiple planes producing an empty scene with no explanation, cap surfaces mistaken for authored geometry, and exported screenshots losing plane context. Another failure is model selection acting on invisible clipped components with no cue.

## Falsification

Reject if section mode cannot be identified; if source geometry changes from a visual section operation; if active plane/direction is invisible; if multiple-plane effects cannot be isolated; if cap display looks editable as real geometry; or if measurements/annotations lose section context after reopening.

## Output contract

Return a `section-and-cut-planes-contract` with: plane identity; coordinate/orientation/offset; clipping side; scope; multiple-plane logic; cap/hatch display; hierarchy/selection behavior; measurement/annotation context; saved-view persistence; and export representation. Include one multiple-plane empty-result scenario.

## Handoffs

Viewport navigation helps orient sections, snapping/measurement supplies precision, camera views may capture section state, and destructive boolean/split modeling remains a separate operation.