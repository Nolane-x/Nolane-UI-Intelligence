"""V13 eighth-wave independently authored rules for trading order."""
from __future__ import annotations

from ._capabilities import interaction_caps


TRADING_RULES_V13 = [{'rule_id': 'ui.trading.side-symbol-venue-bound',
  'domain': 'trading',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Trading orders must bind side, instrument, and venue as one reviewable identity',
  'statement': 'Buy or sell intent is meaningful only with the exact instrument and execution '
               'venue; those fields must not drift independently between quote and submit.',
  'intent': 'Prevent orders from being sent for the wrong instrument, direction, or venue after '
            'context changes.',
  'applies_when': ['An order ticket can change symbol, side, account, or venue before submission.'],
  'does_not_apply_when': [],
  'failure_modes': ['The user switches from ABC to XYZ after entering quantity, but the '
                    'confirmation still shows the prior quote while submit targets XYZ.'],
  'user_impacts': ['An irreversible order can be sent with parameters that were never reviewed '
                   'together.'],
  'observables': ['Change symbol, side, and venue after quote retrieval and inspect confirmation, '
                  'request payload, and resulting order.'],
  'falsifiers': ['The submitted order matches one coherent reviewed tuple of side, instrument, and '
                 'venue.'],
  'repairs': ['Version the order draft and invalidate stale quote/confirmation context whenever '
              'identity fields change.'],
  'exceptions': [],
  'verification': ['Mutate identity fields at each step and verify submit cannot combine values '
                   'from different draft versions.'],
  'owner_hints': ['designing-trading-order-entry'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-trading-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.trading.quantity-distinct-from-notional',
  'domain': 'trading',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Trading quantity and notional amount must remain distinct and explicitly labeled',
  'statement': 'Units/shares/contracts and currency notional are different order semantics and '
               'conversion between them can depend on price.',
  'intent': 'Prevent users from submitting a magnitude different from what they intended.',
  'applies_when': ['Order entry supports quantity-based and notional-based orders.'],
  'does_not_apply_when': [],
  'failure_modes': ['The ticket retains “100” when switching from shares to dollars, silently '
                    'changing a 100-share order into a $100 order.'],
  'user_impacts': ['Users can create dramatically under- or oversized orders.'],
  'observables': ['Switch input mode with populated values and inspect labels, conversions, '
                  'validation, and submitted fields.'],
  'falsifiers': ['Input mode, unit, and resulting order field remain explicit and stale numeric '
                 'values are not silently reinterpreted.'],
  'repairs': ['Store quantity and notional as separate typed fields and require deliberate '
              'conversion when mode changes.'],
  'exceptions': [],
  'verification': ['Toggle modes under changing prices and verify the transmitted order exactly '
                   'matches the labeled amount type.'],
  'owner_hints': ['designing-trading-order-entry'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-trading-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.trading.order-type-parameters-complete',
  'domain': 'trading',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Trading order types must require every parameter needed for their execution semantics',
  'statement': 'Limit, stop, stop-limit, trailing, and time-in-force choices are incomplete '
               'without their dependent values.',
  'intent': 'Prevent partially configured orders from being accepted under unintended defaults.',
  'applies_when': ['The ticket supports order types with conditional price or duration '
                   'parameters.'],
  'does_not_apply_when': [],
  'failure_modes': ['A stop-limit order is submitted with a stop price but the hidden limit price '
                    'remains from an earlier draft.'],
  'user_impacts': ['Execution behavior can differ materially from the visible configuration.'],
  'observables': ['Switch among order types after entering parameters and inspect which fields '
                  'persist, clear, validate, and submit.'],
  'falsifiers': ['Only parameters valid for the selected type are present and all required '
                 'dependent values are explicit before submit.'],
  'repairs': ['Model each order type with a typed parameter schema and clear incompatible stale '
              'values on transition.'],
  'exceptions': [],
  'verification': ['Exercise every order-type transition and verify submitted payload contains '
                   'exactly the required reviewed parameters.'],
  'owner_hints': ['designing-trading-order-entry'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-trading-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.trading.estimated-distinct-from-executable-price',
  'domain': 'trading',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Estimated prices must not be presented as guaranteed executable prices',
  'statement': 'Market impact, spread, latency, and order type can make an estimate differ from '
               'actual execution.',
  'intent': 'Prevent users from reading indicative pricing as a firm execution promise.',
  'applies_when': ['The product shows estimated proceeds, cost, or price before execution.'],
  'does_not_apply_when': [],
  'failure_modes': ['A market order preview says “Price $20.00” with no estimate marker even '
                    'though the trade can fill at multiple prices.'],
  'user_impacts': ['Users can make decisions based on a price the venue never guaranteed.'],
  'observables': ['Change spread and market depth between preview and execution and compare '
                  'estimated versus fill price labeling.'],
  'falsifiers': ['Indicative values are labeled as estimates and final fills remain separately '
                 'authoritative.'],
  'repairs': ['Carry price provenance and estimate status into the review UI; never reuse an '
              'indicative quote as fill truth.'],
  'exceptions': [],
  'verification': ['Execute under moving prices and verify preview and fill values remain '
                   'semantically distinct.'],
  'owner_hints': ['designing-trading-order-entry'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-trading-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.trading.market-session-state-visible',
  'domain': 'trading',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Trading tickets must expose the effective market session and eligibility state',
  'statement': 'Regular, pre-market, after-hours, auction, and closed sessions can change routing '
               'and order eligibility.',
  'intent': 'Prevent orders from being submitted under session assumptions different from the '
            'venue state.',
  'applies_when': ['Instrument trading rules depend on market session.'],
  'does_not_apply_when': [],
  'failure_modes': ['The ticket appears normal after the regular close but the order is queued for '
                    'the next session without explaining that behavior.'],
  'user_impacts': ['Users may expect immediate execution when the order cannot trade now.'],
  'observables': ['Cross session boundaries with open tickets and inspect eligibility, routing '
                  'choices, time-in-force, and confirmation.'],
  'falsifiers': ['The effective session and consequences for execution or queuing are visible '
                 'before submit.'],
  'repairs': ['Resolve session state from authoritative market calendars and revalidate when an '
              'open ticket crosses a boundary.'],
  'exceptions': [],
  'verification': ['Hold a ticket across session changes and verify submission behavior matches '
                   'the newly disclosed session.'],
  'owner_hints': ['designing-trading-order-entry'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-trading-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.trading.partial-fill-lifecycle-visible',
  'domain': 'trading',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Partially filled orders must expose filled, remaining, and active quantities '
           'separately',
  'statement': 'An order can be partly executed while the remainder stays open; a single status or '
               'quantity hides what remains at risk.',
  'intent': 'Keep order lifecycle and remaining exposure understandable.',
  'applies_when': ['Orders can fill in multiple executions.'],
  'does_not_apply_when': [],
  'failure_modes': ['A 100-share order fills 30 shares but the UI says “filled” and still displays '
                    '100 as the order quantity.'],
  'user_impacts': ['Users can duplicate remaining exposure or assume the order is complete.'],
  'observables': ['Generate multiple fills, cancel the remainder, and inspect order detail, '
                  'positions, and execution history.'],
  'falsifiers': ['Original, filled, remaining, canceled, and executed quantities reconcile and '
                 'remain visibly distinct.'],
  'repairs': ['Track executions as immutable child records and derive remaining quantity from '
              'authoritative order state.'],
  'exceptions': [],
  'verification': ['Apply partial fills and cancellation in different orders and verify quantities '
                   'and status reconcile exactly.'],
  'owner_hints': ['designing-trading-order-entry'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-trading-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.trading.cancel-replace-race-reconciled',
  'domain': 'trading',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Cancel-replace races must reconcile against fills and acknowledgments that occur '
           'concurrently',
  'statement': 'An order may fill while a cancel or replacement is in flight; local optimistic '
               'state must converge to venue truth.',
  'intent': 'Prevent duplicate exposure or phantom cancellations during concurrent order '
            'transitions.',
  'applies_when': ['The platform supports cancel or replace of active orders.'],
  'does_not_apply_when': [],
  'failure_modes': ['The UI reports an order canceled, submits a replacement, and later receives a '
                    'fill for the supposedly canceled original.'],
  'user_impacts': ['Users can end up with more exposure than the interface showed.'],
  'observables': ['Race fills against cancel and replace acknowledgments while delaying and '
                  'reordering events.'],
  'falsifiers': ['The UI preserves venue event ordering and reports any late fill/conflict before '
                 'presenting a replacement as final.'],
  'repairs': ['Link cancel/replace requests to immutable order versions and reconcile asynchronous '
              'fills before finalizing replacement state.'],
  'exceptions': [],
  'verification': ['Replay fill/cancel/replace events in different arrival orders and verify final '
                   'exposure matches venue truth.'],
  'owner_hints': ['designing-trading-order-entry'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-trading-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.trading.quote-freshness-visible',
  'domain': 'trading',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Trading quotes must expose freshness when used to support an order decision',
  'statement': 'A price snapshot can become stale rapidly; users need to know whether preview '
               'calculations are based on current or aged market data.',
  'intent': 'Prevent stale quote data from masquerading as current market context.',
  'applies_when': ['Order entry displays real-time or delayed quotes and calculations.'],
  'does_not_apply_when': [],
  'failure_modes': ['A quote remains on screen after the feed stalls but retains the same styling '
                    'and no timestamp.'],
  'user_impacts': ['Users may size or place orders using materially outdated information.'],
  'observables': ['Pause quote updates and compare timestamp, stale indication, preview '
                  'calculations, and submit behavior.'],
  'falsifiers': ['Quote age/source are visible and stale data are not represented as fresh; '
                 'critical calculations revalidate when required.'],
  'repairs': ['Propagate market-data freshness into the ticket and distinguish live, delayed, '
              'stale, and unavailable states.'],
  'exceptions': [],
  'verification': ['Interrupt and resume the feed and verify displayed freshness and calculations '
                   'track the actual quote watermark.'],
  'owner_hints': ['designing-trading-order-entry'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-trading-owners-v13'],
  'status': 'active'}]

__all__ = ["TRADING_RULES_V13"]
