---
name: designing-shopping-carts
description: Use when shoppers collect one or more purchasable items before checkout and the interface must reconcile quantity, variant identity, price changes, inventory changes, saved state, removal, and order-summary truth.
---

# Designing Shopping Carts

## Parent Contract
**Required parent:** `designing-commerce-checkout`.

This faculty owns pre-checkout collection state. A cart is not merely a list of product cards; it is a mutable commercial draft whose item identities, quantities, prices, promotions, availability, and fulfillment assumptions can change between addition and checkout. Final payment authorization remains outside this skill.

## Decision Architecture
Represent every line with canonical purchasable identity, selected variant, quantity, unit price evidence, applicable promotion state, and availability. Editing quantity or variant must recompute dependent totals from authoritative pricing rules rather than arithmetic performed only in the client. If taxes, shipping, or fees are not yet known, label subtotal versus estimated total honestly.

Persistence needs a declared scope: browser session, signed-in account, server cart, or merge between anonymous and authenticated state. Login should not silently discard either cart; define merge rules for duplicate SKUs, quantities, incompatible currencies, and items unavailable in the account’s region. Saved-for-later is a different intent state from cart and should not count toward checkout totals or inventory reservation unless policy explicitly says otherwise.

Changes after add-to-cart require reconciliation. Price changes, expired promotions, low stock, discontinued variants, purchase limits, or seller changes should be surfaced at the affected line before checkout commitment. Removal may offer Undo when technically reversible, but the UI must not imply inventory is reserved simply because an item remains in cart.

## Failure Topology
- Anonymous cart disappears on sign-in despite valid items in both states.
- Quantity update optimistically changes total, server rejects purchase limit, and UI keeps the wrong total.
- “Total” excludes known mandatory fees but is visually presented as final.
- Out-of-stock item remains selectable at checkout and failure appears only after address/payment entry.
- Saved-for-later items remain included in item count or promotional threshold.
- Cart shows old sale price after promotion expiration with no line-level reconciliation.

## Falsification and Recovery
Falsify with login/cart merge, duplicate variants, quantity limits, price change, promotion expiry, regional currency change, inventory loss, browser refresh, cross-device cart, keyboard/screen-reader quantity editing, and an item removed then undone. The design fails if the visible cart cannot be reconciled to authoritative line-level commercial state or if totals claim certainty beyond known costs.

Recover by maintaining canonical line IDs, server-authoritative recomputation, explicit cart-merge rules, separating saved intent from active cart, surfacing line-specific changes before commitment, and distinguishing subtotal/estimate/final totals by evidence.

## Output Contract
Return `shopping-cart-contract` with cart persistence scope, line identity, quantity/variant mutation, pricing recomputation, anonymous/account merge rules, saved-for-later separation, inventory/promotion reconciliation, subtotal/estimate semantics, removal/Undo, accessibility controls, and falsification cases.