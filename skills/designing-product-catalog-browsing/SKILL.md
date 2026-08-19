---
name: designing-product-catalog-browsing
description: Use when commerce users browse a product assortment and the interface must support category orientation, comparison, availability cues, price context, density, and return position before a specific item decision.
---

# Designing Product Catalog Browsing

## Parent Contract
**Required parent:** `designing-commerce-checkout`.

This faculty owns assortment exploration before a specific product is selected. It does not own checkout, product-detail persuasion, or generic search infrastructure. The core problem is helping users construct and refine a consideration set while keeping commercial facts such as price and availability truthful enough to compare.

## Decision Model
Choose catalog organization from the merchandise and user task: categories, collections, use cases, brands, compatibility, recency, or another domain-native structure. Do not reproduce an internal inventory taxonomy when shoppers think in different terms. Browsing and search may converge on the same listing component, but the origin and active scope should remain visible.

Define the product card as a comparison instrument. Show only attributes needed to decide whether to inspect the item: recognizable identity, representative media, current price or price range with conditions, variant/availability summary, rating evidence when legitimate, and key differentiators. Do not overload cards with every product-detail field or hide material price qualifiers behind hover.

List state matters. Filters, sort, view density, pagination/continuation, and scroll position should survive a product-detail detour. Availability and price can change while browsing; update without reordering the list under the user unless the selected sort genuinely requires it, and disclose stale/approximate values when backend freshness is bounded.

## Failure Topology
- Categories mirror warehouse codes and shoppers cannot predict where products live.
- Cards show a low “from” price while the pictured/default variant is materially more expensive with no qualifier.
- Returning from product detail resets filters and scroll to the catalog top.
- Inventory updates reorder cards continuously while the user compares them.
- Hover reveals the only variant/availability information, making touch and keyboard use incomplete.
- Sponsored products are blended into relevance/merchandising order without disclosure.

## Falsification and Recovery
Falsify with large assortments, long localized titles, mixed in-stock/out-of-stock variants, price ranges, sale pricing, sponsored placements, mobile grid/list transformations, browser Back, permission/region-dependent assortment, keyboard/screen-reader navigation, and a product removed while visible. The design fails if a catalog card omits information necessary to understand the commercial comparison or if normal detail exploration destroys the consideration-set state.

Recover by using shopper-facing taxonomy, defining a bounded comparison schema, qualifying variable prices, preserving listing state, stabilizing updates, disclosing promotion, and treating availability/price freshness as explicit data evidence.

## Output Contract
Return `product-catalog-browsing-contract` with browse taxonomy, listing scope, card comparison schema, commercial fact qualifiers, filters/sort handoff, state restoration, availability/price freshness, sponsored-content treatment, responsive density, accessibility behavior, and falsification cases.