"""V13 eighth-wave independently authored rules for portfolio monitoring."""
from __future__ import annotations

from ._capabilities import interaction_caps


PORTFOLIO_RULES_V13 = [{'rule_id': 'ui.portfolio.position-quantity-and-value-source-visible',
  'domain': 'portfolio',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Portfolio positions must expose the source basis for quantity and valuation',
  'statement': 'Position quantity and market value may come from different ledgers and price '
               'feeds; their source basis should be inspectable.',
  'intent': 'Prevent users from treating a derived valuation as if every underlying component were '
            'equally fresh and settled.',
  'applies_when': ['A portfolio combines ledger positions with external price data.'],
  'does_not_apply_when': [],
  'failure_modes': ['The position quantity is current but market value uses yesterday’s close with '
                    'no indication that the sources differ.'],
  'user_impacts': ['Users can make allocation decisions from a value whose basis they '
                   'misunderstand.'],
  'observables': ['Delay price data independently from ledger updates and inspect quantity, value, '
                  'timestamps, and drilldowns.'],
  'falsifiers': ['Quantity and valuation sources/freshness are individually identifiable and '
                 'reconcile to the displayed value.'],
  'repairs': ['Carry ledger and price provenance separately into each position snapshot.'],
  'exceptions': [],
  'verification': ['Update quantity and price feeds out of phase and verify the portfolio never '
                   'hides which source drives each field.'],
  'owner_hints': ['designing-portfolio-position-monitoring'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-portfolio-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.portfolio.price-timestamp-visible',
  'domain': 'portfolio',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Portfolio valuations must show the timestamp or market basis of the price used',
  'statement': 'A valuation without price time can appear current even when the market is closed '
               'or the feed is stale.',
  'intent': 'Keep portfolio valuation freshness explicit whenever users compare or act on reported market values.',
  'applies_when': ['Position values depend on market prices that update over time.'],
  'does_not_apply_when': [],
  'failure_modes': ['A portfolio total changes only once per day but appears as a live number with '
                    'no price timestamp.'],
  'user_impacts': ['Users can interpret stale value as present market value.'],
  'observables': ['Pause price feeds, cross market close, and inspect position and portfolio-level '
                  'timestamps.'],
  'falsifiers': ['The valuation displays or exposes the price time/basis and aggregates do not '
                 'imply fresher data than constituents.'],
  'repairs': ['Persist price timestamp with each valuation and propagate the oldest/material '
              'freshness state to rollups.'],
  'exceptions': [],
  'verification': ['Freeze selected price feeds and verify affected positions and totals disclose '
                   'stale valuation basis.'],
  'owner_hints': ['designing-portfolio-position-monitoring'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-portfolio-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.portfolio.settled-distinct-from-unsettled',
  'domain': 'portfolio',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Portfolio views must distinguish settled from unsettled positions and cash',
  'statement': 'Recent trades can affect economic exposure before settlement; combining both '
               'states can misstate spendable cash or transferable holdings.',
  'intent': 'Prevent actions based on assets that are not yet settled.',
  'applies_when': ['The portfolio includes trades or cash movements subject to settlement.'],
  'does_not_apply_when': [],
  'failure_modes': ['A sale immediately increases “available cash” even though proceeds are '
                    'unsettled and cannot yet be withdrawn.'],
  'user_impacts': ['Users may initiate transfers or trades that the account cannot support.'],
  'observables': ['Create buys/sells across settlement dates and inspect holdings, cash, buying '
                  'power, and transfer eligibility.'],
  'falsifiers': ['Settled and unsettled components remain separately visible and action '
                 'eligibility follows authoritative settlement rules.'],
  'repairs': ['Track settlement state explicitly for positions and cash rather than folding '
              'pending events into final balances.'],
  'exceptions': [],
  'verification': ['Advance through settlement and verify amounts move between unsettled and '
                   'settled exactly once.'],
  'owner_hints': ['designing-portfolio-position-monitoring'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-portfolio-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.portfolio.base-currency-visible',
  'domain': 'portfolio',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Portfolio rollups must expose the base currency used for converted totals',
  'statement': 'Cross-currency holdings cannot be meaningfully aggregated without disclosing '
               'conversion currency and basis.',
  'intent': 'Prevent users from reading a converted aggregate as native instrument value.',
  'applies_when': ['A portfolio contains assets denominated in multiple currencies.'],
  'does_not_apply_when': [],
  'failure_modes': ['A total shows 50,000 with no currency label while individual positions are '
                    'USD, EUR, and JPY.'],
  'user_impacts': ['Users can misread both scale and FX exposure.'],
  'observables': ['Change reporting currency and inspect totals, position conversions, gains, and '
                  'exports.'],
  'falsifiers': ['Every rollup states its base currency and converted position values remain '
                 'distinguishable from native values.'],
  'repairs': ['Store native amounts separately and calculate rollups using an explicit selected '
              'base currency and FX snapshot.'],
  'exceptions': [],
  'verification': ['Switch base currencies and verify native amounts remain unchanged while '
                   'rollups and FX metadata update consistently.'],
  'owner_hints': ['designing-portfolio-position-monitoring'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-portfolio-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.portfolio.cost-basis-method-visible',
  'domain': 'portfolio',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Portfolio gains must disclose the cost-basis method used',
  'statement': 'FIFO, average cost, specific identification, and jurisdictional methods can '
               'produce different gain values from the same trades.',
  'intent': 'Prevent users from treating one computed gain as method-independent truth.',
  'applies_when': ['The product calculates realized or unrealized gains from transaction history.'],
  'does_not_apply_when': [],
  'failure_modes': ['A realized gain is displayed without revealing that FIFO was used even though '
                    'the account supports specific-lot selection.'],
  'user_impacts': ['Users can misunderstand tax or performance figures.'],
  'observables': ['Create multiple acquisition lots and compare gain outputs under supported '
                  'cost-basis methods.'],
  'falsifiers': ['The effective method is visible and lot-level calculations reconcile to the '
                 'displayed gain.'],
  'repairs': ['Bind gain calculations to an explicit cost-basis policy and preserve lot lineage '
              'used in each result.'],
  'exceptions': [],
  'verification': ['Switch or simulate supported methods and verify displayed gain and lot '
                   'attribution follow the disclosed policy.'],
  'owner_hints': ['designing-portfolio-position-monitoring'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-portfolio-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.portfolio.corporate-action-pending-state-visible',
  'domain': 'portfolio',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Pending corporate actions must remain visible until position adjustments are '
           'authoritative',
  'statement': 'Splits, mergers, dividends, and symbol changes can create temporary discrepancies '
               'between market and ledger state.',
  'intent': 'Prevent transient corporate-action processing from looking like unexplained loss or '
            'duplication.',
  'applies_when': ['Positions are affected by corporate actions processed asynchronously.'],
  'does_not_apply_when': [],
  'failure_modes': ['A stock split occurs and price halves before share quantity updates, making '
                    'the portfolio appear to lose 50% with no pending-action indicator.'],
  'user_impacts': ['Users may react to a temporary processing mismatch as if it were real '
                   'performance.'],
  'observables': ['Simulate corporate-action timing gaps between price, security master, and '
                  'position ledger updates.'],
  'falsifiers': ['Pending corporate-action state is visible and related fields reconcile when '
                 'processing completes.'],
  'repairs': ['Attach corporate-action lifecycle metadata to affected positions and suppress '
              'misleading derived performance until inputs are coherent.'],
  'exceptions': [],
  'verification': ['Stagger split/merger processing inputs and verify the UI exposes the pending '
                   'state rather than a false gain/loss.'],
  'owner_hints': ['designing-portfolio-position-monitoring'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-portfolio-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.portfolio.rollup-drilldown-population-consistent',
  'domain': 'portfolio',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Portfolio rollups must drill down to the same position population they aggregate',
  'statement': 'Totals grouped by account, asset class, sector, or strategy must open details '
               'derived from the same snapshot and filters.',
  'intent': 'Keep aggregate-to-position investigation trustworthy.',
  'applies_when': ['Portfolio summaries support filtered or grouped drilldowns.'],
  'does_not_apply_when': [],
  'failure_modes': ['An asset-class total is based on a prior snapshot, but clicking it opens '
                    'current positions whose values no longer sum to the displayed total.'],
  'user_impacts': ['Users cannot reconcile the portfolio and may misattribute exposure.'],
  'observables': ['Change positions between summary load and drilldown and compare member '
                  'identities, values, and snapshot time.'],
  'falsifiers': ['The drilldown either uses the same snapshot/population or explicitly refreshes '
                 'both total and members together.'],
  'repairs': ['Carry aggregate snapshot and filter identity into drilldown navigation.'],
  'exceptions': [],
  'verification': ['Race position updates against drilldown and verify member sum always '
                   'reconciles to the displayed aggregate or a refresh boundary is shown.'],
  'owner_hints': ['designing-portfolio-position-monitoring'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-portfolio-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.portfolio.zero-distinct-from-unavailable',
  'domain': 'portfolio',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Portfolio metrics must distinguish a true zero from unavailable or unpriced data',
  'statement': 'Zero exposure, zero gain, missing price, unsupported metric, and pending '
               'calculation are different states.',
  'intent': 'Prevent missing valuation from being mistaken for no value or no risk.',
  'applies_when': ['Portfolio fields can be unavailable because of missing price, history, or '
                   'unsupported instruments.'],
  'does_not_apply_when': [],
  'failure_modes': ['An unpriced private asset displays market value $0, causing the total to '
                    'imply the asset is worthless.'],
  'user_impacts': ['Users can underestimate assets or exposure.'],
  'observables': ['Remove price/history inputs for selected instruments and inspect position '
                  'fields and rollups.'],
  'falsifiers': ['Unavailable values render as unavailable/pending with cause, while real numeric '
                 'zero remains a valid explicit value.'],
  'repairs': ['Use typed missingness states and exclude or separately account for unavailable '
              'components in aggregates.'],
  'exceptions': [],
  'verification': ['Test genuine zero and each missing-data cause, verifying the UI and totals '
                   'never conflate them.'],
  'owner_hints': ['designing-portfolio-position-monitoring'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-portfolio-owners-v13'],
  'status': 'active'}]

__all__ = ["PORTFOLIO_RULES_V13"]
