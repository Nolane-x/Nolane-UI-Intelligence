---
name: designing-motion-performance-fallbacks
description: Use when motion quality may degrade under device, browser, rendering or workload constraints and the design needs explicit tiers that preserve meaning before visual richness.
---

# Designing Motion Performance Fallbacks

## Parent Contract
**Required parent:** `designing-motion`.

This specialist owns degradation of temporal effects under constrained rendering. It does not set the entire application performance budget or certify runtime performance by itself.

## Decision Model
Classify every motion channel by **semantic necessity**. Tier A communicates state/causality and must retain an equivalent even when animation is removed. Tier B improves orientation and can simplify. Tier C is ornamental and should disappear first. This prevents emergency performance work from randomly deleting the animation that carried the only state cue while preserving a background flourish.

Prefer cheap properties only when they preserve the intended mechanism. “Use transform and opacity” is not universal: a layout transition may require actual geometry, and faking it can displace focus/hit testing. Design a fallback rather than forcing one rendering technique.

Define triggers conservatively. User reduced-motion preference is an accessibility choice, not a proxy for slow hardware. Device heuristics are imperfect; runtime evidence such as sustained frame misses, battery/thermal context where available, or known low-power modes may justify simplification, but adaptation must not oscillate during a task.

Fallbacks should be stable across a session/context. Constantly switching between spring and snap based on instantaneous frame rate creates more perceptual instability than a consistently simpler transition.

## Failure Topology
- Decorative blur is retained while focus/selection transition becomes janky.
- A “low-end device” heuristic stereotypes capability and disables useful orientation unnecessarily.
- Runtime degradation toggles every few seconds and the interface feels inconsistent.
- Removing animation also removes the only indication that an item changed.
- GPU-heavy filters turn a simple modal into a frame-drop event.

## Falsification and Recovery
Throttle CPU/GPU where possible, create long lists, run concurrent updates, test battery/low-power modes, background/foreground transitions and reduced motion. Measure whether interaction latency, frame pacing and semantic feedback remain acceptable. A fallback that preserves smooth ornament but loses state information fails.

Recover by ranking channels, removing expensive Tier C effects, simplifying Tier B spatial travel, replacing Tier A motion with immediate redundant state cues, and locking the selected tier until a safe reevaluation boundary.

## Output Contract
Return `motion-performance-fallback-contract` with motion channel tiers, degradation triggers, stable tier policy, per-effect fallback, semantic equivalence, instrumentation requirements and constrained-runtime tests.