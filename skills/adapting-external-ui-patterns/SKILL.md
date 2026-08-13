---
name: adapting-external-ui-patterns
description: Use when an external UI source has been selected for adaptation or inspiration and its mechanism must be reconciled with the product's actions, semantics, content, tokens, states, accessibility, platform behavior and visual identity without creating a foreign island.
---

# Adapting External UI Patterns

## Parent Contract
**Required parent:** `selecting-ui-building-blocks`.

Receive a source selection whose decision is `adapt` or `inspire`, with canonical citation, inspected mechanism, source role, license posture where code reuse is material, local capability/action IDs, component system, design tokens, visual direction, platform constraints and known integration risks.

## Decision Boundary
This faculty owns **translation into the local product language**. It decides what of an external pattern survives, what is re-expressed, and what is discarded. It does not discover candidates, choose between libraries, or certify the final implementation. It must preserve the useful mechanism while preventing external code from importing a second semantic model, second design system or demo-specific content into the product.

Adaptation is not restyling. Changing a purple gradient to the brand blue while leaving foreign states, labels, focus behavior, motion timing and data assumptions untouched is still a bad transplant. The adaptation contract operates across semantics, state, interaction, content, visual tokens, motion, responsiveness and accessibility.

## Product Truth
Copy-paste UI libraries optimize for demonstration and reuse. Their examples often contain placeholder labels, isolated states, ideal content lengths, default icons, demo timing, fixed assumptions about data, and their own radius/shadow/color vocabulary. When AI pastes them verbatim, the result becomes a collage: one section behaves like shadcn, another like a motion gallery, another like Material, while the underlying product has different actions and domain language.

The strongest use of external work is usually **mechanism transfer**. A morphing card can teach object continuity; a command palette can teach progressive access; an animated number can teach change emphasis; a state-machine primitive can teach keyboard/focus transitions. The product then owns the final expression.

## Decision Model
1. **Name the source mechanism in neutral terms.** Replace brand/demo wording with behavior: shared-layout continuity, staggered reveal, inertial drag with snap, collision-aware popover, semantic disclosure, animated numeric interpolation, masked text transition, canvas pan/zoom, or another concrete relation.
2. **Bind to canonical product actions.** Every trigger and completion event maps to `action-registry` IDs. Remove demo handlers and invented actions. If no action exists, return a closure defect rather than fabricating one.
3. **Map state machines.** Align source states to the product's component and screen states. Add product-required loading, empty, error, disabled, permission, destructive confirmation, offline, interrupted and recovery states that the demo omitted. Delete source states that have no product meaning.
4. **Reconcile semantics.** Use the product's roles, names, keyboard contract, focus policy and announcement requirements. If the source is visual-only, pair it with the selected semantic primitive instead of reimplementing semantics from scratch.
5. **Reconcile content.** Replace demo copy with domain language, realistic lengths, localization stress cases, numbers, dates, errors and labels. Content geometry is part of adaptation; a card that only works with two-word English labels is not adapted.
6. **Reconcile tokens.** Map typography, spacing, radius, color, border, elevation, iconography and density through the local token/component system. Record intentionally new tokens instead of scattering literal values.
7. **Reconcile motion.** Preserve the information purpose, not exact spectacle. Map durations/easing to local motion grammar, define interruption and retargeting, reduced-motion alternative, focus continuity, entry/exit symmetry and low-performance behavior.
8. **Reconcile responsive behavior.** Define what the mechanism becomes under smaller viewport, touch, keyboard, coarse pointer, zoom, large text and reduced motion. An effect may collapse to a simpler transition without losing the action.
9. **Remove foreign coupling.** Strip demo analytics, unused providers, unrelated dependencies, global CSS, sample assets and source-specific layout assumptions. If a dependency is retained, expose it through a local component or adapter boundary appropriate to its depth.
10. **Record provenance in the implementation.** Keep a reference-ledger citation and adaptation boundary near the decision record. Attribution/license notices are preserved where required. Inspiration and code reuse must remain distinguishable after months of maintenance.
11. **Define verification obligations.** Name the local behaviors that must be runtime-tested after adaptation, especially focus, keyboard, hydration, drag/drop, async transitions and reduced motion.

## Evidence
Evidence is the selected source's inspected files and docs plus local product contracts. Before/after renders can prove visual reconciliation; accessibility-tree snapshots and keyboard tests can prove semantic reconciliation; performance traces can prove the mechanism fits the budget; localized content fixtures can prove geometry survives realistic content.

A material external mechanism must keep its canonical source citation even after heavy adaptation. This is not only attribution hygiene: it lets future agents trace why an unusual mechanism exists, revisit upstream fixes, and detect when a copied implementation has diverged beyond safe updateability.

If the selected decision was `inspire`, the contract should explicitly state that final code is locally implemented and which abstract mechanism was learned. If `adapt`, identify the retained code/algorithmic boundary and license obligations. Never blur the two to make provenance easier to ignore.

## Output Contract
Return `ui-adaptation-contract` with:
- `source {id, canonical_url, usage: adapt|inspire, inspected[], provenance_refs[]}`
- `mechanism`
- `adaptation_boundary`
- `product_actions[] {source_event, canonical_action_id}`
- `state_mapping[] {source_state, local_state, disposition}`
- `semantic_mapping {roles, keyboard, focus, announcements}`
- `content_rewrite[]`
- `token_mapping[]`
- `motion_mapping {purpose, timing, interruption, retargeting, reduced_motion}`
- `responsive_mapping[]`
- `dependency_cleanup[]`
- `attribution_and_license_obligations[]`
- `runtime_verification_obligations[]`
- `unresolved_conflicts[]`

No unresolved semantic or product-action conflict may be silently accepted.

## Failure Traps
- Copying demo labels such as “Get Started” into a domain workflow with a specific action name.
- Keeping foreign radii, gradient palette, shadow system and hover language because “it looks premium.”
- Mapping two distinct source events to one vague product action.
- Preserving an animation even when reduced motion removes the information it carried.
- Reimplementing dialog/menu semantics just to keep an effect rather than composing with a stronger local primitive.
- Leaving provider/global-style dependencies that exist only for the demo page.
- Treating responsive adaptation as scaling the desktop component smaller.
- Forgetting long labels, RTL, text zoom, touch and coarse-pointer behavior.
- Removing attribution or license notices required by the selected material.
- Losing the source citation after code is copied into a local component.
- Copying a recognizable brand composition or trade dress when only a mechanism was needed.
- Declaring the adaptation correct without downstream integration and runtime proof.

**Hard gate:** adaptation must map the external mechanism to canonical product actions, states, semantics, tokens, content, motion and responsive behavior; visual resemblance alone is never sufficient.
