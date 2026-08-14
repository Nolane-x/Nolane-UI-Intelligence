---
name: engineering-rich-interactive-components
description: Use when a UI contains animation, direct manipulation, drag, morphing, gesture, scroll-linked behavior, shared-layout transitions, 3D/canvas interaction, or other rich interaction whose behavior must remain precise under interruption, alternate input, reduced motion, hydration and performance pressure.
---

# Engineering Rich Interactive Components

## Parent Contract
**Required parent:** `designing-interactions`.

Receive canonical actions, component states, task-flow consequences, accessibility obligations, platform/input profiles, selected implementation mechanism or engine, visual motion intent, performance budget and recovery semantics. The parent owns the interaction's purpose; this faculty owns the detailed mechanics that make the interaction trustworthy.

## Decision Boundary
This faculty owns **behavioral engineering of rich interaction**. It is activated when time, space or continuous input changes state: animated transitions, drag/sort, sliders with kinetic behavior, morphing surfaces, spring-following controls, scroll-linked stories, shared-element continuity, canvas manipulation, 3D interaction or gesture systems. It does not add motion merely to make a static interface exciting, and it does not select libraries.

The output is a contract that implementation and runtime verification can test. “Smooth 300ms animation” is not a contract. A valid contract names state ownership, activation, interruption, retargeting, focus, modalities, reduced motion, completion/cancellation, SSR/hydration and performance degradation.

## Product Truth
Rich interactions fail in subtle ways that screenshots cannot reveal. A button can animate beautifully while accepting duplicate activation. A dragged item can be impossible to move with keyboard. A spring can continue after navigation and mutate an unmounted view. A shared-layout morph can steal focus. ScrollTrigger-style effects can become nonsensical after content changes. A layout measurement during server render can produce hydration mismatch. A GPU-heavy background can consume the budget needed by the actual task.

Animation also changes meaning. It can preserve object continuity, establish causality, reveal hierarchy, communicate spatial relationship and acknowledge manipulation. It can also delay work, create vestibular discomfort, hide state change, or become the only cue that something happened. The decision is therefore functional before aesthetic.

## Decision Model
1. **State the informational purpose.** Classify the rich behavior as continuity, causality, orientation, manipulation feedback, hierarchy, attention, progress, celebration, ambience or pure decoration. Decorative behavior has the lowest budget and strongest permission to disappear.
2. **Define state ownership.** Name who owns `idle`, `armed`, `active`, `settling`, `interrupted`, `cancelled`, `failed`, `complete` or equivalent states. Avoid competing React/local/animation-engine state that can diverge.
3. **Define activation thresholds.** For pointer/touch gestures specify hit target, movement threshold, long-press or drag threshold, axis lock, scroll conflict and cancellation. A tiny pointer movement must not accidentally reorder data.
4. **Define semantic action boundaries.** Continuous visual motion may have many frames but the product action has explicit commit semantics. For sorting, determine when order becomes committed and how undo/recovery works. For destructive gestures, do not commit merely because a swipe crossed a visual threshold without the product's authority model.
5. **Define interruption.** Every non-instant interaction states what happens when the user reverses direction, presses Escape, navigates away, changes viewport, receives new data, loses permission or starts another action. Avoid animations that must finish before the interface accepts truth.
6. **Define retargeting.** If the destination changes mid-flight, specify whether motion retargets from current visual state, snaps, cancels or restarts. Retargeting from stale logical coordinates is a common source of jumps.
7. **Guarantee modality equivalence.** Pointer, touch, keyboard, switch/assistive activation and platform-specific alternatives must reach equivalent product actions when required. Drag-and-drop receives explicit keyboard controls, not a statement that “keyboard users can edit elsewhere” unless product obligations permit that difference.
8. **Preserve focus and announcements.** Motion must not visually move a focus target while DOM focus disappears. Dialog/morph transitions define focus entry, containment and return. Significant asynchronous results have non-motion announcement/label alternatives.
9. **Specify reduced motion.** `prefers-reduced-motion` or platform preference is a semantic branch, not `animation-duration: 0` by default. Preserve hierarchy, continuity and status through opacity, instant state change, restrained crossfade or static placement while removing vestibular transforms, parallax and unnecessary looping.
10. **Define rendering lifecycle.** For SSR/hydration, keep initial markup deterministic; measure layout after hydration; isolate browser-only APIs; prevent first-frame jumps. Define cleanup for observers, RAF, timelines, listeners, physics and WebGL resources.
11. **Budget performance.** Identify hot paths, layout reads/writes, animation properties, canvas/WebGL cost, low-end fallback, offscreen pausing and maximum concurrent effects. Measure representative worst cases rather than trusting engine marketing.
12. **Define an exit strategy.** The product task must remain operable if the enhancement is disabled, the engine is replaced, or the effect is degraded. Deep 3D/canvas products may legitimately depend on the engine, but that dependency must be acknowledged rather than accidental.

## Evidence
Strong evidence includes state diagrams, event traces, pointer/keyboard/touch probes, reduced-motion renders, accessibility-tree observations, performance profiles, hydration tests, resize/content-change tests and interruption recordings. Engine examples prove API possibilities, not product correctness.

When using external animated components, inspect how they manage presence, layout measurement, portals, focus, cleanup and dependencies. Known upstream issues about hydration or ARIA are risk evidence. Local wrappers must still be tested because composition can break upstream guarantees.

## Output Contract
Return `rich-interaction-contract` with:
- `purpose`
- `canonical_action_ids[]`
- `states[]` and `state_owner`
- `activation {targets, thresholds, gesture_conflicts}`
- `commit_semantics`
- `modalities[]` and `equivalence_map[]`
- `interruptions[]`
- `retargeting`
- `focus_behavior`
- `announcement_behavior`
- `reduced_motion`
- `ssr_strategy`
- `cleanup_strategy`
- `performance_budget`
- `degradation_strategy`
- `exit_strategy`
- `runtime_probes_required[]`

At minimum, an interactive pointer path that owns a product action must have a keyboard-equivalent path unless a documented product/platform exception says otherwise.

## Failure Traps
- Adding animation because the interface “feels too static.”
- Treating duration/easing as the whole motion system.
- Using CSS `transition: all` on state-heavy controls.
- Letting drag visuals commit data before canonical action semantics authorize the change.
- Missing Escape/cancel behavior or assuming a spring cannot be interrupted.
- Using transform/zoom as the only explanation of spatial change under reduced motion.
- Drag-only sorting with no keyboard operation.
- Reading layout during SSR or initial render and causing hydration mismatch.
- Leaving RAF, observers, timelines or WebGL resources running after the surface disappears.
- Running decorative ambient effects at full fidelity behind a data-heavy task.
- Trusting an upstream demo's focus behavior after wrapping it in portals/layout animation.
- Making the business task impossible when the animation dependency is disabled.

**Hard gate:** rich interaction cannot ship without explicit states, modality equivalence, interruption/retargeting, reduced motion, focus semantics, rendering lifecycle, performance budget and a testable exit/degradation strategy.

## V6 Rich Interaction Engineering Protocol
Represent complex widgets with an **interaction statechart** covering stable/intermediate states, events, guards, async outcomes, cancellation, and error recovery. Define an **event ownership boundary** so nested components do not both react to Escape, outside-click, pointer capture, selection, drag, or keyboard commands.

Build a **focus-transition graph** for entry, roving focus, nested overlays, async replacement, virtualization, and exit/restoration. Stress an **async race envelope** with reordered responses, repeated activation, unmount, retry, and stale results. Track **performance-interaction coupling** where virtualization, animation, rendering engines, or debouncing can alter focus/selection/feedback semantics.

### Falsification
Rapidly interleave input events and async completions while switching focus/modal state. Any impossible state, duplicate action, or lost focus falsifies the component model.

### Recovery
Centralize state/event authority, cancel/ignore stale work, preserve semantic identity, and simplify interaction before adding patches.

## V9 Motion Implementation Fidelity
Implement **semantic motion** from the `designing-motion` contract rather than translating adjectives such as “smooth,” “premium,” or “cinematic” directly into springs. Each timeline, transition or gesture binds a semantic purpose, canonical state transition, interruption model, reduced-motion branch and evidence probe. The animation engine owns interpolation mechanics; product state owns truth.

Keep one authoritative temporal state model. CSS transitions, React state, animation-library presence/layout state, canvas/WebGL loops and async product state must not independently decide whether an operation is complete. Visual settling may continue after the semantic action has committed, but the user must not be blocked from valid next actions unless the product contract explicitly requires serialization.

Translate the V9 motion hierarchy into **performance degradation** order. Under throttled CPU/GPU, low battery/data-saving modes, many simultaneous objects or background tabs, remove or simplify ambient/celebratory/signature effects before task feedback, progress, focus, drag tracking or state acknowledgement. Pause offscreen loops and release observers/timelines/resources when ownership ends.

Implement reduced motion as an explicit state branch. Avoid merely setting every duration to zero when that creates focus jumps, destroys continuity or bypasses expected completion events. Choose instant state, crossfade, restrained opacity, persistent highlight/status or another equivalent representation and test the branch independently.

For motion coupled to layout or pointer input, preserve current visual state during retargeting. Rapid resize, reordered data, reversed gesture, repeated activation and navigation can all invalidate a destination. Retarget/cancel from current state rather than restarting from stale coordinates and creating visible jumps.

### V9 Falsification
Run the same interaction at normal speed, rapid repeated input, reduced motion, background/foreground transition, throttled rendering and with the destination changing mid-flight. If state truth diverges, focus disappears, duplicate actions occur or decorative effects consume the task feedback budget, implementation fidelity fails even when the happy-path animation looks excellent.

### V9 Recovery
Centralize semantic state and event ownership, cancel stale async/animation work, simplify choreography, and restore task feedback before visual richness. If the engine makes correct interruption or reduced-motion semantics unreasonably fragile, replace or bound the engine instead of encoding product truth inside it.

## V10 Temporal Runtime Realization Test
This faculty participates in `H-MOTION-SEMANTIC` but does **not** own the product-level decision about whether motion should exist. Its empirical question is narrower: once a semantic motion contract exists, does implementation preserve canonical action truth under interruption, retargeting, alternate input, reduced motion, hydration and performance pressure?

Record a runtime event trace for material interactions:

`input/event → semantic action state → visual state → interruption/retarget event → authoritative commit/cancel → focus/announcement result → settled state`

Pair that trace with the design-motion purpose and reduced-motion equivalent. A motion system can look identical in two screenshots while one version duplicates actions, loses focus, completes against stale data or keeps an offscreen loop alive. Those are runtime failures, not visual preferences.

For the `motion-decoration-priority` mutation, implementation must not “rescue” the experiment by silently fixing the product-level priority; it should faithfully expose the consequence of the mutated contract while preserving basic runtime safety. Conversely, the full condition must degrade ambient/signature effects before task feedback when performance pressure rises. The evaluator should test throttling, rapid repeated input, changed destinations, unmount/navigation, reduced motion and keyboard-equivalent operations.

### V10 failure attribution
If the design-motion contract is semantically correct but runtime traces fail, attribute the defect here. If runtime follows the contract perfectly but the motion purpose is wrong, attribute it to `designing-motion`. This separation prevents a motion engine from being blamed for a bad product decision or a motion director from receiving credit for robust interruption mechanics supplied elsewhere.

A targeted efficacy claim can mention this runtime owner only when full NUI shows lower impossible-state, duplicate-action, focus-loss or reduced-motion-equivalence failure rates than a matched ablation/mutation on rich-interaction tasks. Smoothness alone is not a V10 empirical success metric.
