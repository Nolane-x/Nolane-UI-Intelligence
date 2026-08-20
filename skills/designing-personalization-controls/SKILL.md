---
name: designing-personalization-controls
description: Use when users can inspect, change, reset, pause, or opt out of signals and preferences that influence recommendations and the interface must distinguish durable controls from cosmetic local filtering.
---

# Designing Personalization Controls

Personalization controls define user agency over ranking inputs and outcomes. They should say what changes, how broadly it applies, when it takes effect, and what remains personalized despite the change.

## Parent Contract
**Required parent:** `designing-recommendation-personalization-surfaces`.

The parent owns recommendation surfaces. This skill owns durable user-facing control of preference and personalization state; it does not own visual theming or unrelated profile settings.

## Control Taxonomy
Separate item feedback (“not interested”), topic preference, followed sources, explicit likes/dislikes, history-derived signals, blocked entities, sensitive-topic controls, personalization pause/opt-out, history clearing, and full reset according to product capabilities. A local “hide this card” action should not be described as changing the recommendation model if it only removes one rendered item.

For each control expose scope and persistence: this item, this topic, this surface, this account, this device, or all personalized services. Cross-product personalization needs especially clear scope; users should not infer that changing one feed also changes email or search ranking without evidence.

## Effect and Reversibility
Tell users when changes take effect and whether prior data remain stored. “Turn off personalization” can mean stop using certain data, stop collecting new data, or show non-personalized ranking; these are different privacy/product states. The UI must use the policy's actual semantics.

Provide undo or review history for low-risk feedback where feasible. A full reset or history deletion may be irreversible and should preview consequences without dark-pattern friction.

## Inspectability
Users need a meaningful view of explicit preferences and controllable signals. Do not expose an enormous opaque inferred-profile dump if items cannot be corrected or understood. Group by user-recognizable concepts and distinguish explicit choices from inferred tendencies when surfaced.

## Evidence
Change one preference and verify subsequent ranking events use the new value. Test hide, undo, topic follow/unfollow, pause, opt-out, reset, cleared history, cross-device synchronization, and delayed ranking cache. Confirm UI state against authoritative preference storage.

## Failure Modes
- “Not interested” only hides the current card but is marketed as model feedback.
- Opt-out toggles UI state while ranking still uses the same personal history.
- Control scope is unclear across surfaces/devices.
- Full reset leaves inferred preferences active with no explanation.
- Users cannot undo accidental negative feedback.
- Explicit and inferred preferences look equally user-authored.

## Falsification
Toggle personalization off, then inspect the next ranking request. Falsify if disallowed personalized signals remain active. Change one topic preference on one device and verify expected account/device scope on another device.

## Recovery
Bind controls to authoritative preference operations, expose scope and effective timing, invalidate ranking caches, and distinguish collection/use/storage semantics. If the product cannot prove a control affects ranking, label it as local presentation behavior instead.

## Handoff
Recommendation reasons use `designing-recommendation-explanations`; feedback-event semantics use `designing-ranking-feedback-loops`; cold-start explicit preferences use `designing-cold-start-preference-capture`.

## Output Contract
Return a `personalization-controls-contract` with `control_types[]`, `scope_model`, `persistence_semantics`, `effective_timing`, `data_use_collection_boundary`, `undo_reset_rules`, `preference_inspection`, `ranking_effect_evidence[]`, `falsification_cases[]`, and `recovery_actions[]`.