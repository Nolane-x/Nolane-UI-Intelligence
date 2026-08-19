---
name: designing-shipping-method-selection
description: Use when a purchase offers multiple fulfillment methods and the interface must compare destination eligibility, delivery estimate, price, carrier/service, pickup constraints, and freshness without presenting uncertain logistics as guaranteed.
---

# Designing Shipping Method Selection

## Parent Contract
**Required parent:** `designing-commerce-checkout`.

This faculty owns choosing among fulfillment options after enough destination and cart context exists. It does not own address entry, carrier operations, or order tracking. Its obligation is to make the alternatives comparable and to show which assumptions make each option available.

## Decision Model
Resolve method eligibility from the actual cart and destination. Home delivery, express, pickup, locker, scheduled delivery, freight, or digital fulfillment may have different geographic, item, quantity, age, or inventory constraints. Do not show an option as selectable and only explain incompatibility after the user commits it.

Compare on meaningful dimensions: price, estimated arrival/window, destination/pickup location, service level, and material conditions. Delivery dates are estimates unless the logistics system provides a guaranteed service; labels should preserve that distinction. If the estimate changes with cut-off time, inventory source, or current time, make freshness and assumptions clear enough to avoid false precision.

Changing fulfillment may alter taxes, discounts, inventory allocation, or total price. Recalculate those consequences before marking the stage complete. Pickup requires location identity, hours, readiness semantics, and perhaps a person authorized to collect; it is not simply “free shipping.”

## Failure Topology
- Express method remains available after an item changes to a seller/location that cannot support it.
- “Arrives Tuesday” is displayed as a guarantee although the source provides only an estimate.
- Switching to pickup removes shipping fee but stale order total remains visible elsewhere.
- Pickup option shows store name but not address or hours, creating an unusable selection.
- Method automatically changes after address edit with no explanation.
- Cheapest option is visually preselected even when it has a materially later delivery window.

## Falsification and Recovery
Falsify with multi-item carts from different fulfillment sources, address changes, cut-off time crossing during checkout, out-of-stock pickup location, remote destination, long delivery estimates, taxes changing by method, screen-reader comparison, and a method becoming unavailable after selection. The design fails if a selected method cannot be justified by current cart/destination evidence or if estimate and guarantee are visually indistinguishable.

Recover by server-authoritative eligibility, explicit estimate semantics, synchronized total recalculation, complete pickup context, visible invalidation when assumptions change, and requiring re-selection rather than silently substituting a materially different method.

## Output Contract
Return `shipping-method-selection-contract` with fulfillment types, eligibility inputs, comparison dimensions, estimate/guarantee semantics, pickup/location data, price/tax recalculation, selection invalidation, defaulting rules, accessibility comparison, and falsification cases.