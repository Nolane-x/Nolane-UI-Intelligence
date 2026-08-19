---
name: designing-staggered-reveal-motion
description: Use when multiple related elements appear together and stagger could communicate order or grouping without serializing access, exaggerating hierarchy or creating repetitive entrance noise.
---

# Designing Staggered Reveal Motion

## Parent Contract
**Required parent:** `designing-motion`.

This faculty owns temporal offset among a set of elements entering the same state. It does not decide content priority, list ordering or whether entrance animation is needed at all.

## Decision Model
A stagger should encode something: reading order, causal propagation, spatial wave, process sequence or group relationship. If every dashboard card simply fades in with `index × delay`, the stagger is ornamental latency.

Define a maximum temporal envelope for the whole group. Ten items should not take ten times longer than two. Use compressed offsets, grouped waves or simultaneous reveal after a threshold. Critical controls and content should become operable when ready rather than waiting for their visual turn.

Repeated surfaces need suppression rules. Virtualized rows entering the viewport, route revisits, filtering, window resize and scroll recycling should not replay the same “first appearance” stagger endlessly. Distinguish initial reveal from newly created content and from ordinary visibility changes.

Direction must match semantics when one is implied. A left-to-right stagger is not universally correct under RTL or vertical reading. If the order is data-driven, derive temporal order from the same authoritative ordering rather than DOM accidents.

## Failure Topology
- The last item waits more than a second even though it is already available.
- Stagger order contradicts RTL or visual reading order.
- Scrolling a virtualized list continuously retriggers entrance waves.
- Important actions appear after decorative items.
- A loading retry replays a celebratory reveal and disguises instability.

## Falsification and Recovery
Test 2, 10, 100 and virtualized items; reorder/filter; revisit route; switch RTL; keyboard-jump into late items; reduce motion. Time the last meaningful item and verify operability is not gated by visual delay. If stagger carries no identifiable information, remove it.

Recover by compressing the group envelope, limiting animation to first meaningful reveal, grouping by semantic clusters and aligning order with locale/task structure.

## Output Contract
Return `staggered-reveal-contract` with semantic ordering rule, per-item/group offset, maximum envelope, replay suppression, interaction availability, locale direction, reduced-motion behavior and scale tests.