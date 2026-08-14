# NUI V10 Empirical Run Protocol

This document defines how a claim that **NUI changes model behavior** may be tested. It is deliberately stricter than ordinary UI completion. A product artifact can be complete while NUI efficacy remains unknown, and a green repository CI can validate the evaluation framework without proving that NUI improves any model.

## 1. Three evidence classes that must never be collapsed

### Structural evidence
Structural evidence proves repository facts: validators execute, schemas parse, task IDs cross-link, hidden rubrics are separate, mutations have targets, statistics reject unpaired samples, and release logic prevents unsupported promotion. Structural evidence can support only `STRUCTURAL_ONLY` claims.

### Artifact evidence
Artifact evidence concerns a particular generated product: screenshots, runtime traces, capability ledgers, accessibility observations, state matrices, interaction tests, visual-regression records, and critique/re-render cycles. This can prove bounded facts about that artifact. It does **not** prove that NUI caused the quality.

### Empirical efficacy evidence
Efficacy evidence compares matched generation conditions and asks whether NUI changes outcomes. It requires model/runtime provenance, matched baseline and NUI conditions, treatment blindness at judgment time, dimension-level results, targeted ablations, uncertainty reporting, and the claim gate. Only this class can support `EMPIRICAL_LOCAL` or `EMPIRICAL_TRANSFER`.

The most important V10 invariant is therefore:

`artifact quality ≠ NUI efficacy`

A beautiful NUI-generated page is an existence example. It is not a causal comparison.

## 2. Unit of comparison

A matched experimental unit is keyed by:

`experiment × task × model family × model name/snapshot × runtime × seed/replicate × temperature × tool budget`

Only treatment is allowed to differ inside the pair or treatment set. If the NUI run has browser access, more execution steps, a different model snapshot, or a larger external-tool budget than baseline, the comparison is confounded unless that difference is itself the declared treatment.

Tool context contributed by NUI is expected to change treatment context size; it must be measured rather than hidden. Report input/output token counts and cost when the provider exposes them.

## 3. Required conditions

A minimal efficacy experiment contains:

- `baseline` — same generation model/runtime without NUI;
- `nui_full` — routed canonical NUI condition;
- at least one `nui_ablation:<plane>` that removes the mechanism attributed by the claim.

Semantic mutation conditions are strongly recommended because an ablation can change context length and instruction density broadly. A mutation changes the relevant semantic obligation while preserving as much surrounding context as practical. A placebo changes non-semantic wording or identifiers and should leave the owned dimensions materially stable.

If `nui_full` beats baseline but does **not** beat the targeted ablation, V10 does not attribute the gain to that mechanism.

## 4. Public task / hidden evaluator split

Generation consumes `benchmarks/v10/tasks-public.json` only. The hidden corpus must never be concatenated into a model prompt, retrieval index, generated task packet, or route context.

The hidden record owns:

- expected failure traps;
- dimension rubric;
- hard blockers;
- evaluator checklist;
- contamination-sensitive phrases;
- linked hypotheses and ablations.

A public prompt intentionally describes the product problem without naming the omissions the benchmark is meant to discover. If the prompt says “remember audit history, settings, recovery and import/export,” a model does not demonstrate broad capability discovery by repeating those items.

`detect_leakage()` flags evaluator-only marker phrases in outputs. A flagged run remains in the raw bundle and is not silently removed; the experiment owner determines whether the condition is contaminated under the declared exclusion policy.

## 5. Dev and holdout

The 48-task corpus contains 12 task families, four tasks per family, and one holdout task per family. Dev tasks may be used while repairing V10 protocols or tuning evaluator implementation. Holdouts must not be used to rewrite a skill and then be cited as independent transfer evidence for that same revision.

A transfer claim requires holdout evidence. When a holdout is exposed during debugging, future releases should add a new holdout or explicitly downgrade the claim scope.

## 6. Run provenance

Every run record binds generation to:

- exact experiment and task;
- treatment;
- provider;
- model family, model name, and provider-visible snapshot/version;
- agent/runtime version;
- exact NUI revision;
- seed and temperature;
- prompt SHA-256;
- treatment/context SHA-256;
- tool-budget SHA-256;
- artifact SHA-256 values;
- terminal status;
- optional but strongly recommended token, cost and wall-time accounting.

A successful run without artifact digests is invalid. A failure or timeout is a result, not missing data to discard.

Exclusion is reserved for protocol/infrastructure defects and uses a closed reason enum. “Bad output,” “judge disliked it,” “outlier,” or “hurts the claim” are never valid exclusion reasons.

## 7. Failure and timeout accounting

Quality aggregation must report denominator loss. A treatment that produces visually strong outputs on 70% of runs but times out on the remaining 30% is not equivalent to a condition with the same scored mean and no failures.

Every dimension summary includes total records, scored records, failures, timeouts, exclusions and missing rate. A release claim states whether failure behavior differs materially by treatment.

## 8. Blind judging

The generation record contains treatment and model metadata; the judge payload does not. `blind_run_for_judge()` exposes only task/artifact/runtime evidence fields needed for the judgment and hashes the raw run ID into a blind identifier.

For pairwise visual or qualitative comparison:

1. match comparable runs;
2. derive left/right orientation from experiment/task/replicate hash;
3. present only blind artifacts/evidence;
4. require `LEFT`, `RIGHT`, `TIE`, or `UNJUDGABLE`;
5. record calibrated confidence;
6. require evidence references for every scored dimension.

Do not show the judge `baseline`, `nui_full`, route names, ablation identifiers, NUI revision, generator provider, or the generator's preferred candidate. Pair order must not always place NUI on the same side.

## 9. Judge plurality and authority

No judge receives global authority. V10 supports several evidence channels:

- deterministic contract validators;
- executable workflow tests;
- runtime/browser observations;
- rendered-image or temporal-state judgments;
- model-based pairwise judges;
- human pairwise review;
- specialist accessibility/security/domain review when applicable.

A VLM judge can observe hierarchy or visual residue but cannot certify backend permission semantics. A navigation agent can execute an operation but cannot infer that omitted product capabilities were appropriate. A human preference panel can compare perceived refinement but does not waive functional or accessibility blockers.

Same-model generator and judge are correlated evidence. Prefer a different judge lineage for material efficacy claims, and report when independence is limited.

## 10. Multi-dimensional scoring

V10 does not define a universal composite score. Results remain a vector. Relevant dimensions include:

- capability recall;
- scope disposition quality;
- workflow/route connectivity;
- settings/account lifecycle completeness;
- professional-workspace instrument adequacy;
- functional correctness;
- state/recovery completeness;
- accessibility/platform-fit preservation;
- genericness resistance;
- visual hierarchy/focal authority;
- typographic/compositional/material craft;
- domain/audience fit;
- rendered-residue detection;
- critique causal specificity;
- repair effectiveness;
- responsive recomposition;
- motion semantics/reduced-motion equivalence;
- design-to-render fidelity;
- maintainability/system coherence;
- cost/context overhead.

Hard constraints are reported separately. A visual preference win cannot compensate for a new destructive-action, accessibility, security or functional failure.

## 11. Paired statistics

For scalar or pass-rate dimensions, compare matched keys. Do not compute the NUI mean over one task/model set and baseline mean over another and call their difference paired.

V10's deterministic kernel provides a percentile bootstrap over matched deltas. The default positive claim gate requires a positive observed paired delta and a confidence interval whose lower bound is above zero. This is a repository policy, not a universal statistical theorem; experiment owners may choose stricter gates, but weakening it must not silently promote repository claims.

Always report the sample size and W/T/L where pairwise interpretation is useful.

## 12. Ablation identification

A claim about a specific NUI faculty needs more than `nui_full > baseline`.

For hypothesis H and target dimension D:

- full NUI should improve D versus baseline under the bounded matrix;
- removing/mutating H should degrade D relative to full NUI;
- placebo perturbations should not create a comparable D shift;
- unrelated hard dimensions should not regress materially;
- the effect should appear on tasks that actually expose H's decision boundary.

If ablation changes every dimension, the perturbation may be too broad. If ablation changes nothing, the skill may be inert, redundant, routed incorrectly, or the benchmark may be insensitive.

## 13. Cross-model transfer

`EMPIRICAL_LOCAL` is explicitly local to its named models, tasks, runtime and revision.

`EMPIRICAL_TRANSFER` requires at minimum:

- two materially distinct model families;
- holdout tasks;
- positive direction in every included model family rather than pooled compensation;
- targeted ablation identification;
- no material hard-blocker regression;
- exact matrix and artifact provenance.

Do not convert “tested on two model names from the same family” into a cross-family claim. Do not hide a negative model-family result under a larger positive family.

## 14. Cost and context

NUI may improve output by supplying more context and more reasoning structure. That is a legitimate mechanism, but the cost must remain visible.

Report:

- treatment context size when measurable;
- input/output tokens;
- cost;
- wall time;
- tool steps;
- failure/timeout rate.

A quality improvement can remain valuable even with higher cost; V10 simply prevents the tradeoff from disappearing.

## 15. Real-run adapter boundary

The repository does not embed paid-provider credentials or require a specific vendor SDK. `nui-v10-build-run-matrix` emits deterministic provider-neutral JSONL cells. An external adapter consumes each cell plus the public task and routed NUI context, invokes the chosen model/runtime, stores artifacts, hashes them, and writes the V10 run-record JSONL contract.

This makes OpenAI, Anthropic, Google, open-weight/local, browser-agent and future harnesses comparable at the record layer without pretending they have identical capabilities.

Provider adapters must document unavailable controls. If a provider cannot expose an exact seed or snapshot, record that limitation; do not invent provenance.

## 16. Importing real bundles

Before aggregation:

1. validate JSONL syntax;
2. validate every run against the manifest;
3. check duplicate run IDs;
4. verify artifact digests against stored artifacts when available;
5. check treatment coverage and matched pair keys;
6. run contamination checks;
7. retain failures/timeouts;
8. hash the final bundle itself.

The bundle digest enters the claim ledger so a release claim can be reproduced from the exact evidence set.

## 17. Claim promotion

### STRUCTURAL_ONLY
Use when the benchmark/harness exists or only synthetic fixtures were run. This is the normal GitHub CI ceiling.

### EMPIRICAL_LOCAL
Requires real-model runs, matched baseline/full comparison, positive bounded statistical evidence, targeted ablation identification and no hard-blocker regression. The claim names exact scope.

### EMPIRICAL_TRANSFER
Adds multiple model families, holdouts and per-family directional consistency.

### REJECTED
Use when evidence contradicts the claim, hard constraints regress, positive uncertainty gate fails, or the attribution test fails.

A downgraded claim is preferable to an inflated one.

## 18. Release semantics

V10 implementation completion and V10 empirical validation are different milestones. A release can legitimately ship a complete evaluation framework with `STRUCTURAL_ONLY` claim state and an explicit statement that real cross-model experiments were not executed in CI.

When real experiments are later imported, produce a new evidence packet bound to the exact NUI revision. If skill text changes after the experiment, the evidence does not automatically transfer to the new revision.

## 19. Anti-gaming checklist

Before publishing any efficacy result ask:

- Did the generation prompt see evaluator-only language?
- Was NUI always placed on the preferred side?
- Did baseline and NUI use the same model snapshot and tool budget?
- Were failures/timeouts removed?
- Was a task excluded because it hurt the claim?
- Was the same task used to tune the skill and then called holdout evidence?
- Did one model family carry the pooled effect?
- Did a visual gain create a hard semantic/accessibility regression?
- Did full NUI beat the targeted ablation?
- Did a placebo unexpectedly move the same dimension?
- Does the bounded claim name exactly what was tested?

If any answer makes attribution ambiguous, retain the evidence but downgrade the claim.
