---
name: designing-design-code-drift-review
description: Use when design artifacts and production UI have evolved independently and reviewers need to classify visual, semantic, token, component, responsive, interaction, content, accessibility, and intentional-exception drift before deciding what should converge.
---

# Designing Design Code Drift Review

Drift is not automatically a defect. Design and code can diverge because implementation fixed an accessibility issue, production constraints changed, design moved ahead, or one side is stale. Review must classify authority and intent before synchronizing anything.

## Parent Contract
**Required parent:** `designing-design-to-code-handoffs`.

The parent owns the handoff baseline. This skill owns comparison after independent evolution and the decision about intentional, stale, conflicting, or erroneous divergence.

## Drift Dimensions
Compare semantic component identity, component props/variants, token references, resolved visual output, content, asset identity, responsive rules, interaction states, accessibility behavior, platform adaptation, and domain-specific behavior. Pixel difference is only one evidence type and can be noisy across rendering environments.

Bind both sides to exact revisions: design file/version/node set, code commit/build, token package version, component library version, and renderer environment. Without revision identity, a drift report cannot prove which state was compared.

## Classification
For each divergence classify: design ahead, code ahead, intentional production exception, intentional design exploration, stale mapping, regression, accessibility correction, platform-specific adaptation, or unresolved conflict. Require owner/rationale for intentional exceptions so they do not become permanent unexplained debt.

Do not “sync” automatically before authority resolution. A design artifact may contain an obsolete component; production may have drifted from approved brand intent; either side can be wrong. Use user/product requirements, normative standards, project design system, and measured evidence in that authority order.

## Review Interaction
Group related drift by component/decision rather than listing thousands of raw property differences. Provide visual overlay/diff where useful, but connect it to semantic changes. Let reviewers accept exception, update design, update code, update mapping, or request deeper evidence.

## Evidence
Compare known intentional and accidental divergences: token theme update, production accessibility fix, stale design component, responsive bug, copy update, missing error state, and one renderer-only pixel shift. Verify the review distinguishes them instead of maximizing match score.

## Failure Modes
- Any pixel difference is labelled regression.
- Design is assumed authoritative on every dimension.
- Production accessibility fix is overwritten to match outdated design.
- Drift report lacks exact design/code revisions.
- Accepted exceptions disappear from history and reappear every review.
- Semantic component mismatch is hidden because screenshots look similar.
- Reviewer can suppress drift without rationale/evidence.

## Falsification
Introduce one accessibility improvement in code and one accidental token regression while keeping design unchanged. Falsify if the review recommends the same convergence direction for both or cannot explain authority by dimension.

## Recovery
Rebind exact revisions, classify divergence by semantic layer, preserve intentional exceptions, and route each item to the correct owner. Suppress renderer noise only with calibrated evidence; do not raise thresholds to hide a real semantic mismatch.

## Handoff
Visual fidelity evidence uses `verifying-design-fidelity` and `validating-rendered-perception`; component/token mapping repairs use their dedicated design-to-code owners; broader design-system evolution remains with `governing-design-systems`.

## Output Contract
Return a `design-code-drift-review-contract` with `design_revision`, `code_revision`, `environment_identity`, `drift_items[]`, `dimension_authority`, `classification`, `intentional_exceptions[]`, `resolution_actions[]`, `render_semantic_evidence[]`, `falsification_cases[]`, and `recovery_actions[]`.