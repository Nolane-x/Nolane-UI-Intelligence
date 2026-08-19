---
name: designing-product-detail-purchase-decisions
description: Use when a product-detail surface must help shoppers decide whether a specific item satisfies their need through truthful identity, variant, price, availability, evidence, delivery, and risk information before purchase.
---

# Designing Product Detail Purchase Decisions

## Parent Contract
**Required parent:** `designing-commerce-checkout`.

This faculty owns the decision surface between catalog consideration and cart/checkout commitment. It does not own variant mechanics in depth, cart persistence, or final transaction review. Its job is to make the currently purchasable proposition understandable: exactly what item/configuration is being considered, at what commercial terms, with what evidence and constraints.

## Decision Architecture
Establish canonical product identity before merchandising. Title, media, seller/brand where material, model/specification, and selected configuration must describe the same purchasable unit. Media should correspond to the active variant when the difference matters; a red product image beside a hidden blue selection is a decision-integrity failure.

Price requires scope. Distinguish unit price, variant range, sale versus reference price, subscription/recurring terms, taxes/fees disclosed later by policy, quantity breaks, and region/currency differences. Do not present urgency, stock scarcity, ratings, or social proof without evidence. If delivery timing materially affects the decision, show the destination assumptions and freshness rather than a generic “fast shipping” claim.

Information hierarchy should answer the user’s highest-risk questions before secondary persuasion. Compatibility, dimensions, ingredients, return restrictions, warranty, included/excluded items, or safety constraints may deserve priority depending on domain. Reviews and recommendations are supporting evidence, not substitutes for factual product specifications.

## Failure Topology
- Hero media and selected variant describe different SKUs.
- A struck-through reference price is shown without a legitimate basis or time context.
- “Only 2 left” persists after inventory changes and creates false urgency.
- Delivery estimate appears precise while destination has not been established.
- Critical compatibility limitation is buried below promotional content.
- Add-to-cart button remains active although the selected configuration is unavailable.

## Falsification and Recovery
Falsify with variant changes, regional price differences, low/unknown inventory, delayed availability refresh, destination change, out-of-stock selected option, long technical specifications, accessible media alternatives, mobile sticky purchase controls, and a product whose return policy differs from the catalog norm. The design fails if the active purchase control can commit an item whose visible identity, terms, or availability are internally inconsistent.

Recover by binding visible product facts to one selected purchasable unit, labeling price scope, sourcing scarcity and ratings from verifiable data, recalculating delivery from actual destination context, elevating domain-critical constraints, and disabling commitment when required selection or inventory evidence is unresolved.

## Output Contract
Return `product-purchase-decision-contract` with purchasable identity, media/configuration binding, commercial term hierarchy, availability evidence, delivery assumptions, domain-critical facts, review/social-proof boundaries, commitment eligibility, responsive purchase controls, accessibility requirements, and falsification cases.