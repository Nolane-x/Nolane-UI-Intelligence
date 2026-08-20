---
name: designing-render-preview-workflows
description: Own preview rendering inside 3D authoring, including camera, frame, quality, sampling, progressive convergence, region render, comparison, cancellation, stale-state detection, and final-render distinction.
---
# Designing Render Preview Workflows

## Decision ownership

Own the interactive workflow for judging rendered appearance before final output. Decide preview camera/frame, quality tier, sampling/convergence, region/viewport render, progressive state, cancellation, before/after comparison, stale result after scene edits, and relationship to final rendering. This owner does not configure every material/light property.

## Inputs and evidence

Require renderer capabilities, camera, resolution, materials/textures, lighting, color management, sampling/noise controls, render cost, GPU/CPU availability, progressive updates, region support, and final-render pipeline. Identify changes that invalidate all versus part of a preview.

## Procedure

Show exact camera/view, render settings preset, resolution/aspect, and quality mode before start. Progressive renders need clear sampling/progress and should never present an early noisy frame as complete. When scene/material/light/camera changes invalidate a result, mark it stale instead of leaving a convincing old image. Region render should show its bounds and relation to the full frame. Allow compare/snapshot across iterations with settings provenance. Cancel must stop resource use promptly and preserve the last meaningful preview. Final render/export remains a separate deliberate action with its own target/output settings.

## Failure topology

Failures include preview from the wrong camera, stale render displayed after geometry change, noisy early samples treated as final, region bounds forgotten, color-management mismatch between viewport and final, and cancel UI returning while compute continues. Another failure is a high-quality preview freezing the authoring app when a lower-quality interactive mode was available.

## Falsification

Reject if camera/settings cannot be recovered from the preview; if scene changes do not mark invalid results stale; if progressive completion state is unknown; if region preview can be mistaken for full frame; if cancel does not actually stop the job; or if final-output settings are silently inherited from a low-quality preview preset.

## Output contract

Return a `render-preview-workflows-contract` with: camera/frame; resolution/aspect; quality/sampling; progressive state; region render; scene-change invalidation; snapshots/comparison; color-management context; cancellation; performance fallback; and final-render separation. Include one stale-after-material-change scenario.

## Handoffs

Materials, lighting, UV/textures, and camera views supply scene inputs; render/export queues own final jobs; file handling manages output artifacts.