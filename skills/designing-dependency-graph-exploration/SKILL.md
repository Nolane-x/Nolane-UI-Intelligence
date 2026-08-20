---
name: designing-dependency-graph-exploration
description: Use when this specialist's decision ownership is materially in scope. Own read-oriented exploration of upstream/downstream dependencies, impact radius, cycles, roots, leaves, and focused neighborhoods in complex graphs.
---
# Designing Dependency Graph Exploration

## Parent Contract

**Required parent:** `designing-diagramming-and-node-graph-editors`.

Inherit the broader routing and decision boundary from this canonical parent; this specialist remains accountable only for the narrower ownership, failure topology, falsification criteria, and output contract defined below.

## Decision ownership

Own investigation of directional dependency relationships rather than graph authoring. Decide how users answer "what depends on this?", "what does this depend on?", "what breaks if this changes?", and "where is the cycle?" through neighborhood expansion, path focus, impact summaries, and structural filters. It does not own how dependencies are created in the source system.

## Inputs and evidence

Require dependency direction semantics, edge types, expected graph size, frequency of cycles, impact metadata, node criticality, hierarchy or package grouping, and common investigative questions. Identify whether dependencies are static, versioned, or live; whether absence means no relationship or missing telemetry; and whether users need exact path proof for decisions.

## Procedure

Start from a selected subject and make upstream versus downstream direction explicit in both controls and visual encoding. Allow bounded expansion by depth, relationship type, or criticality rather than exploding the entire graph. Provide path-to-target and path-to-root operations that isolate the chain while preserving a way back to context. Detect cycles as first-class structures and offer cycle-focused views instead of letting recursive expansion loop. Impact mode should distinguish direct from transitive dependents and show confidence/freshness when evidence may be incomplete. Preserve exploration history so users can compare hypotheses without repeatedly reconstructing filters.

## Failure topology

Failures include reversed dependency direction, unlimited expansion producing unreadable hairballs, hidden transitive impact, cycle navigation that repeats nodes endlessly, path highlighting that loses off-path context completely, and stale dependencies presented as current fact. Another failure is using node proximity as implied impact when layout distance has no semantic meaning.

## Falsification

Reject if two users can interpret the same arrow in opposite dependency directions; if expanding a high-degree node can freeze or flood the view without a scope control; if a cycle cannot be isolated and enumerated; if impact counts do not distinguish direct/transitive; if selected paths disappear on zoom/filter changes; or if stale/incomplete evidence cannot be identified from the exploration surface.

## Output contract

Return a `dependency-graph-exploration-contract` containing: direction convention; expansion depth/type controls; path-isolation behavior; cycle representation; impact-radius calculation/presentation; direct-versus-transitive distinction; evidence freshness cues; criticality filters; exploration history; and fallback for incomplete dependency data. Include one cycle and one high-degree impact scenario.

## Handoffs

Use graph search/navigation for locating subjects, minimap/virtualization for scale, and topology maps when physical/logical infrastructure status matters. Security attack-path visualization is a different downstream owner because exploitability/risk semantics differ from ordinary dependency impact.