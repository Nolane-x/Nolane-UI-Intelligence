---
name: designing-controller-disconnect-recovery
description: Use when a gamepad, remote, or other primary controller can disconnect during navigation or gameplay and the UI must preserve focus, pause or protect unsafe actions, identify the missing device, and recover cleanly when control returns.
---

# Designing Controller Disconnect Recovery

## Disconnect is an interaction-state failure
A controller disappearing mid-action can strand focus, leave a held input logically active, or let gameplay continue while the user has no control. This skill owns the UI state transition from connected control to degraded/no-control state and back. The decision is not simply whether to show a toast; it is what the product must suspend, preserve, and restore.

## Parent Contract
**Required parent:** `routing-ui-work`.

The routing parent selects this specialist for controller-dependent surfaces. Focus topology, remapping, and prompt identity are neighboring concerns; this skill owns loss and restoration of the active control channel.

## Disconnect state model
Track active device identity, assigned player, last confirmed focus/action state, pressed-button state, gameplay/menu mode, replacement devices available, and recovery status. On disconnect, clear synthetic held-input state so a missing controller cannot leave a menu scrolling or character moving indefinitely.

The decision owner is whether the application should pause, continue, or degrade. Single-player gameplay may pause automatically; online multiplayer may be unable to pause and instead needs a protected reconnect overlay. A noncritical TV browsing screen may continue while accepting another remote. Apply domain rules rather than one universal behavior.

## Player and device identity
In multiplayer, reconnect must bind the correct device to the correct player. Avoid “any button reconnects player one” when multiple users are active. If a replacement controller takes ownership, show that assignment and preserve per-player focus/UI state where possible.

When a device reconnects, do not immediately execute the button that caused reconnection as a destructive UI action unless the platform convention clearly requires it. Treat reconnect input separately from subsequent activation.

## Focus and task continuity
Preserve the logical focus target, pending settings edits, modal state, and unsaved menu changes. If the focused control no longer exists by the time reconnection occurs, choose a semantic fallback and explain only when necessary. Gameplay overlays should return to the prior state without introducing accidental menu activation from stale button presses.

## Evidence
Evidence includes device-connect/disconnect events, active-player mappings, last focus identity, pause/degrade decisions, held-input clearing, reconnect input handling, and restored state. Test disconnect during navigation, while a button is held, during an irreversible confirmation, and with multiple controllers assigned.

## Failure modes
Characteristic Failure includes endless scrolling after a held stick disconnects, gameplay continuing during single-player loss of control, reconnect input confirming a destructive dialog, assigning the replacement controller to the wrong player, resetting focus to the top of a long menu, and showing a generic “controller disconnected” message with no path to recover.

## Falsification
Disconnect during every high-risk phase, reconnect a different device, reconnect while another player is active, and send noisy duplicate connection events. The contract fails if input state remains stuck, ownership becomes ambiguous, recovery repeats an action, or the user cannot regain control without restarting the task.

## Recovery
Clear active input state, preserve UI/task checkpoint, establish device/player identity, then restore focus and control only after connection is stable. If a pending action’s preconditions changed while control was absent, require revalidation rather than resuming blindly. If player assignment cannot be determined, block ambiguous input and ask for explicit association.

## Output and Handoff
Output: `controller-disconnect-recovery-contract`, containing disconnect state, pause/degrade rules, player identity, held-input clearing, focus preservation, reconnect filtering, and evidence. Handoff displayed button identity to input-device prompt switching and user mapping choices to controller remapping surfaces.

## Sibling Boundary and delete-the-skill
Sibling gameplay-to-menu handoff owns intentional mode transitions; this skill owns unplanned loss of the control channel. Directional focus graphs own where focus can move while input exists. The delete-the-skill test passes because without a disconnect owner, controller loss produces stranded or unsafe intermediate states that ordinary navigation rules cannot repair.