---
name: designing-saved-analysis-workspaces
description: Use when exploratory analytical work must be saved, reopened, shared, forked, renamed, migrated, or recovered without confusing personal state with governed team assets.
---

# Designing Saved Analysis Workspaces

Saving analysis is not equivalent to storing a URL. A saved workspace must preserve enough analytical state to reproduce intent while exposing which dependencies may evolve independently.

## Parent Contract
**Required parent:** `designing-business-intelligence-workspaces`.

The parent defines the overall analytical environment. This skill owns persistence, identity, ownership, sharing, forking, recovery, and reopen semantics for saved analyses.

## Saved-State Boundary
Enumerate what is persisted: metric identifiers/versions, dimensions, filters, time semantics, query text or structured query, visualization settings, layout, notes, sort, selected comparison, and data snapshot references. Separate persisted definition from ephemeral interaction such as hover, temporary selection, or transient loading state.

Choose whether saved analyses are live definitions evaluated on reopen or immutable snapshots. Many products need both concepts. A live analysis should say that values may change as data refreshes; a snapshot should bind to a frozen result or as-of context. Never let the same “Save” action imply both depending on hidden backend behavior.

Ownership must be explicit. Personal drafts, shared team analyses, published governed artifacts, and forked copies require different edit authority and discoverability. Forking should preserve lineage to the source without making the source owner responsible for the fork.

When dependencies change, reopening needs a migration state. A renamed field can migrate automatically if identity is stable; a removed metric or incompatible schema may require user action. Preserve recoverable information and explain exactly what failed rather than resetting to an empty editor.

## Sharing and Concurrency
Shared saved work should expose permissions and revision identity. If concurrent editing is unsupported, prevent silent last-write-wins. If supported, show collaboration state and meaningful conflict resolution. Copying a share link should not accidentally leak a private draft or session-only filter.

## Evidence
Save, close, and reopen analyses across data refresh, renamed fields, metric revision, permission change, and browser/session changes. Test fork, ownership transfer, deletion/restore where available, and opening an older link after the source analysis has changed. Compare reconstructed state field by field.

## Failure Modes
- A saved URL omits filters held only in client memory.
- Reopen silently substitutes a new metric definition.
- Personal draft controls look identical to team-published assets.
- Broken dependencies cause state loss rather than recoverable migration.
- Sharing copies session secrets or private state.
- Concurrent edits overwrite without revision awareness.

## Falsification
Create a complex analysis, save it, change one dependency, and reopen from a clean session. Falsify if the user cannot tell what persisted, what changed externally, or whether current values are live versus snapshotted.

## Recovery
Add explicit persistence schema, stable dependency identities, migration diagnostics, ownership states, revision checks, and snapshot/live labels. When exact restoration is impossible, preserve the surviving parts and surface a bounded recovery path.

## Handoff
Use `designing-query-provenance-inspection` for executed query history, `designing-dashboard-permission-boundaries` for shared authorization, and `designing-dashboard-edit-view-modes` if a saved analysis is promoted into a dashboard.

## Output Contract
Return a `saved-analysis-workspaces-contract` with `persisted_state_schema`, `ephemeral_state_boundary`, `live_vs_snapshot_model`, `ownership_states[]`, `sharing_policy`, `revision_model`, `dependency_migration`, `recovery_states[]`, `evidence_cases[]`, and `failure_findings[]`.