---
name: orchestrating-creative-toolchains
description: Use when a material visual asset requires coordinated generation, vector or raster editing, 3D, animation, design-canvas work, browser rendering, optimization, or verification across more than one production tool
---

# Orchestrating Creative Toolchains

## Parent Contract
**Required parent:** `orchestrating-implementation-authorities`.

The parent separates implementation authorities by layer. This owner specializes that rule for visual production pipelines. A tool can be excellent at one production stage without owning product truth, visual intent, rights interpretation, accessibility, or release completion.

## Decision Boundary
Own the ordered production route from an approved asset brief to a verified product artifact. Do not decide whether imagery belongs, what the subject means, or whether a source asset is reusable; those decisions belong to media-mapping, domain-native authoring, and provenance owners. Output a `creative-toolchain-plan`.

## Stage Authority Map
Create a **stage authority map** before selecting brands or tools. Separate discovery, reuse, generation, modeling, vector construction, raster editing, layout composition, motion, rendering, optimization, export, and product verification. For each stage state the input contract, operation, expected output, evidence owner, and what the tool is explicitly *not* allowed to decide.

Use a **cross-tool handoff contract** whenever one artifact crosses applications. Preserve dimensions, coordinate systems, color profile, alpha behavior, font/text treatment, naming, animation timing, data binding, source references, and editability expectations. A beautiful intermediate render that cannot survive the next stage is not a successful handoff.

Maintain an **artifact lineage chain** from brief → source/reference → intermediate files → transformations → optimized derivative → integrated UI asset. Lineage records are about reproducibility and provenance, not bureaucracy: if the final asset is wrong, the team must be able to locate which stage introduced the error.

Define a **tool fallback route** for every material stage. If a connected design canvas is read-only, if a generator cannot preserve factual geometry, if a 3D runtime is too expensive, or if an animation library is unavailable, degrade to a controllable alternative without changing semantic intent. Do not fabricate tool capability.

Finish with **render-stage verification** inside the real target medium. A Figma frame, Blender render, image-generation output, or isolated SVG is intermediate evidence. Verify the actual browser/app surface, responsive states, interaction overlays, loading behavior, reduced-motion behavior where applicable, and final asset compression.

## Tool Selection Heuristics
Choose the minimum tool chain that preserves the required control. Prefer web-native SVG/CSS for lightweight semantic vectors; vector editors for authored illustration; raster tools or image models for photographic/painted assets; Blender/3D engines for genuinely spatial subject matter; data-viz libraries for truthful encoded data; animation engines only when temporal choreography is material. More tools increase handoff and provenance risk, so every additional stage must earn its cost.

## Decision Model
Lock asset brief → decompose production stages → assign stage authority → choose the minimum capable tool per stage → define handoff contracts and fallbacks → preserve lineage → integrate → verify in the target runtime.

## Evidence
Require stage list, selected tool and current capability evidence, input/output contract, handoff checks, lineage identifiers, fallback, performance/export assumptions, and final runtime verification reference.

## Output Contract
Emit `creative-toolchain-plan` with goal, ordered stages, tool authority, inputs, outputs, handoff contract, lineage link, fallback, human-or-agent check, and final integration verification. Generated assets must include a render/integration stage before completion.

## Failure Traps
Tool chosen because it is fashionable; generator output treated as product truth; design-canvas preview treated as runtime proof; duplicated transformations lose provenance; color/profile changes between tools; 3D complexity exceeds target budget; motion tool adds choreography without semantic purpose; no editable source remains.

## Falsification
Remove one tool from the chain or make it read-only. If the plan cannot name the lost capability and a bounded fallback, the routing was tool-dependent rather than intent-preserving. Replace a generated intermediate with a source-correct but visually different asset; product semantics should survive even though production mechanics change.

## Recovery
Return to the last lineage checkpoint whose semantics and provenance are known-good, discard downstream derivatives that cannot be explained, choose the smallest controllable replacement stage, rerun handoff checks, and re-verify the final asset inside the product rather than polishing a broken intermediate.
