---
name: designing-animation-interruption-and-retargeting
description: Use when users or system events can change the target state before an animation finishes and the interface must converge immediately toward current truth without queued stale timelines or discontinuous jumps.
---

# Designing Animation Interruption and Retargeting

## Parent Contract
**Required parent:** `designing-motion`.

This faculty owns temporal correctness when target state changes mid-animation. It is cross-cutting: tabs, sheets, menus, toggles, shared elements and layout transitions may all depend on it.

## Decision Boundary
Animation is a projection of state, not an independent script. When the authoritative target changes, decide whether to **retarget from current visual state**, reverse, cancel-and-snap, or complete then transition. Queuing every requested animation is rarely correct for interactive UI because the queue can become history rather than current intent.

Retargeting must preserve continuity and semantics. If a sheet moving toward expanded is redirected to closed, derive the new trajectory from its current position/velocity while applying the closed-state safety policy. If a menu is semantically dismissed, it should stop receiving input immediately even if the opacity finishes naturally.

Different properties may have different interruption rules. Position can preserve velocity; color may interpolate from current computed value; discrete content/ARIA state should switch at semantic boundaries rather than crossfade through two truths. Shared-element transitions can abort if either identity disappears.

External events matter: viewport resize, reduced-motion preference change, route navigation, permission loss, server correction and component unmount can all invalidate the original target.

## Failure Topology
- Rapid toggles queue and the UI keeps animating after the model settles.
- Reversal restarts from the original endpoint, causing a visible jump.
- A dismissed surface remains interactive during visual exit.
- Route change leaves orphaned animation callbacks mutating unmounted state.
- Mid-animation reduced-motion preference is ignored until the next interaction.

## Falsification and Recovery
Hammer controls faster than transition duration, reverse drag release, resize mid-flight, navigate away, revoke permission, inject server rollback and toggle reduced motion. At every checkpoint compare semantic target, interactive hit region and visual trajectory. Any continued motion toward obsolete truth is a failure.

Recover by deriving animations from current state + latest target, centralizing cancellation lifecycle, separating semantic and visual completion, and snapping when continuity cannot be preserved safely.

## Output Contract
Return `animation-interruption-contract` with authoritative target source, per-property interruption policy, retarget/reverse math, semantic cutoff, external invalidators, cleanup behavior, reduced-motion response and adversarial event sequences.