---
name: designing-3d-layer-and-collection-management
description: Use when this specialist's decision ownership is materially in scope. Own non-hierarchical organization of 3D content through layers, collections, tags, visibility sets, renderability, selectability, membership, and view-specific overrides.
---
# Designing 3D Layer and Collection Management

## Parent Contract

**Required parent:** `designing-3d-cad-authoring-workspaces`.

Inherit the broader routing and decision boundary from this canonical parent; this specialist remains accountable only for the narrower ownership, failure topology, falsification criteria, and output contract defined below.

## Decision ownership

Own orthogonal organization of scene entities independent of parent-child geometry. Decide layers/collections/tags, multi-membership, visibility, renderability, selectability, lock, nested organizational groups, default membership, and view-specific overrides. This owner differs from scene hierarchy and assembly structure.

## Inputs and evidence

Require organization model, whether multi-membership is supported, expected layer count, import conventions, visibility/render/selectability states, collaboration, permissions, saved views, export filtering, and cross-reference to scene hierarchy. Identify semantic layers such as discipline/system versus purely workflow layers.

## Procedure

Make membership and state explicit in both layer manager and selected-object inspector. If objects can belong to multiple collections, distinguish visibility combination logic (any/all/override). Keep visibility, selectability, and renderability separate. Bulk membership changes need affected-count preview. View-specific overrides should clearly indicate they differ from global state and be recoverable/resettable. Imports should map external layers predictably without flattening names silently. Hidden layers containing selected/errored objects need cues.

## Failure topology

Failures include hidden objects still selectable unexpectedly, one eye icon overloaded for visibility/renderability, multi-membership causing an object to reappear mysteriously, view overrides mistaken for global changes, and imported layers merging due name collision. Another failure is layer lock preventing edits but giving no explanation when a viewport action fails.

## Falsification

Reject if object visibility cannot be explained from its memberships; if selectability/renderability are conflated; if a view override is visually indistinguishable from global state; if bulk membership can silently affect hidden objects; if locked-layer rejection has no source cue; or if imported layer collisions cannot be reviewed.

## Output contract

Return a `3d-layer-and-collection-management-contract` with: organizational entities; membership rules; multi-membership visibility logic; visibility/selectability/renderability/lock states; nesting; bulk membership; view overrides; import mapping; hidden-selected/error cues; and reset behavior. Include one multi-membership override case.

## Handoffs

Scene hierarchy owns parentage, named camera views may capture visibility overrides, render preview consumes renderability, and export/manufacturing can filter by layer/collection under explicit rules.