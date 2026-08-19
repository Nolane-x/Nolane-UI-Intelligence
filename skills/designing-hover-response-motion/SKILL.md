---
name: designing-hover-response-motion
description: Use when pointer hover should preview interactivity, reveal secondary affordance or increase target confidence without becoming required information or causing visual chatter.
---

# Designing Hover Response Motion

## Parent Contract
**Required parent:** `designing-motion`.

Hover motion is anticipatory feedback for devices that can genuinely hover. This faculty owns how an eligible target changes while a fine pointer crosses, dwells on, or leaves it. It does not own tooltip content, pointer semantics, focus treatment, or the action invoked after activation.

## Decision Model
Start by classifying the hover purpose. **Recognition hover** confirms “this is interactive.” **Preview hover** exposes a nonessential hint or media state. **Control-reveal hover** surfaces secondary actions that must also have focus/touch paths. **Spatial hover** highlights the exact row, node, segment or drop target under the pointer. Different purposes require different persistence and latency.

Do not animate every pointer crossing. Dense tables, menus and canvases can receive dozens of hover transitions per second; long fades and springy lifts accumulate into noise. Fast transit should usually produce subtle, interruptible state changes. A dwell-gated preview can wait longer because its cost is larger. Exit should not leave a ghost trail that lags behind the pointer.

Treat hover capability as conditional. `hover: none` and coarse pointers need an alternative; stylus hover, trackpad pointer and mouse may have different precision. Never hide a required action solely until hover. Focused elements should reach the same meaningful affordance without pretending keyboard focus is pointer hover.

Geometry must remain stable unless the interface explicitly uses spatial magnification. Enlarging a target on hover can move neighbors, change the pointer hit test and cause oscillation at boundaries. Prefer transforms that do not alter layout, or use reserved space.

## Failure Topology
- Critical labels or delete controls exist only on hover and disappear for touch/keyboard users.
- Every card lifts and casts a shadow, producing a generic “floating tiles” language unrelated to hierarchy.
- Slow exit easing leaves several rows visually active while the pointer moves quickly.
- A hover expansion changes hit geometry and repeatedly enters/leaves itself.
- Hover and selected state are indistinguishable.
- Remote desktop latency turns subtle motion into distracting delayed flicker.

## Falsification
Sweep the pointer rapidly across a dense region, alternate fine/coarse pointer emulation, navigate the same targets by keyboard, zoom text, and test a selected item while hovering a different one. The design fails if hover becomes necessary for discovery, obscures persistent state, destabilizes geometry, or produces more temporal noise than information.

## Recovery
Collapse to a single high-signal channel—tone, border, underline, cursor, or small transform—then reintroduce preview/reveal motion only where the purpose is explicit. If a hidden action is important, give it a persistent or focus/touch-accessible route.

## Output Contract
Return `hover-response-motion-contract` with hover purpose, eligible modalities, enter/dwell/exit behavior, interruption rules, geometry policy, focus/touch equivalence, state-separation rules, reduced-motion treatment and stress tests.