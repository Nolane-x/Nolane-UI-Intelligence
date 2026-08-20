---
name: designing-accounts-receivable-workflows
description: Use when this specialist's decision ownership is materially in scope. Own receivable operations across customer invoices, balances, due status, receipts, allocations, partial payments, credits, disputes, aging, collections, and write-off evidence.
---
# Designing Accounts Receivable Workflows

## Parent Contract

**Required parent:** `designing-financial-operations-workspaces`.

Inherit the broader routing and decision boundary from this canonical parent; this specialist remains accountable only for the narrower ownership, failure topology, falsification criteria, and output contract defined below.

## Decision ownership

Own lifecycle of amounts owed by customers after invoicing. Decide invoice/open-item identity, due state, receipt allocation, partial/overpayment, credits, disputes, aging buckets, collection activity, promise-to-pay, and write-off/adjustment handoff. This owner does not design checkout or initial purchase flow.

## Inputs and evidence

Require customer/entity identity, invoices, currencies, payment terms, receipts, credit notes, unapplied cash, disputes, aging policy, collection notes, write-off authority, and ledger integration. Identify one receipt paying multiple invoices and cross-currency limitations.

## Procedure

Keep customer and legal entity explicit. Display open items with original amount, applied, remaining, due date, age, dispute/hold, and currency. Receipt allocation must conserve amount and support partial/multiple invoice matching plus unapplied remainder. Credits and write-offs remain distinct from cash receipts. Aging is derived from due policy and date basis, not a mutable label. Collection notes/promises have owner/date and do not change accounting balance until actual transactions occur. Closed items retain allocation history.

## Failure topology

Failures include receipt allocated twice, partial payment shown as fully paid, credit note confused with cash, aging based on invoice date when policy uses due date, disputed invoice pursued without cue, and unapplied cash disappearing from customer balance context. Another failure is collections promise treated as received payment.

## Falsification

Reject if receipt allocation cannot reconcile to receipt amount; if remaining balance is unexplained; if cash/credit/write-off types are conflated; if aging basis is hidden; if dispute state can be missed in collections flow; if promise-to-pay affects ledger balance; or if closed invoice cannot reveal allocation history.

## Output contract

Return an `accounts-receivable-workflows-contract` with: customer/entity; invoice/open-item identity; original/applied/remaining; due/aging basis; receipt allocation; partial/overpayment/unapplied cash; credits; disputes; collection notes/promises; write-off handoff; and closed-item history. Include one multi-invoice receipt scenario.

## Handoffs

Ledger/journal record accounting effects, cash forecasting consumes expected/received cash, financial transaction systems may provide receipt feeds, and approvals govern write-off authority.