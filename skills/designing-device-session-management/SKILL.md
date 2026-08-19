---
name: designing-device-session-management
description: Use when users inspect and revoke authenticated sessions across browsers or devices and the UI must communicate session identity, freshness, current-device safety, approximate location, bulk revocation, and uncertain telemetry.
---

# Designing Device Session Management

## Parent Contract
**Required parent:** `designing-authentication-and-passkeys`.

This faculty owns post-authentication session visibility and revocation. It does not define token architecture or device attestation. The interface must help a user decide whether a session is expected and safely terminate unwanted access without overstating what sparse device/IP metadata can prove.

## Decision Architecture
Represent each session with stable server identity plus bounded descriptors: device/browser/app when known, platform, created/last-active evidence, approximate network location if policy allows, authentication method, and whether it is the current session. Do not invent a friendly device name from unreliable user-agent parsing as if it were verified hardware identity.

Freshness matters. “Active now” should have an evidence window; “last used 2 hours ago” may be delayed. IP-derived location is approximate and can reflect VPNs, carrier gateways, or travel. Use city/region wording conservatively and avoid alarming language that implies precise physical tracking.

Revocation is a security action with current-session consequences. Users should be able to revoke one session, all other sessions, or organization-defined scopes where supported. Protect against accidentally revoking the current session when the intent was “sign out other devices,” and explain that a stolen refresh token/session may not disappear from an already-loaded offline page until it contacts the server.

## Failure Topology
- Three sessions from one browser profile appear as three different named devices with no stable identity explanation.
- Approximate IP city is treated as proof of account compromise.
- “Sign out all devices” includes the current device unexpectedly and interrupts recovery work.
- Revoked session remains displayed active for minutes with no “revocation pending/stale telemetry” state.
- Session list exposes raw IP addresses in a context where policy intended a less sensitive summary.
- Current-session badge is based on display name rather than the actual session ID and marks the wrong row.

## Falsification and Recovery
Falsify with VPN, mobile carrier IP change, multiple tabs sharing one session, native app plus browser, expired session, current-device revocation, “all others” revocation, telemetry lag, screen-reader table/list navigation, and account password/factor change revoking sessions automatically. The design fails if users cannot distinguish current session from other sessions by authoritative identity or if approximate metadata is presented as forensic certainty.

Recover by using server session IDs, conservative device/location labels, explicit freshness, safe current-session protection, scoped bulk actions, authoritative revocation acknowledgement, and refresh after account-security events.

## Output Contract
Return `device-session-management-contract` with session identity, descriptors, freshness semantics, current-session detection, location uncertainty, single/bulk revocation, current-session safeguards, automatic revocation events, privacy display rules, accessibility behavior, and falsification cases.