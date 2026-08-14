# NUI V10 Behavioral Design Intelligence & Empirical Proof Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build a falsifiable, provider-neutral empirical evaluation system that can measure whether NUI changes UI/product-design behavior, detect inert or harmful skills through mutations/ablations, and prevent unsupported empirical quality claims.

**Architecture:** Preserve the 174-skill canonical graph. Add focused V10 kernels for hypothesis/task/experiment contracts, blinded judging, statistical aggregation and claim promotion; add original public/hidden benchmark corpora and mutation registries; connect V10 to existing skill owners, repository validation, release packets and GitHub Actions. Real model execution remains opt-in via JSONL provider protocol, while CI verifies all deterministic logic with synthetic fixtures and emits `STRUCTURAL_ONLY` unless genuine empirical bundles are imported.

**Tech Stack:** Python 3.10+ standard library, JSON/JSONL contracts, existing `unittest` suite, GitHub Actions, repository skill/knowledge/eval conventions.

## Global Constraints
- Preserve exactly 174 canonical skills unless an ownership audit proves a genuinely non-decomposable new decision class.
- Do not use prose length, file count or benchmark count as a quality proxy.
- Do not copy proprietary benchmark tasks; transfer evaluation mechanisms only.
- No universal beauty score and no single aggregate may override hard functional/accessibility/safety regressions.
- Structural CI must never manufacture `EMPIRICAL_LOCAL` or `EMPIRICAL_TRANSFER` claims.
- Every empirical claim must bind to exact NUI revision, model/runtime identity, task set, treatment, run provenance, artifact digests and statistical evidence.
- Judge inputs must be treatment-blind and pair ordering deterministic but concealed from model-generation conditions.
- Failed/timed-out/missing runs remain visible; exclusion requires an enumerated reason.

---

### Task 1: V10 behavioral hypothesis kernel

**Files:**
- Create: `src/nolane_ui/behavior_v10.py`
- Create: `knowledge/v10-behavioral-hypotheses.json`
- Test: `tests/test_v10_hypotheses.py`

**Interfaces:**
- Produces: `validate_hypothesis_registry(record: dict) -> dict`
- Produces: stable hypothesis schema consumed by tasks, mutations, experiments and release claims.

- [ ] Write failing tests requiring unique IDs, canonical owners, decision boundary, observable behavior, baseline failure, positive/negative controls, evidence channels, falsifiers, task/dimension links, mutation/ablation targets and prohibited overclaim text.
- [ ] Verify RED: registry with descriptive prose but no falsifier/task exposure must fail.
- [ ] Implement validation with cross-field checks: every target task/dimension/mutation must be non-empty IDs; every hypothesis must have at least one falsifier and both control classes; duplicate observable behaviors on different owners emit an overlap error unless an explicit interaction relationship exists.
- [ ] Add 12 deep hypotheses spanning product scope, settings, account continuity, professional workspace, comparative taste, rendered critique, interface residue, domain/audience fit, motion semantics, render fidelity, responsive recomposition and compound closure.
- [ ] Verify GREEN and commit.

### Task 2: Original benchmark corpus with hidden evaluator separation

**Files:**
- Create: `benchmarks/v10/tasks-public.json`
- Create: `benchmarks/v10/tasks-hidden.json`
- Create: `src/nolane_ui/benchmark_v10.py`
- Test: `tests/test_v10_benchmark_tasks.py`

**Interfaces:**
- Produces: `validate_task_corpus(public, hidden, hypotheses) -> dict`
- Produces: `materialize_task_for_generation(task_id) -> public task only`
- Produces: `materialize_task_for_judge(task_id) -> blind evaluator contract`

- [ ] Write failing tests proving public prompts cannot contain hidden checklist phrases, expected omissions, treatment names or answer-key fields.
- [ ] Add at least 48 original tasks across 12 families, with explicit `dev` versus `holdout` split and low/medium/high complexity strata.
- [ ] Hidden records define failure traps, required artifact classes, scoring dimensions, hard blockers, judge checklist, leakage-sensitive phrases and applicable hypotheses/ablations.
- [ ] Implement referential-integrity checks between public/hidden IDs, minimum family coverage, holdout coverage, rubric blindness and contamination-phrase separation.
- [ ] Verify GREEN and commit.

### Task 3: Mutation/ablation sensitivity plane

**Files:**
- Create: `benchmarks/v10/mutations.json`
- Create: `src/nolane_ui/mutation_v10.py`
- Test: `tests/test_v10_mutations.py`

**Interfaces:**
- Produces: `validate_mutation_registry(record, hypotheses, tasks) -> dict`
- Produces: `expected_mutation_effects(registry) -> mapping`

- [ ] Write RED tests for mutations without a targeted owner/dimension, without expected degradation, or with no exposed benchmark tasks.
- [ ] Add semantic mutations for each core V10 hypothesis, including prompt-literal scope compression, flat settings, login-only accounts, all-tools-visible workspace, scalar beauty self-score, spec-only critique, accidental native residue, generic domain theming, decorative motion dominance and design-file-only fidelity.
- [ ] Require negative-control/placebo mutations that should *not* change unrelated dimensions; this prevents a harness from rewarding generic perturbation sensitivity.
- [ ] Implement registry checks for target isolation and interaction mutations.
- [ ] Verify GREEN and commit.

### Task 4: Experiment manifest and run provenance

**Files:**
- Create: `schemas/v10-experiment.schema.json`
- Create: `schemas/v10-run-record.schema.json`
- Create: `src/nolane_ui/experiment_v10.py`
- Test: `tests/test_v10_experiments.py`

**Interfaces:**
- Produces: `validate_experiment_manifest(record, corpus, mutations) -> dict`
- Produces: `validate_run_record(record, manifest) -> dict`
- Produces: `pairing_key(run) -> tuple`

- [ ] Write RED tests for unmatched baseline/full conditions, missing model snapshot/runtime/NUI revision, missing prompt/context/artifact hashes, silent failures, invalid exclusion reasons and mixed tool budgets.
- [ ] Define conditions `baseline`, `nui_full`, `nui_ablation:<id>`, `nui_mutation:<id>` and optional placebo.
- [ ] Enforce paired-comparison keys over task/model/runtime/replicate/tool budget.
- [ ] Record provider, model family/name/snapshot, harness, seed, temperature, context/prompt SHA-256, token/cost/time accounting, tool capabilities, artifact digests and terminal status.
- [ ] Verify GREEN and commit.

### Task 5: Blind evaluation and anti-leakage court

**Files:**
- Create: `src/nolane_ui/judging_v10.py`
- Create: `benchmarks/v10/judge-rubric.json`
- Test: `tests/test_v10_judging.py`

**Interfaces:**
- Produces: `blind_run_for_judge(run) -> dict`
- Produces: `pair_orientation(experiment_id, task_id, replicate) -> tuple[str, str]`
- Produces: `validate_judgment(record, hidden_task, run_index) -> dict`
- Produces: `detect_leakage(text, hidden_task) -> list[str]`

- [ ] RED-test that treatment labels, NUI route names, ablation IDs and provider-specific generation metadata never enter judge payloads.
- [ ] Implement deterministic SHA-256 pair orientation so reruns are reproducible without a global left/right bias.
- [ ] Require raw evidence refs for every judge dimension; rationale-only scoring fails.
- [ ] Add contamination detection for hidden checklist phrases and answer-key-like content.
- [ ] Require pairwise verdict `LEFT|RIGHT|TIE|UNJUDGABLE` plus confidence calibration and hard-blocker findings.
- [ ] Verify GREEN and commit.

### Task 6: Multi-dimensional statistical aggregator

**Files:**
- Create: `src/nolane_ui/stats_v10.py`
- Test: `tests/test_v10_stats.py`

**Interfaces:**
- Produces: `paired_delta(samples_full, samples_control) -> float`
- Produces: `bootstrap_ci(paired_deltas, confidence=0.95, resamples=5000, seed=...) -> tuple`
- Produces: `aggregate_dimension(records, judgments, dimension) -> dict`
- Produces: `evaluate_ablation_recovery(...) -> dict`

- [ ] RED-test mismatched pairs, dropped failures, zero-sample claims, unstable pairwise ordering and confidence intervals computed from unpaired data.
- [ ] Implement standard-library deterministic percentile bootstrap over paired deltas.
- [ ] Aggregate pass-rate, mean/median, paired delta, CI, W/T/L, missing/error rates, cost/context overhead and per-model/task-family strata.
- [ ] Treat hard-blocker regressions separately from soft score improvements.
- [ ] Require targeted ablation degradation for a hypothesis to count as behaviorally identified.
- [ ] Verify GREEN and commit.

### Task 7: Empirical claim promotion gate

**Files:**
- Create: `src/nolane_ui/claims_v10.py`
- Create: `schemas/v10-claim.schema.json`
- Test: `tests/test_v10_claims.py`

**Interfaces:**
- Produces: `validate_claim(record, aggregate, provenance) -> dict`
- Produces: `promote_claim(...) -> STRUCTURAL_ONLY|EMPIRICAL_LOCAL|EMPIRICAL_TRANSFER|REJECTED`

- [ ] RED-test attempts to promote structural fixtures to empirical status.
- [ ] `EMPIRICAL_LOCAL` requires real-model provenance, matched baseline/full comparisons, positive targeted delta with CI gate, no hard-blocker regression and applicable ablation recovery.
- [ ] `EMPIRICAL_TRANSFER` additionally requires at least two model families, holdout tasks, cross-family direction consistency and no model family with a material contradictory effect hidden by pooled averaging.
- [ ] Store bounded claim language, model/task/runtime scope and explicit unresolved regressions.
- [ ] Verify GREEN and commit.

### Task 8: Provider-neutral empirical runner protocol

**Files:**
- Create: `docs/V10-EMPIRICAL-RUN-PROTOCOL.md`
- Create: `scripts/nui-v10-build-run-matrix`
- Create: `scripts/nui-v10-validate-run-bundle`
- Create: `scripts/nui-v10-aggregate`
- Create: `examples/v10/experiment.example.json`
- Create: `examples/v10/run-record.example.jsonl`
- Test: `tests/test_v10_cli_protocol.py`

**Interfaces:**
- CLI outputs JSON only on stdout for machine chaining; diagnostics go to stderr.
- External provider runners consume generation task JSONL and return run-record JSONL.

- [ ] RED-test deterministic matrix generation and rejection of fabricated empirical status when no external runs are present.
- [ ] Build matrix expansion over tasks × models × treatments × replicates with stable IDs.
- [ ] Document provider adapter boundary without embedding any vendor credential or API dependency.
- [ ] Validate imported bundles and compute exact file digests.
- [ ] Verify GREEN and commit.

### Task 9: Deep skill integration without ownership duplication

**Files:**
- Modify: `skills/modeling-product-intent/SKILL.md`
- Modify: `skills/inventorying-product-capabilities/SKILL.md`
- Modify: `skills/architecting-information/SKILL.md`
- Modify: `skills/designing-authentication-and-passkeys/SKILL.md`
- Modify: `skills/designing-editor-canvas-workspaces/SKILL.md`
- Modify: `skills/designing-desktop-windowed-workspaces/SKILL.md`
- Modify: `skills/exploring-aesthetic-directions/SKILL.md`
- Modify: `skills/critiquing-visual-design/SKILL.md`
- Modify: `skills/verifying-design-fidelity/SKILL.md`
- Modify: `skills/modeling-users-and-tasks/SKILL.md`
- Modify: `skills/designing-motion/SKILL.md`
- Modify: `skills/engineering-rich-interactive-components/SKILL.md`
- Modify: `skills/nolane-ui/SKILL.md`
- Modify: `skills/using-nolane-ui/SKILL.md`
- Modify: `skills/routing-ui-work/SKILL.md`
- Modify: `AGENTS.md`
- Test: `tests/test_v10_skill_protocols.py`

**Interfaces:**
- Each owner links its V10 behavioral hypothesis, falsification condition, evidence output and mutation/ablation exposure; it does not repeat generic benchmark prose.

- [ ] RED-test semantic anchors unique to each owner, including explicit boundary between design generation evidence and empirical efficacy evidence.
- [ ] Add V10 sections that deepen the owner's specific decision logic rather than repeating one template.
- [ ] Add root invariants: empirical claims require imported real-run evidence; absence remains `STRUCTURAL_ONLY`; ablation sensitivity is required for attributed efficacy; hidden benchmark rubrics must not enter generation context.
- [ ] Verify GREEN and commit.

### Task 10: Research provenance and source-depth ledger

**Files:**
- Create: `knowledge/v10-empirical-evaluation-sources.json`
- Modify: `docs/research/SOURCES.md`
- Test: `tests/test_v10_research_sources.py`

**Interfaces:**
- Source entries bind primary source, inspected mechanism, authority role, transfer boundary, contraindication, drift posture and V10 hypothesis/eval use.

- [ ] Add WebCoderBench, ArtifactsBench, Vision2Web, WebGen-Bench and Design2Code from primary papers/official publication pages.
- [ ] Require mechanism-level transfer notes and explicit non-copy boundary.
- [ ] Ensure no source is treated as global design authority or proof of NUI efficacy.
- [ ] Verify GREEN and commit.

### Task 11: V10 repository/release/CI closure

**Files:**
- Create: `src/nolane_ui/v10_repository.py`
- Modify: `src/nolane_ui/validators.py`
- Modify: `src/nolane_ui/__init__.py`
- Modify: `scripts/nui-release-packet`
- Modify: `.github/workflows/verify.yml`
- Modify: `pyproject.toml`
- Modify: `README.md`
- Test: `tests/test_v10_repository.py`
- Test: `tests/test_v10_completion.py`

**Interfaces:**
- Repository validator reports V10 hypotheses/tasks/holdouts/mutations/dimensions and structural-vs-empirical claim state.
- Release packet must be `STRUCTURAL_ONLY` in ordinary CI unless a validated empirical bundle is explicitly supplied.

- [ ] RED-test V10 required-file graph, cross-link integrity and overclaim prevention.
- [ ] Set package version `0.10.0`.
- [ ] Chain V10 repository validator after V9 without weakening inherited gates.
- [ ] Extend release packet with exact revision, hypothesis coverage, task/mutation coverage, empirical bundle digests, claim ledger and explicit unrun statement.
- [ ] CI runs full tests, validates repository, generates bounded V10 packet, packages complete project and uploads both artifacts.
- [ ] Verify GREEN and commit.

### Task 12: Full adversarial review and final verification

**Files:**
- Create: `evals/v10-behavioral-empirical-adversarial.json`
- Test: `tests/test_v10_adversarial.py`
- Modify any V10 implementation file only when review finds a concrete loophole.

**Interfaces:**
- Adversarial corpus includes both `BLOCK` and anti-overcorrection `ALLOW` cases.

- [ ] Add at least 48 adversarial cases covering fake provenance, same-output duplicate conditions, judge leakage, pooled Simpson-style masking, missing holdout, mutation without targeted degradation, cherry-picked exclusions, timeouts dropped from denominator, cost blow-up hidden by quality score, false cross-model claim and legitimate structural-only release.
- [ ] Run the full suite and repository validator on the branch.
- [ ] Review branch diff against base for duplicated prose/owners and cross-field loopholes.
- [ ] Add RED tests for each review-discovered loophole before fixing it.
- [ ] Run fresh full verification again.
- [ ] Fast-forward/merge to `main` only after branch CI is green, then rerun CI on `main`.
- [ ] Download exact-main complete-project artifact, verify ZIP integrity/digest, persist ZIP and completion packet to ChatGPT Library.
