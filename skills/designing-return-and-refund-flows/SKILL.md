---
name: designing-return-and-refund-flows
description: Use when customers reverse or dispute a completed purchase and the interface must coordinate eligibility, item selection, reason, return logistics, refund destination, timing, partial outcomes, and irreversible checkpoints.
---

# Designing Return and Refund Flows

## Parent Contract
**Required parent:** `designing-financial-transaction-ui`.

This faculty owns post-purchase reversal from customer intent through return/refund resolution. It does not set legal return rights or merchant policy independently; current jurisdiction, merchant rules, payment method, item condition, and fulfillment state are authorities that must be verified when material.

## Decision Architecture
Start by establishing eligible order items and their current states. A return can be item-level, quantity-level, shipment-level, or entire-order. Show why an item is eligible, conditionally eligible, or ineligible without inventing rights beyond policy. If a return window or fee applies, expose the basis and consequence before the customer commits.

Separate physical return from financial refund. The product may require drop-off, pickup, label printing, QR code, in-store return, no-return refund, or inspection. Refund destination may be original payment method, store credit, split tender, or another policy-authorized route. Do not show “Refunded” when the merchant merely approved the request; preserve requested, authorized, item-in-transit, received, inspected, refund initiated, and refund settled/expected states as evidence allows.

Partial outcomes are normal. One item can be accepted and another rejected; shipping fees may be non-refundable; refund amounts can differ after discounts or tax adjustments. Present a line-level calculation and preserve reason/evidence when customers need support or appeal.

## Failure Topology
- Flow lets users select an item already refunded or returned.
- “Refund complete” appears when funds have only been submitted to a payment processor.
- Customer learns about a restocking fee only after generating the return label.
- Partial refund is summarized as the original order total and creates false expectation.
- Cancelling a return after carrier acceptance is offered even though the process is irreversible.
- Policy denial gives only “Not eligible” with no relevant reason or support path.

## Falsification and Recovery
Falsify with partial quantities, mixed eligible/ineligible items, discounted bundles, split payment, no-return refund, pickup/drop-off, damaged item evidence, return cancelled before/after logistics handoff, payment-method expiry, and a refund that takes days to settle. The design fails if physical-return and financial-refund states are conflated or if the displayed amount cannot be reconciled to the original transaction and policy adjustments.

Recover by binding return units to order lines, sourcing eligibility and fee rules authoritatively, separating logistics/refund timelines, showing line-level amounts, defining irreversible checkpoints, and preserving escalation evidence for disputed outcomes.

## Output Contract
Return `return-refund-flow-contract` with eligible units, policy authority, reason/evidence model, return logistics, refund destination, amount calculation, lifecycle states, partial outcomes, cancellation boundaries, support/appeal handoff, accessibility behavior, and falsification cases.