---
name: designing-snapping-and-guides
description: Use when direct manipulation should align objects to grids, edges, centers, baselines, time points or semantic guides and the system must balance precision, discoverability, priority and override.
---

# Designing Snapping and Guides

## Parent Contract
**Required parent:** `designing-pointer-touch-pen-input`.

This specialist owns snap target discovery and alignment feedback. Post-release inertia is owned by `designing-drag-inertia-and-snap`; layout alignment rules are separate.

## Decision Model
Create a taxonomy of guides: fixed grid, rulers, margins, object edges/centers, text baselines, distribution gaps, timeline frames, anchors or domain-specific constraints. Give each a semantic priority; nearest pixel distance alone is not sufficient when an important baseline competes with an incidental edge.

Snap tolerance should be predictable across zoom. Human acquisition occurs in screen space, while final coordinates exist in world/domain space. Use screen-space activation with exact domain-space resolution where appropriate. Add hysteresis so an active snap remains stable until the pointer moves meaningfully away, preventing jitter among neighboring candidates.

Guides are explanations, not decoration. Show the relation being enforced—aligned centers, equal gap, baseline, grid coordinate—and hide obsolete guides promptly. When multiple constraints are active, avoid a visual explosion; prioritize the constraints controlling final position.

Provide temporary override and explicit enable/disable. Precision experts need to bypass snapping without turning it off globally, but modifier conventions should have visible alternatives in settings/toolbars.

## Failure Topology
- Object jumps to a weak nearby edge instead of the intended major guide.
- Snap tolerance changes wildly with zoom.
- Guides appear after the snap, so users cannot anticipate capture.
- Equal-spacing guides claim equality based on screen pixels while world units differ.
- Two targets alternate every frame and the object vibrates.
- Snapping cannot be temporarily bypassed for fine placement.

## Falsification and Recovery
Test competing targets, zoom extremes, high-density scenes, rotated objects, baseline/distribution guides, modifier override, keyboard nudge and drag reversal. Log active target and resolved coordinate; unstable target switching under nearly fixed pointer input fails.

Recover by ranking semantics, adding hysteresis, limiting displayed guides, separating activation tolerance from final coordinate and exposing override/state.

## Output Contract
Return `snapping-guides-contract` with target taxonomy, semantic priority, screen/world tolerance, hysteresis, guide visualization, override controls, keyboard/numeric parity and competition tests.