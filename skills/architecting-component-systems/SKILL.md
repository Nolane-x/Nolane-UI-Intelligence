---
name: architecting-component-systems
description: Use when repeated UI patterns need stable component APIs, variants, composition rules, ownership, reuse boundaries, or governance across multiple screens or teams.
---

# Architecting Component Systems

## Overview
A component system is a semantic API for product UI. Reuse should reduce inconsistent decisions without forcing unrelated behaviors into one abstraction.

## Parent Contract
**Required parent:** `routing-ui-work`.

Consume component semantics, state matrices, tokens, platform constraints, and existing project components. Existing components are authoritative only within the project’s explicit design-system contract.

## Component boundary test
Create/reuse a component when there is a stable repeated concept with shared behavior, anatomy, states, or accessibility semantics. Do not extract a component solely because two pieces of markup look similar.

A good component can answer:
- what concept does it represent?
- what slots/inputs are valid?
- which states/behaviors does it own?
- which styling decisions are fixed by the system?
- what should consumers not override?

## API design
Prefer semantic props/variants (`intent="danger"`, `density="compact"`) over raw visual switches (`red`, `smallPadding`). Make invalid combinations difficult to express. When combinations are truly independent, use composition rather than a variant explosion.

## Anatomy and slots
Define required/optional parts and their relationships. Slot flexibility is not unlimited layout freedom: specify what content types, length, actions, and nesting are valid.

## Variants
A variant requires a semantic difference that repeats. One-off “marketing-special-blue-compact” variants signal a broken abstraction. Consider composition, local layout, or a new component concept instead.

## State ownership
Centralize universal component behavior—focus, disabled, loading, selected, validation, semantic attributes—while allowing product-specific data/state to remain outside. Shared components should not hide domain state machines behind vague booleans.

## Accessibility as API
If a component requires a label, accessible name, description, relationship, focus management, or keyboard model, make the requirement visible in its API/documentation rather than relying on callers to remember.

## Escape hatches
Every system needs exceptions, but they must be explicit and costly enough to notice. Prefer `className`/style escape hatches only when they do not violate semantic states; record when a repeated escape indicates a missing token/variant/component.

## Governance
Define:
- owner
- contribution criteria
- visual/behavioral regression expectations
- versioning/deprecation
- migration path
- documentation/examples

A component that no one can safely evolve is not a system asset.

## Output: `component-system`
Return `components[] {name, concept, anatomy, api, variants, states, tokens, semantics, accessibility, composition_rules}`, `reuse_decisions`, `new_components`, `exceptions`, `governance`, and `deprecations`.

## Common failures
- One giant component with dozens of booleans.
- Visual variants that encode product semantics inconsistently.
- Reusing a component because it exists even though semantics differ.
- Consumers overriding internal spacing/focus until every instance looks unique.
