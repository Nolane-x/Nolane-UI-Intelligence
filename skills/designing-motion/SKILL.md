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

## V5 Motion as Dynamic Information
When the product thesis is “living”, evolving, causal, temporal, simulated, or agentic, test motion as **dynamic information**, not merely polish. It may communicate **propagation**, experiment state change, lineage, causal updates, simulation progress, memory consolidation or continuity. Each motion channel declares its semantic role; ambient motion stays explicitly decorative. The **reduced motion** branch must preserve the information through state, text, structure or discrete transitions rather than deleting meaning.

## V6 Temporal Interaction Model
Allocate a **temporal-information budget**: every animation must declare whether it communicates causality, continuity, hierarchy, spatial origin, progress, confirmation, attention, or expressive identity. Decorative movement competes with those signals and with user attention; it does not inherit a free budget.

For moving/morphing objects build a **continuity-anchor map** stating which identity remains perceptually stable across before/after states—position, shape, label, color, parent surface, or shared layout ID. Model an **interruption graph** for rapid repeat activation, navigation mid-animation, drag reversal, async completion while transitioning, and multiple concurrent motions. Define which transitions retarget, finish, cancel, or snap.

The reduced-motion mode requires **reduced-motion semantic equivalence**: remove vestibular/ornamental movement without deleting information about change, origin, progress, or completion. Validate timing with a **settling-envelope test** across low/high refresh, throttled CPU/GPU, different content lengths, and spring overshoot; the UI should not remain physically “busy” after the user is ready to act.

### Falsification
Disable all motion and ask what meaning disappears; then accelerate user input so transitions overlap. If state becomes ambiguous without spectacle or interaction blocks behind animation, the motion model is false.

### Recovery
Move meaning into persistent state cues, shorten/retarget transitions, simplify effects, or replace physical travel with opacity/crossfade under reduced motion. Never preserve animation solely because the reference looked impressive.

## V7 Temporal Craft Lineage
When motion is material, separate **why the product moves** from **which engine executes movement**. Product state and information semantics own the transition truth; Motion, GSAP, platform animation APIs, canvas/3D runtimes, or local CSS may become implementation authorities only for the mechanics they can prove. Record that lineage in the implementation-authority plan.

Design choreography as a temporal sentence: establish context, expose the causal change, then settle into a state ready for action. Timeline labels, presence modes, shared-layout identity, spring behavior, scroll coupling, or shader interpolation are mechanisms—not aesthetic justification. Capture before/transition/settled states in rendered-perception evidence and verify that reduced-motion mode carries equivalent information. A motion that exists only to resemble a reference fails even if technically smooth.

### Falsification
Replace the engine while keeping the semantic sequence. If the product meaning disappears, state truth was incorrectly encoded inside the animation library.

### Recovery
Move meaning into explicit product state, simplify choreography, and reselect an engine only after the temporal contract is stable.

## V9 Motion Direction
Treat motion as a product-level direction with four questions before choosing easing or duration: **what structure does motion teach, what causality does it confirm, what emotional cadence does it contribute, and where is intentional absence stronger?** High-quality motion is often noticeable as coherence rather than spectacle.

### Structural teaching
Use motion to reveal relationships that are otherwise hard to infer: a panel belongs to a selected object, a card expands into detail, a timeline edit shifts dependent material, a workspace pane is moved rather than destroyed, or a modal action returns focus to its origin. Maintain continuity anchors so the movement explains architecture. If the relationship is already obvious from stable layout, motion may add no value.

### Causality and state truth
Acknowledgement should make cause and effect legible: the pressed control, affected object, pending operation and final state belong to one temporal story. Async truth outranks optimistic spectacle. Do not celebrate success before the authoritative state exists, and do not make error/reversal feel like a visual afterthought. Repeated expert actions should settle quickly enough that users operate at their own speed.

### Emotional cadence
When emotion is part of the product thesis, allocate cadence deliberately across an experience rather than animating every component. A creative tool may use a restrained expressive beat at creation/export while keeping trimming, selection and property edits immediate. A consumer product may allow more delight around low-consequence milestones. Financial, medical, operational and high-pressure surfaces usually need calmer transitions where confidence and state legibility dominate. Emotional cadence is domain- and audience-sensitive, not a universal “premium easing.”

### Intentional absence
**Intentional absence** is a first-class motion decision. Prefer no motion when transition delay would slow repeated work, when movement competes with dense scanning, when the platform convention is instant, when state remains clearer as a cut, or when motion would trivialize a high-consequence action. A still interface can feel more expensive than an animated one when the restraint is deliberate.

### Reduced motion equivalence
Require **reduced motion equivalence**, not merely a disabled animation flag. For every informational transition specify which persistent cue, crossfade, instant layout state, text/status update or focus movement carries the same meaning. Remove parallax, large-scale zoom/travel and continuous ambient effects when needed, while preserving causal acknowledgement and orientation.

### Motion hierarchy
Classify motion priority: `critical-information`, `task-feedback`, `orientation`, `signature`, `celebration`, `ambient`. Performance or reduced-motion degradation must remove from the bottom upward. Ambient/background effects never consume the latency or frame budget required by direct manipulation, scrolling, input or status feedback.

### V9 Falsification
Watch the interface at normal speed, 2× interaction speed, reduced motion, throttled hardware and without audio/haptics. Ask whether structure and causality remain understandable, whether expressive movement repeats into fatigue, and whether any interaction feels slower solely to look sophisticated. If removing decorative animation improves the task with no identity loss, the original motion was excess.

### V9 Recovery
Preserve state truth, remove low-value channels, rebalance cadence around meaningful moments, and simplify spatial travel. When motion is necessary but implementation cannot hit the interaction/performance budget, degrade the effect before degrading task responsiveness or feedback.
