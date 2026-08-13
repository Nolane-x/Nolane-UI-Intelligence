---
name: designing-ambient-context-aware-interfaces
description: Use when smart environments, buildings, homes, appliances, context-aware software, adaptive interfaces, sensors, or ambient intelligence infer state and change behavior without continuous foreground interaction.
---

# Designing Ambient and Context-Aware Interfaces

## Overview
Ambient systems often act when no screen is open. Design discoverability, context provenance, predictability, override, privacy, and conflict so automation remains understandable even when interaction is distributed across devices and time.

## Parent Contract
**Required parent:** `routing-ui-work`.

Require sensed context, actuators/actions, spaces/devices, users/roles, automation rules or models, privacy boundaries, failure/safety consequences, notification channels, and manual controls. AI-driven adaptation also routes through human-AI trust and agency review.

## Decision Model
Define a context model with source, confidence, freshness, ownership, and failure modes. Location, occupancy, activity, identity, mood, environment, and device state are inferences, not facts merely because a sensor produced them. Use context only when the benefit justifies collection and the system can recover from being wrong.

Make automation legible at the right moment. Users need to understand *what changed, why, and how to override* without receiving a notification for every background action. Persistent state surfaces, subtle local indicators, history, or explain-on-demand may be more appropriate than interruptive prompts. Consequential or surprising changes need stronger notice or preauthorization.

Manual override must remain meaningful. If a user turns off a light, thermostat rule, privacy sensor, or adaptive UI behavior, the automation should not immediately fight the person unless a safety policy explicitly governs that conflict. Define override duration and priority among multiple users, schedules, AI policies, and physical controls.

Multi-system conflict is first-class: two automations can issue contradictory actions or oscillate. Establish precedence, cooldown, ownership, and conflict visibility. Shared spaces complicate consent; one resident’s personalization or sensor permission may affect others.

## Evidence
Test incorrect/stale context, sensor failure, multiple occupants, guest/shared-space privacy, simultaneous automations, manual override, offline hub/cloud loss, physical control versus app state, daylight/timezone changes, and history/recovery. Verify actual device effects, not only app representation.

## Output Contract
Return an `ambient-context-contract` with `context_sources[]`, `inference_uncertainty`, `automation_rules_or_policies[]`, `foreground_explanations`, `background_feedback`, `override_model`, `multi_user_priority`, `multi_system_conflict`, `privacy_boundaries[]`, `failure_safe_behavior`, and `ambient_tests[]`.

## Failure Traps
- Sensor inference treated as certain identity or intent.
- Automation silently changes a high-impact setting.
- Manual override immediately reversed by background policy.
- Every ambient change sends a push notification.
- Two automations oscillate with no conflict arbitration.
- Shared-space sensing consent assumed from the device owner alone.
- Screen UI says a physical state changed when the actuator actually failed.

Ambient intelligence succeeds when users can benefit from less interaction without losing comprehension or control.

## V6 Ambient Context Protocol
Attach **context-signal confidence** to location, presence, time, device proximity, activity, sensor, or inferred environment inputs. Set an **ambient privacy perimeter** describing what may be shown/heard when bystanders can perceive the surface.

Use **context-change hysteresis** to prevent UI/actions oscillating when signals fluctuate near a boundary. Define a **background-action ceiling** for what may happen without foreground confirmation; contextual inference cannot silently authorize high-consequence actions. Always provide a **foreground override path** to inspect, correct, pause, or disable adaptation.

### Falsification
Feed noisy/contradictory sensors, move rapidly across context boundaries, and introduce bystanders. If sensitive content leaks or behavior flips repeatedly, the design is false.

### Recovery
Fall back to a conservative stable context, stop background actions, request explicit confirmation, and let the user correct/disable the inferred context.
