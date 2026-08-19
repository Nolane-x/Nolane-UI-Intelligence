---
name: designing-progressive-feature-discovery
description: Use when advanced or infrequent capabilities should become discoverable as users gain context and the product must stage exposure without hiding essential actions or overwhelming newcomers.
---

# Designing Progressive Feature Discovery

## Parent Contract
**Required parent:** `designing-onboarding`.

This faculty owns when and how nonessential capabilities become visible or emphasized over time. It does not authorize hiding required functionality behind unexplained maturity gates. Progressive discovery should reduce early cognitive load while preserving stable paths for expert users who already know what they need.

## Decision Model
Classify capabilities by necessity, frequency, prerequisite knowledge, consequence, and expert value. Core actions should remain directly discoverable from the beginning. Advanced filters, automation, shortcuts, bulk operations, or specialized modes may be introduced after relevant context exists, but there should still be a searchable or documented power path for users who arrive experienced.

Trigger discovery from evidence: repeated manual behavior that an automation could replace, first use of a related workflow, creation of enough objects to make bulk action useful, or explicit exploration of an advanced area. Avoid opaque engagement scoring that makes the product mutate unpredictably between users. A suggestion should explain the connection between observed need and capability without exposing creepy telemetry detail.

Exposure is not mastery. After a feature is introduced, do not permanently badge or pulse it until clicked. Let users dismiss suggestions, find them later through help/search, and preserve interface stability. Newly revealed controls should not reflow primary actions unpredictably or alter keyboard order without reason.

## Failure Topology
- Essential export function remains hidden until a user reaches an arbitrary activity score.
- UI constantly rearranges as new features unlock, destroying spatial memory.
- Advanced user cannot find a known capability because the discovery engine thinks they are a beginner.
- Pulsing “New” badges remain for weeks because acknowledgement is tied only to click-through.
- Suggestion appears after one accidental action and feels unrelated to the user's actual task.
- Dismissed feature education returns in multiple surfaces because suppression is not shared.

## Falsification and Recovery
Falsify with an experienced new account, a novice high-activity account, feature availability changed by plan/permission, dismissed suggestions, keyboard navigation after a reveal, mobile layout, a capability reachable through command search, and telemetry unavailable. The design fails if access to required functionality depends on behavioral profiling or if progressive exposure changes the core navigation model unpredictably.

Recover by keeping essential actions stable, using explicit contextual prerequisites, providing expert bypass/search paths, separating availability from promotion, persisting acknowledgement/dismissal, and limiting visual emphasis to a bounded introduction period.

## Output Contract
Return `progressive-feature-discovery-contract` with capability classes, visibility baseline, contextual triggers, expert bypass paths, promotion surfaces, acknowledgement/dismissal, layout-stability rules, permission/plan interaction, telemetry fallback, and falsification cases.