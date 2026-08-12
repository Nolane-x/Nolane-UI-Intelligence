---
name: ui-contracting
description: Use when a UI task has material ambiguity about outcome, users, authority, fidelity, constraints, success, non-goals, or allowable assumptions.
---

# UI Contracting

## Overview
A strong UI cannot be judged against a moving target. This skill turns a request into a bounded design contract without inventing requirements the user never gave.

## Parent Contract
**Required parent:** `nolane-ui`.

Consume the original request and context. Do not replace explicit user language with a fashionable interpretation.

## Contract dimensions
Compile eight dimensions:
1. **Outcome:** what users must be able to understand or accomplish.
2. **Actors:** primary users, secondary users, operators, reviewers, assistive-technology users, and affected non-users when relevant.
3. **Authority:** exact user requirements, product constraints, existing design-system rules, platform rules, standards, references, and model assumptions. Tag the source of each.
4. **Surface scope:** screens, states, flows, breakpoints, themes, locales, and platforms in or out of scope.
5. **Fidelity:** exploratory, directionally consistent, design-system consistent, or faithful reproduction. Never silently downgrade a user-stated fidelity level.
6. **Success:** observable task outcomes, required information, visual/brand outcomes, interaction behavior, and verification expectations.
7. **Non-goals:** what the agent must preserve or not redesign.
8. **Unknowns:** missing facts that could materially change a decision.

## Assumption policy
Classify assumptions as:
- `safe-default`: reversible, low-consequence, easy to expose.
- `design-hypothesis`: plausible but must be tested/criticized.
- `blocking`: guessing could violate a material requirement.

Do not ask questions merely because an answer could be nicer. Ask only when the unknown is blocking and cannot be resolved from authoritative context. Otherwise choose a bounded default and record it.

## Conflict resolution
When two instructions conflict, use the repository authority hierarchy. Do not solve conflict by blending incompatible requirements. Name the winning authority and record the displaced rule. A community heuristic can never override a user requirement or normative constraint merely because it sounds more “professional.”

## Preservation boundary
For redesigns, explicitly list what is frozen: product semantics, copy, flow, data, routes, keyboard behavior, brand assets, or existing component contracts. “Improve the UI” is not permission to rewrite the product.

## Output: `ui-contract`
Required fields:
- `objective`
- `primary_user_outcomes`
- `actors`
- `authorities[] {statement, level, source}`
- `surface_scope {included, excluded}`
- `fidelity_level`
- `success_observables`
- `preservation_boundary`
- `constraints`
- `non_goals`
- `assumptions[] {statement, class, falsifier}`
- `unknowns[] {question, materiality, disposition}`

## Hard gate
A contract is not valid if “beautiful,” “modern,” “clean,” or “premium” is used as a success criterion without operational meaning. Translate such language into observable design qualities appropriate to the product: hierarchy, density, material treatment, distinctiveness, typography character, restraint, motion behavior, trust, or fidelity.

## Common failures
- Treating a reference screenshot as authority over hidden product behavior it cannot show.
- Inventing fake metrics, marketing claims, navigation, or content to make a mockup look full.
- Turning every unknown into a user question instead of using bounded defaults.
- Treating implementation-framework convenience as a product requirement.
- Forgetting non-goals, then “improving” adjacent surfaces the user wanted preserved.
