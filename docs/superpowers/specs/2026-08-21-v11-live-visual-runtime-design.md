# NUI V11 Phase 5 — Live Visual Runtime Design

**Status:** Approved architectural direction; implementation not started by this document.

## Goal

Phase 5 turns the existing V11 browser-observation and Live Lab protocol foundations into a real visual iteration runtime without making any one browser provider, framework, or preview mechanism authoritative.

The target loop is:

```text
browser collector
  -> rendered element identity
  -> source attribution
  -> bounded live selection
  -> immutable preview candidate(s)
  -> preview transport
  -> overlay evidence
  -> explicit accept
  -> existing conflict-safe source mutation
  -> fresh browser observation
  -> existing runtime re-observation
  -> existing evidence/completion gates
```

Phase 5 is a runtime/transport subsystem beneath the existing 874-skill cognition graph. It adds no canonical skill and does not alter `skills/skill-graph.json`.

## Why this phase exists

V11 already has:

- provider-neutral browser observation packets;
- explicit browser capability truthfulness;
- runtime findings for browser errors, horizontal overflow, and explicit occlusion;
- revision-bound evidence;
- finding-to-existing-owner routing;
- deterministic re-observation closure;
- conflict-safe Live Lab source mutation;
- append-only Live Lab session state and recovery boundaries;
- Phase 4 generation governance, anti-generic craft observations, project-local design memory, blinded taste court, and bounded quality residue.

What is missing is the real transport between a rendered element and source-backed visual iteration. Today NUI can reason about a browser packet and can safely mutate a known source range, but it cannot yet prove how a selected rendered element maps to source, create a non-destructive visual preview, refresh that preview through a concrete browser adapter, or present overlay evidence tying visual state to source/revision.

Phase 5 closes that gap.

## Architectural choice

NUI uses a **provider-neutral Live Visual Core with a Playwright reference adapter**.

Rejected alternatives:

1. **Playwright-first monolith.** Faster initially, but it would make one provider's object model the implicit architecture and make future Codex browser, extension, MCP, WebDriver, or native bridges second-class.
2. **Browser-extension-first architecture.** Attractive interaction ergonomics, but it prematurely couples Phase 5 to extension lifecycle, browser permissions, messaging, packaging, and framework integration.

The selected architecture keeps source attribution, preview state, evidence binding, overlay packets, and refresh semantics provider-neutral. Playwright is the first concrete adapter because it can exercise the full contract and prevent the core from remaining a theoretical protocol.

## Non-goals

Phase 5 does not:

- add canonical skills;
- make Playwright design authority;
- make browser transport responsible for taste decisions;
- infer a source file when attribution evidence is ambiguous;
- let preview mutate canonical source;
- treat a successful reload/HMR event as product verification;
- treat screenshots without matching revision/scope as fresh evidence;
- implement a global NUI house style;
- bypass existing V11 runtime findings, routing, re-observation, evidence, or completion gates;
- claim mathematically lock-free cross-process source mutation;
- require HMR to exist;
- claim browser overlay UI itself proves accessibility, product truth, or quality.

## Core invariants

1. **Rendered identity is not source authority.** A DOM locator identifies a rendered node, not automatically a source file/range.
2. **Attribution fails closed.** Ambiguity is represented, not guessed away.
3. **Preview is non-destructive.** Preview candidates may alter a browser/runtime sandbox but may not write canonical source.
4. **Acceptance is explicit.** Source mutation occurs only after a selected preview candidate is explicitly accepted.
5. **Mutation reuses the existing conflict-safe path.** Phase 5 must route canonical source writes through V11's existing transactional source mutation boundary rather than inventing a weaker write path.
6. **Refresh capability is truthful.** HMR is a capability, not an assumption. Reload is a valid fallback.
7. **Rendered evidence is revision-bound.** A capture, overlay, or runtime packet supports only the exact source/runtime revision it observed.
8. **Missing capability preserves UNKNOWN.** Missing mapping, refresh, capture, or browser capability cannot silently become PASS.
9. **Overlay is evidence presentation, not judgment authority.** It may show facts and uncertainty but cannot select a design winner.
10. **Adapters cannot escalate authority.** A provider may supply capabilities and observations only.

## System decomposition

Phase 5 is split into six independently testable units.

### 1. Source Attribution Resolver

Purpose: convert rendered-element metadata into bounded source candidates without inventing certainty.

Proposed module:

`src/nolane_ui/runtime_v11/source_attribution.py`

Proposed schema:

`schemas/runtime-source-attribution-v11.schema.json`

Primary APIs:

```python
validate_source_attribution(record: dict) -> dict
resolve_source_attribution(
    rendered_identity: dict,
    candidates: list[dict],
    *,
    repository_root: str | Path,
) -> dict
select_source_candidate(attribution: dict, candidate_id: str) -> dict
```

Attribution status is a closed enum:

- `EXACT`
- `CANDIDATE`
- `AMBIGUOUS`
- `UNKNOWN`

`EXACT` means the supplied evidence resolves one canonical source target with no competing target at equivalent confidence. It does not mean the source is semantically the only possible implementation owner.

`CANDIDATE` means one target is strongest but the system does not have enough evidence to authorize mutation automatically.

`AMBIGUOUS` means multiple materially plausible source targets remain.

`UNKNOWN` means the runtime cannot establish a source target.

Each source candidate must carry:

- stable candidate ID;
- repository-relative canonical source path;
- optional line/range or character range;
- source digest;
- attribution mechanisms used;
- evidence references;
- confidence class, not an opaque scalar quality score;
- framework/provider metadata only as evidence, never as authority.

Candidate-selection authority:

- `EXACT` can proceed to bounded live selection automatically only when path/range/digest validation succeeds;
- `CANDIDATE` and `AMBIGUOUS` require explicit candidate selection before mutation authority exists;
- `UNKNOWN` cannot proceed to source mutation.

Path safety is mandatory. Candidate paths must be canonicalized inside the repository root. Absolute escape, `..` traversal, symlink escape, and equivalent root-escape patterns are rejected.

### 2. Browser Transport Contract

Purpose: define the capability-neutral interface used by concrete browser collectors/transports.

Proposed module:

`src/nolane_ui/runtime_v11/browser_transport.py`

Proposed schema:

`schemas/runtime-browser-transport-v11.schema.json`

A transport declares capabilities explicitly, including:

- navigation;
- geometry;
- computed style;
- runtime errors;
- capture;
- document metrics;
- occlusion;
- rendered element metadata;
- preview injection;
- hot reload;
- bounded reload;
- source instrumentation metadata, when available.

The core must not branch on provider name for authority. It branches only on declared capabilities.

A provider lacking a capability must return a capability gap/UNKNOWN result, not fabricate empty observations.

### 3. Playwright Reference Adapter

Purpose: prove the provider-neutral contract against a concrete browser automation implementation.

Proposed module:

`src/nolane_ui/runtime_v11/playwright_adapter.py`

The adapter is optional at import time. NUI core must remain importable without Playwright installed. Adapter availability is therefore detected explicitly.

The adapter may:

- navigate to a supplied URL;
- capture viewport and DPR;
- collect element geometry;
- collect selected computed styles;
- collect page/console/runtime errors;
- collect document metrics;
- produce capture references;
- collect explicit occlusion/hit-test evidence where supported;
- collect rendered identity and framework/source instrumentation metadata when supplied by the page/toolchain;
- perform preview injection through the generic preview contract;
- request HMR when a compatible bridge exists;
- fall back to bounded reload otherwise.

The adapter must emit canonical V11 packets and pass them through existing validators. It cannot bypass normalization because it happens to be the reference implementation.

Provider-specific metadata is isolated under adapter metadata fields and does not leak into canonical authority semantics.

**Concrete-adapter completion rule:** optional importability must not become an excuse for a paper adapter. Final Phase 5 verification requires at least one exact-head browser smoke flow using real Playwright and a real browser engine. Mock/fake adapter tests remain useful for deterministic unit coverage but cannot satisfy this completion criterion, and a skipped Playwright smoke test cannot be reported as adapter verification. If the default repository workflow cannot provision Playwright/browser binaries, Phase 5 must add a dedicated exact-head browser integration job or equivalent recorded exact-head verification environment.

### 4. Immutable Preview Runtime

Purpose: create visual alternatives without mutating canonical source.

Proposed module:

`src/nolane_ui/runtime_v11/preview.py`

Proposed schema:

`schemas/runtime-live-preview-v11.schema.json`

Primary APIs:

```python
build_preview_candidate(...)
validate_preview_candidate(...)
assess_preview_freshness(...)
prepare_preview_application(...)
record_preview_observation(...)
```

Each preview candidate is immutable and includes:

- preview/candidate ID;
- originating live-session ID;
- selected source candidate;
- base source digest;
- exact bounded replacement/patch intent;
- visual-direction or generation candidate ID when relevant;
- preserve constraints;
- creation provenance;
- transport requirements;
- observation state;
- capture references only after actual render observation.

Preview state uses a closed lifecycle such as:

- `PREPARED`
- `INJECTED`
- `OBSERVED`
- `STALE`
- `CONFLICT`
- `REJECTED`
- `ACCEPTED`

Preview injection must not modify the canonical repository file. An adapter may use browser-side style injection, an isolated runtime bridge, ephemeral filesystem/worktree state, dev-server transforms, or another sandboxed mechanism, but the canonical contract records only that a preview transport rendered the candidate—not how provider internals did it.

Before preview and again before accept, source digest is checked. If canonical source changes, candidate becomes `STALE` or `CONFLICT` and must not silently apply.

### 5. Overlay Evidence Packet

Purpose: represent what a visual client may show without turning the overlay into design authority.

Proposed module:

`src/nolane_ui/runtime_v11/overlay.py`

Proposed schema:

`schemas/runtime-live-overlay-v11.schema.json`

An overlay packet may include:

- selected rendered locator;
- selected bounding box;
- source attribution status;
- bounded source candidate summary;
- current source digest/revision;
- active preview candidate IDs;
- before/after capture refs;
- runtime finding summaries;
- unresolved/unknown capability indicators;
- preview freshness/conflict state;
- re-observation closure summary.

It must not include:

- a scalar beauty score;
- generator self-score;
- hidden taste-court preference;
- an automatic winner declaration;
- fabricated source certainty;
- `VERIFIED` or `RELEASED` authority.

Overlay output is view-model evidence only.

### 6. Live Visual Coordinator

Purpose: orchestrate the Phase 5 loop while preserving existing Live Lab and evidence boundaries.

Proposed module:

`src/nolane_ui/runtime_v11/live_visual.py`

This coordinator composes existing and new modules rather than duplicating them.

Target flow:

```text
select rendered target
  -> resolve source attribution
  -> bind selected source digest
  -> construct preview candidates
  -> inject preview through available transport
  -> prove refresh/reload completion
  -> collect fresh browser observation
  -> build overlay evidence
  -> explicit accept/reject
  -> if accepted, call existing transactional source mutation
  -> collect fresh browser observation on new digest/revision
  -> convert to findings
  -> compare runtime observations
  -> persist closure summary into existing Live Lab journal
```

The coordinator cannot jump directly from `preview created` to `accepted render observed`. It needs explicit transport evidence that the candidate actually rendered.

## Render identity contract

A rendered identity should remain compact and portable. It may include:

- canonical DOM locator generated by the collector;
- tag/role/test-id/attributes needed for stable matching;
- visible text fingerprint when useful;
- bounding box evidence;
- framework component name when instrumented;
- source-location metadata when instrumented;
- runtime-generated element identity token when a development bridge can provide one.

No single field is universally required except a stable rendered locator/identity key. Framework metadata may increase attribution confidence but is never assumed to exist.

## Source attribution mechanisms

NUI should support multiple evidence mechanisms rather than one magical mapper. Examples include:

- explicit development instrumentation attributes;
- framework debug metadata;
- source maps;
- compiler/dev-server instrumentation;
- component stack metadata;
- repository search constrained by unique test IDs/identifiers;
- caller-supplied mapping records.

These are evidence inputs. The resolver owns normalization and ambiguity semantics.

A filename/line supplied by an external runtime is not trusted until canonicalized against repository root and bound to the current source digest.

## Refresh and HMR semantics

Refresh is modeled as capability evidence.

Preferred sequence:

1. inject preview;
2. request HMR when `hot_reload=true` and the bridge supports the target;
3. confirm a refresh event tied to candidate ID/revision;
4. otherwise use bounded reload when `reload=true`;
5. re-identify the target element after refresh;
6. collect a new observation packet;
7. bind captures/overlay to the new observation.

Failure outcomes include:

- `HOT_RELOAD_UNAVAILABLE`
- `HOT_RELOAD_FAILED`
- `RELOAD_FAILED`
- `TARGET_NOT_REFOUND`
- `OBSERVATION_INCOMPLETE`

These preserve `UNKNOWN` where needed. They do not imply source rollback because preview has not mutated canonical source.

## Canonical mutation boundary

Phase 5 must not introduce a second source-write primitive.

After explicit acceptance, the selected source target and replacement are passed to the existing V11 transactional mutation primitive with the source digest that was last proven current.

If source has changed:

- return conflict;
- leave new source untouched;
- mark accepted preview as non-applicable/stale;
- require attribution/preview rebase before a later apply.

This keeps browser UX from weakening the concurrency model already established in V11.

## Evidence and capture binding

Every capture used by Phase 5 needs a binding containing enough information to prevent screenshot theater:

- collector/adapter identity;
- URL/state identifier;
- viewport/DPR;
- source/revision binding;
- preview candidate ID when previewing;
- selected target identity where relevant;
- capture reference/digest when available;
- observation timestamp only as metadata, never freshness proof by itself.

A capture without current source/revision binding may be displayed historically but cannot support a current closure claim.

## Capability-scoped closure

Phase 5 should refine the existing coarse `capabilities_complete` concept for visual loops.

A finding or visual assertion is considered resolvable only when the required capability set for that specific observation is satisfied.

Examples:

- layout overflow closure requires document metrics/geometry as declared by its rule;
- text occlusion closure requires occlusion capability;
- source-attribution closure requires a valid selected source target and digest;
- preview observation requires preview transport plus successful refresh/reload plus browser observation;
- capture comparison requires fresh capture capability.

Missing one capability makes only the affected assertion `UNKNOWN`; it does not necessarily invalidate unrelated observations.

## Doctor integration

Runtime Doctor should inspect Phase 5 installation and report:

- missing Phase 5 modules/schemas;
- Playwright adapter unavailable when explicitly requested;
- unsupported browser transport capability;
- source-attribution contract errors;
- unsafe/out-of-root mapping candidates;
- stale preview candidates;
- preview state that claims observation without refresh evidence;
- capture evidence bound to obsolete revision/digest;
- required HMR absent where a caller explicitly requires HMR rather than accepting reload fallback.

Doctor remains read-only.

## Public API boundary

Phase 5 public APIs should be exposed through `runtime_v11` and top-level `nolane_ui` using explicit runtime-prefixed aliases where ambiguity would otherwise arise.

Public exposure does not grant release authority. API results retain narrow claim boundaries such as:

- `source-attribution-only`
- `preview-transport-only`
- `overlay-evidence-only`
- `live-visual-closure-only`

## Testing strategy

Implementation is TDD-first.

### Source attribution RED tests

- exact one-candidate mapping;
- candidate/ambiguous/unknown outcomes;
- explicit candidate selection requirement;
- repository path traversal rejection;
- absolute path escape rejection;
- symlink/root escape rejection where runtime permits;
- stale source digest rejection;
- provider metadata cannot itself force `EXACT`.

### Preview RED tests

- preview cannot mutate canonical source;
- preview candidate is immutable by contract;
- source change marks preview stale/conflicted;
- accepted candidate still requires transactional mutation;
- preview observation cannot exist without successful refresh/reload evidence;
- stale capture cannot be rebound to a new revision.

### Transport/adapter RED tests

- adapter capability declaration is explicit;
- missing Playwright dependency keeps core importable;
- canonical browser packet passes existing validator;
- unsupported capability remains UNKNOWN;
- HMR fallback to bounded reload;
- failed HMR + failed reload does not claim observation;
- re-identification required after refresh;
- a dedicated real-browser smoke test executes against installed Playwright/browser and is not skipped on the Phase 5 completion head.

### Overlay RED tests

- ambiguity/UNKNOWN visibly preserved;
- overlay cannot include beauty score, automatic winner, or release authority;
- capture/source revision mismatch is rejected;
- overlay runtime findings preserve canonical finding identities.

### End-to-end RED tests

- rendered target -> exact attribution -> preview -> observed refresh -> accept -> conflict-safe apply -> fresh observation -> runtime closure;
- ambiguous attribution blocks mutation;
- source edit during preview causes conflict instead of overwrite;
- missing refresh capability prevents false observed state;
- after-only runtime regression remains visible after accepted visual repair;
- closing Live Visual session never upgrades to product release claim.

### Regression gate

Full existing repository suite must continue to pass, including:

- all 874 skill graph integrity tests;
- all Batch 006 duplicate/trivial-rename protections;
- all V10 empirical claim ceilings;
- V11 runtime rules/adjudication/routing/re-observation/evidence/Doctor/Live Lab;
- Phase 4 aesthetic governor/craft-floor/design-memory/taste/residue tests.

## Failure semantics

Phase 5 uses explicit machine states instead of optimistic prose.

Representative failures:

- `ATTRIBUTION_UNKNOWN`
- `ATTRIBUTION_AMBIGUOUS`
- `SOURCE_OUTSIDE_ROOT`
- `SOURCE_STALE`
- `PREVIEW_STALE`
- `PREVIEW_CONFLICT`
- `TRANSPORT_UNAVAILABLE`
- `HOT_RELOAD_UNAVAILABLE`
- `HOT_RELOAD_FAILED`
- `RELOAD_FAILED`
- `TARGET_NOT_REFOUND`
- `OBSERVATION_INCOMPLETE`
- `CAPTURE_STALE`
- `APPLY_CONFLICT`

None of these may be silently coerced to PASS.

## Security and repository-safety boundary

Source attribution and preview transport add new attack/error surfaces, so Phase 5 must enforce:

- repository-root path containment;
- no arbitrary external file mutation;
- no shell command construction from rendered text or selector data;
- transport payload validation before execution;
- canonical source digest check before apply;
- no secret/runtime token persistence in overlay packets;
- bounded capture references rather than embedding uncontrolled browser payloads;
- explicit adapter availability and capability negotiation.

## Performance boundary

The visual loop should optimize for interactive latency without sacrificing evidence semantics.

- Source attribution may cache repository metadata by source digest/revision.
- Browser observations should be scoped to selected/affected regions when full-page collection is unnecessary.
- Preview candidates may share immutable base context.
- Capture generation may be optional for non-visual mechanical checks, but flagship visual comparison requires capture capability when the caller requests it.
- Performance shortcuts cannot reuse stale visual evidence across source revisions.

## Research/provenance boundary

External browser/devtool/live-edit systems may be studied for architectural ideas. NUI Phase 5 implementation remains independently authored.

No external source mapping logic, Playwright helper code, extension source, preview protocol, HMR bridge, overlay implementation, schema, threshold, or state machine is incorporated unless a future explicitly scoped adaptation is reviewed for provenance/license and isolated accordingly.

The purpose of research is to learn failure modes and architectural questions, not to import a competitor's implementation identity.

## Completion criteria

Phase 5 is complete only when all of the following are true:

1. provider-neutral source-attribution, transport, preview, overlay, and coordinator contracts exist;
2. a concrete Playwright reference adapter exists and cannot bypass canonical packet validation;
3. at least one exact-head Playwright smoke flow uses a real browser engine and passes without being skipped or replaced by a mock;
4. source attribution has explicit exact/candidate/ambiguous/unknown semantics;
5. unsafe paths and stale digests fail closed;
6. preview never mutates canonical source;
7. source mutation still flows through the existing conflict-safe V11 write primitive;
8. HMR is capability-negotiated with bounded reload fallback;
9. successful preview observation requires proven refresh/reload plus fresh browser observation;
10. captures are revision/source bound;
11. overlay remains evidence-only and cannot declare taste/release winners;
12. Doctor covers Phase 5 artifacts and capability gaps;
13. public APIs are explicit;
14. no canonical skills are added or modified by Phase 5;
15. changed-path audit contains no `skills/` paths;
16. the canonical graph remains exactly 874 declared/validated skills unless a separately authorized skill batch changes main first;
17. all new tests pass plus the complete pre-existing suite;
18. fresh completion packet and exact-revision repository validation pass on final head;
19. PR #22 body is updated with final Phase 5 capability and limitation boundaries;
20. PR #22 remains unmerged unless the user explicitly authorizes merge.

## Claim ceiling

Phase 5 can prove that NUI has a structurally validated, provider-neutral, conflict-safe live visual iteration protocol with a concrete reference browser adapter when the implementation and tests exist and the real-browser smoke gate passes.

It cannot, from structural/unit/browser smoke tests alone, prove that the browser workflow improves real-model UI quality, designer preference, task success, or production velocity. Those remain empirical claims and stay under the existing V10 evidence/claim system.
