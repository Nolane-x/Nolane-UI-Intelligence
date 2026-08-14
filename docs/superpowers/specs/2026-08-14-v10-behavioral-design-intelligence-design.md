# NUI V10 — Behavioral Design Intelligence & Empirical Proof

## Status
Approved direction: evidence-coupled behavioral intelligence with empirical/cross-model benchmark support. This specification converts that approved direction into an implementation contract.

## Problem
NUI V9 improved product-completeness, taste, rendered critique, domain/audience fit and render fidelity, but much of its release evidence remains structural: required files exist, anchors occur in skills, JSON objects contain expected fields, and deterministic validators reject obvious omissions. Those checks are useful, but they cannot prove that a skill changes model behavior, that an aesthetic rule improves human-perceived quality, that a scope critic catches omissions under pressure, or that the same gain transfers across models and tasks.

V10 therefore treats every material NUI improvement as a falsifiable behavioral hypothesis. A new mechanism is incomplete until the repository can state what decision it should change, what evidence should reveal that change, what mutation or ablation should destroy the effect, what benchmark task exposes it, and what empirical result is required before a quality claim is promoted.

## Research basis and transfer boundary
V10 borrows evaluation mechanisms, not benchmark trade dress or private data.

- WebCoderBench (ACL 2026) demonstrates the value of multi-perspective, fine-grained web-generation evaluation rather than hiding model behavior behind one score; it reports 24 metrics across 9 perspectives over 1,572 real user requirements.
- ArtifactsBench evaluates rendered interactive artifacts with temporal screenshots and fine-grained per-task checklists, then validates automated ranking against human preference.
- Vision2Web separates static visual reproduction, multi-page interaction and long-horizon full-stack development and combines GUI-agent verification with VLM judging.
- WebGen-Bench evaluates generated multi-file websites with executable operation/expected-result tests.
- Design2Code combines automatic metrics with human evaluation to validate ranking and exposes layout/visual-element failure modes.

NUI does not copy their task sets into the repository unless licensing and redistribution are explicitly compatible. Instead V10 records source citations and builds an original, product-centered corpus whose dimensions are specific to NUI's hypotheses.

## Core architecture
V10 consists of five independent planes connected by typed evidence.

### 1. Behavioral Hypothesis Registry
Every V10 behavioral mechanism declares:
- a stable `hypothesis_id`;
- the canonical skill owner(s) and decision boundary;
- an observable behavior expected to change;
- a baseline failure mode;
- positive and negative controls;
- required evidence channels;
- falsifiers;
- linked benchmark dimensions and tasks;
- mutation and ablation targets;
- prohibited overclaim language.

A mechanism without a falsifier or empirical exposure is documentation, not validated behavioral intelligence.

### 2. Experimental Task Corpus
The corpus is original and stratified. It must include at least these task families:
- product-scope/completeness under ambiguous prompts;
- settings/account/workspace lifecycle;
- professional editor/tool-workspace architecture;
- visual direction/taste discrimination;
- screenshot critique and repair;
- default-platform/interface residue;
- domain/audience adaptation;
- motion semantics and reduced-motion equivalence;
- design-to-render fidelity;
- cross-axis compound tasks where multiple faculties interact.

Each task contains a prompt, hidden evaluator checklist, expected failure traps, artifact requirements, judge dimensions, execution requirements, leakage-sensitive terms, and applicable ablations. Public task text must not reveal hidden expected omissions or scoring rubrics.

### 3. Controlled Run Matrix
A valid empirical experiment compares matched conditions. Minimum conditions are:
- `baseline`: same model/runtime with no NUI;
- `nui_full`: same model/runtime with the complete routed NUI context;
- `nui_ablation:<plane>`: same model/runtime with one targeted plane removed or semantically neutralized.

Recommended robustness conditions include:
- mutation variants that invert or weaken one rule;
- unrelated-context placebo injection;
- repeated seeds/temperature replicates;
- at least two model families when making cross-model claims.

The harness records provider/model identifier, model snapshot/version when available, agent/runtime version, prompt/context hashes, NUI revision, route, seed, temperature, token/cost accounting, wall time, tool availability and artifact hashes. Results without provenance cannot enter release evidence.

### 4. Multi-channel Evaluation Court
No single judge owns V10 quality. The court separates:
- deterministic product-completeness checks;
- executable functionality/workflow checks;
- rendered visual checks;
- pairwise preference/taste checks;
- accessibility/platform/fidelity checks;
- judge-model assessments with explicit rubric and blindness;
- optional human pairwise review.

Judges are blind to treatment labels. Pairwise comparisons randomize left/right presentation. The evaluator stores raw observations and verdicts separately from aggregate summaries. A judge cannot receive the hypothesis answer key or NUI treatment identity.

### 5. Statistical Claim Gate
V10 never treats one successful run as proof. For each hypothesis, aggregation reports:
- sample count by condition/model/task family;
- mean/median or pass rate as appropriate;
- paired delta for matched tasks;
- bootstrap confidence interval for the paired delta;
- win/tie/loss counts for pairwise preference;
- consistency across model families;
- ablation recovery: `nui_full` must outperform the targeted ablation in the intended dimension without unacceptable regressions in hard constraints;
- regression dimensions and unresolved uncertainty.

Claims are typed:
- `STRUCTURAL_ONLY`: repository/eval contracts exist; no empirical efficacy claim.
- `EMPIRICAL_LOCAL`: evidence supports the claim for named models/tasks/runtime only.
- `EMPIRICAL_TRANSFER`: evidence supports the claim across the configured transfer matrix.
- `REJECTED`: evidence contradicts or fails to support the claim.

No repository-only CI may emit `EMPIRICAL_LOCAL` or `EMPIRICAL_TRANSFER` unless it consumes signed/pinned empirical result artifacts that satisfy provenance and statistical gates.

## Benchmark dimensions
V10 reports a vector, not one beauty score. Core dimensions are:
1. capability recall;
2. scope disposition quality;
3. workflow/route connectivity;
4. settings/account lifecycle completeness;
5. professional-workspace instrument adequacy;
6. functional correctness;
7. state/recovery completeness;
8. accessibility and platform-fit preservation;
9. genericness resistance;
10. visual hierarchy and focal authority;
11. typographic/compositional/material craft;
12. domain/audience fit;
13. rendered-residue detection;
14. critique causal specificity;
15. repair effectiveness after critique;
16. responsive recomposition;
17. motion semantics/reduced-motion equivalence;
18. design-to-render fidelity;
19. maintainability/system coherence;
20. cost/context overhead.

Hard constraints are not averaged away by visual gains. Safety, accessibility, functional correctness and destructive-action integrity can block a release claim.

## Anti-gaming and contamination controls
- Hidden evaluator checklists are stored separately from public task prompts.
- Treatment labels are removed from judge inputs.
- Pair order is deterministically randomized from experiment/task hashes.
- Prompt/context SHA-256 hashes are persisted.
- A task records contamination-sensitive phrases; provider output containing evaluator-only phrases is flagged.
- The same judge cannot certify a claim solely from self-authored rationale; raw artifact evidence is required.
- Aggregate metrics cannot silently drop failed or timed-out runs; missingness is reported explicitly.
- Excluding a run requires a recorded exclusion reason from a closed enum.
- Benchmark tuning tasks and holdout tasks are separate; holdout results are required for transfer claims.

## Mutation and ablation design
V10 adds semantic mutations whose expected consequence is known. Examples:
- replace broad-before-narrow with prompt-literal scope compression;
- remove `EXPECTED` capability disposition;
- allow settings as a flat miscellaneous page;
- remove account deletion/recovery continuity;
- replace comparative taste with scalar self-score;
- remove screenshot evidence from visual critique;
- allow accidental native chrome without an intentionality decision;
- remove audience consequences from domain signatures;
- allow decorative motion to override task feedback;
- remove runtime visual-regression evidence.

A deep skill should show mutation sensitivity: the benchmark dimension it owns should degrade under the corresponding mutation. If it does not, the skill may be inert, redundant or poorly evaluated.

## Cross-model empirical protocol
A publishable-strength claim should run at least two materially different model families and, where budgets allow, multiple agent harnesses. The default matrix is configurable; V10 never hardcodes vendor superiority.

For each model/task/treatment cell, the harness supports repeated runs. Matched comparisons use identical task material and comparable runtime/tool budgets. Cost/token differences are reported rather than silently normalized away. A full NUI condition that wins quality by using dramatically more context must expose that tradeoff in the result vector.

## Runtime/provider boundary
The repository must remain useful without paid model credentials. Therefore:
- deterministic CI validates schemas, statistics, randomization, leakage guards, aggregation and synthetic fixtures;
- empirical generation is performed by a provider-neutral JSONL protocol or external runner adapters;
- real provider/model runs are opt-in and must not be fabricated when credentials are absent;
- CI can validate imported empirical run bundles but cannot promote them beyond their recorded provenance.

## V10 knowledge depth requirement
V10 does not accept list-only knowledge as deep evidence. Every benchmark reference/mechanism promoted into a V10 research ledger requires:
- primary source URL;
- source type and authority role;
- inspected mechanism;
- transfer boundary;
- contraindication/counterexample;
- applicable task classes;
- drift/freshness posture;
- empirical hypothesis link where the source materially informs a V10 mechanism.

The V9 benchmark gallery remains a retrieval seed but is not treated as empirical proof.

## Release and CI contract
V10 release validation must distinguish three separate gates:
1. repository structural validity;
2. behavioral-eval contract validity on deterministic/synthetic fixtures;
3. empirical evidence validity for any empirical claim.

A green CI with no real model runs may release the V10 framework as `STRUCTURAL_ONLY`. It may not state that NUI empirically improves UI generation.

The release packet includes:
- exact git revision;
- structural test summary;
- mutation/ablation fixture summary;
- empirical claim ledger;
- imported empirical bundle digests;
- unresolved claims;
- explicit statement of what was not run.

## Non-goals
- No universal beauty score.
- No claim that one benchmark predicts every product/domain.
- No forced increase in canonical skill count.
- No copying proprietary benchmark tasks or brand trade dress.
- No hidden model credentials in the repository.
- No empirical claim inferred from structural tests.

## Success criteria
V10 is structurally complete when the repository can reject malformed experiments, non-blind judging, treatment leakage, unpaired comparisons, invalid ablation claims, unsupported empirical promotion and benchmark bundles with missing provenance; when each V10 hypothesis links to tasks/mutations/metrics; and when CI packages a bounded `STRUCTURAL_ONLY` release packet in the absence of real empirical runs.

V10 is empirically validated only after external real-model runs satisfy the configured statistical gates. That state is deliberately separate from implementation completion.
