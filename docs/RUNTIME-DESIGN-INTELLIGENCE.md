# NUI V11 Runtime Design Intelligence

NUI V11 adds a deterministic runtime-observation layer beneath the canonical cognition graph. It does **not** add canonical skills, replace routed design owners, or turn a clean scan into release authority. Its job is narrower and more useful: observe implementation and rendered behavior, emit bounded evidence, detect when prior evidence has become stale, and feed those facts back into the existing NUI finding/critique/completion machinery.

The architecture deliberately separates three responsibilities:

1. **Cognition owns design decisions.** Product truth, task modeling, authority, aesthetic direction, interaction semantics, accessibility intent, and repair strategy remain owned by the existing NUI graph.
2. **Runtime intelligence owns observation.** Source scans, browser packets, hook execution, evidence fingerprints, and live-edit conflict checks produce facts about the implementation.
3. **Evidence gates own claims.** Runtime evidence can support or block a claim, but runtime tools do not self-certify product quality or release readiness.

This separation is the primary difference between V11 and a conventional lint pack. A detector rule is a machine observation contract, not a new design faculty.

## Runtime rule model

The canonical runtime registry is `knowledge/runtime-detector-rules-v11.json`. Rules are independently authored NUI runtime contracts and are intentionally outside `skills/skill-graph.json`.

Each rule declares a stable `rule_id`, domain, class, tier, severity, supported engines, falsifier, owner hints, and provenance. Four classes are used:

- `mechanical`: high-confidence implementation failures that can usually be reported without product-specific interpretation.
- `contextual`: suspicious implementation states that require product, platform, design-system, or runtime authority before they become confirmed violations.
- `genericness`: structural convergence signals that can indicate template-like UI but never prove bad design by themselves.
- `advisory`: taste/craft signals that can inform critique but cannot act as automatic blockers.

Genericness and advisory rules are prohibited from becoming edit-time blockers. This prevents the runtime layer from turning aesthetic heuristics into hidden design authority.

Runtime provenance is deliberately narrow. Every rule is marked `implementation: independently-authored`; optional `research_inspiration` records conceptual areas that informed investigation. The legacy name `mechanism_sources` is rejected because it can incorrectly imply that implementation or source artifacts were transferred into NUI.

## Execution tiers

V11 uses three execution tiers so fast feedback and deep evidence do not compete with each other.

### EDIT

The edit tier is the smallest deterministic pass. It is suitable for post-write or preflight hooks and focuses on high-confidence findings worth surfacing immediately. Host integrations must remain thin: they invoke the same canonical detector rather than maintaining provider-specific copies of rule logic.

The canonical command is:

```bash
python scripts/nui-detect <file-or-directory> --tier edit
```

A host with a blocking pre-write mechanism may use the result as a local edit guard only for rule classes permitted to block. A host without that mechanism must not pretend to provide one.

### SESSION

The session tier evaluates the complete runtime rule set over UI files touched during a working session. It is where contextual, genericness, and advisory observations can be surfaced without interrupting every edit.

```bash
python scripts/nui-detect <file-or-directory> --tier session
```

Session findings should be routed into the relevant existing NUI owners for interpretation and repair. They are not a separate critique system.

### RELEASE

Release-time runtime evidence combines source observations with browser/rendered observations and evidence freshness. The release layer must preserve missing capability as `UNKNOWN` or `BLOCKED`; it may never infer PASS because a collector could not observe something.

A clean source detector result therefore means only: no registered source rule produced a finding for the observed scope. It does **not** mean the UI is accessible, responsive, correct, beautiful, or releasable.

## Source detector

`src/nolane_ui/runtime_v11/detector.py` provides dependency-free text/source observation for common web UI files. The detector emits stable NUI-shaped findings with source location, rule identity, evidence detail, impact, falsifier, repair guidance, severity, and status.

Observation and adjudication are separate by design. A contextual rule may match source text while remaining unresolved until the active product/design authority is supplied. `src/nolane_ui/runtime_v11/adjudication.py` converts raw matches into confirmed findings, accepted narrow exceptions, or unknowns.

Exceptions are intentionally narrow. A runtime exception needs explicit scope and rationale; project-wide suppression is not something the detector grants itself. The goal is reviewable evidence, not a convenient path around failing feedback.

## Agent hook boundary

`src/nolane_ui/runtime_v11/hooks.py` describes runtime-detection capabilities for supported host projections. `build_agent_install_plan()` exposes those capabilities without escalating host permissions or design authority.

The invariant is:

```text
one canonical detector -> many thin host projections
```

Codex, Claude, Cursor, and generic agents may expose different lifecycle events, but they all point to the same `scripts/nui-detect` implementation. V11 records what a host can genuinely do: post-write advice, stop/session pass, preflight blocking, or manual fallback. Missing host behavior is represented as missing capability rather than simulated certainty.

## Browser observation protocol

The core browser boundary is provider-neutral. NUI does not require one browser vendor, extension, or automation framework. A collector produces a versioned observation packet described by `schemas/runtime-browser-observation-v11.schema.json`.

A packet declares its collector, URL, viewport, observation capabilities, element observations, runtime errors, and optional capture reference. Capabilities are explicit because absence matters: a packet that cannot observe geometry cannot claim that layout is clean; a packet that cannot observe occlusion cannot claim that content is unobstructed.

`browser_observation_findings()` converts supported observations into the same finding vocabulary used by source detection. Current browser rules include deterministic runtime-error, horizontal-overflow, and explicit-occlusion findings. New browser rules should be added only when their evidence contract is concrete enough to falsify.

The browser packet is intentionally transport-agnostic. A Playwright driver, Codex browser surface, extension, MCP tool, or future native bridge can produce the packet without changing the NUI core.

## Revision-bound evidence

`src/nolane_ui/runtime_v11/evidence.py` binds evidence to the source scope it actually certifies. Each binding records source digests rather than relying on repository-wide commit counts.

Freshness has three meaningful outcomes:

- `CURRENT`: every source digest in the certified scope still matches.
- `STALE`: at least one overlapping source digest changed after the evidence was produced.
- `UNKNOWN`: current state cannot be observed for at least one required source in the binding.

Unrelated source changes do not invalidate scoped evidence. Conversely, an overlapping change cannot leave old evidence silently current. This gives NUI a causal evidence boundary: screenshots and runtime observations remain valid only for the implementation they actually observed.

## Runtime doctor

`scripts/nui-runtime-doctor` is a read-only maintenance pass. It reports problems in four families:

- installation/schema drift,
- projection/runtime artifact drift,
- evidence freshness problems,
- required observation-capability gaps.

The canonical installation inventory is exported as `REQUIRED_RUNTIME_ARTIFACTS`; it covers the detector, doctor, schemas, evidence layer, browser protocol, hook contracts, and Live Lab protocol rather than treating only the Phase 1 detector as a complete runtime installation.

Doctor does not redesign the product, rewrite context, or infer truth drift from a large number of commits. A commit count can be a maintenance clue, but it is not evidence that product or design truth is wrong. When evidence is stale, doctor preserves and reports it; it does not delete inconvenient evidence.

Example:

```bash
python scripts/nui-runtime-doctor --root .
```

A required capability that cannot be observed is reported as an unresolved capability gap, never transformed into a passing result.

## Live Lab transaction contract

`src/nolane_ui/runtime_v11/live.py` provides the protocol foundation for interactive visual iteration. The current layer intentionally prioritizes source safety and recoverability before browser-overlay ergonomics.

A live session is an append-only state machine. The normal path is:

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

Only an active `PREVIEWING` state may enter `RECOVERY` after an interruption. Once source has been accepted/applied, the journal cannot rewind into preview, because that would make session state disagree with the already-mutated source tree. Illegal transition skips are rejected rather than silently repaired.

Live source application uses optimistic concurrency. Selection records the source digest that the user/agent actually inspected. `transactional_replace()` checks that digest once before staging the replacement, writes the candidate to a sibling temporary file, then performs a second existence/digest check immediately before commit:

- source still exists and both guards match -> commit through an atomic filesystem replace and return the new digest;
- source changed during either guard window -> return `CONFLICT` and preserve the newer source;
- source was deleted while staging -> return `CONFLICT`, delete the temporary candidate, and do not recreate the source.

The second guard closes the preparation-window race that a single up-front digest check would miss. This is intentionally described as optimistic concurrency with a final pre-commit guard, not as a mathematical lock-free compare-and-swap: an uncooperative writer can still race after the final check. A future cooperative lock/transaction coordinator can strengthen that boundary without changing the session protocol.

Preview approval is therefore not blanket permission to clobber newer source state. After a successful apply, the normal next step is re-observation so old overlapping evidence cannot silently certify the new implementation.

The next layer built on this protocol can add element selection, source mapping, variant preview transport, and browser overlays while preserving the same conflict-safe core.

## External architectural research

V11 studied `pbakaus/impeccable` as one external reference for workflow ideas such as deterministic UI checks, edit/session feedback, browser-aware iteration, maintenance passes, and live visual workflows. That study is **research inspiration only**.

NUI V11 does not incorporate Impeccable source code, detector rule text, skill bodies, schemas, thresholds, state machines, configuration formats, or implementation artifacts. V11 code, rule wording, schemas, tests, thresholds, evidence semantics, Doctor behavior, and Live Lab protocol are independently designed and authored for NUI.

The research record is kept at `docs/research/impeccable-runtime-mechanism-transfer-v11.md`; its historical filename remains for link stability, while the document itself explicitly states that no implementation transfer occurred.

## Non-goals

V11 does not:

- add runtime rules as canonical skills;
- replace product, accessibility, visual, or interaction owners;
- use one scalar detector score as a release verdict;
- allow genericness heuristics to override explicit product/design authority;
- fabricate observations when a browser/host lacks capability;
- make a clean scan sufficient evidence of completion;
- overwrite known concurrent edits during live application;
- claim lock-free cross-process atomic compare-and-swap where the filesystem/runtime does not provide it;
- describe external research inspiration as copied or transferred implementation.

These boundaries are deliberate. Runtime Intelligence should make the existing NUI graph more observable and harder to fool, not make the graph larger for its own sake.
