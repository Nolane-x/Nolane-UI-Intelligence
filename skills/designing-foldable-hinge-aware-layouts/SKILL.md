---
name: designing-foldable-hinge-aware-layouts
description: Use when a foldable or dual-screen device can occlude, separate, or reshape usable regions and layout must account for hinge geometry, posture, spanning, continuity, and task placement.
---

# Designing Foldable Hinge-Aware Layouts

## Physical Discontinuity
A fold or hinge can create two visible regions with a non-interactive or distorted gap. This is not an ordinary wide breakpoint. This skill owns how interface regions span, avoid, or exploit that physical discontinuity while preserving interaction and content continuity across device postures.

## Parent Contract
**Required parent:** `adapting-responsive-layouts`.

The parent controls responsive composition. This specialist adds posture and occlusion geometry as constraints beyond rectangular viewport size.

## Posture Model
Represent posture, fold orientation, hinge bounds, spanning state, and usable segments. A single logical viewport may contain two physical panes; decide which tasks benefit from master-detail separation and which must remain entirely on one pane. Critical controls and text must not straddle an occluding hinge.

Transitions between folded, tabletop, book, and flat states require state continuity. Do not remount the task or reset scroll/selection merely because region assignment changes.

## Evidence
Evidence includes emulator/device hinge metrics, portrait/landscape postures, spanning and non-spanning windows, focus traversal across panes, pointer/touch targets near hinge edges, and stateful transitions while content is selected or edited. Capture actual safe regions rather than assuming a fixed hinge width.

## Failure Modes
Failure includes dialogs centered under the hinge, text columns split through unreadable gaps, drag targets crossing unreachable space, master and detail swapping unexpectedly on posture change, keyboard focus jumping between panes, and designs that treat two panes as a decorative wide canvas instead of separate physical attention zones.

## Falsification
Falsification changes posture while a modal, selection, or edit is active; varies hinge orientation and bounds; and runs tasks near the discontinuity. Any critical content occluded, action unreachable, or task state lost falsifies the layout contract.

## Recovery
Recovery reassigns regions according to semantic pane roles, moves critical overlays wholly into one safe segment, and preserves state independent of pane placement. If a task cannot safely span, constrain it rather than forcing symmetry.

## Output
Output: `foldable-hinge-aware-layouts-contract` with posture states, hinge/safe-region rules, pane roles, spanning policy, continuity requirements, and device evidence.

## Handoff
Handoff generic content thresholds to responsive parent skills and across-separate-device continuation to multi-surface continuity specialists.

## Sibling Boundary and delete-the-skill
Container queries model allocated size but not a physical non-content gap inside that allocation. Removing this skill leaves hinge occlusion and posture transition decisions unowned.