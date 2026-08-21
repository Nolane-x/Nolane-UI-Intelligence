---
name: diagnosing-runtime-text-rendering-drift
description: Use when implemented text does not match expected wrapping, weight, line boxes, glyph shapes, spacing, or baselines and the cause may be resolved fonts, browser metrics, platform rasterization, fallback, or runtime CSS.
---

# Diagnosing Runtime Text Rendering Drift

## Drift Is an Observation Problem
A visual mismatch in text can originate from the wrong font file, synthetic weight, fallback glyphs, CSS inheritance, browser rounding, variable-axis defaults, platform rasterization, or different content. This skill owns the diagnosis that separates those causes before anyone “fixes” the screenshot with arbitrary spacing.

## Parent Contract
**Required parent:** `crafting-typography`.

The parent defines intended typography. This specialist investigates why runtime evidence diverges from that intent; it does not redesign the type system as the first response.

## Diagnostic Stack
Capture canonical content first, then computed style, resolved font face, font file/revision, variation settings, language/script, font-feature settings, actual line boxes, device pixel ratio, zoom, browser/OS, and screenshot. Distinguish metric drift from raster-only appearance drift: a glyph may look heavier on one platform while geometry remains identical.

Compare a known control string and the failing string. If only certain glyphs differ, suspect fallback or subset coverage; if all lines wrap differently, inspect metrics/size/container width; if weight differs with identical geometry, inspect available instances and synthetic styling.

## Evidence
Evidence is a reproducible render packet, not a verbal “looks off.” Include computed CSS, `document.fonts`/resolved-face information where available, resource hashes, geometry measurements, and side-by-side captures at matched scale. Pin environment versions when claiming a browser/platform-specific drift.

## Failure Modes
Characteristic Failure includes fixing line-height when the wrong fallback face loaded, adding letter spacing to compensate for a stale font build, blaming anti-aliasing for actual container-width differences, comparing screenshots at different DPR/zoom, and declaring parity based on CSS declarations even though the browser resolved a different font.

## Falsification
Falsification recreates the render in a controlled environment, swaps only one suspected variable, and predicts the observed change before testing. If changing the alleged cause does not remove the drift, reject that hypothesis. A diagnosis without a variable-isolation experiment is provisional.

## Recovery
Recovery restores the intended resource/metric/style source, removes compensating hacks, and re-renders under the same evidence packet. If the drift is an unavoidable platform rasterization difference with preserved geometry and readability, record the bounded variance rather than chasing pixel identity.

## Output
Output: `runtime-text-rendering-drift-contract`, containing symptom, controlled environment, resolved font/style evidence, competing hypotheses, isolation experiment, root cause, accepted variance, and corrective action.

## Handoff
Handoff font-resource timing to loading transitions, fallback geometry to metric compatibility, and actual typographic redesign to the parent.

## Sibling Boundary and delete-the-skill
Rendered-UI critique may detect that text differs, but it does not own font-resolution root-cause diagnosis. Removing this skill leaves runtime typography drift vulnerable to cosmetic patches without falsifiable causal evidence.