# NUI v5 Affective & Aesthetic Intelligence — Design Specification

## Status
Approved by the user's explicit v5 completion request and the supplied 36-finding ATLAS/NUI-v4 failure analysis. This specification treats the critique as acceptance criteria rather than optional suggestions.

## Problem statement
NUI v4 is strong at design governance, task/product reasoning, external UI ecosystem research, implementation closure, and deterministic structural validation. Its demonstrated failure is different: correct local rules can compose into an undesirable visual attractor while all structural/runtime checks stay green. Affective intent can be operationalized away, high visual ambition can be routed like ordinary product UI, anti-generic rules can be known but unenforced, and a visual critic can reward faithful execution of a direction that was inadequate for the original intent.

ATLAS is the regression case: a system can render without overflow/errors and still fail the actual request for exceptional beauty, awe, magnitude, and aspirational scientific identity.

## Design alternatives considered

### A. Patch-only v4
Add clauses to existing craft skills. Low migration cost, but repeats the v4 failure mode: prose knowledge without global enforcement. Rejected as the primary architecture.

### B. One monolithic “pro-beauty” skill
Give one specialist ownership of visual excellence. Simple routing, but it would compete with typography/color/layout/data-viz/motion owners, become too broad, and still lack executable gates. Rejected.

### C. Affective & Aesthetic Enforcement Spine — selected
Add a small set of non-overlapping v5 decision owners plus deterministic validators and evidence schemas. Existing craft faculties remain authoritative in their domains; v5 owns preservation of experiential intent, ambition escalation, global accumulation, adequacy, semantic visualization evidence, escape from bad aesthetic basins, and cross-surface/skill-interaction evaluation.

## Architecture

The v5 control path is:

`RAW USER INTENT`
→ `EXPERIENTIAL INTENT`
→ `VISUAL AMBITION`
→ `HARD ROUTES`
→ `DIVERGENT RENDERED CANDIDATES + REFERENCE FRONTIER`
→ `CRAFT EXECUTION`
→ `GLOBAL PERCEPTUAL/SEMANTIC EVIDENCE`
→ `THESIS EXECUTION CRITIC`
→ `THESIS ADEQUACY CRITIC`
→ `KEEP / RE-DIVERGE / BLOCK`
→ `AESTHETIC RELEASE GATE`

Operationalization supplements affective language; it may not replace or delete it.

## New v5 decision owners

1. `preserving-experiential-intent`
   - Owns desired feelings, forbidden feelings, emotional intensity, memorability target, identity projection, and magnitude targets.
   - Output: `experiential-intent`.

2. `directing-visual-ambition`
   - Owns `utilitarian | polished | distinctive | flagship | exceptional | experiential` classification and escalation policy.
   - Output: `visual-ambition-contract`.
   - Flagship/exceptional/experiential triggers non-optional visual hard routes.

3. `modeling-aspirational-identity`
   - Owns actual/aspirational role, perceived power/agency, competence signaling, rituals, institutional presence, emotional reward, symbolic objects.
   - Output: `aspirational-identity-model`.

4. `composing-spatial-dramaturgy`
   - Owns magnitude semantics and compression/expansion/reveal/quiet/monumental moments rather than merely geometric correctness.
   - Output: `spatial-drama-contract`.

5. `detecting-aesthetic-attractors`
   - Owns global trope accumulation, subject specificity, removal cost, information gain, boundary/material repetition, and anti-timidity checks.
   - Output: `aesthetic-attractor-audit`.

6. `engineering-visual-legibility`
   - Owns computed-style legibility evidence, microtext budget, compound-risk escalation, and resolved-font evidence.
   - Output: `visual-legibility-evidence`.

7. `directing-visual-energy`
   - Owns expressive dynamic range relative to the experiential target: luminance range, chroma mass, focal color mass, material variation, warm/cool tension and depth contrast.
   - Output: `visual-energy-contract`.
   - It defines neither a universal color minimum nor a scalar “beauty score”.

8. `deepening-signature-mechanisms`
   - Owns semantic, interaction, visual and information depth of signature mechanisms plus product specificity, memorability and failure-if-removed.
   - Output: `signature-depth-contract`.

9. `proving-visual-encoding-semantics`
   - Owns channel provenance for non-decorative visualization: position, radius/size, edge, color, opacity, motion, texture and other channels must declare meaning or explicitly be decorative.
   - Output: `encoding-provenance-table`.

10. `critiquing-aesthetic-adequacy`
    - Independent from thesis execution critique. Asks whether the chosen direction was adequate to original experiential intent and visual ambition.
    - Output: `aesthetic-adequacy-findings`.

11. `escaping-aesthetic-basins`
    - Owns escalation from local refinement to re-divergence when affective fit, distinctiveness, reference-frontier comparison, or signature depth repeatedly underperform.
    - Output: `aesthetic-basin-decision`.

12. `evaluating-perceptual-diversity`
    - Owns coherent diversity across screens/workspaces: dominant geometry, density, signature, visualization grammar, surface pattern, typography gesture, color mass and interaction signature.
    - Output: `workspace-visual-matrix`.

13. `testing-skill-interactions`
    - Owns semantic mutation tests, factorial/ablation interaction tests, transfer cases, and causal claims about whether a skill changes decisions rather than merely exists as prose.
    - Output: `skill-interaction-evidence`.

These owners intentionally do not replace typography, color, motion, data visualization, hierarchy, surface, reference research or rendered iteration skills.

## Experiential intent contract

`EXPERIENTIAL_INTENT` must preserve:
- `desired_feelings[]`
- `forbidden_feelings[]`
- `identity_projection`
- `emotional_intensity` in `[0,1]`
- `memorability_target` in `[0,1]`
- `magnitude_target` with `scope`, `data`, `spatial`, `institutional`, `temporal`, `network`, `visual`
- `source_language[]` preserving user phrases or faithful paraphrases
- `operational_proxies[]` that supplement the above

A contract fails if experiential fields are silently replaced by only density/hierarchy/material/token proxies.

## Visual ambition and hard routing

Ambition levels:
- `utilitarian`
- `polished`
- `distinctive`
- `flagship`
- `exceptional`
- `experiential`

For `flagship | exceptional | experiential`, mandatory routes include:
- `preserving-experiential-intent`
- `directing-visual-ambition`
- `exploring-aesthetic-directions`
- `researching-visual-references`
- `directing-visual-hierarchy`
- `crafting-typography`
- `crafting-color`
- `crafting-spacing-and-rhythm`
- `crafting-depth-and-surfaces`
- `directing-iconography-and-imagery`
- `designing-motion`
- `preventing-generic-ui`
- `detecting-aesthetic-attractors`
- `engineering-visual-legibility`
- `directing-visual-energy`
- `deepening-signature-mechanisms`
- `critiquing-visual-design`
- `critiquing-aesthetic-adequacy`
- `iterating-rendered-visual-design`
- `escaping-aesthetic-basins`

When visualization is material, add `designing-data-visualization` and `proving-visual-encoding-semantics`.
When status/role fantasy language is material, add `modeling-aspirational-identity`.
When magnitude/scale language is material, add `composing-spatial-dramaturgy`.
For multi-screen products at high ambition, add `evaluating-perceptual-diversity`.

The router may not drop these routes merely to save context.

## Divergence artifact gate

When visual freedom is high and ambition is at least flagship:
- require at least three materially different candidates;
- candidates must differ in more than palette: composition logic, typography character, density/rhythm, surface/material treatment, media/visualization role, and signature mechanism are comparison dimensions;
- each candidate records a rendered evidence reference when the host can render;
- the selected candidate must be compared against a reference frontier and at least one alternative direction.

Missing required divergence is BLOCKED/UNKNOWN, not a soft recommendation.

## General aesthetic attractor detector

For each repeated visual mechanism, collect:
- `semantic_necessity`
- `subject_specificity`
- `frequency`
- `information_gain`
- `emotional_contribution`
- `removal_cost`

A probable trope is escalated when frequency is high while subject specificity and removal cost are low. The detector is mechanism-general; it does not ban “cyberpunk HUD” or any named style dogmatically.

Global metrics also inspect:
- `boundary_density`
- `edge_density`
- `surface_entropy`
- `boundary_repetition`
- `material_variety`
- `quiet_region_ratio`

This closes the card-soup → pane/border-soup loophole.

## Legibility and typography evidence

Computed/rendered evidence, when the host can provide it, takes priority over grep of source CSS.

Microtext policy:
- below 11 CSS px: semantic reason required;
- below 10 CSS px: cannot contain required task information;
- below 9 CSS px: decorative/auxiliary only;
- small + low contrast + uppercase + tracking compounds risk and escalates severity.

Resolved type evidence includes intended family, actual resolved family, loading status, fallback delta, key numeric metrics/glyph coverage where relevant, and layout-shift risk. Expert-user/data-dense context never implies “make all text small”; information throughput is optimized subject to a protected legibility floor.

## Visual energy

Color/restraint is conditional on experiential intent. High awe/beauty/presence does not imply more saturation; it does require the critic to test whether restraint has collapsed expressive energy.

Evidence dimensions:
- luminance range
- chroma mass
- focal color mass
- warm/cool tension when applicable
- depth contrast
- material variation

Absence of a memorable mechanism is itself a finding at flagship+ ambition unless the candidate demonstrates that quietness is the intentional, distinctive mechanism.

## Aspirational identity and magnitude

Role fantasy is treated as product experience, not avatar copy. Evidence can include strategic overview, orchestration authority, delegation, institutional scale, research lineage, rituals, meaningful alerts, symbolic objects and programs/resources under the user's control.

Magnitude is decomposed into scope/data/spatial/institutional/temporal/network/visual magnitude. “Huge” may not be satisfied by adding pages/menu items alone.

## Spatial dramaturgy

Layouts may define:
- compression zones
- expansion zones
- reveal moments
- monumental-scale moments
- quiet fields
- institutional anchors
- depth transitions
- viewport occupation strategy

This strengthens, but does not override, information architecture and responsive/accessibility obligations.

## Signature depth

A signature mechanism is evaluated on:
- semantic depth
- interaction depth
- visual depth
- information gain
- product specificity
- reusability
- memorability
- failure-if-removed

A decorative topology/diagram with hard-coded positions that encode no relation cannot pass semantic depth merely because it looks scientific.

## Visualization semantics and art direction

Pipeline:
`analytical question → data semantics → truthful encoding → encoding provenance → visualization grammar → coordinated system composition`.

Every non-decorative channel must map to meaning. If a channel has no defensible meaning, mark it decorative or remove it. Visual art direction may improve character, notation, coordination and spatial narrative but cannot falsify data semantics.

## Motion as dynamic information

When the product thesis is dynamic/living, motion must be considered as a possible information channel for propagation, state change, lineage, causal updates, simulation progress, memory consolidation, etc. “Restrained” may not collapse to near-static by default. Reduced-motion alternatives remain mandatory.

## Dual critics and epistemic lineage

Two separate questions:
1. Thesis execution: did the implementation faithfully execute the selected direction?
2. Thesis adequacy: was the selected direction itself good enough for the original intent/ambition?

Adequacy may reopen exploration.

Critic evidence records `generator_model`, `generator_context`, `critic_model`, `critic_context`, optional visual/human judge and a `correlation_class`. Same-model/same-context roles are `CORRELATED`, never silently treated as epistemically independent.

## Basin escape

A visual iteration must choose between local refinement and re-divergence.

Return `RE_DIVERGE` when any configured condition is met, including:
- affective fit remains below target;
- distinctiveness remains below target;
- repeated comparison loses to the reference frontier;
- signature depth remains below required level;
- adequacy critic identifies wrong aesthetic basin.

A mediocre baseline plus local improvement cannot establish aesthetic adequacy.

## Cross-surface coherent diversity

For product-wide high-ambition work, build a workspace visual matrix containing per-screen:
- signature
- dominant geometry
- density
- primary visualization/media
- surface pattern
- typographic gesture
- color mass
- interaction signature

Low coherence is fragmentation; low diversity is template repetition. The target is coherent diversity, not maximal variation.

## Aesthetic excellence vector

NUI v5 does not reduce beauty to one score. High-ambition evidence uses a vector:
- aesthetic fit
- emotional force
- memorability
- material richness
- visual refinement
- signature strength
- perceptual harmony
- role identity fit
- subject specificity

These are review dimensions with evidence/status, not pseudo-precise universal numbers.

## Evaluation architecture

v5 adds four executable/specification layers:

1. `affective-aesthetic` adversarial cases
   - intent loss, visual ambition routing, reference/divergence, legibility, border/material accumulation, visualization semantics, role/magnitude, dual critic, basin escape, cross-surface diversity.

2. `semantic-mutations`
   - mutations such as `DO NOT→ALWAYS`, `must→may`, `preserve→discard`, `independent→self`, `minimum→maximum` must be behaviorally detectable by target cases.

3. `skill-interactions`
   - factorial cases for combinations such as expert+dense+scientific+restrained+anti-card to detect emergent collapse.

4. `craft-distribution`
   - expressive operational, luxury scientific, cinematic professional, playful expert, editorial analytical, tactile creative, organic biotech, monumental command, warm medical, bright high-tech and other styles so NUI learns no hidden “serious UI = restraint” house style.

ATLAS is a named regression case: v4-like evidence that passes code/render health but misses exceptional affective objectives must be BLOCKED by the v5 aesthetic completion gate.

## Depth testing policy

Word count is not accepted as behavioral depth evidence for v5. New v5 tests assert:
- required decisions exist;
- route decisions change under relevant profiles;
- validators reject known failure artifacts;
- semantic mutations are represented and mapped to detecting cases;
- interaction cases exercise multi-skill compositions;
- completion is blocked when high-ambition aesthetic evidence is absent or inadequate.

Historical files may retain prose, but v5 repository quality is not advanced by adding words to satisfy a threshold.

## Completion semantics

`validate_v5_completion_evidence` preserves v4/v3 precedence and adds high-ambition gates.

For `flagship | exceptional | experiential`, completion requires:
- experiential intent PASS;
- visual ambition contract PASS;
- divergence evidence PASS with >=3 candidates when visual freedom is high;
- reference frontier PASS;
- visual legibility PASS;
- aesthetic attractor audit PASS;
- signature depth PASS;
- visual energy evidence PASS/justified;
- aesthetic adequacy PASS;
- basin decision not `RE_DIVERGE`;
- if data visualization is material, encoding provenance PASS;
- if product-wide/multi-screen, perceptual diversity PASS.

Structural CI may verify the v5 framework itself, but it must explicitly bound claims: repository tests do not prove every future generated UI is beautiful. Task-specific high-ambition completion, however, may no longer be marked PASS from compile/render health alone.

## Compatibility

- No third-party UI code is added.
- v1–v4 contracts remain valid and continue to be enforced.
- v5 adds routes only when profiles trigger them.
- Existing accessibility, safety, product truth, data truth and runtime evidence remain higher-priority constraints; aesthetic goals never waive them.
- No new runtime dependency is required for deterministic validators.
