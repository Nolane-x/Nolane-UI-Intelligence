---
name: designing-first-run-onboarding
description: Use when a new user enters the product for the first time and the experience must establish identity, initial context, essential setup, first value, and a safe exit into normal product use.
---

# Designing First-Run Onboarding

## Parent Contract
**Required parent:** `designing-onboarding`.

This faculty owns the transition from an uninitialized user/account/workspace into a usable first product state. It does not own the entire education system, a multi-stop product tour, or every setup wizard. Its success criterion is not “the user saw onboarding”; it is that the minimum required state exists and the user reaches a meaningful first-value surface without avoidable coercion.

## Decision Architecture
Separate mandatory initialization from optional education. Required steps may include accepting an invitation context, choosing a workspace, creating a first object, confirming a profile field, selecting a minimal preference, or connecting a required resource. Optional personalization, tutorials, and marketing questions must not be disguised as blockers.

Design the shortest credible path to first value. A blank dashboard followed by seven preference questions is not inherently onboarding. If the product can infer safe defaults, use them and let users revise later. When a choice has lasting consequence—public username, organization region, billing entity, data residency—make that consequence visible and avoid presenting it like a lightweight preference.

State must survive interruption. Define what happens if the browser closes halfway through, an invitation expires, a required external connection fails, or the user reaches the normal product through a deep link before onboarding is formally complete. Do not create an unescapable loop that redirects every route back to a generic wizard when the missing step is only relevant to one capability.

## Failure Topology
- Optional “tell us about yourself” questions are marked required and delay first value.
- User completes four steps, refreshes, and starts from step one because progress was client-only.
- Invitation context is lost and onboarding creates a new empty workspace instead of joining the intended one.
- A long setup path explains features before the user has any concrete product context.
- Skip button exists but leads to a broken empty product with no recovery route.
- A consequential region or account type is chosen with no explanation that changing it later may be difficult.

## Falsification and Recovery
Falsify with invitation-based entry, direct signup, interrupted setup, external service failure, mobile viewport, deep link into a capability before onboarding completes, returning user on a new device, keyboard/screen-reader operation, and a user who wants to skip all nonessential education. The design fails if first-run completion is measured by screen visitation rather than the existence of required usable product state.

Recover by defining required initialization facts, persisting progress server-side where durable, preserving entry context, deferring optional learning, providing safe defaults, and routing incomplete capability-specific setup only when the user reaches that capability.

## Output Contract
Return `first-run-onboarding-contract` with required initialization state, optional/deferred steps, first-value target, defaulting policy, entry-context preservation, interruption/resume behavior, deep-link handling, consequential-choice warnings, skip semantics, accessibility requirements, and falsification cases.