---
name: designing-split-fulfillment-shipments
description: Use when one marketplace order is fulfilled through multiple sellers, warehouses, packages, carriers, pickup routes, or dates and users need item-to-shipment mapping, status, cost, and exception clarity.
---

# Designing Split Fulfillment Shipments

A single order confirmation can become several real-world fulfillment journeys. The interface must show which items belong to which shipment, who fulfills each one, and how delivery state changes independently.

## Parent Contract
**Required parent:** `designing-marketplace-operations`.

The parent owns the marketplace order. This skill owns decomposition into fulfillment groups, package/shipment identities, delivery promises, and recomposition back into an understandable order view.

## Fulfillment Graph
Represent order items → fulfillment group → package/shipment → carrier/pickup → delivery event. A seller suborder may produce multiple shipments; a shipment may contain several items. Keep those relationships stable even as packages are split or merged operationally.

Buyer-facing summaries should prioritize outcomes: which items arrive together, estimated/confirmed dates, tracking, pickup instructions, and who to contact. Seller/operations views can expose warehouse and allocation detail. Do not make buyers reason from internal fulfillment IDs.

## Cost and Promise
Shipping fees, taxes, discounts, and delivery promises can be scoped by shipment or order. Explain recalculation when a split changes. If one item becomes backordered after checkout, show how that affects only the relevant delivery promise and whether the buyer can cancel that portion.

Tracking events are carrier evidence, not guaranteed delivery truth. Distinguish label created, handed to carrier, in transit, out for delivery, delivered, pickup ready, delayed, lost, returned, and unknown. Mixed shipments should not produce one global “delivered” state while items remain outstanding.

## Evidence
Test one order split by seller and warehouse, second split after partial inventory loss, multiple tracking numbers, pickup plus shipping, partial delivery, lost package, and partial cancellation. Verify item mappings remain correct across order detail, notifications, returns, and disputes.

## Failure Modes
- Order-level status says delivered while one package is still in transit.
- Items move between shipment cards without preserving historical events.
- Tracking number appears against the wrong seller/item group.
- Shipping fee recalculation is unexplained after split.
- Partial cancellation accidentally cancels every shipment.
- Return flow asks the buyer to ship items to the wrong seller/location.

## Falsification
Split three items into two sellers and three shipments, then cancel one item and mark one package lost. Falsify if any item-to-shipment relationship becomes ambiguous or if order-level status hides the unresolved package.

## Recovery
Rebuild from canonical fulfillment entities, display per-shipment state, derive order summary conservatively, and retain historical mappings when operational splits change. Unknown carrier state should not be converted into delivered or lost without evidence.

## Handoff
Inventory/reservation belongs to `designing-marketplace-inventory-availability`; shipment failures route to `designing-order-exception-management`; disputes should reference the exact affected shipment/item through `designing-marketplace-dispute-resolution`.

## Output Contract
Return a `split-fulfillment-shipments-contract` with `fulfillment_graph`, `shipment_identity_fields`, `buyer_summary_rules`, `delivery_state_taxonomy`, `cost_scope`, `split_merge_history`, `partial_action_rules`, `evidence_cases[]`, `falsification_cases[]`, and `recovery_actions[]`.