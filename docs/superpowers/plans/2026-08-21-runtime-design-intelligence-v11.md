# NUI V11 Runtime Design Intelligence Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build the first mergeable V11 runtime-design-intelligence slice: a dependency-free, context-aware deterministic UI detector with NUI-native findings, CLI, host-hook capability contracts and browser-observation ingestion, without adding canonical skills.

**Architecture:** Add a focused `nolane_ui.runtime_v11` package beneath the existing cognition/evidence graph. Raw observations are produced by source engines, adjudicated with rule class and explicit exceptions, converted to existing NUI finding semantics, and exposed through `scripts/nui-detect`. Host hooks and browser collection are represented as capability/observation protocols so later live automation extends the kernel instead of duplicating it.

**Tech Stack:** Python 3.10+ standard library only, `unittest`, JSON registries/schemas, existing NUI interop/evidence contracts.

**Spec:** `docs/superpowers/specs/2026-08-21-runtime-design-intelligence-v11-design.md`

## Global Constraints

- Add zero canonical skills and do not modify `skills/skill-graph.json`.
- Do not touch `design/ui-industry-1000-batch-006` or its skill inventory.
- Keep the runtime core dependency-free.
- Deterministic findings are evidence, never independent release certification.
- Genericness/advisory rules may not silently become hard edit blockers.
- Reimplement mechanisms independently; do not copy Impeccable source code or rule wording.
- All production behavior follows test-first red/green development.

---

### Task 1: Runtime contracts and rule registry validator

**Files:**
- Create: `src/nolane_ui/runtime_v11/__init__.py`
- Create: `src/nolane_ui/runtime_v11/contracts.py`
- Create: `src/nolane_ui/runtime_v11/registry.py`
- Create: `knowledge/runtime-detector-rules-v11.json`
- Create: `tests/test_runtime_v11_registry.py`

**Interfaces:**
- Produces: `validate_rule_registry(record: dict) -> dict`, `load_rule_registry(root: Path | str) -> dict`, stable class/tier/engine constants.

- [ ] Write failing registry tests covering duplicate IDs, missing falsifier/provenance, invalid class/tier/engine, edit-block safety and valid registry loading.
- [ ] Run `python -m unittest tests.test_runtime_v11_registry -v` and confirm failures are caused by the missing runtime package.
- [ ] Implement contracts/registry validation and a hand-authored initial registry with at least 10 rules across runtime-integrity, accessibility-mechanics, layout-integrity, design-system-integrity and genericness.
- [ ] Re-run the focused test and confirm PASS.

### Task 2: Source observation engines and NUI finding conversion

**Files:**
- Create: `src/nolane_ui/runtime_v11/detector.py`
- Create: `tests/test_runtime_v11_detector.py`
- Create: `tests/fixtures/runtime_v11/clean.html`
- Create: `tests/fixtures/runtime_v11/defects.html`
- Create: `tests/fixtures/runtime_v11/clean.tsx`
- Create: `tests/fixtures/runtime_v11/defects.tsx`

**Interfaces:**
- Consumes: validated registry from Task 1.
- Produces: `scan_text(text, path, registry, *, tier='session', context=None) -> list[dict]`, `scan_path(path, registry, *, tier='session', context=None) -> dict`.

- [ ] Write failing detector tests for positive, negative and counterexample fixtures, stable ordering, deduplication and complete NUI finding fields.
- [ ] Run the focused detector tests and verify RED.
- [ ] Implement bounded text/markup source observations for the initial registry. Every match records engine and concrete evidence; no AST certainty is claimed.
- [ ] Re-run registry + detector tests and confirm PASS.

### Task 3: Context-aware adjudication and narrow exceptions

**Files:**
- Create: `src/nolane_ui/runtime_v11/adjudication.py`
- Create: `tests/test_runtime_v11_adjudication.py`

**Interfaces:**
- Produces: `adjudicate_match(match, rule, context=None, exceptions=None) -> dict`, returning disposition `finding | accepted-exception | unknown`.

- [ ] Write failing tests proving contextual rules can become `unknown`, explicit scoped authority can accept an exception, broad implicit suppression is rejected, and revision/file/value scope is preserved.
- [ ] Run focused tests and verify RED.
- [ ] Implement adjudication and connect it to detector output without weakening mechanical rules.
- [ ] Re-run Tasks 1–3 tests and confirm PASS.

### Task 4: CLI `nui-detect`

**Files:**
- Create: `src/nolane_ui/runtime_v11/cli.py`
- Create: `scripts/nui-detect`
- Create: `tests/test_runtime_v11_cli.py`

**Interfaces:**
- Produces: `main(argv=None) -> int` and JSON batch output with `valid`, `target`, `tier`, `finding_count`, `findings`, `unknowns`, `accepted_exceptions`.

- [ ] Write failing CLI tests for clean file exit 0, findings exit 2, invalid target exit 1, JSON shape and directory extension filtering.
- [ ] Run focused tests and verify RED.
- [ ] Implement CLI with no network access and deterministic ordering.
- [ ] Re-run Tasks 1–4 tests and confirm PASS.

### Task 5: Hook capability contract and interop projection

**Files:**
- Create: `src/nolane_ui/runtime_v11/hooks.py`
- Create: `tests/test_runtime_v11_hooks.py`
- Modify: `src/nolane_ui/interop.py`
- Modify: `tests/test_agent_adapters_v7.py`

**Interfaces:**
- Produces: `build_hook_capability(agent_id: str) -> dict` with explicit support for pre-write, post-write, session-stop, blocking and context-return semantics.
- Extends: `build_agent_install_plan()` with a `runtime_detection` field pointing to `python scripts/nui-detect` and canonical hook capabilities.

- [ ] Write failing hook tests proving no adapter claims unsupported blocking/stop behavior and every projection uses the same canonical detector entrypoint.
- [ ] Run hook/interop tests and verify RED.
- [ ] Implement the capability matrix and thin interop projection metadata only; do not install host manifests yet.
- [ ] Re-run hook + existing adapter tests and confirm PASS.

### Task 6: Browser-observation protocol and ingestion validation

**Files:**
- Create: `src/nolane_ui/runtime_v11/browser.py`
- Create: `schemas/runtime-browser-observation-v11.schema.json`
- Create: `tests/test_runtime_v11_browser.py`

**Interfaces:**
- Produces: `validate_browser_observation(record: dict) -> dict`, `normalize_browser_observation(record: dict) -> dict`.

- [ ] Write failing tests for viewport/location/runtime-error/computed-style evidence, malformed geometry, absent capture references and capability-limited observations.
- [ ] Run focused tests and verify RED.
- [ ] Implement protocol validation/normalization with no browser dependency.
- [ ] Re-run Tasks 1–6 tests and confirm PASS.

### Task 7: Public exports, repository validation and documentation

**Files:**
- Modify: `src/nolane_ui/__init__.py`
- Modify: `README.md`
- Modify: `docs/AGENT-INTEGRATION.md`
- Create: `docs/research/impeccable-runtime-mechanism-transfer-v11.md`
- Create: `tests/test_runtime_v11_integration.py`

**Interfaces:**
- Exposes stable runtime APIs through `nolane_ui` without changing canonical skill ownership.

- [ ] Write an integration test asserting imports, registry validity, zero skill-count coupling and install-plan detector exposure.
- [ ] Verify the integration test fails before exports/docs integration.
- [ ] Add public exports and concise docs. Record Impeccable as an Apache-2.0 mechanism source and explicitly state that V11 implementation/rule wording is independently authored.
- [ ] Run `python -m unittest discover -s tests -v`.
- [ ] Run `python scripts/nui-validate .`.
- [ ] Do not claim completion unless both commands pass on the feature head.

## Plan self-review

- Spec coverage: Tasks 1–4 cover kernel/CLI/adjudication; Task 5 covers hook architecture; Task 6 fixes the browser-driver boundary; Task 7 covers provenance/integration. Live Lab and full doctor are deliberately deferred by the approved spec.
- No placeholders: all production interfaces and test expectations needed for this first slice are named above.
- Type consistency: registry → detector → adjudication → CLI all use dictionaries compatible with the existing NUI JSON/evidence style; hook/browser protocols remain provider-neutral.
