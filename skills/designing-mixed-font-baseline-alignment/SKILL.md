---
name: designing-mixed-font-baseline-alignment
description: Use when text runs combine fonts, scripts, icon glyphs, badges, inline controls, or fallback faces and their baselines, optical centers, line boxes, and vertical rhythm must remain coherent.
---

# Designing Mixed-Font Baseline Alignment

## One Line Can Contain Several Metric Systems
A line containing Latin text, CJK fallback, an icon, a badge, and an inline code token can expose several ascender, descender, baseline, and visual-center conventions at once. This skill owns how those elements align without clipping or optical drift.

## Parent Contract
**Required parent:** `crafting-typography`.

The parent defines text roles. This specialist begins when multiple metric systems coexist in one line or repeated row and must form one visual/semantic rhythm.

## Alignment Model
Identify the typographic baseline for text and distinguish it from geometric center alignment. Inline icons may need optical offset while remaining within the line box. Badges and pills may align to the text's baseline, cap-height region, or center depending on meaning and size. Script fallback can change ascent/descent enough to expand line boxes; that expansion should be anticipated rather than clipped.

Do not apply a single negative `top` tweak globally. Alignment offsets are tied to specific face/size/icon relationships and must survive zoom and fallback.

## Evidence
Evidence includes mixed-script strings, superscripts/subscripts where relevant, icons of different visual bounds, badges, inline code, fallback font activation, text scaling, and screenshots at several rasterization scales. Measure baselines/line boxes and inspect clipping, not just apparent centering at 100% zoom.

## Failure Modes
Failure includes icons appearing to sag below adjacent text, CJK or accented glyphs clipped by a line-height tuned to Latin, badges expanding row height unpredictably, fallback runs jumping vertically, and center-aligned inline controls that visually disconnect from the textual baseline. Repeated per-component nudges that disagree across contexts are another failure signal.

## Falsification
Falsification forces fallback faces, inserts tall/deep glyphs, increases text size, and compares multiple inline element types in the same row. If alignment requires different ad-hoc offsets at each zoom or supported glyphs clip, the baseline contract fails.

## Recovery
Recovery restores adequate line-box metrics, defines shared alignment tokens/relationships for recurring inline element classes, and adjusts icons by optical bounds rather than arbitrary container coordinates. Where script metrics differ materially, allow line-height growth instead of cropping language support to preserve a rigid row.

## Output and Handoff
Output: `mixed-font-baseline-alignment-contract` with participating metric systems, baseline/optical rules, line-box allowances, reusable offsets, fallback behavior, and mixed-run evidence. Handoff whole-role fallback geometry to fallback-metric engineering.

## Sibling Boundary and delete-the-skill
Fallback metric compatibility compares alternate faces occupying the same role over time. This skill aligns different metric systems present simultaneously. Removing it leaves mixed-run baseline and clipping decisions without an owner.