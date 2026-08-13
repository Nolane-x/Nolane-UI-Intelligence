---
name: modeling-component-semantics
description: Use when choosing or creating UI components and the visual pattern must accurately represent content, action, selection, disclosure, navigation, status, or containment semantics.
---

# Modeling Component Semantics

## Overview
Choose components by what they mean and how they behave, then style them. This skill is a constraint solver against component-by-fashion design.

## Parent Contract
**Required parent:** `routing-ui-work`.

Consume IA and interaction needs. Existing design-system components are candidates, not automatic answers when their semantics are wrong.

## Semantic classification
For each UI element first classify its role:
- command/action
- navigation/destination
- value/input
- selection among options
- disclosure of additional content
- status/state
- feedback/message
- grouping/containment
- data comparison
- media/content

Then identify cardinality, persistence, urgency, reversibility, and whether the element owns focus or changes context.

## Pattern choice questions
Before using a component ask:
1. What user concept does this represent?
2. Is the action immediate, navigational, or stateful?
3. Must alternatives be visible simultaneously?
4. How many items can exist now and later?
5. Does the user need comparison or only selection?
6. What keyboard/touch semantics are expected?
7. What happens under long content and localization?
8. Is the container carrying meaning or merely decoration?

## Examples of semantic distinctions
- Tabs switch among peer panels in one context; they are not a generic replacement for navigation hierarchy.
- Radio options expose a small mutually exclusive set; a select may hide a larger/less frequently compared set.
- A button performs an action; a link changes location/resource. Styling them alike does not erase semantic behavior.
- Tooltip supplies supplemental information; essential instructions need a persistent/discoverable home.
- A card is useful when a bounded object/group needs a shared interaction or visual boundary. Whitespace/list structure is often better when no boundary is semantically required.

## Native/system-first policy
Prefer, in order:
1. correct native semantic element/pattern
2. project design-system component with correct semantics
3. composition of existing primitives
4. new custom component when the task genuinely introduces a reusable semantic pattern

Do not custom-build a familiar control to gain a decorative effect if it weakens keyboard/accessibility behavior.

## Nested interaction rule
If a container is clickable and contains other controls, explicitly define activation regions, keyboard order, event behavior, and user expectation. Avoid ambiguous nested interactive surfaces.

## Output: `component-semantic-model`
Return `elements[] {concept, semantic_role, chosen_pattern, rejected_patterns, behavior, accessibility_semantics, scale_constraints, rationale}`, plus `new_component_candidates` and `semantic_conflicts`.

## Anti-patterns
- “Everything is a card.”
- Using badges/pills for plain text metadata with no status/filter semantics.
- Turning headings into pseudo-controls through hover styling.
- Icon-only commands where the metaphor is not established and no accessible name exists.

## V6 Semantic Component Proof
Bind every reusable interactive component to a **role-action-state invariant**: the meaning exposed to assistive technology, the action understood by users, and the state changed by activation must describe the same concept. Styling cannot turn a navigation link into an action, a disclosure into a tab, or a checkbox into a command without changing semantics.

Make a **native-first semantic decision** before custom behavior. Record whether a platform-native element already supplies the required semantics, focus, activation, form behavior, and accessibility hooks; reject native use only for a concrete mismatch, not because custom markup is easier to animate. Estimate the component's **semantic surface area**: roles, relationships, keyboard rules, focus ownership, labeling, state announcements, and form/browser behavior that the implementation must preserve.

Specify **accessible-name computation** explicitly for icon-only, composite, labeled-by, described-by, dynamic-count, and validation states. Names must come from stable product language rather than visual tooltip timing. Run a **composition ownership test** when primitives nest: determine which layer owns focus, disabledness, selection, dismissal, escape, outside interaction, and announcements so wrappers do not duplicate or suppress behavior.

### Falsification
Remove CSS and inspect the accessibility/DOM semantics; then replace mouse activation with keyboard/screen-reader use. If meaning disappears with appearance, or nested primitives fight over focus/state, the semantic model is false.

### Recovery
Prefer a stronger primitive or simplify composition before adding ARIA patches. Re-map state/action semantics and retest every consumer because a semantic component bug has system-wide blast radius.
