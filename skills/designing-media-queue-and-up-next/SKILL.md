---
name: designing-media-queue-and-up-next
description: Use when playback can continue across multiple items and the product must expose queue order, auto-advance, manual edits, recommendations, repeat/shuffle, and the boundary between user intent and algorithmic continuation.
---

# Designing Media Queue and Up Next

## Parent Contract
**Required parent:** `designing-media-playback-experiences`.

This faculty owns ordered future playback. It does not own catalog recommendation algorithms. It decides how explicit queue entries, contextual next items, autoplay recommendations, repeat/shuffle, and current item interact without hiding why something will play next.

## Decision Boundary
Model sources of queue intent separately: user-added, playlist/order, series progression, host-controlled session, and algorithmic autoplay. Establish precedence. If users add an item manually, it should not be silently displaced by a recommendation. Make the immediate next item visible before automatic transition when surprise or data use matters. Define whether clearing the queue disables autoplay or merely removes explicit items.

Queue edits need stable identity while playback advances. Moving, removing, or adding items should not accidentally restart current playback. Repeat-one, repeat-all, shuffle, and autoplay are orthogonal states in some products; do not encode them as one ambiguous cycle button unless users can identify the active policy.

## Failure Topology
- Algorithmic recommendation jumps ahead of an item the user explicitly queued.
- Removing current item stops playback immediately when user expected only future removal.
- Queue reorder loses track identity after duplicate items appear.
- Shuffle icon looks active but queue preview remains in original deterministic order with no explanation.
- Clearing queue unexpectedly continues endless autoplay.
- Cross-device playback reconstructs a different queue because only current item was synchronized.

## Falsification and Recovery
Test explicit add/remove/reorder, duplicate items, item end, manual skip, repeat modes, shuffle, autoplay on/off, clearing, app restart, and remote playback. The design fails if users cannot answer “what will play next and why?” or if algorithmic continuation overrides stronger user intent silently.

Recover by separating queue sources and precedence, exposing up-next rationale, using stable item-instance IDs, and representing repeat/shuffle/autoplay as explicit state. Synchronize queue when distributed sessions promise continuity.

## Output Contract
Return `media-queue-contract` with queue sources/precedence, item identity, edit behavior, auto-advance, up-next disclosure, repeat/shuffle/autoplay states, persistence/sync scope, and queue verification scenarios.
