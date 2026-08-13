---
name: directing-visual-energy
description: Use when restraint, dark mode, neutral palettes, or anti-excess guidance may suppress the emotional energy required by the experiential intent.
---

# Directing Visual Energy

## Parent Contract
**Required parent:** `crafting-color`.

This child strengthens the parent and may not waive parent obligations.

## Decision Boundary
Own expressive-energy requirements and evidence, not specific palette tokens. Inspect luminance range, chroma mass, focal color mass, warm/cool tension where relevant, depth contrast, and material variation.

## Product Truth
A chroma ceiling without an expressive floor can collapse into visual starvation. Conversely, high awe does not automatically require saturation. Energy is the perceptual range and tension/release needed for the target, not ‘more color’.

## Decision Model
Derive an energy posture from experiential intent. For high beauty/awe/presence, ask whether restraint is actively supporting tension and focus or merely deleting expressive mechanisms. Establish target relationships such as quiet field vs focal mass, low-chroma structure vs meaningful spectral event, matte surface vs luminous evidence layer, or warm/cool opposition. Evaluate luminance_range, chroma_mass, focal_color_mass, depth_contrast, material_variation, and optional warm_cool_tension. Permit monochrome when contrast, material, typography, image/diagram behavior, and spatial rhythm provide the required force.

## Evidence
Return measured/observed visual-energy evidence tied to the experiential target and explain why the chosen range is sufficient. Do not output a universal beauty number.

## Output Contract: `visual-energy-contract`
Return the canonical `visual-energy-contract` artifact with explicit status, evidence references, unresolved unknowns, and downstream routes. Missing material evidence must remain UNKNOWN/BLOCKED rather than being inferred from confidence.

## Failure Traps
High ambition⇒neon; restraint⇒nearly black everything; treating low chroma as automatically sophisticated; measuring saturation without area; adding random accent colors to satisfy a metric; ignoring material/luminance energy in monochrome interfaces.

## V6 Visual Energy Topology
Map energy spatially rather than describing a palette. The **energy topology** identifies focal peaks, secondary pulses, quiet fields, directional flows and transitions over the screen/product journey. Energy can come from scale, contrast, color, motion, density, image detail, depth, shape tension and information velocity; chroma is only one channel.

Build a **chroma mass map**: where saturated color occupies area, where it is concentrated into small signals, and whether saturation has semantic or emotional purpose. Track a **quiet-field ratio** so expressive peaks have perceptual room. A uniformly muted interface can be lifeless; a uniformly saturated interface can be exhausting.

Inspect **luminance excursion** from the dominant field to the strongest focal points, including dark/light themes and HDR-like media where relevant. Large luminous contrast can create magnitude and direction; tiny bright labels on dark chrome can create glare without hierarchy.

Define desired tensions: warm/cool, soft/hard, organic/geometric, matte/luminous, still/kinetic. An **energy contradiction** occurs when these tensions communicate the opposite of the experiential contract—for example a calm medical workflow using constant pulsing alerts, or an awe-driven scientific explorer with uniformly timid gray surfaces.

Energy must be state-sensitive. Loading, success, danger, focus, selection, live update and completion do not all deserve the same intensity. Motion energy should decay when the user is reading or making a high-stakes choice.

### Falsification
Blur/squint the render and observe whether intended focal peaks remain. Remove color while preserving hierarchy; if all meaning collapses, color may be overburdened. Remove motion; if the design becomes emotionally inert despite a high experiential ambition, confirm whether motion was carrying legitimate temporal meaning or only spectacle.

### Recovery
When energy is too low, deepen one product-specific peak before globally increasing contrast/chroma. When energy is too high, create quiet fields and hierarchy rather than desaturating everything. If energy contradiction persists across several craft layers, re-open the aesthetic thesis.
