---
name: designing-query-builders
description: Use when technical or analytical users construct structured queries and the interface must preserve expression semantics, scope, parameterization, validation, execution cost, preview, and reversible editing without hiding the underlying logic.
---

# Designing Query Builders

## Parent Contract
**Required parent:** `designing-data-dense-interfaces`.

This faculty owns construction of structured data queries through visual, assisted-text, or hybrid interaction. It does not own faceted end-user search and does not claim that every query language can be losslessly represented by a simple rule builder. The underlying query semantics remain authoritative.

## Decision Model
Declare the supported expression model: selected fields, source, joins/relationships, filters, grouping, aggregation, ordering, limit, parameters, or domain-specific operations. A visual builder should represent operator precedence and grouping explicitly; rows of conditions without nested structure can silently change `A AND (B OR C)` into `(A AND B) OR C`.

Choose the relationship between visual and source modes. If round-trip conversion is not lossless for advanced syntax, state the boundary and prevent switching modes from destroying unsupported clauses. Parameter values and secrets should remain separate from query text when possible, especially for saved/shared queries. Validation should distinguish syntax/type errors from runtime permission, missing data, or resource-limit failures.

Execution can be expensive. Provide estimates, sample/preview modes, limits, explain plans, or warnings when the backend supplies useful evidence. Do not fabricate cost from client heuristics. Keep query history and saved definitions revisionable enough to recover from accidental edits without storing sensitive parameter values indiscriminately.

## Failure Topology
- Rule rows flatten nested boolean logic and execute a materially different query.
- Switching to visual mode silently deletes a CTE or unsupported expression.
- Saved query stores production secret parameters inside a shareable definition.
- “Valid” check only parses syntax and users interpret it as permission/data correctness.
- Preview runs the unrestricted full query and causes the same expensive impact as Execute.
- Reordering filter chips changes semantics because grouping was implicit.

## Falsification and Recovery
Falsify with nested boolean groups, joins, aggregations, unsupported source syntax, parameterized secrets, permission denial, expensive query warning, large result limit, source↔visual round trip, keyboard-only expression editing, and query history restore. The design fails if the visible builder cannot serialize to an unambiguous expression or if switching representations can silently discard semantics.

Recover by maintaining an explicit expression tree, exposing unsupported constructs, separating definition from parameter values, distinguishing validation layers, providing backend-grounded cost controls, and protecting round-trip fidelity with loss warnings or one-way mode transitions.

## Output Contract
Return `query-builder-contract` with expression model, grouping/precedence, visual-source relationship, parameter handling, validation layers, execution/cost controls, preview semantics, saved/history behavior, accessibility editing, and falsification cases.