---
name: designing-ripple-roll-slip-slide-edits
description: Use when this specialist's decision ownership is materially in scope. Own advanced trim semantics where changing one edit point can move timeline position, adjacent clip boundaries, or source content, with precise mode, preview, collision, and sync consequences.
---
# Designing Ripple Roll Slip Slide Edits

## Parent Contract

**Required parent:** `designing-nonlinear-media-editors`.

Inherit the broader routing and decision boundary from this canonical parent; this specialist remains accountable only for the narrower ownership, failure topology, falsification criteria, and output contract defined below.

## Decision ownership

Own the four high-leverage edit modes whose consequences differ substantially: ripple changes sequence duration/downstream positions; roll moves a shared edit point while duration stays; slip changes source content while timeline position stays; slide moves a clip while trimming neighbors. Decide mode entry, affected clips, preview, handle limits, sync, collisions, and numeric deltas.

## Inputs and evidence

Require clip source/timeline bounds, adjacent clips/gaps, handles, linked tracks, sync groups, locks, transitions, timebase, and downstream ripple policy. Identify protected music/dialog sync and multi-track collisions.

## Procedure

Persistently indicate current trim mode through cursor plus textual affordance where possible. During drag/numeric entry, show delta and a multi-frame preview appropriate to the mode: roll shows outgoing/incoming edges, slip shows new source in/out, slide shows moved clip and neighbor trims, ripple shows resulting gap/sequence shift. Validate source handles and locked/sync-sensitive downstream items before commit. Multi-track ripple needs explicit track selection/lock semantics and sync-lock cues. Cancel restores the entire compound transaction.

## Failure topology

Failures include users performing ripple when expecting normal trim, slip changing timeline position, hidden downstream clips moving, sync drifting across tracks, roll running out of source handles, and slide collapsing a neighbor unexpectedly. Another failure is mode indicated only by subtle cursor shape on high-resolution displays.

## Falsification

Reject if the user cannot identify the active advanced trim mode; if affected neighbors/downstream scope is hidden; if sync-locked content can shift with no warning; if preview does not match committed positions; if handle limitations surface only after commit; or if cancel fails to restore every clip in the compound edit.

## Output contract

Return a `ripple-roll-slip-slide-edits-contract` with: mode semantics; active-mode cue; affected clip/track scope; source handle constraints; sync/lock rules; mode-specific preview; numeric delta; collision handling; sequence-duration effect; and atomic undo/cancel. Include one multi-track ripple sync case.

## Handoffs

Basic trimming supplies edge interaction, track management supplies lock/target state, snapping supplies temporal alignment, and playback preview verifies edit continuity.