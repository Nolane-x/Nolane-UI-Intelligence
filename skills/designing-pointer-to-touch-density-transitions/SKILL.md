---
name: designing-pointer-to-touch-density-transitions
description: Use when the same interface can move between precise pointer input and coarse touch input and control density, target geometry, spacing, and adjacent-action risk must adapt without changing task semantics.
---

# Designing Pointer-to-Touch Density Transitions

## Precision Changes the Error Model
A pointer can acquire small targets with high precision; a finger introduces occlusion, coarse targeting, and accidental-neighbor risk. This skill owns the transition in density and target geometry when input capability changes, including hybrid devices that can switch without viewport change.

## Parent Contract
**Required parent:** `adapting-responsive-layouts`.

The parent owns broad adaptation. This specialist treats input precision as an independent responsive signal rather than assuming small screens are touch and large screens are mouse.

## Capability State
Model `fine pointer`, `coarse pointer`, `hybrid`, and `unknown/recent-input` states separately. Decide whether adaptation follows device capability, current input, or a stable user setting; avoid oscillating layout after every incidental mouse/touch event. Touch density must preserve information hierarchy while increasing acquisition safety.

Target enlargement may use padding/hit areas without visually inflating every control. Adjacent destructive and benign actions require sufficient separation. Dense data interfaces may offer a deliberate compact mode for expert pointer users while keeping touch-safe interaction when coarse input is active.

## Evidence
Evidence includes physical/coarse-pointer testing, target hit-box inspection, hybrid laptop/tablet switching, zoom/text scaling, edge and adjacent target acquisition, and representative high-density workflows. Record both visual dimensions and actual interactive hit regions.

## Failure Modes
Failure includes hover-sized icon buttons on touch, invisible hit regions overlapping neighbors, layout jumping after a single accidental touch, dense expert mode automatically forced on a large touch display, and increased spacing that destroys critical data comparison without providing an alternative.

## Falsification
Falsification performs repeated adjacent-target tasks with touch, switches from pointer to touch at fixed viewport, rotates or docks a hybrid device, and verifies target geometry and task state. High mis-hit risk or unstable oscillation falsifies the transition policy.

## Recovery
Recovery separates capability detection from current-input hints, sets stable mode-selection rules, enlarges true hit targets, and preserves dense comparison through alternate navigation or zoom rather than shrinking touch targets below safe acquisition.

## Output
Output: `pointer-to-touch-density-transitions-contract` containing capability states, density policy, target geometry, stability/hysteresis, high-risk adjacency rules, and acquisition evidence.

## Handoff
Handoff hover-only semantics to hover-to-nonhover affordance transitions and platform gesture behavior to input specialists.

## Sibling Boundary and delete-the-skill
Viewport layout can be identical while input precision changes. Without this skill, no owner decides how density and target-risk adapt across pointer/touch modality, so the delete-the-skill test passes.