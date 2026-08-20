---
name: designing-dashboard-edit-view-modes
description: Use when dashboards have materially different authoring and consumption states and the interface must prevent accidental production edits while preserving realistic preview, sharing, and review behavior.
---

# Designing Dashboard Edit and View Modes

Dashboard authoring and dashboard consumption are different operational modes. A robust interface makes the boundary legible without making authors guess whether they are editing a draft, a published asset, or only their own viewing state.

## Parent Contract
**Required parent:** `designing-business-intelligence-workspaces`.

The parent owns cross-workspace analytical continuity. This skill owns the mode contract for dashboard editing, preview, personal viewing state, draft publication, and permission-sensitive controls.

## Mode Model
Name the states explicitly in the product model: view, personal exploration, edit draft, preview-as-viewer, review, and published when applicable. Avoid a binary `isEditing` model if publication and personal filters have independent persistence.

Classify every interaction by persistence target. A viewer changing a time range may alter only session state; an editor changing the default time range may alter the dashboard definition. Controls that look identical but write to different scopes must communicate that scope before the user leaves the page.

Entering edit mode should establish a revision boundary. Record the base version, ownership, lock or collaboration state, and whether edits auto-save. If multiple authors can work simultaneously, distinguish live collaborative editing from optimistic overwrite and from explicit checkout.

Preview must use the same rendering and permission assumptions as the eventual viewing mode as far as the system can prove. An editor-only preview that includes inaccessible metrics or hidden filters gives false confidence. Provide a way to preview representative viewer roles without letting authors grant themselves authorization through the UI.

Publishing is consequential. Show what changed, where it will apply, and whether subscribers, embeds, or alerts depend on the asset. If publish fails after some server-side steps, preserve the draft and explain which version remains live.

## Evidence
Evidence should include entering edit from a shared dashboard, changing layout and defaults, abandoning or saving, previewing with a lower-permission role, publishing, encountering a version conflict, and returning as a normal viewer. Verify browser refresh and deep link behavior in every mode.

A visual toggle labelled “Edit” is not evidence that mode boundaries work. Inspect actual persistence targets and published revision identities.

## Failure Modes
- Personal filter changes accidentally become shared defaults.
- A draft looks published because the URL and chrome are identical.
- Preview uses editor permissions and hides viewer failures.
- Autosave overwrites a newer collaborator revision silently.
- Publish failure leaves the user unsure which revision is live.
- Exit from edit discards work without a recoverable draft or explicit decision.

## Falsification
Give a viewer and an editor the same dashboard. Have both change a filter with identical-looking controls, then reload in a second session. Falsify the design if persistence scope cannot be predicted from the interface. Also falsify if an editor can publish from stale base state without conflict detection in a system that allows concurrent changes.

## Recovery
Separate persistence scopes, show draft/live revision identity, make role-based preview explicit, and add conflict-aware publication. When mode state is uncertain after an interrupted publish, query the server and present the confirmed live revision instead of assuming success.

## Handoff
Coordinate with `designing-dashboard-filter-scope` for filter semantics and `designing-dashboard-permission-boundaries` for authorization. Layout behavior belongs to the dashboard composition owner, while this skill governs mode and persistence authority.

## Output Contract
Return a `dashboard-edit-view-modes-contract` with `mode_states[]`, `entry_exit_rules`, `persistence_targets`, `draft_revision_model`, `autosave_policy`, `role_preview_model`, `publish_sequence`, `conflict_handling`, `evidence[]`, `failure_findings[]`, and `recovery_actions[]`.