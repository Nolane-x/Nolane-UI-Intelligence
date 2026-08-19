---
name: designing-checkout-step-orchestration
description: Use when a commerce checkout spans address, fulfillment, payment, review, authentication, or policy stages and the UI must coordinate dependencies, commitment boundaries, recalculation, and recovery without turning checkout into a generic wizard.
---

# Designing Checkout Step Orchestration

## Parent Contract
**Required parent:** `designing-commerce-checkout`.

This faculty owns the staged transaction path from a viable cart toward final order commitment. It is narrower than generic multi-step forms because each stage can change commercial truth—tax, shipping, inventory, promotions, payment eligibility, or final authorization. It does not own the details of payment entry or shipping-method comparison.

## Decision Architecture
Define stages from transactional dependencies rather than visual convenience. Address may be required before taxes or delivery options are known; shipping choice may change total; payment method may impose eligibility or authentication; review should show the exact proposition that will be committed. Allow stage collapse or editing only when downstream effects can be recalculated and made visible.

Separate data completion from commitment. Entering payment details is not purchase. Selecting a shipping method is not inventory reservation unless the backend says so. The final action must be uniquely identifiable, show the final amount and material terms, and avoid accidental double submission. If the product uses express checkout, it may compress stages but cannot omit required evidence or consent merely for speed.

Backtracking must invalidate downstream state where necessary. Changing country can replace tax/shipping options; editing cart quantity can invalidate a promotion; changing payment method can alter fees. Preserve information that remains valid, but do not retain stale “complete” indicators after the proposition changed.

## Failure Topology
- Checkout stepper marks Shipping complete after address change invalidates the selected method.
- Final button says Continue even though it actually places the order.
- Re-entering a prior step resets payment unnecessarily and forces duplicate work.
- Express flow skips a required review disclosure and presents speed as consent.
- Total changes between stages with no explanation of which component changed.
- Double click or retry creates duplicate orders because submission state has no transaction identity.

## Falsification and Recovery
Falsify with cart edit mid-checkout, address/country change, promotion expiry, inventory loss, payment authentication interruption, browser Back, session expiry, express checkout, final-submit timeout with unknown outcome, keyboard/screen-reader progression, and a retry after order creation. The design fails if step completion can remain true after its commercial assumptions change or if the final commitment action is ambiguous.

Recover by defining dependency invalidation between stages, recalculating commercial truth authoritatively, preserving only valid state, labeling commitment explicitly, using transaction/idempotency identity, and checking order status before retrying an uncertain final submission.

## Output Contract
Return `checkout-step-orchestration-contract` with stage graph, dependencies, completion predicates, downstream invalidation, recalculation rules, express-flow equivalence, final commitment semantics, double-submit protection, backtracking/recovery, accessibility progression, and falsification cases.