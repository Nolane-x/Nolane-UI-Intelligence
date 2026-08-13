---
name: designing-accessible-interfaces
description: Use when a UI must support keyboard, assistive technology, contrast, reflow, target size, motion preferences, semantic structure, or other inclusive interaction requirements.
---

# Designing Accessible Interfaces

## Overview
Accessibility is part of design semantics from the start. This skill converts relevant standards and user needs into design obligations; automated tools remain partial evidence.

## Parent Contract
**Required parent:** `routing-ui-work`.

Normative standards and authoritative platform accessibility guidance outrank community heuristics. For web work, ground requirements in the applicable WCAG version and ARIA Authoring Practices when custom widget semantics/keyboard patterns are relevant. Do not quote a remembered rule when exact conformance materially matters; consult the authoritative source.

## Three layers
### Design-time
Specify:
- information hierarchy and reading order
- non-color state cues
- contrast obligations
- target sizing/spacing
- zoom/reflow/content growth
- motion/reduced-motion plan
- error identification and recovery
- understandable labels/instructions

### Component-time
Specify:
- native semantic element or justified custom role
- accessible name/description relationships
- role/state/value exposure
- keyboard interaction
- focus visibility and focus movement
- disabled/read-only semantics
- live-region/status behavior when needed

### Runtime
Verify:
- actual accessibility/semantic tree
- keyboard traversal and activation
- focus after dialogs, deletion, navigation, async updates
- zoom/reflow and text resize as applicable
- contrast with rendered colors
- high contrast/forced colors where targeted
- screen-reader behavior for critical custom widgets when capability exists

## Native-first principle
Use native controls and semantics whenever they satisfy the interaction. Custom widgets inherit an obligation to reproduce the expected keyboard, focus, state, name, and platform behavior.

## Focus model
Define where focus starts, how it moves, where it is trapped (only for true modal contexts), where it returns, and what happens when the focused item is removed. Visual focus must remain perceivable against every relevant surface/state.

## Keyboard
Every critical pointer action needs an appropriate keyboard path unless the contract explicitly targets a context where that requirement differs. Avoid positive tabindex ordering hacks. Ensure composite widgets follow the correct established pattern rather than exposing every internal item as an incoherent tab stop.

## Errors and status
Associate errors with affected inputs/regions and expose meaningful state. Do not rely on red borders alone. Async success/error announcements should inform without creating noisy repeated live-region output.

## Color and contrast
Use deterministic measurement against rendered foreground/background combinations when the applicable standard defines thresholds. Do not treat disabled/decorative exemptions as permission to mute information users still need.

## Reflow and magnification
Preserve content, task order, and access when text grows/viewport narrows. Horizontal scrolling may be appropriate for intrinsically two-dimensional data, but ordinary reading/controls should not require both-axis hunting.

## Target and motor accessibility
Provide adequate interactive target size/spacing according to the applicable standard/platform. Separate visible icon size from hit target where needed.

## Motion
Respect user motion preferences. Replace motion-carried information with non-motion cues rather than merely removing transitions and losing meaning.

## Automated tests
Use axe/Lighthouse/platform tools as **oracles for the rules they test**, not as a declaration that the interface is accessible. Many usability, naming, focus-order, screen-reader, cognitive, and contextual issues require manual/independent evaluation.

## Output: `accessibility-obligations`
Return `standard_scope`, `semantic_structure`, `keyboard_model`, `focus_model`, `name_role_state`, `contrast_checks`, `reflow_checks`, `target_checks`, `motion_checks`, `error_status_checks`, `assistive_tech_checks`, `automated_checks`, and `manual_checks`.

## Stop conditions
If the requested claim is “WCAG compliant” or equivalent and required normative criteria/runtime evidence cannot be checked, scope the claim or mark it `UNKNOWN/BLOCKED`. Never convert a tool score into full compliance.

## V6 Accessibility Requirement Trace
Build an **accessibility-requirement trace** from each material task to perceptual, operable, understandable, robust, and communication obligations plus relevant platform/standard requirements. Generic “WCAG compliant” is not a task model and cannot prove a particular flow usable.

For interaction-heavy surfaces produce a **keyboard-path proof** including focus order, visible focus, entry/exit, composite navigation, shortcuts, modal trapping/restoration, drag alternatives, and no keyboard trap. Maintain a **programmatic-relationship map** for labels, descriptions, errors, groups, headings, landmarks, tables, ownership, current/selected state, and dynamic changes.

Apply a **sensory-equivalence test** whenever meaning is carried by color, sound, spatial placement, animation, haptics, or imagery: alternate access must preserve the information/action, not merely provide a generic text label. Track the **conformance-usability gap** where automated or standards checks pass but disabled users still face excessive verbosity, disorientation, inaccessible timing, or inefficient task paths.

### Falsification
Complete critical workflows with keyboard only, screen reader, zoom/forced colors, reduced motion, and relevant alternative inputs; also inspect automated results for false confidence. Any material action or state with no workable path falsifies accessibility completion.

### Recovery
Fix semantics/flow/component ownership at the source, not with after-the-fact overlays. Route unresolved disability-specific problems to the relevant specialist and block release claims until evidence exists.
