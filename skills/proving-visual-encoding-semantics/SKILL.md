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
