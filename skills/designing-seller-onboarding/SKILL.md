---
name: designing-seller-onboarding
description: Use when a marketplace must admit sellers through business identity, policy acceptance, payout setup, tax or regulatory data, catalog readiness, verification, and activation states without conflating account creation with selling eligibility.
---

# Designing Seller Onboarding

Seller onboarding establishes whether an account may transact on behalf of a merchant. It combines identity, business verification, payout readiness, policy acceptance, and operational setup; merely creating credentials is not sufficient.

## Parent Contract
**Required parent:** `designing-marketplace-operations`.

The parent defines multi-party marketplace operations. This skill owns seller admission and activation state from initial intent through verified, restricted, active, or rejected seller status.

## Admission State
Separate account state from seller state. Useful seller lifecycle states may include draft, information incomplete, verification pending, action required, payout setup incomplete, approved but not activated, active, restricted, suspended, and rejected. Never render “profile complete” as “ready to sell” unless all required gates have passed.

Collect business/legal identity, beneficial-owner or representative data, tax information, payout destination, return/fulfillment settings, prohibited-category declarations, and policy acceptance only where the marketplace actually requires them. Explain why high-sensitivity data are requested and which provider processes them.

## Progressive Verification
External verification often completes asynchronously. Preserve submitted evidence and expose which check is pending rather than restarting the wizard. A verification failure should distinguish data mismatch, unsupported document, expired evidence, provider outage, and policy ineligibility. Do not label every failure “identity could not be verified.”

Activation may depend on catalog or fulfillment readiness. If sellers can prepare listings before final verification, clearly mark drafts as non-live and block publish/transaction actions until activation.

## Evidence
Test individual/business variants, verification pending, requested resubmission, payout account failure, policy rejection, interrupted return, external provider outage, seller approved while catalog incomplete, and later suspension. Verify capability checks rather than only step completion.

## Failure Modes
- Account signup success appears as marketplace approval.
- Verification retry loses previously accepted data.
- External provider outage is presented as seller ineligibility.
- Sensitive business data are requested without reason or privacy boundary.
- Draft listings accidentally become purchasable before seller activation.
- Seller is “active” while payout destination is invalid and policy requires it.

## Falsification
Approve identity but intentionally fail payout readiness, then create a listing. Falsify if the UI lets the seller transact despite an unmet hard gate or if the seller cannot tell which verification dependency remains unresolved.

## Recovery
Recompute seller capability from authoritative gates, preserve verified steps, isolate external technical failure from eligibility, and provide targeted resubmission. If platform policy is the blocker, state the policy outcome and review route where available.

## Handoff
Listing creation/moderation belongs to `designing-listing-moderation-workflows`; payout lifecycle to `designing-marketplace-payout-status`; trust badges shown to buyers require `designing-marketplace-trust-signals`.

## Output Contract
Return a `seller-onboarding-contract` with `seller_states[]`, `admission_gates[]`, `sensitive_data_rationale`, `verification_dependencies[]`, `failure_taxonomy`, `draft_capability_policy`, `activation_rules`, `evidence_cases[]`, `falsification_cases[]`, and `recovery_actions[]`.