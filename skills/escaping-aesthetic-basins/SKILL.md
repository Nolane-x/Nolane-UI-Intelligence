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

## V6 Basin Escape Mechanics
Detect the **local-optimum signature**: many small craft improvements, shrinking critic findings, and stable implementation quality while affective fit, distinctiveness, signature depth or reference-frontier position remain flat. This pattern means the system is optimizing the wrong neighborhood.

Use a **plateau detector** across critique rounds. Track which dimensions actually move after each iteration. If spacing/shadow/type polish improves but core adequacy metrics do not, further local iteration has diminishing causal value.

A **direction mutation** changes at least one high-level variable—composition grammar, material regime, typography role split, media system, spatial dramaturgy, signature mechanism, interaction ritual, or visual-energy topology—rather than generating another color variant of the same layout.

Define a **re-divergence threshold** before fatigue sets in: repeated adequacy failure, two or more rounds with no material movement on target invariants, reference frontier consistently dominating the candidate, or evidence that the signature is shallow/borrowed. High implementation sunk cost must not raise this threshold.

Prevent **basin relapse** by recording why the prior attractor failed. New directions must intentionally break at least one causal assumption of the failed basin; otherwise the agent often regenerates the same dark dashboard with different gradients.

### Falsification
Try a constrained radical alternative that preserves product semantics but changes the suspected basin variables. If adequacy does not improve, the basin diagnosis may be wrong and the underlying intent/constraints should be revisited.

### Recovery
`RE_DIVERGE` freezes local polish, returns selected constraints and failure evidence to aesthetic exploration, and requires materially distinct candidates. If repeated re-divergence converges to the same result, inspect routing/reference bias and hidden design-system defaults.
