---
name: validating-rendered-perception
description: Use when preparing to declare a distinctive, flagship, exceptional, experiential, or visually material UI complete; requires the agent to inspect actual rendered states rather than certify visual quality from source code or prose.
---

# Validating Rendered Perception

## Parent Contract
**Required parent:** `iterating-rendered-visual-design`.

Receive rendered artifacts, target viewports, task-critical states, affective/visual ambition, typography contract, signature contract, motion contract, references, and the latest iteration hypothesis. This skill is evidence collection and falsification, not an image-aesthetic oracle.

## Decision Boundary
Own proof that the agent **looked at what users will perceive**. Reject **screenshot theater**: attaching one hero image, saying “looks polished,” or reporting that the page rendered without overflow is not perceptual evidence.

## Capture Matrix
Build a **capture matrix** over material viewport × state × renderer/environment cells. Cover default and every state capable of changing hierarchy, density, action availability or emotional reading: menus/dialogs, loading, empty, error, selected, validation, streaming, dense data, or responsive navigation as applicable. High-ambition responsive work requires materially different viewport compositions, not one desktop crop.

## Observation Planes
Inspect separately:
- attention order and whether task-critical content wins at the right moment;
- actual resolved typography, fallback, line breaks and raster behavior;
- signature mechanism, subject link and removal cost;
- surface/material roles, boundary density, depth and quiet regions;
- responsive recomposition and information loss;
- image/icon/data encoding truth;
- temporal staging where motion changes state or continuity;
- reference distance on named dimensions.

Record observations against artifact IDs. “Source CSS says Inter” is weaker than the browser resolving Inter. A signature described in a design plan but visually invisible has not survived implementation.

## Temporal Evidence
When motion is material, capture before/transition/settled states plus semantic purpose and reduced-motion equivalent. Timeline or presence mechanics can coordinate motion; they do not themselves prove that the choreography clarifies change.

## Calibrated Regression
Pixel comparison is optional **calibrated pixel evidence**. When used, pin renderer/environment, baseline/candidate, delta, threshold and rationale. Anti-aliasing and font-rendering variance can create harmless pixel noise, while a low pixel delta can still hide a disastrous hierarchy change. Pixel math is a regression instrument, never a beauty score.

## Critique Loop
For high ambition, compare with task-relevant references on explicit axes and record at least one observed weakness, intervention and re-observed result before claiming adequacy. If the direction itself is weak, return `RE_DIVERGE` rather than polishing local details forever.

## Output — `rendered-perception-evidence`
Return `capture_matrix[]`, `required_states[]`, `observations`, optional `temporal_evidence`, optional `pixel_diff`, `reference_comparison`, `critique_cycle`, `unobserved_cells[]`, and `decision`.

## Falsification
Inspect the UI at a target viewport/state not used during implementation. Disable the intended display font. Trigger reduced motion. Inflate content. If the quality claim collapses under any expected condition, the rendered thesis was conditional and must be narrowed or repaired.

## Recovery
Add the missing capture cell, fix the observed perceptual failure, and re-observe the same cell plus adjacent states. For renderer noise, calibrate a justified threshold rather than weakening all visual tests. For a weak aesthetic thesis, return to divergence/reference work.

## Hard gate
**High-ambition visual completion is blocked unless a multi-cell rendered capture matrix, actual type/signature/material observations, reference comparison, and a traceable critique/fix cycle support the claim; screenshot existence and clean runtime alone cannot pass.**
