# NUI V11 Runtime Design Intelligence

NUI V11 adds deterministic runtime perception, generation governance, live visual iteration, and evidence closure beneath the canonical NUI cognition graph. It does **not** add canonical skills, replace routed design owners, or let a clean scan, selected direction, taste preference, preview, browser observation, or closed live session become release authority by itself.

The integrated Batch 006 baseline contains exactly **874 canonical skills**. V11 remains outside that graph. Runtime rules observe implementation state; canonical skills still own design reasoning and repair decisions; completion gates still own product/release claims.

The governing separation is:

```text
Skills / cognition
  -> design reasoning and decisions
Runtime rules / perception
  -> deterministic source/browser observations
Adjudication + owner routing
  -> finding / accepted exception / unknown
Evidence + re-observation
  -> resolved / persisted / unknown / regression
Generation governance
  -> bounded divergence, genericity, taste comparison, residue passes
Live Visual Runtime
  -> source attribution, immutable preview, browser transport, conflict-safe apply
Existing NUI completion authority
  -> final product/release interpretation
```

A runtime rule is therefore a machine-observation contract, not a new skill category. A Playwright adapter is a transport provider, not design authority. A live preview is a candidate, not canonical source. A clean runtime closure is bounded evidence, not a product-wide proof.

---

## 1. Runtime rule model

The canonical runtime registry is `knowledge/runtime-detector-rules-v11.json`. Rules are independently authored NUI contracts and are intentionally absent from `skills/skill-graph.json`.

Each rule declares a stable `rule_id`, domain, class, tier, severity, supported engines, falsifier, owner hints, and provenance. The four rule classes are:

- `mechanical`: high-confidence implementation failures;
- `contextual`: suspicious states that require product/platform/design-system authority;
- `genericness`: convergence signals that can support anti-generic critique but cannot prove bad design alone;
- `advisory`: craft observations that may inform critique but cannot act as automatic blockers.

Genericness and advisory rules are prohibited from becoming edit-time blockers. Provenance uses `implementation: independently-authored`; optional `research_inspiration` records conceptual research without implying implementation transfer. The legacy `mechanism_sources` field is rejected.

The Phase 4/5 registry currently contains **16 independently authored runtime rules**. Owner hints are routing suggestions only and must resolve to existing canonical skills. V11 never synthesizes an owner merely to make routing appear complete.

---

## 2. Execution tiers

V11 separates runtime observation into three tiers.

### EDIT

The smallest deterministic pass for post-write/preflight feedback:

```bash
python scripts/nui-detect <file-or-directory> --tier edit
```

Only eligible mechanical checks belong here. A host without a genuine blocking lifecycle must not pretend to provide one.

### SESSION

The broader UI pass where contextual, genericness, advisory, and craft-floor observations can surface:

```bash
python scripts/nui-detect <file-or-directory> --tier session
```

These findings route to existing NUI owners for interpretation; the detector does not become a second design court.

### RELEASE

Release-relevant runtime evidence may combine source and browser observations with freshness checks. Missing capability remains `UNKNOWN`/`BLOCKED`, never false PASS.

A clean detector result means only that no registered rule produced a finding for the observed scope. It does not mean the UI is accessible, responsive, product-complete, beautiful, verified, or releasable.

---

## 3. Source detector and adjudication

`src/nolane_ui/runtime_v11/detector.py` performs dependency-free source observation over common web UI files. It reports the evidence and engine it actually used; text heuristics are never silently upgraded into AST/browser certainty.

`src/nolane_ui/runtime_v11/adjudication.py` keeps observation separate from disposition. Contextual matches can remain unknown; accepted exceptions require explicit, narrow scope and authority. Broad wildcard suppression is rejected.

---

## 4. Finding-to-owner routing

`src/nolane_ui/runtime_v11/routing.py` intersects each rule's owner hints with the supplied canonical graph.

Outcomes are:

- `ROUTED`: one or more hinted canonical owners exist;
- `UNRESOLVED`: the rule is known but none of its hints resolve;
- `UNKNOWN_RULE`: the finding references a rule absent from the registry.

Unknown hints remain visible. Batch 006 integration re-audited the hints against all 874 canonical skills and repaired historical naming drift without creating aliases or new skills.

---

## 5. Agent hook boundary

`src/nolane_ui/runtime_v11/hooks.py` projects the same canonical detector into supported hosts. The invariant is:

```text
one canonical detector -> many thin host projections
```

Codex, Claude, Cursor, and generic hosts may expose different lifecycle capabilities, but a missing host feature remains missing capability rather than simulated certainty.

---

## 6. Browser observation and transport contracts

The core browser observation boundary remains provider-neutral. `schemas/runtime-browser-observation-v11.schema.json` describes canonical packets containing collector identity, URL, viewport, capability declaration, element observations, runtime errors, optional document metrics, and optional capture evidence.

`src/nolane_ui/runtime_v11/browser.py` validates/normalizes those packets and derives supported browser findings such as runtime errors, document horizontal overflow, and explicit text occlusion. Missing geometry, occlusion, capture, or document metrics cannot be interpreted as clean evidence for that dimension.

Phase 5 adds `schemas/runtime-browser-transport-v11.schema.json` and `src/nolane_ui/runtime_v11/browser_transport.py`. Transport capability is explicit and closed-vocabulary. `require_transport_capabilities()` returns `READY` or `UNKNOWN`; provider identity never upgrades authority.

### Concrete Playwright reference adapter

`src/nolane_ui/runtime_v11/playwright_adapter.py` is the first concrete reference transport. It is deliberately **optional**: the core package performs no top-level Playwright import, so `nolane_ui.runtime_v11` remains importable without the `live` extra.

The adapter can:

- launch real Chromium and navigate to a target URL;
- collect target geometry, selected computed styles, rendered attributes/text, document metrics, page/console errors, and optional screenshot evidence;
- validate and normalize the result through the canonical browser packet contract before returning it;
- inject an **ephemeral browser-only preview** into a selected rendered node;
- prefer a caller-supplied HMR bridge when available and fall back to bounded page reload when HMR is unavailable or fails.

The adapter explicitly reports `hot_reload: false` because NUI does not ship a universal project HMR bridge. It reports `reload: true`. Occlusion is also not claimed by the reference adapter unless a future collector implements that capability.

The CI workflow installs the optional `live` dependency and a real Chromium build, then runs `RuntimeV11PlaywrightRealSmokeTests` with `NUI_REQUIRE_REAL_PLAYWRIGHT=1`. Under that gate Playwright/Chromium absence is a failure, not a skip.

Current limitations are precise: **no browser-extension UX, no universal framework source mapper, and no global HMR bridge**. Those are future integration surfaces, not hidden capabilities.

---

## 7. Revision-bound evidence

`src/nolane_ui/runtime_v11/evidence.py` binds evidence to the source scope it actually certifies using source digests rather than repository-wide commit count.

Freshness outcomes are:

- `CURRENT`: every bound source digest still matches;
- `STALE`: at least one overlapping source changed;
- `UNKNOWN`: current state cannot be observed for at least one required source.

Unrelated source changes do not invalidate scoped evidence; overlapping changes cannot leave old evidence silently current.

---

## 8. Deterministic repair closure

`src/nolane_ui/runtime_v11/reobserve.py` compares bounded before/after finding sets. Matching is conservative and multiset-safe across rule identity and observed scope.

Each prior finding becomes:

- `PERSISTED` when the same scoped finding remains;
- `RESOLVED` only when it is absent and the required re-observation capability is complete;
- `UNKNOWN` when it is absent but required capability is incomplete.

After-only findings are regressions. Phase 5 extends the API with optional `capabilities_by_rule`, so missing capability for one rule does not force unrelated assertions to become unknown. The coarse `capabilities_complete` API remains backward compatible.

Aggregate decisions remain `CLEAN`, `OPEN`, or `UNKNOWN`, with `claim_boundary: runtime-closure-only`.

---

# Phase 4 — Aesthetic Generation Governor

Phase 4 addresses the case where an AI can satisfy component requirements yet repeatedly converge on visually generic UI. It changes the **search and judgment protocol** rather than prescribing a house style:

```text
UI contract + task/profile + experiential intent + authority
  -> Design Intent Compiler
  -> materially divergent candidate directions
  -> Generation Governor
  -> committed direction (not verified)
  -> dynamic Genericity / Craft Floor observations
  -> project-local Design Memory
  -> blinded multi-dimensional Taste Court
  -> bounded Quality Residue pass
  -> runtime re-observation / evidence gates
  -> existing NUI completion authority
```

The generator may propose; it may not self-certify.

---

## 9. Design Intent Compiler

`src/nolane_ui/runtime_v11/aesthetic_intent.py` compiles supplied product/design context into a machine-readable generation contract. It records protected axes, forbidden moves, aspirations, mutable axes, and explicit redesign authority.

Redesign authority is never inferred from ambition. The result declares `claim_boundary: generation-intent-only`.

---

## 10. Generation Governor and material divergence

`src/nolane_ui/runtime_v11/aesthetic_governor.py` evaluates direction candidates on causal axes such as information hierarchy, interaction model, signature mechanism, spatial composition, product metaphor, and motion logic.

Palette/radius/shadow-only variants are not materially distinct directions. Identity-locked violations invalidate candidates. Missing render evidence remains unknown.

`commit_direction()` records `claim_boundary: generation-direction-commit-only`; `COMMITTED` never means `VERIFIED` or `RELEASED`.

---

## 11. Dynamic Genericity Engine

`src/nolane_ui/runtime_v11/genericity.py` and `knowledge/aesthetic-trend-tells-v11.json` separate stable structural convergence from time-bounded trend tells. Tells carry provenance, falsifiers, status, and `review_after` metadata so a fashionable anti-pattern cannot become permanent dogma.

Genericity uses accumulation, not singleton matches and not an opaque scalar AI score. `product_substitution_assessment()` separately reports interchangeability evidence without turning it into a beauty score.

---

## 12. Craft Floor runtime perception

Phase 4 adds three session-tier, observation-only genericness signals:

1. `runtime.genericness.decorative-pill-saturation`
2. `runtime.genericness.all-caps-micro-label-accumulation`
3. `runtime.genericness.uniform-boundary-accumulation`

They are accumulation detectors, not style bans. Semantic status/category/filter/metadata pills, legitimate identifiers/table/axis labels, and justified independent object/state/interaction boundaries are protected counterexamples.

The governing logic is:

```text
bad approach: familiar pattern -> ban it
NUI approach: repeated convergence signal -> inspect accumulation -> require semantic/product justification -> route to existing owner -> compare rendered alternatives
```

---

## 13. Project-local Design Memory

`src/nolane_ui/runtime_v11/design_memory.py` preserves accepted/rejected mechanisms and identity constraints for one project/revision/source scope. It never becomes a global NUI house style.

Overlapping changes can make memory `STALE`; missing source state yields `UNKNOWN`; unrelated changes leave it `CURRENT`.

---

## 14. Blinded Taste Court

`src/nolane_ui/runtime_v11/taste_court.py` strips generator preference, self-score, reference prestige, and scalar beauty fields before comparative judgment. Supported per-dimension verdicts include `LEFT`, `RIGHT`, `TIE`, and `UNJUDGABLE`.

Accessibility/product-truth blockers are non-compensatory. The result remains `claim_boundary: taste-comparison-only`.

---

## 15. Bounded Quality Residue Loop

`src/nolane_ui/runtime_v11/quality_residue.py` distinguishes micro-craft debt from a wrong design thesis. Small bounded polish is allowed only after macro direction is stable. A false thesis or exhausted polish budget returns `RE_DIVERGE` instead of endless ornamentation.

Residue closure uses `claim_boundary: quality-residue-only` and never upgrades to release authority.

---

# Phase 5 — Live Visual Runtime

Phase 5 closes the loop between rendered evidence and conflict-safe source iteration without making browser identity a source-of-truth shortcut.

```text
rendered target
  -> source attribution
  -> explicit source selection when needed
  -> immutable preview candidate
  -> transport capability check
  -> ephemeral browser injection
  -> refresh (HMR if supplied, otherwise reload)
  -> canonical browser observation
  -> evidence-only overlay
  -> explicit accept
  -> transactional source apply with digest guard
  -> fresh post-apply observation
  -> capability-scoped re-observation closure
```

Every arrow has an uncertainty boundary. Missing mapping, transport, refresh, observation, or freshness evidence leaves the affected step blocked/unknown rather than silently clean.

---

## 16. Fail-closed source attribution

`src/nolane_ui/runtime_v11/source_attribution.py` and `schemas/runtime-source-attribution-v11.schema.json` define four states:

- `EXACT`
- `CANDIDATE`
- `AMBIGUOUS`
- `UNKNOWN`

A rendered locator is evidence, not mutation authority. Candidate paths are canonicalized inside the repository root, symlink/parent/absolute escapes are rejected, and source digests must still match. Provider metadata alone cannot force exactness.

`CANDIDATE` and `AMBIGUOUS` require explicit candidate selection. `UNKNOWN` can never authorize source mutation.

---

## 17. Immutable preview lifecycle

`src/nolane_ui/runtime_v11/preview.py` and `schemas/runtime-live-preview-v11.schema.json` implement immutable preview records with closed states including `PREPARED`, `INJECTED`, `OBSERVED`, `STALE`, `CONFLICT`, `REJECTED`, and `ACCEPTED`.

Building or transitioning a preview never writes canonical source. The preview records the base source digest and becomes stale if that source changes. Observation requires successful `HMR_OK` or `RELOAD_OK` evidence plus a valid canonical browser packet.

The preview boundary is `claim_boundary: preview-transport-only`.

---

## 18. Evidence-only overlay

`src/nolane_ui/runtime_v11/overlay.py` and `schemas/runtime-live-overlay-v11.schema.json` expose a pure evidence view-model containing rendered identity, source-attribution status, selected source only when exact, preview state, capture refs, runtime finding IDs, capability gaps, and optional re-observation summary.

Overlay packets reject unsupported authority fields. They cannot declare a beauty winner, `VERIFIED`, `RELEASED`, or silently upgrade ambiguous/unknown source attribution.

The overlay boundary is `claim_boundary: overlay-evidence-only`.

---

## 19. Live Visual Coordinator and conflict-safe apply

`src/nolane_ui/runtime_v11/live_visual.py` composes the existing contracts rather than inventing a second mutation system.

`prepare_live_visual_selection()` resolves attribution and blocks ambiguous/unknown mutation unless explicit selection is valid. `prepare_live_visual_preview()` builds a non-destructive preview, checks freshness, and checks transport capability before returning a preview that is ready for provider injection.

`accept_live_visual_preview()` requires an `OBSERVED` preview, rechecks source freshness, and delegates the canonical write to existing `transactional_replace()`. If another editor changed the source during preview, acceptance returns `APPLY_CONFLICT`/`SOURCE_STALE` and preserves the newer file.

A successful apply sets `requires_fresh_observation: true`; pre-apply preview evidence is not recycled as proof of post-apply closure.

The coordinator boundary is `claim_boundary: live-visual-closure-only`.

---

## 20. Live Lab journal and transactional safety

`src/nolane_ui/runtime_v11/live.py` remains the session/journal/source-safety foundation. Normal progression is:

```text
SELECTED
  -> CONTEXT_BOUND
  -> VARIANTS_READY
  -> PREVIEWING
  -> ACCEPTED
  -> APPLIED
  -> REOBSERVED
  -> CLOSED
```

`transactional_replace()` uses optimistic concurrency with initial and final pre-commit digest/existence guards followed by atomic filesystem replace. It is intentionally described as optimistic concurrency, not mathematical lock-free cross-process CAS.

Live session closure is not product release. `OPEN` or `UNKNOWN` re-observation may still end an interactive session; the journal records that the session ended, not that NUI completion gates passed.

---

## 21. Runtime Doctor

`scripts/nui-runtime-doctor` is read-only. It reports installation/schema drift, evidence freshness problems, and capability gaps.

`REQUIRED_RUNTIME_ARTIFACTS` now covers the detector/browser/evidence/live foundation, Phase 4 generation-governance artifacts, and all Phase 5 source-attribution, browser-transport, preview, overlay, Playwright, and live-visual coordinator modules/schemas.

Doctor never redesigns the product, rewrites context, mutates source, or infers product truth from repository churn.

---

## 22. Public API boundaries

The top-level `nolane_ui` package exposes explicit runtime-prefixed aliases so consumers can use supported contracts without importing private modules.

Phase 4 exposes intent compilation, direction evaluation/commit, genericity/product-substitution assessment, project design memory, blinded taste court, and quality-residue planning/closure.

Phase 5 additionally exposes explicit aliases for:

- source-attribution validation/resolution/selection;
- browser transport validation/build/requirement checks;
- preview validation/build/freshness/application/observation;
- overlay validation/build;
- Playwright availability/capability/refresh/injection/collection;
- live visual selection/preview/acceptance;
- per-assertion visual observation capability assessment.

These are protocol/runtime APIs. None bypasses canonical skills or completion gates.

---

## 23. Verification and TDD boundary

V11 Phase 4 and Phase 5 were implemented through explicit RED -> GREEN cycles. Phase 5 specifically proved missing APIs first, then added the smallest production contracts needed to satisfy them. The Playwright transport was separately proven with a real Chromium smoke gate rather than a mock-only claim.

Before this documentation revision, the Task 6 GREEN checkpoint at branch head `9c66c0ae8a18d0defc370e3e478eeeb6228f3299` passed:

- real Chromium smoke: PASS, non-skipped;
- **585 / 585** unit/contract tests: PASS;
- fresh bounded completion packet generation: PASS;
- exact-revision repository validation: PASS;
- repository `valid: true`, `errors: []`, `warnings: []`;
- `skill_count: 874`, `declared_skill_count: 874`;
- completion decision: `PASS`;
- complete project packaging/upload: PASS.

That checkpoint is intentionally **not** called the final documentation head. Task 7 must run the same proof again after this documentation commit so documentation cannot create an unverified newer SHA. The authoritative final exact-head run is recorded in PR #22 after the documentation head passes.

---

## 24. External architectural research

V11 studied `pbakaus/impeccable` as one external reference for general workflow ideas such as deterministic UI checks, edit/session feedback, browser-aware iteration, maintenance passes, and live visual workflows. This is **research inspiration only**.

NUI V11 does not incorporate Impeccable source code, detector rule text, skill bodies, schemas, thresholds, state machines, configuration formats, or implementation artifacts. V11 runtime code, Phase 4 generation-governance code, Phase 5 Live Visual Runtime code, rule wording, schemas, tests, thresholds, evidence semantics, routing, Doctor behavior, re-observation logic, and Live Lab protocol are independently designed and authored for NUI.

The historical file `docs/research/impeccable-runtime-mechanism-transfer-v11.md` remains only for link stability; its contents explicitly state that no implementation transfer occurred.

---

## 25. Non-goals and current limitation boundary

V11 does not:

- add runtime rules, generation protocols, browser transports, previews, or overlays as canonical skills;
- modify the 874-skill graph to make routing easier;
- create an owner when an owner hint cannot resolve;
- impose one NUI house style;
- treat a familiar component/pattern as automatically bad;
- use one scalar AI-looking/genericity/beauty score as aesthetic authority;
- infer redesign authority from visual ambition;
- let generator preference/reference prestige leak into blinded judging;
- allow an aesthetic win to compensate for accessibility/product-truth blockers;
- fabricate browser evidence when capability is unavailable;
- treat absence under incomplete observation as resolved;
- let a preview mutate canonical source before explicit acceptance;
- let ambiguous/unknown source attribution authorize mutation;
- reuse stale pre-apply evidence as post-apply proof;
- overwrite known concurrent source edits during live application;
- claim browser-extension UX that is not implemented;
- claim a universal framework/component source mapper;
- claim a global HMR bridge; HMR is caller-supplied and bounded reload is the built-in fallback;
- treat the concrete Playwright reference adapter as universal browser or design authority;
- make a clean scan, committed direction, taste win, residue closure, clean runtime closure, observed preview, or live-session close sufficient evidence of product completion;
- describe external research inspiration as copied/transferred implementation.

These boundaries are deliberate. V11 is intended to make NUI more observable, harder to game, less likely to converge on generic AI UI, and more disciplined about live visual evidence without making the canonical graph larger for its own sake.
