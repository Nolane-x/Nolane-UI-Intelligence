---
name: designing-order-tracking
description: Use when customers need post-purchase visibility into fulfillment progress and the interface must translate multiple logistics events into trustworthy order, shipment, item, delivery, exception, and support states.
---

# Designing Order Tracking

## Parent Contract
**Required parent:** `designing-commerce-checkout`.

This faculty owns post-order fulfillment visibility. It does not own carrier operations or return/refund workflows. Its job is to reconcile order-level and shipment-level evidence into a customer-readable status without inventing precision or collapsing split shipments and exceptions into one cheerful progress bar.

## Decision Model
Separate commercial order state from fulfillment state. Paid, processing, partially shipped, shipped, out for delivery, delivered, delayed, pickup ready, cancelled, and returned may be derived from several item/parcel records. A multi-item order can be partly delivered while another item is backordered; the UI must preserve that decomposition rather than choosing one misleading global label.

Timeline events need source and freshness. Carrier scans can arrive late, duplicate, or out of order. Display customer-relevant milestones and exception messages, not every raw logistics code. Estimated delivery is distinct from confirmed appointment or delivered evidence. If a carrier page is linked, keep the product's own order context so users can return easily.

Tracking should expose actionable exceptions: address problem, missed delivery, pickup deadline, customs requirement, damaged/lost investigation, or seller delay. Support escalation should carry order/shipment identity without requiring users to copy long IDs manually. Privacy-safe tracking links should not leak full personal details to anyone who obtains the URL.

## Failure Topology
- Order shows “Delivered” because one of three packages arrived.
- Carrier sends an older scan after a newer event and the visible timeline appears to move backward.
- Exact delivery time is shown from a broad estimated window.
- Raw carrier code such as `EXC_17` is exposed with no customer meaning.
- Tracking page reveals recipient name/address from an unauthenticated guessable URL.
- Exception state says “Delayed” but provides no affected package, next expectation, or support path.

## Falsification and Recovery
Falsify with split shipments, partial cancellation, backorder, duplicate/out-of-order carrier events, delivery estimate changes, pickup order, missing scan, delivered-but-not-received report, guest tracking, screen-reader timeline, and a return initiated after delivery. The design fails if a global status contradicts any material item/shipment state or if estimated and confirmed milestones are indistinguishable.

Recover by modeling order/item/shipment hierarchy, normalizing source events into customer milestones, ordering by authoritative event semantics, labeling estimates, exposing exception actions, protecting guest tracking tokens, and handing post-delivery return actions to the return/refund owner.

## Output Contract
Return `order-tracking-contract` with order/item/shipment hierarchy, normalized milestone states, event-source/freshness rules, estimate semantics, split-shipment representation, exception actions, support handoff, guest/privacy policy, accessibility timeline, and falsification cases.