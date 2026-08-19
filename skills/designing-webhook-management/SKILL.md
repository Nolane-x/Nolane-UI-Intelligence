---
name: designing-webhook-management
description: Use when developers configure event delivery to external HTTP endpoints and the interface must coordinate subscriptions, endpoint identity, signing, retries, delivery history, test events, rotation, and failure recovery.
---

# Designing Webhook Management

## Parent Contract
**Required parent:** `designing-data-dense-interfaces`.

This faculty owns operational UX for outbound event subscriptions. It does not own generic API exploration or secret custody. Webhooks create side effects outside the product boundary, so configuration and observability must connect event selection, endpoint authority, security material, and delivery evidence.

## Decision Architecture
Represent each webhook with stable ID, destination URL, subscribed event types, scope, active/paused state, API/event schema version, signing configuration, and retry policy as provided by the platform. Validate obvious URL/scheme issues locally, but do not claim an endpoint is healthy until an actual delivery/test result proves reachability.

Secret values require one-way handling. A signing secret may be shown once at creation or rotated through the secret-management owner; the management table should expose fingerprint/last-rotated status rather than the secret. Test delivery needs a clearly labeled sample event or selected real-event replay with safeguards so developers know what external side effect may occur.

Delivery history should connect attempt, event ID, timestamp, response status, duration, retry number, and truncated/redacted request/response evidence. Retrying or replaying must clarify whether it reuses the same event identity and signature timestamp or creates a new delivery attempt. Repeated failures can pause or disable an endpoint according to service policy; show why and how to recover.

## Failure Topology
- Saving an endpoint displays “Connected” before any request has succeeded.
- Signing secret is repeatedly retrievable from the settings page and leaks through screenshots/support.
- “Send test” uses a production event payload without warning and triggers a real downstream action.
- Delivery log exposes authorization tokens or sensitive payload fields unredacted.
- Retry button creates a new business event rather than replaying delivery of the existing event.
- Endpoint is auto-disabled after failures but UI only shows a generic inactive toggle with no reason.

## Falsification and Recovery
Falsify with DNS/TLS failure, 2xx/4xx/5xx responses, timeout, signing-secret rotation, duplicate/replayed event, schema-version change, endpoint auto-disable, large sensitive payload, keyboard/screen-reader inspection, and URL edit while deliveries are in flight. The design fails if configuration state is mistaken for delivery health or if replay semantics can duplicate the underlying business event ambiguously.

Recover by separating configured from verified/healthy state, one-way secret presentation, explicit test payload semantics, redacted delivery evidence, stable event/delivery IDs, documented retry/replay behavior, and actionable disabled-state recovery.

## Output Contract
Return `webhook-management-contract` with subscription schema, endpoint configuration, event/version scope, secret handoff, test delivery semantics, health evidence, delivery-history schema, redaction, retry/replay identity, disable/recovery policy, and falsification cases.