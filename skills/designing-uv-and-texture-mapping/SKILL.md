---
name: designing-uv-and-texture-mapping
description: Own texture-coordinate authoring across seams, unwrap, islands, packing, texel density, image linkage, transforms, overlap, UDIM/tiles, and model-to-texture correspondence.
---
# Designing UV and Texture Mapping

## Decision ownership

Own the mapping between model surfaces and 2D texture space. Decide seam marking, unwrap mode, island selection/editing, packing, scale/texel density, overlap policy, image/tile linkage, transforms, and correspondence between UV and 3D selection. This owner does not paint textures or define shader materials generally.

## Inputs and evidence

Require mesh topology, supported mapping methods, texture assets/resolution, UV sets/channels, tile/UDIM support, texel-density goals, overlap allowances, material slots, and export target. Identify mirrored/reused UVs that are intentional versus collisions.

## Procedure

Keep 3D and UV selections linked with clear scope. Seam changes should preview their effect on islands where possible. Unwrap actions need method/settings and preserve prior UV set until commit/undo. Display image/tile identity, UV bounds, overlaps, flipped/mirrored state, and texel density. Packing must state whether island rotation/scaling is allowed and what margin units mean. Multiple UV sets require explicit active/render set. Missing texture images should not make UV geometry disappear; retain mapping context and provide relink.

## Failure topology

Failures include editing the wrong UV set, packing that changes intended relative scale, overlap warnings flagging intentional mirrors with no exception, texture image missing and UV view blank, seam changes creating tiny fragmented islands unnoticed, and 3D/UV selection desynchronization. Another failure is margin interpreted in pixels for one resolution and normalized units for another without explanation.

## Falsification

Reject if active UV set cannot be identified; if pack operation can rescale/rotate without preview/settings; if overlap cannot distinguish intentional versus unintended; if missing image destroys coordinate visibility; if UV and 3D selection refer to different faces without cue; or if texel-density/margin units are ambiguous.

## Output contract

Return a `uv-and-texture-mapping-contract` with: UV set identity; seam/unwrap behavior; island selection; 3D correspondence; pack settings; rotation/scale policy; margin units; overlap classification; texel density; texture/tile linkage; missing-asset recovery; and export set. Include one intentional-overlap case.

## Handoffs

Material assignment supplies texture/material context, file/media relink handles assets, mesh selection supplies topology, and manufacturing/export decides which mapping data survives target formats.