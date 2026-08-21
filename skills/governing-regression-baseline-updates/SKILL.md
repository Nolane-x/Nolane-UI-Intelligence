---
name: governing-regression-baseline-updates
description: Use when visual, interaction, snapshot, or other regression references need to change and the team must prove the baseline is obsolete because the product contract intentionally changed rather than accepting new output merely to make verification pass.
---

# Governing Regression Baseline Updates

## Baseline changes are contract changes
Updating a regression baseline changes what future verification will call correct. That makes baseline promotion a governance decision, not test maintenance. This skill owns when a reference may move, what evidence must accompany the move, and how reviewers distinguish intentional product evolution from accidental normalization of a defect.

## Parent Contract
**Required parent:** `binding-ui-evidence`.

The parent governs evidence and claim lineage. This specialist begins after a regression comparison differs and someone proposes changing the approved reference rather than changing the product output.

## Update admissibility
A baseline update is admissible only when there is evidence of an intentional contract change, an invalid prior fixture/environment, or a corrected reference artifact. Record the decision source: approved design change, component contract revision, normative requirement update, fixture correction, supported-environment rebaseline, or documented rendering-tool migration.

The decision owner is not whether the new image “looks okay”; it is whether the old expectation is no longer the correct expression of the product contract. If the rationale is unknown, the diff remains unresolved.

## Scope control
Promote the smallest affected baseline set. A typography token change may legitimately affect many components, but bulk approval still needs a shared causal explanation plus sampling or automated checks proving no unrelated layout changes hitchhiked on the update. Avoid “accept all” operations whose review unit exceeds human ability to inspect.

When one change intentionally modifies only a subset of states, preserve untouched baselines. If fixture semantics also changed, separate fixture-change evidence from appearance-change evidence so future reviewers can reconstruct what moved and why.

## Authority and review
Define who may approve baseline movement by risk. Low-risk isolated visual changes may be reviewed by a component owner; high-risk accessibility, financial, safety, public-service, or design-system-wide changes may require a separate reviewer or evidence owner. The implementer should not be the only authority for changes that erase failing evidence.

## Evidence packet
A baseline update should include old reference, current render, diff, relevant contract/design decision, environment fingerprint, fixture identity, affected state set, and approval record. For large changes, include an impact summary generated from actual changed artifacts but keep representative raw diffs available.

## Failure modes
Characteristic Failure includes updating references automatically after tests fail, accepting large baseline sets with no causal grouping, rebaselining from an unpinned environment, letting fixture changes silently redefine expected behavior, and using baseline promotion to hide a real browser-specific defect. Another failure is missing history: only the new baseline remains, so reviewers cannot reconstruct what was intentionally changed.

## Falsification
Introduce an unrelated regression alongside a legitimate design change, change a fixture and image in the same patch, and generate baselines from a drifting environment. The governance contract fails if the unrelated defect is accepted under the same rationale, if no reviewer can reconstruct the old expectation, or if a new baseline can be promoted without naming the product contract that changed.

## Recovery
When a questionable baseline was accepted, restore the prior reference from history, isolate intended changes, regenerate in a pinned environment, and reopen unresolved diffs. Keep the mistaken promotion as evidence in the decision record rather than erasing it. Tighten scope or reviewer requirements if the failure exposed a systematic approval weakness.

## Output and Handoff
Output: `regression-baseline-updates-contract`, containing admissible reasons, affected scope, reviewer authority, old/new evidence, environment and fixture identity, and historical trace. Handoff raw image expectation to visual-regression baselines and suspected nondeterminism to visual-diff triage.

## Sibling Boundary and delete-the-skill
Sibling visual-regression baselines define reference identity; this skill governs changing that reference. Manual-review evidence defines how human verdicts are recorded, not the special risk of erasing regression evidence. The delete-the-skill test passes because without update governance, any failing regression test can be converted into a pass by redefining expected output.