---
name: designing-spatial-xr-interfaces
description: Use when designing augmented, mixed, virtual, or spatial interfaces with windows, volumes, immersive scenes, world anchoring, depth, field of view, embodied scale, locomotion, or gaze/hand interaction.
---

# Designing Spatial and XR Interfaces

## Overview
Spatial UI adds depth, embodiment, comfort, and environmental context; it does not justify placing ordinary 2D panels everywhere. Choose spatial representation only when it improves understanding, manipulation, presence, or task continuity.

## Parent Contract
**Required parent:** `routing-ui-work`.

Require headset/platform, immersion level, physical environment, seated/standing/moving posture, locomotion, input modalities, shared-space needs, passthrough/privacy, and comfort/accessibility constraints. Coordinate with `designing-gaze-hand-spatial-input`.

## Decision Model
Choose among window, volumetric object, bounded immersive region, and full immersive space based on task semantics. Text-heavy configuration often belongs in stable windows; 3D models benefit from volumes; simulations or spatial training may justify immersion. Avoid spatial novelty where depth provides no information.

Define a comfortable field of view and depth range for frequent content. Large angular movement, extreme near/far placement, head-locked overlays, forced camera motion, and persistent peripheral stimuli can create fatigue or discomfort. Keep critical controls stable relative to the appropriate frame: window, object, world, or user — explicitly choose rather than mix accidentally.

Scale is semantic. Real-world size may matter for training or products; exaggerated scale can improve manipulation but must not confuse units. Occlusion and depth ordering need clear ownership. Spatial audio/haptics can reinforce direction but require redundant cues.

Design transitions between levels of immersion. Users need orientation, easy exit, preserved task state, and awareness of physical surroundings where the platform supports it. Locomotion and camera movement require reduced-motion/comfort alternatives.

## Evidence
Test actual headset field of view, gaze/hand targeting, seated/standing reach, occlusion, comfort over time, recentering, environment changes, reduced-motion settings, accessibility inputs, and transitions into/out of immersion. Flat screenshots cannot validate spatial comfort or target depth.

## Output Contract
Return a `spatial-xr-contract` with `representation_by_content[]`, `coordinate_frames[]`, `field_of_view_budget`, `depth_and_scale_rules`, `occlusion_rules`, `anchoring`, `locomotion_and_camera`, `immersion_transitions`, `comfort_alternatives[]`, `environment_privacy`, and `headset_tests[]`.

## Failure Traps
- Wall of floating settings panels around the user.
- Head-locked UI that follows every movement and causes discomfort.
- Tiny controls at distant depth.
- Forced camera animation with no comfort alternative.
- Gaze treated as commit rather than attention.
- World-anchored content with no recenter/recovery path.
- Claiming spatial quality from a 2D browser preview.

Spatial design is strongest when depth becomes part of the task model, not a decorative dimension.