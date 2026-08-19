---
name: designing-toggle-state-motion
description: Use when a binary or tri-state control changes persistent state and motion must make the new state, causality and pending/error conditions legible without confusing transient press feedback with committed value.
---

# Designing Toggle State Motion

## Parent Contract
**Required parent:** `designing-motion`.

This faculty owns the transition between persistent toggle states: switch on/off, checkbox checked/unchecked/mixed, visibility, favorite, mute and similar reversible values. It does not choose the semantic control type or decide whether optimistic updates are safe.

## Decision Model
First name the committed states and any intermediate truth. A local setting may be `off ↔ on` synchronously. A remote device might be `off → requesting-on → on|failed`. A parent checkbox can include `mixed`. The animation must never erase those distinctions.

Use trajectory to reinforce state where spatial metaphor exists—such as a switch thumb moving between endpoints—but do not rely on position alone when color/label/assistive semantics are needed. For icon toggles, morphing can reinforce continuity if both silhouettes remain recognizable; a crossfade may be safer when morph geometry becomes ambiguous.

Separate the moment of physical activation from committed state. Press feedback can begin on contact; toggle motion should begin only when the product model says the value changed or when an explicitly optimistic state is entered. If rollback occurs, communicate reversal as a state correction rather than replaying a cheerful toggle animation.

Repeated activation must be retargetable. Do not queue `on`, `off`, `on` animations after the model has already settled on `on`. The visual state should converge on the latest truth.

Reduced motion can snap between endpoints while retaining redundant state cues. For photosensitive or high-attention contexts, avoid flashes or full-surface color inversions for tiny state changes.

## Failure Topology
- The thumb reaches “on” while the server has rejected the change.
- Mixed checkbox animates through unchecked, falsely implying all children are off.
- Rapid toggling queues stale animations and ends visually opposite the model.
- Icon morph passes through an unreadable shape that resembles a third command.
- Motion is the only way to notice a state change.

## Falsification
Test latency, rejection, rapid reversal, offline transition, externally updated state, mixed state, keyboard activation and reduced motion. Compare rendered state against authoritative model state at arbitrary animation frames. Any frame that materially claims the wrong persistent value is a failure.

## Recovery
Bind motion endpoints to model states, introduce explicit pending/error visuals where truth is not yet committed, and replace queued animation sequences with retargetable interpolation. Simplify morphs to crossfades or token changes when shape semantics degrade.

## Output Contract
Return `toggle-state-motion-contract` with state graph, commit boundary, optimistic policy reference, visual channels, interruption/retargeting behavior, failure rollback, reduced-motion equivalent and model-vs-render verification cases.