---
name: designing-occlusion-aware-interface-placement
description: Use when spatial UI can be blocked by scene geometry, hands, people, physical surfaces, passthrough content, or other interface layers and must choose visibility, depth, relocation, clipping, and interaction rules intentionally.
---

# Designing Occlusion Aware Interface Placement

Occlusion is part of spatial semantics. Sometimes an object should hide behind a wall because it belongs in the world; sometimes a safety alert or system menu must remain legible despite scene geometry. The design must declare which rule applies.

## Parent Contract
**Required parent:** `designing-spatial-xr-interfaces`.

The parent owns XR scene structure. This skill owns how interface elements respond to occluders and depth conflicts across VR, AR, and passthrough contexts.

## Occlusion Classes
Classify elements as world-occluded, environment-respecting overlay, always-visible system layer, soft-occlusion label, or temporarily elevated alert according to meaning. Avoid blanket “render UI on top” because it destroys depth cues and can make distant controls appear reachable through physical surfaces.

Determine relevant occluders: scene mesh, depth sensor, physical wall estimate, virtual object, user's hands, avatars, other panels, and transient effects. Different sources have different confidence. If environment depth is uncertain, avoid precise claims that a panel is safely in front of a real obstacle.

## Visibility Recovery
When a required control becomes occluded, choose among edge indicator, leader line, reposition, summon, fade occluder, context-aware ghosting, or temporary foreground treatment. The recovery should preserve the spatial relationship when that relationship matters.

Do not relocate anchored content automatically just because the user's hand briefly passes in front. Use duration, occluder type, and criticality to avoid interface jitter. Likewise, do not allow a persistent physical obstacle to hide the only exit or safety control.

## Interaction Semantics
Visual occlusion and hit testing must agree. If a wall visually blocks a panel, a ray should not normally activate the panel through the wall unless the product explicitly supports X-ray interaction. Transparent visuals can still be interaction blockers; document the rule.

## Evidence
Test walls, furniture/scene mesh, hand occlusion, moving avatar, two overlapping panels, passthrough depth noise, critical alert behind object, and user walking around an occluder. Compare rendered depth with hit-test results.

## Failure Modes
- UI is always on top and destroys depth ordering.
- Hidden control remains ray-clickable through a wall.
- Panel jumps every time a hand briefly crosses it.
- Essential exit control can be permanently occluded.
- Uncertain environment mesh causes rapid pop-through.
- Transparent layer visually reveals a control but blocks interaction without feedback.

## Falsification
Place an interactive panel behind a solid virtual/physical occluder, then test visual and ray behavior from several angles. Falsify if visible depth and interaction priority disagree or if required controls can become unrecoverably hidden.

## Recovery
Align render and hit-test layers, classify critical elements, add bounded reveal/summon behavior, and filter low-confidence environment depth. If real-world geometry confidence is insufficient, avoid auto-placement near hazards.

## Handoff
Panel positioning uses `designing-world-space-panel-placement`; ray interaction uses `designing-ray-pointer-interaction`; safety-critical physical boundary rules use `designing-xr-safety-boundaries`.

## Output Contract
Return an `occlusion-aware-interface-placement-contract` with `occlusion_classes[]`, `occluder_sources[]`, `confidence_policy`, `visibility_recovery`, `relocation_thresholds`, `render_hit_test_alignment`, `critical_control_rules`, `evidence_cases[]`, `falsification_cases[]`, and `recovery_actions[]`.