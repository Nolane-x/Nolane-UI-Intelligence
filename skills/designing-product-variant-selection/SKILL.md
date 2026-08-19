---
name: designing-product-variant-selection
description: Use when a purchasable product has option combinations and the UI must express availability, dependency, identity, media, price, and impossible combinations without making shoppers guess which configuration they are buying.
---

# Designing Product Variant Selection

## Parent Contract
**Required parent:** `designing-commerce-checkout`.

This faculty owns selection of the exact sellable configuration—size, color, capacity, material, bundle, term, or another option set. It does not own general dependent form fields: variant options are constrained by a product matrix where combinations map to purchasable SKU identity, price, media, inventory, and delivery consequences.

## Decision Model
Model the variant matrix explicitly. Each selection state should distinguish available, unavailable under current choices, globally unavailable, low inventory when evidence exists, and not-yet-specified. Disable impossible choices only when users can still understand why; hiding unavailable values can make shoppers think a product never offered that option or prevent them from discovering a configuration by changing an earlier selection.

Decide selection order based on dependency and shopper intent. If color determines which sizes exist, update size availability after color selection without silently replacing a previously chosen size. When a combination becomes invalid, either preserve the incompatible choice with a clear conflict or reset it with an explicit explanation. Auto-selecting the first available variant is acceptable only when it cannot create surprise about price, media, or commitment.

Every valid combination must update the commercial representation consistently: SKU/product identity, price, media, stock, delivery, URL when deep linking is supported, and Add-to-cart eligibility. Swatches need text names and non-color cues; size values need domain-appropriate labels rather than unexplained codes.

## Failure Topology
- Selecting color silently changes size to the first available value and alters the item without notice.
- Unavailable options disappear, so users cannot understand whether another choice would make them available.
- Image updates to blue while hidden selected swatch remains red due to async race.
- Price changes with variant but sticky mobile purchase bar retains the old amount.
- Color swatches have no accessible names and identical colors cannot be distinguished.
- URL points to a product but not its selected configuration, so sharing loses the intended variant.

## Falsification and Recovery
Falsify with sparse variant matrices, out-of-stock combinations, asynchronous inventory refresh, deep-linked configuration, rapid option switching, mobile sticky controls, keyboard/screen-reader selection, colors with similar appearance, and a variant whose price/delivery differs materially. The design fails if the visible configuration cannot resolve to exactly one purchasable identity or if async updates can combine facts from different variants.

Recover by using one canonical selection state, matrix-derived option availability, revision-safe async updates, explicit invalidation/reset semantics, synchronized commercial facts, accessible option names, and configuration-aware deep links where supported.

## Output Contract
Return `product-variant-selection-contract` with option dimensions, variant matrix, availability states, selection/invalidation rules, auto-selection policy, SKU identity resolution, synchronized price/media/stock/delivery facts, deep-link semantics, accessibility treatment, and falsification cases.