# UX Intelligence v2 Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build an end-to-end UX verification layer that promotes selected UX reasoning capabilities into canonical skills, binds them to provenance, models user journeys explicitly, consumes V11-compatible observations, and returns deterministic UX findings.

**Architecture:** UX v2 extends the existing `nolane_ui.ux_intelligence` package without replacing v1. It adds a selective canonical-skill bridge, immutable provenance ledger, structured journey validation, deterministic rule evaluators, a verifier, and namespaced Python/MCP surfaces while reusing V11 provider-neutral runtime observations and preserving V13 authority boundaries.

**Tech Stack:** Python 3.10+, standard-library `unittest`, existing NUI catalog/MCP patterns, Markdown canonical skills, GitHub Actions.

**Spec:** `docs/superpowers/specs/2026-09-06-ux-intelligence-v2-design.md`

## Global Constraints

- Scale by semantic novelty, never by count.
- Do not create a second browser/runtime stack.
- Do not promote all 32 v1 registry entries automatically.
- UX findings must inherit rule mechanism/severity/enforcement rather than creating authority ad hoc.
- Missing evidence yields `insufficient-evidence`, never an inferred failure.
- Fuzzy similarity is never an automatic blocking criterion in v2.
- V13 canonical-rule authority remains separate from UX v2.
- Public query limits remain integers in the inclusive range 1..100 and reject `bool`.
- Use standard-library `unittest`; preserve existing CI behavior.

---

### Task 1: Canonical UX skill bridge

**Files:**
- Create: `src/nolane_ui/ux_intelligence/canonical_bridge.py`
- Create: six `skills/<slug>/SKILL.md` files named in the spec
- Create: `tests/test_ux_intelligence_v2_bridge.py`
- Modify: `src/nolane_ui/ux_intelligence/catalog.py`
- Modify: `src/nolane_ui/ux_intelligence/__init__.py`

**Interfaces:**
- Consumes: `UX_SKILLS` from `skills.py`.
- Produces: `UX_CANONICAL_SKILL_BRIDGE`, `get_ux_canonical_skill_bridge(skill_id)`, `query_ux_canonical_skill_bridge(*, mechanism_id=None, limit=100)`.

- [ ] **Step 1: Write failing bridge tests**

```python
class UXCanonicalBridgeTests(unittest.TestCase):
    def test_bridge_is_selective_and_resolves_registry_entries(self):
        ids = {item["skill_id"] for item in UX_CANONICAL_SKILL_BRIDGE}
        self.assertEqual(ids, {
            "identifying-user-goals",
            "mapping-critical-user-journeys",
            "conducting-cognitive-walkthroughs",
            "testing-mental-model-alignment",
            "assessing-recovery-completeness",
            "evaluating-task-success",
        })
        self.assertLess(len(ids), len(UX_SKILLS))

    def test_supported_mechanisms_are_registry_subset(self):
        skills = {item["skill_id"]: item for item in UX_SKILLS}
        for item in UX_CANONICAL_SKILL_BRIDGE:
            self.assertTrue(set(item["supported_mechanisms"]) <= set(skills[item["skill_id"]]["related_mechanisms"]))
```

- [ ] **Step 2: Run RED**

Run: `PYTHONPATH=src python -m unittest tests.test_ux_intelligence_v2_bridge -v`

Expected: import/module failure because the bridge does not exist yet.

- [ ] **Step 3: Implement explicit bridge records and validators**

Use literal tuple records; no generation loops. Each record contains the fields defined by the spec and names one canonical skill path.

- [ ] **Step 4: Add six canonical `SKILL.md` nodes**

Each skill document must expose goal, reasoning procedure, required outputs, evidence discipline, anti-patterns, and mechanism coverage. Keep them operational rather than duplicating registry prose.

- [ ] **Step 5: Run focused GREEN**

Run: `PYTHONPATH=src python -m unittest tests.test_ux_intelligence_v2_bridge -v`

Expected: all bridge tests pass.

- [ ] **Step 6: Commit**

```bash
git add src/nolane_ui/ux_intelligence skills tests/test_ux_intelligence_v2_bridge.py
git commit -m "feat: bridge UX cognition into canonical skills"
```

### Task 2: UX provenance ledger

**Files:**
- Create: `src/nolane_ui/ux_intelligence/provenance.py`
- Create: `tests/test_ux_intelligence_v2_provenance.py`
- Modify: `src/nolane_ui/ux_intelligence/catalog.py`
- Modify: `src/nolane_ui/ux_intelligence/__init__.py`

**Interfaces:**
- Produces: `UX_PROVENANCE`, `get_ux_provenance(provenance_id)`, `query_ux_provenance(*, source_kind=None, verification_mode=None, text=None, limit=100)`.

- [ ] **Step 1: Write failing provenance tests**

```python
class UXProvenanceTests(unittest.TestCase):
    def test_records_have_transfer_boundaries_and_contraindications(self):
        for record in UX_PROVENANCE:
            self.assertTrue(record["transfer_boundaries"])
            self.assertTrue(record["contraindications"])
            self.assertTrue(record["verification_modes"])

    def test_missing_id_returns_none_and_queries_are_defensive(self):
        self.assertIsNone(get_ux_provenance("missing"))
        rows = query_ux_provenance(limit=1)
        rows[0]["title"] = "mutated"
        self.assertNotEqual(query_ux_provenance(limit=1)[0]["title"], "mutated")
```

- [ ] **Step 2: Run RED**

Expected: missing provenance API.

- [ ] **Step 3: Add explicit evidence records**

Seed only records needed by v2 evaluator semantics, including product-contract evidence for journey transition expectations and runtime-observation evidence for V11-derived UI state.

- [ ] **Step 4: Add deterministic validation/query helpers**

Validate unique/sorted IDs, allowed source kinds/statuses, non-empty transfer boundaries/contraindications, and query limits 1..100.

- [ ] **Step 5: Run focused GREEN and commit**

Run: `PYTHONPATH=src python -m unittest tests.test_ux_intelligence_v2_provenance -v`

### Task 3: Structured journey contracts

**Files:**
- Create: `src/nolane_ui/ux_intelligence/journeys.py`
- Create: `tests/test_ux_intelligence_v2_journeys.py`

**Interfaces:**
- Produces: `validate_ux_journey_spec(journey) -> dict`, `normalize_ux_journey_spec(journey) -> dict`.
- A normalized step always contains `step_id`, `intent`, `action`, `expected_transition`, `required_context`, `preserved_context`, `allowed_detours`, `recovery_expectation`, and `evidence_requirements`.

- [ ] **Step 1: Write RED validation tests**

Cover valid journey, duplicate step IDs, missing success criteria, unresolved provenance, empty critical state, and invalid evidence requirement shapes.

- [ ] **Step 2: Implement deterministic schema validation**

Reject malformed journey content with `TypeError` for wrong primitive/container types and `ValueError` for invalid domain values/references.

- [ ] **Step 3: Add normalization without inference**

Normalization may canonicalize tuples/strings and defensive-copy data but must not invent expected transitions or evidence requirements.

- [ ] **Step 4: Run focused GREEN and commit**

Run: `PYTHONPATH=src python -m unittest tests.test_ux_intelligence_v2_journeys -v`

### Task 4: Deterministic UX evaluators

**Files:**
- Create: `src/nolane_ui/ux_intelligence/evaluators.py`
- Create: `tests/test_ux_intelligence_v2_verifier.py`

**Interfaces:**
- Produces: `UX_JOURNEY_EVALUATORS` and evaluator functions returning one of `pass`, `fail`, `insufficient-evidence`, `not-executed` plus evidence detail.

- [ ] **Step 1: Write evaluator RED tests**

At minimum cover:

```python
self.assertEqual(result["status"], "insufficient-evidence")  # required runtime field absent
self.assertEqual(result["status"], "fail")                   # false completion proven
self.assertEqual(result["status"], "fail")                   # context proven lost
self.assertEqual(result["status"], "fail")                   # dead-end recovery absent
self.assertEqual(result["status"], "pass")                   # evidence satisfies expected transition
```

- [ ] **Step 2: Implement explicit evaluator registry**

Each evaluator record declares `rule_id`, `required_evidence`, and function identity. Resolve all rule IDs against `UX_RULES` and inherit rule mechanism/severity/enforcement at finding construction time.

- [ ] **Step 3: Implement only deterministic predicates**

Do not add free-text similarity or probabilistic rule matching. Evaluators consume structured observation fields and journey expectations.

- [ ] **Step 4: Run focused GREEN and commit**

### Task 5: Journey verifier

**Files:**
- Create: `src/nolane_ui/ux_intelligence/verifier.py`
- Extend: `tests/test_ux_intelligence_v2_verifier.py`

**Interfaces:**
- Produces: `verify_ux_journey(journey, observations, *, rule_catalog=UX_RULES, provenance_catalog=UX_PROVENANCE) -> dict`.

- [ ] **Step 1: Add RED end-to-end tests**

Include one complete passing journey and one mixed journey where missing evidence does not become a failure.

- [ ] **Step 2: Implement observation indexing by step**

Support provider-neutral mappings only. Reject Playwright-specific objects at the UX boundary.

- [ ] **Step 3: Implement derived journey status**

`failed` outranks `insufficient-evidence`; `passed` requires all critical checks and success criteria to pass.

- [ ] **Step 4: Construct findings from rule authority**

Finding `mechanism_id`, `severity`, and `enforcement` come directly from the referenced UX rule.

- [ ] **Step 5: Run focused GREEN and commit**

### Task 6: Public Python and MCP integration

**Files:**
- Modify: `src/nolane_ui/ux_intelligence/__init__.py`
- Modify: `src/nolane_ui/__init__.py`
- Modify: `src/nolane_ui/mcp_server.py`
- Create: `tests/test_ux_intelligence_v2_api_mcp.py`

**Interfaces:**
- Top-level exports: all v2 constants/getters/query/verify/status APIs named in the spec.
- MCP tools: `nui_ux_v2_status`, `nui_get_ux_provenance`, `nui_query_ux_provenance`, `nui_get_ux_canonical_skill_bridge`, `nui_query_ux_canonical_skill_bridge`, `nui_verify_ux_journey`.

- [ ] **Step 1: Write integration RED tests**

Assert imports fail before production wiring and that MCP catalog lacks the v2 tools.

- [ ] **Step 2: Wire top-level exports**

Preserve every v1/V13/runtime export.

- [ ] **Step 3: Add read/verify MCP wrappers**

Missing exact IDs raise `ValueError`. Verify tool returns report data and performs no writes.

- [ ] **Step 4: Register FastMCP tools and metadata**

Keep distinct UX namespace descriptions so no tool is presented as V13 authority.

- [ ] **Step 5: Run integration GREEN and commit**

Run: `PYTHONPATH=src python -m unittest tests.test_ux_intelligence_v2_api_mcp -v`

### Task 7: Quality court and regression closure

**Files:**
- Modify: `src/nolane_ui/ux_intelligence/catalog.py`
- Extend: all v2 tests as needed

**Interfaces:**
- Produces: `ux_v2_status()` with bridge/provenance/evaluator/journey-support counts and integrity diagnostics, all descriptive rather than quota targets.

- [ ] **Step 1: Add RED tests for invalid semantic contracts**

Mutate copies to prove rejection of unresolved bridge IDs, unsupported mechanisms, unresolved provenance, unresolved evaluator rules, duplicate step IDs, blocking contextual/convergence authority, and finding rule/mechanism mismatch.

- [ ] **Step 2: Implement the minimal validators**

Keep fuzzy similarity non-blocking and preserve v1 exact operational-signature court.

- [ ] **Step 3: Run focused v1+v2 suites**

Run:

```bash
PYTHONPATH=src python -m unittest \
  tests.test_ux_intelligence_v1 \
  tests.test_ux_intelligence_v1_api_mcp \
  tests.test_ux_intelligence_v2_bridge \
  tests.test_ux_intelligence_v2_provenance \
  tests.test_ux_intelligence_v2_journeys \
  tests.test_ux_intelligence_v2_verifier \
  tests.test_ux_intelligence_v2_api_mcp -v
```

Expected: all focused tests GREEN.

- [ ] **Step 4: Run local full discovery**

Run: `PYTHONPATH=src python -m unittest discover -s tests`

If the only failure is the known local missing-browser executable condition, record it exactly and rely on the official dedicated Chromium CI job for browser proof. Any other failure is a real regression and must be fixed before continuing.

### Task 8: Remote CI and delivery gate

**Files:**
- Update plan checkboxes/evidence after verification.
- No production change unless CI identifies a defect.

- [ ] **Step 1: Push final implementation head and open a draft PR**

Use `feat/ux-intelligence-v2` -> `main` with an evidence-oriented PR body.

- [ ] **Step 2: Read final-head GitHub Actions jobs**

Require success for Core Python 3.10, 3.11, 3.12, Real Chromium runtime, and current-head release gate.

- [ ] **Step 3: Inspect failures before patching**

Fetch exact failed job logs and root-cause them; do not rerun blindly.

- [ ] **Step 4: Final self-review**

Verify no authority mixing, no quota language, no generated rule loops, no fuzzy automatic blocking, no removal of v1 APIs, and no false empirical claim.

- [ ] **Step 5: Update PR body with final evidence**

Only after final-head CI is green, record RED->GREEN evidence and exact run/job conclusions. Leave merge to an explicit user instruction.
