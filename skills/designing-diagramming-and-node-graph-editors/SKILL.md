---
name: designing-diagramming-and-node-graph-editors
description: Own the interaction architecture for editable semantic node-and-edge canvases where structure, connectivity, scale, and authoring safety matter more than freeform drawing.
---
# Designing Diagramming and Node-Graph Editors

## Decision ownership

Own the graph-editor interaction model: how semantic nodes and edges are created, selected, connected, moved, inspected, validated, navigated, and understood as one structured system. This owner decides the boundary between canvas gestures and structural commands, what must remain visible as topology, and which operations need preview, confirmation, undo, or validation. It does not own the domain meaning of a UML class, incident dependency, workflow step, or network host; those meanings belong to narrower graph or product owners.

## Inputs and evidence

Require the graph schema, expected node and edge cardinality, whether the surface is primarily authoring or exploration, edit permissions, expected graph sizes, keyboard/accessibility obligations, collaboration model, layout constraints, and any runtime state that can overlay the graph. Inspect real dense examples rather than designing from a six-node demo. Record whether identity is stable across layout changes and whether edges have direction, type, capacity, or execution meaning.

## Procedure

First classify the graph as free topology, constrained diagram, hierarchical graph, dependency graph, or executable graph; mixed products may expose more than one mode but should not silently blend their rules. Define the semantic selection unit before gestures: node, port, edge, group, lane, or subgraph. Separate structure-changing operations from viewport navigation so pan/zoom cannot accidentally rewire content. Choose explicit creation and connection grammars, then specify feedback for valid, ambiguous, and forbidden structure. Establish scale behavior from overview to detail, including what labels and controls disappear or aggregate. Finally bind validation, history, collaboration, and inspector surfaces to stable graph identities rather than screen coordinates.

## Failure topology

A graph editor fails when it becomes a drawing tool with hidden semantics, when panning and editing share ambiguous gestures, when dense graphs become unreadable wallpaper, when edge direction or type is only encoded by subtle styling, or when layout changes destroy the user's mental map. Other critical failures are off-screen creation, accidental rewiring, selection that changes under virtualization, hidden structural errors, and destructive automatic layout with no preview or recovery.

## Falsification

Reject the design if a user cannot explain what object will change before committing a structural gesture; if the same action sometimes pans and sometimes edits without an explicit state cue; if a 500-node representative graph loses selection or focus while zooming; if keyboard users cannot create and connect a minimal graph; if layout can move pinned/meaningful objects without warning; or if two visually identical edges can have materially different semantics with no inspectable signal.

## Output contract

Return a `diagramming-and-node-graph-editors-contract` containing: graph classification; semantic object types; edit versus navigation modes; selection model; creation grammar; connection grammar; viewport/scale policy; validation surfaces; history/undo guarantees; collaboration assumptions; accessibility equivalents; inspector handoffs; and unresolved graph-scale risks. Include one dense representative scenario and the expected state transitions for a structural edit.

## Handoffs

Delegate node placement, ports, routing, auto-layout, subgraphs, formal diagram types, large-graph virtualization, graph validation, graph history, and executable debug overlays to their dedicated owners. Reuse generic editor/canvas, direct manipulation, pan/zoom, undo/redo, collaboration, and accessibility owners for lower-level mechanics. This skill remains accountable for making those mechanics cohere as one semantic graph editor.