---
name: designing-flight-deck-interfaces
description: Use when controls, displays, alerts, automation, procedures, or interactive equipment are intended for pilots or flightcrew in an aircraft flight deck or closely coupled certified flight-operations environment.
---

# Designing Flight Deck Interfaces

## Overview
A flight-deck interface is a safety-critical crew-system coordination surface, not an ordinary dashboard with stricter colors. Meaning depends on phase of flight, aircraft state, crew role, automation mode, alert priority, procedure, workload, and what action remains possible under abnormal conditions. The design must help trained operators form an accurate model of what the aircraft is doing, what automation is doing, what changed, what requires attention, and what action will follow from a control input. A visually legible display that creates mode confusion or hides a design-related flightcrew error is not acceptable.

## Parent Contract
**Required parent:** `routing-ui-work`.

Consume the aircraft/system function, pilot and crew roles, phases of flight, operational environment, control authority, automation levels, alerting scheme, failure conditions, applicable certification basis, task analysis, training assumptions, and evidence capabilities. Flight-deck work automatically requires `engineering-human-factors`, `designing-high-stakes-decisions`, and `critiquing-human-factors-and-safety`. If the task is not tied to a real certification/operational context, preserve the boundary and do not claim aviation compliance.

## Decision Model
### 1. Model phase, state, and crew role
Map functions across preflight, taxi, takeoff, climb, cruise, descent, approach, landing, go-around, shutdown, and applicable abnormal/emergency states. Record which crew member observes, commands, cross-checks, or confirms each critical operation. A control that is benign in cruise can be high workload or unavailable during another phase.

### 2. Make automation mode and authority observable
Define active mode, armed/pending mode, target, source of target, transition trigger, and what the system will do next. Changes in automation authority or mode must be timely and perceivable without requiring pilots to infer them from downstream aircraft behavior. Avoid hidden coupling where one control silently changes several automation assumptions.

### 3. Integrate controls and displays around task consequences
For each control, specify manipulated object, current state, allowed action, feedback, resulting state, reversibility, and failure response. Physical knobs, switches, cursor controls, touch surfaces, and multifunction controls require appropriate motor/visual evidence rather than a generic touchscreen pattern. Accidental activation and inadvertent mode changes need prevention proportional to consequence.

### 4. Treat alerts as an operator-response system
Alerts must indicate abnormal conditions with prioritization, timing, distinguishability, persistence, acknowledgement, and relationship to procedure. Do not maximize salience independently: excessive alarms can create masking, habituation, workload and attention capture. Route complex alert systems through supervisory-control and notification faculties when useful, while retaining flight-deck ownership of phase/crew consequences.

### 5. Design for error detection and management
Identify plausible design-induced slips, mode errors, data-entry errors, wrong-target actions, confirmation errors, memory failures, and crew coordination failures. The interface should prevent errors where feasible and make remaining errors detectable and manageable before unsafe consequence. Confirmation must expose the object/action/consequence, not merely add an “Are you sure?” dialog.

### 6. Preserve scan, workload, and degraded operation
Evaluate information placement and interaction under high workload, vibration, glare, turbulence, gloves where relevant, time pressure, divided attention, equipment failure, and partial automation loss. Critical information should remain interpretable under degraded modes. Recovery from automation or display failure must not rely on the failed channel.

### 7. Bind design claims to certification evidence
Keep a trace from each material interface decision to task analysis, human-factors rationale, requirement, simulation/test evidence, and applicable certification guidance. Evidence from consumer usability testing cannot substitute for representative flightcrew evaluation in operationally realistic conditions.

## Evidence
FAA Flight Deck Human Factors guidance explicitly treats displays, controls, procedures, automation, alerting, human error, workload, complexity, fatigue, and safety as one certification-oriented discipline. Active FAA guidance includes AC 20-175 for flight-deck control devices and AC 25.1302-1 for installed systems/equipment used by flightcrew, with the purpose of reducing design-related flightcrew error and enabling crews to detect and manage errors. Use current aircraft-category regulations, advisory circulars, manufacturer/system safety evidence, representative pilot testing and simulation as the actual authority. Do not convert this skill into a certification claim.

## Output Contract
Produce a `flight-deck-interface-contract` containing: certified/assumed operating context; crew roles; phase-of-flight matrix; system and automation modes; active/armed/target representation; control-display mapping; alert priority and acknowledgement model; error taxonomy; prevention/detection/recovery controls; workload and scan assumptions; degraded/failure states; physical and digital input constraints; procedure integration; crew cross-check points; training assumptions; evidence trace; applicable FAA/EASA/other authority references; unresolved hazards; and required independent human-factors/safety verification.

## Failure Traps
- Treating a flight display as a dense enterprise dashboard with aviation colors.
- Showing automation state without what it will do next or why a mode transition occurred.
- Using generic confirmation dialogs instead of making target, action and consequence explicit.
- Adding more alarms for safety until the alert system itself becomes an attention hazard.
- Assuming a touchscreen is acceptable because the function works in a simulator with a mouse.
- Moving critical controls/information dynamically in ways that break learned scan or muscle memory.
- Testing only nominal cruise and ignoring takeoff, approach, failure, turbulence or high-workload states.
- Encoding crew role or responsibility ambiguously across two operators.
- Calling a UI “FAA compliant” because it followed this skill without certification evidence.

The interface succeeds when trained flightcrew can correctly perceive aircraft/system state, understand automation and alert meaning, act on the intended target, detect and recover from errors, and maintain safe performance across relevant operational phases and failures.

## V6 Flight-Deck Protocol
Prioritize information by **phase-of-flight priority** because workload and time-to-action change across taxi, takeoff, climb, cruise, approach, landing, and abnormal events. Preserve a **mode-awareness invariant** for automation/flight guidance: active/armed modes, source, transitions, and unexpected reversion must remain perceivable.

Define **alert acknowledgement semantics** separately from resolving the underlying condition. Surface **sensor disagreement display** when redundant sources conflict rather than averaging into false certainty. Support **crew cross-check support** by making shared state, inputs, and confirmation observable to both operators without encouraging heads-down duplication.

### Falsification
Inject mode reversion, sensor disagreement, multiple alerts, high workload, and crew handoff. If operators can misidentify active mode/source, the UI is unsafe.

### Recovery
Return to conservative/known state, elevate source/mode truth, preserve alert history, and require procedural/authority revalidation before resuming automation-dependent action.
