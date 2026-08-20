---
name: designing-diagram-export-and-presentation
description: Use when this specialist's decision ownership is materially in scope. Own diagram-specific static and presentation outputs, including bounds, pagination, vector fidelity, themes, labels, hidden state, and narrative focus.
---
# Designing Diagram Export and Presentation

## Parent Contract

**Required parent:** `designing-diagramming-and-node-graph-editors`.

Inherit the broader routing and decision boundary from this canonical parent; this specialist remains accountable only for the narrower ownership, failure topology, falsification criteria, and output contract defined below.

## Decision ownership

Own turning an interactive graph or diagram into a shareable static or presentation artifact. Decide export bounds, page tiling, vector/raster formats, theme/background, label/legend inclusion, collapsed-content treatment, resolution, font handling, and presentation-mode navigation. Generic export configuration owns file-format mechanics; this skill owns preserving diagram meaning outside the editor.

## Inputs and evidence

Require target media (PDF, SVG, PNG, slide/presentation, print), diagram dimensions, expected zoom, font and icon dependencies, hidden/collapsed states, external asset licensing, color/contrast modes, audience, and whether interactive states must be flattened. Determine whether the artifact is archival evidence or a narrative view where selected subsets are acceptable.

## Procedure

Offer sensible bounds such as full diagram, selection, current subgraph, or explicit frame. Preview the exact export area and scale before creation. For paginated output, repeat lane/container headers and provide continuation cues rather than chopping connectors without context. Vector export should preserve text and line crispness where possible; raster export needs explicit resolution. Define how collapsed groups, hidden layers, validation markers, comments, and remote cursors are included or excluded. Presentation mode should use authored frames or focus states, not force a giant diagram onto every slide. Theme changes must retain semantic colors and contrast.

## Failure topology

Failures include cropped nodes at bounds, connectors disappearing at page breaks, unreadable tiny text from fit-to-page, missing fonts shifting layout, dark-theme exports on transparent backgrounds, hidden validation errors omitted from an audit artifact, and exports that include transient collaborator cursors. Presentation can fail when navigation loses the relationship between a focused region and the full topology.

## Falsification

Reject if the preview differs materially from exported bounds; if page tiling produces orphan edge segments with no continuation cue; if text becomes unreadable at the chosen default scale; if font fallback changes node geometry enough to alter topology; if export can silently omit required validation/audit markers; or if a presentation focus cannot return to a meaningful overview.

## Output contract

Return a `diagram-export-and-presentation-contract` with: export scopes; supported artifact modes; exact preview behavior; page/continuation rules; vector/raster fidelity; font/icon handling; theme/background policy; hidden/collapsed-state treatment; transient-overlay exclusions; validation/audit inclusion; and presentation-frame navigation. Include one oversized paginated diagram case.

## Handoffs

Use generic export/file skills for destination, naming, progress, and download recovery. Formal diagram owners provide semantic legends, and accessibility owners provide textual alternatives. This skill remains responsible for exported structural fidelity.