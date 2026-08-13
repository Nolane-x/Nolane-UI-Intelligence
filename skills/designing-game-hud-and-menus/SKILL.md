---
name: designing-game-hud-and-menus
description: Use when a game needs heads-up display, combat or status signaling, controller menus, inventories, maps, settings, difficulty, tutorials, or accessibility across high-attention gameplay and pause/meta interfaces.
---

# Designing Game HUD and Menus

## Overview
Game UI spans two attention modes: moment-to-moment play where UI competes with the world, and deliberate menu/meta interaction where players can inspect and configure. Design each signal around gameplay consequence and input reality.

## Parent Contract
**Required parent:** `routing-ui-work`.

Require game genre/camera, platforms, viewing distance, controller/keyboard/touch inputs, core gameplay loop, critical player states, multiplayer context, difficulty/accessibility goals, and whether UI is diegetic, non-diegetic, or hybrid.

## Decision Model
Build a signal hierarchy: immediate threat/action, short-horizon resource/cooldown, objective/navigation, social/team state, long-horizon progression, optional flavor. The HUD should surface what changes player decisions now and allow quiet periods to breathe. Do not make every number permanently visible.

Use redundant coding for threat, team, damage, objectives, and status: shape/icon/text/audio/haptic cues where appropriate, not color alone. Consider peripheral perception during high motion. Keep crosshair, prompts, subtitles, and alerts from colliding at the visual center.

Menus need deterministic gamepad focus, fast Back behavior, persistent settings, safe application of graphics/control changes, remappable inputs where supported, and accessible narration/contrast/text options. Pause state and multiplayer constraints must be explicit: can gameplay truly pause, or must the menu protect the player another way?

Tutorials should teach in context, allow replay, and avoid trapping experienced players. Difficulty and accessibility are separate axes; do not hide captions, control remap, reduced motion, or assist features behind a difficulty label.

## Evidence
Test during actual gameplay intensity, not static menu screenshots. Verify controller/keyboard focus, screen distance, motion, color-vision alternatives, subtitle readability, remapping conflicts, repeated alerts, HUD scaling/safe area, multiplayer interruption, and accessibility settings. Use platform accessibility guidance such as XAG where applicable.

## Output Contract
Return a `game-ui-contract` with `gameplay_signal_hierarchy[]`, `hud_elements[]`, `adaptive_visibility`, `multimodal_cues[]`, `menu_focus_model`, `pause_semantics`, `settings_and_remap`, `tutorial_strategy`, `difficulty_vs_accessibility`, `multiplayer_constraints`, and `gameplay_tests[]`.

## Failure Traps
- Color-only enemy/team distinction.
- Permanent HUD clutter unrelated to current decisions.
- Tiny menu focus indicator on TV.
- Accessibility options reset per session.
- Input remap creating unreachable menu controls.
- “Pause” menu that leaves the player vulnerable without warning.
- Camera/motion effects required to understand gameplay with no alternative.

The best HUD disappears from conscious attention until the player needs the information.

## V6 Game HUD Attention Protocol
Set a **playfield occlusion budget** by gameplay mode so HUD information does not hide threats, objectives, aiming space, or cinematic cues. Map **combat-attention priority** separately from inventory/menu priority; information that matters during active play needs faster recognition and different persistence.

Support **safe-zone adaptation** for TV overscan, aspect ratios, ultrawide, handheld, split-screen, and accessibility scaling. Make a **diegetic-vs-overlay decision** per information class based on clarity, fiction, camera motion, accessibility, and failure cost—not novelty. Preserve **pause-state parity** so critical settings/help/status remain reachable even when real-time play is paused or unavailable.

### Falsification
Stress the HUD during high-action scenes, visual effects, low health, split screen, color/contrast settings, and unusual aspect ratios. Missed critical information or occluded play falsifies the hierarchy.

### Recovery
Reduce low-value HUD persistence, relocate/aggregate status, strengthen alternate cues, or move complexity to paused menus without hiding necessary live feedback.
