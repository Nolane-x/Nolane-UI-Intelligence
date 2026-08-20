---
name: designing-cold-start-preference-capture
description: Use when a recommendation product has little or no behavioral history and asks users for topics, goals, examples, constraints, follows, or other seed preferences to create an initial experience without overstating what is known.
---

# Designing Cold Start Preference Capture

Cold start is an uncertainty state. Preference capture should gather the smallest useful set of explicit signals while making skipping, revising, and exploring possible instead of forcing users to define a permanent identity before they have seen the product.

## Parent Contract
**Required parent:** `designing-recommendation-personalization-surfaces`.

The parent owns recommendation behavior. This skill owns first-use preference seeding and the transition from explicit onboarding signals into normal ranking.

## Seed Strategy
Choose preference questions that materially affect available ranking. Topics, creators, goals, skill level, content format, budget, dietary constraints, location, or examples may be useful depending on domain. Do not ask for data simply because it is easy to collect or visually fills an onboarding screen.

Show representative options without creating selection bias toward only popular categories. Search/browse can supplement curated seeds when the taxonomy is large. If a user cannot find their interest, allow free exploration rather than forcing a nearest wrong category.

## Commitment Level
Make selections provisional and editable. Avoid language like “build your perfect feed” when a handful of taps cannot establish stable preferences. Explain that recommendations will improve or adapt based on future choices only if the system actually behaves that way.

Provide skip when personalization is optional. A skipped user should receive a coherent contextual/editorial baseline rather than a broken empty surface or repeated coercive prompt.

## Diversity and Exploration
Initial selections can overconstrain the feed. Reserve space for adjacent/exploratory items so users can discover preferences they did not know to declare. Do not interpret missing selections as explicit dislike unless the onboarding explicitly says so.

## Evidence
Test no selections, one selection, many conflicting selections, rare interest, changed selection after onboarding, skipped onboarding, taxonomy update, and child/new account scenarios where policy differs. Compare emitted preference seed with first ranking request.

## Failure Modes
- Onboarding asks for signals that ranking ignores.
- Missing selection is treated as negative preference.
- Skip produces empty or unusable experience.
- Early choices become difficult to change later.
- Only popular categories are offered, narrowing new users immediately.
- Copy claims precise personalization from minimal evidence.

## Falsification
Complete onboarding with one rare topic, then inspect the first recommendations and preference store. Falsify if the topic is not used, if unrelated omissions become dislikes, or if the interface claims certainty inconsistent with sparse evidence.

## Recovery
Reduce questions to ranking-effective signals, make seeds editable, treat omissions as unknown, provide baseline content, and preserve exploration. If seed-to-ranking linkage cannot be proven, remove the question or recast it as non-personalized setup.

## Handoff
Durable editing belongs to `designing-personalization-controls`; exploration balance to `designing-recommendation-diversity-controls`; post-onboarding behavior to `designing-ranking-feedback-loops`.

## Output Contract
Return a `cold-start-preference-capture-contract` with `seed_signals[]`, `ranking_linkage`, `skip_baseline`, `selection_commitment`, `taxonomy_access`, `omission_semantics`, `exploration_policy`, `first_rank_evidence[]`, `falsification_cases[]`, and `recovery_actions[]`.