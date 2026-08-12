# Nolane UI Intelligence v1 Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build a platform-agnostic, depth-locked UI/UX Agent Skill system with routing, design faculties, deterministic verification, adversarial critics, runtime adapters, and evidence-gated completion.

**Architecture:** A universal cognitive kernel owns lifecycle, authority, routing, obligations, evidence, recovery, and completion. Narrow design skills provide judgment; Python validators own deterministic invariants; adapters translate generic capabilities to agent runtimes. The implementation is intentionally modular so only task-relevant skills enter context.

**Tech Stack:** Agent Skills Markdown/YAML, JSON contracts and fixtures, Python 3 standard library, unittest, GitHub Actions.

## Global Constraints
- Universal core MUST NOT depend on a single runtime or UI framework.
- Skill frontmatter descriptions MUST begin with `Use when...` and describe triggers, not workflows.
- Missing evidence MUST resolve to `UNKNOWN`/`BLOCKED`, never inferred PASS.
- Deterministic invariants MUST be validated by code when feasible.
- Third-party skill text MUST NOT be bulk-copied; mechanisms are synthesized and sources recorded.
- Normative standards and explicit product requirements outrank community heuristics.
- A design MUST NOT certify itself for material completion.
- No `TODO`, `TBD`, placeholder skills, or generated filler are permitted in v1.

---

### Task 1: Repository contract and skill graph
**Files:** create `README.md`, `AGENTS.md`, `pyproject.toml`, `nui.config.json`, `skills/skill-graph.json`, `schemas/*.json`.

**Interfaces:** produces canonical lifecycle states, parent-child skill graph, typed task profile, finding, evidence, obligation, and completion-packet shapes.

- [ ] Write tests/fixtures that fail when required graph nodes, lifecycle states, or schema fields are absent.
- [ ] Verify the tests fail against the empty implementation.
- [ ] Implement repository metadata, graph, and schemas.
- [ ] Run the structural tests to green.
- [ ] Commit the repository contract.

### Task 2: Mandatory cognitive kernel skills
**Files:** create the nine kernel `skills/*/SKILL.md` files.

**Interfaces:** consumes task input and graph contracts; produces typed UI contract, routing decision, obligations, evidence ledger entries, findings, recovery records, and completion decisions.

- [ ] Add pressure fixtures for direct-to-code, self-certification, missing-evidence, and bypass attempts.
- [ ] Record expected baseline failures in `evals/pressure/baselines.md`.
- [ ] Write each kernel skill with one responsibility, parent contract, observable procedure, typed return, stop conditions, rationalization counters, quick reference, and common failures.
- [ ] Validate all skill metadata and graph edges.
- [ ] Commit kernel skills.

### Task 3: Product, architecture, and interaction faculties
**Files:** create skills for product modeling, information architecture, task flow, interaction design, component semantics, forms, navigation/search, and state modeling.

**Interfaces:** produces product/task model, IA map, flow model, interaction contracts, and applicable state matrices.

- [ ] Add scenario fixtures covering dense enterprise, destructive workflows, search, forms, and expert keyboard use.
- [ ] Write narrow skills that derive structure from user/task constraints before visual styling.
- [ ] Validate skill graph and state-matrix fixtures.
- [ ] Commit product/interaction faculties.

### Task 4: Visual craft and aesthetic intelligence
**Files:** create skills for aesthetic exploration, visual hierarchy, composition, typography, color, spacing/rhythm, depth/material, iconography/imagery, and contextual anti-slop.

**Interfaces:** produces visual-direction candidates, selected rationale, hierarchy map, craft tokens, and contextual findings.

- [ ] Add eval prompts that tempt generic purple-gradient/card-grid UI and style dogma.
- [ ] Write skills that require structurally distinct exploration when valuable and forbid unsupported aesthetic approval.
- [ ] Encode contextual anti-slop: pattern + context + intent + frequency + impact + justification.
- [ ] Commit visual craft faculties.

### Task 5: Design systems, responsive, platform, and inclusive design
**Files:** create skills for token architecture, component systems, responsive/adaptive behavior, platform adaptation, accessibility, localization/RTL, UX writing, and motion.

**Interfaces:** produces token model, component contract, breakpoint/adaptation rules, platform delta, accessibility obligations, locale stress plan, content rules, and motion constraints.

- [ ] Add fixtures for long labels, RTL, narrow viewport, reduced motion, high contrast, keyboard focus, and platform divergence.
- [ ] Implement skills with authority hierarchy and standard-aware obligations.
- [ ] Validate token tiers and state coverage.
- [ ] Commit system/inclusive faculties.

### Task 6: Specialized surfaces and verification critics
**Files:** create dashboard/data-viz, empty/error/loading states, fidelity verification, visual critic, UX critic, accessibility critic, design-system critic, responsive critic, and platform critic skills.

**Interfaces:** produces specialized surface contracts and typed independent findings.

- [ ] Add critic fixtures with known failures and required severity/evidence fields.
- [ ] Implement critics with `may_modify: false` semantics and evidence-first findings.
- [ ] Implement fidelity ledger rules for target-vs-render work.
- [ ] Commit verification faculties.

### Task 7: Deterministic kernel and tests
**Files:** create `src/nolane_ui/*.py`, `tests/*.py`, `scripts/nui-validate`.

**Interfaces:** `validate_repository(root)`, `validate_completion_packet(packet, root)`, `validate_skill_graph(graph, skills)`, `validate_state_matrix(matrix)`, `validate_tokens(tokens)`.

- [ ] Write failing unit tests for missing skill, illegal parent edge, invalid description, unresolved blocker, missing evidence, invalid token tier, and incomplete state matrix.
- [ ] Run tests and confirm correct failures.
- [ ] Implement minimal validators using Python standard library.
- [ ] Run the full unittest suite to green.
- [ ] Commit deterministic kernel.

### Task 8: Runtime adapters and capability model
**Files:** create `adapters/{generic,codex,claude-code,gemini-cli,cursor,opencode}/README.md` and capability mapping JSON.

**Interfaces:** maps generic capabilities such as browser inspection, screenshot capture, file mutation, subagents, component retrieval, and test execution to runtime-specific instructions without changing core semantics.

- [ ] Add adapter completeness test.
- [ ] Implement six adapters and fallback behavior when a capability is absent.
- [ ] Validate adapters.
- [ ] Commit adapters.

### Task 9: Research/source ledger and installation documentation
**Files:** create `docs/research/SOURCES.md`, `docs/research/SYNTHESIS.md`, `docs/INSTALL.md`, `docs/USAGE.md`, `LICENSE`.

**Interfaces:** records source authority, mechanism absorbed, scope, and license caution; documents portable installation.

- [ ] Record authoritative and community sources actually consulted.
- [ ] Distinguish normative guidance from heuristics and copied text from synthesized mechanisms; v1 contains synthesized mechanisms only.
- [ ] Document installation for Agent Skills-compatible runtimes and manual adapter usage.
- [ ] Commit docs.

### Task 10: Evals, self-verification, CI, and release packet
**Files:** create `evals/**/*.json`, `artifacts/v1-completion-packet.json`, `.github/workflows/verify.yml`.

**Interfaces:** repository validator consumes all artifacts and must accept the release packet only after tests and structural checks pass.

- [ ] Add routing, pressure, craft, accessibility, responsive, fidelity, and adversarial eval fixtures.
- [ ] Run unit tests and repository validator.
- [ ] Produce completion packet with bounded claims and fresh evidence references.
- [ ] Re-run validator against the completion packet.
- [ ] Add CI workflow executing the same checks.
- [ ] Commit, review diff, merge to `main`, and verify the resulting main commit.

## Self-review
Coverage: every architecture section in the approved spec maps to at least one task. No placeholder implementation task remains. Interfaces use the same canonical nouns across tasks: task profile, obligation, evidence, finding, state matrix, token model, completion packet. The plan intentionally avoids dependencies beyond Python standard library so verification works in constrained agent runtimes.
