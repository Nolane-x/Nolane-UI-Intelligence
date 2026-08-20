---
name: designing-marketplace-operations
description: Use when a marketplace coordinates buyers, sellers, listings, inventory, orders, fulfillment, disputes, payouts, messaging, and trust signals across multiple parties with different rights and obligations.
---

# Designing Marketplace Operations

A marketplace is not a single-store checkout with more products. It coordinates independent actors whose inventory, fulfillment, payment, moderation, communication, and dispute states can diverge while still appearing inside one customer journey.

## Parent Contract
**Required parent:** `designing-commerce-checkout`.

Inherit commerce transaction clarity, but do not assume one merchant owns the entire order. This skill owns the marketplace-level operating model and routes seller/listing/inventory/order/dispute/payout/trust decisions to specialized owners.

## Multi-Party State Model
Declare the entities that can change independently: buyer, seller, listing, offer/variant, inventory location, marketplace order, seller suborder, shipment, payment, fee, payout, dispute, moderation case, and message thread. Show which party owns the next action and which state is platform-controlled.

Separate buyer-facing order identity from seller fulfillment identities. One checkout may create several fulfillment groups with different carriers, cancellation rights, return addresses, and delivery dates. The interface should preserve the relationship without forcing buyers to understand internal merchant identifiers.

## Authority and Responsibility
Make platform, seller, carrier, and payment-provider responsibility visible where it changes user options. A delivery delay caused by one seller should not render the entire order as failed. A platform moderation hold should not masquerade as “seller processing.”

Marketplace policies—fees, returns, protection, prohibited items, dispute windows, payout holds—must be surfaced at decision moments and bound to the actual transaction/listing state. Do not use trust language that exceeds the evidence the platform can verify.

## Evidence
Test mixed-seller checkout, partial cancellation, split shipment, seller inventory loss, disputed item, refund before payout, payout hold, moderated listing, seller suspension, and buyer-seller message escalation. Verify each surface against authoritative party/state ownership.

## Failure Modes
- A marketplace order is treated as one indivisible fulfillment.
- Seller and platform responsibilities are visually indistinguishable.
- One failed seller item marks all items failed.
- Buyer cancellation is offered after a seller-specific irreversible state.
- Platform protection language implies guarantees not encoded in policy.
- Payout/refund timing is hidden from sellers after buyer resolution.

## Falsification
Create one order spanning two sellers, then cancel one item, delay another shipment, and open a dispute. Falsify if the buyer or seller cannot identify which suborder/state each action affects or if a platform-controlled hold is attributed to the wrong party.

## Recovery
Reconstruct the transaction as party-owned subgraphs, surface responsibility, rebind actions to the correct suborder/listing/dispute, and preserve cross-party audit events. Unknown ownership blocks consequential action rather than defaulting to the platform or seller.

## Handoff
Seller lifecycle routes to `designing-seller-onboarding`; listing policy to `designing-listing-moderation-workflows`; inventory to marketplace inventory; exceptions/fulfillment/disputes/payout/trust route to their respective owners.

## Output Contract
Return a `marketplace-operations-contract` with `marketplace_entities[]`, `party_ownership_map`, `order_subgraph`, `responsibility_rules`, `policy_bindings[]`, `cross_party_actions[]`, `audit_events[]`, `evidence_cases[]`, `falsification_cases[]`, and `recovery_actions[]`.