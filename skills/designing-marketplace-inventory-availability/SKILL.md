---
name: designing-marketplace-inventory-availability
description: Use when marketplace stock comes from independent sellers, locations, reservations, offers, or fulfillment channels and the interface must communicate sellable availability, scarcity, reservation, substitution, and oversell risk accurately.
---

# Designing Marketplace Inventory Availability

Marketplace availability is an offer-level promise, not just a stock counter. Different sellers may hold the same catalog item with separate quantities, locations, lead times, fulfillment capabilities, and reservation rules.

## Parent Contract
**Required parent:** `designing-marketplace-operations`.

The parent defines marketplace entities. This skill owns availability semantics from seller offer through reservation and fulfillment commitment.

## Availability Layers
Distinguish catalog existence, seller offer active state, physical/on-hand stock, reserved quantity, sellable quantity, inbound expected stock, and channel-specific availability. A positive warehouse quantity does not guarantee the marketplace offer can be sold if the seller is suspended, the location cannot ship to the buyer, or stock is fully reserved.

For multi-location sellers, decide whether buyers need location detail or only delivery promise. Sellers, however, may need to see allocation source and reservation state. Do not expose operational complexity to buyers unless it changes choice or confidence.

## Reservation and Concurrency
Inventory can change between browse, cart, checkout, and order acceptance. Communicate the strongest promise the system can actually make. “Only 1 left” must come from current sellable evidence, not synthetic urgency. If checkout reserves stock, show the reservation window only when authoritative and define expiry behavior.

Oversell recovery should preserve order context and offer alternatives—different seller, quantity adjustment, substitution, backorder, or refund—according to platform policy. Do not silently move a buyer to a different seller with different terms.

## Evidence
Test two sellers for one product, low stock, simultaneous buyers, reservation expiry, location exclusion, seller suspension, inbound/backorder, partial quantity, and stock becoming unavailable after payment authorization. Verify seller and buyer surfaces against the same reservation events.

## Failure Modes
- Catalog stock is shown as seller-specific sellable stock.
- Scarcity language is generated without inventory evidence.
- Cart state appears guaranteed when no reservation exists.
- Expired reservation remains visually held.
- Oversell recovery silently changes seller or price.
- Seller UI cannot distinguish on-hand from reserved quantity.

## Falsification
Have two buyers attempt the last unit concurrently. Falsify if both see an unqualified confirmed availability beyond the reservation/commit point, or if one order is moved to another seller without explicit acceptance.

## Recovery
Recompute sellable quantity from authoritative offer/location/reservation state, invalidate expired holds, and present bounded alternatives preserving seller/price/terms. Unknown inventory synchronization should reduce promise strength rather than invent certainty.

## Handoff
Split fulfillment routes to `designing-split-fulfillment-shipments`; order-level failure after commit to `designing-order-exception-management`; trust copy must not transform stock evidence into manipulative urgency.

## Output Contract
Return a `marketplace-inventory-availability-contract` with `availability_layers[]`, `sellable_formula`, `location_rules`, `reservation_semantics`, `promise_strength`, `concurrency_cases[]`, `oversell_recovery`, `seller_buyer_views`, `evidence_cases[]`, and `recovery_actions[]`.