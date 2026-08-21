# NUI V11 — Runtime Design Intelligence & Live Perception

## Status

Design approved in conversation and implementation authorized. This work intentionally avoids the concurrent `design/ui-industry-1000-batch-006` skill-expansion branch.

## Problem

NUI v0.10.0 already has a deep cognition graph, lifecycle controller, evidence contracts, independent criticism, product-completeness gates, rendered-perception evidence, comparative taste protocols and empirical evaluation. The missing capability is not another set of design owners. The missing capability is a fast, deterministic runtime layer that can observe source and rendered UI, convert observations into NUI-native findings, feed those findings into the existing evidence lifecycle, and provide edit-time/live feedback without requiring a model to rediscover mechanical defects.

Impeccable demonstrates several useful mechanisms: deterministic anti-pattern detection, per-edit and stop-time hooks, project-local design context, doctor-style drift inspection, and browser live iteration. V11 adopts those mechanisms at the architecture level while reimplementing them as NUI-native subsystems. It does not copy Impeccable's one-skill command model, does not import its taste rules as universal truth, and does not create one canonical NUI skill per detector rule.

## Non-negotiable boundaries

1. **No new canonical skills in this work.** V11 must not compete with or overlap the concurrent 100-skill expansion.
2. **No skill templating or generated skill batches.** Runtime rules are machine rules, not cognition faculties.
3. **No duplicate design authority.** Existing NUI owners remain authoritative for typography, layout, motion, accessibility, product truth, platform behavior, aesthetics and verification.
4. **No universal beauty score.** Deterministic output is evidence and findings, never a scalar substitute for NUI's comparative critique.
5. **No silent release certification.** A clean detector cannot by itself move a task to `VERIFIED` or `RELEASED`.
6. **No wholesale source copy from Impeccable.** Reimplement mechanisms in NUI style. Any future vendored Apache-2.0 code must be isolated and attributed explicitly.
7. **No mutation of host permissions.** Hooks and live drivers may only use capabilities already granted by the host.
8. **No main-branch implementation.** Work stays isolated on `build/v11-runtime-design-intelligence` until reviewed.

## Core architecture

```text
user / agent
    ↓
NUI command facade
    ↓
existing contract + task profile + routing graph
    ↓
existing design owners / implementation
    ↓
┌──────────────────────────────────────────────┐
│ V11 Runtime Design Intelligence              │
│                                              │
│ source scanner                               │
│ static markup/CSS scanner                    │
│ rendered/browser observation adapter         │
│ design-system drift checks                   │
│ rule registry + contextual policy            │
│ edit/session/release execution tiers         │
└───────────────────┬──────────────────────────┘
                    ↓
              NUI findings
                    ↓
existing evidence binding / critics / recovery
                    ↓
repair → re-observe → verify
```

The runtime is deliberately subordinate to the cognition graph. It detects observable conditions; owners decide the design meaning and repair when context matters.

## Runtime rule model

A detector rule is a typed machine contract with fields:

- `rule_id`: stable `runtime.<domain>.<name>` identifier.
- `domain`: layout, typography, color, imagery, motion, accessibility-mechanics, browser-residue, runtime-integrity, design-system, copy-pattern or another explicit machine-observable domain.
- `class`: `mechanical | contextual | genericness | advisory`.
- `tier`: `edit | session | release`.
- `severity`: NUI finding severity default.
- `engines`: one or more of `text | markup | css | browser`.
- `description`: observable failure class, not an aesthetic slogan.
- `falsifier`: what evidence would show the finding does not apply.
- `owner_hints`: existing NUI faculties that may own repair; hints do not create routes or ownership.
- `source_provenance`: mechanism/research origin and license metadata where relevant.

### Rule classes

**Mechanical** rules have high enough precision to interrupt an edit: broken image references, content-hidden-at-rest patterns, invalid interactive markup, obvious clipping/overflow declarations, focus-removal without replacement, unsafe animation patterns, malformed design token usage and similar mechanically falsifiable defects.

**Contextual** rules require product/design authority before they can become a violation. A font, visual material, motion behavior or native control is not wrong merely because it resembles a common AI pattern.

**Genericness** rules identify convergence signals such as repeated nested-card templates or reflex decorative treatments. They cannot independently block release. They feed comparative taste and design-specificity criticism.

**Advisory** rules are low-confidence or taste-sensitive signals. They are never counted as hard failures and never run in the edit-time interruption tier by default.

## Context-aware adjudication

A raw match is not automatically a NUI finding. The runtime converts a match through an adjudication step:

```text
raw match
  + task profile
  + product/design authority
  + explicit exception policy
  + rule class
  ↓
adjudicated finding | suppressed-with-provenance | unresolved
```

Suppression is narrow and auditable. It records rule ID, value or selector when applicable, file scope, authority, reason, created revision and optional expiry. An exception does not erase the observation; it changes its disposition.

The adjudicator must preserve three cases:

- `finding`: evidence supports a real violation.
- `accepted-exception`: explicit authority makes the pattern intentional.
- `unknown`: required context is absent, so NUI may ask an owner/critic rather than invent intent.

## Finding integration

V11 emits the existing NUI finding vocabulary instead of inventing a parallel report format. Each runtime finding contains:

- `finding_id`
- `domain`
- `severity`
- concrete `evidence`
- `violated_constraint`
- `user_impact`
- `falsifier`
- `recommended_repair`
- `status`

Additional V11 metadata may include rule ID, engine, file/line/selector, viewport, confidence class, task/revision binding and raw-observation digest.

Runtime observations must be bindable into `rendered-perception-evidence` capture matrices and existing completion/recovery flows.

## Execution tiers

### EDIT tier

Goal: sub-second to low-hundreds-of-milliseconds source feedback where possible.

- Runs only high-precision text/markup/CSS rules.
- Scans changed files, not the repository.
- Must remain useful without browser or LLM access.
- Clean files may stay silent.
- Findings must include a concrete location and repair path.

### SESSION tier

Goal: inspect the complete set of UI files touched in a session without interrupting every edit.

- Runs broader deterministic rules.
- Deduplicates against EDIT findings.
- Adds cross-file design-system drift and repeated-pattern detection.
- Produces a stable finding batch suitable for critique/polish.

### RELEASE tier

Goal: bind source and rendered evidence before a release-relevant claim.

- May require browser/runtime capabilities when available.
- Inspects computed style, geometry, clipping/occlusion, console/runtime failures, representative responsive captures and browser residue.
- A missing required runtime capability yields `UNKNOWN/BLOCKED`, never `PASS`.
- Feeds existing independent critics and completion gates.

## Initial detector scope

The first implementation slice must be intentionally smaller than Impeccable's 59-rule set and higher precision. It starts with independently authored rules in five families:

1. **Runtime integrity** — broken/empty image source, suspicious hidden-at-rest content, invalid empty interactive target patterns.
2. **Accessibility mechanics** — focus suppression without visible replacement, image alt omissions in static markup, animation with no reduced-motion evidence where a rule can be mechanically established.
3. **Layout integrity** — fixed viewport-hostile widths, obvious horizontal-overflow risk declarations, clipping declarations on content containers when mechanically identifiable.
4. **Design-system integrity** — uncontrolled hard-coded presentation values when a supplied token contract explicitly marks an axis as token-owned.
5. **Genericness signals** — nested-card structural repetition and a small number of high-signal AI-template patterns; advisory by default.

The registry is designed for extension, but V11 must prefer ten strong rules with adversarial fixtures over fifty shallow regexes.

## Source detector design

The source detector is dependency-free Python to match NUI's current zero-runtime-dependency core.

Components:

- registry loader/validator;
- extension classifier;
- text observation engine;
- lightweight markup observation engine based on `html.parser` for HTML-like inputs where valid;
- generic line-pattern engine for JSX/TSX/Vue/Svelte/Astro/CSS where full parsing is unavailable;
- adjudicator;
- finding formatter/batch validator;
- path filter and bounded directory walker.

The scanner must never claim AST-level certainty when it only used text heuristics. Evidence records the engine used.

## Browser observation interface

V11 defines a browser-observation protocol before tying NUI to one automation product. A driver returns typed observations such as:

```text
viewport
url / route
selector or stable element locator
bounding box
computed style subset
visible text
accessibility-relevant attributes
scroll dimensions
runtime/console errors
capture artifact ref
```

The NUI core consumes observations; host adapters own how they are collected. This prevents Playwright, browser extensions, Codex Browser, Claude browser tooling or future native drivers from becoming design authority.

The first browser implementation may be a protocol/validator plus CLI ingestion of an observation JSON packet. Direct browser automation can be added without changing rule semantics.

## Hook compiler

NUI keeps one canonical hook contract and generates thin provider projections.

Canonical event vocabulary:

- `ui-file-will-change` when a host supports pre-write inspection;
- `ui-file-changed` for post-write inspection;
- `session-stop` for deep session scan;
- `release-check` for explicit release verification.

Provider adapters map only supported events. Unsupported events remain absent rather than simulated dishonestly.

The hook compiler must expose whether the host can block, advise, run on stop, and return findings to model context. Provider manifests are projections, not duplicated detector logic.

## Command facade

V11 adds ergonomic commands as CLI/macros rather than canonical skills:

- `nui detect` — deterministic runtime scan.
- `nui audit` — route technical critics + deterministic evidence.
- `nui critique` — independent semantic/perceptual criticism + deterministic evidence.
- `nui polish` — consume open findings, route repair owners, require re-observation.
- `nui doctor` — inspect runtime/config/evidence drift.
- `nui live` — future live-selection protocol entry.

The first implementation slice ships `nui detect` and the underlying contracts. Other macros may follow after the kernel is stable.

## Project-local runtime state

Shared and ephemeral state are separated:

```text
.nui/
  runtime.json                 # shared runtime policy/version
  detector-exceptions.json     # shared reviewed exceptions
  findings/                    # optional persisted shared findings
  live/                        # live configuration/protocol artifacts
  cache/                       # ephemeral
  sessions/                    # ephemeral journals
```

User-specific overrides belong in an ignored local file such as `.nui/runtime.local.json`. The implementation must not silently create broad ignore rules.

## Doctor and staleness

`nui doctor` eventually distinguishes:

- tool/runtime version drift;
- schema/config drift;
- evidence staleness after overlapping source changes;
- hook projection drift;
- missing browser capability for required release evidence;
- stale detector exceptions whose bound revision/target disappeared.

Truth drift is never inferred merely from commit count. Doctor reports evidence and routes the owner that can establish truth.

## Live Lab direction

NUI Live Lab is a later V11 subsystem built on the same finding/runtime contracts. The protocol is transactional:

```text
select element
→ capture source + runtime identity
→ bind task/product/design context
→ route existing owners
→ produce materially distinct variants when appropriate
→ preview without committing source
→ independent critique / detector observation
→ user accepts one or discards
→ transactional source application
→ invalidate overlapping old evidence
→ re-observe accepted result
```

Live Lab must preserve framework state and recover from interrupted sessions through an append-only journal. It must never let a browser overlay become a hidden second design system.

## Testing strategy

Every production behavior is developed test-first.

### Registry tests

- reject duplicate rule IDs;
- reject invalid class/tier/engine combinations;
- require falsifier and provenance;
- prove advisory/genericness rules cannot default to edit-blocking behavior.

### Detector tests

Each rule has positive, negative and counterexample fixtures. Counterexamples are mandatory for context-sensitive patterns.

### Adjudication tests

- explicit authority can create a narrow accepted exception;
- missing authority returns unknown when required;
- a broad ignore cannot be created implicitly;
- exception scope and revision are preserved in evidence.

### Batch/finding tests

- every emitted hard finding satisfies NUI finding fields;
- deterministic batch ordering is stable;
- duplicate observations deduplicate without losing evidence.

### CLI tests

- file scan JSON output;
- directory scan filtering;
- clean exit code vs finding exit code vs invalid-input exit code;
- no network dependency.

### Hook tests

- provider capability matrix is explicit;
- unsupported blocking/stop semantics are not claimed;
- generated projections point back to the same canonical detector entrypoint.

### Empirical V10 integration

Later V11 evaluation adds treatments that isolate runtime effects from cognition effects:

- baseline model;
- NUI cognition only;
- NUI + detector;
- NUI + detector + hook;
- NUI + full live/runtime loop.

Claims stay `STRUCTURAL_ONLY` until matched real-model runs satisfy existing V10 gates.

## License and provenance

Impeccable is a mechanism/reference source, not copied implementation. V11 records external mechanism provenance in research/design documentation and independently authors rule wording, code, thresholds and tests. Any future direct Apache-2.0 code reuse must carry the required license/notice and be isolated so NUI's MIT-owned core remains provenance-clear.

## Implementation sequence

1. Runtime rule/finding contracts and validator.
2. Test-first source scanner with a small high-precision registry.
3. CLI `scripts/nui-detect`.
4. Context-aware exception/adjudication layer.
5. Hook capability contract and provider projection support.
6. Browser observation protocol and ingestion validator.
7. Doctor/staleness runtime checks.
8. Live Lab protocol and transactional journal.
9. V10 treatment/ablation integration.

## Success criteria for the first mergeable V11 slice

- zero canonical skill count change;
- no modification to the concurrent skill-expansion branch;
- dependency-free detector kernel in `src/nolane_ui`;
- independently authored rule registry with at least 10 tested rules across at least four families;
- positive, negative and counterexample tests;
- `scripts/nui-detect` returns deterministic JSON and meaningful exit codes;
- emitted findings satisfy NUI's existing finding semantics;
- rule classes prevent taste-sensitive rules from becoming silent hard gates;
- source/provenance boundaries documented;
- full existing unit suite and `scripts/nui-validate .` pass on the feature head before merge claim.

## Deliberately deferred from the first slice

Direct browser automation, HMR variant injection, native-device drivers, full hook installation and large rule-count expansion are deferred until the source kernel proves stable. Their interfaces are designed now so later work extends rather than rewrites the runtime core.
