---
name: designing-saved-searches-and-views
description: Use when users need to preserve a search, filter, sort, grouping, or display configuration as a reusable view with clear scope, update, sharing, and deletion semantics.
---

# Designing Saved Searches and Views

## Parent Contract
**Required parent:** `designing-search`.

This faculty owns persistence of a query/view configuration as a named reusable object. It does not own the underlying search or filter syntax. The core decision is whether users are saving a snapshot of current criteria, subscribing to a live query definition, or preserving a broader presentation state such as columns and grouping.

## Decision Boundary
Define the saved payload explicitly: query text, facets, sort, grouping, visible columns, density, scope, and perhaps ownership context. Do not save incidental state such as current scroll position unless the product explicitly offers session restoration. A saved view should re-run against current data unless it is labeled as a historical snapshot.

Ownership changes behavior. Personal views, team-shared views, and administrator-provided defaults need different rename/delete rights and conflict rules. If editing criteria while inside a saved view, decide whether changes are temporary, auto-update the saved definition, or require an explicit “Save changes.” Silent mutation is dangerous because the next user may depend on the shared definition.

Naming needs collision semantics and enough context to distinguish similar views. If the underlying schema changes and a saved facet/column disappears, degrade visibly: identify the invalid portion and let users repair the view rather than silently dropping constraints.

## Failure Topology
- “Save view” stores only filters but not the sort/grouping users considered part of the view.
- Editing a team-shared view silently changes everyone’s workflow.
- A deleted field causes the saved view to broaden results without warning.
- Personal and shared views look identical, obscuring authority.
- Duplicate names make command/search invocation ambiguous.
- Saving a live query is presented as a frozen report and users expect historical data.

## Falsification and Recovery
Falsify with schema evolution, permission loss, a shared view edited by two people, duplicate names, owner deletion, a view opened from a deep link, and temporary criterion changes that are later abandoned. The design fails if users cannot tell whether they changed the current session or the persistent definition, or whether opening the view re-runs current data.

Recover by versioning definitions, separating transient from persisted edits, labeling scope/ownership, validating references on open, showing degraded criteria explicitly, and providing duplicate/rename/share/delete rules tied to authority.

## Output Contract
Return `saved-search-view-contract` with persisted state fields, snapshot-vs-live semantics, ownership/scope, edit persistence model, naming/collision policy, sharing permissions, schema-drift handling, deletion/default behavior, deep-link identity, and falsification cases.