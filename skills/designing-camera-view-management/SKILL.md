---
name: designing-camera-view-management
description: Use when this specialist's decision ownership is materially in scope. Own named 3D views and cameras, including save/restore, perspective parameters, clipping, target, lock, update, thumbnails, presentation, and distinction between editor camera and render camera.
---
# Designing Camera View Management

## Parent Contract

**Required parent:** `designing-3d-cad-authoring-workspaces`.

Inherit the broader routing and decision boundary from this canonical parent; this specialist remains accountable only for the narrower ownership, failure topology, falsification criteria, and output contract defined below.

## Decision ownership

Own persistent camera/view entities beyond transient viewport navigation. Decide named views, render cameras, editor view versus active camera, focal/projection settings, clipping, targets, locking, update-from-current, ordering, thumbnails, and sharing/presentation. This owner prevents a saved engineering viewpoint from being an opaque bundle of coordinates.

## Inputs and evidence

Require camera/view types, transform/projection parameters, render settings linkage, section/isolation context, model revision behavior, collaboration, permissions, and presentation/export use. Determine whether saved views capture only camera or also visibility/layer/section state.

## Procedure

Explicitly define saved-view scope: camera only or a view state containing visibility, section, selection, render style, and annotations. Give stable names plus preview thumbnails generated from known model revision. Switching to a render camera should clearly enter camera view without overwriting the editor camera. Updating a named view from current state needs deliberate commit and history where shared. Locked views prevent accidental edits while still permitting temporary navigation that can be reset. If model geometry changes, show stale/missing target conditions instead of silently re-aiming.

## Failure topology

Failures include saving a view that unexpectedly captures hidden layers, changing the editor camera and accidentally changing production render framing, shared views overwritten without attribution, thumbnails no longer matching state, and deleted targets producing bizarre camera orientation. Another failure is "reset view" whose target saved state is unclear.

## Falsification

Reject if users cannot know what state a saved view captures; if entering/exiting render camera can overwrite it accidentally; if shared-view edits lack provenance; if stale thumbnails/state are undetectable; if locked views can be modified silently; or if reset cannot identify its restoration source.

## Output contract

Return a `camera-view-management-contract` with: camera/view taxonomy; saved-state scope; projection/focal/clipping parameters; active/editor distinction; save/update/lock/reset; thumbnail freshness; model-revision/target handling; shared ownership/history; and presentation/export linkage. Include one shared locked view and one deleted-target scenario.

## Handoffs

Viewport navigation supplies transient camera motion, lighting/render preview consumes render cameras, section planes may be captured as view state, and presentation/export uses named viewpoints.