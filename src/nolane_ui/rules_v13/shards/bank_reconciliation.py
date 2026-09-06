"""V13 eighth-wave independently authored rules for bank reconciliation."""
from __future__ import annotations

from ._capabilities import interaction_caps


RECONCILIATION_RULES_V13 = [{'rule_id': 'ui.reconciliation.statement-period-visible',
  'domain': 'reconciliation',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Bank reconciliation must expose the exact statement period being closed',
  'statement': 'Opening/closing balances and transaction inclusion only make sense relative to one '
               'explicit statement interval.',
  'intent': 'Prevent users from reconciling transactions against the wrong period.',
  'applies_when': ['A reconciliation session is tied to a bank statement or date range.'],
  'does_not_apply_when': [],
  'failure_modes': ['The user changes statement end date but the transaction list and closing '
                    'balance still reflect the previous period without warning.'],
  'user_impacts': ['A reconciliation can appear balanced while containing the wrong transactions.'],
  'observables': ['Change period boundaries and inspect opening balance, included transactions, '
                  'closing balance, and saved session state.'],
  'falsifiers': ['All reconciliation inputs resolve to one visible period and stale period-derived '
                 'data are invalidated on change.'],
  'repairs': ['Version the reconciliation session by statement period and recompute included '
              'transactions whenever boundaries change.'],
  'exceptions': [],
  'verification': ['Move period start/end across transaction dates and verify balances and '
                   'included items remain consistent.'],
  'owner_hints': ['designing-bank-reconciliation'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-reconciliation-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.reconciliation.matched-transaction-identity-stable',
  'domain': 'reconciliation',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Reconciliation matches must bind stable bank and ledger transaction identities',
  'statement': 'Description, date, and amount can change or collide; a match must remain tied to '
               'immutable records rather than display text.',
  'intent': 'Prevent previously reviewed matches from drifting to another transaction.',
  'applies_when': ['Users match imported bank transactions to ledger entries.'],
  'does_not_apply_when': [],
  'failure_modes': ['Two ledger rows share amount/date and a later edit causes an existing match '
                    'to silently point to the other row.'],
  'user_impacts': ['The reconciliation becomes incorrect without showing that the reviewed pairing '
                   'changed.'],
  'observables': ['Create duplicate-looking transactions, edit labels/dates, and inspect persisted '
                  'match relationships.'],
  'falsifiers': ['Each match retains immutable source identities and survives non-identity field '
                 'changes without retargeting.'],
  'repairs': ['Store explicit bank-to-ledger record IDs for matches and treat display similarity '
              'only as suggestion evidence.'],
  'exceptions': [],
  'verification': ['Edit matched and neighboring transactions and verify match identity never '
                   'changes unless the user rematches it.'],
  'owner_hints': ['designing-bank-reconciliation'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-reconciliation-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.reconciliation.split-match-sum-consistent',
  'domain': 'reconciliation',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Split reconciliation matches must keep component sums equal to the bank transaction',
  'statement': 'One bank line can map to multiple ledger entries, but the split is valid only when '
               'component amounts reconcile to the authoritative total.',
  'intent': 'Prevent partially allocated or over-allocated matches from appearing complete.',
  'applies_when': ['The product supports one-to-many or many-to-one reconciliation.'],
  'does_not_apply_when': [],
  'failure_modes': ['A $1,000 bank deposit is marked matched even though its selected ledger '
                    'components total only $980.'],
  'user_impacts': ['Unreconciled differences can be hidden inside a completed match.'],
  'observables': ['Create split matches with exact, under, over, and currency-rounded sums and '
                  'inspect completion state.'],
  'falsifiers': ['A split cannot become fully matched unless component sum and allowed rounding '
                 'rules reconcile to the target.'],
  'repairs': ['Calculate split residual explicitly and keep the match incomplete while nonzero '
              'residual remains.'],
  'exceptions': [],
  'verification': ['Vary component amounts and verify completion toggles only at a reconciled sum '
                   'under the disclosed currency precision.'],
  'owner_hints': ['designing-bank-reconciliation'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-reconciliation-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.reconciliation.duplicate-bank-feed-transaction-visible',
  'domain': 'reconciliation',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Potential duplicate bank-feed transactions must remain visible and distinguishable '
           'from legitimate repeats',
  'statement': 'Feed retries can import duplicate events, but identical real transactions also '
               'occur; deduplication must preserve review evidence.',
  'intent': 'Prevent silent deletion or double-counting of imported bank activity.',
  'applies_when': ['Bank transactions arrive through external feeds that may retry or resend.'],
  'does_not_apply_when': [],
  'failure_modes': ['The importer collapses two same-day same-amount charges without retaining '
                    'source IDs, deleting a legitimate repeated purchase.'],
  'user_impacts': ['Balances and reconciliation decisions can be wrong with no trace of the '
                   'removed item.'],
  'observables': ['Replay provider events and create genuine duplicate-looking transactions while '
                  'inspecting source IDs and dedup decisions.'],
  'falsifiers': ['Potential duplicates retain source evidence and any suppression/merge decision '
                 'is reviewable and reversible.'],
  'repairs': ['Deduplicate using provider identity/provenance rather than presentation similarity '
              'and preserve contributing records.'],
  'exceptions': [],
  'verification': ['Test resend, correction, and legitimate-repeat scenarios and verify no '
                   'transaction disappears without explicit lineage.'],
  'owner_hints': ['designing-bank-reconciliation'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-reconciliation-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.reconciliation.opening-closing-balance-consistent',
  'domain': 'reconciliation',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Opening balance, activity, and closing balance must reconcile mathematically',
  'statement': 'A reconciliation session should preserve the accounting equation connecting prior '
               'close, included activity, and current close.',
  'intent': 'Detect state drift that would otherwise be hidden behind matched transaction counts.',
  'applies_when': ['The workflow presents opening and closing statement balances.'],
  'does_not_apply_when': [],
  'failure_modes': ['All transactions are marked matched but opening plus period activity does not '
                    'equal the closing balance shown.'],
  'user_impacts': ['Users can close a reconciliation that is numerically inconsistent.'],
  'observables': ['Modify opening balance, included items, and closing balance while observing '
                  'residual/difference state.'],
  'falsifiers': ['The displayed difference derives from the same signed amounts and reaches zero '
                 'only when the statement equation balances.'],
  'repairs': ['Centralize balance arithmetic and expose the residual independently from match '
              'completion.'],
  'exceptions': [],
  'verification': ['Test positive/negative balances and mixed credits/debits, verifying the '
                   'equation and residual remain exact.'],
  'owner_hints': ['designing-bank-reconciliation'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-reconciliation-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.reconciliation.lock-state-visible',
  'domain': 'reconciliation',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Closed reconciliation periods must expose their lock state before mutation',
  'statement': 'A locked period constrains edits because changes can invalidate later '
               'reconciliations; the restriction must be visible and enforceable.',
  'intent': 'Prevent silent edits to financially closed history.',
  'applies_when': ['The product allows completed reconciliation periods to be locked or closed.'],
  'does_not_apply_when': [],
  'failure_modes': ['A ledger entry inside a closed period remains editable from another screen '
                    'with no indication that it affects a locked reconciliation.'],
  'user_impacts': ['Historical reports and subsequent opening balances can become inconsistent.'],
  'observables': ['Close a period, attempt edits through every transaction surface, and inspect '
                  'warnings, permissions, and reopen flow.'],
  'falsifiers': ['Lock state is visible on affected records and unauthorized mutations cannot '
                 'bypass it through alternate interfaces.'],
  'repairs': ['Enforce period lock in the write path and link blocked edits to the '
              'reconciliation/reopen authority.'],
  'exceptions': [],
  'verification': ['Attempt direct, bulk, import, and API-backed edits to locked-period records '
                   'and verify enforcement is consistent.'],
  'owner_hints': ['designing-bank-reconciliation'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-reconciliation-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.reconciliation.late-transaction-after-lock-visible',
  'domain': 'reconciliation',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Late transactions entering a locked period must create an explicit reconciliation '
           'exception',
  'statement': 'New or corrected bank activity can arrive after a period is closed; it must not '
               'silently alter closed totals.',
  'intent': 'Preserve closed-period integrity while exposing newly discovered activity.',
  'applies_when': ['External feeds or ledger corrections can add transactions dated inside a '
                   'locked period.'],
  'does_not_apply_when': [],
  'failure_modes': ['A delayed bank transaction appears inside last month and silently changes the '
                    'historical balance without reopening or exception state.'],
  'user_impacts': ['Previously approved reconciliation evidence no longer matches the ledger.'],
  'observables': ['Inject delayed and corrected transactions into locked periods and inspect '
                  'history, balances, alerts, and reopen choices.'],
  'falsifiers': ['Late activity is flagged as an exception with a deliberate reopen or next-period '
                 'adjustment path; closed evidence is not silently rewritten.'],
  'repairs': ['Detect effective-date overlap with locked periods and create a reconciliation '
              'exception record.'],
  'exceptions': [],
  'verification': ['Add late entries before/after lock and verify historical close remains '
                   'immutable until an authorized resolution occurs.'],
  'owner_hints': ['designing-bank-reconciliation'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-reconciliation-owners-v13'],
  'status': 'active'},
 {'rule_id': 'ui.reconciliation.unreconciled-export-consistent',
  'domain': 'reconciliation',
  'class': 'behavioral',
  'severity': 'major',
  'enforcement': 'block',
  'title': 'Unreconciled transaction exports must preserve the exact session filters and residual '
           'state',
  'statement': 'Exports used for follow-up must represent the same unmatched population and period '
               'the user reviewed.',
  'intent': 'Prevent offline reconciliation work from starting from a different population than '
            'the product.',
  'applies_when': ['Users can export unmatched or exception transactions from a reconciliation '
                   'session.'],
  'does_not_apply_when': [],
  'failure_modes': ['The UI shows twelve unmatched rows but the export contains fifteen because it '
                    'ignores a statement-period filter.'],
  'user_impacts': ['Finance teams can investigate or modify the wrong transactions.'],
  'observables': ['Export under varying periods, account filters, match states, and exceptions, '
                  'then compare identities and residual amounts.'],
  'falsifiers': ['Exported rows and session metadata reconcile exactly to the displayed '
                 'unreconciled population.'],
  'repairs': ['Generate exports from the canonical reconciliation query/snapshot and include '
              'session/period identifiers.'],
  'exceptions': [],
  'verification': ['Compare exported IDs and totals with the UI under changing filters and verify '
                   'exact population consistency.'],
  'owner_hints': ['designing-bank-reconciliation'],
  'verifier_hints': ['critiquing-functional-completeness'],
  'capabilities': interaction_caps(),
  'provenance_ids': ['nui-reconciliation-owners-v13'],
  'status': 'active'}]

__all__ = ["RECONCILIATION_RULES_V13"]
