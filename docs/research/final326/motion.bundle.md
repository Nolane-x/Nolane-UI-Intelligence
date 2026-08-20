<!-- SKILL: designing-checkbox-mark-motion | parent=designing-motion | family=motion-specialist | output=checkbox-mark-motion-contract -->
---
name: designing-checkbox-mark-motion
description: Use when a checkbox changes between unchecked, checked, mixed, disabled, or pending states and motion must clarify committed value without delaying interaction.
---
# Designing Checkbox Mark Motion

## Parent Contract
**Required parent:** `designing-motion`.

## Decision ownership
Own the temporal relationship among box, mark, mixed indicator, press feedback, validation, and value commitment. The skill decides whether geometry draws, fades, scales, or swaps, and when motion must be omitted because state truth is more important than flourish.

## Evidence and inputs
Require the checkbox state machine, latency model, repeated-toggle rate, platform conventions, reduced-motion obligation, high-contrast behavior, and whether mixed state represents partial child selection or an independent value. Inspect rapid toggles and programmatic updates, not only a single happy-path click.

## Decision procedure
Anchor animation to the semantic commit, not pointer-down. Keep the container stable so the mark carries the change. Make checked-to-mixed and mixed-to-unchecked visually distinguishable, preserve legibility under forced colors, and allow reversal when a user toggles again mid-flight. If saving is asynchronous, do not animate success before the value is accepted; pending feedback must remain separable from the mark itself.

## Failure topology
Failures include a checkmark appearing before commitment, an animation that masks mixed state, repeated clicks queuing stale transitions, scaling that moves neighboring layout, and decorative drawing that becomes slow at high frequency.

## Falsification
Toggle rapidly through all states, inject delayed rejection, switch reduced motion on, and test keyboard plus assistive activation. The contract fails if visual state can contradict the accessible value, if an obsolete animation finishes after a newer value, or if the control becomes harder to read in any supported contrast mode.

## Output contract
Return a `checkbox-mark-motion-contract` with commit trigger, state-to-state transitions, durations/easing bounds, reversal rules, async behavior, reduced-motion equivalent, contrast constraints, and tests for rapid retargeting and mixed-state truth.

<!-- SKILL: designing-radio-selection-motion | parent=designing-motion | family=motion-specialist | output=radio-selection-motion-contract -->
---
name: designing-radio-selection-motion
description: Use when selection moves within a mutually exclusive radio group and animation must communicate exclusivity, transfer of choice, and immediate state truth.
---
# Designing Radio Selection Motion

## Parent Contract
**Required parent:** `designing-motion`.

## Decision ownership
Own motion across a radio group rather than inside one isolated circle. Decide how the newly selected indicator appears, how the previous one clears, and whether any spatial continuity is useful when options are nearby, reordered, or virtualized.

## Evidence and inputs
Require group semantics, selection source, keyboard arrow behavior, orientation, density, virtualization, validation, reduced-motion settings, and platform expectations. Observe both pointer selection and fast keyboard traversal where selection may advance several times before prior animation completes.

## Decision procedure
Treat exclusivity as an atomic transaction: old and new visual states change in one temporal window. Favor short local emphasis rather than a moving dot that falsely suggests drag-and-drop. Retarget immediately during arrow-key traversal; never queue every intermediate pulse. When validation can reject a choice, reserve a separate error transition instead of animating a false commitment.

## Failure topology
Failures include two radios appearing selected during crossfade, lag behind keyboard focus, traveling indicators crossing unrelated options, and animation tied to focus rather than value. Another failure is forcing motion on every programmatic initialization, creating noise in large forms.

## Falsification
Traverse a ten-item group rapidly by keyboard, select with pointer, restore a saved value, and inject a rejected update. Fail if exclusivity is visually violated for a frame perceptible to users, if focus and selection are confused, or if reduced motion removes the state cue rather than only the transition.

## Output contract
Return a `radio-selection-motion-contract` defining atomic group transition, retargeting, initialization behavior, validation rollback, focus separation, reduced-motion behavior, and stress tests for rapid traversal.

<!-- SKILL: designing-switch-thumb-motion | parent=designing-motion | family=motion-specialist | output=switch-thumb-motion-contract -->
---
name: designing-switch-thumb-motion
description: Use when a binary switch uses spatial thumb movement and the transition must preserve cause, direction, commitment timing, and rollback semantics.
---
# Designing Switch Thumb Motion

## Parent Contract
**Required parent:** `designing-motion`.

## Decision ownership
Own the movement of switch thumb, track treatment, press deformation, and async commitment. Decide which geometry represents value and which feedback merely represents touch. This is separate from general switch semantics because spatial travel can itself become misleading state evidence.

## Evidence and inputs
Require switch dimensions, directionality, RTL policy, input modes, async mutation behavior, disabled/pending states, reduced motion, and platform conventions. Test taps near each side, keyboard activation, repeated activation, and server rejection.

## Decision procedure
Bind thumb destination to the authoritative value. Use press deformation only while contact is active; release must not imply value if the action was cancelled. If optimistic mutation is allowed, define explicit rollback that reverses from current position rather than teleporting. Mirror directional conventions only when the platform/value semantics warrant it; logical on/off must remain readable independent of left/right.

## Failure topology
Failures include thumb arriving before value commit, color changing on a different schedule than position, stale rollback after a second toggle, and RTL mirroring that reverses learned on/off meaning. Excessive spring overshoot can also make a binary control appear indeterminate.

## Falsification
Toggle during network delay, toggle again during rollback, change writing direction, and enable reduced motion. Fail if position, accessible state, and persisted state disagree; if an animation cannot be interrupted; or if direction becomes the sole carrier of on/off meaning.

## Output contract
Return a `switch-thumb-motion-contract` with authoritative state binding, press/release phases, travel curve, optimistic policy, rollback/retarget rules, directionality, reduced-motion equivalent, and contradiction tests.

<!-- SKILL: designing-selection-highlight-motion | parent=designing-motion | family=motion-specialist | output=selection-highlight-motion-contract -->
---
name: designing-selection-highlight-motion
description: Use when selection highlight changes across rows, tabs, cards, text ranges, or canvas objects and temporal emphasis must preserve selected identity.
---
# Designing Selection Highlight Motion

## Parent Contract
**Required parent:** `designing-motion`.

## Decision ownership
Own animated highlight appearance, transfer, and removal while keeping selection semantics separate from hover and focus. Decide when a shared highlight can move between peers and when independent state changes are safer because items are distant, virtualized, or reordered.

## Evidence and inputs
Require selection cardinality, focus model, virtualization/reordering behavior, object identity, density, input modality, and reduced-motion policy. Inspect multi-select, range extension, deselection, data refresh, and selection restoration after navigation.

## Decision procedure
Animate only stable identities. A peer indicator may translate when the spatial relationship is meaningful; otherwise use synchronized local transitions. For multi-select, avoid sequential choreography that suggests ordering where none exists. Keep focus rings temporally independent. On virtualization or sort, prioritize immediate semantic truth over attempting to fly a highlight to a recycled DOM position.

## Failure topology
Failures include highlight following index instead of identity, hover stealing selected styling, range selection producing a wave that slows feedback, and shared indicators crossing unrelated groups. Motion can also hide deselection when opacity lingers too long.

## Falsification
Select, reorder, filter, virtualize, and restore items while changing focus independently. Fail if a highlight lands on the wrong object, if multiple selection is temporarily understated, or if reduced motion causes selected and unselected states to become visually ambiguous.

## Output contract
Return a `selection-highlight-motion-contract` covering identity binding, local/shared transition choice, multi-select behavior, focus separation, virtualization rules, reduced motion, and tests for reordering and restoration.

<!-- SKILL: designing-tooltip-appearance-motion | parent=designing-motion | family=motion-specialist | output=tooltip-appearance-motion-contract -->
---
name: designing-tooltip-appearance-motion
description: Use when tooltips appear or disappear and timing plus motion must support discovery without chasing pointers, delaying help, or obscuring targets.
---
# Designing Tooltip Appearance Motion

## Parent Contract
**Required parent:** `designing-motion`.

## Decision ownership
Own tooltip delay, entrance, exit, anchor continuity, and handoff between adjacent targets. Decide how motion responds to pointer intent, keyboard focus, touch alternatives, and reduced-motion preferences without changing tooltip semantics.

## Evidence and inputs
Require tooltip trigger model, dwell policy, anchor geometry, pointer trajectories, keyboard behavior, collision placement, content length, accessibility constraints, and whether the tooltip is purely descriptive or interactive content that should be a different component.

## Decision procedure
Separate delay from animation duration. Use short opacity/scale or displacement tied to the resolved anchor, but never animate from arbitrary screen origins. Preserve fast handoff across a toolbar after the first tooltip has opened, while cancelling stale opens when the pointer has left. Exit should not create a dead zone that blocks the next target.

## Failure topology
Failures include tooltips chasing rapid hover, delayed stale content opening over a new target, motion moving the bubble through actionable UI, and focus-triggered tooltips disappearing before screen-reader or keyboard users can use the information. Long animation can multiply an already intentional dwell delay.

## Falsification
Sweep across dense toolbar targets, alternate pointer and keyboard, force collision placement, and enable reduced motion. Fail if a tooltip ever presents content for a non-current anchor, if motion adds meaningful access delay, or if cancellation leaves invisible hover blockers.

## Output contract
Return a `tooltip-appearance-motion-contract` with dwell rules, entrance/exit behavior, handoff timing, cancellation, collision retargeting, keyboard parity, reduced-motion behavior, and pointer-sweep tests.

<!-- SKILL: designing-carousel-page-motion | parent=designing-motion | family=motion-specialist | output=carousel-page-motion-contract -->
---
name: designing-carousel-page-motion
description: Use when a carousel or paged viewport moves among items and motion must preserve order, destination, interruption, and user-controlled pacing.
---
# Designing Carousel Page Motion

## Parent Contract
**Required parent:** `designing-motion`.

## Decision ownership
Own page-to-page motion for bounded collections, including direct jumps, swipes, button navigation, autoplay interruption, and wraparound representation. Decide how distance and direction encode collection order without implying impossible intermediate content.

## Evidence and inputs
Require collection size, looping policy, page width variability, drag physics, pagination indicators, autoplay, reduced motion, RTL behavior, media state, and whether content can change while transition is running.

## Decision procedure
Map drag distance to viewport movement during direct manipulation, then settle to an explicit destination. For multi-page jumps, avoid traversing every intermediate slide if that creates long motion; use compressed continuity or a direct transition. Pause autoplay on interaction and do not steal the viewport during reading. Define wraparound so the visual jump does not corrupt semantic index.

## Failure topology
Failures include unstoppable autoplay, long travel for distant jumps, stale media continuing on an offscreen slide, wraparound reversing unexpectedly, and swipe velocity choosing a destination inconsistent with visible displacement.

## Falsification
Swipe slowly and quickly, reverse mid-gesture, jump from first to last, resize during travel, and test autoplay with focus. Fail if the destination is unpredictable, if control input is ignored until animation ends, or if reduced motion still performs large spatial travel.

## Output contract
Return a `carousel-page-motion-contract` defining direct-manipulation mapping, settle thresholds, jump compression, wraparound, autoplay interruption, media handoff, directionality, reduced-motion equivalent, and destination tests.

<!-- SKILL: designing-navigation-stack-motion | parent=designing-motion | family=motion-specialist | output=navigation-stack-motion-contract -->
---
name: designing-navigation-stack-motion
description: Use when navigation has push, pop, drill-in, and return semantics and transition direction should expose stack relationships without becoming a source of truth itself.
---
# Designing Navigation Stack Motion

## Parent Contract
**Required parent:** `designing-motion`.

## Decision ownership
Own temporal/spatial encoding of stack depth for forward navigation, back navigation, modal detours, and interrupted transitions. Decide when spatial direction reinforces hierarchy and when crossfade or immediate replacement is less misleading.

## Evidence and inputs
Require navigation graph, history semantics, platform back behavior, RTL conventions, deep links, restored sessions, modal routes, reduced motion, and transition interruption support.

## Decision procedure
Derive motion from semantic relationship, not URL string order. A push/pop pair should be reversible and preserve source/destination identity. Deep-link entry has no fabricated predecessor and should not animate as if one existed. If a modal sits above a stack, separate its presentation axis from stack depth. Back during transition must retarget or complete deterministically.

## Failure topology
Failures include direction contradicting actual back history, deep links sliding from invented screens, double navigation leaving stacked visual remnants, and transitions that lock the back action. RTL mirroring can be wrong when spatial hierarchy is not linguistic direction.

## Falsification
Enter by deep link, push twice, pop during animation, restore history, and test both writing directions. Fail if transition direction can imply a false navigation relation, if interruption changes final route, or if reduced motion breaks orientation cues entirely.

## Output contract
Return a `navigation-stack-motion-contract` with relationship classes, push/pop pairing, deep-link policy, modal separation, interruption rules, directionality, reduced-motion equivalent, and history-consistency tests.

<!-- SKILL: designing-route-depth-motion | parent=designing-motion | family=motion-specialist | output=route-depth-motion-contract -->
---
name: designing-route-depth-motion
description: Use when routes express parent, child, peer, or cross-domain relationships and motion should reveal information depth rather than merely decorate page changes.
---
# Designing Route Depth Motion

## Parent Contract
**Required parent:** `designing-motion`.

## Decision ownership
Own transition grammar across information-architecture relationships beyond a simple back stack. Classify parent-child, peer switch, context switch, and external jump, then assign only motion that helps users update their mental map.

## Evidence and inputs
Require route taxonomy, persistent shell regions, shared objects, cross-fades, loading boundaries, history behavior, reduced motion, and responsive transformations. Identify which regions persist and which actually change.

## Decision procedure
Keep persistent shell stable. Use depth cues only for genuine hierarchy; peer routes should not look like deeper drill-down. Cross-domain jumps may need a neutral transition plus stronger orientation after arrival. Shared elements are permitted only when identity is stable. Loading should not force a second unrelated transition once data arrives.

## Failure topology
Failures include every route sliding the same way, shell chrome moving unnecessarily, peer tabs appearing hierarchical, and route change followed by content jump that destroys continuity. Motion that encodes hierarchy incorrectly is worse than no motion.

## Falsification
Traverse parent-child, sibling, deep-link, and cross-section routes; resize between wide and narrow layouts. Fail if users could infer the wrong route relation from motion, if persistent regions lose continuity, or if reduced motion removes all post-navigation orientation.

## Output contract
Return a `route-depth-motion-contract` with route relationship taxonomy, stable regions, transition families, loading handoff, responsive mapping, reduced-motion replacement cues, and hierarchy-consistency tests.

<!-- SKILL: designing-drop-settlement-motion | parent=designing-motion | family=motion-specialist | output=drop-settlement-motion-contract -->
---
name: designing-drop-settlement-motion
description: Use when a dragged object is released and the interface must reconcile pointer position with a valid destination, snap, rejection, or restored origin.
---
# Designing Drop Settlement Motion

## Parent Contract
**Required parent:** `designing-motion`.

## Decision ownership
Own the post-release phase of direct manipulation: acceptance, snapping, insertion, rejection, and rollback. The skill begins when pointer ownership ends and ensures the object settles into semantic layout without inventing a false successful drop.

## Evidence and inputs
Require drag/drop contract, valid targets, insertion geometry, snapping rules, async acceptance, source placeholder behavior, virtualization, reduced motion, and whether a rejected item returns to a stable origin.

## Decision procedure
Resolve destination first, then animate to canonical geometry. Keep source/destination placeholders consistent so layout does not jump twice. For async acceptance, distinguish provisional placement from confirmed placement. Rejection should return or dissolve according to object persistence, with a clear reason available separately from motion. Retarget settlement if layout shifts before completion.

## Failure topology
Failures include animating into an invalid target then teleporting back, source placeholders collapsing too early, stale coordinates after scroll, settlement that obscures insertion order, and long elastic bounces that imply uncertainty.

## Falsification
Drop at target edges, into a target that becomes invalid, during scrolling, and into a virtualized list. Fail if the animation endpoint differs from canonical layout, if rejected operations look committed, or if reduced motion eliminates the necessary destination cue.

## Output contract
Return a `drop-settlement-motion-contract` covering destination resolution, placeholder timing, canonical endpoint, provisional state, rejection recovery, retargeting, reduced motion, and geometry-consistency tests.

<!-- SKILL: designing-resize-feedback-motion | parent=designing-motion | family=motion-specialist | output=resize-feedback-motion-contract -->
---
name: designing-resize-feedback-motion
description: Use when panels, objects, columns, or windows resize and feedback must remain coupled to user movement while constraints and post-release layout settle visibly.
---
# Designing Resize Feedback Motion

## Parent Contract
**Required parent:** `designing-motion`.

## Decision ownership
Own temporal behavior during and after resize: live response, throttled preview, constraint resistance, snap points, and final settlement. It does not define resize semantics themselves; it prevents motion smoothing from decoupling geometry from the user's hand.

## Evidence and inputs
Require resizable dimensions, minimum/maximum values, snap thresholds, performance budget, expensive content reflow, pointer/keyboard alternatives, reduced motion, and persistence behavior.

## Decision procedure
During direct manipulation, favor one-to-one geometry or a clearly declared lightweight proxy. Never add spring lag between pointer and edge. Show resistance or hard stop consistently at constraints. If expensive content updates are deferred, keep boundary feedback live and reconcile content at release without a second surprising size change. Keyboard resizing should use deterministic increments rather than simulated drag animation.

## Failure topology
Failures include rubbery lag, hidden min/max thresholds, preview size differing from committed size, text reflow chasing the handle, and snapped dimensions overshooting then bouncing. Another failure is animated persistence restoration that makes startup layout unstable.

## Falsification
Resize rapidly, hit constraints, cross snap points, resize with keyboard, and simulate slow content. Fail if the edge trails input, if committed size differs from indicated size, or if reduced motion changes reachable geometry.

## Output contract
Return a `resize-feedback-motion-contract` with live/proxy policy, constraint response, snap settlement, content-reflow strategy, keyboard behavior, persistence, reduced-motion treatment, and latency tests.

<!-- SKILL: designing-pan-inertia-motion | parent=designing-motion | family=motion-specialist | output=pan-inertia-motion-contract -->
---
name: designing-pan-inertia-motion
description: Use when a pannable surface continues after release and inertial movement must preserve control, boundaries, selection context, and predictable stopping.
---
# Designing Pan Inertia Motion

## Parent Contract
**Required parent:** `designing-motion`.

## Decision ownership
Own velocity sampling, decay, bounds, cancellation, and handoff for inertial panning on canvases, maps, timelines, and large workspaces. Separate viewport momentum from object dragging and from browser/page scrolling.

## Evidence and inputs
Require coordinate space, pan bounds, overscroll policy, input device, zoom coupling, nested scroll surfaces, selection behavior, reduced motion, and frame-rate budget. Measure real pointer/touch velocity rather than assuming a fixed fling.

## Decision procedure
Estimate release velocity from a stable recent window, cap pathological spikes, then use monotonic decay. Any new direct input cancels inertia immediately. At bounds, stop or use a platform-consistent constrained response; do not bounce if precision work is primary. Preserve world coordinates and selected object identity while the viewport moves.

## Failure topology
Failures include momentum that cannot be stopped, diagonal drift from noisy samples, overshoot beyond valid world bounds, nested scroll stealing, and zoom occurring around a moving unintended anchor. Long inertia can also make precise editors feel uncontrollable.

## Falsification
Fling at different velocities, interrupt instantly, hit every bound, change zoom mid-motion, and test nested scrolling. Fail if motion survives new input, if viewport position becomes non-deterministic, or if reduced motion still launches prolonged autonomous travel.

## Output contract
Return a `pan-inertia-motion-contract` with velocity estimator, decay model, caps, boundary handling, cancellation, nested-scroll ownership, zoom interaction, reduced-motion policy, and stopping-distance tests.

<!-- SKILL: designing-zoom-continuity-motion | parent=designing-motion | family=motion-specialist | output=zoom-continuity-motion-contract -->
---
name: designing-zoom-continuity-motion
description: Use when viewport scale changes and animation must keep the user's focal object spatially coherent across wheel, pinch, controls, fit, and semantic zoom levels.
---
# Designing Zoom Continuity Motion

## Parent Contract
**Required parent:** `designing-motion`.

## Decision ownership
Own animated scale continuity and focal anchoring. Decide when zoom should be continuous, stepped, or immediate, and how semantic detail changes are synchronized without making objects appear to jump identity.

## Evidence and inputs
Require world/viewport transforms, zoom limits, anchor policy, semantic thresholds, input modalities, fit/selection commands, performance budget, and reduced motion. Identify whether labels and controls change representation at scale thresholds.

## Decision procedure
Anchor pointer/pinch zoom to the interaction focal point and command zoom to a declared target such as selection or viewport center. Maintain world coordinate truth throughout interpolation. Cross semantic thresholds with short crossfades or discrete swaps tied to stable object identity; do not combine major representation change with uncontrolled camera travel.

## Failure topology
Failures include focal objects drifting from the cursor, transform rounding accumulating error, fit commands overshooting, labels flickering around thresholds, and semantic zoom replacing an object with a visually unrelated one mid-flight.

## Falsification
Zoom repeatedly in/out around one point, cross every semantic threshold, invoke fit and zoom-to-selection, and interrupt. Fail if the anchor drifts, if scale cannot be reversed cleanly, or if reduced motion alters the final world transform.

## Output contract
Return a `zoom-continuity-motion-contract` with anchor rules, interpolation, semantic thresholds, command targets, interruption, numerical precision, reduced-motion behavior, and round-trip transform tests.

<!-- SKILL: designing-parallax-motion | parent=designing-motion | family=motion-specialist | output=parallax-motion-contract -->
---
name: designing-parallax-motion
description: Use when layers move at different rates and parallax must communicate depth or hierarchy without harming readability, orientation, vestibular comfort, or input precision.
---
# Designing Parallax Motion

## Parent Contract
**Required parent:** `designing-motion`.

## Decision ownership
Own whether differential layer motion is justified, its amplitude, coordinate source, clamping, and reduced-motion replacement. This skill treats parallax as a spatial claim, not a decorative default.

## Evidence and inputs
Require depth semantics, scroll/pointer source, content hierarchy, text-bearing layers, vestibular risk, platform performance, touch behavior, and reduced-motion settings. Determine whether the apparent depth helps users understand structure or only adds spectacle.

## Decision procedure
Keep primary reading/action layers stable. Apply small bounded offsets to genuinely background or contextual layers and ensure movement never changes hit-test geometry. Clamp at edges and define behavior during fast jumps or restored scroll position. Under reduced motion, collapse differential movement while preserving hierarchy through static depth, scale, or tonal cues.

## Failure topology
Failures include text sliding independently of its controls, pointer targets visually drifting from hit areas, nausea from large opposing motion, scroll-jacking, and backgrounds exposing blank edges. Decorative parallax can also compete with data or task urgency.

## Falsification
Scroll slowly and rapidly, jump by keyboard, resize, restore a deep scroll position, and enable reduced motion. Fail if interactive geometry and visual geometry diverge, if content readability worsens, or if depth meaning disappears completely when motion is disabled.

## Output contract
Return a `parallax-motion-contract` with semantic justification, layer eligibility, amplitude/clamp, input source, hit-test invariants, reduced-motion substitution, performance bounds, and edge-case tests.

<!-- SKILL: designing-progress-indicator-motion | parent=designing-motion | family=motion-specialist | output=progress-indicator-motion-contract -->
---
name: designing-progress-indicator-motion
description: Use when determinate or indeterminate progress is animated and temporal behavior must reflect real work rather than fabricate certainty or stall perception.
---
# Designing Progress Indicator Motion

## Parent Contract
**Required parent:** `designing-motion`.

## Decision ownership
Own interpolation between reported progress values, indeterminate cycles, completion transition, and regression handling. The skill protects quantitative truth while preventing jitter from noisy backend updates.

## Evidence and inputs
Require progress semantics, update frequency, monotonicity guarantees, phase weighting, cancellation, failure states, reduced motion, and expected duration. Determine whether percent is measured, estimated, or merely phase-based.

## Decision procedure
Never animate beyond the latest defensible value. Smooth frequent monotonic updates within a bounded lag so visual progress catches up promptly. If progress can regress because total work changes, show the reason rather than hiding truth. Indeterminate motion should be low-attention and switch cleanly to determinate once measurement exists. Completion animation begins only after successful completion.

## Failure topology
Failures include bars reaching 100% before success, fake steady progress over a stalled task, infinite indeterminate loops with no status, regression concealed by clamping, and reduced-motion mode replacing progress with no perceivable activity.

## Falsification
Feed bursty, stalled, regressing, failed, and cancelled progress streams. Fail if the visual value exceeds authoritative value, if completion is shown before success, or if users cannot distinguish active work from a hung task.

## Output contract
Return a `progress-indicator-motion-contract` with value truth, interpolation lag, indeterminate cycle, regression policy, completion gate, cancellation/failure behavior, reduced-motion equivalent, and stream tests.

<!-- SKILL: designing-skeleton-shimmer-motion | parent=designing-motion | family=motion-specialist | output=skeleton-shimmer-motion-contract -->
---
name: designing-skeleton-shimmer-motion
description: Use when skeleton placeholders animate and the motion must indicate temporary loading without drawing attention away from content structure or becoming a false progress signal.
---
# Designing Skeleton Shimmer Motion

## Parent Contract
**Required parent:** `designing-motion`.

## Decision ownership
Own optional shimmer/pulse behavior on skeletons, including cadence, grouping, duration ceiling, stopping, and reduced-motion substitution. It does not decide whether skeleton loading itself is appropriate; it governs motion once that pattern is chosen.

## Evidence and inputs
Require expected latency distribution, skeleton geometry, number of simultaneous placeholders, theme contrast, reduced motion, battery/performance constraints, and transitions to partial real content.

## Decision procedure
Prefer subtle low-frequency motion that reinforces “placeholder” without resembling a determinate meter. Synchronize large groups rather than creating noisy independent waves. Stop animation as each real region resolves; do not leave shimmer behind opaque content. For long waits, supplement with status rather than increasing animation intensity.

## Failure topology
Failures include high-contrast sweeping glare, dozens of asynchronous shimmers, animation continuing behind loaded content, and users inferring progress from shimmer travel. Constant GPU-heavy gradients can also waste resources on low-end devices.

## Falsification
Load many skeletons, resolve regions out of order, keep a request stalled, test dark/high-contrast themes, and enable reduced motion. Fail if shimmer becomes the dominant visual element, consumes significant frame budget, or persists after authoritative content arrives.

## Output contract
Return a `skeleton-shimmer-motion-contract` with eligibility, cadence, synchronization, stop conditions, long-wait behavior, reduced-motion fallback, performance budget, and partial-resolution tests.

<!-- SKILL: designing-chart-enter-exit-motion | parent=designing-motion | family=motion-specialist | output=chart-enter-exit-motion-contract -->
---
name: designing-chart-enter-exit-motion
description: Use when chart marks enter, exit, or change membership and animation must preserve data correspondence rather than imply invented trajectories or values.
---
# Designing Chart Enter Exit Motion

## Parent Contract
**Required parent:** `designing-motion`.

## Decision ownership
Own membership-change animation for bars, points, lines, areas, and categorical marks. Decide how identity keys map old to new marks, how exits avoid masking new values, and when immediate redraw is safer because correspondence is ambiguous.

## Evidence and inputs
Require stable data keys, chart grammar, sorting/filtering behavior, axis changes, sampling, uncertainty, update frequency, reduced motion, and whether marks can split/merge. Data identity outranks screen position.

## Decision procedure
Match marks by semantic key before interpolating. Enter from a neutral baseline only when that baseline has quantitative meaning; otherwise use opacity or local emphasis. Exit without dragging a mark through values it never held. When sorting changes, separate reordering from value change so users can track identity. Large streaming updates may need sampled or no animation.

## Failure topology
Failures include index-based morphs linking unrelated categories, bars growing from zero on a truncated axis, line points flying across missing intervals, and exit animation leaving obsolete data visible during decisions.

## Falsification
Reorder categories, filter, add/remove series, change axis domains, and stream high-frequency updates. Fail if animation depicts a data value never present, if identity swaps, or if reduced motion changes the quantitative endpoint.

## Output contract
Return a `chart-enter-exit-motion-contract` with keying strategy, entry/exit primitives, sort handling, axis/domain rules, update-rate threshold, reduced-motion equivalent, and correspondence tests.

<!-- SKILL: designing-spring-motion | parent=designing-motion | family=motion-specialist | output=spring-motion-contract -->
---
name: designing-spring-motion
description: Use when an interface uses spring dynamics and stiffness, damping, mass, initial velocity, and settlement must be chosen from interaction intent rather than copied as decorative constants.
---
# Designing Spring Motion

## Parent Contract
**Required parent:** `designing-motion`.

## Decision ownership
Own physical spring parameterization, settlement criteria, velocity inheritance, and suitability. Decide whether spring dynamics fit the interaction at all; precision and high-stakes state changes often require critically damped or non-physical transitions.

## Evidence and inputs
Require travel distance, direct-manipulation velocity, acceptable overshoot, interaction frequency, target size, interruption behavior, platform convention, reduced motion, and performance constraints.

## Decision procedure
Choose damping regime from semantic intent, then parameterize for consistent perceived settlement across realistic distances. Inherit release velocity only when motion continues a user gesture. Cap overshoot where crossing a boundary could imply invalid state. Define a numerical rest threshold so state does not oscillate indefinitely. Retarget from current position and velocity rather than restarting.

## Failure topology
Failures include one copied spring producing wildly different duration by distance, bounce on destructive controls, rest thresholds that consume frames forever, and retargeting that jumps because velocity is discarded. Excessive overshoot can communicate uncertainty.

## Falsification
Exercise short and long travel, high release velocity, repeated retargets, reduced motion, and low frame rate. Fail if settlement time becomes unpredictable, boundaries are crossed misleadingly, or the final state depends on frame cadence.

## Output contract
Return a `spring-motion-contract` with suitability rationale, parameter set, velocity policy, overshoot bounds, rest thresholds, retargeting, reduced-motion alternative, and deterministic trajectory tests.

<!-- SKILL: designing-decay-motion | parent=designing-motion | family=motion-specialist | output=decay-motion-contract -->
---
name: designing-decay-motion
description: Use when released velocity should coast and decay, such as scrolling or free panning, and stopping distance must remain controllable and bounded.
---
# Designing Decay Motion

## Parent Contract
**Required parent:** `designing-motion`.

## Decision ownership
Own non-spring inertial decay: velocity capture, friction curve, stopping threshold, maximum travel, and cancellation. Choose decay only when no semantic destination must be selected immediately.

## Evidence and inputs
Require gesture velocity distribution, coordinate units, bounds, snap destinations, nested scrolling, device class, reduced motion, and precision needs. Distinguish continuous world travel from discrete paging, where decay alone is insufficient.

## Decision procedure
Sample velocity robustly, clamp outliers, apply a monotonic friction model, and calculate expected stopping distance. Cancel on new input. If a snap target becomes relevant, hand off once to a settlement owner rather than layering spring and decay simultaneously. Constrain travel near edges without silently changing content selection.

## Failure topology
Failures include endless low-velocity drift, travel too far after small gestures, frame-rate-dependent stopping, decay fighting snap animation, and inability to interrupt. Applying decay to discrete choices can land between valid states.

## Falsification
Compare stopping distance across frame rates, device velocities, bounds, and immediate interruption. Fail if identical initial conditions produce materially different endpoints, if users cannot stop motion, or if reduced motion still creates long autonomous travel.

## Output contract
Return a `decay-motion-contract` with velocity estimator, friction function, caps, stop threshold, boundary/snap handoff, cancellation, reduced-motion policy, and frame-rate invariance tests.

<!-- SKILL: designing-elastic-overscroll-motion | parent=designing-motion | family=motion-specialist | output=elastic-overscroll-motion-contract -->
---
name: designing-elastic-overscroll-motion
description: Use when a scrollable or draggable surface permits temporary movement beyond a boundary and elasticity must signal resistance without implying additional content.
---
# Designing Elastic Overscroll Motion

## Parent Contract
**Required parent:** `designing-motion`.

## Decision ownership
Own resistance curve, maximum displacement, release return, nested-boundary handoff, and platform eligibility for elastic overscroll. Decide whether elasticity belongs at all in precision, desktop, or high-stakes contexts.

## Evidence and inputs
Require scroll bounds, platform behavior, nested containers, pull-to-refresh conflicts, direct manipulation, reduced motion, hit testing, and content at the boundary. Identify any gesture whose meaning begins only after overscroll threshold.

## Decision procedure
Map additional input to diminishing visual displacement while keeping logical scroll position clamped. Keep hit targets and content state tied to logical coordinates. On release, return promptly unless a separate threshold action has explicitly claimed the gesture. Nested containers must declare which boundary owns resistance.

## Failure topology
Failures include users believing hidden content exists beyond the edge, overscroll triggering refresh accidentally, visual displacement breaking hit testing, nested rubber bands stacking, and large recoil causing vestibular discomfort.

## Falsification
Overscroll each edge, nest two scroll surfaces, cross and retreat from a refresh threshold, and enable reduced motion. Fail if logical position changes beyond bounds, if ownership is ambiguous, or if reduced motion leaves a large recoil animation.

## Output contract
Return an `elastic-overscroll-motion-contract` with eligibility, resistance curve, displacement cap, logical-coordinate invariant, nested ownership, threshold handoff, reduced-motion behavior, and boundary tests.

<!-- SKILL: designing-motion-reversal | parent=designing-motion | family=motion-specialist | output=motion-reversal-contract -->
---
name: designing-motion-reversal
description: Use when a user reverses an action while its transition is still running and the interface must reverse continuously without stale completion or temporal discontinuity.
---
# Designing Motion Reversal

## Parent Contract
**Required parent:** `designing-motion`.

## Decision ownership
Own reversal of a transition toward its source state. Distinguish true reversal from retargeting to a third state and define continuity for position, velocity, opacity, and semantic commitment.

## Evidence and inputs
Require reversible state pairs, current interpolation state, side effects, commit timing, easing or physics model, focus behavior, and reduced-motion policy. Determine whether the underlying action itself can still be undone or only the visual transition can reverse.

## Decision procedure
Read current rendered state and reverse from there; never restart from the nominal endpoint. Preserve velocity when physically coherent, or remap timing to avoid an abrupt jerk. If the semantic action has already crossed an irreversible boundary, do not visually reverse as though it were cancelled; instead complete and expose explicit recovery.

## Failure topology
Failures include double flashes from restarting animations, stale completion callbacks writing the old state, reversing visuals after irreversible side effects, and focus moving twice. Repeated reversals can accumulate timing error or event listeners.

## Falsification
Reverse at 10%, 50%, and 90%, repeat rapidly, and combine with async commit. Fail if there is a visible jump, if final semantic state differs from the latest intent, or if obsolete completion handlers fire after reversal.

## Output contract
Return a `motion-reversal-contract` with reversible state pairs, semantic cutoff, continuity rules, callback invalidation, velocity/timing policy, reduced-motion behavior, and rapid-reversal tests.

<!-- SKILL: designing-motion-cancellation | parent=designing-motion | family=motion-specialist | output=motion-cancellation-contract -->
---
name: designing-motion-cancellation
description: Use when an animation becomes irrelevant because context, navigation, data, or user intent changed and it must stop without leaving transient geometry or stale side effects.
---
# Designing Motion Cancellation

## Parent Contract
**Required parent:** `designing-motion`.

## Decision ownership
Own cancellation semantics for in-flight animation: what state is committed, what callbacks are invalidated, what temporary layers are cleaned up, and whether the visual snaps to source, destination, or latest canonical state.

## Evidence and inputs
Require animation ownership, semantic action status, navigation lifecycle, async tasks, temporary DOM/layers, focus restoration, reduced-motion mode, and concurrency. Catalog animations that can outlive their component or data identity.

## Decision procedure
Tie every animation to a cancellable owner and generation/version. On invalidation, read authoritative semantic state, render that state immediately or with a new valid transition, and suppress stale completion effects. Remove temporary clones, transforms, pointer blockers, and timers. Cancellation must not silently cancel the underlying user action unless that is its explicit contract.

## Failure topology
Failures include orphaned overlays, hidden elements remaining `pointer-events:none`, old completion callbacks changing state on a new screen, and cancellation mistakenly rolling back saved data. Memory leaks are temporal UX failures when repeated transitions degrade responsiveness.

## Falsification
Navigate away mid-transition, replace data identity, destroy and recreate the component, and trigger several cancellations. Fail if stale layers remain, focus is lost, callbacks mutate new state, or repeated cancellation degrades performance.

## Output contract
Return a `motion-cancellation-contract` with owner/version model, canonical-state resolution, cleanup list, callback invalidation, semantic-action separation, reduced-motion interaction, and lifecycle stress tests.

<!-- SKILL: designing-attention-cue-motion | parent=designing-motion | family=motion-specialist | output=attention-cue-motion-contract -->
---
name: designing-attention-cue-motion
description: Use when motion is intentionally used to direct attention to a changed, urgent, or newly relevant element and salience must be proportional, finite, and non-coercive.
---
# Designing Attention Cue Motion

## Parent Contract
**Required parent:** `designing-motion`.

## Decision ownership
Own eligibility, intensity, repetition, and stopping for attention-directing motion such as a brief pulse, highlight sweep, or positional nudge. Distinguish notification importance from marketing desire for engagement.

## Evidence and inputs
Require event severity, user task, frequency, competing alerts, whether the change is otherwise visible, accessibility/vestibular constraints, reduced motion, and acknowledgement state. Measure how often the cue can occur in real workflows.

## Decision procedure
Use motion only for actionable state change whose location might otherwise be missed. Prefer one brief finite cue and persist significance through static styling or status until resolved. Escalate salience by information architecture before repetition. Never loop motion simply to force engagement, and never move controls away from a user's pointer.

## Failure topology
Failures include perpetual pulsing, several regions competing simultaneously, low-priority marketing animation resembling critical alerts, and cues that disappear without a persistent state indication. Repeated motion can become both inaccessible and functionally invisible through habituation.

## Falsification
Generate bursts of low- and high-severity events while the user is typing or manipulating another object. Fail if motion steals input, loops without new information, makes priority indistinguishable, or if reduced motion removes the only indication of changed state.

## Output contract
Return an `attention-cue-motion-contract` with eligibility criteria, salience tiers, duration/repetition limits, persistent companion cue, interruption policy, reduced-motion substitute, and alert-burst tests.

<!-- SKILL: designing-motion-choreography | parent=designing-motion | family=motion-specialist | output=motion-choreography-contract -->
---
name: designing-motion-choreography
description: Use when multiple interface regions animate in one state change and sequencing must communicate causality and priority without turning the transition into a staged spectacle.
---
# Designing Motion Choreography

## Parent Contract
**Required parent:** `designing-motion`.

## Decision ownership
Own relative timing among concurrent animations belonging to one semantic transition. Decide which elements move together, which sequence, and which remain stable, based on causal dependency and visual hierarchy rather than arbitrary stagger formulas.

## Evidence and inputs
Require the semantic state change, affected regions, persistent anchors, dependency order, interaction readiness, total latency budget, reduced motion, and device performance. Identify which element provides orientation and must not be delayed.

## Decision procedure
Group simultaneous effects that represent one atomic change. Sequence only when later state genuinely depends on earlier revelation or when overlap would obscure causality. Bound total transition time independent of item count; large collections should not accumulate per-item stagger. Make actionable destinations ready no later than their visible availability.

## Failure topology
Failures include cascade delays proportional to list length, controls visible before interactive, shell regions animating merely because content changed, and overlapping effects that conceal the primary result. Choreography can make routine work feel slow even when each animation is short.

## Falsification
Run the same transition with 3, 30, and 300 affected items, interrupt halfway, and test low-end performance. Fail if total duration grows unbounded, if visual readiness and input readiness diverge, or if reduced motion destroys causal ordering needed to understand the change.

## Output contract
Return a `motion-choreography-contract` with animation groups, dependency graph, concurrency/sequence rules, duration ceiling, readiness gates, large-set policy, reduced-motion mapping, and scale tests.

<!-- SKILL: designing-loading-content-handoff-motion | parent=designing-motion | family=motion-specialist | output=loading-content-handoff-motion-contract -->
---
name: designing-loading-content-handoff-motion
description: Use when placeholders, previous content, or progress states transition into real content and the handoff must avoid flash, layout shift, stale overlap, or delayed usability.
---
# Designing Loading Content Handoff Motion

## Parent Contract
**Required parent:** `designing-motion`.

## Decision ownership
Own the exact temporal handoff between loading representation and authoritative content. Decide whether to replace immediately, crossfade, preserve stale content until new data is ready, or resolve regions independently.

## Evidence and inputs
Require loading pattern, layout skeleton accuracy, partial response behavior, stale-while-refresh semantics, content dimensions, focus/selection, reduced motion, and latency distribution. Identify which content can arrive independently.

## Decision procedure
Reserve geometry before arrival. When real content is ready, prioritize interactivity and semantic exposure, then use only brief visual blending if it prevents flash. Never leave both placeholder and real controls focusable. Preserve stale content explicitly when it remains useful; label refresh rather than dimming it into ambiguous limbo. Partial regions may hand off separately if their boundaries are stable.

## Failure topology
Failures include skeleton and real text overlapping, crossfades delaying clickability, focus jumping as placeholder nodes disappear, stale data looking current, and a second layout shift after animation ends.

## Falsification
Resolve content instantly, slowly, partially, and after stale refresh; keep keyboard focus inside the region. Fail if two semantic copies coexist, if input readiness lags visual readiness, if focus is lost, or if reduced motion increases layout shift.

## Output contract
Return a `loading-content-handoff-motion-contract` with geometry reservation, semantic swap point, visual blend policy, partial-resolution rules, stale-content treatment, focus preservation, reduced-motion behavior, and overlap/layout tests.

<!-- SKILL: designing-spatial-reorientation-motion | parent=designing-motion | family=motion-specialist | output=spatial-reorientation-motion-contract -->
---
name: designing-spatial-reorientation-motion
description: Use when the interface recenters, rotates, fits, changes projection, or otherwise reorients a spatial workspace and users must retain a reliable sense of where they are.
---
# Designing Spatial Reorientation Motion

## Parent Contract
**Required parent:** `designing-motion`.

## Decision ownership
Own camera/view transition used for orientation recovery: fit-to-selection, reset view, north-up, scene focus, timeline jump, or similar large spatial changes. Decide path, duration, anchor, and static orientation cues.

## Evidence and inputs
Require coordinate system, current and target view transforms, selected/focused object, world scale, rotation/projection options, motion sensitivity, and input interruption. Determine whether direct interpolation would cross meaningless or disorienting space.

## Decision procedure
Keep a stable semantic anchor visible whenever possible. Compress very long travel rather than literally flying across the entire world. For rotation, choose the shortest unambiguous path unless domain direction matters. Pair large changes with static cues such as minimap, compass, breadcrumbs, selection outline, or coordinate readout so reduced motion can jump without loss of context.

## Failure topology
Failures include cinematic flights through irrelevant space, rotation taking the long path, selected objects disappearing, projection changes morphing geometry misleadingly, and new input being ignored until travel ends.

## Falsification
Reorient between extreme views, interrupt immediately, switch projections, and enable reduced motion. Fail if target identity is lost, if motion passes through misleading intermediate states, if orientation depends solely on animation, or if final transform differs by interruption path.

## Output contract
Return a `spatial-reorientation-motion-contract` with anchor, path selection, travel compression, rotation/projection rules, static orientation cues, interruption, reduced-motion equivalent, and extreme-view tests.
