# NUI v6 — Deep Research & Design Synthesis Intelligence

## Status
Design approved by the user's explicit instruction to autonomously deepen NUI, make source research mandatory, broaden current UI-industry coverage, eliminate shallow/repetitive skill growth, and continue implementation without waiting for further direction.

## Problem
NUI v5 correctly introduced affective and aesthetic enforcement, but the repository still contains three structural failure modes:

1. **Depth asymmetry.** The strongest ecosystem skills are ~1k words and contain operational detail, while many core UI, critic, and v5 aesthetic owners are far thinner. A concept can exist in the graph without supplying enough decision procedure to reliably change an agent's behavior.
2. **Shallow source proof.** `ui-ecosystem-registry.json` records source, role, license posture, drift, and coarse provenance, but a material source can still be treated as researched after README/license/implementation-level inspection. The repository does not yet prove that the agent inspected the source artifacts that actually determine the mechanism it plans to use.
3. **Coverage claims are too coarse.** The historical industry atlas is strong for surfaces/modalities/AI/risk/temporal/social routing but is not a complete ontology of contemporary UI craft and implementation ecosystems. Important source classes—icon systems, typography/font infrastructure, design-token tooling, CSS/style systems, visual-testing tooling, geospatial UI, node/diagram UI, code editors, creative rendering, Lottie/Rive-style animation assets, TUI systems, and AI-native component systems—are not first-class source-intelligence categories.

The goal of v6 is not to inflate skill count. The goal is to make a smaller number of new mechanisms enforce **research depth, synthesis quality, and causal evidence**, while substantially deepening existing skills that already own the correct decisions.

## Design Principles

### 1. Depth is behavioral, not textual
NUI must never use word/token count as a release criterion. A deep skill must instead expose a decision topology that can be falsified: inputs, observations, branching conditions, counterfactuals, evidence, failure topology, escalation, output semantics, and downstream verification. Prose length can be reported diagnostically, never used as proof.

### 2. Source links are discovery, not research
A URL in the registry is only an index entry. Material influence requires a `ui-source-research-dossier` tied to a specific repository snapshot/ref and to inspected source artifacts. README-only material influence must fail.

### 3. Read obligations depend on source role
A motion engine, design system, icon corpus, chart library, component gallery, editor, canvas SDK, or design-token tool has different authoritative surfaces. The research planner must derive required artifact classes from the source role instead of imposing one generic checklist.

### 4. Mechanism extraction precedes adoption
The agent must identify the transferable mechanism and evidence first. Then it selects `adopt|adapt|inspire|build|reject`. This prevents dependency choice from becoming the design decision.

### 5. Cross-source synthesis must prevent collage
Exceptional UI often benefits from several sources: semantic primitive, motion mechanism, icon system, chart engine, typography reference, or visual experiment. NUI must require a synthesis contract showing which source owns which layer, where local product semantics override upstream defaults, and how the final system remains one coherent visual/interaction language.

### 6. Industry coverage is a basis, not a combinatorial product
The v6 ontology adds independent axes and source domains, then tests pairwise/high-risk interactions. It does not claim to enumerate every cross-product combination of every UI context.

### 7. Research can reopen
Source snapshots, licenses, APIs, component inventories, standards, and design systems drift. Any high-drift source or changed upstream ref reopens material research.

## Architecture

### A. Deep Source Intelligence Plane
Create `src/nolane_ui/source_intelligence.py` with deterministic functions:

- `required_artifact_classes(source_role, usage, visual_ambition, risk_class)`
- `plan_source_research(source, task_profile, usage)`
- `validate_source_research_dossier(dossier, source=None)`
- `validate_source_mix(record)`
- `validate_cross_source_synthesis(record)`

A dossier records repository identity/ref/commit, inspected artifacts with exact paths or canonical documents, why each artifact was inspected, findings, extracted mechanisms, contradictions, integration hazards, license/accessibility/performance evidence, unread material, and stop reason.

Material `adopt|adapt` requires implementation-level evidence plus role-specific evidence. Material visual `inspire` may not require reusable code inspection, but it still requires actual component/example/demo or equivalent mechanism-bearing evidence rather than README-only discovery.

### B. Role-Specific Archaeology Rules
The planner maps roles to artifact classes. Examples:

- animated component gallery → component source + demo/example + dependency/config + motion/reduced-motion behavior + license
- headless primitive/design system → implementation + interaction/a11y docs + tests/examples + tokens/themes where applicable + license
- motion engine → core API/docs + examples + interruption/gesture/layout behavior + reduced-motion/performance guidance + license
- chart/visualization → encoding API + examples + accessibility/interaction + scale/data semantics + performance + license
- icon system → source/catalog + grid/stroke/weight conventions + naming/tags + framework delivery + icon-specific license implications
- typography/font source → font files/catalog metadata + script coverage + variable axes/weights + license + delivery/subsetting guidance
- editor/canvas/code editor → core model + interaction examples + keyboard/focus + plugin/extension boundary + performance/virtualization + license
- design-token/style tool → token schema/transform pipeline + theme examples + generated outputs + migration/versioning + license
- creative renderer/3D/shader → renderer API + examples + device/performance constraints + input/accessibility fallback + license

### C. v6 Source Ecosystem Registry
Preserve v4 registry compatibility while creating `knowledge/ui-source-intelligence-v6.json`. It contains:

- source identity and role
- source tier: `anchor|specialist|discovery`
- source domains/capabilities/stacks
- drift and live-verification requirement
- license posture
- `research_map` with recommended paths/doc classes to inspect
- `mechanism_families`
- known anti-patterns and local adaptation boundaries
- provenance snapshot for deeply inspected anchor sources

The registry expands beyond the existing 52 sources into missing current UI ecosystem classes. Sources not deeply verified are explicitly `discovery` and cannot be silently treated as anchor evidence.

### D. UI Industry Ontology v6
Create `knowledge/ui-industry-ontology-v6.json` with axes covering:

- surfaces/platforms
- input modalities
- product/interface archetypes
- information/data character
- interaction mechanics
- visual-media systems
- aesthetic/art-direction regimes
- design-system maturity
- accessibility/inclusive contexts
- localization/script conditions
- temporal/network behavior
- collaboration/social topology
- AI agency
- trust/risk
- implementation ecosystem

Each axis value owns: decision owner(s), verifier(s), evidence classes, and source domains. Add interaction cells for combinations with known emergent risk rather than the full Cartesian product.

### E. Skill Depth Constitution v6
Create `knowledge/skill-depth-constitution-v6.json` and validator rules. Every material skill is audited for the presence of behavior-bearing dimensions appropriate to its family, such as:

- owned decision/failure class
- required inputs and inherited obligations
- observation protocol
- decision branches/tradeoffs
- counterfactual or falsification step
- evidence requirements
- output artifact semantics
- failure topology
- escalation/recovery
- downstream verification/handoff

The constitution does **not** demand identical headings. It explicitly rejects a single repeated template as proof of depth.

### F. Bespoke Deepening Wave
Rewrite all 13 v5 aesthetic skills individually. Each gets a domain-specific decision procedure, not appended boilerplate. Also deepen the thinnest high-leverage legacy owners/critics involved in visual quality and closure, including responsive critique, platform critique, design-system critique, UX critique, accessibility critique, visual-design critique, typography, layout, and iconography/media direction where necessary.

### G. Four New Decision Owners
Only four new skills are added because they own genuinely new decisions:

1. `performing-ui-repository-archaeology` → owns source-depth plan and file/doc inspection evidence.
2. `synthesizing-cross-source-ui-language` → owns coherent multi-source synthesis and foreign-system conflict resolution before implementation.
3. `auditing-ui-research-depth` → independent critic for whether source research was actually sufficient for the claimed influence.
4. `benchmarking-ui-skill-effect` → owns causal/ablation evaluation of whether a skill changes decisions or catches failures rather than merely existing in prose.

### H. Behavioral and Adversarial Evaluation
Create v6 eval planes covering:

- README-only source research must fail
- stale/unpinned high-drift material source must fail
- gallery-only source monoculture must fail for exceptional design unless justified
- source-role mismatch must fail
- external demo semantics transplanted without reconciliation must fail
- cross-source collage with incompatible token/motion/semantic languages must fail
- source mechanism with unsupported accessibility/performance assumptions must fail
- deep skill mutation/ablation cases must change evaluator outcome
- industry ontology gaps and unowned interaction cells must fail repository validation

### I. CLI / CI
Add scripts:

- `scripts/nui-source-plan`
- `scripts/nui-source-audit`
- `scripts/nui-depth-audit`

Upgrade `nui-validate` and release packet to v6. CI runs full tests, v6 repository gate, and packages the complete v6 project artifact plus completion packet.

## Completion Boundaries
v6 can prove structural depth contracts, source-research sufficiency rules, registry/ontology coverage, deterministic routing/gating, and eval integrity. It still cannot honestly prove that every future generated UI is objectively beautiful. A future runtime benchmark with actual model generations/screenshots and independent judges remains a separate empirical layer; v6 adds the causal benchmark contract needed for that layer rather than pretending static CI is the benchmark itself.
