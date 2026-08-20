---
name: designing-authentication-anomaly-review
description: Use when analysts review suspicious sign-ins or authentication behavior and must reason about identity, device, session, geography, factors, conditional access, travel, and baseline uncertainty without turning anomaly scores into verdicts.
---
# Designing Authentication Anomaly Review

## Decision ownership

Own the analyst-facing review of suspicious authentication activity. Decide how sign-in attempts, successful sessions, factors, device posture, IP/network context, application target, conditional-access decisions, impossible-travel signals, token use, and identity baseline are assembled into one inspectable narrative. This faculty does not define authentication UX for end users and does not calculate the anomaly model. Its job is to let analysts distinguish unusual from malicious and understand what controls actually allowed or blocked access.

## Inputs and evidence

Require identity identifiers and aliases, authentication timestamps, source network, geo confidence, device identifiers and management state, browser/client, application/resource, authentication protocol, factor sequence, MFA result, conditional-access policy outcome, token/session identifiers, risk signals, prior sign-in baseline, password/reset events, travel context when available, and telemetry freshness. Include VPNs, mobile carriers, shared egress, service accounts, privileged accounts, newly enrolled devices, token refreshes, failed MFA, and sessions that continue after the initial sign-in.

## Procedure

Separate authentication attempts from established sessions and later token activity. Build a chronological chain showing challenge, factor, policy evaluation, grant/deny, token issuance, session continuation, and revocation where evidence exists. Explain anomaly contributors individually—new country, new ASN, new device, atypical time, unfamiliar application, rapid location change—rather than exposing only a risk score. Display geo precision and network ambiguity so VPN or mobile routing does not look like physical travel certainty. Compare against a bounded baseline with sample size and recency. Give privileged identities stronger context but avoid automatically equating rarity with compromise. Preserve links to password changes, device enrollment, and administrative events around the same period.

## Failure topology

- “Impossible travel” is shown as fact despite VPN, proxy, or coarse geolocation uncertainty.
- A blocked attempt and a successful authenticated session look equivalent.
- MFA success is treated as proof of legitimacy even when a stolen session or prompt fatigue is plausible.
- Token refresh activity is mistaken for a fresh interactive sign-in.
- Baseline labels hide that the account has almost no historical data.
- Service-account behavior is judged against human travel patterns.
- Session revocation is displayed without showing whether downstream tokens remain active.

## Falsification

Review a legitimate VPN traveler, a service account, a new managed device, a failed MFA burst followed by success, a stolen-token scenario with no fresh login, and a low-history privileged user. The design fails if analysts cannot distinguish attempt versus session, cannot inspect why an anomaly exists, or are pushed toward malicious/benign conclusions by an unexplained scalar score.

## Output contract

Return `authentication-anomaly-review-contract` containing authentication/session state model, anomaly-factor explanation, geo/network uncertainty, device and factor context, baseline confidence, policy-outcome representation, token/session continuity, privileged-account treatment, and review scenarios.

## Handoffs

Identity truth routes to `designing-security-entity-investigation`; privilege-change context routes to `designing-privilege-escalation-review`; containment or session revocation uses trust/security action owners; correlation with endpoint or network evidence routes to `designing-security-event-correlation`. End-user authentication design remains with `designing-authentication-and-passkeys`.