---
name: designing-incident-severity-declaration
description: Use when this specialist's decision ownership is materially in scope. Own incident severity assessment, declaration, change provenance, uncertainty, impact criteria, and escalation consequences without reducing severity to a colored badge.
---
# Designing Incident Severity Declaration

## Parent Contract

**Required parent:** `designing-incident-response-operations`.

Inherit the broader routing and decision boundary from this canonical parent; this specialist remains accountable only for the narrower ownership, failure topology, falsification criteria, and output contract defined below.

## Decision ownership

Own how an incident receives and changes severity. Decide criteria presentation, evidence required, provisional severity, authority to declare/change, consequence preview, and history. Severity is a coordination contract because it can alter paging, leadership attention, communication cadence, and response process; this owner keeps those effects inspectable.

## Inputs and evidence

Require severity policy, impact dimensions, affected-user/service metrics, regulatory/contractual triggers, declaration roles, escalation consequences, uncertainty handling, and downgrade criteria. Identify whether severity is based on current impact, potential impact, duration, breadth, or combinations.

## Procedure

Present severity definitions in operational language with observable impact examples. Allow a provisional classification when evidence is incomplete, and distinguish it from confirmed severity. The declaration control should summarize current evidence and the operational consequences of the chosen level. Changing severity must record actor, time, previous/new level, rationale, and affected response obligations. Downgrade should require recovery evidence appropriate to policy; avoid pressure to lower severity merely because responders are active. Where dimensions conflict, show the conflict rather than hiding it inside one opaque score.

## Failure topology

Failures include arbitrary badge selection, severity driven by alert priority rather than impact, silent downgrades, historical changes overwritten, policy text inaccessible during the incident, and automation changing severity without human understanding. Another failure is making declaration so bureaucratic that responders delay coordination during a rapidly expanding event.

## Falsification

Reject if a responder cannot see the operational definition of a selected severity; if changing level leaves no rationale/history; if provisional and confirmed severity are indistinguishable; if one detector's alert severity automatically becomes incident severity with no impact assessment; if downgrade lacks recovery evidence; or if declaration requires enough form filling to impede urgent response.

## Output contract

Return an `incident-severity-declaration-contract` containing: severity levels and criteria; provisional state; evidence fields; declaration authority; consequence summary; change/downgrade rules; provenance; automation limits; conflict/uncertainty treatment; and response-obligation handoffs. Include one evidence-conflict case.

## Handoffs

Incident response consumes the declared level, escalation controls enact paging/leadership consequences, stakeholder communications use cadence requirements, and service health/impact analysis supply evidence without owning the severity decision.