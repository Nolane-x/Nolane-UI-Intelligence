---
name: designing-commerce-checkout
description: Use when a UI moves users from cart or selection through pricing, delivery, identity, payment, order review, purchase, inventory changes, failure recovery, and post-purchase confirmation.
---

# Designing Commerce Checkout

## Overview
Checkout is a state-consistency problem across item, price, inventory, delivery, identity, payment, and commitment. Keep the total and consequences stable enough to trust while making inevitable changes explicit and recoverable.

## Parent Contract
**Required parent:** `routing-ui-work`.

Require product/cart model, price/discount/tax/fee rules, inventory timing, shipping/delivery choices, payment providers, guest/account flow, geography, recurring/subscription terms, and post-purchase support.

## Decision Model
Preserve cart intent through the funnel. Do not erase variants, quantities, or applied benefits without explanation. Separate editable stages from final review while avoiding unnecessary page count; progressive disclosure is useful only when users retain context.

Price transparency is continuous. Show subtotal, discounts, tax estimate/final tax, shipping/service fees, recurring charges, trial conversion, and total before the purchase action. If a material value changes — inventory, shipping, exchange rate, promotion — highlight the delta and require re-review when consequence warrants it.

Validation should be local and recoverable. Preserve correct fields after payment/address failure. Use address/payment provider assistance without silently changing meaningful data. Guest checkout should not be blocked by forced account creation unless the product truly requires identity.

At commit, disable duplicate purchase without freezing the page into ambiguity. If network state becomes unknown, tell the user not to retry blindly and provide order lookup/reconciliation. Success requires order id/receipt, purchased items, amount, delivery expectation, and support/cancel/return next steps appropriate to the business.

## Evidence
Test expired inventory, promotion changes, invalid address, payment decline, 3DS/reauth return, duplicate tap, network loss after authorization, guest flow, subscription/trial disclosure, long locales, accessibility, mobile keyboard, and post-purchase retrieval.

## Output Contract
Return a `checkout-contract` with `cart_state`, `pricing_breakdown`, `inventory_rules`, `delivery_flow`, `identity_strategy`, `payment_states`, `validation_and_preservation`, `change_reconfirmation`, `duplicate_protection`, `unknown_commit_recovery`, `receipt_and_support`, and `checkout_tests[]`.

## Failure Traps
- Surprise fee after the purchase action.
- Account creation inserted after payment details with no prior warning.
- Entire form cleared after one validation error.
- “Try again” after unknown payment state.
- Discount silently disappearing between cart and checkout.
- Subscription renewal terms visually subordinate to the CTA.
- Success screen with no durable order identifier.

A checkout earns trust when the final committed state matches the state the user believed they reviewed.

## V6 Checkout Integrity Protocol
Preserve a **total-cost invariant** from cart through authorization: item price, quantity, discount, tax, shipping, fees, currency, and final charged total must reconcile, with changes surfaced before payment. Expose **fulfillment-option truth**—availability, delivery/pickup estimate, location, stock reservation, and restrictions—before irreversible steps.

Maintain **cart-state persistence** across auth redirects, device/session transitions, inventory changes, and failed payment. Define **payment-failure continuity** so entered non-sensitive data, cart, selected fulfillment, and error reason survive without accidental duplicate charge. Keep a clear **guest-account boundary**: account creation is optional unless genuinely required and must not silently merge/lose guest state.

### Falsification
Change stock/tax/shipping after review, fail authentication/3DS, retry payment, and sign in from guest state. Any unexplained total/cart mutation invalidates checkout trust.

### Recovery
Return to review with changed values highlighted, preserve cart/draft, verify payment status before retry, and avoid coercive account creation as a recovery shortcut.
