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

## V6 Deep Intent Preservation Protocol
Treat the user's expressive language as evidence, not garnish. Build an **affective invariant ledger** before translating the brief into operational requirements. Each invariant records the original phrase or observable source, the felt quality it implies, what product experience would satisfy it, what would violate it, and how downstream visual decisions can prove they preserved it. Examples include awe without intimidation, scientific authority without cold sterility, playful mastery without toy-like triviality, or calm density without visual anaesthesia.

Run a **source-language checkpoint** at every lossy boundary: contract creation, task routing, aesthetic direction selection, implementation specification, rendered critique, and release. Compare the current formalized requirement back to the original language. Name **semantic compression loss** explicitly when rich intent has been reduced to generic adjectives such as modern, premium, clean, futuristic, elegant, or delightful. Those adjectives are not accepted substitutes unless their product-specific meaning has been reconstructed.

Maintain two representations simultaneously: verbatim/high-fidelity user language and operational interpretation. The operational layer can evolve as evidence appears; the high-fidelity layer is immutable evidence. When the two disagree, run an **intent contradiction test**: ask whether a reasonable user seeing the current render would recognize the desired identity and emotional consequence without being told the implementation rationale. If not, the operationalization has overridden the brief.

Distinguish emotional target, role identity, sensory quality, symbolic meaning, intensity, avoidance boundaries, and temporal arc. “Powerful” may mean agency, information command, speed, scale, authority, or dramatic visual energy. Do not collapse these into one visual trope. Record ambiguity and route it to the faculty capable of resolving it rather than silently selecting a familiar style.

### Falsification
Try a semantic substitution: replace the preserved experiential language with generic SaaS adjectives while keeping all functional requirements. If the generated direction would be unchanged, the experiential contract is not exerting causal pressure. Try a blind intent test on rendered evidence: remove labels/brand name and ask whether the intended affective identity is still legible. A coherent screen can still falsify the contract if the emotional/identity outcome is absent.

### Recovery
A **recovery trigger** fires when downstream outputs repeatedly satisfy functional obligations while missing an affective invariant, when critics can no longer trace a major aesthetic decision to the source language, or when implementation convenience has silently lowered the requested experience. Recovery may reopen the contract, increase visual ambition, re-diverge aesthetic directions, or remove an accidental constraint. Never repair intent loss only by adding decoration after the structure has already converged.
