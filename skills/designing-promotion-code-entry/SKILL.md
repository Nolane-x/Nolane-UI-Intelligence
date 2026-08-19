---
name: designing-promotion-code-entry
description: Use when checkout accepts coupons, vouchers, referral codes, or promotions and the interface must apply, explain, remove, replace, and reconcile promotional state without hiding eligibility rules or destabilizing the order total.
---

# Designing Promotion Code Entry

## Parent Contract
**Required parent:** `designing-commerce-checkout`.

This faculty owns manual promotional-code interaction. It does not define campaign policy or pricing authority. Its job is to let users submit a code, understand its outcome, see the exact commercial effect, and recover when eligibility changes later in checkout.

## Decision Boundary
Treat a code as a request to apply a promotion, not as a local string validation problem. Client syntax may trim harmless whitespace or normalize documented case behavior, but only authoritative pricing logic can decide valid, expired, usage-limited, account-restricted, item-ineligible, minimum-spend, region-specific, or mutually exclusive outcomes.

After success, show which promotion is active and what it changed. A generic green “Applied” is insufficient if the discount only affects one line item or free shipping. If multiple codes are permitted, define stacking/order semantics; if only one can apply, replacing the current promotion should be explicit. Removal must recompute totals immediately.

Eligibility can change after cart, address, shipping, or account edits. Do not leave an invalid promotion displayed as active while silently restoring full price. Surface the reason and allow a repair path when possible. Avoid hiding the field so aggressively that users who possess a code cannot find it, while also avoiding a prominent empty field that makes full-price shoppers feel they are missing a deal.

## Failure Topology
- Code is declared invalid client-side because of casing although backend accepts case-insensitive values.
- “Applied” appears but total and affected items do not show the discount effect.
- Cart edit invalidates minimum spend and discount disappears without explanation.
- Entering a second code silently replaces the first.
- Error copy reveals sensitive campaign eligibility or another customer's code state.
- Code submission reloads checkout and clears payment/address progress.

## Falsification and Recovery
Falsify with expired code, valid single-item discount, free shipping, minimum-spend drop after cart edit, non-stackable code conflict, account-specific eligibility, rapid repeated submit, server timeout, remove/reapply, keyboard/screen-reader operation, and a promotion becoming invalid at final review. The design fails if visible promotion state and authoritative order total can diverge or if users cannot identify the code's actual commercial effect.

Recover by delegating validity to pricing authority, rendering promotion effect alongside totals/items, defining stacking/replacement, revalidating on dependent checkout changes, preserving checkout state through submission failure, and using privacy-bounded reason messages.

## Output Contract
Return `promotion-code-entry-contract` with input normalization, authoritative validation states, applied-promotion representation, discount-effect evidence, stacking/replacement/removal rules, dependent revalidation, error privacy, checkout-state preservation, accessibility feedback, and falsification cases.