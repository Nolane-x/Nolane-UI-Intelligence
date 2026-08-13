---
name: designing-wearable-glanceable-interfaces
description: Use when designing smartwatch, fitness, wearable, heads-up, or tiny-body-worn interfaces where interactions last seconds, screen area is constrained, context sensing matters, and haptics or complications carry ambient state.
---

# Designing Wearable and Glanceable Interfaces

## Overview
A wearable is not a miniature phone. It should answer a small number of immediate questions or actions within seconds, preserve attention to the physical world, and hand off deep work rather than compress it.

## Parent Contract
**Required parent:** `routing-ui-work`.

Require critical wearable tasks, typical glance duration, screen shape/size, context sensors, offline expectations, haptic capability, and phone/companion handoff. If the product has no task that benefits from immediacy or body context, question whether it belongs on the wearable.

## Decision Model
Rank tasks by *time-to-value on wrist*. Prefer check, acknowledge, start/stop, quick capture, status, navigation cue, timer, alert, or small choice. Multi-paragraph reading, complex configuration, dense analysis, and long forms usually hand off to a larger device unless the domain proves otherwise.

Design the first screen as an answer, not a menu. Use clear primary state, one dominant action when appropriate, and progressive depth measured in a handful of interactions. Round displays need center-weighted legibility and safe edge placement; avoid small corner targets. Scrolling is acceptable for short lists but not a substitute for prioritization.

Context can reduce interaction, but automation must be legible. Location/activity/health context may be sensitive, stale, or wrong. Show state when it changes action behavior and provide correction. Offline behavior matters because a watch may lose phone/network connectivity.

Haptics are valuable for discreet acknowledgement, timing, navigation, and alerts, but critical meaning requires visual/audio/semantic equivalence. Notifications should be ruthlessly filtered; a wrist amplifies interruption cost.

## Evidence
Test real-device glance time, one-handed/body posture, round/tiny targets, outdoor brightness, haptics disabled, phone disconnected, stale sensor context, notification burst, accessibility scaling, and handoff continuity. Evaluate whether users can return attention to the world quickly.

## Output Contract
Return a `wearable-contract` with `critical_glance_tasks[]`, `time_to_value`, `first_screen_answer`, `interaction_depth`, `round_or_edge_geometry`, `context_rules[]`, `offline_behavior`, `haptic_mapping`, `notification_budget`, `companion_handoff`, and `wearable_tests[]`.

## Failure Traps
- Full phone dashboard shrunk onto a watch.
- Six charts where one status/action is needed.
- Tiny edge controls on a round screen.
- Every phone notification mirrored to the wrist.
- Sensor inference silently changing actions.
- Network failure producing an empty spinner.
- Haptic-only critical alerts.

The wearable earns its place when it reduces time and attention cost, not when it reproduces feature count.

## V6 Wearable Glance Protocol
Set a **glance-duration budget** for each state: what can be recognized in sub-second, one-to-two-second, and deliberate inspection windows while the user's other activity continues. Separate a **complication-information tier** for persistent ambient facts from interactive app detail; ambient presence must not pretend to support deep decision-making.

Account for **wrist-motion tolerance**: raise-to-wake, walking, exercise, one-handed posture, screen dimming, and small angular targets change both perception and touch accuracy. Define the **ambient-to-active transition** so stale summary state, privacy-sensitive content, focus, and pending actions update predictably when the screen wakes or expands. Balance a **battery-attention tradeoff** for refresh frequency, animation, always-on rendering, haptics, and sensor sampling; “live” is not free in either power or distraction.

### Falsification
Run the core task while walking, with short display-on windows, one hand occupied, delayed sensor updates, and low battery/power-saving modes. If understanding requires prolonged reading or frequent wake cycles, the wearable model is false.

### Recovery
Promote only the highest-value status/action to the glance layer, move detail to the companion/full app, reduce update/animation demand, and preserve continuity when the user resumes on another surface.
