---
name: designing-print-preview
description: Use when users need to understand how screen content will paginate onto paper or PDF and preview must expose page size, margins, scaling, headers/footers, hidden content, and fidelity before invoking the print system.
---

# Designing Print Preview

## Parent Contract
**Required parent:** `designing-device-integration-interfaces`.

This faculty owns print-output preview, not printer discovery. A print preview is a different composition from screen UI and must be bound to the exact print settings that influence pagination and visibility.

## Decision Boundary
Define print artifact scope and layout rules: paper size/orientation, margins, scale, page breaks, repeated headers, footers, background graphics, comments, collapsed sections, selected rows, or chart rendering. Preview should use the same print stylesheet/render pipeline as actual output as closely as possible. Controls for preview are not themselves printable.

Make page count and clipped/overflow content visible. Interactive-only states such as hover, sticky headers, scroll containers, virtualized rows, and collapsed accordions need explicit print behavior. Sensitive content that is visually hidden on screen must not appear in print unless the export contract includes it. If browser/system print dialog applies additional settings after app preview, state that preview is approximate where exact fidelity cannot be guaranteed.

## Failure Topology
- Virtualized table preview prints only rows mounted in the viewport.
- Sticky headers duplicate over content on every page.
- Dark-mode screen colors produce unreadable or ink-heavy output.
- Hidden admin fields appear in print because CSS merely moved them offscreen.
- Preview shows A4 while system dialog defaults to Letter and pagination changes.
- Page break splits signature/table row in a way the preview did not show.

## Falsification and Recovery
Compare preview and actual PDF/physical print across page sizes, orientations, long content, virtualized data, charts/images, hidden/sensitive regions, multiple themes, and system-dialog changes. The design fails if preview claims exact placement that the print path cannot preserve.

Recover by sharing render pipeline, materializing print data independently from viewport virtualization, defining print-specific colors/break rules, and labeling settings still controlled by the system dialog. Provide warnings for known clipping or unsupported elements.

## Output Contract
Return `print-preview-contract` with artifact scope, page/layout settings, print-specific content rules, virtualization handling, fidelity boundary, sensitive-content exclusions, system-dialog deltas, and preview-to-output verification cases.
