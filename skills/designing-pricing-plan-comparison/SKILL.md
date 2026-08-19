---
name: designing-pricing-plan-comparison
description: Use when users compare commercial plans or tiers and the interface must align price basis, billing cadence, included limits, feature differences and eligibility without manipulating comparison through inconsistent units or hidden caveats.
---

# Designing Pricing Plan Comparison

## Parent Contract
**Required parent:** `designing-commerce-checkout`.

This faculty owns the decision interface before choosing a plan. It does not set prices, write contractual terms or authorize marketing claims.

## Decision Boundary
Normalize comparison dimensions before visual hierarchy. Price must identify currency, tax posture where applicable, billing cadence, unit (`per user`, `per workspace`, `per 1K events`) and minimum commitments. A monthly equivalent of an annual plan is not the same as month-to-month billing; disclose the actual charge cadence near the prominent price.

Feature comparison should use semantic capabilities, not marketing adjectives. Group features by decision task and explain limit values/conditions. “Unlimited” must not be shown if fair-use, storage, rate or seat restrictions materially bound the capability. When a feature is available only as add-on or higher usage fee, distinguish that from included.

Highlighting a recommended plan can guide attention only when rationale is product-owned; it must not distort the comparison through different card sizes, missing competitor details or preselected expensive cadence that obscures alternatives. Current customers need a clear marker for present plan and whether shown prices are upgrade deltas or total future price.

Responsive comparison must preserve cross-plan comparability. On mobile, stacked cards can make users forget previous feature states; use sticky plan selectors, concise difference views or a dedicated comparison matrix where needed rather than hiding detail.

## Failure Topology
- Annual plan displays `$10/month` most prominently while actual checkout charges `$120` upfront with weak disclosure.
- One plan says “Advanced analytics” and another says “Analytics,” with no comparable capability definition.
- “Unlimited projects” hides a workspace limit that changes the decision.
- Mobile stack removes feature rows and leaves only marketing headlines.
- Recommended badge visually suppresses lower-cost options.
- Existing user sees price per seat but current seat count/total impact is absent.

## Falsification and Recovery
Falsify across monthly/annual, currencies, tax/seat/usage bases, existing vs new customer, mobile, localization and feature eligibility. Ask whether two plans can be compared without mentally converting incompatible units or hunting footnotes. If not, the interface fails.

Recover by normalizing units, pairing monthly-equivalent with actual billing cadence, turning feature claims into comparable rows, surfacing material limits and preserving difference visibility on small screens.

## Output Contract
Return `pricing-comparison-contract` with plan identities, price basis/cadence, currency/tax disclosure, capability comparison schema, limits/add-ons, recommendation rationale boundary, current-plan context, responsive comparison and unit-consistency tests.