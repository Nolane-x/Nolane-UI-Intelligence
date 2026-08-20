---
name: designing-chart-of-accounts-management
description: Use when this specialist's decision ownership is materially in scope. Own lifecycle and governance of financial accounts across codes, names, types, hierarchy, entity availability, effective dates, dimensions, mappings, deactivation, merge/reclassification, and downstream impact.
---
# Designing Chart of Accounts Management

## Parent Contract

**Required parent:** `designing-financial-operations-workspaces`.

Inherit the broader routing and decision boundary from this canonical parent; this specialist remains accountable only for the narrower ownership, failure topology, falsification criteria, and output contract defined below.

## Decision ownership

Own administrative management of accounting account definitions used across journals, reporting, budgets, and integrations. Decide account identity/code, type, hierarchy, effective availability, entity scope, dimensions/defaults, statement mappings, deactivation, rename, merge/reclassification, and change impact. This owner does not decide accounting policy but protects historical consistency.

## Inputs and evidence

Require account schema, codes/names, types, parent hierarchy, legal entities, effective dates, active postings, financial statement mappings, tax mappings, dimensions, permissions, integration references, and close/history requirements. Identify immutable identifiers separate from user-visible account codes.

## Procedure

Use stable internal account identity so code/name changes do not break history. Validate type/hierarchy and unique codes within scope. Before changing mappings, type, or hierarchy, show downstream impact on reporting/budgets/integrations. Accounts with historical postings generally deactivate rather than delete. Merge/reclassification should create explicit mappings/effective dates and preserve old identifiers. New accounts require effective date/entity scope and required reporting/tax mappings per policy. Search/selectors show inactive status and prevent new use where prohibited while historical records remain readable.

## Failure topology

Failures include deleting used accounts, reusing an old code for a different account, hierarchy changes restating reports unintentionally, inactive accounts still selectable for new journals, mappings changed with no effective date, and code rename breaking integrations. Another failure is confusing financial statement hierarchy with account parent hierarchy when they differ.

## Falsification

Reject if historical postings can lose account identity; if used accounts can be deleted without migration; if code reuse creates ambiguity; if material mapping/type changes lack impact preview/effective date; if inactive state is hidden in selectors; or if integration references cannot be assessed before change.

## Output contract

Return a `chart-of-accounts-management-contract` with: stable account ID; code/name/type; hierarchy; entity/effective scope; dimensions/defaults; report/tax mappings; change impact; deactivate/delete rules; merge/reclassification; code reuse policy; and integration/history preservation. Include one code rename and one used-account deactivation case.

## Handoffs

Journal entry consumes eligible accounts, statements consume mappings, tax category mapping may be separate, budgets use account dimensions, and organization admin/permissions govern who may change the chart.