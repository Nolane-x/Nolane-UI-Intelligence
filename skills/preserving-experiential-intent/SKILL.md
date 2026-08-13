---
name: preserving-experiential-intent
description: Use when a user expresses how the interface should feel, who they should feel like while using it, how large or important the system should seem, or when aesthetic adjectives risk being reduced to implementation proxies.
---

# Preserving Experiential Intent

## Parent Contract
**Required parent:** `ui-contracting`.

This child strengthens the parent and may not waive parent obligations.

## Decision Boundary
Own preservation of affective and identity intent from raw request into an explicit experiential contract. Do not own typography, color, layout, or motion choices; those faculties consume this contract. Operationalization supplements affective intent—it never replaces it.

## Product Truth
A request such as “extremely beautiful”, “awe-inspiring”, or “make me feel like the principal scientist” contains product requirements even when they are not directly measurable. Translating them only into density, hierarchy, restraint, or technical styling destroys information.

## Decision Model
Capture `desired_feelings`, `forbidden_feelings`, `identity_projection`, `emotional_intensity`, `memorability_target`, seven-axis `magnitude_target`, and `source_language`. Then add `operational_proxies` as hypotheses that may help realize those feelings. Preserve conflicts: if the user asks for both extreme density and grandeur, do not silently choose one—route the tension to composition and legibility owners. The original affective terms remain evaluable targets for the adequacy critic.

## Evidence
Evidence is traceability: each high-level feeling must point back to user language or an explicit product brief, and each proxy must point forward to a craft decision without claiming equivalence. A contract that contains proxies but no desired_feelings/forbidden_feelings is incomplete.

## Output Contract: `experiential-intent`
Return the canonical `experiential-intent` artifact with explicit status, evidence references, unresolved unknowns, and downstream routes. Missing material evidence must remain UNKNOWN/BLOCKED rather than being inferred from confidence.

## Failure Traps
Affective Intent Loss; replacing “awe” with “dark + dense”; treating status fantasy as avatar copy; inventing emotions not grounded in the brief; using a numeric score as if beauty were objective; deleting source language after operationalization.
