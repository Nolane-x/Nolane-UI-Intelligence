---
name: designing-script-sensitive-typography
description: Use when one typographic system must support scripts with different x-heights, shaping, line metrics, word boundaries, diacritics, and emphasis conventions without forcing Latin assumptions onto every locale.
---

# Designing Script-Sensitive Typography

## Parent Contract
**Required parent:** `designing-localized-interfaces`.

This faculty owns typographic adaptation across writing systems. It does not pick a global brand font in isolation; it decides how hierarchy, size, weight, line-height, letter spacing, emphasis, and fallback adapt when scripts have materially different optical and shaping behavior.

## Decision Boundary
Evaluate typography by script and rendered font, not by nominal CSS values. A 14px Latin interface font and a 14px CJK or Arabic face may have very different perceived size and vertical density. Disable Latin-centric tracking rules where scripts require connected shaping or where extra letter spacing damages readability. Ensure diacritics and tall glyphs have sufficient line box and are not clipped by compact controls.

Preserve hierarchy without demanding identical physical metrics. Heading scale, weight availability, and emphasis mechanisms may need script-specific mappings. Bold may be weak or unavailable in a fallback family; italics can be inappropriate for some scripts. Uppercase transformations must not be used as a universal hierarchy tool. Mixed-script interfaces need optical balancing so a fallback segment does not look like an accidental font swap.

## Failure Topology
- Global negative letter spacing breaks Arabic joining or script legibility.
- Fixed line-height clips Vietnamese diacritics or tall glyphs in buttons.
- Locale fallback lacks the requested weight and silently produces fake bold with poor readability.
- All-caps labels are applied to scripts without case or with undesirable transformed forms.
- CJK text appears materially smaller than Latin at the same nominal size.
- Mixed-script content produces baseline jumps and visual hierarchy inconsistent with the surrounding UI.

## Falsification and Recovery
Render representative alphabets and real UI strings for every supported script across body, labels, buttons, dense tables, headings, errors, and responsive states. Inspect line boxes, shaping, fallback, weight, emphasis, and mixed-script baselines. The design fails when global tokens preserve numeric equality but destroy optical hierarchy or legibility.

Recover with script-aware font/token mappings, intrinsic line-height, disabled inappropriate tracking/transforms, real weight availability, and optical calibration. Treat script adaptation as a controlled extension of the design system, not ad hoc per-screen overrides.

## Output Contract
Return `script-sensitive-typography-contract` with supported scripts, typeface mappings, optical size/line-height adjustments, weight/emphasis policy, tracking/case restrictions, mixed-script behavior, and rendered script verification set.
