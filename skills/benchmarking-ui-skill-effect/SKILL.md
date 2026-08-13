---
name: benchmarking-ui-skill-effect
description: Use when evaluating whether a Nolane UI skill or group of skills causally improves agent behavior; designs controlled baseline, mutation, ablation, transfer and interaction experiments rather than treating the existence of skill prose or passing structural tests as evidence of effect.
---

# Benchmarking UI Skill Effect

## Parent Contract
**Required parent:** `testing-skill-interactions`.

Receive a target skill/interaction hypothesis, adversarial fixtures, treatment/control definitions, evaluator lineage and measurable outcomes. The parent owns interaction-test obligations; this skill owns controlled causal benchmarking and bounded interpretation.

## Decision Boundary
This faculty owns **causal evidence about the skill system itself**. `testing-skill-interactions` defines semantic mutation/factorial evaluation obligations; this owner turns them into controlled comparisons with explicit hypotheses, baselines, variance handling and bounded conclusions. It does not claim a model-independent quality improvement without experiments.

A skill can be beautifully written, structurally valid, routed correctly, and still have no measurable influence on an agent. Worse, it can improve one dimension while causing a hidden regression: stronger anti-excess guidance may create timid sameness; stronger reference research may increase imitation; richer motion guidance may hurt task clarity. Therefore v6 distinguishes “skill exists” from “skill exerts useful causal pressure.”

## Experimental unit
Define what is being varied: one skill, one clause, one hard gate, a route set, or an interaction between skills. Freeze everything else that can reasonably be held constant: task brief, model/version, tool availability, seed/sampling configuration where supported, source snapshot, implementation environment, evaluation rubric, runtime/browser settings and number of retries.

## Baseline families
Use more than one baseline when the claim is broad:
- **no-skill**: task without the target skill;
- **parent-only**: parent obligations but target child removed;
- **mutated-skill**: force-reversing semantic mutation such as MUST→MAY or preserve→discard;
- **ablation**: target evidence/gate removed while prose remains;
- **alternative-guidance**: a simpler competing instruction tests whether complexity adds real value;
- **full graph**: interaction effects under realistic routing.

Do not compare a carefully optimized treatment against a deliberately incompetent baseline and call the gap causal proof.

## Metrics and evidence
Pre-register task-relevant outcomes. Structural outcomes can include correct routing, evidence completeness, detection of a known regression, source-depth validity, interaction/state coverage, accessibility obligations, or completion-gate behavior. Behavioral/UI outcomes can include reference diversity, distinct candidate count, mechanism specificity, task success, visual-hierarchy findings, cross-screen coherence, rendered defects, accessibility/runtime failures, or blinded preference scores where a legitimate evaluator exists.

Separate **mechanism metrics** from **final-quality metrics**. A source-research skill may directly increase artifact-level evidence; beautiful UI is a downstream hypothesis with many mediators. Do not claim the direct metric proves the final outcome.

## Variance and correlated critics
Same-model repeated runs are not independent human judges. Record lineage: generator model, critic model, prompt/context overlap, and whether evaluators saw treatment labels. Prefer blinded comparison when possible. If only one model/context is available, bound the claim to deterministic/within-run behavior and do not call multiple role prompts independent experts.

Run enough repetitions for the uncertainty of the claim, but never use run count as a substitute for experimental design. Report dispersion and failure cases. A skill that wins on average but catastrophically fails a safety-critical condition may still be unacceptable.

## Causal probes
1. **Ablation:** remove the target skill while preserving neighbors. Does the expected failure become more frequent or the target evidence disappear?
2. **Semantic mutation:** reverse obligation force. Do evaluators/gates detect the mutation, and does behavior move in the predicted direction?
3. **Factorial interaction:** target skill on/off crossed with a neighboring skill on/off. Look for synergy and antagonism.
4. **Transfer:** test tasks from different archetypes/aesthetic regimes/platforms. A skill that only works on dark SaaS dashboards is not universal visual intelligence.
5. **Adversarial target:** include a case deliberately constructed to exploit the skill’s blind spot.
6. **Mechanism removal:** preserve rendered polish but remove the semantic mechanism the skill is intended to create. A good evaluator should notice.
7. **Source perturbation:** change source role/quality/currentness while keeping task constant to see whether research gates respond appropriately.

## Falsification
Before running, state what result would make the skill claim weaker: no detectable decision delta; equal evidence quality without the skill; regressions larger than gains; benefits disappearing under transfer; mutations not detected; critics unable to distinguish treatment; or outcomes attributable to extra context length rather than the skill mechanism.

Where possible, test **minimal causal clauses**. If deleting 80% of a skill leaves behavior unchanged, the excess prose may not be carrying decision pressure. That finding should trigger skill refactoring, not defensive metric selection.

## Output — `ui-skill-effect-benchmark`
Return hypothesis; treatment/controls; exact task/eval fixtures; model/tool/runtime lineage; pre-registered direct and downstream metrics; repetition policy; raw per-run decisions or artifact references; aggregate deltas; interaction effects; regressions; transfer results; mutation sensitivity; evaluator correlation limitations; causal interpretation; falsifiers observed; and bounded conclusion (`SUPPORTED | MIXED | NO_EFFECT | HARMFUL | INCONCLUSIVE`).

## Failure topology
- structural-test substitution for behavioral effect;
- treatment leakage to evaluator;
- no-skill strawman baseline;
- cherry-picked aesthetic regime;
- same-model roleplay counted as independent judges;
- aggregate score hiding catastrophic regressions;
- context-length effect mistaken for decision-quality effect;
- post-hoc metric selection;
- causal language from one anecdotal output;
- benchmark overfitting that produces skill text tailored to fixtures rather than UI work.

## Recovery
If results are inconclusive, improve experimental power or narrow the claim. If the skill has no effect, simplify/rewrite or remove it rather than increasing prose length. If harmful interactions appear, adjust routing/ownership or add a specific conflict gate. If improvement exists only in one regime, mark the skill’s scope instead of presenting it as universal. If evaluation is correlated, seek a different model/human/runtime signal or explicitly bound the conclusion.

## Hard gate
**NUI may not claim that a skill “improves UI quality” merely because it is present, long, routed, or structurally tested. Causal claims require an explicit control/treatment design, falsifiable metrics, lineage/variance accounting, and evidence that the target behavior changes without unacceptable regressions.**

## V6 Causal Skill-Effect Protocol
Use a **controlled-baseline family** rather than one baseline: no skill, parent-only, full routed graph, plausible alternative instruction, and context-matched control where feasible. Measure **skill-ablation delta** by removing the target skill while holding prompt, model lineage, tools, reference set, and evaluation protocol as stable as practical.

Test **mutation sensitivity** with force-changing semantic mutations (`must→may`, remove evidence requirement, invert gate) to prove the evaluator detects weakened behavior rather than surface wording. Run a **transfer-regime test** across materially different aesthetic/domain/platform regimes so a skill is not declared beneficial from one favorable benchmark. Define a **harm-signal threshold** for increased failure, variance, over-constraint, latency/cost, accessibility loss, or aesthetic homogenization.

### Falsification
Seek cases where ablation is equal/better and where the skill induces a consistent harmful interaction with another owner. A positive average cannot hide a harmful subgroup.

### Recovery
Narrow routing, rewrite the harmful decision rule, add interaction constraints, and downgrade the effect verdict to MIXED/INCONCLUSIVE until replicated.
