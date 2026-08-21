# NUI V11 Phase 4 — Aesthetic Generation Governor & Craft Intelligence Design

**Status:** proposed design approved in chat; written-spec review required before implementation

**Date:** 2026-08-21

**Branch:** `build/v11-runtime-design-intelligence`

**Current integration reality:** Batch 006 has merged to `main` and expanded the canonical graph from 774 to 874 skills. The existing V11 branch still contains the Phase 1–3 runtime foundation on the pre-Batch-006 base and must be integrated with current `main` before Phase 4 implementation is considered complete.

## 1. Purpose

V11 Phase 4 turns NUI from a system that can reason about visual quality and detect runtime defects into a system that also governs **how an AI forms and executes a visual direction before code is written**.

The target failure is not merely invalid CSS or inaccessible markup. It is the familiar failure mode where generated UI is technically functional yet visually generic, timid, trend-derived, over-carded, decorative without product causality, or superficially polished in a way that still reads as “AI-generated.”

NUI already contains strong cognitive owners for this problem, including `preventing-generic-ui`, `exploring-aesthetic-directions`, `directing-visual-hierarchy`, typography/color/spacing/surface craft owners, comparative taste protocols, and render-first critique. Phase 4 does **not** create duplicate canonical skills. It operationalizes those existing owners as an execution governor with machine-readable contracts, generation-time checkpoints, rendered comparison, and causal repair closure.

The core thesis is:

```text
NUI cognition decides what should be designed.
The Aesthetic Generation Governor controls how design freedom is spent.
Runtime/Browser intelligence observes what actually got built.
Independent critique and evidence gates decide whether the result is good enough.
```

## 2. Research basis and transfer boundary

Phase 4 is independently authored for NUI. External systems are research references only.

### 2.1 Impeccable

Research value:

- treating “looks AI-generated” as a production-quality problem rather than a vague preference;
- committing to a visual world instead of remaining safe/timid;
- separating a craft floor from direction selection;
- extracting existing visual identity before generating variants;
- requiring materially different variant axes rather than palette swaps;
- bounded browser inspection and iterative finish loops;
- maintaining project-local design memory so subsequent agent work remains on-brand.

NUI will not copy Impeccable skill bodies, rule text, thresholds, schemas, configuration formats, state machines, or implementation code. In particular, NUI will not inherit universal style bans such as fixed radius ranges, font bans, or category-wide light/dark prescriptions.

### 2.2 Anthropic frontend-aesthetics guidance

Research value:

- models tend to converge toward safe/on-distribution visual defaults;
- design quality improves when attention is explicitly allocated across typography, color, motion, backgrounds, and common-default avoidance;
- one cohesive aesthetic with committed choices generally outperforms timid distribution across many weak choices.

NUI adapts this insight as **dimension attention and commitment contracts**, not as a static list of banned fonts, colors, or effects.

### 2.3 Vercel, Primer, Carbon, Linear and mature product craft

Research value:

- production polish is the accumulation of many small coherent decisions, not one hero effect;
- optical alignment, typography metrics, spacing rhythm, interaction feedback, responsive behavior, and state completeness materially affect perceived maturity;
- accessibility and responsive behavior must be designed with the system rather than retrofitted after visual polish;
- quality requires repeated papercut detection and causal repair, not one large redesign pass;
- generated output is not equivalent to design: form must fit product context, user task, and interaction semantics.

### 2.4 Research governance

External references may influence:

- questions NUI asks;
- dimensions NUI observes;
- evaluation methods;
- workflow structure;
- falsification strategies.

They may not silently become:

- NUI house style;
- copied prose/rules;
- aesthetic authority above product/user/platform evidence;
- universal visual bans;
- prestige-reference imitation targets.

Every Phase 4 registry record that names an external influence must retain `implementation: independently-authored` and describe the external source as `research_inspiration` only.

## 3. Non-negotiable constraints

1. **No new canonical skill by default.** Phase 4 must consume the existing 874-skill graph. A new skill is allowed only if a separate admission court proves a genuinely unowned decision/failure topology; this spec identifies no such gap.
2. **No NUI house style.** Minimal, maximal, editorial, utilitarian, playful, brutalist, native, dense, quiet, cinematic, and other directions remain valid when product-specific.
3. **No static anti-AI blacklist as authority.** A gradient, card, Inter, serif, glass, pills, dark mode, grid, or animation is not a failure by itself.
4. **No aesthetic self-certification.** The generator cannot mark its own output VERIFIED or RELEASED.
5. **No scalar beauty score.** Comparative judgment must preserve dimension-level evidence and allow ties or re-divergence.
6. **No missing-capability optimism.** If a required render, viewport, state, or critic capability is unavailable, the relevant conclusion is `UNKNOWN`/`BLOCKED`, never inferred PASS.
7. **No reference imitation authority.** References donate mechanisms and quality bars, never trade dress or exact expression.
8. **No skill ownership synthesis.** Runtime/generation routing may only resolve owners already present in the supplied canonical graph.
9. **No infinite polish loop.** Inspection/repair is bounded and evidence-driven; persistent thesis failure routes to re-divergence instead of endless micro-tweaks.
10. **No stale pre-Batch-006 verification claim.** Phase 4 completion requires exact-head validation on the integrated graph with at least 874 canonical skills.

## 4. System architecture

Phase 4 adds six execution units beneath the cognition graph and above/beside the existing V11 runtime layer.

```text
Canonical NUI cognition graph (874+ skills)
          |
          v
+-------------------------------+
| 1. Design Intent Compiler     |
+-------------------------------+
          |
          v
+-------------------------------+
| 2. Generation Governor        |
+-------------------------------+
          |
          +----------------------+
          |                      |
          v                      v
+-------------------+   +------------------------+
| 3. Dynamic        |   | 4. Project-local       |
| Genericity Engine |   | Design Memory          |
+-------------------+   +------------------------+
          |                      |
          +----------+-----------+
                     v
              generated UI/code
                     |
                     v
        existing V11 source/browser layer
                     |
                     v
+-------------------------------+
| 5. Blinded Taste Court        |
+-------------------------------+
                     |
                     v
+-------------------------------+
| 6. Quality Residue Loop       |
+-------------------------------+
                     |
                     v
          V11 re-observation closure
                     |
                     v
          existing NUI evidence gates
```

The units are deliberately separable. A host may support only some capabilities; absent pieces remain explicit rather than simulated.

## 5. Design Intent Compiler

### 5.1 Responsibility

Compile routed NUI cognition outputs into a bounded, machine-readable **Design Intent Packet** that controls generation without replacing the underlying skill owners.

The compiler does not invent aesthetic direction. It serializes already-supported decisions from product intent, user/task model, selected aesthetic direction, hierarchy/composition/craft contracts, project design-system evidence, and anti-generic analysis.

### 5.2 Design Intent Packet

Versioned contract: `version: 11`, `kind: "aesthetic-generation-intent"`.

Required fields:

```text
intent_id
revision
scope
ambition
mode
product_thesis
user_job
subject_anchors[]
identity_invariants[]
frozen_axes[]
flexible_axes[]
novelty_budget
signature_mechanism
quiet_system[]
composition_principles[]
typography_character
palette_behavior
surface_material_logic
media_role
motion_posture
anti_references[]
preserve[]
rejection_conditions[]
required_owner_outputs[]
source_evidence_refs[]
claim_boundary
```

`claim_boundary` is always `generation-intent-only`.

### 5.3 Modes

`mode` is one of:

- `IDENTITY_LOCKED`: existing product has established visual identity; generation must preserve identity invariants and spend freedom only on explicitly flexible axes.
- `BOUNDED_DEPARTURE`: user/product asks for meaningful refresh while retaining named identity invariants.
- `NEW_DIRECTION`: new surface/product or explicit redesign grants broad visual freedom.
- `IMPLEMENTATION_ONLY`: accepted visual authority already fixes the design; generation must faithfully implement rather than re-explore.

Mode selection must be evidence-bound. A model may not infer “redesign” merely because it prefers a different aesthetic.

### 5.4 Ambition

`ambition` is one of:

- `UTILITY`
- `STANDARD`
- `HIGH`
- `FLAGSHIP`

Ambition changes required exploration/evaluation depth, not hard product/accessibility truth.

## 6. Generation Governor

### 6.1 Responsibility

Control the sequence by which an agent spends visual freedom before writing final UI code.

The governor is a protocol, not a style prompt.

### 6.2 Candidate requirements

- `UTILITY`: one direction is allowed when product conventions and task efficiency dominate; genericity is judged as unearned decoration or category-strangeness rather than insufficient novelty.
- `STANDARD`: one selected direction plus at least one explicit counterfactual when meaningful visual freedom exists.
- `HIGH`: at least two materially distinct candidates before selection when visual freedom is material.
- `FLAGSHIP`: at least three materially distinct candidates when rendering capability exists; if rendering is unavailable, preserve `UNKNOWN` for rendered-divergence evidence and produce mechanism-level candidates only.

### 6.3 Material divergence

Candidates are materially distinct only when they differ on at least two relevant causal axes, and high/flagship work should normally differ on three or more:

- hierarchy/focal authority;
- layout topology/composition silhouette;
- typographic system/personality;
- density/rhythm distribution;
- material/surface logic;
- media/imagery role;
- motion vocabulary;
- structural decomposition/progressive disclosure;
- interaction emphasis;
- signature mechanism.

Palette-only, radius-only, shadow-only, or copy-only variation is not divergence.

### 6.4 Identity protection

In `IDENTITY_LOCKED` mode:

- current tokens/components/computed identity are evidence, not obstacles;
- new font families, palette families, aesthetic-world shifts, or signature replacement require explicit departure authority;
- candidates explore different flexible axes while preserving the identity sentence and frozen axes;
- a candidate that violates an identity invariant is invalid, not merely lower-scoring.

### 6.5 Commitment rule

After selection, the governor records a `Committed Direction Contract`:

```text
direction_id
thesis
subject_causality
signature_mechanism
quiet_system
frozen_axes
flexible_axes
preserve
known_risks
rejection_conditions
```

Subsequent generation must optimize **within** this contract unless a falsifier triggers re-divergence.

This prevents the common failure where an agent explores boldly, then implementation converges back to its safe default shell.

## 7. Dynamic Genericity Engine

### 7.1 Why dynamic

“AI-looking” patterns drift. A fixed blacklist eventually becomes wrong and can itself create a house style. NUI therefore separates stable structural signals from time-bounded trend tells.

### 7.2 Structural signals

Structural signals are long-lived hypotheses about absence of authored decisions. Examples:

- repeated containment replacing hierarchy;
- equal visual weight/density across unrelated regions;
- signature mechanism disconnected from product semantics;
- composition plausible for many unrelated products after noun/logo substitution;
- decorative effect accumulation with low removal cost;
- type roles that fail to create intended hierarchy/personality;
- every section repeating the same spatial formula;
- multiple component sources creating incompatible material worlds;
- “distinctiveness” created only by unusual decoration while information/task structure remains generic.

Structural signals remain contextual/genericness findings and require falsifiers.

### 7.3 Trend tells

Trend tells capture patterns models are currently over-producing. They are not permanent design laws.

Each tell record requires:

```text
tell_id
observed_pattern
first_observed
last_reviewed
review_after
source_provenance[]
applicable_contexts[]
non_applicable_contexts[]
falsifier
status
```

`status` is `ACTIVE | WATCH | RETIRED`.

An expired tell without review cannot contribute to a blocking decision.

### 7.4 Accumulation model

One tell never proves genericity. The engine computes an evidence ledger over:

```text
subject_specificity
semantic_necessity
frequency
cross-region accumulation
hierarchy_cost
interaction_cost
removal_cost
reference_dependence
trend_density
```

It returns typed signals and a qualitative verdict:

- `SPECIFIC`
- `WATCH`
- `GENERICITY_DEBT`
- `UNJUDGABLE`

It does not emit a scalar “AI score.”

### 7.5 Product-substitution falsifier

For high/flagship work, when artifacts permit:

1. mask logos/brand names;
2. normalize or substitute domain nouns;
3. preserve interaction/layout structure;
4. ask whether the shell still fits multiple unrelated product archetypes with little loss;
5. record which mechanisms remain subject-specific and which become interchangeable.

A substitution result is evidence, not aesthetic authority. Familiar task UI may intentionally remain category-conventional.

## 8. Project-local Design Memory

### 8.1 Responsibility

Persist accepted visual invariants and prior causal decisions so subsequent agent runs do not repeatedly rediscover or drift from product identity.

Memory is project-local and revision-aware. It must not become a global style preference.

### 8.2 Memory record

```text
memory_version
project_identity
accepted_mechanisms[]
rejected_mechanisms[]
identity_invariants[]
visual_tokens_or_refs[]
signature_history[]
preserve_patterns[]
known_genericity_traps[]
last_verified_revision
```

Every memory assertion carries provenance (`user`, `design-system`, `rendered-evidence`, `accepted-direction`, etc.). Model preference is the weakest provenance.

### 8.3 Staleness

Project memory follows the same causal principle as V11 evidence binding:

- overlapping identity/design-system changes may mark relevant memory `STALE`;
- unrelated code changes do not invalidate it;
- missing source state yields `UNKNOWN`;
- stale memory remains visible and is never silently deleted.

## 9. Craft Floor Runtime

### 9.1 Purpose

Extend V11 runtime observation beyond correctness defects into bounded craft observations that explain why technically valid UI may still feel immature or AI-generated.

The craft floor is **not** direction selection. The committed direction and product truth remain higher authority.

### 9.2 Rule admission

A craft rule is admitted only when it has:

- observable evidence;
- explicit scope;
- falsifier;
- class/tier/severity;
- existing NUI owner hints;
- negative examples/false-positive tests;
- explanation of why the behavior is not merely personal taste.

No target rule count is allowed. Phase 4 must not imitate another repository’s detector count.

### 9.3 Candidate rule families

Candidate families to implement only where evidence is sufficiently deterministic/contextual:

- repeated equal-radius/equal-border containment accumulation;
- excessive separator/border density relative to actual object boundaries;
- typography role collapse (insufficient hierarchy between known role classes);
- heading/body line-measure outliers under supplied typography contracts;
- repeated all-caps micro-label accumulation;
- inconsistent interactive control heights within the same component family;
- mismatched adjacent radii/borders/elevation in declared shared groups;
- uncontrolled shadow/material vocabulary drift;
- repeated decorative pills/badges without state/metadata semantics;
- motion accumulation or incompatible timing vocabularies when motion evidence exists;
- generic copy-density signals only when copy contracts classify terms as non-domain filler;
- desktop-to-mobile thesis loss where capture evidence proves generic stacking erased priority/signature.

Exact rules must be independently designed in TDD and may be rejected during implementation if falsification quality is insufficient.

### 9.4 Rule authority

- `mechanical`: may block only for truly mechanical craft/integrity failures.
- `contextual`: requires product/design-system authority to confirm violation.
- `genericness`: never edit-time blocks by itself.
- `advisory`: observation only.

This preserves the Phase 1–3 authority model.

## 10. Blinded Taste Court

### 10.1 Responsibility

Compare rendered candidates or before/after states without allowing the generator’s self-rationale, preferred label, or prestige reference to dominate judgment.

### 10.2 Inputs

Required when available:

- candidate/render references;
- task and product intent;
- accepted hard constraints;
- viewport/state identifiers;
- dimension list;
- preserve list.

Excluded from judge input by default:

- generator self-score;
- “preferred candidate” label;
- source prestige/brand names where not needed for truth;
- generator rationale about why its own candidate should win.

### 10.3 Comparison dimensions

The court may compare:

- focal authority;
- compositional tension/coherence;
- negative-space quality;
- density modulation;
- typographic character and rendered metrics;
- optical alignment;
- rhythm/cadence;
- material precision/restraint;
- signature-to-quiet ratio;
- subject/domain specificity;
- audience fit;
- motion posture;
- responsive durability;
- perceived production maturity;
- preservation of task/state/accessibility truth.

Every dimension verdict is:

`LEFT | RIGHT | TIE | UNJUDGABLE`

with observable evidence and causal rationale.

### 10.4 Court outcome

`PREFER_LEFT | PREFER_RIGHT | TIE | RE_DIVERGE | BLOCKED`

The court never produces a universal beauty score.

Hard regressions in accessibility, product truth, interaction semantics, security, or functional closure are non-compensatory.

## 11. Quality Residue Loop

### 11.1 Purpose

After the macro direction survives critique, run a bounded pass for small accumulated defects that create a “cheap”, unfinished, or AI-generated impression despite otherwise correct structure.

### 11.2 Residue classes

Examples include:

- one-off optical misalignment;
- inconsistent control heights;
- nearby elements using slightly conflicting radius/material rules;
- dirty/stacked shadow residue;
- accidental double borders;
- weak icon/text baseline alignment;
- awkward line wraps at critical widths;
- hover/focus timing mismatch;
- mobile safe-area/overlay roughness;
- inconsistent media crop/edge treatment;
- browser-default residue that conflicts with the committed system;
- spacing discontinuities that break an otherwise stable rhythm.

### 11.3 Bounded operation

Default maximum:

1. one batched residue observation pass;
2. one repair batch;
3. one confirmation re-observation.

If macro hierarchy/thesis still fails, stop residue polishing and route back to the owning macro layer or `RE_DIVERGE`.

## 12. Integration with existing V11 Phase 1–3

Phase 4 reuses, rather than replaces:

- runtime rule registry and rule classes;
- source detector;
- browser observation protocol;
- adjudication;
- evidence binding/freshness;
- runtime Doctor;
- existing-owner routing;
- repair re-observation closure;
- Live Lab transaction safety and closure journal.

New generation/craft findings must flow through the same NUI finding vocabulary and evidence-only ownership boundary.

The resulting loop is:

```text
product/task context
  -> NUI cognition routing
  -> Design Intent Packet
  -> governed divergence / identity lock
  -> committed direction
  -> implementation
  -> source/browser runtime observation
  -> craft/genericity findings
  -> route to existing owners
  -> repair or re-diverge
  -> blinded rendered comparison
  -> residue pass
  -> re-observation closure
  -> existing completion gates
```

## 13. Batch 006 / graph-874 integration strategy

Before Phase 4 implementation work modifies runtime behavior, V11 must be integrated with current `main`.

Required integration properties:

1. preserve every Batch 006 canonical skill and `skills/skill-graph.json` node;
2. preserve all V11 Phase 1–3 runtime files/tests;
3. resolve V11 runtime `owner_hints` against the 874-skill graph;
4. replace obsolete hint slugs only when a current existing owner is semantically correct;
5. retain unresolved hints explicitly when no current owner exists; do not create skills to make counts look complete;
6. run the full repository suite and exact-revision validator after integration;
7. update PR #22 evidence from 774 to the actual integrated graph count;
8. do not claim Phase 4 complete until the integrated PR is mergeable and exact-head CI is green.

The implementation may merge current `main` into the V11 branch or reconstruct an equivalent integration branch, but history manipulation must not discard either side’s independent work.

## 14. Schemas and proposed modules

Phase 4 should prefer focused modules rather than expanding existing files indefinitely.

Proposed new schemas:

- `schemas/aesthetic-generation-intent-v11.schema.json`
- `schemas/aesthetic-genericity-ledger-v11.schema.json`
- `schemas/aesthetic-taste-comparison-v11.schema.json`
- `schemas/aesthetic-project-memory-v11.schema.json`

Proposed runtime modules:

- `src/nolane_ui/runtime_v11/aesthetic_intent.py` — validate/build Design Intent Packets.
- `src/nolane_ui/runtime_v11/generation_governor.py` — mode/ambition/candidate/divergence contracts.
- `src/nolane_ui/runtime_v11/genericity.py` — structural signals, trend-tell lifecycle, accumulation ledger.
- `src/nolane_ui/runtime_v11/design_memory.py` — project-local identity memory and scoped staleness.
- `src/nolane_ui/runtime_v11/taste_court.py` — blinded pairwise dimension ledger and bounded verdict aggregation.
- `src/nolane_ui/runtime_v11/residue.py` — bounded residue classification/closure contracts.

The detector/browser modules may gain admitted craft observations, but taste logic must not be embedded as opaque regexes inside `detector.py`.

## 15. Error and uncertainty handling

### 15.1 Missing inputs

If required owner outputs or design evidence are absent:

- compiler returns incomplete obligations;
- governor cannot fabricate identity or brand truth;
- mode-sensitive claims become `UNKNOWN`/`BLOCKED` depending on severity.

### 15.2 Conflicting authority

Use the canonical NUI authority order. Explicit product/safety/platform/design-system truth outranks model aesthetic preference. A taste court cannot override hard truth.

### 15.3 Judge uncertainty

`TIE` and `UNJUDGABLE` are first-class outcomes. The system must never manufacture a winner to progress lifecycle state.

### 15.4 Trend-tell staleness

Expired/unreviewed trend tells remain auditable but are excluded from blocking contribution until reviewed.

### 15.5 Reference contamination

If a candidate’s advantage is mainly recognizable resemblance to a prestigious reference, run a reference-blind/product-native countercomparison. Prestige resemblance is not evidence of product fit.

## 16. Evaluation and falsification

Phase 4 is an **artifact/protocol implementation** until real matched model experiments prove efficacy. Repository CI must not claim that NUI objectively makes every model more beautiful.

### 16.1 Structural tests

Must cover:

- packet/schema validation;
- mode invariants;
- candidate divergence rejection for palette-only variants;
- identity-lock violations;
- no owner synthesis;
- trend-tell expiry;
- single-tell non-blocking behavior;
- genericity accumulation behavior;
- product-substitution packet logic;
- blinded judge payload stripping generator preference metadata;
- `TIE`/`UNJUDGABLE` preservation;
- hard-regression non-compensation;
- bounded residue loop;
- project-memory staleness;
- 874+ graph compatibility.

### 16.2 Adversarial fixtures

Include at minimum:

- polished but interchangeable AI SaaS shell;
- product-specific quiet utilitarian interface that should not be penalized for low novelty;
- justified card-heavy object browser;
- unjustified nested-card marketing shell;
- established identity where governor attempts unauthorized redesign;
- three “variants” that only recolor one topology;
- expressive candidate that improves memorability but harms focus/accessibility;
- prestigious-reference lookalike vs less fashionable product-native candidate;
- expired trend tell that would otherwise bias the court;
- incomplete browser capability that cannot prove rendered divergence.

### 16.3 Future empirical evaluation

Real efficacy claims require matched baseline/full/ablation runs under the existing V10 empirical framework, including holdout tasks, blinded judges, treatment provenance, hard-regression accounting, and more than one model lineage before transfer claims.

Relevant Phase 4 ablations should eventually include:

- no Design Intent Compiler;
- no Generation Governor;
- no Dynamic Genericity Engine;
- no Blinded Taste Court;
- no Project-local Design Memory;
- no Residue Loop.

Until those experiments exist, claim ceiling remains structural/protocol-level.

## 17. Acceptance criteria

Phase 4 is complete only when all of the following are true:

1. V11 is integrated with current main and the canonical graph is at least 874 skills.
2. No Batch 006 skill or graph node is lost.
3. No Phase 4 canonical skill is added unless separately admitted by an explicit court; default expected count remains unchanged by Phase 4.
4. Design Intent Packet contract is implemented and validated.
5. Generation Governor enforces mode, ambition, identity lock, and material divergence.
6. Dynamic Genericity Engine separates structural signals from expiring trend tells.
7. Genericity decisions preserve contextual falsifiers and never reduce to a scalar AI score.
8. Project-local Design Memory is provenance-bound and supports scoped staleness.
9. Blinded Taste Court strips generator preference metadata and preserves ties/unknowns.
10. Quality Residue Loop is bounded and routes macro failure back upstream rather than polishing forever.
11. Admitted craft observations use the existing V11 rule authority model.
12. All new outputs preserve explicit claim boundaries below VERIFIED/RELEASED authority.
13. New public APIs are exported through `runtime_v11/__init__.py` and top-level aliases where appropriate.
14. Runtime Doctor covers all required Phase 4 artifacts without silently mutating them.
15. Full unit/contract suite is green on the exact integrated head.
16. `scripts/nui-validate` reports repository valid with no errors on the exact integrated revision.
17. Fresh completion packet decision is PASS.
18. PR #22 or its explicitly superseding integration PR is mergeable at the verified head.
19. PR documentation states external research is inspiration only and does not imply copied implementation.
20. Changed-path review confirms Phase 4 does not accidentally introduce template-generated canonical skill prose.

## 18. Explicit non-goals

Phase 4 does not:

- build a universal design generator model;
- add an image-generation model;
- guarantee objective beauty;
- replace human/product authority;
- copy another project’s aesthetic language;
- rank all UIs on one beauty/AI score;
- ban popular fonts/components/effects globally;
- require novelty for utilitarian/task-dense software;
- make every surface flagship;
- turn runtime heuristics into canonical skills;
- perform endless autonomous polish;
- claim cross-model empirical improvement without real experiments.

## 19. Intended end state

After Phase 4, a capable host should no longer receive only “make a beautiful UI” plus a large body of design knowledge. It should receive an executable design discipline:

```text
understand the product
-> bind identity and task truth
-> decide how much visual freedom exists
-> explore causally different directions when warranted
-> commit to one direction
-> generate within its invariants
-> inspect the actual render
-> detect genericity/craft residue without style dogma
-> compare alternatives blindly when judgment is ambiguous
-> repair the smallest causal mechanism
-> re-observe the same scope
-> preserve project identity for the next run
-> let existing NUI evidence gates decide completion
```

That is the Phase 4 definition of “anti-AI UI”: not unusual decoration, but **authored causality, product specificity, coherent commitment, rendered craft, and falsifiable evidence**.