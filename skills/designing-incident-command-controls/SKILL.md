---
name: designing-incident-command-controls
description: Use when this specialist's decision ownership is materially in scope. Own commander-level incident controls for objectives, operational phases, role authority, decision gates, pause points, delegation, and high-consequence action oversight.
---
# Designing Incident Command Controls

## Parent Contract

**Required parent:** `designing-incident-response-operations`.

Inherit the broader routing and decision boundary from this canonical parent; this specialist remains accountable only for the narrower ownership, failure topology, falsification criteria, and output contract defined below.

## Decision ownership

Own the compact set of controls and evidence a designated incident commander needs to coordinate response. Decide current objective, phase, role authority, decision queue, high-consequence approvals, delegation, pause/hold semantics, and confirmation of resolution criteria. This skill must not turn the commander into a click-through bottleneck for routine specialist work.

## Inputs and evidence

Require command role policy, severity obligations, action classes needing approval, current incident state, responder roles, mitigation queue, communication deadlines, recovery criteria, and escalation paths. Identify commands that are irreversible or legally significant and those that should remain delegated.

## Procedure

Center the command view on current objective, affected scope, severity, roles, active mitigations, unresolved critical decisions, and next verification point. Present high-consequence actions as evidence-backed decisions with target, expected effect, rollback, owner, and approval state. Support delegation with explicit authority boundaries. A hold/pause should state what is paused and what continues. Command phase changes—investigation, mitigation, recovery, resolved—must capture rationale and criteria. Keep routine task execution out of the command surface unless it becomes blocked or escalated.

## Failure topology

Failures include commander dashboards full of low-level telemetry, every action requiring commander approval, irreversible actions buried in chat, delegation with unclear authority, phase changes without rationale, and resolution controlled by one button detached from recovery evidence. Another failure is stale role information causing the wrong person to see privileged controls.

## Falsification

Reject if the command view cannot identify the current response objective; if a high-consequence action lacks target/owner/rollback or explicit no-rollback warning; if delegated authority cannot be inspected; if phase change has no evidence/rationale; if routine work is unnecessarily serialized through command; or if role transfer leaves old commander controls active.

## Output contract

Return an `incident-command-controls-contract` with: command summary; objective model; phase state machine; decision queue; high-consequence action schema; approval/delegation rules; hold semantics; role-authority binding; recovery/resolution gate; and stale-role revocation behavior. Include one delegated mitigation and one no-rollback decision.

## Handoffs

Responder roles establish command authority, mitigation tracking supplies action state, severity/escalation define obligations, and high-stakes decision owners govern irreversible confirmation mechanics.