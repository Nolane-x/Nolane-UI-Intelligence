"""V13 commerce lifecycle rules for price certainty, payment recovery, fulfillment, returns, and subscription authority."""
from __future__ import annotations

from ._capabilities import interaction_caps


COMMERCE_HIGH_CONSEQUENCE_RULES_V13 = [
    {'rule_id': 'ui.commerce.estimated-tax-shipping-distinct-from-final',
     'domain': 'commerce',
     'class': 'behavioral',
     'severity': 'major',
     'enforcement': 'block',
     'title': 'Estimated tax and shipping must remain distinct from final payable charges',
     'statement': 'When tax, duties, shipping, or service fees are not final until address, provider, inventory, or '
                  'payment context is confirmed, the checkout must not present an estimate as an authoritative final '
                  'total.',
     'intent': 'Keep price certainty aligned with the stage of the transaction so users know which amounts can still '
               'change before commitment.',
     'applies_when': ['Checkout displays cost components whose final amount depends on information or provider results '
                      'not yet resolved.'],
     'does_not_apply_when': [],
     'failure_modes': ['An estimated charge is styled and totaled as final without an estimate qualifier, then changes '
                       'later with no explicit transition in certainty.'],
     'user_impacts': ['Users can make purchase decisions based on a price the system already knows is provisional.'],
     'observables': ['Run checkout before and after each price-determining input becomes available and compare component '
                     'labels, total certainty, and final authorization amount.'],
     'falsifiers': ['Provisional charges are marked as estimates and the final payable total becomes authoritative only '
                    'after required inputs and provider calculations resolve.'],
     'repairs': ['Model monetary components with certainty state and promote them from estimated to final only at the '
                 'corresponding pricing authority boundary.'],
     'exceptions': [],
     'verification': ['Test address change, shipping method, tax jurisdiction, duties, and provider recalculation and '
                      'verify estimate/final status updates with the actual amount authority.'],
     'owner_hints': ['designing-commerce-checkout'],
     'verifier_hints': ['critiquing-user-experience'],
     'capabilities': interaction_caps(),
     'provenance_ids': ['nui-commerce-lifecycle-owners-v13'],
     'status': 'active'},
    {'rule_id': 'ui.commerce.promotion-removal-explains-total-change',
     'domain': 'commerce',
     'class': 'behavioral',
     'severity': 'major',
     'enforcement': 'block',
     'title': 'Removing or invalidating a promotion must explain the resulting total change',
     'statement': 'If a coupon, promotion, bundle, loyalty credit, or conditional discount stops applying, checkout must '
                  'identify that change and its monetary effect instead of silently increasing the payable total.',
     'intent': 'Preserve price-change causality so users can understand why a total differs from the amount they '
               'previously reviewed.',
     'applies_when': ['Checkout totals can include conditional promotions that may become invalid after cart, address, '
                      'account, inventory, or timing changes.'],
     'does_not_apply_when': [],
     'failure_modes': ['The promotion disappears and the total rises without an explicit state transition or explanation '
                       'tied to the affected discount.'],
     'user_impacts': ['Users can authorize a higher payment while believing the earlier promotion is still included.'],
     'observables': ['Apply a promotion, invalidate each of its conditions, and compare cart line items, total deltas, '
                     'confirmation copy, and payment authorization amount.'],
     'falsifiers': ['Promotion removal is represented as a distinct price event with the affected amount visible before '
                    'the next commitment boundary.'],
     'repairs': ['Keep promotion eligibility as an explicit pricing component and surface invalidation alongside the '
                 'recalculated total rather than dropping the line silently.'],
     'exceptions': [],
     'verification': ['Test quantity, account, expiry, inventory, shipping, and stacking-condition invalidation and '
                      'verify each total increase is attributable before purchase.'],
     'owner_hints': ['designing-shopping-carts'],
     'verifier_hints': ['critiquing-functional-completeness'],
     'capabilities': interaction_caps(),
     'provenance_ids': ['nui-commerce-lifecycle-owners-v13'],
     'status': 'active'},
    {'rule_id': 'ui.commerce.payment-retry-reuses-order-identity',
     'domain': 'commerce',
     'class': 'behavioral',
     'severity': 'major',
     'enforcement': 'block',
     'title': 'Retrying payment must not create a second order for the same checkout intent',
     'statement': 'When an order exists but payment fails or remains uncertain, retrying payment should continue against '
                  'the same order or explicit recovery object rather than rebuilding checkout into a duplicate order '
                  'unless the product deliberately creates a new purchase.',
     'intent': 'Separate payment-attempt lifecycle from order identity so recovery does not multiply fulfillment or '
               'inventory commitments.',
     'applies_when': ['Checkout can create an order before payment reaches a terminal success state and users can retry '
                      'failed or ambiguous payment attempts.'],
     'does_not_apply_when': [],
     'failure_modes': ['Each payment retry resubmits the entire checkout create operation and generates multiple order '
                       'records for one intended purchase.'],
     'user_impacts': ['Users can be charged, shipped, reserved, or emailed multiple times while thinking they only '
                      'retried payment.'],
     'observables': ['Create an order, force payment failure and ambiguous provider timeouts, retry repeatedly, and '
                     'compare order IDs, payment-attempt IDs, fulfillment state, and inventory holds.'],
     'falsifiers': ['Payment attempts remain attached to one purchase identity unless the UI explicitly starts a new '
                    'order and clearly abandons or closes the previous one.'],
     'repairs': ['Persist order identity before payment recovery and route retries to a payment-attempt endpoint or '
                 'equivalent bounded transaction continuation.'],
     'exceptions': [],
     'verification': ['Test card decline, provider timeout after authorization, 3DS interruption, wallet cancellation, '
                      'and reconnect and verify one intended purchase maps to one order lifecycle.'],
     'owner_hints': ['designing-payment-failure-recovery'],
     'verifier_hints': ['critiquing-functional-completeness'],
     'capabilities': interaction_caps(),
     'provenance_ids': ['nui-commerce-lifecycle-owners-v13'],
     'status': 'active'},
    {'rule_id': 'ui.commerce.partial-fulfillment-state-per-item',
     'domain': 'commerce',
     'class': 'behavioral',
     'severity': 'major',
     'enforcement': 'block',
     'title': 'Partially fulfilled orders must expose fulfillment state at item or shipment scope',
     'statement': 'When an order is split across items, shipments, pickup locations, or fulfillment providers, the order '
                  'surface must not collapse the entire purchase into a single shipped, delivered, or delayed state that '
                  'applies only to part of it.',
     'intent': 'Keep fulfillment truth at the scope where customers can actually take action or form expectations.',
     'applies_when': ['One order can contain items with different fulfillment methods, shipment dates, cancellations, or '
                      'delivery states.'],
     'does_not_apply_when': [],
     'failure_modes': ['A single top-level order badge reports shipped or delivered while other items remain '
                       'unfulfilled, backordered, or cancelled.'],
     'user_impacts': ['Users can miss outstanding items, wait for packages that were cancelled, or assume a completed '
                      'order when only one shipment finished.'],
     'observables': ['Create split-fulfillment fixtures and progress each item independently, then compare order '
                     'summary, item states, shipment groups, and available actions.'],
     'falsifiers': ['Each item or shipment exposes its own authoritative state and the top-level summary accurately '
                    'aggregates rather than overwrites those differences.'],
     'repairs': ['Model fulfillment by shipment or item identity and derive order-level status from those components '
                 'with mixed-state handling.'],
     'exceptions': [],
     'verification': ['Test split shipment, partial pickup, backorder, item cancellation, replacement, and partial '
                      'delivery and verify every component remains individually legible.'],
     'owner_hints': ['designing-order-tracking'],
     'verifier_hints': ['critiquing-user-experience'],
     'capabilities': interaction_caps(),
     'provenance_ids': ['nui-commerce-lifecycle-owners-v13'],
     'status': 'active'},
    {'rule_id': 'ui.commerce.return-eligibility-basis-visible',
     'domain': 'commerce',
     'class': 'contextual',
     'severity': 'moderate',
     'enforcement': 'warn',
     'title': 'Return eligibility should expose the basis when similar items have different outcomes',
     'statement': 'If items in the same order differ in return eligibility because of date, category, condition, seller, '
                  'fulfillment, final-sale status, or prior return state, the interface should explain the applicable '
                  'basis instead of showing an unexplained eligible or ineligible badge.',
     'intent': 'Help users understand and act on return policy as applied to their specific item without claiming a '
               'broader legal rule than the product knows.',
     'applies_when': ['The return flow can compute item-specific eligibility from authoritative order and policy data.'],
     'does_not_apply_when': [],
     'failure_modes': ['Similar items show different return availability with no visible basis or the UI displays a '
                       'generic deadline that does not match the item policy used by the backend.'],
     'user_impacts': ['Users can waste time, miss a valid return window, or believe an arbitrary product bug is blocking '
                      'a return.'],
     'observables': ['Construct items across eligibility conditions and compare backend policy result, visible reason, '
                     'deadline, and enabled actions for each item.'],
     'falsifiers': ['Eligibility state and any shown deadline map to the same authoritative policy decision, with '
                    'unsupported reasons left unspecified rather than invented.'],
     'repairs': ['Carry structured eligibility reason and effective deadline from the return authority into the '
                 'item-level return surface.'],
     'exceptions': [],
     'verification': ['Test final sale, damaged exception, seller-specific policy, partial return, prior return, and '
                      'deadline boundary and verify visible basis matches authority.'],
     'owner_hints': ['designing-return-and-refund-flows'],
     'verifier_hints': ['critiquing-user-experience'],
     'capabilities': interaction_caps(),
     'provenance_ids': ['nui-commerce-lifecycle-owners-v13'],
     'status': 'active'},
    {'rule_id': 'ui.commerce.plan-downgrade-effective-date-visible',
     'domain': 'commerce',
     'class': 'behavioral',
     'severity': 'major',
     'enforcement': 'block',
     'title': 'Subscription downgrades must expose when the lower plan actually takes effect',
     'statement': 'If a plan downgrade is scheduled for renewal rather than immediate, the subscription UI must '
                  'distinguish current entitlements from future-plan state and show the effective boundary before '
                  'confirmation.',
     'intent': 'Keep subscription authority legible across deferred changes so users know what they can use now and what '
               'will change later.',
     'applies_when': ['The subscription system supports plan changes that may apply immediately, at period end, after '
                      'proration, or on another provider-defined date.'],
     'does_not_apply_when': [],
     'failure_modes': ['The UI says the user is on the lower plan immediately even though current higher entitlements '
                       'remain active, or hides that a downgrade is merely scheduled.'],
     'user_impacts': ['Users can misjudge current access, billing, or cancellation decisions because present and future '
                      'subscription states are collapsed.'],
     'observables': ['Schedule downgrades under each timing policy and compare current plan, pending change, effective '
                     'timestamp, entitlements, and billing provider state.'],
     'falsifiers': ['Current and scheduled plans are shown as separate states with the effective date tied to the '
                    "provider's authoritative subscription transition."],
     'repairs': ['Model pending plan changes separately from active subscription state and render both until the '
                 'effective boundary commits.'],
     'exceptions': [],
     'verification': ['Test immediate, period-end, trial-end, proration, cancellation, and change reversal and verify '
                      'visible dates and entitlements follow the actual lifecycle.'],
     'owner_hints': ['designing-subscription-management'],
     'verifier_hints': ['critiquing-functional-completeness'],
     'capabilities': interaction_caps(),
     'provenance_ids': ['nui-commerce-lifecycle-owners-v13'],
     'status': 'active'},
    {'rule_id': 'ui.commerce.credit-allocation-visible-before-charge',
     'domain': 'commerce',
     'class': 'behavioral',
     'severity': 'major',
     'enforcement': 'block',
     'title': 'Store credit and gift balance allocation must be visible before the remaining charge is authorized',
     'statement': 'When a purchase combines gift balance, store credit, loyalty value, or account credit with an '
                  'external payment method, the user must see how much value will be consumed from each source before '
                  'authorizing the remainder.',
     'intent': 'Expose split tender allocation so users understand both the external charge and the depletion of '
               'internal value.',
     'applies_when': ['Checkout can apply one or more internal-value sources before charging a card, bank, wallet, or '
                      'other external method.'],
     'does_not_apply_when': [],
     'failure_modes': ['The final button shows only the external charge or only the total price and hides how much gift '
                       'or account value will be consumed.'],
     'user_impacts': ['Users can unexpectedly drain stored value or misunderstand the amount that will reach their '
                      'external payment method.'],
     'observables': ['Construct purchases with partial and full internal balances, change cart totals, and compare '
                     'pre-commit allocation with ledger entries and external authorization amount.'],
     'falsifiers': ['The visible allocation equals the authoritative split tender calculation and updates whenever cart '
                    'value or selected balance sources change.'],
     'repairs': ['Represent each tender source as a monetary component in the payment plan and render the exact planned '
                 'depletion before commitment.'],
     'exceptions': [],
     'verification': ['Test insufficient balance, multiple credits, currency mismatch, refund/retry, and cart changes '
                      'and verify the pre-charge allocation matches resulting ledgers.'],
     'owner_hints': ['designing-commerce-checkout'],
     'verifier_hints': ['critiquing-user-experience'],
     'capabilities': interaction_caps(),
     'provenance_ids': ['nui-commerce-lifecycle-owners-v13'],
     'status': 'active'},
    {'rule_id': 'ui.commerce.dispute-state-distinct-from-refund',
     'domain': 'commerce',
     'class': 'behavioral',
     'severity': 'major',
     'enforcement': 'block',
     'title': 'Payment disputes and chargebacks must remain distinct from merchant refunds',
     'statement': 'A transaction under dispute, chargeback, reversal review, or issuer investigation must not be labeled '
                  'as refunded unless the product has authoritative evidence of an actual refund settlement.',
     'intent': 'Keep fundamentally different money-movement lifecycles separate so users understand who controls the '
               'next step and whether funds are final.',
     'applies_when': ['The product surfaces both merchant-initiated refunds and issuer or network dispute processes for '
                      'transactions.'],
     'does_not_apply_when': [],
     'failure_modes': ['A dispute opened or provisional credit granted causes the order or payment UI to display '
                       'refunded even though merchant refund settlement never occurred.'],
     'user_impacts': ['Users can stop following a dispute, duplicate a refund request, or misunderstand whether '
                      'provisional funds can still reverse.'],
     'observables': ['Run fixtures for refund requested, refund settled, dispute opened, provisional credit, chargeback '
                     'won/lost, and reversal and compare visible lifecycle labels with payment authority.'],
     'falsifiers': ['Each state remains in its own lifecycle and only actual settled refund authority produces a refund '
                    'state.'],
     'repairs': ['Map provider event types into separate refund and dispute state machines and avoid deriving one from '
                 'the presence of any negative payment adjustment.'],
     'exceptions': [],
     'verification': ['Test overlapping refund and dispute scenarios and verify the UI can represent both without '
                      'collapsing them into one terminal label.'],
     'owner_hints': ['designing-return-and-refund-flows'],
     'verifier_hints': ['critiquing-functional-completeness'],
     'capabilities': interaction_caps(),
     'provenance_ids': ['nui-commerce-lifecycle-owners-v13'],
     'status': 'active'},
]

__all__ = ['COMMERCE_HIGH_CONSEQUENCE_RULES_V13']
