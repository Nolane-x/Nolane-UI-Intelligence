---
name: designing-one-time-code-entry
description: Use when a verification or authentication flow accepts a short-lived code and must coordinate delivery, input, expiry, retry, autofill, privacy, and recovery without trapping users.
---

# Designing One-Time Code Entry

## Parent Contract
**Required parent:** `designing-authentication-and-passkeys`.

This faculty owns the interaction state around short-lived verification codes. It does not define authentication assurance or delivery-channel security policy. It makes the factor entry understandable, resilient to delay, and consistent with the backend’s actual expiry and attempt rules.

## Decision Model
Treat code entry as a state machine: destination selected, code requested, delivery pending, entry active, checking, accepted, expired, attempts exhausted, destination changed, and fallback invoked. The UI must never show a countdown or resend promise that differs from server authority.

A visually segmented six-box control may be useful, but implementation must behave like one coherent input for paste, deletion, selection, screen readers, password managers, and OS one-time-code autofill. Do not force users to manually advance focus between boxes or block pasting an entire code. Numeric-looking codes may still need leading zeros; never coerce them to numbers.

Communicate the destination at a privacy-safe level and keep “change email/phone” reachable. Resend creates a new causality problem: specify whether prior codes remain valid, which code is newest, and how the interface responds if deliveries arrive out of order. Rate limits are not generic errors; they need truthful retry timing when available and a non-abusive fallback.

## Failure Topology
- Six separate inputs require six focus moves and break paste/autofill.
- Client countdown reaches zero while the server still accepts the code, or vice versa.
- Resending makes the first code invalid but the UI never says so.
- Leading zero disappears because code is stored as an integer.
- Error text reveals whether a protected account exists beyond allowed disclosure.
- Users cannot correct the destination without abandoning the whole authentication flow.

## Falsification and Recovery
Falsify with full-code paste, mobile OTP autofill, screen readers, slow delivery, duplicate messages, resend before first delivery, leading zeros, expiry during submission, multiple incorrect attempts, destination correction, and a rate-limited channel. The design fails if users cannot tell which code is valid or if input mechanics become harder than the security check itself.

Recover by using a single semantic input model, server-sourced expiry/attempt state, explicit resend semantics, destination correction, bounded disclosure, and fallback factors owned by the parent authentication flow.

## Output Contract
Return `one-time-code-entry-contract` with factor destination display, semantic input model, paste/autofill behavior, expiry authority, attempt policy, resend causality, rate-limit feedback, destination correction, fallback handoff, privacy constraints, and falsification scenarios.