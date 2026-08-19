---
name: designing-translation-expansion-resilience
description: Use when translated strings can become materially longer, shorter, or structurally different and components must preserve meaning without truncation, overlap, or locale-specific one-off fixes.
---

# Designing Translation Expansion Resilience

## Parent Contract
**Required parent:** `designing-localized-interfaces`.

This faculty owns layout tolerance to translated string length and grammatical structure. It does not produce translations. It challenges any component whose geometry assumes the source language's compactness, word order, or number of words.

## Decision Boundary
Identify high-risk surfaces: buttons with fixed widths, tabs, breadcrumbs, side navigation, data-table headers, banners, segmented controls, mobile toolbars, empty states, and paired labels/values. Decide which strings may wrap, which components may grow, when labels can reflow to another row, and where an abbreviated variant is permissible only if it has an approved localized meaning.

Do not set universal expansion percentages as a substitute for testing. Short source strings can expand dramatically while long paragraphs may expand modestly. Some scripts do not break at spaces; others can produce very long compounds. Preserve the full accessible name if visual abbreviation is necessary and ensure truncation does not remove the differentiating portion among sibling commands.

## Failure Topology
- German or Finnish labels overflow a fixed button and cover adjacent actions.
- Tab text is truncated until several tabs become indistinguishable.
- A translated warning wraps beneath an absolutely positioned icon and hides the first line.
- Mobile action rows preserve desktop widths and force horizontal scrolling.
- Engineers introduce locale-specific pixel overrides for each discovered overflow.
- An abbreviation copied from English is meaningless or ambiguous in another language.

## Falsification and Recovery
Run pseudolocalization plus real long-string locales through every component state, including errors, badges, counts, selected tabs, dialogs, and narrow viewports. Test scripts with different break behavior, not only expanded Latin. The design fails when translation length changes action reachability, hierarchy, or semantic distinction.

Recover by adopting intrinsic sizing, wrapping/reflow rules, content-priority collapse, responsive regrouping, and approved localized short forms only where needed. Repair the component primitive so all locales benefit rather than accumulating route-specific exceptions.

## Output Contract
Return `translation-expansion-contract` with high-risk component inventory, wrap/grow/collapse policy, abbreviation authority, truncation limits, accessible full-label behavior, pseudolocale/real-locale stress cases, and component-level recovery rules.
