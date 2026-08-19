---
name: designing-rtl-component-mirroring
description: Use when individual controls, iconography, progress indicators, carousels, steppers, and directional affordances need component-specific mirroring rules under RTL.
---

# Designing RTL Component Mirroring

## Parent Contract
**Required parent:** `designing-localized-interfaces`.

This faculty owns component-level mirroring, especially visual affordances whose shape conveys start/end, forward/back, indentation, or progression. It complements layout directionality but does not assume every glyph or control should flip.

## Decision Boundary
Classify component visuals into semantic-directional, physical, neutral, and brand-authored classes. Chevrons that mean “next in reading order” often mirror; play icons, clock hands, mathematical symbols, check marks, and many device metaphors often do not. Indentation and hierarchical disclosure may mirror because they encode inline-start nesting. Sliders, progress bars, and steppers require domain-specific decisions: percentage progression may follow locale direction, while media time may retain a conventional left-to-right timeline depending on product/platform expectations.

Mirror state geometry consistently with interaction. If a carousel's previous/next icons flip, swipe direction and keyboard arrows must still map to the user's conceptual previous/next, not to a copied LTR event handler. Avoid transforming an entire component canvas when that also reverses text or images unintentionally.

## Failure Topology
- All SVG icons are globally flipped, including logos, play buttons, and physical-direction symbols.
- A mirrored chevron visually says “next” but activates the previous item.
- Tree indentation remains on the left while disclosure arrows move to the right.
- A progress component fills from one side while milestone order communicates the other.
- CSS transform mirroring also reverses text inside the control.
- Component snapshots pass but hit areas remain positioned according to pre-mirror geometry.

## Falsification and Recovery
Create an icon/control inventory and inspect each under RTL with its actual action. Exercise previous/next, expand/collapse, hierarchy, sliders, progress, steppers, carousels, and keyboard/touch gestures. The design fails if shape, action, and spatial outcome disagree, or if global transforms reverse content that is not directional.

Recover by assigning explicit mirror policy at the semantic asset/component level, mapping actions to logical previous/next rather than physical left/right, and keeping text/images outside raw transform mirroring. Verify branded and third-party icons separately because their internal assumptions may differ.

## Output Contract
Return `rtl-mirroring-contract` with component/asset classification, mirror/no-mirror decisions, action-direction mapping, gesture/keyboard behavior, hierarchy/progress exceptions, transform prohibitions, and RTL interaction verification cases.
