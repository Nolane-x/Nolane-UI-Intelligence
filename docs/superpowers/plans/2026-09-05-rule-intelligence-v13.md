# NUI V13 Rule Intelligence Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build the V13 Rule Intelligence foundation: typed/sharded canonical rules, provenance, deterministic anti-duplication, capability truth, unified current-head validation, coherent versioning, and first-class Python/MCP access.

**Architecture:** Keep V11 runtime as evidence authority and V12 reality rules as a compatibility source. Add a focused `rules_v13` package that normalizes/migrates V12, validates richer contracts, evaluates deterministic similarity, and composes shards without imposing a count quota. Extend the current validator/API/MCP surfaces rather than introducing a competing lifecycle.

**Tech Stack:** Python 3.10+ standard library, unittest, existing NUI JSON/schema conventions, optional MCP unchanged.

**Spec:** `docs/superpowers/specs/2026-09-05-rule-intelligence-v13-design.md`

## Global Constraints

- Package/current config version becomes exactly `0.13.0`.
- Core remains dependency-free.
- `advisory`, `aesthetic`, and `convergence` rules can never block.
- Missing detector capability remains unknown/unsupported, never a false PASS.
- V10 efficacy claim ceiling remains `STRUCTURAL_ONLY` without real-model evidence.
- No rule-count quota or minimum-per-shard validator is allowed.
- External research informs provenance/mechanisms only; V13 implementation and wording remain independently authored.

---

### Task 1: V13 contracts and provenance

**Files:**
- Create: `src/nolane_ui/rules_v13/__init__.py`
- Create: `src/nolane_ui/rules_v13/contracts.py`
- Create: `src/nolane_ui/rules_v13/provenance.py`
- Test: `tests/test_rules_v13_contracts.py`

**Interfaces:**
- Produces: `validate_rule_v13(rule) -> dict`, `validate_catalog_v13(record) -> dict`, `validate_provenance_ledger_v13(record) -> dict`, constants for classes, enforcement, evidence/capability vocabularies.

- [ ] Write tests that reject missing operational fields, placeholder-strength prose, invalid class/enforcement combinations, invalid capability states, and malformed provenance.
- [ ] Run CI and confirm RED because `nolane_ui.rules_v13` does not exist.
- [ ] Implement the minimum validators and typed vocabularies.
- [ ] Run CI and confirm Task 1 tests GREEN.

### Task 2: Deterministic anti-duplication court

**Files:**
- Create: `src/nolane_ui/rules_v13/similarity.py`
- Test: `tests/test_rules_v13_similarity.py`

**Interfaces:**
- Consumes: V13 rule dictionaries.
- Produces: `compare_rule_similarity(left, right) -> dict`, `audit_catalog_similarity(rules) -> dict`.

- [ ] Write adversarial tests for exact duplicate text, noun-substitution duplicates, duplicated failure/repair/verification signatures, and boilerplate concentration.
- [ ] Write controls proving legitimate accessibility/recovery near-neighbors remain distinct.
- [ ] Run CI and confirm RED.
- [ ] Implement normalization, token/character shingles and strict duplicate thresholds using only stdlib.
- [ ] Run CI and confirm GREEN.

### Task 3: V12 compatibility and first canonical V13 shards

**Files:**
- Create: `src/nolane_ui/rules_v13/compat_v12.py`
- Create: `src/nolane_ui/rules_v13/shards/__init__.py`
- Create: `src/nolane_ui/rules_v13/shards/foundation.py`
- Create: `src/nolane_ui/rules_v13/catalog.py`
- Create: `knowledge/rule-provenance-v13.json`
- Test: `tests/test_rules_v13_catalog.py`

**Interfaces:**
- Produces: `normalize_v12_rule(rule)`, `load_rule_catalog_v13(root)`, `query_rules_v13(...)`, `get_rule_v13(rule_id)`.

- [ ] Test lossless authority normalization of representative V12 mechanical/contextual rules.
- [ ] Test convergence rules cannot block and carry capability/provenance metadata.
- [ ] Test catalog validation + similarity audit succeeds for canonical shards.
- [ ] Run CI RED.
- [ ] Implement compatibility adapter and an independently authored mixed foundation shard covering reality + convergence examples from the supplied corpus without copying its wording.
- [ ] Run CI GREEN.

### Task 4: Unified current-head integrity court and version coherence

**Files:**
- Modify: `src/nolane_ui/validators.py`
- Modify: `pyproject.toml`
- Modify: `nui.config.json`
- Test: `tests/test_rules_v13_repository.py`

**Interfaces:**
- Current `validate_repository(root)` additionally reports V11 runtime, V12 reality, V13 catalog/provenance/similarity, and version-coherence metrics.

- [ ] Write tests proving version mismatch blocks current-head validation and invalid V13 catalog/provenance blocks repository validity.
- [ ] Run CI RED.
- [ ] Implement current-head extension without changing historical V10 efficacy semantics.
- [ ] Set package/config version to `0.13.0`.
- [ ] Run CI GREEN.

### Task 5: Public API and bounded MCP exposure

**Files:**
- Modify: `src/nolane_ui/__init__.py`
- Modify: `src/nolane_ui/mcp_server.py`
- Test: `tests/test_rules_v13_api_mcp.py`

**Interfaces:**
- Export top-level V13 aliases for catalog status/query/get/provenance/capability explanation.
- MCP adds read-only `nui_rule_status`, `nui_get_rule`, `nui_query_rules`, `nui_rule_provenance`, and `nui_runtime_doctor` tools.

- [ ] Write tests for exact tool catalog entries and bounded lookup/query behavior.
- [ ] Run CI RED.
- [ ] Implement aliases and MCP tools with no new permissions.
- [ ] Run CI GREEN.

### Task 6: V12.1 fingerprint completeness

**Files:**
- Modify: `src/nolane_ui/external_ui_execution.py`
- Test: `tests/test_rules_v13_reference_fingerprint.py`

**Interfaces:**
- Existing task fingerprint changes when any routing-significant dimension changes.

- [ ] Add tests that independently mutate platform, modalities, temporal behavior, social context, named source, adoption intent, rich interaction, evidence capabilities, stack, visual ambition, and material UI state.
- [ ] Run CI RED for currently unbound dimensions.
- [ ] Extend canonical fingerprint payload deterministically.
- [ ] Run CI GREEN.

### Task 7: Documentation/current-truth cleanup and CI matrix

**Files:**
- Modify: `README.md`
- Modify: `README-VN.md`
- Modify: `README-CN.md`
- Modify: `docs/USAGE.md`
- Modify: `.github/workflows/verify.yml`
- Test: `tests/test_rules_v13_current_truth.py`

**Interfaces:**
- Current docs derive/count current graph truth consistently; historical documents remain historical.
- Core deterministic tests run on Python 3.10, 3.11 and 3.12; heavy Playwright smoke may remain on one supported runtime.

- [ ] Write tests rejecting stale current-system version/skill-count badges in current docs.
- [ ] Run CI RED.
- [ ] Update current docs and split lightweight Python-version matrix from heavy live-browser job as needed.
- [ ] Run CI GREEN.

### Task 8: First-wave rule authoring expansion and adversarial quality gate

**Files:**
- Create focused shards under `src/nolane_ui/rules_v13/shards/`
- Extend: `knowledge/rule-provenance-v13.json`
- Test: `tests/test_rules_v13_authorship_quality.py`

**Interfaces:**
- New rules must pass full contract, similarity, provenance and capability validation.

- [ ] Add tests that forbid a quota field, reject high boilerplate concentration, and require distinct operational signatures across newly authored rules.
- [ ] Author a substantial first wave of independent rules across multiple domains, using the uploaded corpus as research input and the existing NUI graph as owner authority.
- [ ] Run full CI.
- [ ] Record exact branch-head validation metrics and remaining corpus-authoring work without claiming >1000 until the repository actually contains >1000 validated distinct rules.

## Plan self-review

- Spec coverage: contracts, provenance, similarity, sharding, V12 compatibility, detector-capability truth, unified validator, version coherence, API/MCP, fingerprint, docs/CI, and staged authoring are all assigned.
- No task requires a rule-count quota.
- No production behavior is scheduled before its failing test.
- V11 runtime and V10 empirical boundaries remain authoritative in their existing domains.