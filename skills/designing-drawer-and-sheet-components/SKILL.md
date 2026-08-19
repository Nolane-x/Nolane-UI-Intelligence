---
name: designing-drawer-and-sheet-components
description: Use when an edge-attached panel or sheet is needed and the product must decide modality, detents, content ownership, navigation relation, safe areas and responsive transformation across desktop and mobile.
---

# Designing Drawer and Sheet Components

## Parent Contract
**Required parent:** `engineering-rich-interactive-components`.

This faculty owns the component semantics and structural behavior of drawers/sheets. Motion/physics are delegated to `designing-drawer-and-sheet-motion`.

## Decision Model
Name the surface’s relationship to the primary task. A **navigation drawer** changes destinations; a **context drawer** inspects/edits the current selection; a **temporary sheet** presents a bounded action; a **persistent side panel** is part of workspace layout. Treating all four as “a panel that slides in” creates focus and persistence errors.

Decide modality. Temporary mobile sheets may block background interaction; desktop inspectors often must remain nonmodal so users can select another object. The same feature may transform across breakpoints—from modal bottom sheet on phone to persistent side pane on wide desktop—but its task state and action semantics must remain equivalent.

Detents belong only when distinct heights support distinct jobs. Define what content is visible/operable at each detent and whether focus traversal can enter clipped content. Safe areas, virtual keyboards and system bars affect usable height.

Navigation/history policy matters. Browser/system Back may close a transient sheet before leaving the route when the sheet represents a user-visible navigation state; ephemeral formatting panels may not deserve history entries. Make this deliberate.

## Failure Topology
- Desktop inspector is implemented as modal, preventing interaction with the object it edits.
- Half-height sheet contains focusable controls below the clipped viewport.
- Responsive change closes the user’s in-progress sheet because component type changed.
- Back navigation exits the page when users expect it to dismiss the sheet.
- Persistent drawer steals scarce phone width instead of transforming to temporary navigation.

## Falsification and Recovery
Resize across breakpoints while open, use keyboard/screen reader, open virtual keyboard, test Back/Escape/outside interaction, switch selected object under nonmodal inspector and restore session state. The contract fails if task state is lost merely because the presentation mode changes.

Recover by defining semantic surface role first, mapping responsive presentations to that role, limiting detents to meaningful tasks and aligning modality/history with consequences.

## Output Contract
Return `drawer-sheet-component-contract` with surface role, modality, responsive presentations, detents/content reachability, focus/dismissal, safe-area/keyboard behavior, history integration, persistence and motion handoff.