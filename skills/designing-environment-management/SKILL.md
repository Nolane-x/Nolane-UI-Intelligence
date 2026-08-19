---
name: designing-environment-management
description: Use when developers operate multiple deployment or runtime contexts and the interface must preserve environment identity, configuration differences, promotion boundaries, production risk, switching, and stale-context protection.
---

# Designing Environment Management

## Parent Contract
**Required parent:** `designing-organization-administration`.

This faculty owns operational context such as development, preview, staging, sandbox, production, region-specific, or tenant-specific environments. It does not own feature-flag evaluation or secret values. Its central job is to make “where will this action happen?” difficult to overlook and to prevent stale context from silently crossing environment boundaries.

## Decision Architecture
Define environment identity through stable ID plus human label, purpose, region/tenant, endpoint/deployment evidence, and risk class. Color can reinforce production versus non-production, but never rely on color alone. The active environment should remain visible on every surface where an action, query, credential, flag, webhook, migration, or data view could have materially different consequences.

Switching is a context transition, not a cosmetic dropdown. Decide which local state can survive: search terms may transfer, selected object IDs may not exist, unsaved edits may target a different schema, and cached data must not be mistaken for the new environment. Prefer clearing or revalidating environment-bound selections over carrying them optimistically.

Configuration comparison can help operators understand drift, but absence does not imply error—staging and production may intentionally differ. Promotion/copy actions need explicit source and destination identities, a change summary, current destination revision, and consequence review. Production mutation may require stronger permission or confirmation without making routine read-only inspection cumbersome.

## Failure Topology
- Environment selector says “Prod” only in a tiny colored dot and is missed by color-deficient users.
- Switching from staging preserves selected resource ID and destructive action targets a different production object with the same ID.
- Cached staging metrics remain visible under a production header during loading.
- “Copy config to production” hides which fields will overwrite existing destination values.
- Two tabs have different environments but share one global client store and leak data across contexts.
- Browser Back restores a URL from another environment without revalidating active context.

## Falsification and Recovery
Falsify with rapid environment switching, identical object IDs across contexts, multiple tabs, production read/write permission differences, stale caches, deployment revision changes, source→destination promotion, region-specific environment, keyboard/screen-reader switching, and deep links containing environment identity. The design fails if an operation can execute without a recoverable environment binding or if data from one environment can appear as current in another.

Recover by including environment ID in routing/cache/request keys, visibly labeling context, invalidating environment-bound selections, segregating tab/session state where necessary, previewing promotions, verifying destination revision, and applying risk friction only to consequence-bearing mutations.

## Output Contract
Return `environment-management-contract` with environment identity, risk/context presentation, switch semantics, state/cache invalidation, routing/deep-link binding, cross-tab isolation, permission differences, configuration comparison/promotion, production mutation safeguards, and falsification cases.