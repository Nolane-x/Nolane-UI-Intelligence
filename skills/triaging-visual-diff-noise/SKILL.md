---
name: triaging-visual-diff-noise
description: Use when visual regression systems produce image differences and reviewers must distinguish product regressions from anti-aliasing, animation, font rasterization, dynamic content, capture timing, subpixel layout, or other nondeterministic noise without masking real defects.
---

# Triaging Visual Diff Noise

## Why triage needs its own owner
Visual diffs are useful only if reviewers can trust signal density. Too much noise causes blanket approvals and inflated thresholds; too aggressive suppression hides meaningful spacing, typography, contrast, clipping, and alignment defects. This skill owns the decision process that classifies a diff and chooses the narrowest mitigation that removes nondeterminism without weakening the visual contract.

## Parent Contract
**Required parent:** `binding-ui-evidence`.

The parent establishes evidence lineage. This specialist activates after a visual comparison has produced a difference and before that difference is accepted, rejected, masked, or used to update a baseline.

## Noise taxonomy
Classify observed deltas by mechanism: anti-aliasing/rasterization, font-load timing, animation or transition frame, dynamic data, timestamps/random IDs, network-delayed assets, subpixel rounding, GPU path, color profile, scrollbar/OS chrome, capture clipping, or true product change. The decision owner is causal classification, not merely pixel area or diff percentage.

A small diff can be highly material—for example a one-pixel focus ring disappearance or a clipped descender. A large diff can be benign if a deterministic timestamp changed across an otherwise correct page. Never equate magnitude with severity.

## Triage workflow
First confirm that baseline and current capture represent the same semantic state and environment. Then inspect diff localization, layout geometry, computed styles, asset/font status, and timing. Reproduce with the same build to estimate nondeterminism before comparing different revisions. If the same revision yields different images, product-change conclusions are premature.

Use masks only for regions whose content is intentionally outside the claim and whose geometry cannot conceal nearby defects. Prefer deterministic fixture data, disabled animations, stable fonts, and pinned environments over broad pixel thresholds. Thresholds should target a known noise distribution, not be raised until CI turns green.

## Evidence
Evidence includes baseline/current/diff images, environment fingerprints, same-revision repeat captures, suspected cause, controlled reproduction, and the mitigation decision. If a mask or tolerance is introduced, record its scope and why it cannot hide a material invariant. Preserve examples of known noise to keep future triage consistent.

## Failure modes
Characteristic Failure includes approving all low-percentage diffs, masking dynamic containers whose size can regress, treating fallback fonts as harmless anti-aliasing, increasing global tolerance after one flaky component, and updating baselines before isolating capture timing. Another failure is reviewer fatigue: a noisy suite creates so many expected diffs that genuine regressions receive no meaningful inspection.

## Falsification
Introduce a deliberate one-pixel alignment error inside a noisy region, shift font load timing, enable animation, randomize fixture text, and capture the same revision repeatedly. The triage policy fails if the deliberate defect is suppressed, if repeated same-revision captures remain unexplained, or if reviewers cannot distinguish a baseline update from a noise mitigation.

## Recovery
When noise is systemic, fix the capture environment or fixture at the narrowest cause. Remove stale masks and retest whether they are still necessary. If a real supported-environment rendering difference exists, do not classify it as noise simply because it is inconvenient; route it to rendered-environment drift and product support decisions.

## Output and Handoff
Output: `visual-diff-noise-contract`, containing noise classification, reproduction evidence, mitigation choice, mask/threshold boundaries, and confidence. Handoff legitimate design changes to regression-baseline governance, environment divergence to rendered-environment drift, and canonical image identity to visual-regression baselines.

## Sibling Boundary and delete-the-skill
Sibling visual-regression baselines define what is expected; this skill decides whether an observed pixel delta is trustworthy evidence of change. Baseline governance decides when the reference may move. The delete-the-skill test passes because without a noise triage owner, teams choose between flaky visual tests and dangerously permissive suppression.