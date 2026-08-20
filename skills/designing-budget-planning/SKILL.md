---
name: designing-budget-planning
description: Use when this specialist's decision ownership is materially in scope. Own financial budget authoring across versions, periods, accounts/dimensions, assumptions, top-down and bottom-up inputs, allocations, scenarios, approvals, locks, and actual-versus-budget lineage.
---
# Designing Budget Planning

## Parent Contract

**Required parent:** `designing-financial-operations-workspaces`.

Inherit the broader routing and decision boundary from this canonical parent; this specialist remains accountable only for the narrower ownership, failure topology, falsification criteria, and output contract defined below.

## Decision ownership

Own planned financial amounts before they become actual transactions. Decide budget version/scenario, fiscal periods, accounts/dimensions, assumptions, allocation, ownership, workflow, top-down targets, bottom-up submissions, locking, revisions, and comparison to actuals. This owner does not forecast cash timing unless delegated.

## Inputs and evidence

Require fiscal calendar, chart of accounts, planning dimensions, currency/rate basis, organizational hierarchy, prior actuals, assumptions, scenario/version model, contributor roles, approval, allocation rules, and lock/calendar. Identify driver-based versus manual line-item budgets.

## Procedure

Anchor every plan to version/scenario/entity/period/currency basis. Separate baseline actuals, submitted plan, top-down target, approved budget, and forecast revisions. Provide spreadsheet-like editing only with stable account/dimension identity and clear formula/assumption provenance. Allocations disclose driver and resulting distributions. Scenario copy must not create indistinguishable versions. Approval freezes a known version; later revisions become a new forecast/version rather than mutating approved history. Variance views trace to actual and budget sources.

## Failure topology

Failures include users editing the approved budget silently, copied scenario overwriting baseline, formulas detached from assumptions, allocations not reconciling to source total, currencies mixed with unknown rate, and filtered subtotal mistaken for full budget. Another failure is many spreadsheet cells with no ownership/workflow state.

## Falsification

Reject if version/scenario is unknown; if approved values can mutate without revision history; if allocation totals do not reconcile; if currency/rate basis is absent; if formula/driver origin cannot be inspected; if contribution status/owner is missing; or if actual-vs-budget compares incompatible periods/scopes.

## Output contract

Return a `budget-planning-contract` with: entity/version/scenario; fiscal periods; currency/rates; account/dimension grid; assumptions/drivers; top-down/bottom-up states; allocation; contributor ownership; approval/lock; revision/forecast behavior; and actual-comparison lineage. Include one approved-budget revision scenario.

## Handoffs

Variance analysis consumes budget/actuals, cash forecasting converts plans into cash timing when appropriate, chart of accounts supplies dimensions, and approvals govern plan sign-off.