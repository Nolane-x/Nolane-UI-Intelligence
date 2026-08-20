---
name: designing-war-room-collaboration
description: Use when this specialist's decision ownership is materially in scope. Own high-tempo incident collaboration spaces where discussion, decisions, actions, evidence, roles, and side conversations must remain coordinated without turning chat into the source of truth.
---
# Designing War-Room Collaboration

## Parent Contract

**Required parent:** `designing-incident-response-operations`.

Inherit the broader routing and decision boundary from this canonical parent; this specialist remains accountable only for the narrower ownership, failure topology, falsification criteria, and output contract defined below.

## Decision ownership

Own the collaboration topology of an active incident room. Decide how conversation relates to canonical incident state, how commands/decisions/actions are promoted from chat, how threads or channels separate topics, how newcomers catch up, and how noise is controlled. Generic chat owns message mechanics; this skill ensures chat supports response rather than becoming an unstructured operational database.

## Inputs and evidence

Require collaboration channels, participant count, external guests, role model, bot/integration messages, incident artifacts, command usage, notification rules, retention, and handoff frequency. Inspect real busy incidents where hundreds of messages coexist with a small number of decisive actions.

## Procedure

Keep the incident summary, current objective, commander, severity, and active mitigations visible alongside conversation. Provide lightweight promotion from a message to a decision, timeline event, action, hypothesis, or evidence link so important content exits the chat stream. Threading should isolate investigations without hiding critical decisions from the main incident context. Bot/telemetry messages need separate treatment and rate control. New responders need a concise catch-up surface built from canonical state plus pinned decisions, not an instruction to read every message. Guest/external participant boundaries must be explicit.

## Failure topology

Failures include chat as the only timeline, critical commands buried under bot spam, side threads containing unshared decisions, responders repeating work because context is not promoted, and newcomers scrolling for twenty minutes before acting. Another failure is accidentally exposing internal diagnostics or customer data to external participants in a shared room.

## Falsification

Reject if a major decision can exist only as an unpinned message; if bot traffic can dominate the collaboration stream; if a thread can change incident strategy without a main-context signal; if a newcomer cannot identify current objective and mitigations quickly; if external participant scope is ambiguous; or if role/commander changes do not update the room context.

## Output contract

Return a `war-room-collaboration-contract` with: room structure; canonical-state sidecar; message-to-artifact promotion; thread/channel rules; bot/noise handling; pinned decision/action behavior; newcomer catch-up; role cues; external-participant boundaries; and retention/export links. Include one high-noise integration scenario.

## Handoffs

Timeline capture, mitigation tracking, hypothesis/evidence, and stakeholder communications own promoted artifacts. Generic threaded conversation and mentions provide mechanics but not incident information architecture.