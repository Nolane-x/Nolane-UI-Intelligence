# NUI V11 Phase 5 — Live Visual Runtime Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build a provider-neutral, conflict-safe live visual iteration runtime with exact/ambiguous source attribution, immutable preview state, evidence-only overlays, and a concrete Playwright browser adapter that passes a real-browser smoke gate.

**Architecture:** Keep the existing V11 browser packet, evidence, Live Lab, and transactional mutation boundaries authoritative. Add focused Phase 5 modules for source attribution, transport capabilities, preview state, overlay view-models, Playwright collection, and orchestration. Playwright is an optional reference adapter; the core remains importable without it.

**Tech Stack:** Python 3.12 in CI, Python standard library for core, JSON contracts/schemas, existing `runtime_v11` modules, optional `playwright>=1.62,<2`, Chromium installed by Playwright in CI, `unittest`, GitHub Actions.

**Spec:** `docs/superpowers/specs/2026-08-21-v11-live-visual-runtime-design.md`

## Global Constraints

- Add no canonical skills and do not modify `skills/skill-graph.json`.
- Preserve the exact 874 declared/validated skill graph unless separately authorized upstream work changes main first.
- Rendered identity is evidence, never source authority.
- Source attribution must fail closed with `EXACT | CANDIDATE | AMBIGUOUS | UNKNOWN`.
- `CANDIDATE` and `AMBIGUOUS` require explicit source-candidate selection before mutation authority exists.
- `UNKNOWN` can never authorize source mutation.
- Canonical file writes must continue through existing V11 transactional mutation logic.
- Preview must not mutate canonical source.
- HMR is optional capability; bounded reload is the fallback.
- Missing mapping, refresh, observation, capture, or transport capability remains `UNKNOWN`/blocked rather than PASS.
- Overlay output is evidence-only and cannot declare taste winners, `VERIFIED`, or `RELEASED`.
- Core package import must not require Playwright.
- Phase 5 completion requires a non-skipped real Chromium Playwright smoke test on exact head.
- Exact-head completion requires full tests, repository validator, fresh completion packet, 874/874 skills, changed-path audit with no `skills/` paths, and successful project packaging.
- PR #22 remains unmerged unless explicitly authorized.

---

### Task 1: Source Attribution Resolver

**Files:**
- Create: `src/nolane_ui/runtime_v11/source_attribution.py`
- Create: `schemas/runtime-source-attribution-v11.schema.json`
- Create: `tests/test_runtime_v11_source_attribution.py`

**Interfaces:**
- Produces: `validate_source_attribution(record: dict) -> dict`
- Produces: `resolve_source_attribution(rendered_identity: dict, candidates: list[dict], *, repository_root: str | Path) -> dict`
- Produces: `select_source_candidate(attribution: dict, candidate_id: str) -> dict`

- [ ] **Step 1: Write RED tests for closed attribution states and mutation authority**

```python
class RuntimeV11SourceAttributionTests(unittest.TestCase):
    def test_one_valid_current_candidate_can_be_exact(self):
        result = resolve_source_attribution(identity(), [candidate("src/App.tsx")], repository_root=self.root)
        self.assertEqual(result["status"], "EXACT")
        self.assertTrue(result["mutation_authorized"])

    def test_ambiguous_candidates_do_not_authorize_mutation(self):
        result = resolve_source_attribution(identity(), [candidate("src/A.tsx"), candidate("src/B.tsx")], repository_root=self.root)
        self.assertEqual(result["status"], "AMBIGUOUS")
        self.assertFalse(result["mutation_authorized"])

    def test_unknown_attribution_cannot_be_selected(self):
        result = resolve_source_attribution(identity(), [], repository_root=self.root)
        self.assertEqual(result["status"], "UNKNOWN")
        with self.assertRaises(ValueError):
            select_source_candidate(result, "missing")
```

- [ ] **Step 2: Add RED path-safety and stale-digest tests**

```python
    def test_parent_traversal_and_absolute_escape_are_rejected(self):
        for bad in ("../secret.txt", "/etc/passwd"):
            with self.subTest(path=bad):
                result = resolve_source_attribution(identity(), [candidate(bad)], repository_root=self.root)
                self.assertEqual(result["status"], "UNKNOWN")
                self.assertIn("SOURCE_OUTSIDE_ROOT", result["failures"])

    def test_stale_digest_cannot_be_exact(self):
        record = candidate("src/App.tsx", digest="sha256:" + "0" * 64)
        result = resolve_source_attribution(identity(), [record], repository_root=self.root)
        self.assertNotEqual(result["status"], "EXACT")
        self.assertIn("SOURCE_STALE", result["failures"])
```

- [ ] **Step 3: Run focused tests and confirm RED**

Run: `PYTHONPATH=src python -m unittest tests.test_runtime_v11_source_attribution -v`

Expected: module/public APIs absent; existing tests unaffected.

- [ ] **Step 4: Implement path canonicalization, digest binding, deterministic candidate normalization, exact/ambiguous/unknown semantics, and explicit candidate selection**

Implementation rules:
- use `Path.resolve(strict=True)` for candidate source and repository root;
- require `candidate_path.is_relative_to(root_path)` on Python 3.12;
- reject symlink escape because resolved path leaves root;
- verify current digest with existing `sha256_file`;
- never use provider metadata alone to force exactness;
- preserve deterministic candidate order by candidate ID/path;
- return `claim_boundary: source-attribution-only`.

- [ ] **Step 5: Add schema matching exact field/state enums and run focused GREEN**

Run: `PYTHONPATH=src python -m unittest tests.test_runtime_v11_source_attribution -v`

Expected: PASS.

- [ ] **Step 6: Commit Task 1**

Commit message: `feat(v11): add fail-closed source attribution`

---

### Task 2: Browser Transport Capability Contract

**Files:**
- Create: `src/nolane_ui/runtime_v11/browser_transport.py`
- Create: `schemas/runtime-browser-transport-v11.schema.json`
- Create: `tests/test_runtime_v11_browser_transport.py`

**Interfaces:**
- Produces: `validate_browser_transport_capability(record: dict) -> dict`
- Produces: `build_browser_transport_capability(provider: str, capabilities: dict) -> dict`
- Produces: `require_transport_capabilities(record: dict, required: list[str]) -> dict`

- [ ] **Step 1: Write RED tests for explicit capability truthfulness**

```python
CAPS = {
    "navigation": True,
    "geometry": True,
    "computed_style": True,
    "runtime_errors": True,
    "capture": True,
    "document_metrics": True,
    "occlusion": False,
    "rendered_metadata": True,
    "preview_injection": True,
    "hot_reload": False,
    "reload": True,
}

class RuntimeV11BrowserTransportTests(unittest.TestCase):
    def test_missing_capability_is_unknown_not_false_clean(self):
        record = build_browser_transport_capability("fake", CAPS)
        result = require_transport_capabilities(record, ["occlusion"])
        self.assertEqual(result["status"], "UNKNOWN")
        self.assertEqual(result["missing"], ["occlusion"])

    def test_provider_name_never_changes_authority(self):
        record = build_browser_transport_capability("playwright", CAPS)
        self.assertEqual(record["claim_boundary"], "browser-transport-only")
        self.assertNotIn("verified", str(record).lower())
```

- [ ] **Step 2: Run focused RED**

Run: `PYTHONPATH=src python -m unittest tests.test_runtime_v11_browser_transport -v`

- [ ] **Step 3: Implement fixed capability vocabulary and UNKNOWN semantics**

Implementation rules:
- every capability key is boolean;
- unknown capability names are rejected;
- required capability evaluation returns `READY` or `UNKNOWN` only;
- capability results cannot contain release/taste authority.

- [ ] **Step 4: Add schema and run focused GREEN**

- [ ] **Step 5: Commit Task 2**

Commit message: `feat(v11): add browser transport capability contract`

---

### Task 3: Immutable Preview Runtime and Overlay Evidence

**Files:**
- Create: `src/nolane_ui/runtime_v11/preview.py`
- Create: `src/nolane_ui/runtime_v11/overlay.py`
- Create: `schemas/runtime-live-preview-v11.schema.json`
- Create: `schemas/runtime-live-overlay-v11.schema.json`
- Create: `tests/test_runtime_v11_preview.py`
- Create: `tests/test_runtime_v11_overlay.py`

**Interfaces:**
- Produces: `build_preview_candidate(...) -> dict`
- Produces: `validate_preview_candidate(record: dict) -> dict`
- Produces: `assess_preview_freshness(record: dict, repository_root: str | Path) -> dict`
- Produces: `prepare_preview_application(record: dict, transport_capability: dict) -> dict`
- Produces: `record_preview_observation(record: dict, *, refresh_evidence: dict, browser_observation: dict) -> dict`
- Produces: `build_overlay_packet(...) -> dict`
- Produces: `validate_overlay_packet(record: dict) -> dict`

- [ ] **Step 1: RED preview non-destructive/immutability tests**

```python
class RuntimeV11PreviewTests(unittest.TestCase):
    def test_build_preview_does_not_write_source(self):
        before = self.source.read_text()
        preview = build_preview_candidate(...)
        self.assertEqual(self.source.read_text(), before)
        self.assertEqual(preview["state"], "PREPARED")

    def test_changed_base_digest_marks_preview_stale(self):
        preview = build_preview_candidate(...)
        self.source.write_text("changed")
        freshness = assess_preview_freshness(preview, self.root)
        self.assertEqual(freshness["status"], "STALE")
```

- [ ] **Step 2: RED preview observation gating tests**

```python
    def test_observed_requires_successful_refresh_and_fresh_browser_packet(self):
        with self.assertRaises(ValueError):
            record_preview_observation(preview, refresh_evidence={"status": "RELOAD_FAILED"}, browser_observation=packet())
```

- [ ] **Step 3: RED overlay authority/capture tests**

```python
class RuntimeV11OverlayTests(unittest.TestCase):
    def test_overlay_rejects_taste_or_release_authority(self):
        bad = valid_overlay() | {"beauty_score": 10, "winner": "A"}
        self.assertFalse(validate_overlay_packet(bad)["valid"])

    def test_overlay_preserves_attribution_ambiguity(self):
        packet = build_overlay_packet(attribution={"status": "AMBIGUOUS", ...}, ...)
        self.assertEqual(packet["source_attribution_status"], "AMBIGUOUS")
```

- [ ] **Step 4: Run RED tests**

- [ ] **Step 5: Implement immutable dict-based preview records with closed state enum and digest freshness checks**

Rules:
- state changes return new records; input record is never mutated;
- no filesystem write API exists in `preview.py`;
- `record_preview_observation` needs `HMR_OK` or `RELOAD_OK` plus a valid canonical browser packet;
- capture refs are copied only from the validated browser observation for the same preview/revision context;
- all records declare narrow claim boundaries.

- [ ] **Step 6: Implement overlay as pure evidence view-model**

Rules:
- explicitly reject `beauty_score`, `winner`, `verified`, `released`, generator preference/self-score fields;
- include runtime finding IDs, source attribution state, source digest, preview state, capture refs, and capability gaps;
- never synthesize source certainty.

- [ ] **Step 7: Add schemas and run focused GREEN**

- [ ] **Step 8: Commit Task 3**

Commit message: `feat(v11): add immutable live preview and overlay evidence`

---

### Task 4: Playwright Reference Adapter + Real Browser Smoke Gate

**Files:**
- Create: `src/nolane_ui/runtime_v11/playwright_adapter.py`
- Create: `tests/test_runtime_v11_playwright_adapter.py`
- Create: `tests/fixtures/runtime_v11/live_visual_smoke.html`
- Modify: `pyproject.toml`
- Modify: `.github/workflows/verify.yml`

**Interfaces:**
- Produces: `playwright_available() -> bool`
- Produces: `playwright_capability() -> dict`
- Produces: `collect_playwright_observation(url: str, *, selector: str, viewport: dict, capture_path: str | None = None) -> dict`
- Produces: `refresh_playwright_preview(page, *, prefer_hmr: bool, hmr_bridge: callable | None = None) -> dict`

- [ ] **Step 1: RED import-optional test**

```python
class RuntimeV11PlaywrightAdapterTests(unittest.TestCase):
    def test_core_import_does_not_require_playwright(self):
        import nolane_ui.runtime_v11
        self.assertTrue(hasattr(nolane_ui.runtime_v11, "validate_browser_observation"))
```

- [ ] **Step 2: RED capability/normalization tests using fake page objects only for contract behavior**

```python
    def test_adapter_output_must_pass_canonical_browser_validator(self):
        packet = normalize_collected_page(fake_page())
        self.assertTrue(validate_browser_observation(packet)["valid"])
```

- [ ] **Step 3: RED HMR fallback tests**

```python
    def test_failed_hmr_falls_back_to_reload(self):
        result = refresh_preview(fake_page(reload_ok=True), prefer_hmr=True, hmr_bridge=lambda _: False)
        self.assertEqual(result["status"], "RELOAD_OK")
        self.assertEqual(result["hmr_status"], "HOT_RELOAD_FAILED")
```

- [ ] **Step 4: Implement adapter with lazy Playwright import**

Rules:
- module import never imports Playwright at top level;
- `playwright_available()` uses import discovery;
- collector creates canonical V11 browser packet and then calls `validate_browser_observation`/`normalize_browser_observation` before returning;
- collect geometry, selected computed-style keys, document metrics, page errors/console errors, target metadata, screenshot ref if requested;
- target is re-selected after reload/refresh;
- provider metadata stays adapter-scoped.

- [ ] **Step 5: Add optional dependency**

Update `pyproject.toml`:

```toml
[project.optional-dependencies]
mcp = ["mcp>=2,<3"]
live = ["playwright>=1.62,<2"]
```

- [ ] **Step 6: Add real-browser smoke test**

The test must:
- launch real Chromium with `sync_playwright()`;
- load the fixture through a `file://` URL or a local standard-library HTTP server;
- select `#nui-smoke-target`;
- collect a canonical packet with non-empty geometry/computed style/document metrics;
- create a screenshot capture path;
- assert `validate_browser_observation(packet)["valid"] is True`;
- assert the target text and bounding box are real observed values;
- never skip when running under CI's Phase 5 smoke step.

- [ ] **Step 7: Modify GitHub Actions so the real browser gate cannot silently skip**

Add before the regular test step:

```yaml
      - name: Install Phase 5 live browser dependencies
        run: |
          python -m pip install -e '.[live]'
          python -m playwright install --with-deps chromium

      - name: Run Phase 5 real Chromium smoke gate
        env:
          NUI_REQUIRE_REAL_PLAYWRIGHT: "1"
        run: PYTHONPATH=src python -m unittest tests.test_runtime_v11_playwright_adapter.RuntimeV11PlaywrightRealSmokeTests -v
```

The smoke test must fail, not skip, when `NUI_REQUIRE_REAL_PLAYWRIGHT=1` and Playwright/Chromium are unavailable.

- [ ] **Step 8: Run focused adapter tests and CI smoke gate; commit**

Commit message: `feat(v11): add real Playwright live visual adapter`

---

### Task 5: Live Visual Coordinator and Capability-Scoped Closure

**Files:**
- Create: `src/nolane_ui/runtime_v11/live_visual.py`
- Create: `tests/test_runtime_v11_live_visual.py`
- Modify: `src/nolane_ui/runtime_v11/reobserve.py`
- Modify: `src/nolane_ui/runtime_v11/live.py`

**Interfaces:**
- Produces: `prepare_live_visual_selection(...) -> dict`
- Produces: `prepare_live_visual_preview(...) -> dict`
- Produces: `accept_live_visual_preview(...) -> dict`
- Produces: `assess_visual_observation_capabilities(requirements: dict, available: dict) -> dict`
- Reuses: `transactional_replace`, `browser_observation_findings`, `compare_runtime_observations`, `append_live_event`

- [ ] **Step 1: RED end-to-end orchestration tests with in-memory/fake transport**

```python
class RuntimeV11LiveVisualTests(unittest.TestCase):
    def test_ambiguous_attribution_blocks_preview_apply(self):
        result = prepare_live_visual_selection(...ambiguous...)
        self.assertEqual(result["status"], "BLOCKED")
        self.assertEqual(result["failure"], "ATTRIBUTION_AMBIGUOUS")

    def test_source_edit_during_preview_returns_apply_conflict(self):
        preview = prepare_live_visual_preview(...)
        self.source.write_text("newer edit")
        result = accept_live_visual_preview(preview, ...)
        self.assertEqual(result["status"], "APPLY_CONFLICT")
```

- [ ] **Step 2: RED capability-scoped closure tests**

```python
    def test_missing_occlusion_only_keeps_occlusion_assertion_unknown(self):
        result = assess_visual_observation_capabilities(
            {"overflow": ["document_metrics"], "occlusion": ["occlusion"]},
            {"document_metrics": True, "occlusion": False},
        )
        self.assertEqual(result["assertions"]["overflow"], "READY")
        self.assertEqual(result["assertions"]["occlusion"], "UNKNOWN")
```

- [ ] **Step 3: Extend re-observation without breaking existing coarse API**

Keep `compare_runtime_observations(..., capabilities_complete=True)` backward compatible. Add an optional capability-scoped mapping parameter so a prior finding can become `RESOLVED` only if that rule/scope's required capabilities are complete; unrelated findings can still resolve.

- [ ] **Step 4: Implement coordinator using composition only**

Rules:
- no duplicate source write primitive;
- preview observation must be proven before accept;
- acceptance passes last proven source digest to `transactional_replace`;
- post-apply must collect fresh browser observation before closure;
- after-only findings remain regressions;
- return `claim_boundary: live-visual-closure-only`.

- [ ] **Step 5: Add Live Lab journal payload linkage**

Add optional Phase 5 evidence refs (`source_attribution_ref`, `preview_id`, `capture_refs`, `transport_provider`) to relevant event payloads without allowing them to replace existing closure counters/decision.

- [ ] **Step 6: Run focused GREEN and all existing V11 live/reobserve tests**

- [ ] **Step 7: Commit Task 5**

Commit message: `feat(v11): orchestrate live visual preview and closure`

---

### Task 6: Runtime Doctor and Public API Integration

**Files:**
- Modify: `src/nolane_ui/runtime_v11/doctor.py`
- Modify: `src/nolane_ui/runtime_v11/__init__.py`
- Modify: `src/nolane_ui/__init__.py`
- Create: `tests/test_runtime_v11_phase5_integration.py`

**Interfaces:**
- Doctor must inventory all Phase 5 modules/schemas.
- Top-level exports use explicit runtime-prefixed aliases.

- [ ] **Step 1: RED Doctor artifact inventory test**

Expected required paths include:
- `schemas/runtime-source-attribution-v11.schema.json`
- `schemas/runtime-browser-transport-v11.schema.json`
- `schemas/runtime-live-preview-v11.schema.json`
- `schemas/runtime-live-overlay-v11.schema.json`
- `src/nolane_ui/runtime_v11/source_attribution.py`
- `src/nolane_ui/runtime_v11/browser_transport.py`
- `src/nolane_ui/runtime_v11/playwright_adapter.py`
- `src/nolane_ui/runtime_v11/preview.py`
- `src/nolane_ui/runtime_v11/overlay.py`
- `src/nolane_ui/runtime_v11/live_visual.py`

- [ ] **Step 2: RED public API test**

Assert callability of source-attribution, transport, preview, overlay, Playwright availability/collection, and live-visual coordinator APIs through both `runtime_v11` and explicit `nolane_ui` aliases.

- [ ] **Step 3: RED ownership test**

Assert no Phase 5 module/schema name appears in `skills/skill-graph.json`, graph count is exactly 874, and public APIs retain non-release claim boundaries.

- [ ] **Step 4: Implement Doctor/public exports and run GREEN**

- [ ] **Step 5: Commit Task 6**

Commit message: `feat(v11): integrate live visual runtime with doctor and public API`

---

### Task 7: Documentation, Full Gate, Exact-Head Proof, PR Update

**Files:**
- Modify: `docs/RUNTIME-DESIGN-INTELLIGENCE.md`
- Modify: `docs/superpowers/plans/2026-08-21-v11-live-visual-runtime-implementation.md`
- Modify: PR #22 body after final exact-head verification only.

- [ ] **Step 1: Update runtime architecture docs**

Document:
- source attribution status/authority rules;
- browser transport capability negotiation;
- Playwright as reference adapter, not core authority;
- immutable preview lifecycle;
- HMR/reload fallback;
- overlay evidence-only boundary;
- real-browser smoke requirement;
- current remaining limitations (no browser extension UX, no universal framework source mapper, no global HMR bridge).

- [ ] **Step 2: Run full unit/contract suite**

Run: `PYTHONPATH=src python -m unittest discover -s tests -v`

Expected: all tests PASS, including Phase 1–5 and Batch 006.

- [ ] **Step 3: Run required real Chromium smoke gate separately**

Run with `NUI_REQUIRE_REAL_PLAYWRIGHT=1`; expected PASS without skip.

- [ ] **Step 4: Generate fresh bounded completion packet for exact head**

Use existing `scripts/nui-release-packet` with exact CI SHA.

- [ ] **Step 5: Run exact-revision repository validator**

Expected:
- `valid: true`
- `errors: []`
- `warnings: []`
- `skill_count: 874`
- `declared_skill_count: 874`
- completion decision `PASS`.

- [ ] **Step 6: Audit PR changed paths**

Expected: zero paths under `skills/`; `skills/skill-graph.json` absent from changed paths.

- [ ] **Step 7: Confirm GitHub Actions artifacts**

Record workflow run/job IDs plus completion-packet and complete-project artifact IDs/digests.

- [ ] **Step 8: Mark plan complete using actual evidence**

Replace unchecked implementation boxes with checked boxes only after their corresponding tests/CI evidence exists. Do not predeclare completion.

- [ ] **Step 9: Update PR #22 body without changing branch SHA**

Include:
- Phase 5 architecture;
- real-browser smoke evidence;
- exact head;
- current test count;
- 874/874 skill count;
- validator/packet results;
- artifact IDs/digests;
- explicit current limitation boundary;
- no auto-merge.
