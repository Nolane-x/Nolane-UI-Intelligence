---
name: designing-spatial-ui-distance-scaling
description: Use when XR UI appears at changing physical distances and text, controls, icons, depth cues, and interaction targets must preserve angular legibility and usability without making objects grow unnaturally or violate scene scale.
---

# Designing Spatial UI Distance Scaling

In spatial UI, physical size and perceived angular size are different variables. A panel that works at arm's length can become unreadable at three meters, while naïvely scaling every distant object toward the user destroys world-scale meaning.

## Parent Contract
**Required parent:** `designing-spatial-xr-interfaces`.

The parent owns XR composition. This skill owns how interface geometry and detail adapt to viewing distance while preserving scene semantics.

## Scaling Strategy
Classify elements by scale behavior. Head-locked/system UI may preserve near-constant angular size; world objects may preserve physical scale; labels may use bounded compensating scale; interaction handles may enlarge their hit volume more than their visible geometry. Avoid one global inverse-distance formula.

Define minimum/maximum angular text and target sizes from platform evidence and testing. Distance scaling should have clamps and hysteresis so elements do not pulse while the user moves. At extreme distance, switch information density or representation rather than enlarging a full desktop panel into a billboard.

## Level of Detail
Use semantic LOD. Far state can show icon/status/summary; medium distance can show label and key action; near state can reveal detailed controls. Preserve object identity and affordance across LOD changes. A disappearing destructive status at distance is unacceptable if the user still acts on the object.

## Depth and Occlusion
Scaling can move visual bounds into nearby geometry or cause labels to overlap. Re-run occlusion and collision rules after scale adaptation. Floating labels may need leader lines or decluttering rather than unlimited growth.

## Interaction Coupling
Visible scale and hit target may diverge, but hidden hit-volume expansion must remain bounded so adjacent distant targets do not compete. Coordinate with ray targeting and near/far transitions; do not independently magnetize every control.

## Evidence
Test the same UI at multiple distances, headsets/FOVs if relevant, user text scaling, locomotion through scale thresholds, adjacent targets, and scene objects whose physical scale must remain stable. Measure angular size and selection error.

## Failure Modes
- Entire UI uses inverse-distance scaling and balloons unnaturally.
- Text crosses thresholds with visible size popping.
- Hidden hit areas overlap after far-distance expansion.
- Important status disappears at lower LOD.
- Scale adaptation pushes labels through walls/objects.
- Accessibility text scaling combines with distance scaling without bounds.

## Falsification
Move continuously from near to far through every LOD threshold while selecting adjacent controls. Falsify if users see oscillation/popping, lose essential meaning, or selection ambiguity rises because target volumes overlap.

## Recovery
Introduce category-specific scaling, clamp angular size, add hysteresis, redesign far-state information density, and recalculate occlusion/target spacing. If a world object must preserve physical scale, move the UI label rather than distorting the object.

## Handoff
Placement geometry uses `designing-world-space-panel-placement`; ray target tolerance uses `designing-ray-pointer-interaction`; occlusion uses `designing-occlusion-aware-interface-placement`.

## Output Contract
Return a `spatial-ui-distance-scaling-contract` with `scale_classes[]`, `angular_size_bounds`, `clamps_hysteresis`, `semantic_lod_states[]`, `essential_information_rules`, `hit_volume_policy`, `occlusion_recheck`, `distance_evidence[]`, `falsification_cases[]`, and `recovery_actions[]`.