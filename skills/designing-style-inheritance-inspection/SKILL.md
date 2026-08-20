---
name: designing-style-inheritance-inspection
description: Use when a visual builder must explain where a rendered style comes from across tokens, themes, component defaults, inherited properties, selectors, variants, states, breakpoints, and local overrides.
---

# Designing Style Inheritance Inspection

## Parent Contract

**Required parent:** `designing-visual-application-builders`.

This skill owns **style provenance** in authoring tools. It is distinct from designing a token system or choosing visual values. The user should be able to identify the winning source of a property, understand what would change if they edit/remove it, and avoid accidental local overrides that sever system relationships.

## Provenance graph

Model a rendered property as a resolved chain, not a flat input box. Possible sources include browser/platform defaults, builder base styles, inherited parent properties, design tokens/aliases, theme mode, component definition, variant, state, selector/class, responsive override, instance override and local inline value. The exact layers depend on the runtime; the inspector must mirror real precedence rather than invent a simplified hierarchy that produces different results.

For every editable property show three truths where material: current computed value, authored source, and inheritance/alias path. A color resolving to `#1f...` is insufficient if the author needs to know it comes from `semantic.action.primary` through a dark-theme alias. Likewise, `font-size: 14` inherited from the parent should not look like an explicitly authored child value.

Editing intent matters. When a user changes an inherited value at an instance, offer the correct target: override this instance, edit component definition, edit token, or modify the current variant/state. Do not default to the narrowest layer merely because it is easiest to implement; that creates override debt. Removing a local value must preview the inherited result so the operation is not a blind reset.

Conflicts deserve explanation. If a state selector or breakpoint outranks the value the user is editing, surface the stronger source immediately. Avoid controls that accept a value but appear to do nothing because another layer wins.

## Evidence

Use the actual style resolution engine, token graph, component/variant schema, runtime computed styles, responsive/state examples and exported output. Compare the inspector's provenance with the runtime for nested components, themes, pseudo/state styles and inheritance-sensitive properties.

## Failure topology

Failures include showing computed values as if locally authored; creating local overrides whenever a user drags a slider; losing token linkage after a harmless-looking edit; hiding a stronger selector that makes edits ineffective; and “reset” clearing several intentional layers instead of only the current one.

A long-term failure is style debt that the UI helped create: thousands of locally frozen values make global theme or component updates appear broken even though the cascade is functioning exactly as authored.

## Falsification

Pick properties with several simultaneous sources, switch theme/state/breakpoint, edit from both definition and instance scopes, remove overrides and inspect exported/runtime styles. The contract fails if the inspector cannot name the winning source, if an edit target differs from what the UI implied, if token/alias relationships disappear silently, or if reset outcome cannot be predicted before commit.

## Recovery

Rebuild the inspector around real resolution provenance. Mark authored versus computed values visually and textually, expose stronger/weaker layers, and provide targeted “edit source” navigation. Offer safe normalization from accidental local values back to system sources with a reviewable diff rather than bulk clearing.

## Output contract

Return a `style-inheritance-inspection-contract` containing precedence layers, property provenance schema, computed/authored distinction, edit-target choices, token/alias traces, conflicting-source behavior, reset semantics, theme/state/breakpoint examples and runtime parity checks.

## Handoffs

Use token and theme owners for semantic value architecture, component-instance overrides for per-instance intent, breakpoint authoring for responsive layers, component authoring for definition scope, and design-code drift owners when runtime CSS no longer matches builder provenance.