---
name: designing-visual-regression-baselines
description: Use when rendered UI must be compared against approved visual references and the team needs a disciplined baseline model that separates intentional design change from rendering defect, environment noise, and stale reference data.
---

# Designing Visual Regression Baselines

## Baseline authority
A screenshot baseline is an assertion about what an interface is expected to look like under a defined state and environment. It is not automatically truth because someone accepted it once. This skill owns how visual baselines are created, scoped, versioned, and linked to design intent so diffs can be interpreted rather than blindly approved.

## Parent Contract
**Required parent:** `binding-ui-evidence`.

The parent governs claim-to-evidence binding. This specialist begins when a visual claim depends on comparison to a prior approved render.

## Baseline identity
Every baseline should bind `(surface, state_fixture, viewport, pixel_density, theme, locale, platform_or_browser, font_assets, revision, approval_reason)`. Omit dimensions only when evidence shows they do not affect rendering. The decision owner is which environment dimensions are part of the visual contract and which should be normalized away.

Baselines must correspond to reachable product states. A manually staged DOM that cannot occur in the real product may be useful for component development but should not masquerade as end-to-end fidelity evidence. Keep state fixture identity and design-system version with the baseline.

## Intentional change versus drift
A changed image is not automatically a regression, and a matching image is not automatically correct. Intentional visual changes need a rationale tied to a design/system decision. Unexpected changes need triage. Some regressions alter no pixels in the chosen baseline because the wrong state was captured; baseline design therefore depends on state coverage, not just screenshot count.

Use masks and thresholds cautiously. Mask truly nondeterministic regions only when they are outside the claim under test. A wide tolerance can turn baseline testing into a ceremonial green check that misses spacing, typography, or contrast drift.

## Evidence quality
Strong visual evidence includes the baseline, current render, diff artifact, environment metadata, state fixture, and decision record for any accepted change. Where anti-aliasing or font rasterization differs by environment, supplement raw pixel comparison with layout geometry, computed styles, or semantic measurements rather than raising the threshold indiscriminately.

## Failure modes
Characteristic Failure includes baselines captured from an unpinned environment, approval of huge diff sets without review, stale references after component state changes, masks that hide real content movement, and visual tests that assert one viewport while claiming responsive fidelity. Another failure is baseline laundering: a broken current render is simply promoted to new baseline to make CI green.

## Falsification
Change one spacing token, load a fallback font, alter device scale factor, mutate fixture content, and inject a deliberate one-pixel alignment defect. The contract fails if the baseline cannot identify which environmental or product change caused the diff, if a meaningful defect disappears under tolerance, or if an accepted baseline has no traceable approval reason.

## Recovery
When diffs explode, first stabilize environment and fixture identity before reviewing design changes. Re-capture only after proving why the old baseline is invalid. Preserve change evidence linking old and new references. If a baseline’s state is no longer reachable, retire it explicitly rather than letting it silently rot.

## Output and Handoff
Output: `visual-regression-baselines-contract`, containing baseline identity, environment pins, fixture binding, tolerance/mask policy, approval lineage, and retirement rules. Handoff noisy diffs to visual-diff triage and baseline promotion decisions to regression-baseline governance.

## Sibling Boundary and delete-the-skill
Sibling responsive regression matrices decide which viewport/layout states need evidence; this skill governs the reference image for an admitted state. Rendered-environment drift diagnoses why the same contract renders differently across environments. The delete-the-skill test passes because without baseline governance, screenshot testing can prove only difference—not whether the reference itself is legitimate.