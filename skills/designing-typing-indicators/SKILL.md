---
name: designing-typing-indicators
description: Use when a conversation exposes ephemeral composing activity and the interface must define start/stop timing, aggregation, privacy, stale-state expiry, and layout behavior without treating typing as durable presence.
---

# Designing Typing Indicators

## Parent Contract
**Required parent:** `designing-chat-interfaces`.

This faculty owns short-lived evidence that another participant is currently composing in the active conversational context. It is not general presence, online status, or proof that a message will be sent. Because typing signals are ephemeral and often lossy, the UI must tolerate missing and stale events gracefully.

## Decision Model
Define the event protocol: start after meaningful input, refresh while composing, stop on send, draft clear, conversation leave, explicit stop event, or a bounded inactivity timeout. Never rely on receiving a stop event in distributed systems; stale indicators need automatic expiry.

Scope the signal precisely to conversation or thread identity. Typing in one channel must not appear in another. In group conversations, aggregate participants in a readable way: name one or two people, then summarize the rest rather than generating a rapidly changing sentence. Avoid large layout shifts; the indicator should occupy stable space or a predictable status region.

Privacy and user expectations matter. Some contexts should not emit typing telemetry, especially when conversations are sensitive or when participants are not mutually visible. The indicator should never reveal draft content, length, cursor activity, or whether someone is deleting rather than typing unless product policy explicitly and safely defines that behavior.

## Failure Topology
- Indicator stays forever because a stop event was lost.
- User types in Thread A but “typing…” appears in the parent channel or another thread.
- Five participant names continuously reorder, producing distracting flicker.
- Typing signal is emitted on every keystroke at a rate that harms performance or privacy.
- Indicator is positioned below the composer and pushes messages up/down on every state change.
- Screen reader repeatedly announces each heartbeat refresh as new content.

## Falsification and Recovery
Falsify with network disconnect, app close without stop event, rapid channel switching, many simultaneous typers, draft cleared without send, privacy-disabled mode, screen-reader use, and slow heartbeat delivery. The design fails if stale activity can persist beyond a bounded timeout or if typing evidence crosses conversational scope.

Recover by using scoped start/refresh events, local expiry timers, coalesced group representation, rate-limited emission, stable placement, privacy controls, and announcement only on meaningful participant-state changes rather than heartbeats.

## Output Contract
Return `typing-indicator-contract` with event triggers, refresh/expiry timing, conversation/thread scope, group aggregation, privacy emission rules, rate limits, stable placement, disconnect cleanup, accessibility announcement policy, and falsification cases.