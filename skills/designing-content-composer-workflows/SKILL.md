---
name: designing-content-composer-workflows
description: Use when creating a publishable content object involves multiple authored regions, metadata, media, taxonomy, collaborators, validation, and draft state beyond a single text editor.
---

# Designing Content Composer Workflows

## Parent Contract
**Required parent:** `designing-editor-canvas-workspaces`.

This faculty owns the composition workspace around a content object: body, title, summary, media, metadata, taxonomy, related entities, SEO/social fields when relevant, and the transitions between editing regions. It does not own the rich-text or Markdown editing engine itself and does not own publishing authority.

## Decision Architecture
Start from the content model. Separate required fields for valid content from optional enhancement and channel-specific metadata. The composer should reflect semantic regions, not mirror a database schema with internal field names. If the same content feeds web, email, social, or app surfaces, distinguish shared canonical content from channel overrides and show which value wins.

Editing state may span many components. Autosave/draft persistence needs one content revision identity so a title save and body save cannot produce mismatched versions. Validation should identify both field-level issues and cross-region requirements such as “featured image required when layout is hero” or “summary exceeds destination limit.” Do not block writing with publication-only checks that can wait until preview/review.

Keep high-frequency authoring actions close to the work while moving infrequent metadata into structured side regions. Collapsible inspectors should preserve errors and dirty-state indicators when closed. Collaboration must bind comments/review to the same revision or region identity rather than floating independently of the composed object.

## Failure Topology
- Composer exposes every CMS database field at equal prominence and overwhelms ordinary writing.
- Body autosaves revision 8 while metadata remains revision 6, then final draft loads an inconsistent combination.
- Channel override silently shadows canonical title but UI gives no indication which value will publish.
- Closed metadata panel contains a required error with no visible cue.
- Publication-only validation fires on every keystroke and interrupts creative drafting.
- Switching content type clears media/taxonomy fields that could have been preserved or explicitly migrated.

## Falsification and Recovery
Falsify with long drafts, multiple channel overrides, content-type changes, closed side panels containing errors, offline/reconnect, concurrent edit, autosave races, validation before publish, keyboard/screen-reader traversal across regions, and draft resume on another device. The design fails if the composed content cannot be reconstructed as one coherent revision or if hidden regions can block progression without visible evidence.

Recover by grounding the workspace in a typed content model, using one revision-aware draft identity, separating draft-time from publish-time validation, making override precedence visible, preserving hidden-region status, and defining explicit migration when content type changes.

## Output Contract
Return `content-composer-workflow-contract` with content regions, required/optional metadata, canonical-vs-channel precedence, revision/persistence model, validation phases, panel/density strategy, content-type migration, collaboration anchors, accessibility navigation, and falsification cases.