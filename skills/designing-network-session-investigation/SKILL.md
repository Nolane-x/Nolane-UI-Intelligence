---
name: designing-network-session-investigation
description: Use when analysts investigate network conversations across flows, packets, proxies, NAT, TLS, DNS, and application metadata and need session identity, direction, timing, and visibility limits to remain explicit.
---
# Designing Network Session Investigation

## Decision ownership

Own the investigation model for network communication sessions. Decide how source/destination identity, direction, protocol, connection lifetime, bytes, requests, DNS/TLS context, proxy/NAT transformations, and capture visibility are presented so analysts can reconstruct what actually communicated. This faculty does not operate packet capture infrastructure and does not decide threat maliciousness. It prevents network summaries from erasing transformations or visibility gaps that materially change interpretation.

## Inputs and evidence

Require flow/session identifiers, sensor location, source and destination addresses and ports, translated addresses, direction inference, protocol metadata, timestamps and duration, byte/packet counts, DNS answers, TLS certificates/SNI where available, HTTP/proxy fields, process attribution, packet-capture availability, retention, and known blind spots. Include asymmetric routing, NAT, load balancers, VPNs, shared proxies, encrypted sessions, retransmissions, short failed connections, long-lived sessions, and telemetry that sees only one side.

## Procedure

Establish a canonical session view while retaining every transformation. Show original endpoint, observed endpoint, translated endpoint, and proxy hop when evidence supports them; do not flatten these into one pair of IPs. Separate transport success from application success. Provide a time-aligned sequence of connection establishment, name resolution, TLS negotiation, requests, responses, resets, and closure when such evidence exists, while indicating missing layers. Bind process or user attribution with confidence and source. Offer pivots to related sessions by host, process, domain, certificate, destination, or time window without losing the originating session. For encrypted traffic, explicitly show what metadata is known and what payload content is unavailable.

## Failure topology

- NAT or proxy rewriting makes an internal host appear to be the actual external destination.
- A SYN attempt and a completed application request share the same “connection” state.
- Encryption is displayed as if no visibility limitation exists.
- Direction is guessed from port numbers and becomes wrong for nonstandard services.
- Flow aggregation merges separate sessions and hides burst behavior or failures.
- Process attribution from one sensor is treated as universal fact across the path.
- Packet-capture absence is mistaken for absence of network activity.

## Falsification

Investigate one proxied HTTPS connection, one failed connection attempt, one long-lived session, one NAT-translated flow, one session with packet capture, and one with metadata only. The design fails if analysts cannot reconstruct observed versus translated endpoints, cannot distinguish transport from application outcome, or cannot tell which details are unavailable rather than negative.

## Output contract

Return `network-session-investigation-contract` containing session identity, direction rules, transformation chain, protocol-layer state, encryption/visibility limits, process/user attribution confidence, aggregation boundaries, pivot state, and network investigation test cases.

## Handoffs

Entity identity routes to `designing-security-entity-investigation`; cross-session patterns route to `designing-security-event-correlation`; IOC matching routes to `designing-indicator-of-compromise-search`; endpoint containment routes to `designing-endpoint-isolation-controls`. Generic log/table/network visualizations remain subordinate to the session truth model here.