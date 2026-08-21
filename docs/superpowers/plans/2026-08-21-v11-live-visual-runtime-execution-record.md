# NUI V11 Phase 5 — Live Visual Runtime Execution Record

This record closes the implementation plan in `2026-08-21-v11-live-visual-runtime-implementation.md` without rewriting the original TDD instructions after every checkpoint. The original plan remains the historical execution contract; this file records what actually happened.

## Scope and authority boundary

- Canonical graph remains exactly **874 skills**.
- Phase 5 adds no canonical skill and does not modify `skills/skill-graph.json`.
- Rendered identity is evidence, never automatic source authority.
- Browser transports, previews, overlays, and runtime closure remain non-release-authoritative.
- PR #22 remains unmerged unless explicitly authorized.

## Task completion ledger

- [x] **Task 1 — Source Attribution Resolver**
  - Implemented `EXACT | CANDIDATE | AMBIGUOUS | UNKNOWN` attribution.
  - Added digest binding, repository-root canonicalization, traversal/symlink escape rejection, and explicit candidate selection.
  - `UNKNOWN` cannot authorize mutation.

- [x] **Task 2 — Browser Transport Capability Contract**
  - Added closed capability vocabulary and provider-neutral `READY | UNKNOWN` negotiation.
  - Provider identity cannot elevate design or release authority.

- [x] **Task 3 — Immutable Preview Runtime and Overlay Evidence**
  - Added immutable preview state with digest freshness and no canonical source writes before explicit acceptance.
  - Added evidence-only overlay that preserves source ambiguity/capability gaps and rejects taste/release authority.

- [x] **Task 4 — Playwright Reference Adapter + Real Browser Smoke Gate**
  - Added lazy optional Playwright adapter so core imports remain dependency-independent.
  - Added real Chromium collection, ephemeral preview injection, caller-supplied HMR support, bounded reload fallback, screenshot evidence, geometry/computed-style/document-metric/runtime-error collection.
  - GitHub Actions installs the `live` extra + Chromium and executes a non-skippable real-browser smoke gate with `NUI_REQUIRE_REAL_PLAYWRIGHT=1`.

- [x] **Task 5 — Live Visual Coordinator and Capability-Scoped Closure**
  - Added fail-closed rendered-target selection.
  - Added non-destructive preview preparation and conflict-safe observed-preview acceptance through existing `transactional_replace()`.
  - Extended re-observation with optional per-rule capability completeness while preserving the coarse API.
  - Missing capability leaves only affected assertions/rules `UNKNOWN`.
  - Successful source apply explicitly requires fresh post-apply observation.

- [x] **Task 6 — Runtime Doctor and Public API Integration**
  - Doctor inventories Phase 5 schemas/modules.
  - `nolane_ui.runtime_v11` exposes the Phase 5 protocol surface.
  - top-level `nolane_ui` exposes explicit runtime-prefixed aliases.
  - Integration tests prove Phase 5 remains outside the 874-skill graph.

- [x] **Task 7.1 — Runtime architecture documentation**
  - `docs/RUNTIME-DESIGN-INTELLIGENCE.md` now documents the concrete Phase 5 runtime and removes the pre-Phase-5 limitation claim.
  - Remaining limitations are explicit: no browser-extension UX, no universal framework source mapper, no global HMR bridge.

## TDD evidence checkpoints

The implementation used explicit RED -> GREEN progression rather than post-hoc tests.

### Playwright adapter RED/GREEN

The adapter contract initially failed because the API did not exist. The GREEN implementation kept Playwright lazy/optional. CI subsequently proved a **real Chromium** run rather than accepting a skipped/mocked browser claim.

### Live Visual Coordinator RED/GREEN

The coordinator RED checkpoint introduced four focused missing behaviors: attribution ambiguity blocking, per-assertion capability truth, source-edit conflict safety, and rule-scoped re-observation. Production code was added only after those failures were observed.

A second RED checkpoint added `prepare_live_visual_preview`; the full suite showed exactly the two new failures while all prior tests remained green. The GREEN implementation composed existing preview/transport contracts without adding a second source-write path.

### Task 6 integration RED/GREEN

RED commit: `146a34e006db8c37a0c757838cfa1db01c12164b`.

GitHub Actions run `32484257407` executed **585 tests** and failed only the three intended integration gaps:

1. Phase 5 artifacts missing from Doctor inventory;
2. Phase 5 runtime APIs missing from `nolane_ui.runtime_v11`;
3. top-level runtime-prefixed aliases missing.

The real Chromium smoke gate still passed in that RED run, and the graph-isolation test still confirmed 874 canonical skills.

GREEN checkpoint head: `9c66c0ae8a18d0defc370e3e478eeeb6228f3299`.

GitHub Actions run `32485623676`, job `96781356778`, passed every gate:

- real Chromium smoke: PASS, non-skipped;
- **585 / 585** unit/contract tests: PASS (`Ran 585 tests in 62.655s`, `OK`);
- fresh bounded completion packet: PASS;
- exact-revision repository validation: PASS;
- repository `valid: true`, `errors: []`, `warnings: []`;
- `skill_count: 874`, `declared_skill_count: 874`, `skill_contracts_checked: 874`;
- completion decision: `PASS`, errors `[]`;
- completion packet artifact ID `9447771518`, uploaded ZIP SHA-256 `6fdf836aef34ad55731b07e52f5755948172ecf84a5c6a2ae4fc7522d4a63280`;
- complete-project artifact ID `9447772159`, uploaded ZIP SHA-256 `60dde1cf2e717082070606222dd37ec3b1497893baf72baf32001baf48b9367d`.

That GREEN checkpoint predates the final documentation commit and is therefore historical evidence, not the authoritative Phase 5 final head.

## Final exact-head protocol

The documentation/execution-record head must now pass the same non-skippable sequence:

- [ ] real Chromium smoke gate;
- [ ] all unit/contract tests;
- [ ] fresh bounded completion packet;
- [ ] exact-revision repository validator with `874 / 874` skills and no errors/warnings;
- [ ] complete project packaging/upload;
- [ ] PR changed-path audit with **zero** paths under `skills/` and no `skills/skill-graph.json`;
- [ ] final workflow/job and artifact IDs/digests recorded in PR #22 body.

The authoritative final proof is intentionally recorded in **PR metadata after CI**, because updating PR metadata does not change the branch SHA. This avoids invalidating the exact-head proof merely by writing the proof back into the repository.
