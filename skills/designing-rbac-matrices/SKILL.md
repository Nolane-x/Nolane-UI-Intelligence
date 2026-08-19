---
name: designing-rbac-matrices
description: Use when administrators must compare or edit permissions across roles and resources in a matrix and the interface must represent allow, deny, inherited, conditional, unavailable and mixed states without reducing authorization to colored checkboxes.
---

# Designing RBAC Matrices

## Parent Contract
**Required parent:** `designing-role-management`.

This faculty owns dense comparison/editing of role-resource-action relationships. It does not define the authorization model, precedence algorithm or policy language.

## Decision Boundary
A matrix cell is not necessarily Boolean. Model the states the backend truly supports: explicit allow, explicit deny, inherited allow/deny, not applicable, conditional, locked by policy, mixed/partial or unset/default. If the system only supports allow/unset, do not invent deny because a tri-state checkbox looks powerful.

Choose axes from the decision task. Roles × permissions is useful for comparing roles; users × roles supports assignment review; resources × actions supports policy design. Avoid one mega-matrix that requires users to reason simultaneously about three dimensions. Provide filters/search/grouping and a details panel for conditions that cannot fit in a cell.

Editing must expose effective consequence. Clicking an inherited grant may require navigating to the source policy rather than toggling locally. Bulk row/column changes need previews and partial-applicability reporting. Sticky headers/first columns can preserve context, but one semantic cell identity must remain accessible.

Color and iconography must be redundant: labels, symbols, tooltips/details and high-contrast state are needed. Keyboard navigation should follow grid semantics with an edit mode rather than creating thousands of Tab stops.

## Failure Topology
- Empty cell means both “denied” and “not configured” depending on row.
- Clicking an inherited checkmark creates a direct override without warning.
- Matrix silently truncates permissions the current admin cannot view.
- Red/green alone encode deny/allow.
- Bulk enable changes locked cells on the server but UI reports universal success.
- Horizontal scroll loses role/resource labels and users edit the wrong intersection.

## Falsification and Recovery
Falsify with inherited/locked/conditional permissions, partial admin visibility, bulk edits, 100+ roles, 1000+ permissions, keyboard/screen reader and concurrent policy updates. Resolve each edited cell to the authoritative effective-access engine.

Recover by expanding the state model, separating explicit from inherited values, routing complex conditions to detail views, exposing partial results and preserving row/column context through dense navigation.

## Output Contract
Return `rbac-matrix-contract` with axis choice, cell state algebra, editability/source rules, grouping/filtering, bulk semantics, effective-access preview, keyboard/accessibility model, virtualization constraints and policy-parity tests.