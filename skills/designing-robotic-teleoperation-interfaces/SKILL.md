---
name: designing-robotic-teleoperation-interfaces
description: Use when humans supervise, command, teleoperate, hand off to, or recover robots, drones, remote vehicles, manipulators, autonomous machines, or other physically embodied systems where latency, world state, autonomy, and physical consequence matter.
---

# Designing Robotic and Teleoperation Interfaces

## Overview
A robotic UI couples screen actions to a changing physical world. Preserve situational awareness, command authority, timing, robot capability, environmental constraints, and safe recovery when sensing or communication is incomplete.

## Parent Contract
**Required parent:** `routing-ui-work`.

Require robot/vehicle capabilities, autonomy levels, physical environment, sensor feeds, latency/jitter, command channel, safety envelope, operator expertise, number of robots, and consequences of wrong or delayed action. Material physical-risk work routes through human factors and independent safety critique.

## Decision Model
Model three states at once: **world state**, **robot believed state**, and **operator interface state**. They can diverge because sensors are stale, video is delayed, localization drifts, commands are queued, or autonomy continues after connectivity loss. Expose freshness and uncertainty where it affects control rather than presenting every telemetry field equally.

Separate command modes: direct teleoperation, waypoint/task command, shared control, supervised autonomy, and emergency/safe-state control. Make current authority unmistakable. A joystick should not appear to control a robot that is actually executing an autonomous plan or has lost communication. Transitions between manual and autonomy require explicit handoff state and confirmation proportional to consequence.

Design navigation around situational awareness: camera perspective and field of view, map/localization, robot pose, obstacles, target/task, communication state, energy, safety zones, and command history. Support viewpoint switching without hiding frame/reference changes. Multi-robot operations need selection identity and prevention of wrong-robot command.

Latency changes control strategy. High or variable delay may require predictive visualization, queued command visibility, rate limits, or higher-level commands instead of direct continuous control. Emergency stop semantics must reflect whether the stop channel is truly independent/reliable.

## Evidence
Use hardware/simulator-in-loop tests, realistic latency/loss, stale sensors, occlusion, localization error, wrong-robot selection, autonomy handoff, operator workload, emergency state, multi-robot supervision, and domain-expert scenarios. A smooth prerecorded video feed is not teleoperation evidence.

## Output Contract
Return a `robotic-teleoperation-contract` with `world_robot_ui_state_model`, `control_modes[]`, `authority_handoff`, `situational_awareness_views[]`, `sensor_freshness_rules`, `latency_strategy`, `command_queue_semantics`, `multi_robot_identity`, `safe_state_and_emergency`, `physical_risk_constraints[]`, and `robotic_tests[]`.

## Failure Traps
- Video appears live when it is several seconds stale.
- Operator sends a command to the wrong selected robot.
- Manual controls remain active visually during autonomous execution.
- Communication loss leaves last control input latched without clear safe behavior.
- Camera perspective changes but reference frame is not obvious.
- “Emergency stop” button is cosmetic or shares the failed command path.
- Desktop usability test used as proof of physical operational safety.

Robotic UI is trustworthy when the operator knows what the machine knows, what it is doing, and which actions can still change the physical outcome.