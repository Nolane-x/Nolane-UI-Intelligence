---
name: designing-color-grading-controls
description: Own color grading interaction across exposure, balance, curves, wheels, qualifiers, masks, shot matching, LUTs, color-space context, bypass, versioning, and scope comparison.
---
# Designing Color Grading Controls

## Decision ownership

Own authored color adjustments for video/imagery in an editing context. Decide grading node/layer scope, primary controls, curves/wheels, secondary qualifiers/masks, LUT application, color-space/transform context, shot comparison, bypass, still/reference capture, and versioning. Generic color crafting does not own image signal transformations.

## Inputs and evidence

Require source media color space/transfer/gamut, timeline/output color management, grading model, control ranges, scopes, LUT assets, shot/clip identity, masks/keyframes, reference frames, and render pipeline. Identify camera-log/HDR/SDR workflows where context errors are severe.

## Procedure

Always surface working/output color-space context and where transforms/LUTs occur. Separate technical input transform from creative grade when both exist. Primary controls should have neutral reset and numeric values. Secondary selections/qualifiers need visible mask/key preview. Bypass must indicate whether it bypasses one node, clip grade, or all color processing. Compare modes should lock reference identity/time. Grade copy/paste reveals what components transfer and handles mismatched color context. Save versions without overwriting prior grade state.

## Failure topology

Failures include grading log footage while preview transform is unknown, LUT double-application, bypass scope ambiguous, copied grade across incompatible color spaces, qualifier mask hidden, neutral reset unavailable, and scopes not matching the displayed pipeline. Another failure is a visually pleasing preview that clips output gamut/luminance without warning.

## Falsification

Reject if working/output color context is unknown; if technical transform and creative grade cannot be distinguished; if bypass scope is unclear; if reference frame identity is lost; if scopes read a materially different pipeline than viewer; if copied grade ignores context mismatch; or if out-of-range/output clipping has no detection where available.

## Output contract

Return a `color-grading-controls-contract` with: source/working/output color context; technical transform; grade scope; primary/secondary controls; LUTs; masks/qualifiers; bypass/reset; reference/compare; versioning; copy/paste compatibility; scope pipeline; and gamut/luminance warnings. Include one double-LUT and one HDR-to-SDR case.

## Handoffs

Video scopes provide measurement evidence, keyframes animate grade parameters, render/export applies output transforms, and external asset provenance governs LUT sources.