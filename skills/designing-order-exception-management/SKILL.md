---
name: designing-order-exception-management
description: Use when marketplace orders encounter seller rejection, inventory loss, address issues, payment problems, carrier failures, cancellations, return conflicts, or other exceptions that require scoped resolution across parties.
---

# Designing Order Exception Management

An exception is a divergence from the expected order path that needs ownership, evidence, and a bounded resolution. Marketplace exceptions are especially complex because platform, seller, buyer, carrier, and payment provider may each control different recovery actions.

## Parent Contract
**Required parent:** `designing-marketplace-operations`.

The parent owns multi-party order state. This skill owns exception detection, classification, ownership, actionability, and resolution history after order creation.

## Exception Taxonomy
Classify by the failed promise: seller cannot fulfill, inventory unavailable, payment capture/authorization issue, invalid address, carrier lost/delayed, buyer cancellation request, item damaged/not as described, return missing, refund failed, or platform policy hold. Avoid a universal “order problem” state because recovery authority differs by class.

Bind each exception to the affected suborder/item/shipment/payment, not automatically the whole marketplace order. One seller's stock loss should not freeze unrelated seller shipments unless policy requires coordinated action.

## Ownership and SLA
Show who can act next and any authoritative deadline: buyer response needed, seller must choose substitution/refund, platform review pending, carrier investigation open. Internal queues may need priority and ageing; buyer/seller surfaces need understandable expectation rather than internal SLA codes.

Resolution options should display consequences before commit—refund amount, shipping delay, seller change, item cancellation, or evidence request. Preserve every transition so support agents can reconstruct what was offered and accepted.

## Evidence
Test partial seller rejection, address correction, shipment loss, refund processor failure, user responding after deadline, duplicate exception events, and two simultaneous exceptions on different items. Verify actions are scoped to the correct order component.

## Failure Modes
- Exception on one item blocks the whole order without policy reason.
- Responsibility is hidden behind “we're working on it.”
- Buyer is asked to act after the response deadline passed.
- Seller can choose a replacement that changes material terms without buyer consent.
- Refund failure is shown as refund complete.
- Duplicate exception events create duplicate customer actions.

## Falsification
Create an order with two sellers, fail one seller's inventory and one carrier shipment independently. Falsify if the interface merges them into one opaque problem or lets resolving one exception mark the other resolved.

## Recovery
Re-scope exceptions to their affected entities, deduplicate by canonical exception identity, restore explicit owner/deadline, and query payment/fulfillment state before claiming resolution. If authority is unclear, pause consequential action and escalate rather than guessing the responsible party.

## Handoff
Shipment topology belongs to `designing-split-fulfillment-shipments`; formal buyer-seller claims to `designing-marketplace-dispute-resolution`; payment-to-seller consequences to `designing-marketplace-payout-status`.

## Output Contract
Return an `order-exception-management-contract` with `exception_classes[]`, `affected_entity_binding`, `responsibility_map`, `deadline_semantics`, `resolution_options[]`, `consequence_preview`, `deduplication_rules`, `audit_history`, `evidence_cases[]`, and `recovery_actions[]`.