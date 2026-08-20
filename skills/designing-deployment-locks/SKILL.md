---
name: designing-deployment-locks
description: Use when this specialist's decision ownership is materially in scope. Own temporary deployment locks on targets or release paths, including owner, reason, scope, expiry, override authority, visibility, and stale-lock recovery.
---
# Designing Deployment Locks

## Parent Contract

**Required parent:** `designing-software-delivery-pipelines`.

Inherit the broader routing and decision boundary from this canonical parent; this specialist remains accountable only for the narrower ownership, failure topology, falsification criteria, and output contract defined below.

## Decision ownership

Own explicit lock state that prevents or restricts deployments. Decide lock scope, actor/owner, rationale, duration/expiry, affected actions, override/break-glass policy, inheritance, and stale-lock cleanup. A lock differs from a broad change freeze because it may target one environment, service, or deployment path.

## Inputs and evidence

Require target hierarchy, lock policy, who may create/remove/override, default duration, incident/maintenance linkage, deployment actions affected, notification, and audit. Identify automated locks created by incidents or safety systems.

## Procedure

Show lock state wherever a user chooses or acts on the affected target, not only in settings. A lock needs clear scope, reason, owner/source, created time, expiry/review, and actions blocked. Inherited locks should explain the parent source. Overrides require explicit authority, reason, and consequence and should not silently delete the original lock. Expired/stale locks need automated or review-driven cleanup while preserving history. Automated locks must identify triggering system/incident and how they release.

## Failure topology

Failures include deployment failing late with no visible lock, indefinite abandoned locks, users removing a lock they do not understand, inherited lock sources hidden, break-glass acting like normal unlock, and automated locks that never clear after trigger recovery. Another failure is lock UI using the same "disabled" appearance as lack of permission with no explanation.

## Falsification

Reject if an affected deployment target can appear fully available; if lock scope/reason/owner are unknown; if locks have no expiry/review policy; if override lacks audit/rationale; if inherited source cannot be traced; or if automated lock release criteria are opaque.

## Output contract

Return a `deployment-locks-contract` with: lock scope; blocked actions; owner/source; rationale; creation/expiry; inheritance; visibility points; override authority/reason; automated trigger/release; stale cleanup; and history. Include one inherited lock and one break-glass override.

## Handoffs

Target selection consumes lock state, incident/maintenance may create locks, change freezes provide broader policy windows, and generic permissions remain separate from lock state.