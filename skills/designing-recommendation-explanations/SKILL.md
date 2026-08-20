---
name: designing-recommendation-explanations
description: Use when users need to understand why a particular recommendation appeared and the product must provide truthful, useful, non-manipulative explanations tied to actual ranking evidence and actionable control.
---

# Designing Recommendation Explanations

An explanation is useful only if it reflects the mechanism that materially affected the recommendation and helps the user decide whether to trust, ignore, or correct it. Generic “recommended for you” copy does not satisfy that contract.

## Parent Contract
**Required parent:** `designing-recommendation-personalization-surfaces`.

The parent owns recommendation presentation. This skill owns item-level and surface-level explanation semantics and their connection to actual ranking provenance.

## Explanation Levels
Use different explanation depth for different decisions. A casual content card may need a short reason; a professional priority recommendation may need source signals, recency, constraints, and uncertainty. Do not dump model features indiscriminately—raw features can be unintelligible or privacy-sensitive.

Classify explanation sources: explicit preference, prior interaction, item similarity, followed person/topic, contextual location/time, collaborative behavior, editorial rule, sponsorship, or system constraint. Only show a source if the production ranking path confirms it materially contributed or if it is clearly labelled as a general policy explanation rather than causal claim.

## Actionable Explanations
Pair explanation with the control it makes possible. “Because you follow Design” can link to manage followed topics; “Because you bought X” can offer “not relevant” or remove that activity from personalization if supported. Avoid explanations that reveal a cause but leave users powerless to correct an incorrect inference.

## Privacy and Social Signals
Do not expose another person's private behavior as the reason for a recommendation. Collaborative signals should be aggregated or described at a safe level. Sensitive inferred attributes should generally not be surfaced as explanatory text unless the product has explicit authority and a clear user benefit.

## Consistency
If the same item appears in different surfaces for different reasons, explanation should match the local ranking context. Cached explanation text must invalidate when ranking reason changes. Sponsored/editorial placement should not borrow organic personalization explanations.

## Evidence
Sample recommendation events with logged contribution/reason data, then compare rendered explanations. Include multiple contributing signals, no strong reason, paid placement, sensitive signal, stale cache, and ranking fallback. Ask whether users can predict which setting or feedback would change future recommendations.

## Failure Modes
- Explanation is post-hoc marketing text unrelated to ranking.
- Top feature is shown even when it had negligible influence.
- Collaborative reason reveals another user's private activity.
- Cached explanation survives after ranking reason changes.
- “Why this?” gives no corresponding control or useful decision context.
- Sponsored placement claims a personalization cause.

## Falsification
Force the ranking system to swap from explicit-preference reason to contextual fallback while keeping the item identical. Falsify if the explanation remains unchanged or claims a causal signal absent from the event evidence.

## Recovery
Bind explanation to logged ranking provenance, downgrade to non-causal policy language when causality is not available, redact sensitive/social detail, and connect to the correct preference/feedback control. Missing reason evidence becomes UNKNOWN rather than invented prose.

## Handoff
Durable preference changes use `designing-personalization-controls`; implicit/explicit feedback processing uses `designing-ranking-feedback-loops`; placement disclosure remains with the parent recommendation surface.

## Output Contract
Return a `recommendation-explanations-contract` with `explanation_levels`, `reason_sources[]`, `causal_evidence_requirement`, `action_links[]`, `privacy_redactions`, `cache_invalidation`, `fallback_explanation`, `evidence_samples[]`, `falsification_cases[]`, and `recovery_actions[]`.