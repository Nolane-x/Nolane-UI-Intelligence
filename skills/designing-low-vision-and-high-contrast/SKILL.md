---
name: designing-low-vision-and-high-contrast
description: Use when a UI must remain usable under magnification, browser or OS zoom, low vision, high-contrast or forced-color modes, reduced contrast sensitivity, large text, glare, or themes that can erase visual state cues.
---

# Designing Low Vision and High Contrast

## Overview
Low-vision accessibility is spatial continuity plus perceivable state under transformed rendering. Design so magnification, large text, high contrast, and forced colors preserve meaning rather than merely satisfy nominal color ratios at default scale.

## Parent Contract
**Required parent:** `designing-accessible-interfaces`.

Require responsive behavior, token/theme system, focus model, component states, charts/imagery, and applicable zoom/reflow obligations. Coordinate with theming and responsive skills because accessibility transformations often change geometry and palette together.

## Decision Model
Test **perception**, **transformation**, and **navigation continuity**. Perception covers text/non-text contrast, focus, borders, selected/error/disabled states, chart distinctions, link/action cues, and whether information depends solely on subtle color difference. Transformation covers text resize, browser zoom, reflow, OS scaling, forced-colors/high-contrast themes, custom font settings, and responsive narrowing. Navigation continuity asks whether a magnified user can maintain location when content reflows or overlays appear.

Use semantic tokens so high-contrast mode can preserve role rather than invert arbitrary hex values. Native controls and system colors often survive forced-color transformations better than painted replicas. When custom visuals are necessary, ensure outlines, current-state indicators, focus, and icons remain perceivable when backgrounds or shadows disappear.

Avoid fixed-height containers that clip enlarged text. Reflow should not require two-dimensional scrolling for ordinary reading unless content intrinsically needs it. Sticky headers, floating toolbars, and overlays can consume a disproportionate magnified viewport; ensure they do not obscure focused or targeted content.

Charts and maps require pattern/shape/text alternatives when color separation collapses. Images containing text should not become the only readable label. Motion or hover cannot substitute for a persistent focus/state cue.

## Evidence
Test 200–400% zoom/reflow as applicable, large text, OS scaling, forced-colors/high-contrast modes, dark/light themes, focus across transformed palettes, long localized labels, chart distinctions, and screen magnifier workflows when available. Automated contrast tools are useful but do not validate clipping or spatial continuity.

## Output Contract
Return a `low-vision-contract` with `contrast_roles[]`, `non_color_state_cues[]`, `zoom_reflow_rules`, `large_text_behavior`, `forced_color_mapping`, `focus_visibility`, `overlay_obscuration_rules`, `chart_image_alternatives[]`, `spatial_continuity_rules`, and `low_vision_tests[]`.

## Failure Traps
- Selected state disappears when custom background color is overridden.
- Box shadow is the only panel boundary in high contrast.
- Fixed card height clips enlarged labels.
- Sticky header covers half the viewport at high zoom.
- Chart series distinguishable only by close hues.
- Focus ring has contrast against one theme but not transformed system colors.
- Passing contrast ratios at 100% treated as complete low-vision validation.

The interface should remain understandable after the user transforms it to fit their vision.