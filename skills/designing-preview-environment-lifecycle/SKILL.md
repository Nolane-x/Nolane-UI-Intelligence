---
name: designing-preview-environment-lifecycle
description: Own ephemeral preview environment creation, readiness, identity, sharing, data policy, refresh, expiry, ownership, failure, and cleanup linked to a change or branch.
---
# Designing Preview Environment Lifecycle

## Decision ownership

Own ephemeral environments used to review a change before merge/release. Decide creation trigger, linkage to source change, readiness, URL/access, data seed, secrets policy, refresh/rebuild, owner, expiry, failure, and cleanup. This owner is not generic environment management because ephemerality and source-change coupling dominate the lifecycle.

## Inputs and evidence

Require source PR/branch identity, provisioning status, environment URL, data source, access control, secrets policy, resource cost/quota, rebuild triggers, TTL, ownership, and teardown behavior. Identify whether previews can trigger external integrations or contain production-like data.

## Procedure

Bind every preview to the exact source revision it represents and show when it is stale relative to the branch/PR. Creation states should distinguish queued, provisioning, seeding, ready, failed, expired, and deleting. Share links need access context and expiry. Data policy must be explicit—synthetic, sanitized snapshot, or other authorized source—and external side effects disabled or clearly bounded. Rebuild/refresh should show what state is reset. Auto-expiry needs countdown/extension rules and reliable cleanup confirmation.

## Failure topology

Failures include preview URL serving an old revision, failed provisioning appearing as merely slow, sensitive data copied without disclosure, orphaned environments consuming resources, stale shared links, deleting while reviewers are active with no warning, and branch update not invalidating readiness. Another failure is preview systems able to send real emails/payments/webhooks unintentionally.

## Falsification

Reject if source revision cannot be identified from the preview; if stale preview looks current; if data origin/side-effect policy is unknown; if expiry/cleanup is invisible; if a failed teardown still appears deleted; if access scope is ambiguous; or if external integrations can fire with production consequence without explicit sandbox controls.

## Output contract

Return a `preview-environment-lifecycle-contract` with: source revision linkage; lifecycle states; readiness/staleness; URL/access; data origin; side-effect restrictions; rebuild/reset semantics; owner; resource/quota cue; TTL/extension; teardown verification; and failure recovery. Include one stale-preview and one failed-cleanup case.

## Handoffs

Environment management supplies infrastructure metadata, deployment pipelines create/update the preview, link sharing governs recipient access, and security/privacy owners govern data/secrets exposure.