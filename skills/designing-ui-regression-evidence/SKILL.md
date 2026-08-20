---
name: designing-ui-regression-evidence
description: Design regression evidence that detects meaningful changes in rendered appearance, interaction, accessibility, content, and responsive state without equating every pixel difference with a defect.
---

# Designing UI regression evidence

UI regressions can be visual, behavioral, semantic, content-related, or responsive. Use this skill when release gates need evidence that an intended change did not damage unrelated user experience.

## Decision ownership

Own regression planes, scenario selection, baseline versioning, diff thresholds, review ownership, and acceptance criteria. Decide which changes can be automatically classified and which require human judgment.

## Inputs and evidence

Collect critical journeys, components/states, viewport matrix, themes, locales, accessibility trees, visual snapshots, interaction tests, content fixtures, and historical regressions. Identify unstable data or animation that creates noisy baselines.

## Procedure

Build a risk-based scenario set that covers important states, not just default screenshots. Pair visual diffs with interaction and semantic checks where appearance alone cannot establish correctness. Freeze or normalize nondeterministic data responsibly.

Version baselines alongside the code or artifact they represent. Require intentional baseline updates to explain why change is expected. Use tolerances for anti-aliasing while keeping structural changes visible.

Include zoom, responsive, error, loading, and empty states for high-risk surfaces.

## Failure topology

Pixel-only tests create noise and review fatigue. Automatic baseline regeneration can approve regressions by construction. Another failure is testing only happy paths while failure states drift.

Snapshot approval without linking to the intended change loses audit value.

## Falsification

Seed known defects—missing focus ring, clipped localization, hidden action, changed error text—and verify the evidence suite detects them. Introduce harmless rendering noise and ensure it does not overwhelm reviewers. Audit random baseline updates for rationale.

## Output contract

Produce a `ui-regression-evidence-contract` defining coverage planes, risk scenarios, baseline lifecycle, deterministic fixtures, diff thresholds, review/approval rules, and seeded-defect sensitivity tests.

## Handoffs

Use `designing-visual-diff-review` for screenshot comparison, `designing-interaction-fidelity-audits` for behavior, `designing-content-fidelity-audits` for text, `designing-accessibility-evidence-packages` for semantics, and responsive parity verification.