---
name: designing-security-centers
description: Use when account users need a consolidated view of security posture and high-impact actions such as authentication factors, sessions, recent security events, recovery state, alerts, and recommended remediation.
---

# Designing Security Centers

## Parent Contract
**Required parent:** `designing-privacy-sensitive-interfaces`.

This faculty owns the security posture overview and routing surface for an account or workspace. It does not implement password, passkey, 2FA, session, or recovery mechanics; those remain specialist flows. Its purpose is to expose current evidence, unresolved risk, and the correct next action without manufacturing a simplistic universal “security score.”

## Decision Architecture
Build posture from concrete security dimensions: active authentication methods, recovery readiness, recent/current sessions, suspicious or security-relevant events, verified contact factors where applicable, organization requirements, and unresolved security alerts. Avoid combining unrelated facts into one gamified percentage that implies scientific risk precision the product cannot justify.

Prioritize by consequence and actionability. “Unrecognized session active now” can deserve more prominence than “Add another recovery method.” Recommendations should explain the evidence and benefit, not shame users. If an organization mandates a factor, show the policy source and effective requirement rather than presenting compliance as optional advice.

Security data has freshness and sensitivity. Last login, device, IP-derived location, or event metadata may be approximate; label them conservatively. Do not expose more historical security detail than the current user is authorized to inspect. Deep links into factor/session flows should preserve a safe return to the security center and update status after remediation.

## Failure Topology
- Product shows “Security score 92%” although the model and weighting have no defensible risk basis.
- A stale device list makes a revoked session look active or an active session look gone.
- Approximate IP location is shown as an exact physical address and triggers false alarm.
- Organization-required 2FA is labeled “Recommended,” so users misunderstand why access will later be blocked.
- High-severity unrecognized session is buried below promotional passkey education.
- Completing a remediation leaves the old warning visible and undermines trust.

## Falsification and Recovery
Falsify with new session from another device, stale telemetry, factor added/removed in another tab, organization policy change, recovery contact unavailable, approximate geo-IP, permission-restricted enterprise account, keyboard/screen-reader operation, and remediation completed through a child flow. The design fails if posture claims cannot be traced to concrete current evidence or if severity is encoded only through a generic score/color.

Recover by using evidence-based sections, consequence-driven prioritization, freshness labels, explicit policy origin, conservative location language, specialist action handoffs, and authoritative refresh after remediation.

## Output Contract
Return `security-center-contract` with posture dimensions, evidence/freshness, severity/actionability rules, policy requirements, recommendation boundaries, security-event/session summaries, specialist-flow links, remediation refresh, privacy/access controls, accessibility semantics, and falsification cases.