---
name: proving-visual-encoding-semantics
description: Use when handling any non-decorative visualization, scientific diagram, topology, map, graph, animated data field, or visual system where graphical channels could imply relationships.
---

# Proving Visual Encoding Semantics

## Parent Contract
**Required parent:** `designing-data-visualization`.

This child strengthens the parent and may not waive parent obligations.

## Decision Boundary
Own the provenance table that maps every visual channel to meaning or explicitly marks it decorative. Do not select statistical encodings or alter source data; designing-data-visualization remains responsible for analytical truth.

## Product Truth
A visualization can look scientific while lying by implication. If position_x, position_y, radius, edge, opacity, color, motion, texture, or angle has no semantic mapping, viewers may infer structure that does not exist.

## Decision Model
For each channel record `channel`, `meaning`, source field/relationship when applicable, transformation/scale, uncertainty treatment, interaction semantics, and `decorative`. Non-decorative channels must have meaning. Decorative channels must not be described in copy or legends as data-bearing. Coordinate multiple views through a shared visualization grammar only after data semantics and encoding truth are proven. Motion used as a channel must declare whether it encodes time, propagation, state change, uncertainty, attention, or is ambient decoration.

## Evidence
Return a complete encoding-provenance-table and a visualization grammar note. Unsupported channels are removed or declared decorative before completion.

## Output Contract: `encoding-provenance-table`
Return the canonical `encoding-provenance-table` artifact with explicit status, evidence references, unresolved unknowns, and downstream routes. Missing material evidence must remain UNKNOWN/BLOCKED rather than being inferred from confidence.

## Failure Traps
Hard-coded orbit angle implying relation; line edges with no dependency meaning; opacity used atmospherically but interpreted as confidence; decorative animation labeled live data; beautiful art direction overriding analytical truth.

## V6 Encoding Truth and Perception Protocol
Construct a **channel truth table** for every material visual channel: x/y position, length, area, angle, curvature, color hue, luminance, saturation, opacity, texture, stroke, radius, depth, motion, particle behavior, edge topology, glyph and annotation. Each row states whether the channel is semantic, redundant, orienting or decorative; what variable it represents; provenance; scale/domain; missing/unknown behavior; and interaction affordance.

Respect **perceptual ordering**. Quantitative values require channels whose perceptual order matches the data relationship; categorical variables must not imply false magnitude; diverging values need a meaningful center; area/volume exaggeration requires explicit justification. Art direction comes after truthful mapping.

Use **decorative quarantine**. A decorative channel may be expressive, but it must be prevented from accidentally tracking data in a way users could interpret as meaning. Procedural particles, glow, jitter or node placement that visually correlate with values without declared semantics are especially dangerous in scientific/financial interfaces.

Define **uncertainty encoding** explicitly: confidence intervals, ranges, missingness, model uncertainty, estimated values, stale data, imputation and forecast status. Uncertainty cannot be hidden behind a tooltip if it materially changes decisions.

Perform a **legend dependency audit**. Ask whether users can recover meaning through direct labels, spatial structure and consistent semantics, or whether every interpretation requires memorizing a legend. Excessive legend dependence increases cognitive load and often signals too many weak encodings.

### Falsification
Randomize the data while preserving visual art direction; any visual feature that stays apparently meaningful without data provenance may be decorative masquerading as evidence. Swap two variable mappings; if critics/users cannot detect the semantic contradiction, the encoding lacks interpretable force.

### Recovery
When an expressive visual conflicts with truthful encoding, preserve data truth and move expression into non-semantic channels or framing. If a chart requires too many legends/encodings, reduce variables or use coordinated views rather than visual overloading.
