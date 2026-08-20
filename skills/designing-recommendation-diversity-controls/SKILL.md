---
name: designing-recommendation-diversity-controls
description: Use when recommendation surfaces risk becoming repetitive or overly narrow and users or product policy need controllable diversity across topic, source, viewpoint, creator, format, novelty, price, or other domain dimensions without a fake universal diversity score.
---

# Designing Recommendation Diversity Controls

Diversity is multidimensional. A feed can contain many creators but one topic, many topics but one format, or broad categories while repeating nearly identical items. The interface must name the dimension being broadened and preserve user goals.

## Parent Contract
**Required parent:** `designing-recommendation-personalization-surfaces`.

The parent owns ranked surfaces. This skill owns user-facing or product-visible diversity mechanisms and their evidence boundaries; it does not define a universal ranking-quality metric.

## Diversity Dimensions
Choose domain-relevant axes: creator/source, topic, format, novelty, popularity, price band, geography, difficulty, ideology/viewpoint where appropriate and carefully governed, recency, or product category. Do not combine them into one unexplained “diversity” percentage that hides tradeoffs.

A diversity control can be direct (“more new creators”), indirect (“explore outside my usual topics”), or policy-driven with disclosure. Make clear whether it adjusts future recommendations, only the current view, or a durable preference.

## Relevance Tradeoff
More variety is not always better. A user asking for a precise operational next action should not receive random exploration for diversity. Set context-specific bounds and keep mandatory/safety content outside optional diversity tuning. Provide a way to return to focused relevance.

## Repetition and Saturation
Track repeated exposure and near-duplicate items. Diversity controls should reduce meaningful redundancy, not merely shuffle order. If inventory is genuinely narrow, say so rather than manufacturing superficial variety with lower-quality substitutes.

## User Agency
Allow users to broaden or narrow without forcing them to understand algorithm parameters. Explain the effect in product language and offer reset. For sensitive viewpoint/political domains, avoid implying normative “balance” without explicit product policy and authority.

## Evidence
Construct inventories with creator concentration, topic concentration, duplicates, and sparse alternative inventory. Toggle each supported diversity mode and inspect resulting distributions while holding other factors as constant as feasible. Test reset and persistence scope.

## Failure Modes
- One opaque diversity score replaces multiple dimensions.
- “More variety” injects irrelevant content into high-precision tasks.
- Repeated near-duplicates remain because only creator IDs differ.
- Sparse inventory is hidden by low-quality filler.
- Diversity preference has unclear persistence or cannot be reset.
- Sensitive viewpoint balancing is introduced without policy authority.

## Falsification
Build two feeds with identical item count: one diverse by creator but not topic, another by topic but not creator. Falsify if the control/system labels both equivalently without naming the chosen dimension. Toggle broadening in a precision task; falsify if core intent is lost.

## Recovery
Expose dimension-specific controls, bound exploration by context, detect semantic repetition, and show inventory limits. If product policy cannot justify a sensitive diversity dimension, remove it rather than dressing it as neutral algorithm quality.

## Handoff
Feedback effects route to `designing-ranking-feedback-loops`; preference persistence to `designing-personalization-controls`; recommendation-surface labeling remains with the parent.

## Output Contract
Return a `recommendation-diversity-controls-contract` with `diversity_dimensions[]`, `control_scope`, `relevance_bounds`, `repetition_model`, `inventory_scarcity_state`, `persistence_reset`, `sensitive_dimension_authority`, `distribution_evidence[]`, `falsification_cases[]`, and `recovery_actions[]`.