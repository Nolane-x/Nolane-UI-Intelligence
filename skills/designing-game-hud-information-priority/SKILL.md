---
name: designing-game-hud-information-priority
description: Use when an active gameplay HUD must decide which status, threat, objective, resource, party, cooldown, navigation, and system information stays persistently visible versus appearing contextually so the UI supports play without consuming attention needed for the game world.
---

# Designing Game HUD Information Priority

## HUD space competes with gameplay attention
A HUD is not a dashboard layered over a game. Every persistent element consumes visual attention that may be needed for aiming, movement, threat detection, spatial understanding, or cinematic composition. This skill owns the priority model that decides what information is persistent, contextual, glanceable, alert-driven, or deferred to menus.

## Parent Contract
**Required parent:** `routing-ui-work`.

The routing parent selects this specialist when active-play information architecture is the problem. Ten-foot density contributes legibility constraints, while pause/menu overlays and split-screen safety own different contexts.

## Information classes
Classify information by decision latency and consequence. `continuous-critical` data may include health or vehicle status; `event-critical` data appears around a threat or state change; `task-relevant` data supports the current objective; `contextual` data appears when interacting with a target; `reference` data can live in a menu. The decision owner is the minimal persistent set that still supports timely player decisions.

Avoid equating importance with permanent visibility. A high-consequence warning may be best delivered as a strong transient cue plus persistent degraded-state indicator, while an always-on panel can habituate the player and hide the world. Consider auditory and haptic channels when appropriate, but never require one modality exclusively for critical meaning.

## Priority under pressure
HUD priority should adapt to combat, traversal, conversation, inventory, spectating, or other play modes without causing the layout to churn unpredictably. Define which elements are suppressed, promoted, or relocated per mode. Preserve spatial anchors for recurring information so players do not have to relearn where to look during the most demanding moments.

## Status hierarchy
Differentiate normal status, actionable warning, urgent threat, and terminal/critical condition with more than color. Establish conflict rules when several alerts compete. A low-priority objective update should not cover an immediate damage warning; multiple urgent alerts need grouping or sequencing that preserves the most time-sensitive action.

## Evidence
Evidence includes gameplay-state captures, attention-critical scenarios, alert collisions, contextual HUD transitions, legibility at target distance, and user/task traces showing whether critical cues are noticed in time. Evaluate representative action, not only static mockups. Record mode/state that caused each HUD configuration.

## Failure modes
Characteristic Failure includes always-on telemetry with no decision value, critical alerts hidden among routine notifications, HUD panels obscuring enemies or navigation, mode changes moving familiar information constantly, and cooldown/resource indicators too subtle to scan under pressure. Another failure is over-minimalism that removes information players need to make informed decisions.

## Falsification
Trigger several alerts simultaneously, enter dense combat, switch modes quickly, reduce health/resources to critical thresholds, and test with color-vision variation plus reduced audio. The contract fails if critical information is missed, if notification competition inverts priority, if spatial anchors become unstable, or if essential state depends on one sensory channel.

## Recovery
Reconstruct the decision-latency map, remove persistent items with weak action value, promote genuinely time-critical signals, and stabilize recurring anchors. If several elements remain equally urgent, redesign the underlying information grouping rather than increasing visual intensity everywhere.

## Output and Handoff
Output: `game-hud-information-priority-contract`, containing information classes, persistence policy, mode transitions, alert conflict rules, multimodal cues, spatial anchors, and evidence. Handoff room-distance readability to ten-foot density and overlay interruption to pause/game-state overlays.

## Sibling Boundary and delete-the-skill
Sibling instrument-cluster priority serves automotive driving constraints, not game-world attention. Ten-foot density addresses readability across menu surfaces, whereas this skill owns active-play prioritization. The delete-the-skill test passes because without a HUD priority owner, interfaces either drown gameplay in telemetry or omit time-critical state based on aesthetic preference rather than decision needs.