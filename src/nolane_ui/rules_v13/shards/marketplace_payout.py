"""V13 eighth-wave independently authored rules for marketplace payout."""
from __future__ import annotations

from ._capabilities import interaction_caps


MARKETPLACE_PAYOUT_RULES_V13 = [{'rule_id': 'ui.payout.gross-net-fee-basis-visible',
  'domain': 'payout',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Payout summaries must distinguish gross proceeds, fees, adjustments, and net amount',
  'statement': 'A single payout total hides how money moved; gross sales, platform fees, refunds, '
               'reserves, taxes, and adjustments need a reconciliable basis.',
  'intent': 'Make seller settlement explainable rather than a black-box number.',
  'applies_when': ['Marketplace payouts aggregate multiple transaction and fee components.'],
  'does_not_apply_when': [],
  'failure_modes': ['A seller sees a $900 payout from $1,000 sales without any line explaining the '
                    '$100 reduction.'],
  'user_impacts': ['Sellers and support operators cannot reconcile settlement or identify '
                   'incorrect fees.'],
  'observables': ['Construct payouts with fees, refunds, reserves, and adjustments and compare '
                  'summary, detail, and export.'],
  'falsifiers': ['Net payout equals the disclosed component lines and every deduction has a stable '
                 'source record.'],
  'repairs': ['Represent payout composition as immutable settlement lines and calculate net from '
              'those authoritative components.'],
  'exceptions': [],
  'verification': ['Reconcile a mixed payout line-by-line and verify displayed net and export '
                   'equal the component sum exactly.'],
  'owner_hints': ['designing-marketplace-payout-status'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-payout-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.payout.pending-available-paid-distinguished',
  'domain': 'payout',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Payout funds must distinguish pending, available, scheduled, and paid states',
  'statement': 'Eligibility, scheduling, transfer initiation, and final payment are separate '
               'stages with different recoverability and timing.',
  'intent': 'Prevent sellers from treating future or in-flight money as already received.',
  'applies_when': ['Seller balances move through multiple payout availability stages.'],
  'does_not_apply_when': [],
  'failure_modes': ['A dashboard labels a scheduled bank transfer “paid” before the provider has '
                    'accepted or settled it.'],
  'user_impacts': ['Sellers may make cash decisions based on funds not yet received.'],
  'observables': ['Move funds through pending, available, scheduled, processing, paid, and failed '
                  'states and inspect balance effects.'],
  'falsifiers': ['Each lifecycle stage is visible and only authoritative settlement produces the '
                 'paid state.'],
  'repairs': ['Model balance eligibility separately from transfer lifecycle and expose both on '
              'payout surfaces.'],
  'exceptions': [],
  'verification': ['Exercise successful, delayed, and failed transfers and verify labels and '
                   'balances reflect the correct stage.'],
  'owner_hints': ['designing-marketplace-payout-status'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-payout-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.payout.destination-identity-visible',
  'domain': 'payout',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Payouts must expose the destination identity actually used for transfer',
  'statement': 'Sellers may have multiple bank accounts or payment destinations; a transfer must '
               'remain tied to the immutable destination selected at initiation.',
  'intent': 'Prevent destination changes from obscuring where an in-flight payout is going.',
  'applies_when': ['A seller can configure or change payout destinations.'],
  'does_not_apply_when': [],
  'failure_modes': ['A bank account is changed after scheduling and the pending payout screen now '
                    'shows the new account even though the transfer targets the old one.'],
  'user_impacts': ['The seller cannot determine where funds will arrive or detect a misdirected '
                   'transfer.'],
  'observables': ['Schedule a payout, change destination settings, and inspect pending history, '
                  'confirmations, and provider records.'],
  'falsifiers': ['Each payout displays a stable redacted destination identity captured at '
                 'initiation regardless of later preference changes.'],
  'repairs': ['Snapshot destination identity on the payout instruction and never re-resolve '
              'historical transfers from current settings.'],
  'exceptions': [],
  'verification': ['Change destinations around scheduled and in-flight payouts and verify each '
                   'transfer retains its original destination.'],
  'owner_hints': ['designing-marketplace-payout-status'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-payout-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.payout.currency-conversion-basis-visible',
  'domain': 'payout',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Payout currency conversions must disclose source amount, rate basis, and resulting '
           'currency',
  'statement': 'Converted payouts need enough information to distinguish marketplace proceeds from '
               'FX effects and fees.',
  'intent': 'Prevent unexplained settlement differences across currencies.',
  'applies_when': ['Seller proceeds and payout destination can use different currencies.'],
  'does_not_apply_when': [],
  'failure_modes': ['A payout shows €910 from $1,000 proceeds with no rate timestamp or '
                    'distinction between FX spread and marketplace fees.'],
  'user_impacts': ['Sellers cannot reconcile settlement or compare conversion costs.'],
  'observables': ['Create payouts across currencies with rate changes and fees, then inspect '
                  'detail and export.'],
  'falsifiers': ['Source currency, converted amount, effective rate basis, and conversion-related '
                 'fees are identifiable.'],
  'repairs': ['Persist conversion result and rate provenance on settlement lines rather than '
              'recalculating history from current rates.'],
  'exceptions': [],
  'verification': ['Recompute expected converted totals from stored lines and verify historical '
                   'payouts remain unchanged after market rates move.'],
  'owner_hints': ['designing-marketplace-payout-status'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-payout-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.payout.failed-payout-recovery-visible',
  'domain': 'payout',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Failed payouts must expose recoverable funds and the next valid recovery path',
  'statement': 'A failed transfer should not make money disappear or encourage a duplicate manual '
               'payout without showing whether funds returned to balance.',
  'intent': 'Keep payout recovery financially consistent and understandable.',
  'applies_when': ['External payout transfers can fail after initiation.'],
  'does_not_apply_when': [],
  'failure_modes': ['A transfer fails at the bank but the seller balance remains reduced and the '
                    'UI only says “failed” with no recovery state.'],
  'user_impacts': ['Funds appear lost or support may trigger duplicate settlement.'],
  'observables': ['Cause provider rejection before and after transfer initiation and inspect '
                  'balance, retry eligibility, and replacement payout linkage.'],
  'falsifiers': ['Failure shows whether funds returned, remain in transit, or require remediation, '
                 'with any retry linked to the failed transfer.'],
  'repairs': ['Model failure settlement explicitly and re-credit or quarantine funds according to '
              'authoritative provider outcome before retry.'],
  'exceptions': [],
  'verification': ['Exercise retry and destination-fix flows and verify money is neither '
                   'duplicated nor stranded invisibly.'],
  'owner_hints': ['designing-marketplace-payout-status'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-payout-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.payout.adjustment-lineage-preserved',
  'domain': 'payout',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Payout adjustments must retain lineage to the event that created them',
  'statement': 'Manual corrections, chargebacks, reversals, and prior-period fixes should remain '
               'traceable to their source rather than appearing as unexplained balance changes.',
  'intent': 'Preserve auditability of settlement corrections.',
  'applies_when': ['Payout calculations include adjustments created after original transactions.'],
  'does_not_apply_when': [],
  'failure_modes': ['A -$75 adjustment appears in the next payout without a link to the refunded '
                    'order or prior settlement it corrects.'],
  'user_impacts': ['Sellers and operators cannot determine whether the adjustment is valid or '
                   'duplicated.'],
  'observables': ['Create different adjustment types against prior payouts and inspect references '
                  'in detail and export.'],
  'falsifiers': ['Every adjustment carries a stable source/reason and historical settlement '
                 'records are not rewritten to hide it.'],
  'repairs': ['Represent corrections as new settlement lines linked to immutable source events.'],
  'exceptions': [],
  'verification': ['Trace each adjustment from payout to originating transaction and verify '
                   'reversing an adjustment creates new lineage rather than mutation.'],
  'owner_hints': ['designing-marketplace-payout-status'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-payout-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.payout.reserve-hold-scope-visible',
  'domain': 'payout',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Reserve holds must expose amount, scope, reason, and release condition',
  'statement': 'Funds held in reserve affect payout availability but are not equivalent to fees or '
               'completed deductions.',
  'intent': 'Prevent sellers from interpreting temporary reserves as permanent charges.',
  'applies_when': ['Marketplace risk or policy systems can hold part of seller proceeds.'],
  'does_not_apply_when': [],
  'failure_modes': ['A seller’s available balance is lower because of a rolling reserve, but the '
                    'payout page only shows a smaller total.'],
  'user_impacts': ['Sellers cannot forecast cash flow or distinguish reserve policy from fees.'],
  'observables': ['Apply fixed, percentage, order-specific, and time-bound reserves and inspect '
                  'balances and releases.'],
  'falsifiers': ['Held amounts are separately identified with scope/reason and release behavior '
                 'that reconciles to future available balance.'],
  'repairs': ['Model reserve as a separate balance bucket with source policy and release '
              'criteria.'],
  'exceptions': [],
  'verification': ['Trigger reserve creation and release and verify funds move between held and '
                   'available exactly according to disclosed conditions.'],
  'owner_hints': ['designing-marketplace-payout-status'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-payout-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.payout.reconciliation-export-consistent',
  'domain': 'payout',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Payout reconciliation exports must match the settlement lines shown in the product',
  'statement': 'Exports used for accounting must preserve the same payout scope, currencies, fees, '
               'adjustments, and identifiers as the reviewed UI.',
  'intent': 'Prevent accounting records from diverging from operational settlement truth.',
  'applies_when': ['Payout details can be exported for reconciliation or bookkeeping.'],
  'does_not_apply_when': [],
  'failure_modes': ['The UI includes a reserve release and fee reversal but the CSV omits both '
                    'while still reporting the final net payout.'],
  'user_impacts': ['Finance teams cannot reproduce the settlement from exported records.'],
  'observables': ['Export complex payouts with every line type and compare row sums, identifiers, '
                  'currencies, and status with UI detail.'],
  'falsifiers': ['Exported settlement lines reconcile exactly to the displayed payout and include '
                 'stable identifiers for each component.'],
  'repairs': ['Generate exports from the canonical settlement ledger rather than a separate '
              'simplified reporting query.'],
  'exceptions': [],
  'verification': ['Reconcile multiple payouts from export alone and verify totals and line '
                   'identities equal the product detail.'],
  'owner_hints': ['designing-marketplace-payout-status'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-payout-owners-v13'],
  'status': 'active'}]

__all__ = ["MARKETPLACE_PAYOUT_RULES_V13"]
