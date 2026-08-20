---
name: designing-responsive-intent-handoff
description: Use when design artifacts contain multiple frames, constraints, breakpoints, container behavior, visibility rules, or recomposition and implementation needs the underlying responsive intent rather than interpolating screenshots.
---

# Designing Responsive Intent Handoff

Responsive handoff should transmit how a layout changes under available space, content pressure, input mode, and platform constraints. Multiple screenshots are samples; they do not by themselves define the rule between samples or beyond them.

## Parent Contract
**Required parent:** `designing-design-to-code-handoffs`.

The parent owns design-to-code translation. This skill owns responsive rule extraction and handoff; generic responsive design principles remain with `adapting-responsive-layouts`.

## Intent Representation
For each structural region describe container behavior, min/max constraints, intrinsic sizing, wrapping, stacking, ordering, overflow, pinning, visibility, density, and breakpoint/recomposition conditions. Prefer content/container-driven rules where that is the product intent rather than inventing breakpoint numbers from frame widths.

Distinguish continuous resize from discrete recomposition. A two-column editor becoming tabbed panes is a structural state change; shrinking both columns until unusable is not responsive fidelity. Record which actions remain reachable after recomposition and where navigation state moves.

## Samples and Coverage
Treat design frames as evidence points. For each point capture viewport/container dimensions and state, then infer only rules supported by design/system guidance. Unknown intermediate behavior should be marked for design decision or prototype validation, not filled with generic CSS defaults.

Text expansion, localization, zoom, dynamic data, virtual keyboard, and safe areas can trigger responsive stress absent from polished frames. Include these obligations in the handoff if material.

## Component Interaction
Responsive behavior may belong inside reusable components or at page composition. Map ownership so generated implementation does not duplicate breakpoint logic at every call site. When production components already own collapse behavior, hand off desired intent to their supported API.

## Evidence
Implement/rescale across more widths than supplied design frames, plus long text, zoom, keyboard, and representative content extremes. Compare structure/action reachability, not only pixel position. Capture where design evidence was insufficient and what decision resolved it.

## Failure Modes
- Breakpoints are guessed solely from screenshot widths.
- Intermediate widths overflow despite endpoint screenshots matching.
- Structural recomposition is replaced with proportional shrinking.
- Hidden mobile action has no alternative path.
- Responsive logic is duplicated outside a component that already owns it.
- Localization/content stress was absent from handoff and breaks production.

## Falsification
Provide only desktop and mobile frames, then render at several intermediate container widths with expanded copy. Falsify if the implementation cannot explain its transitions from handed-off rules or loses required actions between samples.

## Recovery
Express responsive states/rules explicitly, assign behavior ownership, add stress constraints, and mark unsupported ranges. If design intent is genuinely unknown, route a design decision instead of generating arbitrary breakpoints.

## Handoff
Component behavior uses `designing-component-mapping-to-code`; visual implementation verification uses `verifying-design-fidelity`; general responsive system ownership remains with `adapting-responsive-layouts`.

## Output Contract
Return a `responsive-intent-handoff-contract` with `sample_frames[]`, `continuous_rules[]`, `recomposition_states[]`, `trigger_conditions`, `action_reachability`, `content_stress_cases[]`, `component_ownership`, `unknown_ranges[]`, `render_evidence[]`, and `recovery_actions[]`.