---
name: designing-edge-routing-and-bendpoints
description: Use when this specialist's decision ownership is materially in scope. Decide how graph edges travel between endpoints, avoid obstacles, expose manual route control, and preserve readable topology after node movement or layout changes.
---
# Designing Edge Routing and Bendpoints

## Parent Contract

**Required parent:** `designing-diagramming-and-node-graph-editors`.

Inherit the broader routing and decision boundary from this canonical parent; this specialist remains accountable only for the narrower ownership, failure topology, falsification criteria, and output contract defined below.

## Decision ownership

Own the visual path of an already valid relationship. Decide straight, curved, orthogonal, bundled, or mixed routing; automatic obstacle avoidance; self-loop treatment; crossing policy; user-created bendpoints; label anchoring; and what happens to manual route edits when nodes move or auto-layout runs. This skill does not decide whether the relationship is legal or which ports connect it.

## Inputs and evidence

Gather graph density, edge count distribution, typical node size, directionality, label frequency, whether crossing carries semantic ambiguity, expected layout algorithms, user need for hand-tuned diagrams, print/export requirements, zoom range, and performance budget. Inspect representative worst-case nodes with many incident edges and long cross-graph connections.

## Procedure

Choose a default routing family based on semantic readability, not aesthetics alone. Orthogonal routing can clarify block diagrams but becomes noisy when over-constrained; curved edges can separate parallel relationships but obscure precise channel structure. Define obstacle margins and crossing behavior, including bridge/jump cues only when they genuinely reduce ambiguity. Manual bendpoints should be insertable, movable, removable, and keyboard inspectable; show whether a segment is user-pinned or algorithmic. When endpoints move, preserve intentional bends where possible and recompute only invalid segments. Edge labels need stable anchors that avoid nodes and do not flip unpredictably. At low zoom, reduce decorative complexity before losing direction or relationship identity.

## Failure topology

Failures include spaghetti crossings, edges hidden beneath nodes, labels detached from their relationship, automatic rerouting that radically changes the mental map after small node movement, manual bendpoints that become impossible to delete, self-loops that overlap controls, and parallel edges collapsing into one indistinguishable line. Performance failure is also material: a perfect router that freezes during drag produces an unusable editor.

## Falsification

Reject if moving one node causes unrelated edges to reshuffle across the graph; if two crossing edges cannot be visually traced end-to-end at normal zoom; if a manual route silently resets after save/reload; if edge labels overlap their own endpoints in representative data; if a user cannot distinguish parallel relationships; or if interactive dragging exceeds the product's latency budget because routing is recomputed synchronously.

## Output contract

Return an `edge-routing-and-bendpoints-contract` with: default routing family; obstacle and crossing rules; parallel-edge and self-loop treatment; bendpoint lifecycle; pinned versus automatic segment semantics; label anchoring; node-move recomputation policy; low-zoom simplification; performance fallback; and export consistency requirements. Include one dense-crossing example used for verification.

## Handoffs

Receive endpoints from `designing-port-and-connector-authoring`. Coordinate with `designing-graph-auto-layout-controls` for layout/routing ordering and with `designing-diagram-export-and-presentation` for print/static output. Generic motion owners may animate route changes, but must not make topology harder to trace.