---
name: routing-ui-work
description: Use when a contracted UI task needs the smallest sufficient set of product, architecture, interaction, visual, system, inclusive, specialist, and verification skills.
---

# Routing UI Work

## Overview
The router is a classifier and scheduler, not a designer. Its job is to keep context focused while preventing a relevant faculty from being silently omitted.

## Parent Contract
**Required parent:** `nolane-ui`.

Require a valid `ui-contract`. If the contract is missing, return to `ui-contracting`; do not infer a new contract inside the router.

## Build the `UI_TASK_PROFILE`
Profile observable task characteristics, not keywords:

### Intent
Choose one or more: `design-new`, `redesign`, `extend`, `audit`, `reproduce`, `implement`, `verify`, `systemize`.

### Surface
Record product family and subtype: marketing, SaaS application, dense enterprise tool, editor/canvas, dashboard, commerce, content/publication, communication, developer tool, mobile application, kiosk/TV, embedded control, game, visualization, or other with a concrete description.

### Users and task pressure
Record expertise, frequency, time pressure, error cost, cognitive load, accessibility needs, and whether the surface is used casually, repeatedly, or under operational stress.

### Information
Estimate density, hierarchy depth, volatility, comparability needs, real-time behavior, and whether scanning or deep reading dominates.

### Interaction
Record keyboard intensity, touch/gesture needs, direct manipulation, selection, drag/drop, destructive actions, async work, permissions, offline/error behavior, and interruption sensitivity.

### Visual freedom
Record brand maturity, existing design-system strength, reference fidelity, desired emotion, novelty tolerance, content/imagery availability, and whether the surface needs a memorable signature or should disappear behind the task.

### Constraints
Accessibility target, localization/RTL, privacy/trust, platform conventions, performance limits, responsive scope, themes, and implementation constraints.

### Evidence capabilities
Browser inspection, screenshot capture, semantic/accessibility tree, interaction testing, component explorer, design source, visual target, and human review availability.

## Faculty selection rules
Select a skill only when it owns a decision or verification obligation that materially exists in this task.

**Always for material new design:** `modeling-product-intent`, `modeling-users-and-tasks`, `architecting-information`, `designing-interactions`, `modeling-component-states`, `exploring-aesthetic-directions` unless direction is already fixed, `directing-visual-hierarchy`, `architecting-design-tokens`, `adapting-responsive-layouts`, and `designing-accessible-interfaces`.

**Conditional routing examples:**
- complex navigation → `designing-navigation`
- multi-step goal → `designing-task-flows`
- forms/validation → `designing-forms`
- search/filtering → `designing-search`
- high-density operational UI → `designing-data-dense-interfaces`
- quantitative comparison → `designing-data-visualization`
- localization/unknown locales/RTL → `designing-localized-interfaces`
- meaningful animation/state transition → `designing-motion`
- new component language → `architecting-component-systems`
- platform-native behavior matters → `adapting-platform-conventions`
- faithful target → `verifying-design-fidelity`

**Verification routing is independent of generation routing.** For material completion, select critic lenses based on failure impact even if the corresponding generation skill was not used.

## Inactive faculties
A relevant-looking faculty may be inactive only with an explicit reason tied to the contract. Good: `designing-motion inactive — accepted static design and reduced-motion-only scope`. Bad: `not needed`.

## Sequence by dependency, not category
Typical dependency edges:
`product/users → IA/flows → interaction/semantics/states → aesthetic/hierarchy/composition → tokens/components → responsive/platform/inclusive → render → critics/fidelity → gate`.

Do not force this into a linear transcript. Parallel faculties may work from the same stable upstream contract.

## Output: `ui-task-profile`
Return all profile dimensions plus:
- `selected_skills[] {name, reason, required_inputs, expected_output}`
- `inactive_faculties[] {faculty, reason}`
- `critical_paths[]`
- `verification_lenses[]`
- `capability_gaps[]`
- `routing_confidence`

## Routing anti-patterns
- Keyword routing: “dashboard” automatically means charts, cards, dark mode.
- Maximal routing: loading every skill “to be safe.” Context dilution is a defect.
- Aesthetic routing before product semantics.
- Letting framework choice suppress accessibility or state modeling.
- Assuming mobile from responsive, or responsive from mobile; route platform behavior explicitly.
