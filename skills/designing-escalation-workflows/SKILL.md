---
name: designing-escalation-workflows
description: Use when work can be raised to a higher expertise, authority or urgency path and the interface must make trigger, destination, added context, ownership and de-escalation consequences explicit.
---

# Designing Escalation Workflows

## Parent Contract
**Required parent:** `designing-task-flows`.

This faculty owns escalation interaction and state. It does not define the organizational escalation policy or generic assignment mechanics.

## Decision Boundary
Escalation is not merely increasing priority. It changes who or what process is responsible, what evidence is required, or what response expectations apply. Model trigger type: manual request, severity threshold, SLA breach risk, automated rule, failed remediation, customer request or safety condition. Preserve trigger provenance.

Before escalation, show destination and consequences: specialist team, supervisor, incident channel, regulatory review, emergency path, or another queue. Gather only context the destination needs and reuse existing case evidence rather than forcing users to retype the story. Required rationale should be proportional to impact.

Escalated status must coexist with lifecycle and ownership. A case can be in progress and escalated; escalation may transfer ownership, add an oversight role, or create a linked child process. Make the chosen model explicit. Avoid silently removing the original handler from visibility when they remain responsible for communication.

Automatic escalation needs explainability and override policy. If a threshold triggered it, show the rule/event. If users can de-escalate, state what conditions are required and whether the original SLA/priority is restored or recalculated.

## Failure Topology
- “Escalate” only changes a red badge while no responsible team is notified.
- Users re-enter incident details because escalation creates an empty new form detached from the case.
- Auto-escalation fires but there is no explanation or way to see the trigger.
- Escalation transfers ownership while prior assignee still appears primary in the header.
- De-escalation erases the fact that an escalation occurred.
- Repeated escalation clicks create duplicate specialist cases.

## Falsification and Recovery
Falsify with manual/automatic triggers, duplicate clicks, destination unavailable, permission failure, transfer vs oversight models, de-escalation and linked child workflows. Audit whether one escalation event has one identity and a traceable destination/outcome.

Recover by modeling escalation as a durable event/state, binding it to a destination and responsibility change, reusing case evidence and preserving history even after de-escalation.

## Output Contract
Return `escalation-workflow-contract` with trigger taxonomy, source provenance, destination, evidence packet, ownership/lifecycle effect, duplicate prevention, automation rationale, de-escalation policy, history and end-to-end routing tests.