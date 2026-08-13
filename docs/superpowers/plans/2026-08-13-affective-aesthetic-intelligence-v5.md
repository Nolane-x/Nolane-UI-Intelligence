# NUI v5 Affective & Aesthetic Intelligence Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Turn the ATLAS v4 failure analysis into an enforceable affective/aesthetic control plane that preserves user emotion, hard-routes high visual ambition, detects global aesthetic collapse, proves visualization semantics, escapes bad visual basins, and blocks unsupported aesthetic completion claims.

**Architecture:** Add a focused `aesthetic.py` deterministic module, thirteen non-overlapping v5 decision-owner skills, v5 schemas/evals, and integrations into routing/repository/completion validators. Strengthen existing visual skills with cross-links to v5 owners instead of duplicating their craft responsibilities.

**Tech Stack:** Python 3.10+, stdlib JSON/unittest, Markdown skill contracts, JSON schemas/eval corpora, GitHub Actions.

## Global Constraints
- Preserve all v1–v4 validation precedence.
- No third-party implementation code or new runtime dependency.
- High aesthetic ambition never waives accessibility, safety, product truth or truthful data encoding.
- Missing required evidence is UNKNOWN/BLOCKED, never PASS.
- v5 behavioral depth must not be proxied by word count.
- The ATLAS “green runtime, failed affective objective” pattern must become a regression failure.

---

### Task 1: Deterministic v5 aesthetic kernel
**Files:** Create `src/nolane_ui/aesthetic.py`; create `tests/test_aesthetic_v5.py`.
**Interfaces:** Produces `mandatory_aesthetic_routes`, `validate_experiential_intent`, `validate_aesthetic_attractor_audit`, `validate_visual_legibility_evidence`, `validate_encoding_provenance_table`, `validate_signature_depth_contract`, `validate_workspace_visual_matrix`, `decide_aesthetic_basin`, and `validate_skill_interaction_evidence`.
- [ ] Write failing tests for each decision function, including v4-like ATLAS failure evidence.
- [ ] Run `python -m unittest tests.test_aesthetic_v5 -v` and confirm failures are caused by missing module/functions.
- [ ] Implement the minimal deterministic kernel.
- [ ] Run the focused suite until green.

### Task 2: v5 routing and completion gates
**Files:** Modify `src/nolane_ui/validators.py`, `src/nolane_ui/__init__.py`; create `tests/test_router_v5.py`, `tests/test_completion_v5.py`.
**Interfaces:** `mandatory_routes_for_profile()` unions v5 aesthetic routes; `validate_v5_completion_evidence(record)` preserves v4 evidence then enforces high-ambition evidence.
- [ ] Write failing routing tests for exceptional/experiential, aspirational identity, magnitude, material visualization and product-wide cases.
- [ ] Write failing completion tests proving code/render health cannot satisfy exceptional ambition without affective/aesthetic evidence and that `RE_DIVERGE` blocks release.
- [ ] Run focused tests and confirm RED.
- [ ] Integrate aesthetic kernel into validators and exports.
- [ ] Run focused tests and confirm GREEN.

### Task 3: v5 skill owners and graph
**Files:** Create thirteen `skills/<name>/SKILL.md`; modify `skills/skill-graph.json`; create `knowledge/v5-skill-manifest.json`; create `tests/test_v5_skill_contracts.py`.
**Interfaces:** Every manifest skill has unique ownership and graph-aligned `family`, `parent`, `output`.
- [ ] Write failing contract tests checking decision-owner uniqueness, required behavioral mechanisms, parent/output bindings, and no word-count threshold.
- [ ] Confirm RED.
- [ ] Write focused skill contracts for the thirteen owners.
- [ ] Extend graph and manifest.
- [ ] Confirm GREEN.

### Task 4: Strengthen existing visual cognition
**Files:** Modify `skills/ui-contracting/SKILL.md`, `routing-ui-work`, `modeling-users-and-tasks`, `exploring-aesthetic-directions`, `researching-visual-references`, `composing-layouts`, `preventing-generic-ui`, `crafting-depth-and-surfaces`, `crafting-spacing-and-rhythm`, `crafting-typography`, `crafting-color`, `directing-visual-hierarchy`, `directing-iconography-and-imagery`, `designing-data-visualization`, `designing-motion`, `critiquing-visual-design`, `challenging-ui-designs`, `iterating-rendered-visual-design`, `gating-ui-completion`.
**Interfaces:** Existing owners retain craft ownership while consuming/producing v5 contracts where appropriate.
- [ ] Write failing semantic-anchor tests for intent preservation, hard ambition route, rendered divergence, reference frontier, accumulation, microtext, resolved type, energy floor, PX hierarchy, channel semantics, dual critics, lineage, basin escape and aesthetic release evidence.
- [ ] Confirm RED.
- [ ] Add concise enforceable clauses and cross-contract references to each owner.
- [ ] Confirm GREEN.

### Task 5: Evidence schemas and adversarial corpus
**Files:** Create v5 JSON schemas; create `evals/v5/manifest.json` and four eval assets; modify `evals/rubric.json`; create `tests/test_v5_eval_integrity.py`.
**Interfaces:** Eval cases reference canonical skills, semantic mutations map to target detectors, skill-interaction cases contain multi-skill combinations, craft distribution spans materially different aesthetic regimes.
- [ ] Write failing integrity tests.
- [ ] Confirm RED.
- [ ] Add schemas and at least 24 v5 cases across affective-aesthetic, semantic mutation, skill interaction and craft distribution assets.
- [ ] Add aesthetic excellence vector to rubric.
- [ ] Confirm GREEN.

### Task 6: Repository/release enforcement and documentation
**Files:** Modify `src/nolane_ui/validators.py`, `scripts/nui-release-packet`, `.github/workflows/verify.yml`, `README.md`, `docs/USAGE.md`, `AGENTS.md`; create `artifacts/v5-completion-packet.example.json`, `tests/test_v5_repository_gate.py`.
**Interfaces:** Repository validator requires v5 assets and reports v5 metrics; CI packages v5 artifacts; release packet explicitly bounds structural verification and names affective/aesthetic behavior limits.
- [ ] Write failing repository mutation tests that remove/change v5 manifest/evals/graph outputs.
- [ ] Confirm RED.
- [ ] Add v5 repository gate and metrics.
- [ ] Update release/CI/docs/version to 0.5.0.
- [ ] Confirm GREEN.

### Task 7: Full verification and milestone packaging
**Files:** Entire repository plus generated milestone artifacts.
- [ ] Run `python -m unittest discover -s tests -v` fresh.
- [ ] Generate a v5 completion packet against the exact local content revision identifier.
- [ ] Run `python scripts/nui-validate . --packet <packet> --revision <revision>`.
- [ ] Verify no untracked accidental files and review diff against this specification.
- [ ] Push one v5 branch/commit set to GitHub, open PR, verify GitHub Actions, and merge only after the exact head is green.
- [ ] Download/verify the GitHub v5 project artifact or create an equivalent verified complete ZIP.
- [ ] Provide a complete milestone ZIP and persist a copy to ChatGPT Library.
