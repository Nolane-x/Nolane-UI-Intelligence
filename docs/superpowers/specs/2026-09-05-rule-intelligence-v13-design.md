# NUI V13 Rule Intelligence Architecture

## Status

Approved for implementation on 2026-09-05.

## Purpose

NUI V13 turns the current V12 reality catalog into a larger, evidence-disciplined Rule Intelligence system without turning repository size into a quality claim. The goal is to support more than one thousand distinct, operational UI rules over time while preserving truth, falsifiability, ownership, capability honesty, and anti-duplication guarantees.

The system must be stronger than a flat anti-slop blacklist. A canonical rule exists because it captures a distinct decision or failure class with a distinct applicability boundary, consequence, repair or verification contract. It does not exist merely because a similar rule can be reworded for another component noun.

The uploaded `artifacts.zip` and `anti-ai-ui-slop-design-convergence-research-corpus-2026-09-01.md` are research inputs, not canonical authority. Their claims are reclassified before adoption. In particular, an aesthetic or convergence tell such as a centered hero, a purple gradient, a particular font, a bento layout, or exactly three cards is never a hard defect by itself. A product-truth failure, accessibility failure, broken interaction, misleading state, unsafe flow, or objectively falsifiable runtime defect can be blocking when its consequence and evidence justify that authority.

## Governing invariants

1. **No quota-driven rule generation.** Rule count is descriptive, never a completion target.
2. **No noun-substitution duplication.** Rules that differ only by component noun must merge unless their failure, consequence, repair, exception, ownership, or verification boundary materially differs.
3. **No citation-as-substitute-for-rule-quality.** User-facing rule text must stand on operational truth. Provenance is retained internally and never compensates for vague wording.
4. **No detector overclaim.** Missing observation capability yields `UNKNOWN`/`UNSUPPORTED`, never a fabricated PASS.
5. **No style-tell blocker.** Advisory, aesthetic, and convergence classes cannot block release by themselves.
6. **No single slop score as authority.** Aggregates may summarize evidence, but hard gates remain non-compensatory and per-rule.
7. **No self-certification.** Generation, detection, critique, and completion authority remain separate.
8. **No stale current-truth claim.** Version/config/public API/repository validation must refer to the same current system revision semantics.
9. **No hidden provenance promotion.** Community or emerging reports cannot silently become normative requirements.
10. **No implementation copy disguised as research.** External projects may inform mechanisms and hypotheses; NUI rule wording, schemas, thresholds, tests, and implementation remain independently authored.

## Four planes

### 1. Reality rules

Reality rules describe objective or consequence-grounded failures: operability, accessibility, state truth, recovery, data truth, safety, privacy, interaction integrity, responsive behavior, performance, product workflow integrity, and similar concerns.

A reality rule can become `block`, `warn`, or `review` according to class and consequence. Blocking requires both an eligible rule class and sufficiently strong evidence for the affected scope.

### 2. Convergence signals

Convergence signals describe repeated statistical/default design behavior. They are observations, not authorship detectors and not style bans.

Examples include repeated generic hero structure, decorative pill accumulation, uniform cardification, decorative gradient text, generic developer typography, undifferentiated feature icon tiles, and cross-generation macrostructure similarity.

A signal becomes meaningful through accumulation, co-occurrence, product substitution evidence, absence of product-specific exceptions, or repeated similarity across generations. Legitimate product/brand/content justification remains a falsifier.

### 3. Provenance ledger

Provenance explains why a rule or signal exists and how strongly it is supported. It is deliberately separate from the operational rule body.

Evidence classes:

- `normative`: standard, platform requirement, regulation, protocol, or another primary authority.
- `reproduced`: independently reproducible implementation/runtime failure.
- `corroborated`: multiple independent primary/practitioner/research observations support the same bounded mechanism.
- `emerging`: early field report or low-confidence hypothesis; may inform radar/review but cannot hard-block.
- `internal-derived`: rule follows from NUI-owned lifecycle/product-truth invariants and is independently falsifiable.

The ledger records source IDs, evidence class, reporter/source role, reviewed date, support role, contraindications, and transfer boundary. Canonical rule text does not require inline citations.

### 4. Observation capability contracts

Each rule declares which evidence modes can support it:

- `static`
- `dom`
- `computed-style`
- `browser-runtime`
- `interaction`
- `accessibility-tree`
- `visual-render`
- `semantic-product`
- `cross-generation`
- `human-review`

Each mode has status `SUPPORTED`, `PARTIAL`, `REQUIRED`, or `UNSUPPORTED`. Provider identity cannot upgrade a capability.

## Canonical rule contract

A V13 rule contains at least:

- `rule_id`
- `domain`
- `class`
- `severity`
- `enforcement`
- `title`
- `statement`
- `intent`
- `applies_when[]`
- `does_not_apply_when[]`
- `failure_modes[]`
- `user_impacts[]`
- `observables[]`
- `falsifiers[]`
- `repairs[]`
- `exceptions[]`
- `verification[]`
- `owner_hints[]`
- `verifier_hints[]`
- `capabilities{}`
- `provenance_ids[]`
- `status`
- optional lifecycle metadata such as `first_seen`, `last_reviewed`, `model_era`, `supersedes[]`, `complements[]`, and `conflicts_with[]`.

Operational arrays are plural because serious rules often require more than one observable or verification path. The schema rejects placeholder-strength prose and incoherent authority combinations.

## Rule classes

V13 keeps the V12 semantic distinction and adds explicit convergence separation:

- `mechanical`
- `behavioral`
- `contextual`
- `advisory`
- `aesthetic`
- `convergence`

`advisory`, `aesthetic`, and `convergence` cannot use `enforcement=block`.

## Rule sharding

The canonical catalog is no longer authored as one enormous Python list. It is composed from independently reviewable shards under `src/nolane_ui/rules_v13/`.

Initial shard families:

- accessibility and alternative input
- forms/authentication/permissions
- navigation/state/async/recovery
- responsive/layout/platform
- data/table/chart/visualization
- editor/canvas/selection/direct manipulation
- performance/motion/media
- content/localization/data truth
- privacy/security/trust
- commerce/financial/high-consequence
- AI/agent/generative UI
- component/design-system/token behavior
- native/device/platform-specific behavior
- convergence/aesthetic/product-fit signals

Shards are allowed to grow unevenly. No validator requires a minimum rule count per family.

## Anti-duplication court

`rule_similarity_v13` performs deterministic duplicate and boilerplate analysis without an AI dependency.

It detects:

- exact duplicate rule IDs;
- exact duplicate normalized titles/statements;
- high token-shingle overlap across operational fields;
- high character-shingle overlap after component/domain noun normalization;
- identical failure/repair/verification signatures under different IDs;
- suspicious boilerplate concentration;
- near-identical rules produced by noun substitution.

A similarity finding does not automatically merge rules. It blocks catalog validation when similarity crosses a strict duplicate threshold unless the rule declares a bounded `distinct_from[]` rationale that identifies a materially different failure, consequence, repair, verification, or ownership boundary.

The anti-duplication court itself is falsifiable through adversarial tests containing legitimate near-neighbor rules that must remain distinct.

## Provenance promotion rules

Promotion is monotonic and explicit:

- `emerging` may become `corroborated` after independent support/review;
- `corroborated` may become a stronger current rule only when the operational failure is independently defensible;
- `normative` authority belongs only to actual normative/primary sources;
- removal or drift of a source never rewrites historical provenance but can change current status;
- no number of community reports transforms an aesthetic preference into a universal blocker.

## Detection and adjudication

V11 runtime remains the canonical evidence engine. V13 does not create a second universal detector.

Rules can bind to existing or future detector rule IDs, browser observation types, interaction tests, or review requirements. For every rule, the system can answer:

- what can be observed automatically;
- what capability is missing;
- what remains contextual or human judgment;
- what evidence would falsify the finding;
- what re-observation closes the finding.

A clean static scan certifies only static-supported assertions. It cannot close visual, interaction, accessibility-tree, semantic-product, or cross-generation requirements.

## Convergence adjudication

Convergence uses evidence vectors rather than a scalar authority score:

- active signals
- signal families
- co-occurrence density
- product-substitution evidence
- cross-generation similarity
- project design-memory conflicts
- explicit product/brand/content justifications
- unknown capability dimensions

A single familiar pattern remains an observation. Escalation requires accumulation or semantic evidence.

## Unified current-head integrity court

`validate_repository()` becomes the public current-head validator and composes:

- inherited V7-V10 repository checks;
- V11 runtime installation/registry checks;
- V12/V12.1 external UI and reference-execution structural checks;
- V12 reality compatibility;
- V13 rule catalog + provenance + anti-duplication checks;
- version/config/public API coherence.

Historical validators remain historical and keep their bounded claim semantics. Current validation does not rewrite V10's `STRUCTURAL_ONLY` efficacy ceiling.

## Version truth

`pyproject.toml`, `nui.config.json`, public `get_status`, documentation current-version badges, and repository metrics must derive from a coherent current package/system version. Historical files may retain historical version language when explicitly historical.

V13 changes the package version to `0.13.0` and the current config version to `0.13.0`.

## Public API and MCP

Top-level Python API exports supported V13 rule functions with explicit names.

MCP adds bounded read/analysis tools:

- catalog status
- exact rule lookup
- domain/family query
- provenance lookup
- rule capability explanation
- runtime doctor summary

MCP does not add arbitrary shell/network authority and does not mutate product source.

## Fingerprint coherence

V12.1 external-reference task fingerprints are expanded to include all routing dimensions that can materially change source/reference selection, including platform surfaces, modalities, temporal/social context, named external source, adoption intent, rich interaction, evidence capabilities, stack, visual ambition, and material UI state.

## Testing strategy

TDD is mandatory for behavior changes.

Required test classes include:

- schema/contract validation;
- placeholder-strength rejection;
- authority/class invariants;
- provenance validation and promotion boundaries;
- duplicate/near-duplicate/boilerplate adversarial cases;
- legitimate-neighbor non-duplication controls;
- capability-truth behavior;
- convergence non-blocking behavior;
- unified repository validation;
- version coherence;
- MCP/public API exposure;
- routing/fingerprint change sensitivity;
- current documentation consistency checks where machine-verifiable.

CI remains the final repository oracle. Real browser tests retain their existing optional/live boundary and Chromium smoke gate.

## Initial migration posture

Existing V12 reality rules remain valid through a compatibility adapter while V13 shards are introduced. Migration must not silently weaken an existing V12 blocker.

The 44 uploaded anti-slop rules are triaged individually:

- objective product/accessibility/runtime failures may become V13 reality rules;
- aesthetic/default-pattern items become convergence signals;
- unsupported detector claims become capability gaps;
- scalar slop-score authority is rejected;
- provenance is captured from the uploaded corpus/source registry but rule text is independently authored.

## Completion criteria for the V13 foundation

The foundation is complete when:

1. V13 contracts and provenance model validate independently.
2. Anti-duplication court catches synthetic noun-substitution duplicates and allows legitimate near-neighbors.
3. Existing V12 rules can be normalized into V13 form without authority loss.
4. At least one independently authored shard demonstrates the full contract and mixed rule classes.
5. Current repository validation includes V11/V12/V13 structural integrity and version coherence.
6. Top-level API and MCP expose bounded V13 read/analysis functions.
7. CI passes on the exact branch head.

The >1000-rule corpus is a staged authoring program built on this foundation. Rule count alone never constitutes completion or quality evidence.