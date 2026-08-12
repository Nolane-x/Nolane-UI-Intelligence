---
name: designing-motion
description: Use when animation, transition, gesture, scrolling, loading, or spatial movement can communicate state, hierarchy, continuity, feedback, or brand character.
---

# Designing Motion

## Overview
Motion should explain change, reinforce continuity, or contribute a deliberate expressive moment. Movement without purpose consumes attention and can harm accessibility.

## Parent Contract
**Required parent:** `routing-ui-work`.

Use interaction/state transitions, hierarchy, aesthetic direction, platform guidance, and reduced-motion constraints.

## Purpose taxonomy
Classify every motion:
- `feedback`: confirms input/activation
- `state-transition`: shows old → new state
- `spatial-continuity`: explains where content came from/went
- `attention`: directs notice to a meaningful change
- `progress`: communicates ongoing work
- `expressive`: brand/emotional signature
- `ambient`: atmosphere with no task meaning

If a motion has no clear class, challenge it.

## Choreography
Prefer a small number of coordinated moments over independent effects on every element. Sequence based on information priority: context first, critical content/action next, secondary details after. Do not delay interaction until decorative entrance animation completes.

## Duration/easing
Choose duration by distance, complexity, and purpose. Quick feedback should feel immediate; spatial transitions can take longer if they help users track change. Reuse timing/easing semantics through tokens while allowing justified exceptions.

Avoid excessive elastic/bouncy motion in serious/high-frequency tools unless the brand and user context explicitly support it.

## Interruptibility
Users can act faster than animations. Define what happens if a transition is interrupted, reversed, repeated, navigated away from, or triggered during async work. State must remain correct independent of animation completion.

## Gesture coupling
For drag/swipe/scrub interactions, motion should track user input and communicate constraints/commit thresholds. Provide non-gesture alternatives where the task requires accessibility/discoverability.

## Reduced motion
Reduced motion is not simply `animation: none`. Preserve the **information function** with opacity, instant state change, simpler transition, or persistent cue when movement carried meaning. Remove parallax, large spatial travel, continuous ambient movement, and other vestibular risks as appropriate.

## Performance
Prefer compositing-friendly effects and avoid animation that causes layout instability in high-density surfaces. Performance is part of perceived craft.

## Output: `motion-contract`
Return `motions[] {trigger, purpose, property, duration_class, easing, hierarchy_role, interrupt_behavior, reduced_motion_alternative}`, `choreography`, `gesture_rules`, `performance_constraints`, and `ambient_budget`.

## Anti-patterns
- Every card rises on hover.
- Scroll reveal hides content users are trying to scan quickly.
- Loading animation with no progress/state meaning.
- Reduced-motion users lose the only cue that content changed.
