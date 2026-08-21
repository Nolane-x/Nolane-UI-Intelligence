---
name: designing-split-screen-safe-interface-regions
description: Use when multiple local players share one display and each viewport needs safe HUD, menu, notification, subtitle, and focus regions that remain legible across horizontal/vertical splits, aspect changes, shared overlays, and platform safe-area constraints.
---

# Designing Split-Screen Safe Interface Regions

## Shared display geometry is not ordinary responsive layout
Split-screen creates several simultaneous viewports plus shared screen-level regions. A layout that works in one full-screen viewport can become unreadable, overlap gameplay, or place critical controls across split boundaries. This skill owns the geometry contract for player-local and shared interface regions.

## Parent Contract
**Required parent:** `routing-ui-work`.

The routing parent activates this specialist when multiple local players share one physical display. Responsive composition may provide general layout primitives, but this skill owns multi-viewport safe regions and shared-screen collision rules.

## Region model
Represent player viewports, per-player safe insets, shared global overlay region, subtitle/caption region, platform safe area, and reserved system UI. The decision owner is where each information class belongs: player-local HUD, player-local notifications, shared match state, shared confirmation, or global system message.

Do not simply scale full-screen HUDs into smaller rectangles. Reprioritize information for the reduced viewport. Player-local content should never leak into another player’s region unless intentionally shared, and global overlays should avoid covering all players’ critical world view when a smaller shared region can work.

## Split modes and aspect pressure
Horizontal and vertical splits create different aspect ratios and failure modes. Four-way layouts create extreme small viewports. Define layout modes by actual per-player geometry, not player count alone. Test safe areas after letterboxing, overscan, dynamic resolution, and aspect-ratio changes.

Shared UI may span the screen only when interaction ownership is clear. If one player opens a private inventory, it should not necessarily steal display space from others. If a match-wide dialog must block everyone, communicate shared ownership and preserve each player’s focus for restoration.

## Text, captions, and notifications
Captions can be global or player-associated depending on audio design. Ensure they do not collide with player HUDs or split separators. Notifications need scope: a player-two pickup should appear in player two’s region, while a server disconnect may be global. Avoid tiny duplicated global messages in every viewport when one shared message is clearer.

## Evidence
Evidence includes layouts for each supported split mode, per-player safe-area overlays, dense HUD states, captions, global/local notifications, focus markers, and transitions when players join or leave. Test on actual target aspect ratios and couch-distance displays, not only editor previews.

## Failure modes
Characteristic Failure includes full-screen HUD scaled until unreadable, player-one notifications covering player-two world view, subtitles clipped by split boundaries, global dialogs obscuring critical content unnecessarily, safe areas computed from full screen instead of player viewport, and focus indicators appearing in the wrong pane. Another failure is geometry reset when player count changes.

## Falsification
Switch between one/two/three/four players, alternate horizontal and vertical split, activate captions and high-notification load, open a shared modal, and resize/aspect-change the display. The contract fails if critical elements overlap, cross player boundaries, become unreadable, or lose ownership during split-mode transitions.

## Recovery
Recompute region ownership from current viewport geometry, reduce local information density before shrinking type below legible limits, and relocate global elements to dedicated shared regions. Preserve player-local state while the split configuration changes. If a feature cannot fit safely in a supported split mode, provide a different interaction surface rather than clipping it.

## Output and Handoff
Output: `split-screen-safe-interface-regions-contract`, containing viewport regions, safe insets, local/global information placement, split modes, captions/notifications, transition rules, and evidence. Handoff interaction authority to multiplayer focus ownership and content priority to HUD/ten-foot specialists.

## Sibling Boundary and delete-the-skill
Sibling multiplayer focus ownership governs who can act; this skill governs where each player’s UI can safely appear. Responsive regression verifies geometric transitions generally, but not multi-player region ownership. The delete-the-skill test passes because without a split-screen geometry owner, teams tend to shrink single-player UI until it technically fits while sacrificing ownership, readability, and world visibility.