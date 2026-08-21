---
name: designing-content-pressure-breakpoints
description: Use when responsive thresholds should be derived from observed content or task failure rather than device categories and each breakpoint needs evidence tied to a real pressure condition.
---

# Designing Content-Pressure Breakpoints

## Breakpoint as Failure Boundary
A breakpoint is justified when the current composition stops satisfying an invariant: labels collide, comparison becomes impossible, line measure degrades, actions wrap into ambiguity, or critical context leaves the visible task. This skill owns the evidence that locates those boundaries and the policy for selecting stable thresholds around them.

## Parent Contract
**Required parent:** `adapting-responsive-layouts`.

The parent chooses the overall responsive architecture. This specialist replaces folklore device widths with measured content/task pressure.

## Pressure Inventory
For each region enumerate pressures: text expansion, numeric growth, optional badges, dynamic actions, localization, zoom/text scaling, user-generated names, validation messages, and data density. Identify the first violated invariant as available space decreases. Do not choose a breakpoint merely because a framework exposes a convenient token.

Use a safety margin around the observed failure so minor font/render differences do not create threshold chatter. When two pressures fail at different widths, decide whether one composition can absorb both or whether separate transitions are materially justified.

## Evidence
Evidence is a sweep of representative content across widths with explicit failure annotations, not a gallery of arbitrary device screenshots. Include long realistic strings, text scaling, loading/error states, and data extremes. Keep a control case showing that the wider composition remains preferable above the threshold.

## Failure Modes
Failure includes breakpoints that work only with English fixture text, command rows that wrap one pixel before the declared breakpoint, thresholds inherited from marketing device classes, excessive micro-breakpoints responding to every small collision, and a narrow layout activated too early despite ample content capacity.

## Falsification
Falsification substitutes worst-plausible content, changes font metrics, enables browser zoom/text scaling, and sweeps through threshold neighborhoods. If failure occurs materially before the selected transition or the alternative composition is already needed above it, the breakpoint evidence is falsified.

## Recovery
Recovery returns to the failing invariant, adjusts the composition or safety margin, and collapses redundant thresholds. If pressure comes from a single pathological component, repair that component rather than moving a global breakpoint that perturbs unrelated regions.

## Output
Output: `content-pressure-breakpoints-contract`, recording each threshold, triggering invariant, tested content envelope, safety margin, composition on each side, and known uncertainty.

## Handoff
Handoff container-local ownership to container-query composition and region sacrifice decisions to priority-collapse design.

## Sibling Boundary
Container queries answer *where* a local threshold is evaluated. This skill answers *why and at what measured failure boundary* a transition is justified. Device-specific viewport strategy remains with the parent.

## delete-the-skill test
Remove this owner and responsive layouts can still change at widths, but there is no faculty requiring those widths to correspond to actual content/task failure. That missing evidence decision is material.