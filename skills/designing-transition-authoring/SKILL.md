---
name: designing-transition-authoring
description: Own creation and editing of audio/video transitions across edit points, source handles, duration, alignment, parameters, overlap, defaults, and insufficient-media recovery.
---
# Designing Transition Authoring

## Decision ownership

Own authored transitions between adjacent media segments. Decide insertion point, type, duration, alignment, source handle requirements, overlap, parameters, default application, preview, replacement/removal, and behavior when media handles are insufficient. Motion design concepts do not replace timeline/source constraints.

## Inputs and evidence

Require transition types, clip adjacency, source handles, sequence timebase, audio/video track types, default duration, render capability, parameters, and nested/effect interaction. Identify transitions that require overlapping source content or can synthesize frames/samples.

## Procedure

Apply transitions to a clearly selected edit point and show duration/alignment relative to the cut. Before commit, indicate available handles and whether frames would be repeated/generated when insufficient. Users should be able to trim duration directly in timeline or inspector with synchronized values. Preview should use actual source handles and current render quality. Replacing transition preserves appropriate duration only when semantics are compatible. Bulk/default transition commands reveal affected edit points and skipped failures. Removal restores the underlying cut without changing clip timing unless explicitly configured.

## Failure topology

Failures include transition silently shortening clips, repeated freeze frames due missing handles, effect placed on the wrong edit point, duration display disagreeing with timeline geometry, replacing a transition resetting timing unexpectedly, and bulk application hiding skipped cuts. Another failure is transition icon obscuring a very short clip or adjacent edit handle.

## Falsification

Reject if source-handle sufficiency is unknown; if insertion can change clip timing without explicit rule; if selected edit point is ambiguous; if preview uses materially different source span than export; if bulk application cannot report skipped/modified points; or if removing transition does not restore the expected underlying cut.

## Output contract

Return a `transition-authoring-contract` with: transition type; edit-point identity; duration/alignment; handle availability; insufficient-media policy; parameters; timeline/inspector synchronization; preview; bulk/default behavior; replace/remove semantics; and render/export fidelity. Include one insufficient-handle scenario.

## Handoffs

Clip trimming manages source handles, timeline identifies edit points, render preview/export realizes effects, and audio mixing may govern audio crossfades where specialized behavior applies.