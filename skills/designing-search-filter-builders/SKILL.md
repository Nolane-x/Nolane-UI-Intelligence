---
name: designing-search-filter-builders
description: Use when users compose structured filters or query clauses and the interface must make field/operator/value logic, grouping, defaults, invalid combinations and reversible editing understandable without requiring query-language expertise.
---

# Designing Search Filter Builders

## Parent Contract
**Required parent:** `designing-search`.

This faculty owns structured query construction UI. It does not define backend search grammar, ranking or domain data schema.

## Decision Boundary
Represent a filter as data: field, operator, value(s), optional negation, and logical grouping. The UI should expose only operators valid for the field type and values valid under domain constraints. Do not let generic string operators leak onto dates/enums merely because the backend accepts them.

Choose composition model based on complexity. Simple products may use independent filter chips implicitly ANDed. Advanced tools may need AND/OR groups, nested logic and saved queries. Do not introduce boolean nesting before users need it; when it is required, make grouping boundaries visually and textually inspectable.

Editing must be reversible. A compact chip such as `Status: Open` should expand into a focused editor without losing the rest of the query. Removing or changing a clause updates results predictably; expensive searches may need explicit Apply while lightweight filters can update immediately.

Always provide a readable query summary. For complex builders, natural-language or structured textual representation helps users verify logic and share/debug it. Empty values, invalid ranges and inaccessible fields need local errors rather than silent omission.

## Failure Topology
- UI shows two chips side by side but users cannot tell AND vs OR.
- Changing field preserves an incompatible old operator/value and yields nonsense.
- Auto-updating results on every clause edit causes expensive network churn and unstable counts.
- Removing a group changes precedence in a way not visible in the summary.
- Saved filters reference deleted schema fields and fail silently.

## Falsification and Recovery
Build simple, nested, invalid and stale-schema queries; switch field types; undo edits; keyboard-navigate clauses; localize long labels; compare displayed summary with backend AST. The contract fails if two different logical expressions can look materially identical.

Recover by exposing grouping/preference explicitly, resetting incompatible dependent values, adding apply/preview boundary where cost warrants it, and versioning saved-query schema.

## Output Contract
Return `search-filter-builder-contract` with query AST mapping, field/operator/value dependencies, grouping model, edit/apply behavior, readable summary, invalid/stale schema handling, saved-query policy and logic-parity tests.