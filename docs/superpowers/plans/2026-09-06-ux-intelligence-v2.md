# UX Intelligence v2 Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build an end-to-end UX verification layer that binds selected fine-grained UX reasoning operations to existing canonical NUI skills, adds bounded provenance, models journeys explicitly, consumes V11-compatible observations, and returns deterministic UX-rule findings.

**Architecture:** UX v2 extends `nolane_ui.ux_intelligence` without modifying v1 catalogs. It uses a selective read-only bridge into the existing canonical skill graph, a provenance ledger, structured journey validation, explicit rule evaluators, a provider-neutral verifier, and namespaced Python/MCP surfaces. Browser transport remains owned by V11; V13 authority remains separate.

**Tech Stack:** Python 3.10+, standard-library `unittest`, existing NUI catalog/MCP patterns, canonical skill graph/Markdown files, GitHub Actions.

**Spec:** `docs/superpowers/specs/2026-09-06-ux-intelligence-v2-design.md`

## Global Constraints

- Scale by semantic novelty, never by count.
- Bridge to an existing canonical skill when semantic coverage exists; do not mint a duplicate node.
- Do not create a second browser/runtime stack.
- Do not promote all 32 v1 registry entries automatically.
- UX findings inherit rule mechanism/severity/enforcement; evaluators never create authority ad hoc.
- Missing evidence yields `insufficient-evidence`, never inferred failure.
- Fuzzy similarity is never an automatic blocker in v2.
- V13 canonical-rule authority remains separate.
- Public query limits are integers 1..100 inclusive and reject `bool`.
- Use standard-library `unittest`; preserve existing CI behavior.

---

### Task 1: Selective canonical UX skill bridge

**Files:**
- Create: `src/nolane_ui/ux_intelligence/canonical_bridge.py`
- Test: `tests/test_ux_intelligence_v2_bridge.py`
- Read-only dependency: `skills/skill-graph.json` and existing `skills/<canonical-slug>/SKILL.md`
- Modify: `src/nolane_ui/ux_intelligence/__init__.py`

**Interfaces:**
- Consumes: `UX_SKILLS`.
- Produces: `UX_CANONICAL_SKILL_BRIDGE`, `get_ux_canonical_skill_bridge`, `query_ux_canonical_skill_bridge`, `validate_ux_canonical_skill_bridge`.

- [x] Define contract tests before production module.
- [x] Implement six explicit cognition -> existing-canonical-skill bindings with no generation loop.
- [x] Validate UX skill resolution, canonical record shape, mechanism compatibility, sorting, quotas, query limits, and defensive copies.
- [x] Add checkout-level test proving every target slug exists in `skill-graph.json`, every target path exists, and the target `SKILL.md` declares its canonical name.
- [ ] Run focused bridge test GREEN on final code.

### Task 2: UX provenance ledger

**Files:**
- Create: `src/nolane_ui/ux_intelligence/provenance.py`
- Test: `tests/test_ux_intelligence_v2_provenance.py`
- Modify: `src/nolane_ui/ux_intelligence/__init__.py`

**Interfaces:**
- Produces: `UX_PROVENANCE`, `get_ux_provenance`, `query_ux_provenance`, `validate_ux_provenance`.

- [x] Define provenance contract tests before implementation.
- [x] Add only the provenance required by v2: product journey contract, UX-rule authority inheritance, and V11 runtime-observation boundary.
- [x] Require transfer boundaries, contraindications, verification modes, unique/sorted IDs, valid source/status values, defensive reads and bounded queries.
- [ ] Run focused provenance test GREEN on final code.

### Task 3: Structured journey contracts

**Files:**
- Create: `src/nolane_ui/ux_intelligence/journeys.py`
- Test: `tests/test_ux_intelligence_v2_journeys.py`

**Interfaces:**
- Produces: `validate_ux_journey_spec(journey) -> dict`, `normalize_ux_journey_spec(journey) -> dict`.

- [x] Define valid/invalid journey contract tests before implementation.
- [x] Validate required journey/step fields, duplicate step IDs, non-empty success criteria and critical state, and provenance references.
- [x] Normalize sequence containers and defensive copies without inventing semantics.
- [ ] Run focused journey test GREEN on final code.

### Task 4: Deterministic UX evaluator registry

**Files:**
- Create: `src/nolane_ui/ux_intelligence/evaluators.py`
- Test/extend: `tests/test_ux_intelligence_v2_verifier.py`, `tests/test_ux_intelligence_v2_quality_court.py`

**Interfaces:**
- Produces: `UX_JOURNEY_EVALUATORS`, `evaluate_ux_journey_rule`, `validate_ux_journey_evaluators`.

- [x] Bind ten deterministic evaluators to existing v1 UX rule IDs only.
- [x] Separate `activation_evidence` from `required_evidence` so irrelevant checks become `not-executed` and incomplete activated checks become `insufficient-evidence`.
- [x] Reject unresolved rules/provenance and duplicate evaluator/rule bindings.
- [x] Prevent contextual/convergence rules from gaining blocking authority.
- [x] Keep fuzzy/NLP matching outside the blocking path.
- [ ] Run evaluator/quality-court tests GREEN on final code.

### Task 5: Provider-neutral journey verifier

**Files:**
- Create: `src/nolane_ui/ux_intelligence/verifier.py`
- Test: `tests/test_ux_intelligence_v2_verifier.py`

**Interfaces:**
- Produces: `verify_ux_journey(journey, observations, *, rule_catalog=UX_RULES, provenance_catalog=UX_PROVENANCE) -> dict`.

- [x] Accept plain step-scoped observation mappings/records and no Playwright-specific objects.
- [x] Track expected transitions, incoming/preserved context, evidence gaps, evaluator outcomes, and success criteria.
- [x] Derive journey status with `failed` > `insufficient-evidence` > `passed` precedence.
- [x] Emit UX findings only from existing rules and inherit rule mechanism/severity/enforcement exactly.
- [x] Allow product-contract mismatches to fail a journey without inventing a UX rule finding.
- [ ] Run complete-pass, false-completion, and missing-evidence tests GREEN on final code.

### Task 6: Public Python and MCP integration

**Files:**
- Modify: `src/nolane_ui/ux_intelligence/__init__.py`
- Modify: `src/nolane_ui/__init__.py`
- Modify: `src/nolane_ui/mcp_server.py`
- Test: `tests/test_ux_intelligence_v2_api_mcp.py`

**Interfaces:**
- Top-level v2 exports named in the spec.
- MCP: `nui_ux_v2_status`, `nui_get_ux_provenance`, `nui_query_ux_provenance`, `nui_get_ux_canonical_skill_bridge`, `nui_query_ux_canonical_skill_bridge`, `nui_verify_ux_journey`.

- [x] Wire top-level exports while preserving v1/V13/runtime APIs.
- [x] Add exact lookup/query/verify wrappers with missing IDs raising `ValueError`.
- [x] Register six read/verify FastMCP tools under the UX namespace.
- [x] Keep v2 MCP surfaces non-mutating and distinct from V13 authority.
- [ ] Run public API/MCP regression tests GREEN on final code.

### Task 7: V2 integrity status and regression court

**Files:**
- Create: `src/nolane_ui/ux_intelligence/v2_catalog.py`
- Test: `tests/test_ux_intelligence_v2_status.py`
- Test: `tests/test_ux_intelligence_v2_quality_court.py`

**Interfaces:**
- Produces: `ux_v2_status()` with descriptive integrity dimensions, never quality quotas.

- [x] Compose bridge/provenance/evaluator validators without changing v1 `catalog.py`.
- [x] Report unresolved bridge skills/evaluator rules and explicit no-quota/no-fuzzy-block/no-V13-inheritance boundaries.
- [x] Add mutation tests for unsupported bridge mechanisms, duplicate provenance IDs, and unknown evaluator rules.
- [ ] Run focused v1+v2 regression suite:

```bash
PYTHONPATH=src python -m unittest \
  tests.test_ux_intelligence_v1 \
  tests.test_ux_intelligence_v1_api_mcp \
  tests.test_ux_intelligence_v2_bridge \
  tests.test_ux_intelligence_v2_provenance \
  tests.test_ux_intelligence_v2_journeys \
  tests.test_ux_intelligence_v2_verifier \
  tests.test_ux_intelligence_v2_api_mcp \
  tests.test_ux_intelligence_v2_quality_court \
  tests.test_ux_intelligence_v2_status -v
```

- [ ] Run full repository discovery or use official CI as the authoritative full-repo environment when local checkout/browser dependencies are unavailable.

### Task 8: Remote CI and delivery gate

**Files:**
- Evidence: `docs/superpowers/evidence/2026-09-06-ux-intelligence-v2-red.md`
- Update this plan and PR body only after evidence exists.

- [x] Open draft PR `#34` from `feat/ux-intelligence-v2` to `main` during the contract-first phase.
- [x] Capture a pull-request workflow for the pre-production contract head: run #1248 / `34021406349` (conclusion still requires reading the finished run).
- [ ] Fetch the exact final branch head after all doc/test cleanup.
- [ ] Require final-head success for Core Python 3.10, 3.11, 3.12, Real Chromium runtime, and current-head release gate.
- [ ] If any job fails, fetch its exact logs and root-cause before patching; never rerun blindly.
- [ ] Final self-review: no authority mixing, quota language, duplicate canonical nodes, generated rule loops, fuzzy automatic blocking, removed v1 API, or false empirical claim.
- [ ] Update PR #34 body with exact RED->GREEN evidence only after final-head CI is green.
- [ ] Leave merge to an explicit user instruction.
