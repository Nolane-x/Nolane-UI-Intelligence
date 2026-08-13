---
name: escaping-aesthetic-basins
description: Use when working during rendered iteration to decide whether to keep locally refining the current direction or abandon/re-diverge from a visually inadequate basin.
---

# Escaping Aesthetic Basins

## Parent Contract
**Required parent:** `iterating-rendered-visual-design`.

This child strengthens the parent and may not waive parent obligations.

## Decision Boundary
Own the REFINE versus RE_DIVERGE decision. Do not design the replacement direction itself; aesthetic exploration does that after re-divergence.

## Product Truth
Local hill-climbing can make the wrong aesthetic 5% better indefinitely. Metadata contrast, border alignment, and animation timing can all improve while the entire thesis remains too timid, generic, cramped, or emotionally wrong.

## Decision Model
Compare current evidence to affective targets, distinctiveness targets, signature depth, adequacy findings, and the reference frontier. Return `RE_DIVERGE` when affective fit remains below target, distinctiveness remains below target, the candidate repeatedly loses reference comparison, signature depth fails at required ambition, or adequacy judges the thesis wrong. Only return local refinement when the basin itself remains viable. Preserve iteration history so repeated losses cannot be forgotten.

## Evidence
Output decision, triggering reasons, comparison history, retained strengths, discarded assumptions, and the axes aesthetic exploration must reopen. Reference frontier means accepted external mechanisms/quality examples, not a style-copy target.

## Output Contract: `aesthetic-basin-decision`
Return the canonical `aesthetic-basin-decision` artifact with explicit status, evidence references, unresolved unknowns, and downstream routes. Missing material evidence must remain UNKNOWN/BLOCKED rather than being inferred from confidence.

## Failure Traps
Polishing a wrong basin; re-diverging after every minor defect; comparing only current vs prior self; keeping a direction because implementation cost is sunk; importing reference trade dress rather than mechanisms.
