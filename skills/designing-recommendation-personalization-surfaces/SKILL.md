---
name: designing-recommendation-personalization-surfaces
description: Use when a product surfaces ranked or personalized content, actions, products, people, media, or workflows and users need to understand, control, correct, and safely act on recommendations without confusing ranking with truth.
---

# Designing Recommendation Personalization Surfaces

A recommendation surface is a selective view of a larger possibility space. The interface should help users understand why items are present, how much control they have, and when personalization is uncertain or inappropriate without exposing a fake mathematical certainty.

## Parent Contract
**Required parent:** `routing-ui-work`.

This owner covers recommendation-specific UI behavior. It does not own visual themes or profile customization handled by `managing-theming-and-personalization`; it owns ranked-content presentation, explanation, feedback, cold start, diversity, and user agency.

## Recommendation Context
Declare the decision being assisted: discovery, next action, purchase, media consumption, learning, people connection, operational prioritization, or another domain. Ranking criteria and risk tolerance differ by context. A “recommended next action” in a professional system may require stronger evidence and override than entertainment discovery.

Distinguish personalized, contextual/non-personalized, sponsored, editorial, trending, and required/system items when they coexist. Do not blend paid placement into algorithmic relevance without disclosure. If an item is mandatory or safety-critical, it should not depend on the same opaque ranking that governs optional discovery.

## Surface Semantics
Expose enough reason and source context to let users form the right mental model. “Because you watched X” is useful only if that signal materially influenced the ranking. Avoid decorative explanations generated after the fact. Provide controls for hiding, dismissing, saving, following, or correcting signals according to product capability.

Ranked lists need stable behavior under refresh and feedback. If every small action reshuffles the page, users lose orientation. Decide which feedback applies immediately, which affects future sessions, and which requires confirmation because it changes a durable preference.

## Uncertainty and Harm
New or sparse users may receive low-confidence recommendations. Use exploration, popular/contextual baselines, or preference capture without claiming deep personalization. Sensitive inferences—health, politics, financial distress, or protected characteristics—require product/legal authority and should not be surfaced casually as “we think you like…”.

## Evidence
Test new user, returning user, contradictory behavior, explicit preference change, hidden item, sponsored placement, repeated recommendations, sparse inventory, and sensitive content category. Inspect actual ranking inputs/events so explanations are not validated only by copy.

## Failure Modes
- Sponsored items look like organic recommendations.
- Ranking is presented as objective truth or universal quality.
- Explanation cites a signal that did not affect ranking.
- Dismissal causes the same item to reappear immediately without reason.
- Small feedback causes unstable full-list reshuffling.
- Sensitive inferred preference is exposed without consent/authority.
- Mandatory items are buried because recommendation score is low.

## Falsification
Change one known ranking signal while holding inventory constant. Falsify if the explanation does not track the actual causal signal or if explicit negative feedback has no observable bounded effect. Include a sparse-history user; falsify if the UI claims personalized certainty without evidence.

## Recovery
Separate placement types, bind explanations to ranking provenance, stabilize list updates, expose durable preference controls, and degrade to contextual baselines when personalization evidence is weak. For sensitive inferences, remove the exposure or require the governed consent boundary.

## Handoff
Explanation depth uses `designing-recommendation-explanations`; durable controls use `designing-personalization-controls`; implicit feedback uses `designing-ranking-feedback-loops`; cold start and diversity have dedicated owners.

## Output Contract
Return a `recommendation-personalization-surfaces-contract` with `recommendation_context`, `placement_types[]`, `ranking_claim_boundary`, `surface_actions[]`, `stability_policy`, `sensitive_inference_rules`, `uncertainty_states[]`, `ranking_evidence[]`, `falsification_cases[]`, and `recovery_actions[]`.