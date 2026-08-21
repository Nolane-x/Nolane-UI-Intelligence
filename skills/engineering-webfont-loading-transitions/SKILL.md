---
name: engineering-webfont-loading-transitions
description: Use when web typography changes between unavailable, fallback, loading, and final font states and readability, layout stability, timing, and failure behavior need an explicit loading contract.
---

# Engineering Webfont Loading Transitions

## Loading Is a Visible State Machine
A webfont is not simply present or absent. The page can render before font metadata is known, show fallback glyphs, swap after first paint, time out, fail a subset, or retain a cached final face. This skill owns how those states transition without sacrificing readable content or destabilizing the interface.

## Parent Contract
**Required parent:** `crafting-typography`.

The parent chooses typographic voice, hierarchy, and broad font roles. This specialist begins when those roles depend on asynchronously available font resources whose arrival changes runtime metrics or appearance.

## State Model
Model each text role as `unrequested -> requesting -> fallback-visible -> final-visible`, with side branches for `blocked`, `failed`, and `cached-final`. Decide separately for critical reading text, display headlines, icons encoded as fonts, and optional decorative faces. The core decision is how long the UI may wait before showing readable fallback and whether a late final face may replace it after the user has begun interacting.

A swap is not free: it can move buttons, truncate labels differently, shift scroll position, or invalidate screenshots. Treat font-display policy, preload priority, subset strategy, and fallback metrics as one transition contract rather than independent performance tweaks.

## Transition Invariants
Text remains readable in every reachable state. Interactive controls do not become unreachable because labels reflow after swap. A late font does not silently change semantic emphasis. Loading policy has a bounded timeout/failure path. Critical UI never depends on font success to expose text that otherwise vanishes.

## Evidence
Evidence includes cold-cache and warm-cache runs, slow-network throttling, disabled font requests, screenshots before and after swap, layout-shift traces, and interaction during the transition. Capture resolved font-family and actual line boxes, not merely network success. Test long/localized strings because metric differences amplify under real content.

## Failure Topology
Characteristic Failure includes invisible body text during a long request, a late swap moving a confirmation control under the pointer, fallback glyphs missing symbols, preloads that compete with more critical resources, duplicate font downloads from mismatched descriptors, and cached runs masking a broken cold-start policy. Another failure is a font timeout that leaves a permanent layout different from the final design but with no evidence that the fallback is acceptable.

## Falsification
Falsification blocks the font host, adds high latency, clears cache, starts an interaction before the final face arrives, and compares geometry across states. The contract is disproved if content becomes unreadable, a task target moves materially during acquisition, or the final/fallback state cannot be identified from runtime evidence.

## Recovery
Recovery restores immediate readable fallback, fixes descriptors/preload policy, and aligns fallback metrics before optimizing swap timing. If final-font arrival remains highly disruptive, keep fallback for the session or defer the swap to a safer boundary rather than forcing visual purity during active work.

## Output and Handoff
Output: `webfont-loading-transitions-contract`, containing role-specific loading states, timeout/swap policy, preload rules, layout-stability thresholds, fallback expectations, and cold/warm evidence. Handoff exact fallback metric tuning to `engineering-font-fallback-metric-compatibility` and visual font selection to the parent.

## Sibling Boundary and delete-the-skill
Fallback-metric engineering can make two faces geometrically compatible but does not decide when either face appears or how load failure behaves. The delete-the-skill test passes because removing this owner leaves asynchronous typography transitions and their interaction hazards ungoverned.