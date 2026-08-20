---
name: designing-incident-response-operations
description: Use when this specialist's decision ownership is materially in scope. Own the command-and-evidence architecture for time-critical operational incidents from declaration through mitigation, communication, recovery, and retrospective handoff.
---
# Designing Incident Response Operations

## Parent Contract

**Required parent:** `designing-high-stakes-decisions`.

Inherit the broader routing and decision boundary from this canonical parent; this specialist remains accountable only for the narrower ownership, failure topology, falsification criteria, and output contract defined below.

## Decision ownership

Own the incident workspace as a coordinated operational state machine. Decide what constitutes an active incident, which facts are canonical, how severity and command roles are represented, how timeline/evidence/mitigation/communications stay synchronized, and what moves the incident from detection to controlled recovery and closure. This skill does not define monitoring algorithms or remediation commands; it makes the human operational process explicit, traceable, and hard to misread under pressure.

## Inputs and evidence

Require incident lifecycle, severity policy, responder roles, escalation model, services/dependencies, alert sources, mitigation actions, communication audiences, audit requirements, time synchronization, and postmortem expectations. Inspect real incident transcripts and high-noise alert sets. Record which actions are reversible, which can affect production, and where stale telemetry can create dangerous false confidence.

## Procedure

Create one canonical incident header with status, severity, start time, affected scope, commander/lead, and current objective. Separate facts, hypotheses, actions, and communications so tentative reasoning is not displayed as confirmed truth. Bind every major action to actor/time/result and allow evidence to be attached without burying the operational summary. Keep mitigation and communication state visible in parallel: operators should not need to infer public messaging from chat activity. Changes in severity, commander, or affected scope require explicit provenance. Recovery should be a distinct monitored phase before resolution, with criteria that verify stability rather than equating one green metric with success.

## Failure topology

Failures include multiple competing incident summaries, severity changing without provenance, chat becoming the only source of truth, hypotheses presented as facts, mitigation actions with no result, public status lagging silently, and declaring resolution immediately after a metric recovers. Another failure is role ambiguity where several responders assume someone else owns the next irreversible action.

## Falsification

Reject if two responders can see different canonical severity or scope; if an irreversible mitigation can be launched without a visible owner/consequence boundary; if a hypothesis cannot be distinguished from confirmed evidence; if the timeline cannot reconstruct who did what and when; if recovery criteria are undefined; or if a resolved incident can still have acknowledged active impact with no contradiction warning.

## Output contract

Return an `incident-response-operations-contract` containing: lifecycle states; canonical header fields; fact/hypothesis/action/communication distinctions; role authority; severity provenance; mitigation evidence; affected-scope model; recovery criteria; resolution gate; audit/time requirements; and handoffs to postmortem. Include one severity escalation and one unstable-recovery scenario.

## Handoffs

Delegate alert triage, severity declaration, timeline, responder roles, war room, runbooks, health, impact, escalation, stakeholder communications, status page, on-call handoff, command controls, mitigation tracking, hypothesis/evidence, postmortem, maintenance windows, and reliability experiments to their dedicated owners. Generic high-stakes and collaboration skills remain authoritative for irreversible actions and communication mechanics.