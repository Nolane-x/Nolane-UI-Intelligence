---
name: designing-visual-diff-review
description: Review visual diffs by classifying perceptual and structural change, separating rendering noise from meaningful regressions, and tying approval to intended design deltas.
---

# Designing visual diff review

Visual diff tools can produce thousands of changed pixels for one font-rendering shift and miss the significance of a tiny moved icon. Use this skill when humans or automated systems review screenshot changes.

## Decision ownership

Own diff presentation, change classification, ignore/tolerance rules, viewport/theme grouping, approval rationale, and escalation. Decide when a perceptual overlay, side-by-side, blink, or structural metadata best supports review.

## Inputs and evidence

Collect baseline/candidate screenshots, DOM/layout metadata where available, intended change description, environment details, font/browser versions, animations, dynamic data, and known anti-aliasing noise.

## Procedure

Present before/after alongside a diff mask and contextual metadata. Group changes by surface and expected feature. Classify changes as intended, incidental but acceptable, regression, environment noise, or unresolved. Require reviewers to inspect the actual rendered states, not only heat maps.

Use stable fonts/data and disable nondeterministic animation where it does not belong to the test. Define narrow ignore regions only with rationale; broad masks can hide real regressions.

## Failure topology

Reviewers habituate to large noisy diffs and click approve. Pixel thresholds can ignore a small but critical label disappearance. Another failure is accepting all diffs because a redesign was intentional, allowing unrelated regressions to ride along.

Masks and tolerance settings can grow until tests have little sensitivity.

## Falsification

Seed small meaningful defects and large harmless noise. Verify reviewers/tools distinguish them. Audit ignored regions and tolerances over time. Compare candidate screenshots against intended change scope and flag unrelated regions automatically where possible.

## Output contract

Produce a `visual-diff-review-contract` defining comparison views, classification taxonomy, environment controls, tolerances/masks, approval rationale, grouping, and sensitivity tests for subtle meaningful changes.

## Handoffs

Use `designing-ui-regression-evidence` for scenario selection, `designing-interaction-fidelity-audits` for nonvisual behavior, typography/responsive specialists for root-cause review, and `designing-design-decision-records` for accepted intentional deltas.