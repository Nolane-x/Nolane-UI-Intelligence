---
name: designing-bank-reconciliation
description: Use when this specialist's decision ownership is materially in scope. Own matching bank-statement/feed items to ledger transactions, including one-to-many splits, timing differences, fees, duplicates, unmatched items, balance proof, and reconciliation closure.
---
# Designing Bank Reconciliation

## Parent Contract

**Required parent:** `designing-financial-operations-workspaces`.

Inherit the broader routing and decision boundary from this canonical parent; this specialist remains accountable only for the narrower ownership, failure topology, falsification criteria, and output contract defined below.

## Decision ownership

Own the process that proves cash ledger records agree with an external bank source for a statement period. Decide statement/feed identity, opening/closing balances, match suggestions, exact/partial/one-to-many matches, adjustments, outstanding items, duplicates, reconciliation difference, and final close. This owner does not initiate payments.

## Inputs and evidence

Require bank account identity, statement period/balance, imported transactions, ledger cash entries, currencies, dates, references, amounts, matching rules/confidence, fees/interest capability, prior reconciliation, and permissions. Identify pending bank items and ledger transactions that legitimately clear later.

## Procedure

Anchor to one bank account and statement/feed period with expected ending balance. Present bank and ledger items with stable IDs and matching evidence. Suggestions show confidence/reasons but require review proportional to ambiguity. Support one-to-one, one-to-many, many-to-one, split, and adjustment workflows with conservation of amounts. Outstanding timing differences remain explicitly unreconciled rather than forced. Continuously calculate reconciled balance and unexplained difference. Closing locks the reconciliation snapshot and produces a report; later changes require reopen/correction policy.

## Failure topology

Failures include automatic match based only on equal amount/date, duplicate feed entries matched twice, split amounts not reconciling, pending items treated as missing, user forcing difference to zero through unexplained adjustment, and statement account confused across similar names. Another failure is a zero difference that hides excluded/unimported statement transactions.

## Falsification

Reject if a match cannot reveal contributing bank/ledger IDs; if amounts fail conservation; if duplicates can be matched twice; if statement opening/closing balances are absent; if unexplained adjustments lack reason/account; if a closed reconciliation can mutate silently; or if zero difference cannot prove all in-scope statement items were considered.

## Output contract

Return a `bank-reconciliation-contract` with: bank account/statement identity; opening/closing balance; bank/ledger item identities; match types/confidence; split/merge amount accounting; outstanding items; adjustments; duplicate handling; reconciliation difference; close/reopen policy; and audit report. Include one one-to-many match and one duplicate-feed case.

## Handoffs

Ledger browsing provides book entries, cash forecasting may consume reconciled balances, accounts payable/receivable create source transactions, and import/file workflows handle bank data ingestion.