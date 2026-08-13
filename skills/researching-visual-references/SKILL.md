---
name: researching-visual-references
description: Use when a UI needs fresh visual intelligence from contemporary products, design systems, component collections, or art-direction references without copying a fashionable screenshot or default AI aesthetic.
---

# Researching Visual References

## Parent Contract
**Required parent:** `exploring-aesthetic-directions`.

Receive product semantics, emotional target, brand constraints, audience, platform, density, content character, accepted visual-system constraints, and any existing references. This faculty researches mechanisms; the parent still owns which aesthetic direction should be explored.

## Decision Boundary
This skill owns a **provenance-bound visual reference set**. It does not choose final components, license third-party code, or copy a whole visual language. It answers: which contemporary references contain mechanisms relevant to this product, what exactly those mechanisms are, what context makes them successful, and which aspects must not transfer.

A mechanism is a transferable design relationship: asymmetric title-to-content scale, dense neutral surfaces with one saturated semantic accent, motion used to maintain object continuity, border hierarchy instead of card elevation, progressive disclosure through anchored panels, editorial type contrast, spatial grouping through negative space, or a particular rhythm between primary data and metadata. “Make it like Linear” is not a mechanism.

## Product Truth
AI visual generation often converges on a small family of defaults: centered hero, oversized gradient headline, rounded cards, purple/blue glow, glass panels, generic dashboard widgets, uniform hover lift, and decorative motion. Repeating these patterns can satisfy the word “modern” while erasing product character.

Reference research fights this convergence only if it is structured. Blindly collecting beautiful screenshots creates another copying problem. The agent must understand why a reference works, what content and interaction constraints it assumes, and whether the product being designed shares those constraints.

## Decision Model
1. **Translate the design question into mechanisms sought.** Examples: “how can high-density financial data feel calm without hiding information?” or “how can a creative tool make direct manipulation feel tactile without excessive animation?” This is more useful than searching “best dashboard UI.”
2. **Diversify source classes.** Search real products, mature design systems, interaction/component experiments, editorial/brand systems, platform-native examples, and adjacent domains. Avoid deriving the entire direction from one gallery ecosystem.
3. **Record provenance.** For each reference, store canonical URL/source, retrieval date, exact page/screen/component inspected, and whether it is primary product evidence, design-system guidance, community experiment, or inspiration.
4. **Decompose the mechanism.** Examine hierarchy, composition, density, typography, color semantics, surface treatment, iconography, imagery, motion, interaction feedback, information disclosure, and responsiveness. State causal hypotheses rather than adjectives.
5. **Record contextual dependency.** A dramatic low-density landing page mechanism may fail in a data-entry surface. A dark translucent effect may fail in bright-field/mobile accessibility. A kinetic text effect may suit campaign content but harm rapid scanning.
6. **Extract transferable and non-transferable aspects.** Transfer relationships and principles; do not copy brand assets, distinctive trade dress, proprietary illustrations, exact layouts, or code without separate source-selection/license review.
7. **Triangulate.** Prefer a mechanism supported by several independent references or by product reasoning. A single fashionable example remains a hypothesis.
8. **Generate contrast pairs.** Include at least one reference that solves the problem with a different visual strategy. Contrast exposes which mechanism matters and prevents premature convergence.
9. **Bind to hypotheses.** Every candidate aesthetic direction names which reference mechanisms it uses, rejects, or transforms and why.
10. **Set freshness.** High-drift product/reference sources need re-checking before future reuse. Store retrieval time; do not make old screenshots eternal truth.

## Evidence
Evidence can include current official product pages, design-system docs, live component demos, source repositories for open experiments, screenshots captured from real interfaces, and user-supplied references. Search snippets alone are discovery leads, not sufficient evidence for a material mechanism. Inspect the actual source or page when possible.

When code repositories influence the visual idea, keep implementation adoption separate. A React animation repo may demonstrate a useful continuity mechanism even if the final project uses Vue or native mobile; that is `inspire`, not `adopt`. This distinction prevents reference research from smuggling dependencies into the build.

## Output Contract
Return `visual-reference-set` with:
- `design_questions[]`
- `references[] {id, canonical_url, source_class, retrieved_at, inspected, context, mechanisms[], transferable[], non_transferable[], freshness, evidence_refs}`
- `mechanism_clusters[] {mechanism, supporting_reference_ids, product_fit, risks}`
- `contrast_pairs[]`
- `anti-copy_boundaries[]`
- `candidate_links[] {visual_direction_id, mechanism_ids}`
- `unresolved_visual_questions[]`

The set must make it possible for another agent to understand **what was learned**, not merely which links looked attractive.

## Failure Traps
- Searching only UI galleries that reproduce the same current trend.
- Writing adjectives such as premium, sleek, futuristic, clean, or delightful without decomposing observable mechanisms.
- Copying exact composition/branding from a distinctive product.
- Treating an animated component repository as evidence that animation belongs in the product.
- Ignoring content density, language length, accessibility, device, and task frequency of the reference context.
- Using star count or social popularity as design authority.
- Mixing implementation-license approval into visual inspiration without review.
- Keeping references forever in project memory without freshness/expiry.
- Selecting only references that confirm the first aesthetic idea.

**Hard gate:** a reference cannot materially influence the direction unless the agent records the inspected source, extracted mechanism, product-fit rationale, and non-transferable boundary.

## V5 Mandatory Reference Frontier
When there is no established brand, **high visual freedom**, and flagship/exceptional ambition, reference research is not optional. `exceptional` work must construct a **reference frontier** from diverse mechanisms and sources before final selection. Compare the current candidate, internal baseline, at least one alternative direction, and accepted reference mechanisms on the same experiential/craft dimensions. The frontier is a quality/mechanism comparison, never permission to copy trade dress.

## V6 Reference Archaeology Beyond Screenshots
A reference is not deeply understood from one hero screenshot. Perform **interaction-state sampling** on the material mechanism: default, hover/focus, active/selected, loading/error, scrolled, expanded, narrow/wide, reduced-motion, and any domain state that changes its meaning. If the source is a live product, run a **cross-screen reference walk** to see whether the apparent visual language survives navigation, dense work, forms, destructive states, and secondary surfaces or exists only on a marketing-quality showcase.

Build **source-context reconstruction** before transfer: audience expertise, content density, business model, task frequency, platform, brand maturity, data character, likely performance envelope, and accessibility context. A mechanism that works because the source has sparse copy, fixed imagery, or one-screen storytelling cannot be assumed to transfer into an operational product.

Run **blind-reference removal**: hide the source name/logo and judge whether the extracted mechanism remains causally useful for the target product. If the argument collapses to prestige (“Linear does it”, “Apple does it”), the mechanism has not been understood. Maintain a **reference contradiction log** when strong sources solve the same problem differently; contradictions are evidence about context, not noise to average away.

### Falsification
Try the mechanism under the target product's worst content/state and compare against an opposite reference strategy. If the supposed benefit vanishes or depends on copied trade dress, reject the transfer hypothesis.

### Recovery
Reopen reference research with a narrower design question, inspect additional states/source classes, and rebind candidate directions. Do not repair a weak reference thesis by copying more surface details.

## V7 Reference Authority Split
A visual reference has two independent values: **possibility evidence** and **decision authority**. A shader gallery, animated component collection, award site, or experimental canvas can prove that a visual mechanism is feasible and expand aesthetic search. It usually cannot certify focus semantics, platform convention, service workflow, or accessibility behavior. Record the reference's authority role before extracting anything.

For material references, extract mechanism-level observations—composition tension, temporal staging, type/image relationship, depth construction, interaction reveal, data-to-form mapping—then send subject-specific signature work to `designing-domain-native-signatures`. Preserve a trade-dress firewall: do not transfer recognizable copy, palette, illustration, layout arrangement, branded motifs, or distinctive motion sequence when the mechanism can be rebuilt from product truth.

### Falsification
Ask whether the reference would still be useful if all styling were removed and only the underlying mechanism remained. If not, it is aesthetic inspiration only and must stay out of semantic authority.

### Recovery
Downgrade the source role, find stronger behavioral/platform authority for non-visual decisions, and keep the reference solely on the visual frontier.
