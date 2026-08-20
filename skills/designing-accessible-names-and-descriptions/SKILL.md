---
name: designing-accessible-names-and-descriptions
description: Use when interactive controls, icons, composite widgets, or dynamic objects need stable nonvisual identities whose names and descriptions match the actions users perceive.
---

# Designing Accessible Names and Descriptions

## Parent Contract
**Required parent:** `designing-screen-reader-experiences`.

This faculty owns how an interface object is named and, when necessary, further described to assistive technology. It separates identity from supplemental explanation and prevents implementation labels from diverging from visible language. It does not own general interface copy; it owns the semantic string exposed for recognition and operation.

## Decision Boundary
Prefer a visible label as the canonical accessible name when one exists. Programmatic naming should not replace clear on-screen language merely to satisfy a technical check. Icon-only controls need a concise action-oriented name; images need alternatives based on the information or function they carry, not file names. Descriptions are reserved for information that changes understanding but would make the name unwieldy, such as constraints, current consequence, or unusual state.

Treat naming as identity across state. A toggle's name should usually remain the object or action family while state is exposed separately, rather than changing unpredictably between unrelated phrases. When multiple controls share visible text, nearby context or semantic grouping must make each one distinguishable. Avoid stuffing role, state, keyboard hints, and decorative punctuation into the name when those are already exposed by platform semantics.

## Failure Topology
- An icon button has no name or exposes an internal asset filename.
- Visible text says “Delete project” while the accessible name says “Remove,” making voice and speech users operate a different vocabulary.
- `aria-label` hides richer visible text from the accessibility name computation.
- A description repeats the name word-for-word and creates redundant speech.
- Dynamic badges are appended to names on every update, destabilizing recognition and voice targeting.
- Several “Edit” controls are indistinguishable when navigated outside visual context.

## Falsification and Recovery
Inspect the computed accessibility tree and then operate with screen reader and voice control. Compare visible labels, spoken names, and command phrases on normal, disabled, selected, loading, and error states. The design fails if users must memorize invisible terminology, if names change for cosmetic state updates, or if descriptions bury the primary action behind a long preamble.

Recover by binding names to the product's canonical action/object vocabulary, exposing state through proper semantics, moving optional explanation into descriptions, and disambiguating repeated controls with product context. Re-test localization because programmatic labels often escape the normal translation path.

## Output Contract
Return `accessible-name-description-contract` with naming source precedence, icon/image rules, repeated-control disambiguation, state/name separation, description eligibility, localization obligations, prohibited redundancy, and assistive/voice verification cases.
