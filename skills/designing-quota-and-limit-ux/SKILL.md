---
name: designing-quota-and-limit-ux
description: Use when users approach or exceed product limits and the interface must explain scope, hard vs soft enforcement, reset/upgrade path, partial availability and recovery without weaponizing scarcity or blocking work without context.
---

# Designing Quota and Limit UX

## Parent Contract
**Required parent:** `designing-subscription-management`.

This faculty owns user-facing resource/entitlement limits. Usage measurement is a sibling; authorization policy and pricing decisions remain external.

## Decision Boundary
Classify the limit before designing warnings: hard cap, soft cap, rate limit, concurrent limit, storage capacity, seat entitlement, feature entitlement, trial quota or policy threshold. Identify scope—user, project, workspace, organization, API key—and reset behavior. “Limit reached” with no scope is operationally useless.

Warn at thresholds only when action is possible or the impending block is material. Use current/remaining amount and expected reset/effective date. Avoid repeated banners on every screen; centralize persistent state and place contextual warnings near blocked actions.

Exceed behavior must match enforcement. Hard cap may block creation while preserving read/export/delete actions needed to recover. Rate limits may show retry time. Storage limits should prioritize cleanup/export and explain whether uploads, edits or background processing are affected. Never disable every control with one global overlay unless the system truly becomes unusable.

Upgrade is one recovery route, not the only one. If users can delete data, reduce seats, wait for reset, request admin action or change scope, surface those options. Where an administrator controls billing, non-admin users need a route to request help rather than a dead-end upgrade button they cannot complete.

## Failure Topology
- “You reached your limit” omits which workspace or meter is exhausted.
- Upgrade modal blocks access to deletion/export that could reduce usage.
- Soft warning is styled as immediate failure and creates unnecessary urgency.
- Rate limit gives no retry time and users hammer the action repeatedly.
- Non-admin sees upgrade CTA that ends in permission denial.
- Limit resets monthly but UI shows no reset date/timezone.

## Falsification and Recovery
Falsify at 0%, near threshold, exact cap, over cap, non-admin/admin, reset boundary, offline/stale meter and multiple scopes. Attempt recovery actions under enforcement. The design fails if a user cannot identify why an action is blocked and at least one valid path to resolution when the system provides one.

Recover by formalizing limit type/scope, preserving recovery-capable actions, matching warning severity to enforcement and routing upgrade/admin/cleanup/wait paths explicitly.

## Output Contract
Return `quota-limit-contract` with limit type, scope, measure/cap, hard/soft behavior, threshold communication, reset/retry timing, blocked/remaining capabilities, recovery paths, admin delegation and boundary tests.