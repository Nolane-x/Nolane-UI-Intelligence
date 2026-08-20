---
name: designing-lighting-authoring-controls
description: Own 3D lighting setup across light types, position/orientation, intensity/units, color/temperature, environment light, shadows, grouping, preview quality, and render-context visibility.
---
# Designing Lighting Authoring Controls

## Decision ownership

Own creation and adjustment of scene illumination for visualization/rendering. Decide light entity types, spatial controls, photometric/relative intensity, color or temperature, shadow state, environment/HDR lighting, grouping, solo/mute, preview fidelity, and relationship to viewport versus final render. It does not define renderer algorithms.

## Inputs and evidence

Require supported light types, unit model, renderer capabilities, environment maps, color management, shadow settings, real-time preview budget, camera/render context, and animation support. Identify whether physically meaningful units are available or values are renderer-relative.

## Procedure

Expose light type and direction/shape in the viewport with manipulators that do not obscure geometry. Label intensity units honestly; do not use "lux" or "lumens" when the renderer value is unitless. Provide color/temperature controls with current transform/color-space context. Environment lighting should show source and rotation. Solo/mute/group controls help diagnose contribution. Preview mode must disclose quality differences from final rendering and avoid presenting noisy/incomplete convergence as final. Keep editor helper visibility separate from whether a light renders.

## Failure topology

Failures include lights invisible in scene hierarchy, ambiguous intensity units, viewport preview differing radically from final with no cue, environment rotation hidden, helper visibility accidentally disabling render contribution, and color management making selected values appear inconsistent. Another failure is performance collapse from updating expensive global illumination on every drag without a preview fallback.

## Falsification

Reject if a user cannot locate a light spatially; if intensity unit/scale is misleading; if preview quality/mode is unknown; if mute/helper/render states are conflated; if environment source/rotation cannot be recovered; or if interactive adjustment exceeds latency budget with no reduced-quality mode.

## Output contract

Return a `lighting-authoring-controls-contract` with: light types; spatial manipulation; intensity units; color/temperature; environment source/rotation; shadows; group/solo/mute; helper-versus-render visibility; viewport/final preview distinction; quality/performance fallback; and saved parameters. Include one unitless-renderer case.

## Handoffs

Render preview consumes lighting, material assignment affects response, camera management defines view context, and visual color management/asset sourcing may govern environment resources.