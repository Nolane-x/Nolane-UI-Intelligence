---
name: designing-diff-interfaces
description: Use when users compare two versions of text, structured data, configuration or visual artifacts and the interface must expose additions, removals, moves, modifications, unchanged context and semantic significance without reducing every change to raw line coloring.
---

# Designing Diff Interfaces

## Parent Contract
**Required parent:** `designing-version-history`.

This faculty owns comparison presentation between two explicitly identified states. It does not compute domain-specific equivalence, resolve conflicts or choose which revision should win.

## Decision Boundary
Begin with **comparison identity**: base revision A, target revision B, direction, timestamps/actors and artifact type. “Before” and “after” labels must stay stable as users navigate differences. Reversing comparison changes addition/removal semantics; never leave red/green styling unchanged after swapping sides.

Choose diff representation based on structure. Text/code can use line and token changes; structured settings benefit from field-level old/new values; tables may need row/column/cell changes keyed by stable IDs; visual designs may use side-by-side, overlay or annotated region changes; hierarchical documents may require section-aware comparison. Raw serialized JSON is fallback evidence, not the default UI when semantic fields are known.

Distinguish add, remove, modify, move/rename and unchanged context when the underlying diff engine can prove them. Treat move detection cautiously: matching similar text or objects probabilistically should not be presented as certain identity without evidence. Whitespace/format-only changes may be suppressible, but any ignore option must be visible because it changes the comparison claim.

Navigation should support next/previous change, change index/summary, filters by type/author/section and context expansion. Preserve reading position while expanding context. Side-by-side views require synchronized alignment without forcing giant blank gaps where files diverge dramatically; unified view may be better on narrow screens.

Accessibility cannot depend on red/green backgrounds. Each change needs textual semantics, accessible labels and reading order. Deletions must remain inspectable even though they no longer exist in target state. For large diffs, virtualize without losing change numbering or focus.

## Failure Topology
- Comparison direction is unclear, so users interpret removed content as newly added.
- Field reorder is shown as delete+add and appears more consequential than it is.
- “Ignore whitespace” remains enabled from a prior session with no visible indicator.
- Side-by-side alignment inserts huge empty blocks and obscures actual nearby changes.
- Red/green are the only add/remove distinction.
- Generated/format noise dominates meaningful policy changes.
- Diff view compares stale local snapshots but header implies current server revisions.

## Falsification and Recovery
Falsify with pure add/remove, rename/move, reordered structured fields, formatting-only changes, large deletions, binary/visual artifacts, narrow viewport and screen reader. Compare rendered change categories against the authoritative diff engine and selected ignore settings. If two comparison directions or filter modes can look the same while making different claims, the interface fails.

Recover by pinning revision identities/direction, selecting structure-aware rendering, exposing ignore/filter state persistently, providing semantic labels beyond color and falling back to raw evidence only where domain mapping is unavailable.

## Output Contract
Return `diff-interface-contract` with base/target identities and direction, artifact-specific representation, change taxonomy, ignore/filter settings, navigation/context strategy, large-diff behavior, accessibility semantics, source freshness and diff-engine parity tests.