---
name: designing-responder-role-assignment
description: Use when this specialist's decision ownership is materially in scope. Own incident role assignment, acceptance, vacancy, transfer, backup, and authority visibility so responders know who is accountable for command, operations, communications, and specialist functions.
---
# Designing Responder Role Assignment

## Parent Contract

**Required parent:** `designing-incident-response-operations`.

Inherit the broader routing and decision boundary from this canonical parent; this specialist remains accountable only for the narrower ownership, failure topology, falsification criteria, and output contract defined below.

## Decision ownership

Own role occupancy and authority during an incident. Decide required/optional roles, assignment/acceptance, temporary vacancy, backup/delegation, handoff, multi-role constraints, and visibility. This is not ordinary task assignment: roles carry incident-wide authority and coordination obligations.

## Inputs and evidence

Require role taxonomy, on-call roster, qualification constraints, severity-specific required roles, assignment authority, communication channels, shift duration, and handoff policy. Identify roles that must remain independent, such as incident command and external communications in some organizations.

## Procedure

Show active roles near the incident header with named occupants and availability status. Assignment should require explicit acceptance when feasible; pending assignment is not occupied. Required vacant roles must remain visible as gaps. If one person holds multiple roles, display the overload rather than hiding duplicate names. Transfer should capture outgoing/incoming actors, effective time, and handoff note. Backups should be distinguishable from current authority. Role changes need immediate propagation to action approval, notification, and communication surfaces that depend on authority.

## Failure topology

Failures include assumed ownership, stale role badges after shift change, two people believing they are incident commander, a person listed before accepting, and hidden role vacancies. Another failure is assignment controls that expose sensitive personal scheduling details beyond operational availability.

## Falsification

Reject if a required role can be vacant without a prominent cue; if two active commanders can coexist unintentionally; if transfer has no effective time; if a pending assignee is shown as fully active; if role-dependent controls still authorize the previous owner after transfer; or if privacy-sensitive roster information is exposed unnecessarily.

## Output contract

Return a `responder-role-assignment-contract` containing: role taxonomy; severity-specific requirements; assignment/acceptance states; vacancy cues; qualification constraints; multi-role policy; backup semantics; transfer/handoff record; authority propagation; and privacy limits. Include one mid-incident commander transfer.

## Handoffs

Incident command controls enforce role authority, on-call handoffs supply shift context, war-room collaboration reflects active roles, and generic assignment mechanics remain subordinate to the incident authority model.