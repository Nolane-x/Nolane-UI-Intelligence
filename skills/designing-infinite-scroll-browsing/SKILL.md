---
name: designing-infinite-scroll-browsing
description: Use when content should continue progressively as users browse and the product must preserve position, termination, loading control, reachability, and return context without endless-scroll traps.
---

# Designing Infinite Scroll Browsing

## Parent Contract
**Required parent:** `designing-navigation`.

This faculty owns continuous continuation through a collection. It is not interchangeable with pagination: the primary state is an anchored stream position rather than an explicit page address. Use it only when uninterrupted exploration is more valuable than bounded position, deterministic jumps, or easy access to page footer content.

## Decision Model
Define the continuation trigger: automatic near-viewport prefetch, explicit “Load more,” or a hybrid. Automatic loading should not fire so aggressively that users cannot reach controls beneath the feed. The system needs a stable item identity and a position anchor so a detail detour, browser back, refresh, or app restoration can return to approximately the same content rather than the beginning.

Loading state belongs at the continuation boundary, not as a full-page reset. New items should append without shifting already-read content. If ranking or real-time updates can insert items above, buffer or badge them rather than moving the user’s viewport unexpectedly.

Termination must be visible. A finite feed should eventually say that the end is reached; an unbounded feed needs boundaries for error, retry, and rate-limiting. Accessibility requires a path that does not create an ever-growing virtual focus sequence with no landmarks or user control.

## Failure Topology
- New batches shift existing cards because image dimensions were unknown, destroying reading position.
- Returning from a detail page starts at item one.
- Automatic loading makes the footer permanently unreachable.
- An API error looks like the end of results.
- Fresh items insert above and move the viewport while the user is reading.
- Screen-reader users must traverse hundreds of accumulated nodes with no section landmarks or load control.

## Falsification and Recovery
Falsify with slow images, network failure on the fifth batch, back-navigation from a deep item, refreshed ranking, dynamic insertion above the viewport, keyboard navigation, screen readers, reduced-data mode, and a finite collection reaching its end. The design fails if continuation cannot distinguish loading/error/end or if the user’s place is not recoverable after ordinary navigation.

Recover by anchoring position to stable item IDs, reserving layout space, buffering upstream insertions, offering user-controlled continuation when needed, preserving return state, and making terminal/error states explicit.

## Output Contract
Return `infinite-scroll-browsing-contract` with continuation trigger, prefetch threshold, item-anchor strategy, layout-stability rules, return/restoration behavior, upstream-update policy, end/error/retry states, footer reachability, accessibility landmarks/control, and falsification scenarios.