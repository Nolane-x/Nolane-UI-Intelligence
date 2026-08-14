# V8 Flagship Visual Synthesis Closure

V8 originally closed an important gap: agents could discover one canonical NUI graph, inspect external skills safely, decide when subject-native media belongs, avoid low-information shape substitution, create or source media with provenance, orchestrate creative tools, and verify assets inside rendered product states. Those capabilities are necessary, but they do not by themselves force a high-ambition interface to resolve into one authored visual world.

This closure adds that missing **cross-owner synthesis contract** without adding duplicate skills to the canonical graph. The graph remains 174 skills. The new artifact is a coordination and falsification layer over existing owners, not a ninth V8 decision owner.

## 1. The unresolved failure mode

A capable agent can satisfy many local craft checks and still ship an interface that feels generated:

- three “directions” are one layout with different accent colors;
- every region becomes a rounded container because containment is easy to synthesize;
- typography is technically legible but has no product voice or optical hierarchy;
- a gradient, orb, glass panel, pseudo-chart or abstract 3D object occupies the most valuable attention slot because the agent has no stronger subject representation;
- color is spread uniformly rather than spent where attention or state needs it;
- motion is applied as a reusable effect instead of preserving causality or spatial continuity;
- desktop looks polished while mobile is only a compressed version of the same geometry;
- a screenshot exists, but nobody records what is wrong with it and proves a correction in a second render;
- the product name and logo can be swapped and the same interface still fits an unrelated SaaS product.

No single inherited owner should absorb all of these decisions. Doing so would recreate the vague “make it beautiful” super-skill NUI was designed to avoid. V8 therefore closes the gap through a **synthesis packet** that requires independent owners to expose compatible decisions and then subjects the combination to anti-generic and rendered-evidence tests.

## 2. What current primary guidance contributes

The closure uses current primary sources only as bounded mechanisms, never as trade dress.

### Apple Human Interface Guidelines

Current Apple guidance places purpose, familiarity, flexibility, simplicity, craft and delight at the foundation of design, and its typography, material and motion guidance repeatedly ties visual treatment to hierarchy, context and purposeful feedback. NUI transfers the mechanism: every visual treatment must earn a role in meaning, hierarchy, place or interaction. It does **not** infer that Apple materials, typography or navigation are appropriate outside Apple-platform contexts.

Primary surfaces reviewed 2026-08-14:

- https://developer.apple.com/design/human-interface-guidelines/design-principles
- https://developer.apple.com/design/human-interface-guidelines/typography
- https://developer.apple.com/design/human-interface-guidelines/materials
- https://developer.apple.com/design/human-interface-guidelines/motion

### Material 3 Expressive / Google Design research

Google's published Material 3 Expressive research is useful because it treats expression as more than decoration. Color, shape, size, motion and containment can steer attention and emotional response; comparative research and eye tracking are used to see whether the intended hierarchy actually helps people find important elements. The same research also documents the failure of expressive layouts that abandon recognizable task structure.

NUI transfers the mechanism: **expression must have a target emotional/functional job, must compete against alternatives, and cannot compensate for broken task clarity**. NUI does not copy Material components, color systems, shape libraries or layout trade dress into unrelated products.

Primary surface reviewed 2026-08-14:

- https://design.google/library/expressive-material-design-google-research

### WCAG 2.2

Accessibility remains an authority boundary rather than an aesthetic preference. Text alternatives, contrast, resize resilience, non-text contrast and applicable motion requirements cannot be traded away because a candidate looks more dramatic.

Primary surface reviewed 2026-08-14:

- https://www.w3.org/TR/WCAG22/

## 3. The synthesis packet

`flagship-visual-synthesis` is required when a task claims `flagship`, `exceptional` or `experiential` visual quality and the project has enough visual freedom to make such a claim meaningful. It does not assign an objective beauty score. It blocks unsupported claims.

The typed schema is `schemas/flagship-visual-synthesis.schema.json`; executable checks live in `src/nolane_ui/flagship.py`; the reusable decision vocabulary lives in `knowledge/flagship-visual-synthesis-v8.json`.

### 3.1 Visual thesis

A thesis is not a style adjective list. It says what the interface is trying to make salient, what emotional/product quality it should embody, and what must recede. A useful thesis predicts choices. “Premium, modern, clean” predicts almost nothing. “A living field notebook: evidence first, salt-air tactility second, controls recede until needed” predicts hierarchy, media, material restraint and composition.

**Falsification:** remove the product nouns. If the thesis still describes thousands of unrelated products, it is not a thesis yet.

### 3.2 Material divergence before convergence

High visual freedom requires at least three candidates that are materially different along **composition, type system, material model and signature mechanism**. Every one of those four axes must exhibit material variation across the candidate set; changing palette, corner radius or hero art while preserving the same skeleton is not divergence.

The point is not to maximize novelty. Divergence is a search instrument that lets the agent compare different ways of expressing the same product truth before local polish makes the first plausible answer emotionally expensive to abandon.

**Falsification:** normalize color and copy across candidates. If their silhouette, typographic behavior, material hierarchy or signature mechanism collapses to one static axis, the search has converged too early for a high-ambition claim.

### 3.3 Attention architecture

Every high-ambition surface declares a ranked attention path. There must be a primary role; subordinate regions must earn lower salience. This avoids the common generated pattern where every card, metric and CTA receives comparable contrast and containment.

Attention can be controlled through scale, whitespace, type contrast, chroma, media, depth, alignment, motion or direct manipulation. The mechanism is chosen by context. NUI does not impose one preferred aesthetic.

**Falsification:** blur or thumbnail the render until small text disappears. If the intended primary and secondary regions cannot still be identified, local detail may be hiding a weak composition.

### 3.4 Typography as a product system

Typography must resolve at least three functional roles and explain measure, optical hierarchy and fallback behavior. Display, reading, utility and numeric roles may share a family; what matters is that their visual responsibilities are deliberate.

The contract rejects both type spectacle with poor reading conditions and “safe sans everywhere” where typography contributes no hierarchy or voice. Variable axes are useful only when their dynamic behavior has a semantic or interaction reason.

**Falsification:** substitute the primary font with the fallback. If wrapping destroys hierarchy or critical labels become ambiguous, the type system was designed around a screenshot instead of a resilient interface.

### 3.5 Composition rhythm

Composition owns spatial relationships, not component inventory. The packet records grid logic, density rhythm, edge behavior and responsive transformation. High-end interfaces often gain character from where the system **breaks** its default grid for a justified focal moment, while routine controls remain stable and predictable.

Density should have rhythm. A surface where every region has equal padding and identical containment has no breathing pattern; a surface where everything is large and open can be equally monotonous.

**Falsification:** draw only the large masses as rectangles. If every product category yields the same dashboard silhouette, return to composition rather than adding decoration.

### 3.6 Color and material causality

The packet records semantic palette, chroma budget, depth model, surface rule and dark-mode behavior. This is deliberately stricter than “choose a palette.”

A chroma budget answers where saturation is allowed to carry attention, status or emotional temperature and where it is withheld. A depth model answers which content is base-plane, which controls truly float, and why. A surface rule prevents glass, blur, shadow or border from becoming universal decoration.

Translucency is not banned. It is justified when preserving context behind a transient foreground layer helps orientation or produces an intended material effect without harming readability or performance. Likewise, flat surfaces are not automatically superior.

**Falsification:** remove shadows/blur and compare hierarchy. If nothing meaningful changes, the material treatment may be cosmetic. In dark mode, verify remapped hierarchy rather than literal palette inversion.

### 3.7 Motion as temporal structure

Motion states its purpose, timing character, gesture relationship and reduced-motion equivalent. The contract distinguishes direct feedback from contextual transitions: frequent micro-actions should not repeatedly tax attention, while a meaningful spatial change may benefit from continuity.

**Falsification:** disable motion. State understanding must remain. Then restore motion and ask whether it teaches relationship, confirms action or carries an intended emotional cadence. If it only makes the interface feel “more premium,” it has no operational job.

### 3.8 Domain-native signature

A signature is a reusable, product-linked mechanism with a restraint rule. It may be typographic, spatial, material, interactive, media-based, data-derived or temporal. It is not a logo in the corner or a one-off hero gimmick.

The signature must explain its subject link: what fact, form, process, environment, artifact, relation or behavior from the domain generated it. It also includes a memory hook: a concise way a user or critic could recognize the experience later.

**Falsification:** move the signature to an unrelated product. If it remains equally appropriate, it is probably a generic motif.

### 3.9 Reference frontier, not reference monoculture

At least three **distinct mechanism-level learnings** are recorded with explicit transfer boundaries. A reference can teach editorial scale, density zoning, motion continuity, data treatment, material layering or another mechanism. Prestige and popularity do not raise authority.

The frontier exists to prevent two opposite errors: designing from memory with no competitive awareness, and visually cloning the first admired reference.

**Falsification:** hide reference names and screenshots, leaving only mechanism notes. The team should still be able to explain the independent product decision.

### 3.10 Generic transfer resistance

For every `flagship`, `exceptional` and `experiential` claim, the packet must report `FAILS_TRANSFER`: if product/domain truth is stripped out, the visual solution should lose important structure or identity rather than revealing a generic shell that could host any SaaS copy.

This is not a demand for novelty everywhere. Familiar controls may and often should remain familiar. The test targets the **authored composition and identity layer**, not basic usability conventions.

### 3.11 Responsive art direction

Rendered evidence includes structural changes, not merely viewport labels. Narrow states may reorder evidence, change navigation modality, alter media crops, collapse persistent utilities into contextual controls, or substitute a representation when the original loses meaning.

`flagship` requires at least two material rendered states. `exceptional` and `experiential` require at least three. All high-ambition packets must represent at least two viewport classes. A loading, theme, long-content or interaction state can provide additional evidence when it materially tests the direction.

**Falsification:** if mobile can be described as “same interface, smaller,” the responsive design has not been authored deeply enough for a high-ambition claim.

### 3.12 Closed critique cycles

At least two critique cycles attack different failure dimensions. Each cycle records a concrete observed finding, a correction and the exact declared rendered-state ID where the correction was re-observed. `verified_in` cannot point to an imaginary or stale render. “Looks good” is not critique, and a defect report with no re-render is unfinished work.

Useful categories include perception, hierarchy, typography, media integration, responsive behavior, motion, accessibility, performance and product specificity. The validator does not prescribe which pair must be used because the highest-risk dimensions differ by product.

## 4. Anti-generic attractors

The repository now names common attractors as **diagnostic hypotheses**, not blanket bans:

1. **Equal-card field** — containment becomes the default answer for every content type.
2. **Decorative data** — fake charts or pseudo-metrics occupy valuable attention without truthful information.
3. **Gradient orb** — a generic luminous object becomes the identity because the product has no subject-native visual grammar.
4. **Radius monoculture** — every control, card, chip, input and media frame shares one fashionable geometry.
5. **Uniform chroma** — color is spread evenly so nothing earns salience.
6. **Cosmetic motion** — hover lift, stagger or spring is repeated without semantic distinction.

Each attractor has legitimate counterexamples. A card can be exactly the right grouping primitive; a data product can be fundamentally geometric; a brand may own a sphere; a playful product may intentionally use round shapes. The audit therefore requires a **replacement mechanism**, not a style prohibition.

## 5. Relationship to the eight V8 owners

The synthesis layer does not absorb their ownership.

- `exporting-nui-to-agent-harnesses` ensures the host exposes the capabilities necessary to observe/render high-ambition work; it does not choose the design.
- `governing-external-agent-skills` prevents borrowed skill prompts from becoming hidden aesthetic authority.
- `mapping-visual-media-opportunities` decides where media has a semantic job inside the attention architecture.
- `sourcing-rights-safe-visual-media` verifies item-level rights and also preserves source/editorial coherence when multiple assets share a surface.
- `authoring-domain-native-visual-assets` turns subject morphology and truth constraints into an asset family that supports the selected direction.
- `orchestrating-creative-toolchains` preserves color, geometry, editability and lineage across production tools and ends in the real runtime.
- `replacing-shape-substitution` attacks low-information high-attention stand-ins and now supplies evidence to the anti-generic audit.
- `validating-visual-asset-integration` verifies crops, overlays, performance and accessible equivalents inside the rendered direction.

The synthesis packet is therefore an **integration proof** across owners, not another source of local rules.

## 6. Release meaning

A passing flagship synthesis packet means:

- the agent did not converge on the first plausible visual answer;
- the selected direction has a concrete product thesis;
- hierarchy, typography, composition, color/material and motion expose explicit mechanisms;
- at least one memorable signature is tied to subject truth;
- references are mechanism-level and bounded against copying;
- the direction resists generic product swapping;
- responsive states are structurally re-authored where necessary;
- rendered critique produced and verified real corrections.

It **does not** mean NUI has mathematically proven beauty. Aesthetic judgment remains partly contextual and human. V8's improvement is that an agent can no longer support a high-ambition claim with style adjectives, a component library, a single screenshot or a self-issued score. The claim must survive evidence that can disagree with it.
