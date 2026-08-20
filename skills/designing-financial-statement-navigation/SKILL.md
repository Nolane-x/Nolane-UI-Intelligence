---
name: designing-financial-statement-navigation
description: Use when this specialist's decision ownership is materially in scope. Own navigation of balance sheet, income statement, cash-flow and related financial reports from statement lines to account/transaction evidence with period, entity, currency, consolidation, and restatement context.
---
# Designing Financial Statement Navigation

## Parent Contract

**Required parent:** `designing-financial-operations-workspaces`.

Inherit the broader routing and decision boundary from this canonical parent; this specialist remains accountable only for the narrower ownership, failure topology, falsification criteria, and output contract defined below.

## Decision ownership

Own the user experience of formal financial statements as structured, drillable reports. Decide statement hierarchy, current/comparative periods, entity/consolidation scope, currency basis, subtotal logic, sign conventions, notes, drill-down to accounts/entries, restatement/version status, and export. This owner does not define accounting standards.

## Inputs and evidence

Require report definitions, account mapping, fiscal periods, entities/consolidation, currency/translation, eliminations, prior periods, restatements, close status, audit/report version, and source ledger. Identify lines derived by formulas rather than direct account sums.

## Procedure

Persistently show statement type, entity/consolidation, period/comparison, currency and status (draft/closed/restated). Use hierarchy and subtotal conventions consistently, with sign meaning recoverable. Each material line should drill to mapped accounts/calculation and then ledger entries where permissions allow. Comparative columns must align periods and accounting basis. Restated reports need version/history and explanation of changed lines. Filters beyond official statement scope should be clearly labeled as analysis, not the canonical statement.

## Failure topology

Failures include sign conventions flipping between statement and ledger, drill-down totals not reconciling due hidden filters, comparative periods mismatched, restated prior figures replacing original history, consolidation eliminations invisible, and exported statements lacking scope/currency. Another failure is ad hoc user filters making an official-looking but noncanonical report.

## Falsification

Reject if line totals cannot trace to calculation/accounts; if drill-down does not reconcile; if period/entity/currency basis is hidden; if restatement overwrites original version; if comparative basis is incompatible without warning; or if analytical filters can masquerade as canonical statement output.

## Output contract

Return a `financial-statement-navigation-contract` with: statement/version; entity/consolidation; period/comparison; currency basis; line hierarchy/formulas; sign conventions; account/ledger drill-down; eliminations; close/restatement status; analytical-filter distinction; and export context. Include one restated comparative-period case.

## Handoffs

Ledger browsing provides entries, chart of accounts supplies mapping, variance analysis compares statements/plans, and file/export owners serialize the defined report.