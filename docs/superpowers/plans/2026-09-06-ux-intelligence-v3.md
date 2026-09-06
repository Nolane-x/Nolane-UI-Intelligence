# UX Intelligence v3 Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build the UX Intelligence v3.0 Autonomous UX Scientist foundation: evidence-bounded product/goal models, autonomous journey hypotheses and promotion, observation planning, temporal UX evidence/regression, and impact ranking while preserving v2/V11 authority boundaries.

**Architecture:** V3 sits above V11 collection and v2 verification. Discovery is allowed to infer and rank hypotheses, but authoritative promotion requires declared intent plus declared/observed product facts; verified findings still come only from existing v2 rules/evaluators. Temporal comparison and impact ranking consume verified outputs and never escalate rule severity/enforcement.

**Tech Stack:** Python 3.10–3.12, standard library (`unittest`, `hashlib`, `json`, `math`, `copy`, `urllib.parse`), existing NUI V11 normalization, existing UX Intelligence v1/v2 package and MCP surface.

**Spec:** `docs/superpowers/specs/2026-09-06-ux-intelligence-v3-design.md`

## Global Constraints

- V11 remains the only browser/runtime collection layer; no Playwright/browser object crosses public UX contracts.
- V2 `validate_ux_journey_spec` and `verify_ux_journey` remain the journey-validation/finding authority.
- Discovery may create inferred hypotheses; inferred-only facts cannot independently satisfy authoritative v2 promotion requirements.
- `goal` and `task` nodes are only `declared` or `inferred`; browser traversal alone never makes intent `observed`.
- Confidence values are finite numeric `[0.0, 1.0]` and reject `bool`.
- Query/planning limits are integers `1..100` and reject `bool`.
- Missing evidence remains missing; it never becomes a fabricated UX failure or invented impact default.
- Priority ranking never mutates or escalates existing UX `severity` or `enforcement`.
- No rule, skill, journey, candidate, or evidence count quota is introduced.
- No fixed click-count, memory-count, or unconditional friction folklore is encoded.
- V1/v2 public behavior must remain backward compatible.
- Use standard-library `unittest` to match repository CI.

---

## File Structure

### New production modules

- `src/nolane_ui/ux_intelligence/product_model.py` — discovery-packet validation/normalization plus product-model validation, normalization, and deterministic model construction.
- `src/nolane_ui/ux_intelligence/goal_graph.py` — declared/inferred intent graph validation and deterministic goal-graph construction from product evidence.
- `src/nolane_ui/ux_intelligence/discovery.py` — journey candidate generation, deterministic scoring/fingerprints, bounded querying, and promotion into unchanged v2 journey contracts.
- `src/nolane_ui/ux_intelligence/discovery_planner.py` — bounded observation requests only; never execution claims.
- `src/nolane_ui/ux_intelligence/temporal_evidence.py` — deterministic semantic fingerprints and immutable-by-contract snapshot creation/validation.
- `src/nolane_ui/ux_intelligence/regression.py` — semantic snapshot comparison, evidence-loss distinction, optional history-aware reintroduction classification.
- `src/nolane_ui/ux_intelligence/impact.py` — evidence-bounded priority scoring that keeps authority unchanged.
- `src/nolane_ui/ux_intelligence/v3_catalog.py` — v3 enums, exported scoring weights, regression mappings, required impact components, and aggregate status.

### Modified integration modules

- `src/nolane_ui/ux_intelligence/__init__.py` — package exports.
- `src/nolane_ui/__init__.py` — top-level Python exports.
- `src/nolane_ui/mcp_server.py` — read/build/plan/compare v3 wrappers, catalog entries, and MCP tools.

### New tests

- `tests/test_ux_intelligence_v3_product_model.py`
- `tests/test_ux_intelligence_v3_goal_graph.py`
- `tests/test_ux_intelligence_v3_discovery.py`
- `tests/test_ux_intelligence_v3_promotion.py`
- `tests/test_ux_intelligence_v3_planner.py`
- `tests/test_ux_intelligence_v3_temporal.py`
- `tests/test_ux_intelligence_v3_regression.py`
- `tests/test_ux_intelligence_v3_impact.py`
- `tests/test_ux_intelligence_v3_api_mcp.py`
- `tests/test_ux_intelligence_v3_acceptance.py`

---

### Task 1: Product Model and Discovery Packet Contracts

**Files:**
- Create: `src/nolane_ui/ux_intelligence/product_model.py`
- Test: `tests/test_ux_intelligence_v3_product_model.py`

**Interfaces:**
- Consumes: existing `UX_PROVENANCE`; lazy V11 `normalize_browser_observation` for optional raw runtime packets.
- Produces:
  - `validate_ux_discovery_packet(packet: dict[str, Any], *, provenance_catalog=UX_PROVENANCE) -> dict[str, Any]`
  - `normalize_ux_discovery_packet(packet: dict[str, Any], *, provenance_catalog=UX_PROVENANCE) -> dict[str, Any]`
  - `validate_ux_product_model(model: dict[str, Any], *, provenance_catalog=UX_PROVENANCE) -> dict[str, Any]`
  - `normalize_ux_product_model(model: dict[str, Any], *, provenance_catalog=UX_PROVENANCE) -> dict[str, Any]`
  - `build_ux_product_model(packet: dict[str, Any], *, provenance_catalog=UX_PROVENANCE) -> dict[str, Any]`

**Discovery evidence sub-records locked by this task:**

```python
# captures[*].object_evidence[*]
{
    "object_id": "cart-42",
    "object_type": "cart",
    "labels": ["Current cart"],
    "identity_fields": ["object_id"],
    "state_ids": ["cart-open"],
    "evidence_refs": ["runtime-v11:locator:#cart:attribute:data-object-id"],
}

# captures[*].action_evidence[*]
{
    "action_id": "checkout",
    "label": "Checkout",
    "action_kind": "activate",
    "object_id": "cart-42",
    "commitment_level": "state-changing",
    "target_surface_ids": ["checkout"],
    "state_changes": {"checkout_started": True},
    "evidence_refs": ["runtime-v11:locator:#checkout:visible_text"],
}

# captures[*].state_evidence[*]
{
    "state_id": "cart-open",
    "object_id": "cart-42",
    "attributes": {"checkout_started": False},
    "evidence_refs": ["runtime-v11:locator:#cart:attribute:data-state"],
}

# captures[*].transition_evidence[*]
{
    "transition_id": "cart-to-checkout",
    "source_id": "cart",
    "relation": "navigates-to",
    "target_id": "checkout",
    "evidence_refs": ["runtime-v11:url-path:https://example.test/checkout"],
}

# captures[*].success_evidence[*]
{
    "outcome_id": "order-submitted",
    "label": "Order submitted",
    "surface_id": "confirmation",
    "evidence_refs": ["runtime-v11:locator:#success:visible_text"],
}
```

- [ ] **Step 1: Write product-model RED contract tests**

```python
import math
import unittest
from nolane_ui.ux_intelligence.product_model import (
    build_ux_product_model,
    normalize_ux_discovery_packet,
    validate_ux_product_model,
)

class UXProductModelV3Tests(unittest.TestCase):
    def test_bool_and_nonfinite_confidence_are_rejected(self):
        model = self.valid_model()
        model["surfaces"][0]["confidence"] = True
        with self.assertRaises((TypeError, ValueError)):
            validate_ux_product_model(model)
        model = self.valid_model()
        model["surfaces"][0]["confidence"] = math.inf
        with self.assertRaises(ValueError):
            validate_ux_product_model(model)

    def test_observed_record_requires_evidence(self):
        model = self.valid_model()
        model["actions"][0]["origin"] = "observed"
        model["actions"][0]["evidence_refs"] = []
        with self.assertRaises(ValueError):
            validate_ux_product_model(model)

    def test_v11_packet_is_normalized_without_inventing_semantics(self):
        packet = self.discovery_packet_with_runtime_v11()
        normalized = normalize_ux_discovery_packet(packet)
        capture = normalized["captures"][0]
        self.assertIn("runtime_v11", capture)
        self.assertEqual(capture["action_evidence"], ())
        self.assertNotIn("inferred_goal", capture)

    def test_build_model_resolves_all_ids_and_deduplicates_exact_evidence(self):
        model = build_ux_product_model(self.complete_discovery_packet())
        self.assertTrue(validate_ux_product_model(model)["valid"])
        self.assertEqual(tuple(item["surface_id"] for item in model["surfaces"]), tuple(sorted(item["surface_id"] for item in model["surfaces"])))
```

- [ ] **Step 2: Run tests to prove RED**

Run:

```bash
PYTHONPATH=src python -m unittest tests.test_ux_intelligence_v3_product_model -v
```

Expected: import failure because `product_model.py` does not exist.

- [ ] **Step 3: Implement strict validators and normalization**

Core validation helper must reject `bool`, NaN, and infinities:

```python
def _confidence(value: Any, label: str) -> float:
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise TypeError(f"{label} must be numeric")
    value = float(value)
    if not math.isfinite(value) or not 0.0 <= value <= 1.0:
        raise ValueError(f"{label} must be finite and within [0, 1]")
    return value
```

Optional raw V11 packets are normalized only as runtime evidence; no semantic action/object/goal is synthesized from them:

```python
def _normalize_optional_v11(capture: dict[str, Any]) -> None:
    packet = capture.get("runtime_v11")
    if packet is None:
        return
    from ..runtime_v11.browser import normalize_browser_observation
    capture["runtime_v11"] = normalize_browser_observation(packet)
```

Model construction merges exact IDs/evidence deterministically and validates references before returning.

- [ ] **Step 4: Run focused Task 1 tests**

```bash
PYTHONPATH=src python -m unittest tests.test_ux_intelligence_v3_product_model -v
```

Expected: PASS.

- [ ] **Step 5: Commit Task 1**

```bash
git add src/nolane_ui/ux_intelligence/product_model.py tests/test_ux_intelligence_v3_product_model.py
git commit -m "feat: add UX v3 product model"
```

---

### Task 2: Goal Graph with Explicit Intent Authority

**Files:**
- Create: `src/nolane_ui/ux_intelligence/goal_graph.py`
- Test: `tests/test_ux_intelligence_v3_goal_graph.py`

**Interfaces:**
- Consumes: `normalize_ux_product_model(...)`.
- Produces:
  - `validate_ux_goal_graph(graph: dict[str, Any], *, provenance_catalog=UX_PROVENANCE) -> dict[str, Any]`
  - `normalize_ux_goal_graph(graph: dict[str, Any], *, provenance_catalog=UX_PROVENANCE) -> dict[str, Any]`
  - `build_ux_goal_graph(product_model: dict[str, Any], *, declared_goals: Iterable[dict[str, Any]] = (), inferred_goals: Iterable[dict[str, Any]] = (), provenance_catalog=UX_PROVENANCE) -> dict[str, Any]`

Declared goal seed shape:

```python
{
    "goal_id": "submit-order",
    "label": "Submit an order",
    "description": "Complete checkout for the current cart",
    "task_ids": ["checkout-cart"],
    "outcome_ids": ["order-submitted"],
    "provenance_ids": ["uxp.product-journey-contract"],
}
```

- [ ] **Step 1: Write RED goal-authority tests**

```python
class UXGoalGraphV3Tests(unittest.TestCase):
    def test_goal_and_task_cannot_be_observed(self):
        graph = self.valid_graph()
        graph["nodes"][0]["kind"] = "goal"
        graph["nodes"][0]["origin"] = "observed"
        with self.assertRaises(ValueError):
            validate_ux_goal_graph(graph)

    def test_browser_traversal_does_not_promote_inferred_goal(self):
        graph = build_ux_goal_graph(
            self.product_model(),
            inferred_goals=[{
                "goal_id": "checkout",
                "label": "Checkout",
                "description": "Inferred from product structure",
                "task_ids": [],
                "outcome_ids": ["order-submitted"],
                "evidence_refs": ["runtime-v11:url-path:/checkout"],
            }],
        )
        goal = next(node for node in graph["nodes"] if node["node_id"] == "goal:checkout")
        self.assertEqual(goal["origin"], "inferred")

    def test_invalid_self_decomposition_is_rejected(self):
        graph = self.valid_graph()
        graph["edges"].append({
            "edge_id": "bad",
            "source_id": "goal:submit-order",
            "relation": "decomposes-to",
            "target_id": "goal:submit-order",
            "origin": "declared",
            "confidence": 1.0,
            "evidence_refs": [],
        })
        with self.assertRaises(ValueError):
            validate_ux_goal_graph(graph)
```

- [ ] **Step 2: Run Task 2 RED**

```bash
PYTHONPATH=src python -m unittest tests.test_ux_intelligence_v3_goal_graph -v
```

Expected: import failure.

- [ ] **Step 3: Implement node/edge court and deterministic builder**

Intent-origin rule is explicit:

```python
if node["kind"] in {"goal", "task"} and node["origin"] == "observed":
    raise ValueError(f"{node_id}: intent nodes cannot use observed origin")
```

`build_ux_goal_graph` must create product `object/action/state/outcome` nodes from normalized model evidence, add declared goals exactly as declared, and add inferred goals only with `origin="inferred"`. It may connect outcomes/actions using deterministic IDs but must not convert a route label into a declared goal.

- [ ] **Step 4: Run Task 2 tests**

```bash
PYTHONPATH=src python -m unittest tests.test_ux_intelligence_v3_goal_graph -v
```

Expected: PASS.

- [ ] **Step 5: Commit Task 2**

```bash
git add src/nolane_ui/ux_intelligence/goal_graph.py tests/test_ux_intelligence_v3_goal_graph.py
git commit -m "feat: add UX v3 goal graph"
```

---

### Task 3: V3 Catalog and Autonomous Journey Candidate Discovery

**Files:**
- Create: `src/nolane_ui/ux_intelligence/v3_catalog.py`
- Create: `src/nolane_ui/ux_intelligence/discovery.py`
- Test: `tests/test_ux_intelligence_v3_discovery.py`

**Interfaces:**
- Consumes: normalized product model + goal graph.
- Produces:
  - `UX_DISCOVERY_SCORE_WEIGHTS`
  - `discover_ux_journeys(product_model: dict[str, Any], goal_graph: dict[str, Any], *, max_depth: int = 8, verified_journey_fingerprints: Iterable[str] = ()) -> tuple[dict[str, Any], ...]`
  - `query_ux_journey_candidates(candidates: Iterable[dict[str, Any]], *, goal_node_id: str | None = None, status: str | None = None, min_score: float | None = None, limit: int = 25) -> list[dict[str, Any]]`

Versioned score weights:

```python
UX_DISCOVERY_SCORE_WEIGHTS = {
    "goal_confidence": 0.25,
    "success_evidence_strength": 0.20,
    "path_evidence_coverage": 0.20,
    "critical_action_presence": 0.15,
    "recovery_relevance": 0.10,
    "novelty_against_verified_journeys": 0.10,
}
```

- [ ] **Step 1: Write RED candidate determinism/authority tests**

```python
class UXDiscoveryV3Tests(unittest.TestCase):
    def test_candidates_are_deterministic_and_duplicate_paths_collapse(self):
        first = discover_ux_journeys(self.product_model(), self.goal_graph(), max_depth=8)
        second = discover_ux_journeys(self.product_model(), self.goal_graph(), max_depth=8)
        self.assertEqual(first, second)
        self.assertEqual(len({item["candidate_id"] for item in first}), len(first))

    def test_cycle_terminates_at_repeated_semantic_state(self):
        candidates = discover_ux_journeys(self.cyclic_product_model(), self.goal_graph(), max_depth=8)
        self.assertLessEqual(max(len(item["step_hypotheses"]) for item in candidates), 8)

    def test_depth_rejects_bool_and_out_of_range(self):
        with self.assertRaises(TypeError):
            discover_ux_journeys(self.product_model(), self.goal_graph(), max_depth=True)
        with self.assertRaises(ValueError):
            discover_ux_journeys(self.product_model(), self.goal_graph(), max_depth=33)

    def test_inferred_goal_candidate_remains_hypothesis(self):
        candidate = next(item for item in discover_ux_journeys(self.product_model(), self.inferred_goal_graph()))
        self.assertEqual(candidate["status"], "hypothesis")
```

- [ ] **Step 2: Run Task 3 RED**

```bash
PYTHONPATH=src python -m unittest tests.test_ux_intelligence_v3_discovery -v
```

Expected: missing `discovery`/`v3_catalog` imports.

- [ ] **Step 3: Implement deterministic graph walk, fingerprint, and score**

Candidate ID is a hash over semantic path identity, never list position:

```python
def _candidate_id(product_id: str, revision: str, goal_node_id: str, action_ids: tuple[str, ...]) -> str:
    payload = json.dumps(
        [product_id, revision, goal_node_id, list(action_ids)],
        ensure_ascii=False,
        sort_keys=True,
        separators=(",", ":"),
    ).encode("utf-8")
    return "uxc:" + hashlib.sha256(payload).hexdigest()[:24]
```

Cycle prevention tracks `(surface_id, action_id, target_surface_id)` semantic states. `max_depth` is only an exploration safety limit. Score components are exposed individually and the weighted sum is rounded deterministically; no score affects rule authority.

- [ ] **Step 4: Implement defensive bounded candidate querying**

```python
def _validate_limit(limit: int) -> int:
    if isinstance(limit, bool) or not isinstance(limit, int):
        raise TypeError("limit must be an integer")
    if not 1 <= limit <= 100:
        raise ValueError("limit must be between 1 and 100")
    return limit
```

Sort query results by `(-discovery_score, candidate_id)` and return deep copies.

- [ ] **Step 5: Run Task 3 tests and commit**

```bash
PYTHONPATH=src python -m unittest tests.test_ux_intelligence_v3_discovery -v
git add src/nolane_ui/ux_intelligence/v3_catalog.py src/nolane_ui/ux_intelligence/discovery.py tests/test_ux_intelligence_v3_discovery.py
git commit -m "feat: add autonomous UX journey discovery"
```

---

### Task 4: Promotion into Unchanged V2 Journey Contracts

**Files:**
- Modify: `src/nolane_ui/ux_intelligence/discovery.py`
- Test: `tests/test_ux_intelligence_v3_promotion.py`

**Interfaces:**
- Consumes: `validate_ux_journey_spec` from v2 and normalized product/goal records.
- Produces:
  - `promote_ux_journey_candidate(candidate: dict[str, Any], product_model: dict[str, Any], goal_graph: dict[str, Any], *, provenance_catalog=UX_PROVENANCE) -> dict[str, Any]`

Return shape:

```python
{
    "status": "promoted" | "promotion-gaps",
    "candidate_id": "uxc:...",
    "journey": {...} | None,
    "promotion_gaps": (
        {"code": "goal-not-declared", "field": "goal_node_id", "because": "..."},
    ),
}
```

- [ ] **Step 1: Write RED promotion-boundary tests**

```python
class UXPromotionV3Tests(unittest.TestCase):
    def test_inferred_goal_cannot_promote(self):
        result = promote_ux_journey_candidate(
            self.inferred_candidate(), self.product_model(), self.inferred_goal_graph()
        )
        self.assertEqual(result["status"], "promotion-gaps")
        self.assertIn("goal-not-declared", {gap["code"] for gap in result["promotion_gaps"]})
        self.assertIsNone(result["journey"])

    def test_missing_recovery_semantics_cannot_be_filled_with_not_applicable(self):
        result = promote_ux_journey_candidate(
            self.candidate_without_recovery(), self.product_model(), self.declared_goal_graph()
        )
        self.assertIn("recovery-expectation-unproven", {gap["code"] for gap in result["promotion_gaps"]})
        self.assertIsNone(result["journey"])

    def test_promoted_mapping_passes_existing_v2_validator_unchanged(self):
        result = promote_ux_journey_candidate(
            self.complete_candidate(), self.complete_product_model(), self.declared_goal_graph()
        )
        self.assertEqual(result["status"], "promoted")
        self.assertTrue(validate_ux_journey_spec(result["journey"])["valid"])
```

- [ ] **Step 2: Run Task 4 RED**

```bash
PYTHONPATH=src python -m unittest tests.test_ux_intelligence_v3_promotion -v
```

Expected: `promote_ux_journey_candidate` absent.

- [ ] **Step 3: Implement deterministic promotion court**

Promotion gaps must be emitted in stable `(code, field)` order. Required checks include:

```python
if goal["origin"] != "declared":
    gaps.append(_promotion_gap("goal-not-declared", "goal_node_id", "authoritative v2 promotion requires an explicitly declared goal"))

if action["origin"] not in {"declared", "observed"}:
    gaps.append(_promotion_gap("action-inferred-only", action_id, "promoted steps require declared or observed action evidence"))

if not step_hypothesis["recovery_hypotheses"]:
    gaps.append(_promotion_gap("recovery-expectation-unproven", candidate_step_id, "v2 requires a non-empty recovery expectation and v3 may not invent one"))
```

For successful promotion, derive `expected_transition={"route": target_surface["locator"]}` only when the target surface/transition is declared or observed. `evidence_requirements` is the sorted union of expected-transition keys plus supported required/preserved context fields. Call `validate_ux_journey_spec(journey, provenance_catalog=...)` before returning.

- [ ] **Step 4: Run Task 4 tests and v2 journey tests**

```bash
PYTHONPATH=src python -m unittest \
  tests.test_ux_intelligence_v3_promotion \
  tests.test_ux_intelligence_v2_journeys \
  tests.test_ux_intelligence_v2_verifier -v
```

Expected: PASS.

- [ ] **Step 5: Commit Task 4**

```bash
git add src/nolane_ui/ux_intelligence/discovery.py tests/test_ux_intelligence_v3_promotion.py
git commit -m "feat: promote verified UX journey candidates"
```

---

### Task 5: Observation Planner without Runtime Authority

**Files:**
- Create: `src/nolane_ui/ux_intelligence/discovery_planner.py`
- Test: `tests/test_ux_intelligence_v3_planner.py`

**Interfaces:**
- Produces:
  - `plan_ux_discovery(subject: dict[str, Any], available_capabilities: Iterable[str], *, limit: int = 25) -> tuple[dict[str, Any], ...]`

- [ ] **Step 1: Write RED planner tests**

```python
class UXPlannerV3Tests(unittest.TestCase):
    def test_planner_returns_requests_not_execution_claims(self):
        requests = plan_ux_discovery(self.candidate(), {"browser-runtime", "interaction"})
        self.assertTrue(requests)
        for request in requests:
            self.assertNotIn("executed", request)
            self.assertNotIn("observed", request)
            self.assertNotIn("success", request)
            self.assertIn("required_evidence_fields", request)

    def test_goal_acceptance_is_not_faked_as_runtime_observation(self):
        requests = plan_ux_discovery(self.inferred_goal_candidate(), {"browser-runtime", "interaction"})
        self.assertNotIn("goal_origin", {field for item in requests for field in item["required_evidence_fields"]})

    def test_limit_rejects_bool(self):
        with self.assertRaises(TypeError):
            plan_ux_discovery(self.candidate(), {"browser-runtime"}, limit=True)
```

- [ ] **Step 2: Run Task 5 RED**

```bash
PYTHONPATH=src python -m unittest tests.test_ux_intelligence_v3_planner -v
```

- [ ] **Step 3: Implement bounded request generation**

Deterministic request ID:

```python
def _request_id(candidate_id: str, step_id: str, fields: tuple[str, ...]) -> str:
    raw = "|".join((candidate_id, step_id, *fields)).encode("utf-8")
    return "uxr:" + hashlib.sha256(raw).hexdigest()[:24]
```

Planner can request route, object identity, context preservation, recovery, and outcome evidence. `preferred_v11_capabilities` is the intersection of requested capabilities and `available_capabilities`; absence of a capability does not claim failure.

- [ ] **Step 4: Run Task 5 tests and commit**

```bash
PYTHONPATH=src python -m unittest tests.test_ux_intelligence_v3_planner -v
git add src/nolane_ui/ux_intelligence/discovery_planner.py tests/test_ux_intelligence_v3_planner.py
git commit -m "feat: add UX discovery observation planner"
```

---

### Task 6: Temporal Evidence Snapshots and Stable Fingerprints

**Files:**
- Create: `src/nolane_ui/ux_intelligence/temporal_evidence.py`
- Test: `tests/test_ux_intelligence_v3_temporal.py`

**Interfaces:**
- Consumes: a validated v2 journey mapping and `verify_ux_journey` output.
- Produces:
  - `create_ux_evidence_snapshot(product_id: str, revision: str, journey: dict[str, Any], verification: dict[str, Any], *, created_from: str, provenance_ids: Iterable[str] = ()) -> dict[str, Any]`
  - `validate_ux_evidence_snapshot(snapshot: dict[str, Any]) -> dict[str, Any]`
  - `ux_semantic_fingerprint(value: Any) -> str`

- [ ] **Step 1: Write RED fingerprint/snapshot tests**

```python
class UXTemporalV3Tests(unittest.TestCase):
    def test_fingerprint_ignores_transient_evidence_refs_but_not_semantics(self):
        a = self.finding(evidence_refs=("capture:A",))
        b = self.finding(evidence_refs=("capture:B",))
        self.assertEqual(self.finding_fingerprint(a), self.finding_fingerprint(b))
        b["expected"] = {"object_id": "cart-2"}
        self.assertNotEqual(self.finding_fingerprint(a), self.finding_fingerprint(b))

    def test_snapshot_creation_does_not_mutate_verification_input(self):
        verification = self.verification()
        before = copy.deepcopy(verification)
        create_ux_evidence_snapshot("shop", "rev-a", self.journey(), verification, created_from="ci:1")
        self.assertEqual(verification, before)

    def test_same_semantics_same_fingerprint_across_revisions(self):
        a = create_ux_evidence_snapshot("shop", "rev-a", self.journey(), self.verification(), created_from="ci:1")
        b = create_ux_evidence_snapshot("shop", "rev-b", self.journey(), self.verification_with_new_capture_refs(), created_from="ci:2")
        self.assertEqual(a["journey_fingerprint"], b["journey_fingerprint"])
```

- [ ] **Step 2: Run Task 6 RED**

```bash
PYTHONPATH=src python -m unittest tests.test_ux_intelligence_v3_temporal -v
```

- [ ] **Step 3: Implement canonical semantic hashing**

```python
def ux_semantic_fingerprint(value: Any) -> str:
    payload = json.dumps(
        _semantic_normalize(value),
        ensure_ascii=False,
        sort_keys=True,
        separators=(",", ":"),
    ).encode("utf-8")
    return hashlib.sha256(payload).hexdigest()
```

`_semantic_normalize` removes only transient keys explicitly listed in the module (`evidence_refs`, `_evidence_refs`, `runtime_evidence_refs`, `capture_ref`, timestamps); it must not remove `rule_id`, `step_id`, expected/observed values, journey structure, or product-local success criteria.

Snapshot fields store tuples/deep copies and there is no mutation API; callers receive serialization-safe values and creation never mutates source verification.

- [ ] **Step 4: Run Task 6 tests and commit**

```bash
PYTHONPATH=src python -m unittest tests.test_ux_intelligence_v3_temporal -v
git add src/nolane_ui/ux_intelligence/temporal_evidence.py tests/test_ux_intelligence_v3_temporal.py
git commit -m "feat: add temporal UX evidence snapshots"
```

---

### Task 7: Semantic UX Regression Engine

**Files:**
- Create: `src/nolane_ui/ux_intelligence/regression.py`
- Modify: `src/nolane_ui/ux_intelligence/v3_catalog.py`
- Test: `tests/test_ux_intelligence_v3_regression.py`

**Interfaces:**
- Produces:
  - `compare_ux_snapshots(baseline: dict[str, Any], candidate: dict[str, Any], *, history: Iterable[dict[str, Any]] = ()) -> dict[str, Any]`

Specific finding-to-regression mapping:

```python
UX_RULE_REGRESSION_CLASSES = {
    "ux.recovery.dead-end-has-recovery-path": "recovery-path-lost",
    "ux.recovery.recovery-path-is-reachable": "recovery-path-lost",
    "ux.task.same-goal-navigation-preserves-context": "preserved-context-regressed",
    "ux.task.no-premature-commitment": "new-premature-commitment",
    "ux.task.hidden-dependency-before-commit": "new-hidden-dependency",
    "ux.comprehension.no-false-completion": "new-false-completion",
}
```

- [ ] **Step 1: Write RED regression tests**

```python
class UXRegressionV3Tests(unittest.TestCase):
    def test_cross_product_comparison_is_rejected(self):
        with self.assertRaises(ValueError):
            compare_ux_snapshots(self.snapshot(product_id="shop"), self.snapshot(product_id="mail"))

    def test_pass_to_missing_evidence_is_not_proven_failure(self):
        result = compare_ux_snapshots(self.passed_snapshot(), self.insufficient_snapshot())
        self.assertEqual(result["status"], "insufficient-evidence")
        self.assertIn("journey-pass-to-insufficient-evidence", {r["class"] for r in result["regressions"]})
        self.assertFalse(any(r.get("proven_failure") for r in result["regressions"]))

    def test_new_context_finding_maps_to_specific_regression_without_authority_escalation(self):
        result = compare_ux_snapshots(self.passed_snapshot(), self.context_failure_snapshot())
        regression = next(r for r in result["regressions"] if r["class"] == "preserved-context-regressed")
        self.assertEqual(regression["enforcement"], "block")
        self.assertEqual(regression["rule_id"], "ux.task.same-goal-navigation-preserves-context")

    def test_reintroduced_requires_history(self):
        result = compare_ux_snapshots(
            self.clean_snapshot("rev-b"),
            self.failure_snapshot("rev-c"),
            history=(self.failure_snapshot("rev-a"),),
        )
        self.assertIn("reintroduced-rule-finding", {r["class"] for r in result["regressions"]})
```

- [ ] **Step 2: Run Task 7 RED**

```bash
PYTHONPATH=src python -m unittest tests.test_ux_intelligence_v3_regression -v
```

- [ ] **Step 3: Implement identity/authority-safe comparison**

Rules:

```python
if baseline["product_id"] != candidate["product_id"]:
    raise ValueError("snapshot products differ")
if baseline["journey_id"] != candidate["journey_id"]:
    raise ValueError("snapshot journeys differ")
```

A finding absent from baseline but present candidate uses the specific rule mapping when available. It is `reintroduced-rule-finding` only when the same finding fingerprint appears in `history`; otherwise use the mapped specific class or `new-rule-finding`. Copy `severity`/`enforcement` from the candidate finding exactly; never derive stronger values.

- [ ] **Step 4: Run Task 7 tests and commit**

```bash
PYTHONPATH=src python -m unittest tests.test_ux_intelligence_v3_regression -v
git add src/nolane_ui/ux_intelligence/regression.py src/nolane_ui/ux_intelligence/v3_catalog.py tests/test_ux_intelligence_v3_regression.py
git commit -m "feat: detect semantic UX regressions"
```

---

### Task 8: Evidence-Bounded Impact Ranking

**Files:**
- Create: `src/nolane_ui/ux_intelligence/impact.py`
- Modify: `src/nolane_ui/ux_intelligence/v3_catalog.py`
- Test: `tests/test_ux_intelligence_v3_impact.py`

**Interfaces:**
- Produces:
  - `UX_IMPACT_SCORE_WEIGHTS`
  - `UX_REQUIRED_IMPACT_COMPONENTS`
  - `rank_ux_impacts(items: Iterable[dict[str, Any]], impact_evidence: dict[str, dict[str, Any]]) -> tuple[dict[str, Any], ...]`

Catalog constants:

```python
UX_IMPACT_SCORE_WEIGHTS = {
    "goal_criticality": 0.22,
    "task_frequency": 0.12,
    "completion_blockage": 0.22,
    "recoverability_cost": 0.14,
    "affected_scope": 0.12,
    "regression_confidence": 0.10,
    "evidence_completeness": 0.08,
}
UX_REQUIRED_IMPACT_COMPONENTS = {
    "goal_criticality",
    "completion_blockage",
    "regression_confidence",
    "evidence_completeness",
}
```

Each component uses:

```python
{"value": 0.9, "origin": "declared" | "observed" | "inferred", "evidence_refs": ("contract:critical-flow",)}
```

- [ ] **Step 1: Write RED ranking authority tests**

```python
class UXImpactV3Tests(unittest.TestCase):
    def test_missing_required_component_returns_unknown_not_default(self):
        assessment = rank_ux_impacts([self.finding()], self.incomplete_evidence())[0]
        self.assertEqual(assessment["status"], "insufficient-evidence")
        self.assertEqual(assessment["priority_band"], "unknown")
        self.assertIsNone(assessment["priority_score"])

    def test_inferred_component_makes_ranking_provisional(self):
        evidence = self.complete_evidence()
        evidence["task_frequency"]["origin"] = "inferred"
        assessment = rank_ux_impacts([self.finding()], evidence)[0]
        self.assertEqual(assessment["status"], "provisional")

    def test_priority_does_not_mutate_warning_authority(self):
        finding = self.warning_finding()
        before = copy.deepcopy(finding)
        assessment = rank_ux_impacts([finding], self.p0_evidence())[0]
        self.assertEqual(assessment["priority_band"], "p0")
        self.assertEqual(finding, before)
        self.assertEqual(finding["enforcement"], "warn")
```

- [ ] **Step 2: Run Task 8 RED**

```bash
PYTHONPATH=src python -m unittest tests.test_ux_intelligence_v3_impact -v
```

- [ ] **Step 3: Implement ranking with explicit status and bands**

Band thresholds are versioned in `v3_catalog.py`:

```python
UX_PRIORITY_BANDS = ((0.85, "p0"), (0.70, "p1"), (0.50, "p2"), (0.0, "p3"))
```

All component values use the same finite/non-bool `[0,1]` validation as confidence. Missing required components produce no numeric score. Any inferred component makes an otherwise complete assessment `provisional`. Sort output by known score descending, then source identity.

- [ ] **Step 4: Run Task 8 tests and commit**

```bash
PYTHONPATH=src python -m unittest tests.test_ux_intelligence_v3_impact -v
git add src/nolane_ui/ux_intelligence/impact.py src/nolane_ui/ux_intelligence/v3_catalog.py tests/test_ux_intelligence_v3_impact.py
git commit -m "feat: rank verified UX impact"
```

---

### Task 9: V3 Status and Public Python Exports

**Files:**
- Modify: `src/nolane_ui/ux_intelligence/v3_catalog.py`
- Modify: `src/nolane_ui/ux_intelligence/__init__.py`
- Modify: `src/nolane_ui/__init__.py`
- Test: `tests/test_ux_intelligence_v3_api_mcp.py`

**Interfaces:**
- Produces `ux_v3_status() -> dict[str, Any]` and all public APIs from the spec.

- [ ] **Step 1: Write RED public API/status tests**

```python
class UXV3PublicAPITests(unittest.TestCase):
    def test_top_level_exports_v3_surfaces(self):
        import nolane_ui
        for name in (
            "validate_ux_product_model", "normalize_ux_product_model", "build_ux_product_model",
            "validate_ux_goal_graph", "build_ux_goal_graph", "discover_ux_journeys",
            "query_ux_journey_candidates", "promote_ux_journey_candidate", "plan_ux_discovery",
            "create_ux_evidence_snapshot", "compare_ux_snapshots", "rank_ux_impacts", "ux_v3_status",
        ):
            self.assertTrue(hasattr(nolane_ui, name), name)

    def test_v3_status_preserves_authority_boundaries(self):
        status = ux_v3_status()
        self.assertEqual(status["version"], 3)
        self.assertFalse(status["discovery_can_create_blocking_findings"])
        self.assertFalse(status["owns_browser_runtime"])
        self.assertTrue(status["uses_v2_verification_authority"])
        self.assertFalse(status["uses_journey_count_quota"])
```

- [ ] **Step 2: Run RED API test**

```bash
PYTHONPATH=src python -m unittest tests.test_ux_intelligence_v3_api_mcp.UXV3PublicAPITests -v
```

- [ ] **Step 3: Implement exports and aggregate status**

`ux_v3_status()` must validate weight sums, known enums, and expose at least:

```python
{
    "version": 3,
    "product_model_valid": True,
    "goal_graph_valid": True,
    "discovery_score_weight_sum": 1.0,
    "impact_score_weight_sum": 1.0,
    "discovery_can_create_blocking_findings": False,
    "owns_browser_runtime": False,
    "uses_v2_verification_authority": True,
    "uses_rule_count_quota": False,
    "uses_skill_count_quota": False,
    "uses_journey_count_quota": False,
}
```

- [ ] **Step 4: Run v1/v2/v3 import/status tests and commit**

```bash
PYTHONPATH=src python -m unittest \
  tests.test_ux_intelligence \
  tests.test_ux_intelligence_v2_status \
  tests.test_ux_intelligence_v3_api_mcp.UXV3PublicAPITests -v
git add src/nolane_ui/ux_intelligence/v3_catalog.py src/nolane_ui/ux_intelligence/__init__.py src/nolane_ui/__init__.py tests/test_ux_intelligence_v3_api_mcp.py
git commit -m "feat: expose UX Intelligence v3 Python API"
```

---

### Task 10: MCP V3 Read/Build/Plan/Compare Surface

**Files:**
- Modify: `src/nolane_ui/mcp_server.py`
- Modify: `tests/test_ux_intelligence_v3_api_mcp.py`

**Interfaces:**
- Adds wrappers:
  - `get_ux_v3_status`
  - `build_ux_product_model_record`
  - `build_ux_goal_graph_record`
  - `discover_ux_journey_records`
  - `query_ux_journey_candidate_records`
  - `promote_ux_journey_candidate_record`
  - `plan_ux_discovery_record`
  - `create_ux_evidence_snapshot_record`
  - `compare_ux_snapshot_records`
  - `rank_ux_impact_records`
- Adds tools named exactly as the v3 spec MCP namespace.

- [ ] **Step 1: Write RED MCP catalog/wrapper tests**

```python
class UXV3MCPTests(unittest.TestCase):
    def test_tool_catalog_contains_complete_v3_namespace(self):
        names = {item["name"] for item in mcp_server.tool_catalog()}
        self.assertTrue({
            "nui_ux_v3_status", "nui_build_ux_product_model", "nui_build_ux_goal_graph",
            "nui_discover_ux_journeys", "nui_query_ux_journey_candidates",
            "nui_promote_ux_journey_candidate", "nui_plan_ux_discovery",
            "nui_create_ux_evidence_snapshot", "nui_compare_ux_snapshots", "nui_rank_ux_impacts",
        }.issubset(names))

    def test_planner_wrapper_returns_requests_only(self):
        result = mcp_server.plan_ux_discovery_record(self.candidate(), ["browser-runtime"])
        self.assertIn("requests", result)
        self.assertFalse(any("executed" in item for item in result["requests"]))
```

- [ ] **Step 2: Run MCP RED**

```bash
PYTHONPATH=src python -m unittest tests.test_ux_intelligence_v3_api_mcp.UXV3MCPTests -v
```

- [ ] **Step 3: Implement wrappers, catalog entries, and `@mcp.tool()` functions**

Wrapper example:

```python
def discover_ux_journey_records(product_model, goal_graph, *, max_depth=8, root=None):
    if root is not None:
        _ = Path(root).resolve()
    candidates = discover_ux_journeys(product_model, goal_graph, max_depth=max_depth)
    return {"count": len(candidates), "candidates": candidates}
```

`nui_plan_ux_discovery` must only return observation requests. None of the v3 MCP functions may modify target product files, V13 rules, canonical skills, or persistent evidence storage.

- [ ] **Step 4: Run Task 10 tests and existing MCP tests**

```bash
PYTHONPATH=src python -m unittest \
  tests.test_ux_intelligence_v3_api_mcp \
  tests.test_mcp_server \
  tests.test_ux_intelligence_v2_api_mcp -v
```

Expected: PASS.

- [ ] **Step 5: Commit Task 10**

```bash
git add src/nolane_ui/mcp_server.py tests/test_ux_intelligence_v3_api_mcp.py
git commit -m "feat: expose UX v3 MCP tools"
```

---

### Task 11: Cross-Layer Acceptance and Adversarial Court

**Files:**
- Create: `tests/test_ux_intelligence_v3_acceptance.py`
- Modify only if a test proves a real defect: the narrow v3 module responsible for that defect.

**Interfaces:**
- Exercises the full v3 pipeline without creating a second runtime.

- [ ] **Step 1: Write end-to-end acceptance tests A–G from the spec**

```python
class UXV3AcceptanceTests(unittest.TestCase):
    def test_declared_goal_observed_path_promotes_and_verifies(self):
        model = build_ux_product_model(self.complete_packet())
        graph = build_ux_goal_graph(model, declared_goals=[self.submit_order_goal()])
        candidate = discover_ux_journeys(model, graph)[0]
        promoted = promote_ux_journey_candidate(candidate, model, graph)
        self.assertEqual(promoted["status"], "promoted")
        report = verify_ux_journey(promoted["journey"], self.verifier_observations())
        self.assertEqual(report["status"], "passed")

    def test_inferred_goal_stays_non_authoritative(self):
        model = build_ux_product_model(self.complete_packet())
        graph = build_ux_goal_graph(model, inferred_goals=[self.inferred_checkout_goal()])
        candidate = discover_ux_journeys(model, graph)[0]
        promoted = promote_ux_journey_candidate(candidate, model, graph)
        self.assertEqual(promoted["status"], "promotion-gaps")
        self.assertIn("goal-not-declared", {gap["code"] for gap in promoted["promotion_gaps"]})

    def test_context_regression_inherits_existing_rule_authority(self):
        comparison = compare_ux_snapshots(self.baseline_context_pass(), self.candidate_context_fail())
        regression = next(item for item in comparison["regressions"] if item["class"] == "preserved-context-regressed")
        self.assertEqual(regression["rule_id"], "ux.task.same-goal-navigation-preserves-context")

    def test_evidence_loss_is_not_proven_failure(self):
        comparison = compare_ux_snapshots(self.baseline_pass(), self.candidate_missing_evidence())
        self.assertEqual(comparison["status"], "insufficient-evidence")

    def test_p0_warning_stays_warn(self):
        finding = self.warning_finding()
        assessment = rank_ux_impacts([finding], self.critical_impact_evidence())[0]
        self.assertEqual(assessment["priority_band"], "p0")
        self.assertEqual(finding["enforcement"], "warn")

    def test_planner_request_does_not_mark_completion_observed(self):
        requests = plan_ux_discovery(self.candidate_needing_success_evidence(), ["browser-runtime", "interaction"])
        self.assertTrue(requests)
        self.assertFalse(any("completion_confirmed" in item and item.get("observed") is True for item in requests))
```

Include adversarial cases for cyclic paths, duplicate semantic actions with different IDs, guessed label-only success, missing object identity, cross-product snapshots, navigation noun as inferred goal, and impact enforcement escalation attempt.

- [ ] **Step 2: Run v3 acceptance + all v3 tests**

```bash
PYTHONPATH=src python -m unittest discover -s tests -p 'test_ux_intelligence_v3*.py' -v
```

Expected: PASS after fixing only proven v3 defects.

- [ ] **Step 3: Run focused v1+v2+v3 UX regression**

```bash
PYTHONPATH=src python -m unittest \
  tests.test_ux_intelligence \
  tests.test_ux_intelligence_v2_bridge \
  tests.test_ux_intelligence_v2_provenance \
  tests.test_ux_intelligence_v2_journeys \
  tests.test_ux_intelligence_v2_verifier \
  tests.test_ux_intelligence_v2_runtime_adapter \
  tests.test_ux_intelligence_v2_api_mcp \
  tests.test_ux_intelligence_v2_quality_court \
  tests.test_ux_intelligence_v2_status \
  tests.test_ux_intelligence_v3_product_model \
  tests.test_ux_intelligence_v3_goal_graph \
  tests.test_ux_intelligence_v3_discovery \
  tests.test_ux_intelligence_v3_promotion \
  tests.test_ux_intelligence_v3_planner \
  tests.test_ux_intelligence_v3_temporal \
  tests.test_ux_intelligence_v3_regression \
  tests.test_ux_intelligence_v3_impact \
  tests.test_ux_intelligence_v3_api_mcp \
  tests.test_ux_intelligence_v3_acceptance -v
```

Expected: PASS.

- [ ] **Step 4: Commit acceptance court**

```bash
git add tests/test_ux_intelligence_v3_acceptance.py
git commit -m "test: add UX v3 acceptance court"
```

---

### Task 12: Repository Verification, Draft PR, and Exact-Head Hosted Gate

**Files:**
- No production changes unless verification proves a defect.
- PR body documents RED evidence, focused/full regression, validator metrics, exact head SHA, and hosted gate results.

**Interfaces:**
- Uses existing repository validator and `.github/workflows/verify.yml`.

- [ ] **Step 1: Run full repository unit/contract suite on the exact final feature tree**

```bash
PYTHONPATH=src python -m unittest discover -s tests -v
```

Expected: all tests PASS in a normal hosted-compatible environment. If the local managed Chromium policy blocks a real-browser `file://` smoke, record it separately and require the official hosted Real Chromium job to prove the browser gate.

- [ ] **Step 2: Run repository validator**

```bash
PYTHONPATH=src python scripts/nui-validate .
```

Expected: `valid=true`, `errors=[]`, `warnings=[]`; existing V13 duplicate/boilerplate courts remain clean.

- [ ] **Step 3: Verify source integrity before PR**

```bash
python -m compileall -q src/nolane_ui/ux_intelligence
```

Then inspect branch diff and ensure only v3 spec/plan, v3 modules, integration exports/MCP, and v3 tests changed; no V1/V2/V13 semantic edits without a regression-backed compatibility reason.

- [ ] **Step 4: Open a Draft PR against `main`**

PR title:

```text
feat: add UX Intelligence v3 autonomous discovery
```

PR summary must include:

```text
Product/Goal Model -> Autonomous Journey Discovery -> V11 observation planning -> V2 verification -> Temporal Regression -> Impact Ranking
```

and explicitly state:

```text
Discovery does not create blocking findings. V11 remains runtime owner. V2 remains UX finding authority.
```

- [ ] **Step 5: Wait for exact-final-head GitHub Actions and inspect every job**

Required hosted jobs:

```text
Core Python 3.10
Core Python 3.11
Core Python 3.12
Real Chromium runtime
Current-head release gate
```

All must complete with `success` on the same final head SHA. The release gate must generate a fresh completion packet for `$GITHUB_SHA`, validate the exact revision, and upload expected project artifacts.

- [ ] **Step 6: Mark Ready for review only after exact-head gates are green**

Do not merge merely because the PR is green. Merge remains a separate explicit integration decision, and the merge command must use the expected final head SHA.

---

## Self-Review Results

### Spec coverage

- Product model and discovery packet: Task 1.
- Declared vs inferred user intent and anti-feature-first authority boundary: Task 2.
- Deterministic bounded journey discovery, scoring, querying: Task 3.
- Authoritative promotion into unchanged v2 contract: Task 4.
- Observation planning / V11 separation: Task 5.
- Temporal snapshots/fingerprints: Task 6.
- Semantic regression + evidence loss + optional history for reintroduction: Task 7.
- Impact ranking without authority escalation: Task 8.
- Python/status surfaces: Task 9.
- MCP namespace: Task 10.
- Acceptance scenarios and adversarial cases: Task 11.
- Full validation/CI/PR delivery gate: Task 12.

### Design conflicts resolved in the plan

1. V2 requires a non-empty `recovery_expectation` for every promoted step. V3 therefore emits a promotion gap when recovery semantics are not declared/observed; it never invents `not-applicable` text just to pass v2 validation.
2. `reintroduced-rule-finding` cannot be proven from only baseline/candidate snapshots. `compare_ux_snapshots` therefore accepts optional prior `history`; without history, a newly appearing fingerprint is classified as the specific mapped regression or `new-rule-finding`, not reintroduced.
3. Raw V11 packets may be normalized inside a discovery capture, but semantic object/action/goal facts still come from explicit discovery evidence fields. Browser structure alone does not silently create user intent.
4. Snapshot values stay serialization-safe mappings/tuples; immutability is enforced as an API contract through fresh defensive construction and absence of mutation APIs rather than non-serializable proxy types.

### Type consistency

- All public v3 names exactly match the design spec.
- `product_id`, `revision`, `journey_id`, and semantic IDs remain strings across product, graph, candidate, snapshot, regression, MCP, and tests.
- Confidence/component values consistently use finite non-bool `[0,1]` validation.
- Query/planner limits consistently use integer `1..100`, rejecting `bool`.
- V2 journey promotion returns the existing journey mapping shape and calls existing v2 validation before success.
