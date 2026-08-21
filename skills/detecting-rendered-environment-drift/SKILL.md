---
name: detecting-rendered-environment-drift
description: Use when the same UI revision renders differently across CI, local development, browsers, operating systems, fonts, GPU paths, themes, or runtime configuration and the team must determine whether the difference is environmental drift or a product regression.
---

# Detecting Rendered Environment Drift

## Diagnostic ownership
Visual and interaction regressions are difficult to trust when the rendering environment itself moves. A screenshot diff can come from a fallback font, browser update, device scale factor, locale, missing feature flag, color profile, animation clock, or GPU path rather than application code. This skill owns the diagnosis that separates environment drift from product change.

## Parent Contract
**Required parent:** `binding-ui-evidence`.

The parent binds evidence to claims. This specialist starts when two artifacts expected to represent equivalent product state disagree and environment variance is a plausible cause.

## Environment fingerprint
Capture a fingerprint that includes application revision, browser engine/version, OS/build, viewport/container geometry, pixel ratio, font files and load status, locale/time zone, theme/preferences, feature flags, animation/reduced-motion state, relevant GPU/rendering mode, and fixture identity. Add domain-specific dependencies when they can alter rendering.

The decision owner is which differing fingerprint field is causally material. Mere correlation is not enough. Compare controlled pairs where one environment dimension changes at a time when feasible. If several dimensions differ, classify the result as underdetermined until the causal set is narrowed.

## Drift classes
Useful classes include `toolchain_drift`, `browser_drift`, `font_asset_drift`, `configuration_drift`, `fixture_drift`, `hardware_rendering_drift`, and `intentional_environment_variance`. Not all variance should be normalized away. A browser-specific layout defect is still a product regression if that browser is supported; environment diagnosis explains the trigger but does not excuse it.

## Evidence strategy
Evidence includes both environment fingerprints, render artifacts, computed/layout measurements where relevant, font/network traces, feature probes, and controlled reproduction attempts. When anti-aliasing differs but geometry and computed style are stable, record that distinction so visual-diff thresholds can target noise without masking layout defects.

## Failure modes
Characteristic Failure includes updating baselines to match a drifting CI image, blaming “browser differences” without identifying the changed capability, treating missing fonts as harmless raster noise, and comparing different fixture data as though it were environment variance. Another failure is over-normalization: freezing the test harness so tightly that supported real-world environments are never exercised.

## Falsification
Pin all environment dimensions and reproduce the diff; then vary suspected dimensions one at a time. Load a fallback font deliberately, alter DPR, switch engine version, change locale, and compare GPU/software rendering where relevant. The diagnosis fails if it cannot explain the artifact delta, if product-code changes are incorrectly classified as environment drift, or if a supported environment defect gets dismissed solely because another environment passes.

## Recovery
Restore a known reference environment for baseline generation, then decide whether the discovered variant belongs in support coverage. If drift came from an unpinned dependency, pin or record it and recapture affected evidence. If the variant is a real supported-environment defect, route it to implementation rather than increasing diff tolerance.

## Output and Handoff
Output: `rendered-environment-drift-contract`, containing fingerprints, suspected dimensions, controlled comparisons, drift classification, support impact, and remediation. Handoff baseline decisions to visual-regression baselines, environment coverage to browser/device evidence matrices, and noisy pixel differences to visual-diff triage.

## Sibling Boundary and delete-the-skill
Sibling browser/device matrices decide which environments deserve testing; this skill explains unexpected divergence between supposedly comparable evidence. The delete-the-skill test passes because without a drift detector, teams either distrust visual evidence entirely or normalize away real regressions while chasing harness noise.