# NUI v7 Concrete Craft & Authority Intelligence Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Turn NUI's meta-intelligence into fast, source-bound concrete design intelligence and rendered-output verification.

**Architecture:** Add three deterministic kernels (`authority.py`, `concrete.py`, `perceptual.py`), three versioned knowledge planes, eight uniquely-owned skills, v7 evals/schemas, and a v7 completion/repository gate that wraps v6. Existing 158 skills remain canonical and are deepened only where new routing/evidence contracts must be consumed.

**Tech Stack:** Python 3.12 stdlib, JSON/JSON Schema artifacts, Markdown skill contracts, unittest, GitHub Actions.

## Global Constraints
- No production code before its failing behavior test.
- Do not use source count, word count, token count, stars, or screenshot existence as quality proxies.
- External authority is decision-dimensional and can never override explicit product/safety/law constraints.
- Pointer/adapter metadata must preserve live verification and license boundaries.
- High-ambition visual completion requires rendered perceptual evidence, not prose claims.

---

### Task 1: Authority resolver
**Files:** Create `tests/test_authority_v7.py`, `src/nolane_ui/authority.py`, `knowledge/ui-authority-mesh-v7.json`.
**Interfaces:** `resolve_authorities(profile, mesh) -> dict`, `validate_authority_mesh(mesh) -> dict`, `validate_authority_route_plan(plan) -> dict`.
- [ ] Write tests proving platform, public-service, component-semantics, enterprise, commerce, visual-frontier and adapter-role precedence.
- [ ] Run tests and verify missing-module failure.
- [ ] Implement the smallest resolver/validator that passes.
- [ ] Run tests green and commit.

### Task 2: Concrete pattern compiler
**Files:** Create `tests/test_concrete_v7.py`, `src/nolane_ui/concrete.py`, `knowledge/concrete-design-patterns-v7.json`, `knowledge/immediate-synthesis-grammar-v7.json`.
**Interfaces:** `compile_concrete_design_packet(profile, authority_result, pattern_kb, grammar) -> dict`, `validate_pattern_kb(kb) -> dict`, `validate_concrete_design_packet(packet) -> dict`.
- [ ] Write failing tests for domain-specific cards, contraindications, bounded decision count, unresolved blockers, and no Shopify→generic-commerce authority smear.
- [ ] Run RED.
- [ ] Implement deterministic tag/domain scoring and packet validation.
- [ ] Run GREEN and commit.

### Task 3: Rendered perceptual evidence
**Files:** Create `tests/test_perceptual_v7.py`, `src/nolane_ui/perceptual.py`, `knowledge/rendered-perception-rubric-v7.json`, `schemas/rendered-perception-evidence.schema.json`.
**Interfaces:** `validate_rendered_perception(record, high_ambition=False) -> dict`.
- [ ] Write failing tests for screenshot-theater rejection, multi-viewport/state coverage, resolved typography, signature observation, motion temporal evidence, reduced-motion equivalent, and calibrated pixel-diff evidence.
- [ ] Run RED.
- [ ] Implement validator.
- [ ] Run GREEN and commit.

### Task 4: Agent-readable adapters
**Files:** Create `tests/test_agent_adapters_v7.py`, `knowledge/agent-readable-ui-sources-v7.json`, `schemas/ui-authority-route.schema.json`, `schemas/concrete-design-packet.schema.json`.
**Interfaces:** data validated through `authority.validate_agent_adapters`.
- [ ] Write failing tests that MCP/llms/skills/open-code are access modes rather than automatic authority escalation.
- [ ] Run RED.
- [ ] Add curated adapters for Primer MCP, Mantine llms/MCP/skills, shadcn open code, Carbon MCP, Shopify AI toolkit, official GSAP skills, and upstream docs as applicable.
- [ ] Run GREEN and commit.

### Task 5: Skill owners and graph
**Files:** Create eight `skills/*/SKILL.md`; modify `skills/skill-graph.json`, `knowledge/v7-skill-manifest.json`, and deepen selected consumers: `routing-ui-work`, `researching-visual-references`, `researching-ui-implementation-ecosystems`, `designing-motion`, `crafting-typography`, `critiquing-visual-design`, `critiquing-aesthetic-adequacy`, `iterating-rendered-visual-design`, `gating-ui-completion`, `selecting-ui-building-blocks`, `adapting-platform-conventions`, `designing-human-ai-interaction`.
- [ ] Write failing graph/contract tests first.
- [ ] Run RED.
- [ ] Add unique skill contracts and graph nodes; no templated duplicate paragraphs.
- [ ] Run GREEN and commit.

### Task 6: V7 completion and repository gates
**Files:** Create `tests/test_completion_v7.py`, `tests/test_v7_repository_gate.py`; modify `src/nolane_ui/validators.py`, `src/nolane_ui/__init__.py`.
**Interfaces:** `validate_v7_completion_evidence(record) -> dict` and extended `validate_repository`.
- [ ] Write failing completion/repository tests.
- [ ] Run RED.
- [ ] Wire authority/concrete/perceptual gates and required files/metrics.
- [ ] Run GREEN and commit.

### Task 7: Adversarial evals and critique closure
**Files:** Create `evals/v7/manifest.json` plus `authority-conflicts`, `concrete-knowledge`, `rendered-perception`, `fast-path` cases; create `docs/V7-CONCRETE-KNOWLEDGE-CLOSURE.md` and `docs/research/UI-AUTHORITY-INTELLIGENCE-V7.md`.
- [ ] Write failing integrity tests for minimum case count, unique ids, expected owners and critique closure coverage.
- [ ] Run RED.
- [ ] Add cases including visual-gallery-as-semantic-authority, Apple-platform-genericization, GOV service without user-research evidence, React-Aria-vs-visual-library conflict, Shopify-generalization, MCP-authority-inflation, screenshot theater, anti-aliasing pixel noise, fast-path obligation loss, and style-database-default convergence.
- [ ] Run GREEN and commit.

### Task 8: Release integration
**Files:** Modify `README.md`, `docs/USAGE.md`, `AGENTS.md`, `pyproject.toml`, `nui.config.json`, `scripts/nui-release-packet`, `.github/workflows/verify.yml`; add `artifacts/v7-completion-packet.example.json`.
- [ ] Write/update tests that require version 0.7.0 and v7 release artifacts.
- [ ] Run targeted RED.
- [ ] Implement release wiring and v7 CI artifact names.
- [ ] Run full suite, validator, release packet, `git diff --check`, and commit.
