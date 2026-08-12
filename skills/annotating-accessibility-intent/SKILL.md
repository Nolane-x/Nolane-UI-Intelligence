---
name: annotating-accessibility-intent
description: Use when a design, prototype, component spec, Figma-like artifact, custom interaction, or handoff needs semantic role, keyboard, focus, state, announcement, reading order, target, and alternative-input intent preserved into implementation.
---

# Annotating Accessibility Intent

## Overview
Accessibility semantics disappear easily between visual design and code because pixels do not encode role, name, focus, keyboard, or announcement behavior. Annotate the interaction contract where design decisions are made.

## Parent Contract
**Required parent:** `routing-ui-work`.

Require component/flow semantics and root accessibility obligations. Annotation complements runtime verification; it is never proof that the implementation matches the annotation.

## Decision Model
Annotate only information that cannot be reliably inferred from the visual artifact. For each custom or nontrivial component record semantic role/pattern, accessible name source, description/help relationship, states/properties, keyboard interactions, focus entry/traversal/exit/return, reading order, dynamic announcements, error semantics, target/gesture alternatives, and reduced-motion behavior.

Use native semantics as the default reference. If design calls for a custom widget, name the intended interaction pattern and why native behavior is insufficient. Avoid specifying ARIA attributes cosmetically without understanding the interaction promise they create.

For flows, annotate focus after route/dialog transitions, error summary behavior, async status, destructive confirmation, drag alternatives, modal scope, and what happens after deletion. For responsive variants, state whether semantic/read order changes or only visual order changes.

Annotations need stable ids tied to design components/regions so developers and QA can trace them. Design-system components can inherit known annotations; product-specific deltas override only with explicit reason. Keep platform-specific input behavior separate when the same design asset targets web, native, TV, or XR.

## Evidence
Review annotation against WCAG/APG/platform guidance, user/task model, component state matrix, and accessibility specialist skills. At implementation, verify DOM/accessibility tree, keyboard/screen reader, zoom/contrast/motion, and actual focus. Track annotation-to-code mismatches as findings.

## Output Contract
Return an `accessibility-annotation-contract` with `annotated_elements[] {id, semantic_role, name_source, states, keyboard, focus, reading_order, announcements, alternatives, motion}`, `flow_annotations[]`, `responsive_semantic_rules`, `inherited_component_annotations[]`, `platform_deltas[]`, and `handoff_verification[]`.

## Failure Traps
- “Add ARIA” annotation with no role/interaction model.
- Visual tab order mistaken for reading/focus order.
- Custom dropdown annotated only with color/contrast.
- No focus return after dialog/delete.
- Drag interaction annotated but no non-drag path.
- Responsive visual reorder silently changing semantic order.
- Assuming design annotation guarantees code behavior.

Accessibility intent should be inspectable before code and falsifiable after code.