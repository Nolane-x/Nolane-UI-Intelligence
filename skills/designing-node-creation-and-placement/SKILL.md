---
name: designing-node-creation-and-placement
description: Use when this specialist's decision ownership is materially in scope. Decide how users instantiate typed graph nodes, choose their insertion context, preview placement, and recover from invalid or accidental creation.
---
# Designing Node Creation and Placement

## Parent Contract

**Required parent:** `designing-diagramming-and-node-graph-editors`.

Inherit the broader routing and decision boundary from this canonical parent; this specialist remains accountable only for the narrower ownership, failure topology, falsification criteria, and output contract defined below.

## Decision ownership

Own the moment a new graph entity becomes real. Decide how node type is chosen, where insertion intent comes from, whether placement is explicit or layout-assisted, what preview is shown before commit, and how constraints such as lanes, containers, coordinates, or parentage are enforced. This owner does not decide edge compatibility or global graph layout; it supplies a well-defined new node and placement intent to those systems.

## Inputs and evidence

Collect the node type catalog, frequency distribution of created types, whether type choice depends on context, legal parent/container rules, coordinate or lane constraints, expected repeated-creation workflows, keyboard and touch input requirements, auto-layout behavior, and persistence latency. Observe expert and novice creation sequences. Determine whether creating a node has side effects such as provisioning resources, creating executable steps, or notifying collaborators.

## Procedure

Choose the lowest-friction entry point that preserves type certainty: palette drag, command/menu insertion, keyboard shortcut, contextual plus target, duplicate, or paste. For large catalogs, separate search/type selection from physical placement instead of making users drag through long palettes. Define a pre-commit ghost or insertion marker whenever location matters. Make constrained containers advertise valid drop zones before release. Specify defaults for size, label focus, parent, and initial attributes, and decide whether creation immediately enters rename/configuration state. Repeated creation should be a deliberate mode with an obvious exit. If layout is automatic, preserve the user's intended neighborhood or relationship rather than pretending coordinates are authoritative.

## Failure topology

Failures include nodes appearing outside the visible viewport, duplicate creation caused by slow persistence, wrong node types created because palette icons are ambiguous, objects silently reparented into the wrong container, creation modes that remain armed and produce accidental extra nodes, and auto-layout relocating a new node so far away that users think creation failed. High-risk products also fail when a visual create gesture triggers real-world provisioning without an explicit consequence boundary.

## Falsification

Reject a design if users cannot predict the new node's type and structural parent before commit; if a keyboard-only user cannot insert a node into a chosen context; if rapid repeated creation can double-submit; if invalid placement is communicated only after the object disappears; if newly created objects can land off-screen without a locator; or if destructive/provisioning creation is indistinguishable from harmless diagram annotation.

## Output contract

Return a `node-creation-and-placement-contract` with: allowed creation entry points; node-type resolution rule; insertion-context model; placement preview; valid/invalid target feedback; initial property defaults; repeated-create behavior; post-create focus; async/persistence states; side-effect confirmation rule; keyboard/touch equivalents; and recovery behavior for failed or duplicate creation. Include one context-sensitive insertion example and one constrained-placement example.

## Handoffs

Use `designing-port-and-connector-authoring` after creation when relationships must be established, `designing-subgraph-and-container-models` for parent/container semantics, and `designing-graph-auto-layout-controls` when placement becomes algorithmic. Generic drag/drop, inline editing, and undo/redo owners supply mechanics but do not decide node-creation semantics.