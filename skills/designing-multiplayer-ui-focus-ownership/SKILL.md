---
name: designing-multiplayer-ui-focus-ownership
description: Use when multiple local players or controllers can interact with menus, lobbies, inventories, split-screen overlays, or shared dialogs and the UI must decide who owns focus, which surfaces are private or shared, and how simultaneous input is arbitrated.
---

# Designing Multiplayer UI Focus Ownership

## One screen can have more than one interaction owner
Local multiplayer interfaces break ordinary single-focus assumptions. Each player may need independent focus in a personal pane while shared dialogs require one coordinated decision. This skill owns the authority model that assigns focus and command ownership across players and shared UI regions.

## Parent Contract
**Required parent:** `routing-ui-work`.

The routing parent activates this specialist when more than one local input principal can manipulate visible UI. Directional adjacency is delegated to focus graphs; controller identity and disconnect handling remain sibling responsibilities.

## Ownership modes
Classify regions as `player_private`, `player_scoped_shared_view`, `shared_single_owner`, or `shared_multi_input`. For private regions, each player keeps an independent focus node and navigation history. For a shared single-owner dialog, only the designated principal can activate actions while others may receive a clear locked/waiting state. Shared multi-input surfaces need explicit collision rules.

The decision owner is how ownership is established and transferred: first opener, host role, turn order, explicit claim, or product-specific rule. Do not infer ownership from whichever controller event arrives first unless that behavior is intentional and visible.

## Simultaneous input arbitration
When two users send conflicting commands, the UI must not produce nondeterministic outcomes. Shared list selection, ready-state toggles, purchases, matchmaking settings, and destructive confirmations need serialized or partitioned mutation rules. Input that is rejected because another player owns the surface should receive feedback rather than disappearing silently.

## Focus presentation
Players need to distinguish their own focus from others’ focus without relying solely on color. Use labels, player glyphs, shape, position, or contextual framing. The visual system should scale beyond two players and remain legible at couch distance. Shared-focus ownership should be obvious before a user presses confirm.

## Transition cases
Ownership changes when a player joins/leaves, a controller disconnects, a private pane opens a shared dialog, or a host transfers role. Preserve per-player prior focus so closing a shared overlay returns each participant to a coherent place. If the current owner disappears, apply a deterministic successor rule.

## Evidence
Evidence includes player-controller assignments, region ownership states, simultaneous-input traces, focus return paths, owner-transfer events, and visuals proving distinguishability. Test at least two controllers pressing opposing directions/confirm simultaneously, owner disconnect during a modal, and a player joining while another is navigating.

## Failure modes
Characteristic Failure includes controller races deciding shared settings unpredictably, one player stealing another’s private focus, shared confirmation triggered by the wrong player, focus indicators distinguished only by similar colors, and owner disconnect leaving a modal permanently locked. Another failure is global focus reset when one player closes a personal pane.

## Falsification
Generate simultaneous events with reversed ordering, reassign controllers, disconnect the owner, add a new player mid-dialog, and open/close shared overlays repeatedly. The contract fails if outcome depends on event timing rather than policy, if players cannot identify their focus, if ownership becomes orphaned, or if one player’s navigation corrupts another’s local state.

## Recovery
Freeze shared mutation during ambiguous ownership, re-establish player/controller identity, select an owner by the declared transfer rule, and restore private focus histories. If conflicting mutations already occurred, reconcile the shared state and show the resolved result to all affected players rather than silently favoring the latest input.

## Output and Handoff
Output: `multiplayer-ui-focus-ownership-contract`, containing region ownership classes, principal assignment, simultaneous-input arbitration, focus presentation, transfer rules, and evidence. Handoff player-device loss to controller-disconnect recovery and spatial adjacency within each owned region to directional focus graphs.

## Sibling Boundary and delete-the-skill
Sibling split-screen safe-region design owns geometry, not interaction authority. Controller remapping owns bindings per player/device. The delete-the-skill test passes because without explicit multiplayer focus ownership, shared UI behavior is governed by event timing and a single-focus assumption that cannot represent several simultaneous principals.