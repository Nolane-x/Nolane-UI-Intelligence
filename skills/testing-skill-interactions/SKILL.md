---
name: testing-skill-interactions
description: Use when validating NUI itself so prose, semantic mutations, and combinations of individually reasonable skills cannot silently produce harmful emergent behavior.
---

# Testing Skill Interactions

## Parent Contract
**Required parent:** `gating-ui-completion`.

This child strengthens the parent and may not waive parent obligations.

## Decision Boundary
Own causal/interaction evaluation of the skill system: semantic mutation, factorial combinations, ablation, transfer, and decision deltas. Do not claim cross-model benchmark superiority without running those experiments.

## Product Truth
A skill can be beautifully written and behaviorally inert. Multiple correct rules can also compose into a bad attractor: expert+dense, scientific+precise, color+restrained, anti-card, and maximize-context can yield tiny gray mono hairline cyan HUD. Structural parse success cannot detect this.

## Decision Model
Define factorial cases across A, B, C, A+B, A+C, B+C, A+B+C where interactions are plausible. Record baseline and combined outputs and inspect objective deltas. Define semantic mutation cases such as `DO NOT→ALWAYS`, `must→may`, `preserve→discard`, `independent→self`, and `minimum→maximum`; each mutation must map to an evaluator expected to fail. Use ablation to ask whether removing a skill worsens the target behavior. Use transfer cases across visual regimes to prevent a hidden house style. Treat same-model repeated samples as correlated evidence unless independence is established.

## Evidence
Return factorial_cases, semantic_mutations, ablations, transfer cases, evaluator lineage and limitations. Behavioral depth is supported by failures caught and decisions changed, not prose volume.

## Output Contract: `skill-interaction-evidence`
Return the canonical `skill-interaction-evidence` artifact with explicit status, evidence references, unresolved unknowns, and downstream routes. Missing material evidence must remain UNKNOWN/BLOCKED rather than being inferred from confidence.

## Failure Traps
Token length as depth; schema-only mutation tests; one golden prompt; same-model samples called independent; interpreting no regression on one case as universal benefit; forcing a skill to win every style regime.

## V6 Interaction-Causality Protocol
Build a **factorial matrix** for skill pairs/groups suspected of interacting. The matrix includes target skill on/off, neighbor on/off, parent-only controls and, when relevant, a mutated obligation. Record the predicted mechanism before observing outputs.

An **antagonistic interaction** occurs when two individually useful skills combine to create a regression: anti-excess + legibility may become visual timidity; density + scientific restraint may create HUD sameness; reference research + signature design may drift into imitation. A **synergistic interaction** occurs when the combination creates an outcome neither reliably produces alone, such as repository archaeology + adaptation preventing both semantic drift and library collage.

Use **semantic force mutation** rather than cosmetic mutation: MUST→MAY, preserve→discard, independent→self, minimum→maximum, block→warn. Tests must detect changed behavioral force, not just broken JSON.

Record **critic lineage**: model/version, prompt/context overlap, treatment visibility and evaluator independence. Two roles generated in one shared context are correlated evidence, not two independent judges.

### Falsification
If ablation/mutation produces no decision delta across adversarial cases, the skill or clause may not exert causal pressure. If factorial outcomes contradict the hypothesized mechanism, revise the interaction model rather than cherry-picking successful tasks.

### Recovery
Harmful interaction routes to ownership/routing changes, not more prose. No-effect clauses are simplified or removed. Regime-specific effects are scoped rather than promoted to universal rules. Causal claims escalate to `benchmarking-ui-skill-effect` when they require controlled repeated evaluation.
