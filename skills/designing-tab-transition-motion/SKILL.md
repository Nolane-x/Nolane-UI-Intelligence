---
name: designing-tab-transition-motion
description: Use when switching among peer tab panels needs continuity that preserves selected-tab truth, reading position and fast keyboard traversal without misrepresenting tabs as a carousel or navigation stack.
---

# Designing Tab Transition Motion

## Parent Contract
**Required parent:** `designing-motion`.

This faculty owns the temporal relation between peer tab panels. Tab semantics, activation mode and keyboard behavior remain with interaction/accessibility owners.

## Decision Model
Tabs express **peer views within one context**. Motion should reinforce that relationship. Directional sliding is appropriate only when the tab order genuinely maps to a spatial sequence; otherwise it can falsely imply back/forward navigation. A short crossfade, content-specific continuity, or no motion may be clearer.

Distinguish automatic activation from manual activation. In automatic tabs, arrow-key traversal can change panels rapidly; expensive transitions must not queue or make focus outrun the visible panel. In manual activation, focus may move across tab labels while the selected panel remains unchanged—do not animate panel content until selection actually changes.

Preserve panel-specific state intentionally. Scroll position, form edits, media playback and virtualized list position may need to persist. Motion must not remount content merely to replay an entrance. If loading is required, transition selected state immediately and hand off to a loading contract rather than leaving the old panel visually selected.

Use shared indicators carefully. An animated underline can clarify selected-tab movement, but it must end at the actual selected tab and remain legible under overflow/scrolling tab lists.

## Failure Topology
- Arrowing through tabs queues five slides that continue after the user stops.
- Directional motion implies a sequence that the information architecture does not have.
- Panel transition remounts forms and loses unsaved input.
- Focus is on one tab while the animated indicator still points to another.
- Loading leaves the previous content visible with the new tab marked selected, creating mixed truth.

## Falsification
Hold arrow navigation, switch nonadjacent tabs, activate a loading panel, resize/overflow the tab strip, preserve form/scroll state, and test reduced motion. Sample the UI mid-transition: selected semantics, indicator and visible content must not contradict each other materially.

## Recovery
Cancel stale transitions on new selection, reduce animation to a local selected indicator, preserve panel state independently of animation lifecycle, and avoid directional travel when hierarchy does not support it.

## Output Contract
Return `tab-transition-motion-contract` containing activation mode, panel transition type, cancellation/retargeting rules, state-persistence policy, loading handoff, indicator motion, overflow behavior and reduced-motion equivalent.