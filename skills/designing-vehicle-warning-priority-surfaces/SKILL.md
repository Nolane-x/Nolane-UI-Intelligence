---
name: designing-vehicle-warning-priority-surfaces
description: Use when an automotive interface must present simultaneous warnings, faults, advisories, confirmations, and status changes with different urgency and required driver response without allowing routine notifications to obscure time-critical vehicle information.
---

# Designing Vehicle Warning Priority Surfaces

## Warning priority is a hazard-routing problem
Vehicles can produce several events at once: safety-critical warnings, degraded-system notices, navigation prompts, comfort messages, maintenance reminders, and communication notifications. This skill owns the priority model that decides what interrupts, what persists, what is queued, and what can be summarized so the driver receives the right information at the right time.

## Parent Contract
**Required parent:** `designing-high-stakes-decisions`.

The parent establishes conservative, evidence-based behavior for high-stakes decisions. This specialist begins when multiple vehicle/system messages compete for limited driver attention.

## Priority classes
Define classes from consequence and response time, not visual styling. A useful model distinguishes `immediate_action`, `prompt_attention`, `degraded_operation`, `advisory`, and `informational`. Map actual OEM/regulatory categories to these classes rather than inventing incompatible semantics. The decision owner is conflict resolution when several classes are active.

High-priority warnings may preempt lower-priority content, but preemption should not permanently lose information. Lower-priority messages can queue, collapse into a summary, or remain available in a message center. Repeated warnings need suppression/hysteresis only when it does not hide a new escalation or state change.

## Multimodal signaling
Critical warnings may combine visual, auditory, and haptic channels. Do not rely on color alone, and do not use the strongest cue for routine notifications. Audio intensity, repetition, iconography, placement, and persistence should align with urgency and required response. If a modality fails or is unavailable, define a safe fallback path.

## Source authority and freshness
Bind warning state to authoritative vehicle signals and fault lifecycle. A warning should clear only when the source clears or the governing specification allows acknowledgement-based dismissal. Acknowledging that the driver saw a warning is not equivalent to resolving the underlying condition.

## Interaction rules
If the driver can expand details, the summary still needs enough actionable meaning before interaction. High-demand reading should not be required for immediate hazards. A lower-priority notification should never capture focus over an active critical warning. Passenger interactions may continue where safe, but shared display arbitration must preserve critical driver information.

## Evidence
Evidence includes warning source, priority classification, timing, simultaneous-message arbitration, presentation channels, acknowledgement behavior, clear conditions, and degraded-modality tests. Capture scenarios with multiple concurrent warnings and transitions from advisory to urgent states. Normative/OEM source versions should be part of the evidence packet.

## Failure modes
Characteristic Failure includes routine notifications covering critical warnings, identical styling for unrelated urgency levels, warnings disappearing on acknowledgement while the condition remains, alert fatigue from repeating unchanged faults, color-only severity, and queued urgent warnings waiting behind older low-priority messages.

## Falsification
Inject several warnings in different orders, escalate one existing condition, fail an audio/haptic channel, acknowledge without clearing the fault, and activate unrelated infotainment notifications. The contract fails if event ordering changes priority, if a critical warning becomes hidden, if acknowledgement falsifies condition status, or if required meaning depends on one failed modality.

## Recovery
When priority conflicts or source disagreement occurs, preserve the highest authoritative hazard state, suppress only demonstrably lower-priority competition, and record the conflict. Reconcile warning source state before clearing. If the taxonomy itself is ambiguous, block local invention and escalate to the governing vehicle/safety specification.

## Output and Handoff
Output: `vehicle-warning-priority-surfaces-contract`, containing priority classes, source authority, conflict arbitration, multimodal signaling, acknowledgement/clear semantics, and evidence. Handoff cluster placement to instrument-cluster information priority and overall density to distraction-aware information density.

## Sibling Boundary and delete-the-skill
Sibling instrument-cluster priority governs the complete information hierarchy of the cluster; this skill specifically owns competing warning urgency and interruption. The delete-the-skill test passes because without a warning-priority owner, alert ordering tends to follow arrival time or visual component conventions rather than hazard consequence.