"""V13 eighth-wave independently authored rules for marketplace operations."""
from __future__ import annotations

from ._capabilities import interaction_caps


MARKET_OPS_RULES_V13 = [{'rule_id': 'ui.marketops.listing-moderation-state-visible',
  'domain': 'marketops',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Marketplace listings must expose moderation state separately from publication state',
  'statement': 'Published, pending review, restricted, rejected, and removed listings have '
               'different operational meanings that should not collapse into a single active flag.',
  'intent': 'Keep operators from treating review state as storefront availability.',
  'applies_when': ['Operators manage listings subject to moderation or policy review.'],
  'does_not_apply_when': [],
  'failure_modes': ['A listing marked “active” is actually hidden pending moderation, but the '
                    'operations table provides no moderation status.'],
  'user_impacts': ['Sellers and operators can make incorrect assumptions about what customers can '
                   'see or buy.'],
  'observables': ['Move a listing through pending, approved, restricted, rejected, and removed '
                  'states while checking list, detail, search preview, and bulk views.'],
  'falsifiers': ['Publication and moderation states remain independently visible and reconcile '
                 'with storefront visibility.'],
  'repairs': ['Persist moderation outcome as its own state with reason and timestamp, and display '
              'it beside publication controls.'],
  'exceptions': [],
  'verification': ['Exercise each moderation transition and verify operator status matches '
                   'customer-visible availability.'],
  'owner_hints': ['designing-marketplace-operations'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-market-ops-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.marketops.order-distinct-from-payout-state',
  'domain': 'marketops',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Marketplace order status must remain distinct from seller payout status',
  'statement': 'Fulfillment, refund, dispute, and payout progress are separate lifecycles and '
               'should not be summarized as one ambiguous completed state.',
  'intent': 'Prevent operators from inferring money movement from order completion.',
  'applies_when': ['Marketplace operations expose both order fulfillment and seller settlement.'],
  'does_not_apply_when': [],
  'failure_modes': ['An order says “completed” after delivery even though seller funds are still '
                    'held and the payout has not begun.'],
  'user_impacts': ['Operators can give incorrect settlement answers or trigger duplicate payout '
                   'actions.'],
  'observables': ['Inspect delivered, refunded, disputed, held, pending-payout, and paid '
                  'combinations for the same order.'],
  'falsifiers': ['Order and payout states remain separately visible and linked by stable '
                 'identifiers without one overwriting the other.'],
  'repairs': ['Model order and settlement as separate state machines and expose both on operations '
              'surfaces.'],
  'exceptions': [],
  'verification': ['Create cross-product state combinations and verify no order label falsely '
                   'implies payout completion.'],
  'owner_hints': ['designing-marketplace-operations'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-market-ops-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.marketops.seller-scope-visible',
  'domain': 'marketops',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Marketplace operations actions must show the effective seller or account scope',
  'statement': 'Shared operational consoles can span sellers, stores, regions, or legal entities; '
               'actions need a visible scope before mutation.',
  'intent': 'Prevent an operator from applying a change to the wrong seller context.',
  'applies_when': ['The same console can administer more than one seller, store, or marketplace '
                   'account.'],
  'does_not_apply_when': [],
  'failure_modes': ['A bulk policy action executes against all sellers while the header still '
                    'shows a previously selected seller filter.'],
  'user_impacts': ['Unintended accounts can be changed with limited ability to reconstruct the '
                   'scope afterward.'],
  'observables': ['Switch seller context, open deep links, and perform single and bulk actions '
                  'while inspecting payload and audit record.'],
  'falsifiers': ['The effective seller/account is visible at action time and matches the '
                 'identities changed server-side.'],
  'repairs': ['Bind mutations to explicit seller/account identifiers and display the resolved '
              'scope in confirmation and result views.'],
  'exceptions': [],
  'verification': ['Attempt actions after context switches and stale tabs, verifying no mutation '
                   'inherits an unintended seller.'],
  'owner_hints': ['designing-marketplace-operations'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-market-ops-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.marketops.inventory-reservation-source-visible',
  'domain': 'marketops',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Operational inventory must expose the reservation source behind unavailable quantity',
  'statement': 'Unavailable stock can be held by carts, orders, transfers, policy quarantine, or '
               'external channels; operators need the source before releasing or reallocating it.',
  'intent': 'Keep stock interventions from cancelling the wrong reservation class.',
  'applies_when': ['Operations tools display reserved or unavailable marketplace inventory.'],
  'does_not_apply_when': [],
  'failure_modes': ['A product shows ten reserved units but does not reveal that eight belong to '
                    'paid orders and two to expiring carts.'],
  'user_impacts': ['Operators can release committed inventory or misdiagnose oversell risk.'],
  'observables': ['Populate reservations from distinct sources and inspect quantity drilldowns, '
                  'release actions, and synchronization.'],
  'falsifiers': ['Reserved quantity decomposes into stable source categories and drilldowns '
                 'reconcile to the aggregate.'],
  'repairs': ['Track reservation provenance and expose source, owning object, and expiry where '
              'applicable.'],
  'exceptions': [],
  'verification': ['Create mixed reservation sources and verify aggregate totals and source-level '
                   'release semantics remain consistent.'],
  'owner_hints': ['designing-marketplace-operations'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-market-ops-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.marketops.bulk-operation-scope-confirmed',
  'domain': 'marketops',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Marketplace bulk operations must confirm the exact selected population and filters',
  'statement': 'A bulk action can span hidden pages or dynamically changing filters; its execution '
               'population must not be inferred from a visible page count.',
  'intent': 'Prevent destructive marketplace changes from affecting an unintended item set.',
  'applies_when': ['Operations tools support bulk changes over filtered listings, orders, or '
                   'sellers.'],
  'does_not_apply_when': [],
  'failure_modes': ['The toolbar says 20 selected while “select all matching” actually targets '
                    '4,000 records across pages.'],
  'user_impacts': ['A policy, price, or visibility change can be applied orders of magnitude '
                   'beyond the operator’s intent.'],
  'observables': ['Select explicit rows, all matching, and a population that changes before '
                  'submit; inspect confirmation and result counts.'],
  'falsifiers': ['The UI names selection mode, effective filter, resolved count, and exclusions '
                 'before commit.'],
  'repairs': ['Represent selection scope explicitly and snapshot or revalidate the population at '
              'execution time.'],
  'exceptions': [],
  'verification': ['Race filter/data changes around a bulk action and verify affected identifiers '
                   'equal the confirmed scope.'],
  'owner_hints': ['designing-marketplace-operations'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-market-ops-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.marketops.policy-hold-reason-and-state-visible',
  'domain': 'marketops',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Policy holds must expose their reason, authority, and release state',
  'statement': 'A generic hold label is insufficient when different policy systems impose '
               'different restrictions and remediation paths.',
  'intent': 'Let operators distinguish actionable policy restrictions from pending or expired '
            'holds.',
  'applies_when': ['Marketplace entities can be restricted by fraud, compliance, quality, or other '
                   'policy systems.'],
  'does_not_apply_when': [],
  'failure_modes': ['An order is blocked by “policy hold” but the operator cannot see whether the '
                    'hold is active, expired, appealed, or which system owns it.'],
  'user_impacts': ['Operators may promise impossible releases or duplicate escalations.'],
  'observables': ['Apply holds from multiple authorities, expire or release them, and inspect '
                  'status, reason, ownership, and audit history.'],
  'falsifiers': ['Each hold exposes a stable authority/reason and current lifecycle state without '
                 'rewriting historical hold events.'],
  'repairs': ['Model holds as identifiable records with authority, reason, timestamps, and '
              'release/appeal transitions.'],
  'exceptions': [],
  'verification': ['Exercise concurrent and sequential holds and verify the effective restriction '
                   'and individual histories remain inspectable.'],
  'owner_hints': ['designing-marketplace-operations'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-market-ops-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.marketops.dispute-linkage-stable',
  'domain': 'marketops',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Marketplace dispute links must remain bound to the correct order and transaction '
           'identities',
  'statement': 'Disputes may reference orders, payments, shipments, refunds, and payouts; '
               'navigation must preserve those immutable relationships.',
  'intent': 'Prevent case investigation from drifting to a similarly named but unrelated '
            'transaction.',
  'applies_when': ['Operations surfaces cross-link disputes with commerce records.'],
  'does_not_apply_when': [],
  'failure_modes': ['After an order is partially refunded, the dispute link opens the latest '
                    'refund rather than the transaction that the dispute concerns.'],
  'user_impacts': ['Operators can review or act on the wrong financial event.'],
  'observables': ['Create multiple transactions and disputes under one order, then navigate '
                  'through every linked entity after updates.'],
  'falsifiers': ['Dispute links resolve by immutable identifiers and continue to point to the same '
                 'evidence-bearing records.'],
  'repairs': ['Persist explicit dispute-to-entity relations and never derive them from current '
              '“latest transaction” heuristics.'],
  'exceptions': [],
  'verification': ['Mutate order/refund history and verify all dispute links retain their original '
                   'targets.'],
  'owner_hints': ['designing-marketplace-operations'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-market-ops-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.marketops.search-index-lag-visible',
  'domain': 'marketops',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Marketplace operations search must disclose when indexed results lag authoritative '
           'records',
  'statement': 'Search indexes can be eventually consistent; stale or missing results should not '
               'be presented as proof that an entity does not exist.',
  'intent': 'Prevent operators from concluding that recent orders or listings are absent because '
            'indexing is delayed.',
  'applies_when': ['Operations search is backed by an asynchronous index or cache.'],
  'does_not_apply_when': [],
  'failure_modes': ['A newly created seller cannot be found for several minutes and the UI reports '
                    '“No seller exists.”'],
  'user_impacts': ['Operators may recreate records, escalate incorrectly, or miss urgent cases.'],
  'observables': ['Create and update searchable entities while delaying index refresh, then '
                  'compare direct lookup and search results.'],
  'falsifiers': ['Search exposes index freshness or provides authoritative-ID lookup when the '
                 'index may lag.'],
  'repairs': ['Surface search freshness and distinguish “no indexed match” from authoritative '
              'absence; provide direct identity lookup for critical workflows.'],
  'exceptions': [],
  'verification': ['Delay indexing and verify the UI never turns an index miss into an existence '
                   'claim.'],
  'owner_hints': ['designing-marketplace-operations'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-market-ops-owners-v13'],
  'status': 'active'}]

__all__ = ["MARKET_OPS_RULES_V13"]
