---
name: designing-world-space-panel-placement
description: Use when XR interfaces place panels, tool palettes, dashboards, or dialogs in 3D space and must choose distance, angle, height, orientation, anchoring, reach, and collision relationships for sustained comfortable use.
---

# Designing World Space Panel Placement

A world-space panel is architecture, not a floating rectangle. Its position changes legibility, neck posture, hand reach, occlusion, privacy, locomotion, and whether the interface remains discoverable after the user moves.

## Parent Contract
**Required parent:** `designing-spatial-xr-interfaces`.

The parent owns the spatial experience. This skill owns placement geometry for planar or panel-like UI in world space, not generic typography or the content hierarchy inside the panel.

## Placement Envelope
Define preferred viewing distance, angular size, vertical band, horizontal eccentricity, orientation relative to head/world, and whether the panel follows, anchors, or can be repositioned. Optimize for comfortable head/eye movement and task duration rather than maximizing field-of-view coverage.

Near panels can become hard to fuse visually and interfere with hand geometry; far panels demand larger angular targets and text. Use actual angular measures and headset optics/platform guidance where available rather than porting desktop pixels into meters.

## Orientation and Following
Decide whether a panel faces the user continuously, faces only on spawn, aligns to a physical surface, or remains world-oriented. Constant billboard behavior can feel artificial and cause unwanted motion; fixed panels can become edge-on or disappear behind users. Provide a bounded reorientation/retrieve action.

Follow-me panels need latency and dead zones so they do not chase every head movement. During reading or interaction, stabilize the panel. Reposition only after meaningful user displacement or explicit summon according to product intent.

## Spatial Competition
Panels compete with scene objects and each other. Avoid stacking translucent interfaces at nearly identical depths, placing controls through walls, or covering safety-critical environment cues. Respect occlusion policy and physical surfaces where passthrough/AR semantics demand it.

## Evidence
Test seated/standing users, different heights, narrow/wide room, prolonged reading, repeated reach, head turn, locomotion, panel behind user, panel near wall, two competing panels, and low-vision text scaling. Measure angular size and reach rather than only screenshots.

## Failure Modes
- Desktop pixel dimensions are mapped directly to arbitrary meters.
- Panel constantly rotates with head micro-movement.
- User walks away and loses essential controls with no summon path.
- Panel spawns inside geometry or beyond comfortable reach.
- Multiple translucent panels overlap at confusing depths.
- Text scaling increases physical size until panel blocks the environment.

## Falsification
Place a task panel for ten minutes of repeated reading/action while users sit, stand, turn, and move. Falsify if sustained posture becomes uncomfortable, controls leave reach/discoverability, or panel tracking motion competes with content reading.

## Recovery
Reposition within a documented comfort envelope, add summon/recenter, stabilize orientation during interaction, and resolve depth/occlusion conflicts. If physical-space constraints are unknown, spawn conservatively and allow deliberate placement.

## Handoff
Distance-dependent scaling uses `designing-spatial-ui-distance-scaling`; occlusion geometry uses `designing-occlusion-aware-interface-placement`; persistent location across sessions uses `designing-spatial-anchor-persistence`.

## Output Contract
Return a `world-space-panel-placement-contract` with `placement_envelope`, `distance_angle_rules`, `height_orientation`, `follow_anchor_mode`, `stabilization_policy`, `summon_retrieve_behavior`, `spatial_conflict_rules`, `comfort_evidence[]`, `falsification_cases[]`, and `recovery_actions[]`.