---
name: designing-collaborative-diagram-editing
description: Use when this specialist's decision ownership is materially in scope. Own concurrency semantics for shared graph editing, including conflicting structural edits, attribution, intent visibility, soft locks, and convergence after simultaneous node or edge changes.
---
# Designing Collaborative Diagram Editing

## Parent Contract

**Required parent:** `designing-diagramming-and-node-graph-editors`.

Inherit the broader routing and decision boundary from this canonical parent; this specialist remains accountable only for the narrower ownership, failure topology, falsification criteria, and output contract defined below.

## Decision ownership

Own collaboration where edits change graph topology, not merely text or cursor positions. Decide what remote intent is shown, when soft locks or reservations are needed, how simultaneous node moves and edge rewires converge, how conflicts are surfaced, and how attribution remains understandable. Generic presence and collaborative cursors provide awareness primitives; this owner governs structural concurrency.

## Inputs and evidence

Require collaboration consistency model, operation types, conflict-resolution strategy, offline/reconnect behavior, number of concurrent editors, permission boundaries, object identity, audit requirements, and whether any topology edit can trigger consequential runtime changes. Inspect collision cases such as two users reconnecting the same edge or moving one node into different containers.

## Procedure

Show remote selection and active structural intent before commit when conflicts would be surprising. Use soft locks only for operations that truly cannot merge; otherwise avoid freezing the canvas. Define convergence per operation: independent moves may merge by last accepted position, but competing reparent or reconnect operations require explicit conflict handling. Remote changes should preserve local viewport/focus and avoid dragging objects away under an active pointer. If a collaborator deletes an object currently being edited, preserve the local unsaved intent long enough to explain and recover. Reconnect after offline work needs a change summary, not a silent topology jump.

## Failure topology

Failures include remote cursor awareness without structural conflict semantics, nodes teleporting during local drag, one user's edge rewire silently overwriting another's, stale offline edits resurrecting deleted structure, permissions changing mid-session with no feedback, and activity feeds that say "updated graph" without object-level attribution. Excessive locking is also a failure when it serializes harmless independent edits.

## Falsification

Reject if two concurrent edge reconnects can converge to an unexplained result; if a remote node move can break an active local drag with no stabilization; if deleted-while-editing content is simply lost; if reconnecting offline changes mutates the shared graph with no review path; if collaborators cannot attribute a structural change to an actor; or if soft locks persist after disconnect with no timeout/recovery.

## Output contract

Return a `collaborative-diagram-editing-contract` with: operation conflict classes; remote intent cues; soft-lock policy; convergence rules; local-interaction stabilization; delete-while-editing behavior; offline reconciliation; permission-change handling; attribution; activity granularity; and unresolved-conflict UI. Include at least one competing-reconnect case.

## Handoffs

Use generic collaboration/presence for cursors and session awareness, graph diff/history for post-hoc review, and node/connector/container owners for operation semantics. Runtime side effects, if any, require their own high-stakes confirmation authority.