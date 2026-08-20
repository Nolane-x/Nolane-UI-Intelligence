---
name: designing-general-ledger-browsing
description: Use when this specialist's decision ownership is materially in scope. Own browsing and investigation of posted ledger entries by account, entity, period, source, journal, dimension, debit/credit, and running balance with audit-safe drill-down.
---
# Designing General Ledger Browsing

## Parent Contract

**Required parent:** `designing-financial-operations-workspaces`.

Inherit the broader routing and decision boundary from this canonical parent; this specialist remains accountable only for the narrower ownership, failure topology, falsification criteria, and output contract defined below.

## Decision ownership

Own read-oriented inspection of the general ledger. Decide account/period/entity context, debit/credit representation, running balance, dimensions, source links, journal grouping, posting status, filters, pagination/virtualization, and trace from summary balance to entry and originating document. This owner does not create journal entries or define accounting policy.

## Inputs and evidence

Require ledger entries with immutable IDs, account IDs, entity, posting date/period, debit/credit or signed amount convention, currency, dimensions, journal/source references, reversal links, posting status, and close state. Identify high-volume accounts and multi-currency reporting requirements.

## Procedure

Anchor the view to one entity, account scope, period/date range, and currency basis. Make debit/credit convention explicit and keep running balances deterministic under sorting/filter constraints; if arbitrary sort invalidates a running balance, disable or explain it. Group or link entries to journal batches and source documents without hiding individual postings. Filters on dimensions/project/cost center should show active scope and reconcile displayed totals. Reversal/adjustment relationships are navigable both ways. Virtualization/search must preserve stable row identity and exact amounts.

## Failure topology

Failures include running balance computed after a user sort that changes chronology, filters hiding rows while total remains unfiltered, reversal entries appearing unrelated, signed amount convention differing across pages, duplicate-looking entries with no immutable ID, and period-end postings shown in the wrong fiscal period due date confusion. Another failure is exporting rows without the context needed to reproduce the displayed balance.

## Falsification

Reject if debit/credit/sign convention is ambiguous; if running balance cannot state its ordering; if filtered row totals do not reconcile to displayed scope; if reversal/source lineage cannot be opened; if entity/period/currency context is missing; or if stable entry identity is lost under virtualization/export.

## Output contract

Return a `general-ledger-browsing-contract` with: entity/account/period; amount convention; currency basis; entry fields; chronological/running-balance rule; filters/dimensions; totals; journal/source/reversal links; stable identity; close status; and export context. Include one reversal and one re-sorted-running-balance case.

## Handoffs

Journal entry workflows create/adjust records, financial statements aggregate account balances, chart-of-accounts management supplies account semantics, and audit log/history preserves administrative changes.