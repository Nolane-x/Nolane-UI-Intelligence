---
name: critiquing-security-and-privacy
description: Use when UI handles authentication, authorization, permissions, secrets, sensitive data, sharing, payments, agent actions, public/shared devices, generated UI actions, or choices that can leak information or coerce consent.
---

# Critiquing Security and Privacy

## Overview
Review the UI as a security boundary explanation, not as the security boundary itself. Detect misleading authorization, account enumeration, unsafe defaults, sensitive disclosure, coercive permission design, and action ambiguity while requiring backend/runtime controls for enforcement.

## Parent Contract
**Required parent:** `challenging-ui-designs`.

**May modify:** false. Consume authentication, consent, privacy, transaction, agent autonomy, and generative-UI contracts as applicable. Missing backend enforcement evidence is not repaired by disabling a button.

## Decision Model
Inspect **identity**, **authority**, **data exposure**, **consent**, and **execution boundary**. Identity: can login/recovery errors leak account or factor existence? Can account switching leave stale private state? Authority: does visible capability match server/tool permission, and are sensitive actions reauthorized appropriately? Exposure: where can sensitive content appear — notifications, history, logs, clipboard, shared links, AI context, kiosk state? Consent: are choices informed, granular, revocable, and free of asymmetric coercion? Execution: does generated or agent UI reference typed authorized actions rather than arbitrary executable code or user-controlled targets?

Test ambiguity at commit. Financial, sharing, permission, deployment, and agent actions need target/scope/consequence visibility. Generic success must not imply an operation completed when state is unknown. Review fallback and error messaging for information disclosure as well as recoverability.

Privacy claims must match actual retention and transmission behavior. A UI cannot promise deletion if backend policy differs. Redaction on screen is not privacy if copy/export/logging still exposes full data.

## Evidence
Use backend/tool authorization tests, error response comparisons, privacy data-flow maps, permission state, shared-device scenarios, network/action logs, generated payload validation, duplicate/replay tests, and OWASP/FIDO/NIST or applicable platform/regulatory guidance. Do not infer security from visual affordance.

## Output Contract
Return a `finding-set` with `may_modify:false`, `artifact_revision`, `findings[] {finding_id, severity, security_or_privacy_class, evidence, boundary, user_impact, falsifier, recommended_repair, required_reverification}`, `authorization_gaps[]`, `exposure_paths[]`, `consent_defects[]`, and `release_recommendation`.

## Failure Traps
- Disabled button treated as authorization.
- Specific login errors reveal which accounts exist.
- Consent acceptance rate treated as success metric despite dark patterns.
- “Delete” UI promise unsupported by retention behavior.
- Generated UI allowed to execute arbitrary code/actions.
- Shared-device session clears visually but cached history remains.
- Security review downgraded because UX friction would increase.

Security and privacy findings are about truth at boundaries, not how secure the screen looks.