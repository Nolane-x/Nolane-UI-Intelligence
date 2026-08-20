---
name: designing-responsive-breakpoint-authoring
description: Use when a visual builder lets authors define responsive behavior and must make breakpoint inheritance, overrides, transformations, preview widths, content pressure, and cross-range state explicit.
---

# Designing Responsive Breakpoint Authoring

## Parent Contract

**Required parent:** `designing-visual-application-builders`.

This faculty owns the authoring UX for responsive rules inside a builder. It consumes responsive design principles from `adapting-responsive-layouts`, but focuses on how people inspect, create, inherit and remove range-specific decisions without accidentally freezing a layout to device-name presets.

## Decision structure

Represent responsiveness as a rule system with explicit precedence. Authors need to know whether the current value is base, inherited from a broader range, locally overridden, computed from a container, or produced by an intrinsic layout algorithm. A highlighted viewport button is not enough. The inspector should answer: **why is this value true at this width?**

Separate viewport preview from breakpoint creation. Dragging a preview continuously is evidence discovery; creating a breakpoint is a durable authoring decision. Encourage breakpoints at pressure transitions in content or interaction, not one per fashionable device. If the runtime supports container queries, surface the containing context and avoid pretending a global viewport width governs every reusable component.

Define how overrides propagate. Mobile-first, desktop-first and range-bounded systems have different inheritance semantics. Deleting an override should reveal the resulting inherited value before commit. Copying styles between breakpoints must not duplicate stale values that were meant to remain fluid. Structural transformations—sidebar to sheet, grid to stack, inspector docking change—need stronger representation than a handful of property overrides because they can alter focus order and capability placement.

Keep authored state continuous while preview widths change. Selection, active component scope, draft property edits and runtime test state should not reset on every breakpoint crossing. When an object is absent in the current range, preserve selection through an outline/ghost representation and clearly indicate why it is not rendered.

## Evidence

Inspect runtime CSS/layout capabilities, actual container hierarchy, representative long/localized content, component reuse in different parent widths, continuous resize recordings and exported code/schema. Test both property changes and structural transformations; simple width/color examples do not exercise the authoring model.

## Failure topology

Failures include every viewport preset silently creating overrides; orphaned values that continue applying after a breakpoint is deleted; components authored against viewport queries even when embedded in narrow panels; hidden elements that vanish from inspector context; and responsive previews that look correct but export contradictory media rules due to source-order precedence.

Another failure is breakpoint archaeology: after several months nobody can determine why a value applies because inheritance is encoded only by small colored dots with no provenance.

## Falsification

Author one reusable component in wide and narrow containers, continuously resize, create/remove overrides, change base values after overrides exist, localize labels, zoom, and perform at least one structural transformation. The contract is falsified if the author cannot predict which ranges change before commit, if exported/runtime behavior differs from inspector provenance, or if deleting a rule leaves an unexplained computed state.

## Recovery

Expose the cascade as inspectable provenance, consolidate redundant breakpoints, replace device presets with pressure-derived rules where possible, and convert structural transformations to explicit modes/variants rather than scattered hidden overrides. Preserve a reversible diff when normalizing old responsive rules.

## Output contract

Return a `responsive-breakpoint-authoring-contract` containing range model, inheritance direction, provenance display, viewport-vs-container rules, preview behavior, override creation/removal, structural-transform representation, hidden-object selection policy, continuous-resize evidence and export verification.

## Handoffs

Use `adapting-responsive-layouts` for product-level transformation decisions, layout-constraint authoring for geometry mechanics, style-inheritance inspection for non-responsive cascade provenance, and design-to-code responsive handoff when authored intent must cross tool boundaries.