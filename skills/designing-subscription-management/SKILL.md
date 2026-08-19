---
name: designing-subscription-management
description: Use when users manage an ongoing paid plan and the interface must make current entitlement, renewal, billing period, upgrade/downgrade timing, cancellation, trial and post-cancel consequences explicit.
---

# Designing Subscription Management

## Parent Contract
**Required parent:** `designing-commerce-checkout`.

This faculty owns the lifecycle after or around recurring purchase. It does not own card-entry checkout, invoice accounting, entitlement engine rules or legal cancellation requirements beyond faithfully surfacing authoritative policy.

## Decision Boundary
A subscription view must answer four truths independently: **what plan is active, what the user is entitled to now, what/when they will be charged next, and what scheduled change will happen later**. “Pro plan” alone is insufficient when cancellation, pending downgrade, trial or grace period changes those answers.

Model lifecycle states from product/billing truth: trialing, active, scheduled change, past due, grace period, canceled-at-period-end, canceled immediately, expired, paused or other supported states. Do not invent universal states. Bind every displayed date to a timezone and distinguish current period end from cancellation effective date and next invoice date.

Plan changes require timing semantics. Upgrade may apply immediately with proration; downgrade may be scheduled for renewal; feature removals can affect stored data, collaborators, limits or integrations. Show effective timing and material consequences before confirmation. If proration is estimated, label it as estimate and update from authoritative billing calculation before commit.

Cancellation must distinguish stopping renewal from immediate loss of access. Explain retention/export/recovery windows when authoritative. “Cancel subscription” must not visually imply account deletion unless they are intentionally linked.

Seat-based or usage-based subscriptions need current quantity source and how changes affect the bill. Do not mix organization seat administration into the payment screen without clear scope.

## Failure Topology
- Page says “Canceled” even though access continues until month end, so users assume features should stop now.
- Pending downgrade is hidden and users think current plan will renew unchanged.
- Upgrade price is shown without proration or effective-date context.
- Cancellation dialog threatens data deletion that billing policy does not actually trigger.
- Trial end, next charge and renewal are rendered as one ambiguous date.
- Organization subscription is edited while UI appears scoped to the personal account.

## Falsification and Recovery
Falsify with trial → paid, immediate upgrade, scheduled downgrade, cancellation at period end, reactivation, failed renewal, seat changes and multiple billing scopes. At every state compare visible plan, entitlement, scheduled change and charge date to billing records.

Recover by separating current vs future state, exposing effective dates, retrieving authoritative price/proration, and routing data-loss/account-lifecycle consequences to their actual owners.

## Output Contract
Return `subscription-management-contract` with billing scope, lifecycle state model, current entitlement, renewal/charge dates, scheduled plan changes, upgrade/downgrade timing, cancellation/reactivation semantics, consequence disclosure and billing-state parity tests.