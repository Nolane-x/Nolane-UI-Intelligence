---
name: designing-swimlane-diagrams
description: Own lane-based process diagrams where rows or columns represent actors, systems, phases, or responsibilities and cross-lane movement carries meaning.
---
# Designing Swimlane Diagrams

## Decision ownership

Own the specialized semantics of lanes in process diagrams. Decide lane orientation, header behavior, lane creation/reordering/resizing, ownership of nodes by lane, cross-lane connector treatment, collapsed lane representation, and how the interface distinguishes actor/responsibility lanes from generic containers. This owner does not define process-step validity itself unless lane membership constrains it.

## Inputs and evidence

Require the lane dimension (actor, department, system, phase, geography), expected lane count, whether order is meaningful, node movement frequency, cross-lane edge volume, print/export needs, and rules for nodes spanning lanes. Determine whether lane changes represent a real responsibility transfer or are merely layout edits. Inspect a representative wide and tall diagram rather than a symmetric toy example.

## Procedure

Choose orientation from reading order and comparison needs; horizontal lanes favor time flowing left-to-right, while vertical lanes may fit actor comparison better. Keep headers sticky or recoverable during pan so users do not lose lane identity. Reordering a lane should preview its effect on connectors and, when order is semantically meaningful, require a deliberate action. Dragging a node across a boundary must clearly indicate whether responsibility changes. Lane resizing should not silently distort node coordinates beyond the user's intent. Cross-lane edges need routing that makes handoff points legible. Collapsed lanes must still signal hidden work and external dependencies.

## Failure topology

Failures include lane headers disappearing off-screen, users mistaking lane boundaries for decorative grid lines, cross-lane connectors becoming a dense braid, nodes accidentally changing owner during pan/drag, collapsed lanes erasing handoffs, and print/export splitting a lane header from its contents. Another failure is using color alone to encode lane ownership when geometry already suggests but does not guarantee it.

## Falsification

Reject if a user inspecting any visible node cannot recover its lane identity without zooming out; if crossing a lane boundary can change semantic ownership without explicit feedback; if lane reorder changes process interpretation but behaves like harmless visual sorting; if collapsed lanes hide active errors or external dependencies; or if the diagram cannot be read in exported/paginated form with headers repeated appropriately.

## Output contract

Return a `swimlane-diagrams-contract` containing: lane dimension and orientation; header/sticky behavior; create/reorder/resize rules; node membership semantics; cross-lane move protocol; connector handoff cues; collapse behavior; hidden-state indicators; accessibility labeling; and export/pagination constraints. Include one cross-lane transfer scenario used to verify the ownership cue.

## Handoffs

Use `designing-subgraph-and-container-models` for generic nesting mechanics, `designing-flowchart-semantics` when the lane hosts formal flowchart logic, and edge routing for connector geometry. Generic table/grid layout owners must not override lane meaning.