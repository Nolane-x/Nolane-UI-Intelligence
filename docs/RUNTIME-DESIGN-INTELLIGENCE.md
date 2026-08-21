# NUI V11 Runtime Design Intelligence

NUI V11 adds a deterministic runtime-perception and generation-governance layer beneath the canonical cognition graph. It does **not** add canonical skills, replace routed design owners, or turn a clean scan, selected direction, taste preference, or closed live session into release authority.

The canonical graph on the integrated Batch 006 baseline contains **874 skills**. V11 remains outside that graph. Its purpose is to make those owners harder to fool: observe concrete source/runtime conditions, preserve uncertainty, route evidence to real owners, govern how aesthetic directions are generated and compared, remember project-local decisions without creating a global house style, and prove whether bounded findings actually close after repair.

The architecture separates four responsibilities:

1. **Cognition owns design decisions.** Product truth, user/task modeling, authority, interaction semantics, accessibility intent, visual direction, repair strategy, and release interpretation remain owned by canonical NUI skills.
2. **Generation governance owns bounded search.** Phase 4 can compile design intent, require materially distinct candidates, detect convergence signals, blind comparative judging, and bound polish. It cannot grant redesign or release authority to itself.
3. **Runtime perception owns observation.** Source scans, browser packets, hook execution, finding routing, evidence fingerprints, re-observation comparison, and live-edit conflict checks produce evidence about implementation state.
4. **Evidence/completion gates own claims.** Runtime and generation evidence can support, block, or keep a claim unknown; V11 does not self-certify product quality or release readiness.

This is why V11 is not a lint pack and Phase 4 is not a style preset. A runtime rule is a machine-observation contract, while the Aesthetic Generation Governor constrains the search/evaluation process without prescribing one visual language.

---

## 1. Runtime rule model

The canonical runtime registry is `knowledge/runtime-detector-rules-v11.json`. Rules are independently authored NUI runtime contracts and are intentionally outside `skills/skill-graph.json`.

Each rule declares a stable `rule_id`, domain, class, tier, severity, supported engines, falsifier, owner hints, and provenance. Four classes are used:

- `mechanical`: high-confidence implementation failures that can usually be reported without product-specific interpretation;
- `contextual`: suspicious implementation states that require product, platform, design-system, or runtime authority before becoming confirmed violations;
- `genericness`: convergence signals that may reveal template habits but cannot prove bad design by themselves;
- `advisory`: craft/taste observations that can inform critique but cannot act as automatic blockers.

Genericness and advisory rules are prohibited from becoming edit-time blockers. That boundary prevents a detector from silently becoming aesthetic authority.

Runtime provenance is narrow by design. Every rule uses `implementation: independently-authored`; optional `research_inspiration` records conceptual areas that informed investigation. The legacy field name `mechanism_sources` is rejected because it can incorrectly imply transferred implementation.

At the current V11 Phase 4 boundary the registry contains **16 independently authored rules**. The first layers cover runtime integrity, accessibility mechanics, layout integrity, design-system drift, browser errors/overflow/occlusion, and initial genericness observations. Phase 4 adds three craft-floor accumulation signals described later in this document.

### Owner hints are not new owners

`owner_hints` are routing suggestions only. Every hint must resolve to a skill already present in the supplied canonical graph. V11 does not create an alias or new skill merely to make a detector route look complete.

For example, broken image-source integrity routes to the existing `validating-visual-asset-integration` owner because the failure is about an asset surviving integration/runtime state, not about inventing a new media skill.

---

## 2. Execution tiers

V11 uses three execution tiers so fast feedback and deep evidence do not compete.

### EDIT

The edit tier is the smallest deterministic pass. It is suitable for post-write or preflight hooks and focuses on high-confidence observations worth surfacing immediately.

```bash
python scripts/nui-detect <file-or-directory> --tier edit
```

A host with a genuine blocking pre-write mechanism may use eligible mechanical rules as a local edit guard. A host without that capability must not pretend to provide one.

### SESSION

The session tier evaluates the broader rule set over UI files touched during work. This is where contextual, genericness, advisory, and craft-floor observations can surface without turning every edit into a style gate.

```bash
python scripts/nui-detect <file-or-directory> --tier session
```

Session findings should be routed to existing NUI owners for interpretation and repair. The detector does not become a second design court.

### RELEASE

Release-time runtime evidence can combine source observations with browser/rendered observations and evidence freshness. Missing capability remains `UNKNOWN` or `BLOCKED`; it is never converted to PASS because a collector could not observe something.

A clean detector result therefore means only that no registered rule produced a finding for the observed scope. It does **not** mean the UI is accessible, responsive, correct, product-complete, beautiful, verified, or releasable.

---

## 3. Source detector and adjudication

`src/nolane_ui/runtime_v11/detector.py` provides dependency-free source observation for common web UI files. It reports the evidence and engine it actually used; it does not upgrade text heuristics into AST/browser certainty.

Findings use the NUI finding vocabulary and include source location, rule identity, evidence, impact, falsifier, repair guidance, severity, status, and runtime metadata. Stable ordering/deduplication keeps hook and CI output reproducible.

Observation and adjudication remain separate. A contextual source match can exist while the final disposition remains unknown. `src/nolane_ui/runtime_v11/adjudication.py` converts raw observations into confirmed findings, accepted narrow exceptions, or unknowns.

Exceptions require explicit scope and authority. Project-wide wildcard suppression is rejected. The goal is reviewable evidence, not a convenient path around feedback.

---

## 4. Finding-to-owner routing

`src/nolane_ui/runtime_v11/routing.py` converts runtime findings into **evidence-only repair routes**. Routing intersects a rule's `owner_hints` with the supplied canonical `skills/skill-graph.json`.

Possible outcomes are:

- `ROUTED`: at least one hinted canonical owner exists;
- `UNRESOLVED`: the rule exists but none of its hints resolve;
- `UNKNOWN_RULE`: the finding references a rule absent from the runtime registry.

Unknown hints remain visible. No skill is synthesized to hide the gap. The result always declares an evidence-only boundary: the selected skill still owns interpretation, repair strategy, and design decisions.

After integrating Batch 006, Phase 4 audited rule hints against the 874-skill graph and corrected historical naming drift such as old conceptual names for visual hierarchy, color, responsive layout, and media integration. The correction is a routing repair, not a new ownership layer.

---

## 5. Agent hook boundary

`src/nolane_ui/runtime_v11/hooks.py` describes runtime-detection capabilities for supported host projections. `build_agent_install_plan()` exposes those capabilities without escalating permissions or design authority.

The invariant is:

```text
one canonical detector -> many thin host projections
```

Codex, Claude, Cursor, and generic hosts may expose different lifecycle events, but they point to the same `scripts/nui-detect` implementation. Missing host behavior is represented as missing capability rather than simulated certainty.

---

## 6. Browser observation protocol

The core browser boundary is provider-neutral. A collector produces a versioned packet described by `schemas/runtime-browser-observation-v11.schema.json`.

Packets declare collector identity, URL, viewport, available observation capabilities, element observations, runtime errors, and optional capture reference. Capability declaration matters because absence is evidence: a packet without geometry cannot prove layout clean; a packet without occlusion capability cannot prove content unobstructed.

`browser_observation_findings()` currently converts supported observations into findings for runtime errors, document-level horizontal overflow, and explicit text occlusion.

The packet is transport-agnostic. A future Playwright driver, browser extension, MCP tool, Codex browser surface, or native bridge may produce it without changing the core contract.

**Current limitation:** V11 defines the browser observation protocol and conversion logic, but does not yet claim a complete first-party Playwright transport, browser overlay, source-map selector, or HMR live-preview system. Live Lab currently provides the safe state/journal/editing foundation for those future capabilities.

---

## 7. Revision-bound evidence

`src/nolane_ui/runtime_v11/evidence.py` binds evidence to the source scope it actually certifies using source digests rather than repository-wide commit count.

Freshness outcomes are:

- `CURRENT`: every bound source digest still matches;
- `STALE`: at least one overlapping source changed;
- `UNKNOWN`: current state cannot be observed for at least one required source.

Unrelated source changes do not invalidate scoped evidence. Conversely, an overlapping change cannot leave old evidence silently current.

This gives V11 a causal evidence boundary: screenshots, browser packets, runtime observations, and design-memory records remain valid only for the implementation/state they actually observed.

---

## 8. Deterministic repair closure

`src/nolane_ui/runtime_v11/reobserve.py` compares bounded before/after runtime finding sets so an agent cannot treat “I edited the code” as evidence that a defect disappeared.

Matching is conservative and multiset-safe across rule identity and observed scope. Each prior finding becomes:

- `PERSISTED` when the same scoped finding remains;
- `RESOLVED` only when it is absent and required re-observation capability is complete;
- `UNKNOWN` when it is absent but capability is incomplete.

After-only findings are regressions. Aggregate runtime closure is:

- `CLEAN`: all prior scoped findings resolved and no regression appeared;
- `OPEN`: at least one finding persisted or a regression appeared;
- `UNKNOWN`: at least one prior finding cannot be judged.

The comparator always returns `claim_boundary: runtime-closure-only`. `CLEAN` is therefore bounded runtime closure evidence, not product verification or release authority.

---

# Phase 4 — Aesthetic Generation Governor

Phase 4 attacks a different failure class: an AI can satisfy component-level requirements and still repeatedly converge on visually generic, over-familiar UI. The solution is not to add more style rules or tell the generator to “make it premium.” That usually creates a different form of sameness.

Phase 4 instead changes the **search and judgment protocol**:

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

The generator may propose. It may not self-certify.

---

## 9. Design Intent Compiler

`src/nolane_ui/runtime_v11/aesthetic_intent.py` converts supplied product/design context into a machine-readable generation contract described by `schemas/aesthetic-generation-intent-v11.schema.json`.

The compiler records axes that must be protected, forbidden moves, desired aspirations, mutable axes, and explicit redesign authority. It rejects conflicting axis declarations rather than guessing which side wins.

A crucial invariant is that redesign authority cannot be inferred from ambition. A request for exceptional quality does not automatically authorize changing product identity, interaction model, hierarchy, or information architecture. Only explicit authority can unlock redesign.

The compiled packet declares:

```text
claim_boundary = generation-intent-only
```

It is an input to creative search, not evidence that the resulting design is correct.

---

## 10. Generation Governor and material divergence

`src/nolane_ui/runtime_v11/aesthetic_governor.py` evaluates direction candidates before the system invests in polish.

Material divergence is measured on causal design axes such as:

- information hierarchy;
- interaction model;
- signature mechanism;
- spatial composition;
- product metaphor;
- motion logic.

Changing palette, radius, shadow, or decorative surface treatment while preserving the same causal structure is not treated as a genuinely different direction.

In identity-locked work, violating protected axes invalidates a candidate. A candidate cannot compensate for breaking identity by receiving a better aesthetic score elsewhere.

Missing render or interaction evidence remains unknown. The governor does not pretend a textual proposal has already survived rendered reality.

`commit_direction()` records a selected direction with:

```text
claim_boundary = generation-direction-commit-only
```

`COMMITTED` means “this is the direction to build/observe,” not `VERIFIED` and not `RELEASED`.

---

## 11. Dynamic Genericity Engine

`src/nolane_ui/runtime_v11/genericity.py` and `knowledge/aesthetic-trend-tells-v11.json` implement a deliberately time-bounded genericity layer.

The system rejects the idea of one permanent “AI look” blacklist. Convergence changes over time. Each trend tell therefore carries provenance, a falsifier, status, and a `review_after` date. Once the review horizon expires, the tell loses active decision weight until refreshed.

Genericity is based on **accumulation**, not a singleton match and not an opaque scalar AI score. One familiar pattern is not proof that a UI is generic.

The engine can return bounded dispositions such as:

- `SPECIFIC`;
- `WATCH`;
- `GENERICITY_DEBT`;
- `UNJUDGABLE`.

`product_substitution_assessment()` separately asks whether the same presentation could be substituted into unrelated products with little loss of meaning. That produces interchangeability evidence, not a beauty score.

---

## 12. Craft Floor runtime perception

Phase 4 extends the runtime registry with three evidence-bounded genericness observations:

1. `runtime.genericness.decorative-pill-saturation`
2. `runtime.genericness.all-caps-micro-label-accumulation`
3. `runtime.genericness.uniform-boundary-accumulation`

These are **accumulation detectors**, not style bans.

### Decorative pill saturation

The detector looks for repeated pill/badge/chip-shaped treatments that accumulate without clear state, category, filter, metadata, or interaction semantics. A single pill is not a failure. Semantic status/metadata usage is an explicit counterexample.

### All-caps micro-label accumulation

The detector looks for repeated small all-caps labels used as simulated sophistication without a real metadata/identifier/state/hierarchy role. Legitimate table headers, axis labels, identifiers, metadata and authorized typographic roles are counterexamples.

### Uniform boundary accumulation

The detector looks for repeated sibling card/panel/surface shells with equivalent containment that may be substituting boundaries for authored hierarchy. A boundary is justified when it represents a real independent object, state, interaction, or containment contract.

All three rules are session-tier `observation` signals. They cannot block edit-time work and they cannot overrule an explicit product/design justification. Their job is to create evidence for existing owners such as `preventing-generic-ui`, `crafting-typography`, `composing-layouts`, `directing-visual-hierarchy`, and component semantics.

This distinction is central to NUI's anti-AI-looking strategy:

```text
bad approach: familiar pattern -> ban it
NUI approach: repeated convergence signal -> inspect accumulation -> ask for semantic/product justification -> route to existing owner -> compare rendered alternatives
```

---

## 13. Project-local Design Memory

`src/nolane_ui/runtime_v11/design_memory.py` and `schemas/aesthetic-design-memory-v11.schema.json` preserve design decisions that are specific to one product/project.

Memory can contain accepted mechanisms, rejected mechanisms, identity constraints, provenance, and revision/source bindings. It does **not** become global NUI style law.

Freshness follows the same causal principles as V11 evidence:

- overlapping identity/design-system/source changes can make memory `STALE`;
- missing required source state yields `UNKNOWN`;
- unrelated changes leave it `CURRENT`.

This prevents two opposite failure modes: forgetting the product's own hard-won identity on every generation, and over-generalizing one project's taste into a universal house style.

---

## 14. Blinded Taste Court

`src/nolane_ui/runtime_v11/taste_court.py` and `schemas/aesthetic-taste-court-v11.schema.json` separate generation preference from comparative judgment.

Before judging, the packet strips fields that can anchor the judge on generator preference, self-score, reference prestige, or scalar “beauty” claims. Redaction metadata itself is also prevented from re-leaking the hidden fields.

Judgment is per dimension and evidence-bound. Supported verdicts include:

- `LEFT`;
- `RIGHT`;
- `TIE`;
- `UNJUDGABLE`.

A judgment records observable cause and evidence references. The court can preserve what works and request re-divergence where candidates remain insufficiently distinct.

Hard accessibility and product-truth regressions are non-compensatory. A candidate cannot “win aesthetically” and thereby erase a blocker on a separate authority plane.

The result remains:

```text
claim_boundary = taste-comparison-only
```

Taste comparison informs selection; it does not certify release.

---

## 15. Bounded Quality Residue Loop

`src/nolane_ui/runtime_v11/quality_residue.py` distinguishes micro-craft debt from a wrong design thesis.

Once a direction is committed and evidence suggests the thesis is basically sound, the residue loop can plan small bounded passes tied to concrete regions/dimensions and a preserve set. It does not reopen macro redesign implicitly.

If the committed thesis is false, or the bounded pass budget is exhausted without closure, the correct action is:

```text
RE_DIVERGE
```

not endless polish.

This prevents a common AI failure mode where a structurally generic direction receives more gradients, shadows, glow, borders, micro-animation, and spacing tweaks instead of being abandoned.

Residue closure uses:

```text
claim_boundary = quality-residue-only
```

It never upgrades into release authority and reuses the existing V11 evidence/re-observation boundaries instead of creating a competing completion system.

---

## 16. Runtime Doctor

`scripts/nui-runtime-doctor` is a read-only maintenance pass. It reports installation/schema drift, evidence freshness problems, and required observation-capability gaps.

`REQUIRED_RUNTIME_ARTIFACTS` now includes the Phase 4 governor modules, schemas, and trend registry in addition to the detector/browser/evidence/live foundation. A runtime installation that lacks the generation-governance contract is therefore reported as incomplete rather than silently treated as healthy.

Doctor does not redesign the product, rewrite context, or infer truth drift from commit count. Repository churn is a maintenance clue, not product/design truth evidence.

```bash
python scripts/nui-runtime-doctor --root .
```

Missing capability is reported as unresolved/blocked, never converted to PASS.

---

## 17. Live Lab transaction and closure contract

`src/nolane_ui/runtime_v11/live.py` provides the state/journal/source-safety foundation for interactive visual iteration.

Normal session progression is:

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

Only `PREVIEWING` can enter recovery after interruption. Once source has been accepted/applied, the journal cannot rewind into preview and pretend the source mutation did not occur.

`transactional_replace()` uses optimistic concurrency with two source guards: an initial digest check and a final pre-commit existence/digest check after staging. Concurrent source edits/deletion return `CONFLICT` and preserve the newer state. Successful commit uses an atomic filesystem replace.

This is intentionally described as optimistic concurrency with a final guard, **not** mathematical lock-free cross-process compare-and-swap. An uncooperative writer can still race after the final guard; a future cooperative coordinator may strengthen that boundary.

A live `reobserve` event records bounded resolved/persisted/unknown/regression counts. `CLEAN` is invalid if persisted, unknown, or regression counts are non-zero.

Closing a live session does not mean product release. `OPEN` or `UNKNOWN` re-observation may still transition to session `CLOSED`; the journal records that the interactive session ended, not that the product passed NUI completion gates.

---

## 18. Public Phase 4 API

The top-level `nolane_ui` package exposes explicit runtime-prefixed aliases so callers do not need to import private modules and so authority boundaries remain visible in naming.

The Phase 4 surface includes:

- `compile_runtime_aesthetic_intent`
- `validate_runtime_aesthetic_intent`
- `evaluate_runtime_direction_candidates`
- `commit_runtime_direction`
- `assess_runtime_genericity`
- `validate_runtime_trend_registry`
- `runtime_product_substitution_assessment`
- `build_runtime_design_memory`
- `validate_runtime_design_memory`
- `assess_runtime_design_memory_staleness`
- `prepare_runtime_blinded_candidates`
- `validate_runtime_taste_judgment`
- `aggregate_runtime_taste_court`
- `plan_runtime_quality_residue_pass`
- `assess_runtime_quality_residue_closure`

These are protocol APIs. They do not bypass canonical skills or completion gates.

---

## 19. Verification and TDD boundary

Phase 4 was implemented through explicit RED → GREEN cycles.

A consolidated RED contract introduced 13 missing behavior tests before production modules existed. The RED run failed specifically because the Phase 4 API was absent while the pre-existing suite remained green. Production modules then made those contracts pass. A judge-packet leakage regression was diagnosed from CI evidence and fixed at the source: the sanitized candidate payload was correct, but audit metadata itself leaked forbidden field names; that metadata was replaced with non-revealing redaction state.

Craft-floor rules were then introduced with positive accumulation cases and negative semantic counterexamples. A final integration RED cycle required top-level public exports, Doctor inventory coverage, and full owner-hint resolution against the 874-skill graph.

The implementation checkpoint before this documentation revision passed **538/538** unit/contract tests plus fresh completion packet generation, exact-revision validation, artifact upload, project packaging and archive upload. The authoritative final exact-head run is recorded in PR #22 after documentation is committed so writing verification metadata cannot create a newer unverified repository SHA.

---

## 20. External architectural research

V11 studied `pbakaus/impeccable` as one external reference for general workflow ideas such as deterministic UI checks, edit/session feedback, browser-aware iteration, maintenance passes, and live visual workflows. This is **research inspiration only**.

NUI V11 does not incorporate Impeccable source code, detector rule text, skill bodies, schemas, thresholds, state machines, configuration formats, or implementation artifacts. V11 runtime code, Phase 4 generation-governance code, rule wording, schemas, tests, thresholds, evidence semantics, routing, Doctor behavior, re-observation logic, and Live Lab protocol are independently designed and authored for NUI.

The research record remains at `docs/research/impeccable-runtime-mechanism-transfer-v11.md` for historical link stability. The document itself explicitly states that no implementation transfer occurred.

---

## 21. Non-goals

V11 does not:

- add runtime rules or Phase 4 protocols as canonical skills;
- modify the 874-skill graph to make routing easier;
- create a new owner when an owner hint cannot resolve;
- impose one NUI house style;
- treat a familiar component/pattern as automatically bad;
- use one scalar “AI-looking”, genericity, or beauty score as aesthetic authority;
- allow trend tells to live forever without review;
- allow genericness/advisory observations to become edit-time blockers;
- infer redesign authority from visual ambition;
- let generator preference or reference prestige leak into blinded judging;
- allow an aesthetic win to compensate for accessibility/product-truth blockers;
- polish indefinitely when the committed thesis should be re-diverged;
- fabricate browser evidence when a host lacks capability;
- treat absence under incomplete observation as resolved;
- make a clean scan, committed direction, taste win, residue closure, or live-session close sufficient evidence of product completion;
- overwrite known concurrent edits during live application;
- claim a complete Playwright/HMR/overlay system that V11 has not yet implemented;
- describe external research inspiration as copied or transferred implementation.

These boundaries are deliberate. V11 is intended to make NUI more observable, more difficult to game, less likely to converge on generic AI UI, and more disciplined about evidence—without making the canonical graph larger for its own sake.
