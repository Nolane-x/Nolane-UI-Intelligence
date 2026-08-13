---
name: designing-automotive-interfaces
description: Use when an interface is used in a vehicle, especially while driving, parked, or transitioning between those states, and glanceability, distraction, task length, voice, hardware controls, or driving safety constrains interaction.
---

# Designing Automotive Interfaces

## Overview
In-vehicle UI is governed by attention to driving before feature completeness. Separate driving and parked capability, minimize eyes-off-road and manual demand, and use platform templates/voice/hardware where they reduce distraction.

## Parent Contract
**Required parent:** `routing-ui-work`.

Require driving versus parked context, supported vehicle/platform, input hardware, display location, passenger role, task criticality, network dependence, and applicable automotive UX requirements. Mandatory companion skills include `engineering-human-factors`; material driver-facing release requires `critiquing-human-factors-and-safety`.

## Decision Model
Classify every task as allowed while driving, restricted/simplified while driving, passenger-only where detectable, or parked-only. Do not rely on a warning label to make a long visual-manual task safe. Reduce step count, visual search, text entry, decision complexity, and interaction duration for driving contexts.

Design for glanceability. Put primary state and next action in stable locations; avoid dense scrolling, tiny text, ambiguous icons, long text blocks, and frequent layout shifts. Voice can reduce manual interaction but introduces recognition/ambiguity risk; use concise prompts and risk-proportional confirmation. Physical controls and steering-wheel inputs may provide safer operation for frequent actions.

Model interruptions and state transitions. Driving conditions can change mid-task; the UI must pause, simplify, defer, or preserve state when an action becomes unavailable. Notifications need strict urgency and batching. Navigation, communication, and media tasks should not compete equally for attention.

Separate driver and passenger privacy/authority. A center display shared by occupants may expose messages or credentials. Passenger-oriented rich interaction must not accidentally become driver-operable if platform safety rules restrict it.

## Evidence
Use current platform car quality/UX requirements, human-factors analysis, driving-context scenario tests, voice failure tests, hardware input, glance/step measurements where required, and parked/driving transition tests. Do not claim automotive safety from desktop usability testing.

## Output Contract
Return an `automotive-contract` with `context_classes`, `task_availability[]`, `driving_constraints[]`, `glance_model`, `manual_step_budget`, `voice_model`, `hardware_controls`, `notification_policy`, `context_transition_rules`, `passenger_privacy`, `deferred_tasks[]`, and `automotive_validation[]`.

## Failure Traps
- Long destination form enabled while moving because the font is large.
- Generic “do not use while driving” warning used as risk control.
- Voice executing ambiguous consequential commands.
- Layout reflow during driving that moves familiar controls.
- Promotional or low-value notifications competing with navigation/safety signals.
- Parked-only task losing all progress when the vehicle moves.
- Applying a car-platform step limit as a universal mobile rule.

Automotive UI quality is measured partly by what it refuses or defers while the person is driving.

## V6 Automotive Attention Protocol
Set a **glance-time envelope** per driving-state task; driving-critical information must be perceivable with minimal eyes-off-road demand. Apply **driving-state lockout** to interactions whose visual/manual demand exceeds safe conditions, with passenger/parked alternatives where allowed.

Enforce **road-attention priority** over notifications, entertainment, animation, and nonessential personalization. Maintain **vehicle-control distinction** between infotainment, climate/convenience, driver-assistance, and safety-critical vehicle controls; visual similarity must not blur authority or consequence. Model **passenger-driver context** so features available to passengers do not accidentally appear actionable to the driver.

### Falsification
Run tasks under motion, vibration, bright/dark transitions, voice failure, alerts, and driver-assistance state changes. If the driver must visually troubleshoot or infer control authority, design is unsafe.

### Recovery
Defer/lock interactions, move appropriate tasks to voice/steering controls, simplify glanceable state, and require parked/passenger continuation for high-demand work.
