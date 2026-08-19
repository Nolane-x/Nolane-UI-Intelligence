---
name: designing-account-recovery-flows
description: Use when a user has lost a normal authentication path and the product must restore account access through bounded identity evidence, fallback factors, risk handling, rate limits, recovery state, and post-recovery security actions.
---

# Designing Account Recovery Flows

## Parent Contract
**Required parent:** `designing-authentication-and-passkeys`.

This faculty owns the end-to-end recovery path when ordinary sign-in cannot be completed. It does not own recovery-code storage, password reset UI in isolation, or support policy. Recovery is a security-sensitive identity re-entry process whose exact evidence and assurance requirements come from the current authentication architecture and risk policy.

## Decision Architecture
Begin with the failure mode without leaking account existence unnecessarily: lost password, unavailable second factor, lost passkey device, inaccessible email/phone, locked account, compromised credentials, or managed-enterprise access problem. Offer only recovery methods the account and policy actually support. Avoid a generic funnel that asks users to repeat impossible factors before revealing the real fallback.

Treat recovery as a state machine with an explicit recovery attempt identity: initiated, challenge issued, evidence pending, cooldown/rate-limited, additional review required, recovered, denied, expired, or cancelled. Some methods can complete automatically; higher-risk cases may require delayed/manual verification. Never present a support or identity-review route as guaranteed account restoration if the evidence may be insufficient.

After successful recovery, security state may need repair: revoke suspicious sessions, rotate password or factors, regenerate recovery codes, review account changes, or notify verified channels. Do not return directly to normal product use while leaving the compromised factor authoritative if policy says it should be replaced. Conversely, avoid forcing unrelated security setup that is not necessary for a legitimate low-risk recovery.

## Failure Topology
- Recovery form reveals “No account with this email” in a context where enumeration should be prevented.
- User without phone access is forced through SMS repeatedly before another supported recovery method appears.
- Manual review page says “We'll recover your account” although verification can still fail.
- Rate limit clears the user's entered recovery context and restarts the process from zero.
- Recovery succeeds but stolen sessions remain active and no post-recovery review occurs.
- A recovery-code flow is mixed with account recovery so users are shown existing backup secrets they should never be able to retrieve.

## Falsification and Recovery
Falsify with lost password, lost second factor, passkey device unavailable, email unavailable, compromised account, rate limiting, expired challenge, manual review, managed enterprise account, recovery from a new device/location, screen-reader operation, and a successful recovery followed by active-session review. The design fails if it leaks protected account state, relies on an unavailable factor without alternative, or restores access without reconciling the security state that caused recovery.

Recover by using policy-authorized factor discovery, bounded disclosure, persistent recovery-attempt identity, explicit cooldown/review states, risk-appropriate escalation, truthful outcome language, and post-recovery session/factor remediation tied to current security evidence.

## Output Contract
Return `account-recovery-flow-contract` with recovery failure modes, supported method discovery, disclosure policy, attempt state machine, challenge/cooldown rules, escalation/manual-review semantics, success/denial/expiry behavior, post-recovery remediation, managed-account handoff, accessibility requirements, and falsification cases.