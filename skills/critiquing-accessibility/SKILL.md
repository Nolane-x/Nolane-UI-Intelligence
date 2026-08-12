---
name: critiquing-accessibility
description: Use when an independent reviewer must evaluate semantic, keyboard, focus, contrast, reflow, motion, target-size, error, or assistive-technology risks in a UI.
---

# Critiquing Accessibility

## Overview
Audit the implemented/inspectable interface against the task’s accessibility obligations and applicable authoritative standards. Do not equate automated test success with accessibility completion.

## Parent Contract
**Required parent:** `challenging-ui-designs`.

`may_modify: false`. Require the accessibility obligation set and runtime evidence available. If exact normative compliance is claimed, consult authoritative standard text rather than relying on memory.

## Review layers
1. **Structure:** landmarks/headings/reading order/content relationships.
2. **Name-role-state:** native semantics or correct custom exposure; labels/descriptions; selected/expanded/checked/invalid/value states.
3. **Keyboard/focus:** reachability, operation, visible focus, logical order, modal trapping, focus restoration, deletion/navigation behavior.
4. **Visual access:** text/non-text contrast, non-color cues, zoom/reflow, high contrast/forced colors where in scope.
5. **Motor/touch:** target size/spacing, drag alternatives, timing, accidental activation/recovery.
6. **Motion:** reduced motion, flashing/continuous movement, semantic replacement.
7. **Errors/status:** association, announcement, recovery, no focus theft/noise.
8. **Assistive technology:** screen-reader/custom-widget behavior for critical paths when capability exists.

## Automated evidence
Use automated tools to find detectable violations, then inspect false positives/coverage. Record what was **not** tested. A clean axe run cannot close focus quality, label meaning, cognitive clarity, screen-reader usability, or every WCAG criterion.

## Severity by exclusion
A blocker that makes a core task impossible for keyboard/screen-reader users can be critical/major even if visually subtle. Conversely, a decorative missing alt attribute on a truly decorative image may be minor or no finding depending on semantics.

## Output: `finding-set`
Return typed findings plus `automated_coverage`, `manual_coverage`, `assistive_tech_coverage`, `untested_criteria`, and a lens recommendation. Never write “WCAG compliant” unless the exact scoped claim has evidence.
