---
name: designing-executable-graph-debug-overlays
description: Own debug-state overlays for runnable graphs, exposing execution position, queued/running/failed states, data or token movement, breakpoints, stepping, and replay without corrupting authoring context.
---
# Designing Executable Graph Debug Overlays

## Decision ownership

Own the visual and interaction layer used when a node graph represents executable behavior. Decide how execution state maps onto nodes/edges, how breakpoints and paused state are shown, how users step or continue, how data/token provenance is inspected, and how historical replay is separated from the live run. This owner does not execute code or choose the runtime scheduler; it translates runtime evidence into a debuggable graph surface.

## Inputs and evidence

Require runtime event model, node/edge execution semantics, concurrency model, queue/running/success/failure states, breakpoint capabilities, variable/data inspection, event ordering, replay availability, latency, and whether execution has real-world side effects. Identify how many nodes may be active simultaneously and whether one logical node can have multiple concurrent instances.

## Procedure

Separate authoring mode from debug mode visually and behaviorally so moving a node cannot be mistaken for changing runtime. Map active state to stable node identity, not screen position. Concurrent execution needs instance counts or lanes rather than one ambiguous green highlight. Edge animation may indicate transfer, but must be backed by inspectable event data and reduced-motion equivalence. Breakpoints should be settable without obscuring validation badges and must indicate scope/version. When paused, show why, current instances, next executable choices, and side-effect warnings before step/continue if actions are consequential. Replay must carry an obvious historical timestamp and never look live.

## Failure topology

Failures include a single highlight implying serial execution when tasks are concurrent, animated particles with no inspectable evidence, stale states after reconnect, breakpoint badges indistinguishable from errors, stepping that triggers irreversible actions without warning, and replay views that operators confuse with current production state. Another failure is debug overlays making ports/labels unreadable, preventing understanding of the graph itself.

## Falsification

Reject if two concurrent node instances collapse into one unexplained state; if an animated edge cannot be tied to an event or data record; if reduced-motion mode loses transfer causality; if a breakpoint's applicable graph version is unknown; if replay can be mistaken for live state; if stepping a side-effecting node lacks an explicit consequence boundary; or if runtime updates overwrite the user's selected historical event.

## Output contract

Return an `executable-graph-debug-overlays-contract` containing: debug-mode entry/exit; runtime-to-node identity mapping; concurrency representation; node/edge state vocabulary; event/data inspection; breakpoint lifecycle; pause/step/continue controls; side-effect warnings; replay mode; stale/disconnected state; reduced-motion equivalent; and overlay priority with validation/selection. Include a concurrent execution and a historical replay scenario.

## Handoffs

Use graph authoring owners for structure, validation for static findings, graph history for version identity, and streaming/realtime owners for transport freshness. High-stakes runtime action policies remain authoritative over step/continue when execution can affect external systems.