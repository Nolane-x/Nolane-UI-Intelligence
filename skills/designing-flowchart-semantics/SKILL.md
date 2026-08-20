---
name: designing-flowchart-semantics
description: Own the UI expression and validation of flowchart-specific start/end, process, decision, branch, merge, loop, and reachability semantics.
---
# Designing Flowchart Semantics

## Decision ownership

Own how a flowchart communicates executable or procedural flow rather than arbitrary connected shapes. Decide how start/end, action, decision, branch labels, merge points, loops, unreachable nodes, and direction are represented and edited. It does not own BPMN or a domain workflow engine; it owns the generic flowchart grammar and the UI obligations created by that grammar.

## Inputs and evidence

Require the supported node kinds, whether decisions must have labeled outcomes, whether multiple starts/ends are legal, expected loop patterns, reachability requirements, edge direction rules, and whether the diagram is descriptive or drives execution. Determine how much formal validation is desirable: teaching diagrams may tolerate incomplete states while deployable process definitions may not.

## Procedure

Give semantic node kinds recognizable structure without relying on shape recognition alone; labels or accessible roles must carry the same information. When a decision is created, surface branch-outcome naming close to the outgoing edges and prevent multiple visually identical unlabeled paths from becoming ambiguous. Make primary reading direction consistent, while allowing loops and exception paths without pretending they are linear. Validate missing start/end, dead ends, unreachable nodes, and unlabelled decision branches at an appropriate lifecycle moment. Editing should permit incomplete intermediate states without turning the whole canvas into an error wall.

## Failure topology

Failures include a diagram that looks like a flowchart but has no detectable direction, decision diamonds with unlabeled branches, loops that resemble accidental back-edges, multiple starts hidden by zoom, impossible paths that look valid, and validation that fires on every intermediate drag. Accessibility fails when semantic role is communicated only through geometric shape.

## Falsification

Reject if a reviewer cannot trace the intended path through every decision without guessing branch meaning; if screen-reader or text-equivalent output loses node type; if an unreachable node can survive into a publish/execute state with no finding; if loop entry/exit cannot be distinguished; or if adding a temporary incomplete edge blocks all further editing with modal errors.

## Output contract

Return a `flowchart-semantics-contract` containing: supported semantic node roles; primary flow direction; start/end constraints; decision-branch labeling; merge/loop representation; incomplete-edit tolerance; validation timing and severity; reachability findings; text/accessibility equivalents; and publish/execute gating rules. Include one branching example and one loop example.

## Handoffs

Use connector authoring for relationship creation, edge routing for geometry, graph validation for issue presentation, and executable debug overlays if the flowchart is runnable. UML/modeling diagrams own typed modeling relationships that are not procedural flow.