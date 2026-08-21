---
name: designing-game-menu-stack-recovery
description: Use when nested game menus, overlays, settings, inventories, dialogs, or platform interruptions can leave navigation history corrupted and the UI needs a deterministic way to reconstruct a valid stack, restore focus, and preserve unsaved state without trapping the player.
---

# Designing Game Menu Stack Recovery

## Menu stacks are persistent navigation state
Game interfaces often layer pause menus, inventories, subpages, modal dialogs, platform overlays, reconnect prompts, and settings. If one layer disappears unexpectedly or a route becomes invalid, Back can strand the user, reopen stale dialogs, or discard edits. This skill owns recovery of the menu navigation stack when its recorded hierarchy no longer matches valid UI state.

## Parent Contract
**Required parent:** `routing-ui-work`.

The routing parent selects this specialist for menu-stack integrity problems. Remote-control navigation defines normal Back semantics; pause/game-state overlays define the world-state relationship. This skill owns exceptional reconstruction after stack corruption or invalidation.

## Stack frame model
Each frame should carry route/surface identity, parent relation, focus return identity, owning player, unsaved-data state, modal/blocking semantics, and validity predicate. The decision owner is whether a frame can still exist given current game state. A store page may become invalid after sign-out; a lobby member detail may disappear when the player leaves; a reconnect modal may be superseded by match termination.

Do not recover by popping blindly until something renders. Validate frames from the top downward and preserve the nearest coherent ancestor. If unsaved edits belong to an invalidated frame, route them through explicit discard/save/recovery policy rather than losing them silently.

## Focus restoration
Every pushed frame should define where focus returns when popped. If that target disappears, resolve a semantic sibling/parent fallback. Preserve rail/grid memory where useful. Recovery should never land focus behind a still-active modal or on an invisible element left from the previous stack.

## External interruptions
Platform dialogs, account changes, controller reconnection, DLC/content availability changes, and network transitions may invalidate several frames at once. Record them as external stack events rather than pretending the user navigated back manually. On resume, reconstruct against current authoritative game state before restoring the top frame.

## Evidence
Evidence includes stack snapshots before/after pushes and pops, invalidation events, focus return identities, unsaved-state handling, player ownership, and reconstructed stack. Test deep nesting, removal of a middle frame, external overlay interruption, sign-out, content disappearing, and repeated Back during asynchronous closure.

## Failure modes
Characteristic Failure includes Back reopening a stale modal, blank screens after a route vanishes, focus returning behind an overlay, unsaved settings silently discarded, duplicate frames after rapid open/close, and a player-private menu recovered under the wrong player. Another failure is stack repair that returns to gameplay even though a blocking recovery condition still exists.

## Falsification
Invalidate the current frame and its parent, remove the prior focus target, interrupt with a platform overlay, and trigger async route closure while Back is pressed repeatedly. The contract fails if recovery reaches an invalid frame, loses unsaved state without policy, traps navigation, or restores focus to hidden/unowned content.

## Recovery algorithm
Freeze new navigation mutations, validate frames against current state, preserve the deepest coherent prefix, resolve or archive invalid frame data, rebuild focus targets, then resume navigation. If no safe frame remains, route to a known root surface appropriate to the current game state—not unconditionally to gameplay.

## Output and Handoff
Output: `game-menu-stack-recovery-contract`, containing frame schema, validity predicates, unsaved-state policy, reconstruction algorithm, focus restoration, external interruption handling, and evidence. Handoff normal Back command semantics to remote navigation and world-state blocking to pause/game-state overlays.

## Sibling Boundary and delete-the-skill
Sibling gameplay-to-menu handoff governs normal transitions between play and menu input. This skill governs abnormal or stale navigation-stack state. The delete-the-skill test passes because ordinary routing and Back semantics cannot repair a stack whose frames are no longer valid in the current game state.