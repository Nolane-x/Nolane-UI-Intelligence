---
name: validating-visual-asset-integration
description: Use when material imagery, illustration, diagram, video, animation, map, or 3D media must be evaluated inside real responsive product states
---

# Validating Visual Asset Integration

## Parent Contract
**Required parent:** `validating-rendered-perception`.

## Decision Boundary
Own whether a visual asset works inside the product composition. A strong standalone asset is intermediate evidence. Output `visual-asset-integration-evidence`.

## Integration Evidence
Collect **responsive crop evidence** at materially different layouts: focal subject, safe area, art-direction variant, object position, overlay region, and content that leaves the frame. A composition that succeeds only at one width is incomplete.

Collect **overlay contrast evidence** from rendered states where text, controls, captions, focus indicators, or badges actually meet the image or video. Variable imagery must be observed in representative difficult frames rather than reduced to one average background value.

Set a **media performance budget** for encoded size, dimensions, format, loading strategy, decode/render cost, poster or fallback, and the asset’s effect on the first useful state. Richness that delays the primary task must be reconsidered or optimized.

Provide an **accessible equivalent** based on the media’s semantic job. Informative imagery needs useful text or explanation; complex visual information may need structured data or a longer description; temporal media needs the applicable alternative and controls; decorative media remains decorative.

Run a **post-integration critique loop**: render at least two material states, record a concrete visual or usability observation, make the required correction, then re-render the changed state. Include loading or fallback presentation when it materially changes composition.

## Decision Model
Bind media to semantic job → render states → inspect crop and overlays → inspect loading/performance → inspect accessible equivalent → critique → correct → re-render → PASS or BLOCKED.

## Evidence
Require asset ids, rendered states, crop observations, overlay observations, performance evidence, accessible equivalent, one observed finding, the correction, and the state where the correction was re-observed.

## Output Contract
Emit `visual-asset-integration-evidence` with assets, rendered states, checks, findings, corrections, and decision. Material media requires at least two materially different rendered states.

## Failure Traps
Desktop-only crop; readable text over only one frame; oversized hero media; missing fallback composition; accessibility copy that does not communicate the media job; critique that reports a defect without re-observing the correction.

## Falsification
Change viewport, content length, theme, loading state, or focal crop. The integration assessment must respond to those changes. If every state receives the same verdict without observation, the evidence is too abstract.

## Recovery
Repair the highest-impact composition or delivery problem first, select a more controllable crop or format when necessary, restore the accessible equivalent, and repeat the rendered critique loop before release.
