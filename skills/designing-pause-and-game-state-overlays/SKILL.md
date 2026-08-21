---
name: designing-pause-and-game-state-overlays
description: Use when gameplay can be paused, suspended, spectated, failed, disconnected, or interrupted by system/game-state overlays and the UI must preserve input ownership, world-state truth, resume conditions, multiplayer constraints, and safe transitions back to play.
---

# Designing Pause and Game-State Overlays

## Overlay semantics depend on world state
“Pause menu” is often a misleading simplification. In single-player, opening a menu may freeze simulation. In online play, the world may continue. A disconnect overlay may suspend local input but not remote events. A failure screen may represent a terminal gameplay state with restart choices. This skill owns the relationship between overlay state and underlying game-state truth.

## Parent Contract
**Required parent:** `routing-ui-work`.

The routing parent selects this specialist when an overlay changes or explains active-play availability. Menu-stack recovery owns navigation-stack failures; gameplay/menu input handoff owns control-mode transfer. This skill owns the overlay’s game-state contract.

## Overlay classes
Classify overlays as `simulation_pausing`, `input_pausing`, `informational_nonpausing`, `blocking_recovery`, `terminal_state`, or `system_delegated`. The decision owner is which world processes continue while the overlay is active: simulation, timers, network activity, matchmaking, voice, input, achievements, recording, or resource consumption.

The visible copy must match reality. Do not say “Paused” if enemies, timers, or remote players continue. In an online game, “Menu open—game continues” may be necessary. For a system-level suspend, distinguish local application suspension from server-side match progression.

## Entry and exit contract
On overlay entry, capture gameplay input state, focus return target, active player, and any held commands that must be cleared. On exit, do not leak the menu-confirm button into gameplay actions. Define a small re-entry guard where necessary, but avoid arbitrary delays that make controls feel unresponsive.

Overlay closure may require preconditions: reconnect completed, save confirmed, respawn selected, or host decision resolved. Resume should return to a coherent camera/control state and restore HUD priority without duplicating previous inputs.

## Multiplayer and split-screen
In multiplayer, identify whether one player’s pause overlay affects everyone, only that player’s viewport, or shared match state. Shared overlays need ownership rules. A local player opening settings should not necessarily freeze or obscure another player’s critical play area. When pause is impossible, provide a safe nonpausing menu pattern and explain risk.

## Evidence
Evidence includes game-state flags before/during/after overlay, simulation/network continuity, cleared input state, focus ownership, re-entry traces, and multiplayer effects. Test pause during combat, while an input is held, during network reconnect, with multiple players, and at transitions into terminal states.

## Failure modes
Characteristic Failure includes calling a continuing online match paused, stuck movement after closing a menu, confirm-to-close immediately firing an attack, overlay state that hides critical continuing timers, one player blocking all split-screen users unexpectedly, and resume returning to stale camera or HUD state. Another failure is a failure/respawn overlay that allows underlying controls to keep mutating gameplay.

## Falsification
Open and close overlays at high input rate, disconnect/reconnect while paused, switch from pause to terminal state, and test online/nonpausing modes. The contract fails if world-state copy is false, if input leaks across the transition, if resume preconditions are bypassed, or if other players’ state is affected without defined policy.

## Recovery
When overlay/game-state diverge, privilege authoritative game state, update the overlay label/actions, clear unsafe input, and restore only controls valid for the current state. If a supposedly pausing overlay did not pause the world, surface the elapsed consequences rather than rewinding local UI fiction.

## Output and Handoff
Output: `pause-and-game-state-overlays-contract`, containing overlay classes, world-process continuity, entry/exit input rules, resume preconditions, multiplayer impact, and evidence. Handoff menu navigation stack to game-menu recovery and mode transfer to gameplay-to-menu input handoffs.

## Sibling Boundary and delete-the-skill
Sibling game HUD priority governs information during active play; this skill governs temporary/terminal overlays and their relationship to play state. The delete-the-skill test passes because without this owner, a menu overlay can visually imply suspension while the underlying game continues under completely different rules.