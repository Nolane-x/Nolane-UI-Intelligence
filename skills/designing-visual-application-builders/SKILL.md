---
name: designing-visual-application-builders
description: Use when people author executable interfaces visually and canvas, hierarchy, component instances, styles, data, events, responsive rules, preview, and publication must remain one coherent source of truth.
---

# Designing Visual Application Builders

## Parent Contract

**Required parent:** `designing-editor-canvas-workspaces`.

This owner governs the top-level interaction architecture of visual website/app builders. It is not a general canvas editor: the artifact being manipulated must eventually execute as an interface with hierarchy, layout, style, data, events and runtime constraints. Specialist children own individual mechanisms such as breakpoint editing, overrides and data binding; this owner ensures they compose without creating several contradictory models of the same application.

## Decision ownership

Define the authored model before arranging panels. Establish what is canonical: a component/tree graph, document schema, source code, hybrid model or generated representation. Canvas pixels, layers tree, properties inspector and code preview must all be views or controlled mutations of that same authority. If one surface can express a state another cannot round-trip, name that asymmetry explicitly.

Distinguish **selection context** from **editing scope**. A user may visually select a nested element while editing an instance, component definition, repeated collection item, breakpoint override or runtime state. Always expose which scope a property mutation will affect. The builder must make structural parentage, component ownership, inherited style, data context and interaction context inspectable without requiring users to infer them from geometry.

The shell must support a progression from authoring to evidence. Preview is not merely hiding editor chrome: runtime navigation, focus, scrolling, data, permissions, responsive behavior and interactions need a mode where editor selection/drag handles cannot alter results. Publication introduces another authority boundary—what revision, environment and dependencies are actually being released.

Treat undo/history as semantic builder operations. Moving a child, converting it to a reusable component, rebinding data and changing a breakpoint are different commands with different downstream effects. Generated code or schema transformations should preserve stable identities so history, collaboration and diagnostics do not drift when visual layout changes.

## Evidence

Study mature visual builders and design/code tools, authored project schemas, real nested components, responsive variants, data-driven pages, collaboration traces, runtime previews and export/publish behavior. Use dense applications, not only landing-page demos. Evidence should include a case where canvas and tree disagree visually, a component instance with overrides, a data-bound repeated structure, and a failed publish/validation state.

## Failure topology

A builder fails when the canvas is authoritative until code changes, then the code is authoritative until the inspector edits again. Other failures include hidden editing scope, irreversible detach-from-component actions, inspector controls that write invalid runtime state, selections that point to generated wrapper nodes rather than meaningful authored objects, and preview that still intercepts gestures for editor selection.

An especially costly failure is non-round-trippable convenience: a visual operation generates code/schema that can no longer be represented by the builder, so future visual edits destroy hand-written intent without warning.

## Falsification

Author a responsive data-bound component, create instances with overrides, rearrange via both canvas and hierarchy, wire an event, preview at several widths, inspect generated/runtime representation, undo/redo across structural changes, collaborate on the same subtree and publish a revision. The contract is falsified if object identity changes unexpectedly, if one editor surface shows stale state, if editing scope is ambiguous before commit, or if preview/publish cannot state which revision and runtime behavior it represents.

## Recovery

Re-establish one canonical authored model and make every mutation declare its target identity and scope. Quarantine transformations that cannot round-trip and expose an explicit code-owned or detached boundary rather than pretending full visual control. Reconcile stale selection by stable IDs, not screen coordinates. When publish state diverges from editor state, bind diagnostics to exact revisions and provide a path back to the authoring object that caused the failure.

## Output contract

Return a `visual-application-builders-contract` containing canonical document model, object identities, canvas/tree/inspector authority map, editing scopes, selection semantics, component/data/event relationships, preview isolation, publish revision model, round-trip boundaries, semantic history, collaboration assumptions, and end-to-end builder verification scenarios.

## Handoffs

Delegate canvas/tree identity to `designing-canvas-hierarchy-synchronization`, responsive authoring to `designing-responsive-breakpoint-authoring`, inherited styling to `designing-style-inheritance-inspection`, instances to `designing-component-instance-overrides`, reusable definitions to `designing-builder-component-authoring`, insertion to `designing-builder-slot-insertion`, data to `designing-builder-data-binding`, runtime conditions to `designing-builder-conditional-visibility`, events to `designing-builder-interaction-wiring`, release modes to `designing-builder-preview-publish-modes`, and spatial constraints to `designing-builder-layout-constraint-editing`.