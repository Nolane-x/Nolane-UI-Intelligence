# NUI v6 Deep Research & Design Synthesis Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build NUI v6 so material UI work is forced through evidence-backed deep source research, coherent cross-source synthesis, deeper aesthetic skill decision procedures, broader UI-industry source coverage, and causal skill-effect gates.

**Architecture:** Keep v1-v5 behavior compatible. Add a v6 overlay module and knowledge/eval planes instead of rewriting historical validators. Deepen existing owners where the ownership is already correct; add only four new decision owners for repository archaeology, synthesis, research-depth criticism, and causal skill-effect benchmarking.

**Tech Stack:** Python 3.10+, JSON schemas/fixtures, Markdown Agent Skills, unittest, GitHub Actions.

## Global Constraints

- Do not use token/word count as proof of skill depth.
- Do not treat source popularity as authority.
- README-only research cannot authorize material external influence.
- High-drift material sources require snapshot/ref evidence and live verification.
- External source mechanisms must be reconciled to local product semantics, state, accessibility, tokens, content, motion, responsiveness, performance, and license boundaries.
- New skills require unique ownership and must not duplicate an existing decision owner.
- v1-v5 deterministic behavior must remain green.
- Structural CI must not claim objective universal beauty.

---

### Task 1: v6 source-intelligence kernel
**Files:** Create `tests/test_source_intelligence_v6.py`, create `src/nolane_ui/source_intelligence.py`.
**Interfaces:** Produces `required_artifact_classes`, `plan_source_research`, `validate_source_research_dossier`, `validate_source_mix`, `validate_cross_source_synthesis`.
- [ ] Write tests proving README-only material research fails, role-specific artifact obligations differ, high-drift sources require snapshot evidence, and coherent cross-source ownership passes.
- [ ] Run `python -m unittest tests.test_source_intelligence_v6 -v` and verify RED because the module/functions do not exist.
- [ ] Implement minimal deterministic functions and constants.
- [ ] Re-run targeted tests to GREEN.
- [ ] Commit kernel and tests.

### Task 2: source dossier/synthesis schemas and CLIs
**Files:** Create `schemas/ui-source-research-dossier.schema.json`, `schemas/ui-cross-source-synthesis.schema.json`, `scripts/nui-source-plan`, `scripts/nui-source-audit`.
**Interfaces:** CLIs load JSON, call source-intelligence functions, emit JSON, non-zero exit on invalid input.
- [ ] Write `tests/test_source_cli_v6.py` for valid/invalid dossiers and plans.
- [ ] Run targeted tests RED.
- [ ] Add schemas and scripts.
- [ ] Run targeted tests GREEN.
- [ ] Commit.

### Task 3: UI source intelligence registry v6
**Files:** Create `knowledge/ui-source-intelligence-v6.json`, `docs/research/UI-SOURCE-INTELLIGENCE-V6.md`.
**Interfaces:** Every source has role/tier/domains/capabilities/stacks/drift/license/research_map/mechanism_families/adaptation boundaries/provenance.
- [ ] Write `tests/test_source_registry_v6.py` that rejects missing research maps, invalid tiers/roles, anchor sources without material provenance, and insufficient domain breadth.
- [ ] Run RED.
- [ ] Build registry from the existing 52 sources and add current missing source classes with explicit discovery-vs-anchor posture.
- [ ] Run GREEN.
- [ ] Commit.

### Task 4: industry ontology v6
**Files:** Create `knowledge/ui-industry-ontology-v6.json`, create `src/nolane_ui/depth.py`, create `tests/test_industry_ontology_v6.py`.
**Interfaces:** `validate_industry_ontology` verifies mandatory axes, owners/verifiers, evidence classes, source domains, and interaction-cell ownership.
- [ ] Write RED tests for missing axes, unknown skills, owner/verifier collision, and unowned high-risk interaction cells.
- [ ] Implement validator and ontology.
- [ ] Run GREEN.
- [ ] Commit.

### Task 5: skill depth constitution v6
**Files:** Create `knowledge/skill-depth-constitution-v6.json`, extend `src/nolane_ui/depth.py`, create `scripts/nui-depth-audit`, create `tests/test_skill_depth_constitution_v6.py`.
**Interfaces:** `validate_skill_depth_record` and `audit_skill_depth` check behavior-bearing dimensions without fixed heading templates or word-count thresholds.
- [ ] Write RED tests showing long shallow prose fails, short behaviorally complete skill can pass, and repeated identical depth evidence across many skills is flagged as suspicious but not rejected solely for shared headings.
- [ ] Implement constitution/auditor/CLI.
- [ ] Run GREEN.
- [ ] Commit.

### Task 6: four new decision owners and graph routing
**Files:** Create four `skills/*/SKILL.md`, update `skills/skill-graph.json`, create `knowledge/v6-skill-manifest.json`, update routing owners where required, create `tests/test_v6_skill_contracts.py`.
**Interfaces:** New owners are `performing-ui-repository-archaeology`, `synthesizing-cross-source-ui-language`, `auditing-ui-research-depth`, `benchmarking-ui-skill-effect`.
- [ ] Write RED tests for graph declaration, parent/ownership uniqueness, outputs, and hard routing for material external-source influence.
- [ ] Write the four bespoke skill contracts.
- [ ] Update graph/manifest/routing.
- [ ] Run GREEN.
- [ ] Commit.

### Task 7: bespoke deepening of v5 aesthetic spine
**Files:** Rewrite the 13 skills listed in `knowledge/v5-skill-manifest.json`; selectively deepen high-leverage legacy visual/critic skills identified by the v6 depth audit.
**Interfaces:** Preserve skill names/parents/outputs while adding domain-specific observations, branch logic, falsification/counterfactuals, evidence, recovery, and handoffs.
- [ ] Write `tests/test_v6_aesthetic_depth.py` with semantic obligations unique to each v5 owner rather than word-count thresholds.
- [ ] Run RED against v5 prose.
- [ ] Rewrite each skill individually; do not append one shared template.
- [ ] Run GREEN and full depth audit.
- [ ] Commit.

### Task 8: v6 adversarial/causal eval planes
**Files:** Create `evals/v6/manifest.json` plus source-depth, synthesis, ontology, and skill-effect case suites; create `tests/test_v6_eval_integrity.py`.
**Interfaces:** Cases declare id, required skills, setup, pressure/failure, expected decision, evidence requirements, and evaluator owner.
- [ ] Write RED eval-integrity tests and at least one executable validator regression per plane.
- [ ] Add adversarial fixtures covering README-only research, stale refs, gallery monoculture, role mismatch, collage, unsupported assumptions, semantic mutations, and ablations.
- [ ] Run GREEN.
- [ ] Commit.

### Task 9: v6 repository/completion gate
**Files:** Create `src/nolane_ui/validators_v6.py` or extend overlay cleanly; update `src/nolane_ui/validators.py`, `src/nolane_ui/__init__.py`; create `tests/test_v6_repository_gate.py`, `tests/test_completion_v6.py`; create `artifacts/v6-completion-packet.example.json`.
**Interfaces:** `validate_v6_completion_evidence` and repository metrics include v6 sources, source domains, ontology axes/interactions, depth audit, v6 skill count, and v6 eval count.
- [ ] Write RED completion/repository tests.
- [ ] Implement v6 overlay while preserving v1-v5 exports.
- [ ] Run targeted then full suite.
- [ ] Commit.

### Task 10: docs, CI, release artifact, final verification
**Files:** Update `README.md`, `docs/USAGE.md`, `docs/UI-ECOSYSTEM-REGISTRY.md`, `AGENTS.md`, `pyproject.toml`, `nui.config.json`, `.github/workflows/verify.yml`, `scripts/nui-release-packet`.
**Interfaces:** v6 version 0.6.0; CI packages `Nolane-UI-Intelligence-v6-complete.zip` and v6 completion packet.
- [ ] Update documentation with deep-reading protocol and bounds.
- [ ] Update CI/release packet/version.
- [ ] Run `python -m unittest discover -s tests -v`.
- [ ] Run `python scripts/nui-validate .` and inspect complete JSON.
- [ ] Build and test complete milestone ZIP.
- [ ] Push branch, open PR, verify GitHub Actions, merge to main, verify post-merge main CI.
- [ ] Download official main CI artifact, re-run tests and validator from that exact artifact.
- [ ] Create final milestone ZIP containing the exact official artifact, CI metadata, test logs, validator output, docs, and checksums; upload exact ZIP to ChatGPT Library.
