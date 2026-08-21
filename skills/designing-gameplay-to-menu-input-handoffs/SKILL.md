---
name: designing-gameplay-to-menu-input-handoffs
description: Use when controls transition between gameplay and menus and the interface must transfer input ownership, clear held commands, establish focus, suppress accidental activation, preserve camera/player state, and return control without leaking one mode's input semantics into the other.
---

# Designing Gameplay-to-Menu Input Handoffs

## Mode boundaries are input boundaries
The same physical button can mean attack in gameplay and confirm in a menu; an analog stick can steer a character and navigate a grid. Opening or closing a menu therefore requires an explicit transfer of input ownership. This skill owns that handoff and the conditions under which input from one mode may begin affecting the other.

## Parent Contract
**Required parent:** `routing-ui-work`.

The routing parent activates this specialist when gameplay and UI command contexts share devices. Pause/game-state overlays own whether the world continues; this skill owns the mechanics of input-context transfer.

## Handoff state
Track source input context, destination context, initiating event, held-button/axis state, destination focus target, active player/device, and guard status. The decision owner is which initiating input is consumed by the transition and which subsequent input is allowed through.

For example, pressing Menu to open an overlay should not also activate the default focused button. Closing with Confirm should not fire the gameplay action bound to the same physical control. Analog axes need neutralization policy so a stick held during closure does not instantly move the player or camera before the user recenters it.

## Entry to menu
On entry, suspend or reroute gameplay commands according to the world-state contract, clear transient held state as required, establish visible focus, and retain enough gameplay context for return. If the menu is player-scoped, bind the input context to the initiating player. Other players’ controls should remain governed by multiplayer ownership rules.

## Return to gameplay
On exit, ensure the menu is actually closed, no blocking modal remains, and the world state is resumable. Restore gameplay input only after transition input is consumed. Some devices benefit from a neutral-axis requirement; others from release-before-reactivation. Apply the least disruptive rule that prevents leakage.

## Context stacking
Nested menus and overlays create stacked input contexts. Pushing a child context should suspend its parent without reactivating gameplay underneath. Pop in reverse order and route to menu-stack recovery if the recorded parent is invalid. System overlays may temporarily supersede both gameplay and menu input without changing the product’s logical stack.

## Evidence
Evidence includes input-context transitions, raw initiating events, consumed/suppressed events, axis/button release state, focus establishment, gameplay action logs, and return timing. Test rapid open/close, held stick, held trigger, remapped controls, controller disconnect during the handoff, and nested overlays.

## Failure modes
Characteristic Failure includes opening a menu and instantly selecting an item, closing a menu and firing a weapon, character drift caused by held analog input, gameplay shortcuts activating behind a modal, focus not established before navigation events arrive, and one player’s menu stealing another player’s controls. Another failure is arbitrary long input lockout used to hide race conditions.

## Falsification
Press and hold the transition button, move sticks through the boundary, remap confirm to a gameplay action, spam open/close, and interrupt with another overlay. The contract fails if one event produces actions in both contexts, if gameplay receives input while blocked, if menu focus misses initial commands, or if recovery requires a fixed delay rather than state evidence.

## Recovery
On suspected leakage, stop processing both contexts briefly by state—not by arbitrary timer—inspect active context stack and held-input state, establish a single owner, then resume after release/neutral conditions are met. If the menu hierarchy is invalid, hand off to menu-stack recovery before re-enabling gameplay.

## Output and Handoff
Output: `gameplay-to-menu-input-handoffs-contract`, containing context stack, transition-event consumption, held-input policy, focus establishment, player/device binding, and return conditions. Handoff world pause semantics to pause/game-state overlays and invalid menu hierarchy to game-menu stack recovery.

## Sibling Boundary and delete-the-skill
Sibling pause overlays decide what the game world does while UI is visible; this skill decides what the input device does at the boundary. Directional focus graphs govern navigation after menu focus exists. The delete-the-skill test passes because without an input-handoff owner, shared bindings can trigger actions in both gameplay and menu contexts during the same transition.