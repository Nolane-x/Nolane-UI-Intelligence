---
name: designing-version-history
description: Use when users inspect, restore or branch historical states of a document, configuration or artifact and the interface must preserve revision identity, authorship, timestamps, autosave/checkpoint meaning and restore consequences.
---

# Designing Version History

## Parent Contract
**Required parent:** `designing-collaboration-and-presence`.

This faculty owns user-facing historical revision navigation and restore semantics. Local command undo/redo, textual/visual diff rendering and merge-conflict resolution are sibling concerns.

## Decision Boundary
A version is a durable historical state or checkpoint with stable identity and provenance, not every transient autosave tick presented to users. Define which events become visible revisions: explicit save, publish, named checkpoint, collaborative snapshot, import, automated migration, scheduled backup or grouped autosaves. The history UI should reflect the storage model rather than inventing a false manual-save metaphor.

Each revision needs enough provenance to reason about it: revision ID, author/actor or automated source, timestamp with timezone, optional label/message, branch/context, and relationship to parent revision. When many autosaves occur, group them into meaningful sessions while preserving a route to finer history if recovery requires it. “3 hours ago” can be a friendly summary, but precise time should be available.

Preview must be clearly historical and read-only unless the product intentionally supports editing a branch. Users need to know whether they are looking at the current state, a past snapshot, or a restored copy. Avoid toolbars/actions that look live while bound to old data.

Restore is a new historical action, not deletion of everything that happened later. Prefer creating a new head whose content matches the selected revision, preserving intervening history for audit/recovery. If the backend instead rewinds/destructively truncates history, disclose that consequence before commit.

Branching/forking from a revision needs identity and destination clarity. A user may create a new document, branch, draft or workspace copy; do not label all of these “Restore.” Collaborative systems must warn when restoring changes the shared current state for others.

Large histories need search/filter by author/date/label and efficient comparison entry points. Retention limits or unavailable old versions should be explicit; a gap caused by retention is not the same as “no changes.”

## Failure Topology
- Every keystroke autosave appears as a revision and history becomes unusable noise.
- Historical preview looks editable and users change controls that actually affect current state.
- Restore deletes later revisions from the visible history, making recovery impossible.
- Relative timestamps hide timezone/sequence ambiguity during incident investigation.
- Automatic migration is attributed to the last human editor.
- Current collaborative head changes while a user previews an old version, but the “current” marker is stale.
- Retention removed old snapshots yet the UI implies the first visible revision is the artifact’s origin.

## Falsification and Recovery
Falsify with rapid autosaves, explicit checkpoints, collaborative edits, automated migrations, restore, restore-then-undo, branch from old revision, retention gaps and simultaneous new head updates. Reconstruct the revision DAG or linear history from visible metadata and authoritative storage records. The design fails if restore can erase provenance or if preview/current identity becomes ambiguous.

Recover by grouping noisy checkpoints without destroying identity, labeling historical mode persistently, implementing restore as a new revision where supported, surfacing automation/retention provenance and refreshing current-head markers independently of the previewed revision.

## Output Contract
Return `version-history-contract` with revision identity/source, visibility/grouping policy, chronology/timezone, preview mode, current-head marker, restore/fork semantics, collaboration consequences, retention/gap treatment, search/comparison entry points and revision-lineage tests.