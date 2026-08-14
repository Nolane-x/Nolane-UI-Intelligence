# VÆL — Garden of Stars Design Specification

**Date:** 2026-08-14  
**Status:** Approved concept, implementation-gated specification  
**Evidence class:** `ARTIFACT_WORK`  
**Target:** Responsive flagship web experience, desktop-first  
**Repository location:** `examples/vael-garden-of-stars/`

## 1. Product truth

VÆL is a fictional single-brand luxury fragrance house. The product is not a marketplace and does not imitate an existing perfume brand. Its flagship digital experience must function as both a shoppable fragrance store and an authored digital exhibition.

The selected art direction is **Garden of Stars**: botanical forms imagined as celestial organisms. Fragrance composition drives visual behavior. The site should feel artistic, colorful, alive, mysterious, and highly crafted without sacrificing commerce clarity.

The intended first-use reaction is curiosity before categorization: the interface should initially read as a strange living art object, then reveal itself as a fragrance house through product, copy, scent notes, pricing, and commerce actions.

### Primary user jobs

1. Discover the VÆL brand and understand its artistic point of view.
2. Explore fragrances by mood and sensory character rather than only by conventional faceted filters.
3. Understand a fragrance through top, heart, and base notes.
4. Compare and save fragrances.
5. Add a fragrance to bag and complete a credible purchase flow.
6. Revisit saved or owned fragrances in a personal scent library.

### Non-goals

- No multi-brand marketplace.
- No admin, inventory-management, team, wholesale, or enterprise surfaces.
- No real payment processing or external commerce backend in the flagship example.
- No claim that VÆL or NUI has a one-million-dollar market valuation.
- No imitation of recognizable brand trade dress.

## 2. NUI route and high-ambition obligations

This task is `flagship` / `experiential` UI work and follows the NUI lifecycle from product truth through rendered criticism and bounded verification.

### Activated design owners

- `modeling-product-intent`
- `modeling-users-and-tasks`
- `architecting-information`
- `designing-task-flows`
- `designing-interactions`
- `modeling-component-semantics`
- `modeling-component-states`
- `designing-navigation`
- `designing-search`
- `exploring-aesthetic-directions`
- `directing-visual-hierarchy`
- `composing-layouts`
- `crafting-typography`
- `crafting-color`
- `crafting-spacing-and-rhythm`
- `crafting-depth-and-surfaces`
- `directing-iconography-and-imagery`
- `preventing-generic-ui`
- `architecting-design-tokens`
- `architecting-component-systems`
- `adapting-responsive-layouts`
- `designing-accessible-interfaces`
- `writing-interface-copy`
- `designing-motion`
- `designing-empty-loading-error-states`
- `designing-commerce-checkout`
- `mapping-visual-media-opportunities`
- `authoring-domain-native-visual-assets`
- `compiling-ui-implementation-specifications`

### Verification owners

- `challenging-ui-designs`
- `critiquing-visual-design`
- `critiquing-user-experience`
- `critiquing-accessibility`
- `critiquing-design-system`
- `critiquing-responsive-behavior`
- `critiquing-functional-completeness`
- `verifying-runtime-ui-behavior`
- `validating-rendered-perception`
- `validating-visual-asset-integration`
- `binding-ui-evidence`
- `gating-ui-completion`

### Flagship-specific gates

Before bounded release, the implementation must preserve:

1. Three materially different visual directions in the design record: Garden of Stars, Chromatic Alchemy, and Cosmic Herbarium.
2. Garden of Stars as the selected thesis, not a bland average of the three.
3. A product-native signature mechanism: **Living Scent Bloom**.
4. Structural desktop/mobile recomposition rather than shrink-only responsiveness.
5. A quiet system around signature moments.
6. At least two concrete critique → correction → re-observation loops on named renders.
7. A generic-transfer test: removing logo/name should not leave a shell that could represent an unrelated SaaS or generic store without meaningful loss.

## 3. Selected visual thesis — Garden of Stars

### Semantic source

The visual system draws from:

- flower anatomy and botanical specimens;
- pollen, filaments, petals, stems, spores, resin, mist, dew, mineral crystals;
- constellations, orbital motion, nebulae, eclipse light, star fields, deep-space darkness;
- perfumery rituals: extraction, layering, evaporation, diffusion, concentration, trace.

These sources are translated into original digital mechanisms rather than literal stock illustrations.

### Emotional target

- poetic;
- mysterious;
- sensorial;
- luxurious through precision rather than ornament accumulation;
- colorful and alive;
- slightly uncanny;
- calm enough that commerce remains trustworthy.

### Signature-to-quiet ratio

Only the following surfaces may reach full spectacle:

- Home hero;
- Scent Universe;
- Fragrance detail journey;
- selected collection transitions.

Navigation, price/size controls, bag, checkout, account utilities, form validation, and purchase confirmation remain quieter and highly legible.

## 4. Brand system

### Name and mark

The brand is **VÆL**. The `Æ` is the visual anchor of the wordmark. The implementation uses text first; any custom mark created later must remain an original VÆL asset.

### Voice

Editorial copy is short, image-rich, and sensorial. Utility copy is direct and conventional. The site must never hide price, quantity, size, shipping state, validation, or purchase consequences behind poetic language.

Example editorial vocabulary:

- bloom;
- trace;
- orbit;
- dusk;
- mineral;
- luminous;
- resin;
- ether;
- garden;
- specimen.

Do not overuse pseudo-scientific labels. Microcopy such as `SPECIMEN 04` is decorative hierarchy, never a substitute for actual product names or required information.

## 5. Fragrance catalogue

The flagship example ships with six fictional fragrances. Each has a distinct visual DNA so the interface proves that scent data changes the system rather than only changing text.

### ASTER I

- Mood: Ethereal
- Top: ozone, bergamot
- Heart: black iris, violet leaf
- Base: white musk, silver cedar
- Character: cool, translucent, radial
- Palette family: violet / celestial blue / silver

### SOLARA

- Mood: Solar
- Top: blood orange, pink pepper
- Heart: saffron flower, heliotrope
- Base: amber, sandalwood
- Character: warm, expansive, radiant
- Palette family: coral / molten amber / pale gold

### NYMPHAEA

- Mood: Aquatic
- Top: rain accord, shiso
- Heart: water lily, jasmine vapor
- Base: mineral musk, driftwood
- Character: floating, fluid, reflective
- Palette family: cyan / opal / jade

### VESPER

- Mood: Nocturnal
- Top: plum skin, incense smoke
- Heart: night rose, clove
- Base: oud, labdanum
- Character: dense, inward, slow
- Palette family: wine / crimson / ember

### VERDANT IX

- Mood: Wild
- Top: crushed basil, grapefruit
- Heart: fern, moss, galbanum
- Base: vetiver, wet bark
- Character: branching, irregular, fibrous
- Palette family: moss / acid green / deep teal

### ORIEL

- Mood: Sacred
- Top: pear skin, aldehydes
- Heart: magnolia, osmanthus
- Base: ambrette, pale woods
- Character: luminous, symmetrical, soft
- Palette family: blush / pearl / pollen gold

## 6. Information architecture

### Global navigation

Desktop:

- VÆL wordmark / home
- Discover
- Scent Universe
- Atelier
- Search
- Saved
- Bag

Mobile:

- wordmark;
- compact menu trigger;
- search;
- bag;
- context-dependent bottom action only when it materially shortens purchase or discovery flow.

No persistent mega-navigation or generic dashboard shell.

### Routes

- `/` — flagship home
- `/discover` — mood-led fragrance discovery
- `/universe` — spatial fragrance constellation
- `/fragrance/:slug` — fragrance detail journey
- `/atelier` — brand story and collection craft
- `/saved` — saved fragrances
- `/bag` — bag review
- `/checkout` — simulated checkout
- `/account` — scent library and purchase history fixture
- `/search` — full search results; search can also open as an overlay from global navigation

## 7. Home — The Garden Awakens

The home route is an authored sequence, not a stack of generic marketing cards.

### Sequence

1. **Awakening hero** — VÆL wordmark, one hero fragrance, one Living Scent Bloom, minimal navigation, short line of copy, clear `Enter the garden` / `Discover scents` path.
2. **Six living specimens** — a non-uniform composition introducing the catalogue without a standard six-card grid.
3. **Scent thesis** — oversized editorial typography with a restrained botanical/celestial visual interruption.
4. **Mood portals** — Ethereal, Solar, Aquatic, Nocturnal, Wild, Sacred.
5. **Featured journey** — one fragrance preview that demonstrates top → heart → base transformation.
6. **Atelier fragment** — concise material/process story.
7. **Footer** — conventional access to shipping, returns, privacy, contact fixture, accessibility preference, and legal placeholder text clearly labeled as demo content.

## 8. Discover — Find Your Scent

Mood is the primary exploration model.

### Primary mood controls

- Ethereal
- Solar
- Aquatic
- Nocturnal
- Wild
- Sacred

Selecting a mood changes:

- background field;
- active bloom morphology;
- accent material;
- suggested fragrances;
- editorial descriptor.

It does not change interaction semantics or hide results.

### Secondary filters

A restrained utility panel can filter by:

- Floral
- Woody
- Amber
- Mineral
- Fresh
- Smoky
- Light / medium / deep intensity

Filters must support clear reset and visible selected states beyond hue alone.

## 9. Scent Universe

The Scent Universe is a domain-native spatial discovery surface.

### Desktop behavior

Each fragrance is an orbital point with its own bloom silhouette. Spatial proximity reflects similarity across mood and accord, but the visualization is curated rather than pretending to be scientific analytics.

Hover/focus:

- enlarges the selected fragrance identity;
- reveals name, mood, three principal notes, and price;
- visually traces its relationship to nearby scents;
- offers a clear detail action.

Keyboard navigation must provide an ordered, non-spatial route through all fragrances.

### Mobile behavior

Do not shrink the constellation. Replace it with an orbital ribbon / stacked radial journey with swipe and buttons. The same six products and relationships remain reachable.

## 10. Fragrance detail — Enter the Fragrance

The product page is a three-act scroll journey with a stable product identity.

### Act 1 — The Opening

- bottle / vessel visual;
- product name;
- concentration and volume;
- price;
- top notes;
- primary purchase action available without completing the entire cinematic scroll.

### Act 2 — The Bloom

- heart notes;
- Living Scent Bloom reaches maximum botanical expression;
- interactive ingredient labels illuminate corresponding bloom regions;
- short editorial copy.

### Act 3 — The Trace

- base notes;
- atmosphere becomes quieter and denser;
- longevity / character copy is qualitative, not fabricated scientific measurement;
- size selector;
- Add to Bag;
- Save;
- shipping / returns fixture;
- related scents based on catalogue-defined similarity.

### Product truth rules

Price and size remain persistent or quickly recoverable. Motion must never delay Add to Bag. Product state must survive interrupted animations.

## 11. Living Scent Bloom

Living Scent Bloom is the signature mechanism and must be implemented as an original domain-native visual asset system.

### Input model

Each fragrance defines:

- palette stops;
- petal count range;
- radial symmetry;
- branch factor;
- translucency;
- particle density;
- particle velocity;
- turbulence;
- glow intensity;
- bloom openness;
- motion cadence;
- visual mass.

### Mapping principles

- Fresh / top-note energy increases fine particles and faster peripheral motion.
- Floral heart increases petal/body expression.
- Woody/resinous base increases visual mass and slower inward movement.
- Ethereal increases translucency and negative space.
- Nocturnal increases density and low-frequency movement.
- Solar increases radial expansion and warm luminance.

The bloom must not become a decorative randomizer. Given the same fragrance seed and state, morphology remains recognizably stable.

### Technology constraint

Prefer original SVG, Canvas 2D, CSS, and Web Animations API behavior over adopting a third-party visual language. Any later adoption of a material external animation/3D library requires its own NUI ecosystem/provenance review.

## 12. Typography

Typography has two voices.

### Editorial voice

Used for:

- hero statements;
- fragrance names;
- section titles;
- sparse quotations / brand statements.

Character:

- high contrast;
- fashion-editorial proportion;
- expressive but not illegible;
- large optical hierarchy;
- allowed to overlap visual media only when text contrast remains deterministic.

### Functional voice

Used for:

- navigation;
- controls;
- price;
- size;
- filters;
- forms;
- shipping/returns;
- account state.

Character:

- clear grotesk / sans-serif;
- strong small-size legibility;
- stable numerals;
- quiet relative to editorial text.

### Minimums

Required information must not render below 11 CSS px. Control and body defaults target 14–18 px depending on viewport. Display scale is fluid and may exceed 140 px on large desktop where composition supports it.

## 13. Color and material system

VÆL has no single permanent accent. The brand owns a chromatic ecosystem.

### Stable neutral foundation

- midnight ink / blue-black canvas;
- cool bone / opal text;
- muted silver utility text;
- subtle mineral dividers.

### Fragrance chroma

Strong chroma belongs to scent worlds, bloom assets, selected states, and focal moments. Utility surfaces do not reuse saturated fragrance colors indiscriminately.

### Material roles

1. **Ink** — deep negative-space canvas.
2. **Crystal** — rare translucent/refractive detail around bottle and overlays.
3. **Bloom** — organic botanical morphology.
4. **Mist** — atmospheric depth and transition.
5. **Light** — fragrance-specific chroma and state emphasis.

Glass/blur is not the default component style. Rounded rectangles are used only where grouping, touch target, or form semantics require them.

## 14. Motion system

The motion thesis is **the garden breathes**.

### Priority order

1. Critical information / state feedback
2. Task feedback
3. Orientation / spatial continuity
4. Signature motion
5. Celebration
6. Ambient motion

Performance degradation removes effects from the bottom upward.

### Signature transitions

- Bloom awakening: closed/resting → active morphology.
- Fragrance change: old bloom disperses into pollen/mist → new bloom reforms.
- Product continuity: product identity remains visually anchored from listing to detail.
- Ingredient focus: a named note illuminates the relevant bloom region.
- Add to Bag: restrained causal trace from product toward bag state; no confetti.

### Reduced motion

`prefers-reduced-motion` removes continuous ambient drift, large spatial travel, parallax, and morphing. It preserves state through instant composition changes, crossfade, persistent labels, selection outlines, and text updates.

## 15. Component system

Core reusable units:

- `GlobalNav`
- `MobileMenu`
- `VaeWordmark`
- `LivingScentBloom`
- `FragranceVessel`
- `FragranceIdentity`
- `MoodPortal`
- `ScentSpecimen`
- `ScentNote`
- `ScentNoteTriptych`
- `ScentUniverse`
- `UniverseNode`
- `FragranceJourney`
- `PriceSizeBlock`
- `QuantityControl`
- `AddToBagButton`
- `SaveButton`
- `BagDrawer`
- `CheckoutForm`
- `ScentLibrary`
- `SearchOverlay`
- `AccessibilityMotionPreference`

Components expose semantic state rather than owning hidden animation truth. Product state must remain valid when animation is disabled or interrupted.

## 16. Commerce flow

### Add to Bag

- choose size;
- quantity defaults to one;
- Add to Bag updates a persistent bag count;
- bag drawer or route shows product, size, quantity, unit price, subtotal;
- remove and quantity changes are reversible in the local demo state.

### Checkout

This is a non-payment simulation but should demonstrate credible UX:

1. Contact
2. Delivery address
3. Shipping method fixture
4. Payment fixture clearly labeled as demo
5. Order review
6. Simulated confirmation

Validation is inline and textual; errors are not color-only. No real card details are transmitted or stored.

## 17. Account / Scent Library

Account is a local fixture used to demonstrate post-purchase experience.

It contains:

- Saved fragrances;
- Owned fragrances;
- recent simulated orders;
- personal constellation summary derived only from catalogue labels, not pseudo-personality claims.

No authentication backend is required for this example; therefore account recovery/session/device management is intentionally excluded from the implementation claim.

## 18. Responsive strategy

### Desktop

- asymmetric cinematic compositions;
- large negative space;
- blooms can exceed viewport bounds;
- editorial text may become a compositional object;
- spatial Scent Universe.

### Tablet

- preserve asymmetric hierarchy but reduce simultaneous visual layers;
- collapse utility controls before reducing required text size;
- preserve scent progression and product action reachability.

### Mobile

- vertical scent journey;
- reduced simultaneous particle count;
- orbital ribbon instead of wide spatial constellation;
- sticky purchase action only where it does not cover required content;
- navigation and controls use familiar mobile affordances;
- hero spectacle is cropped/recomposed, not simply scaled down.

Target evidence viewports:

- 1440 × 1000 desktop
- 1024 × 768 tablet/compact desktop
- 390 × 844 mobile
- 360 × 800 narrow mobile

## 19. Accessibility obligations

- Semantic landmarks and heading order.
- Full keyboard reachability for nav, discover, universe alternatives, product actions, bag, checkout, and saved state.
- Visible focus treatment that is not removed for aesthetics.
- Text and control contrast validated against actual local backgrounds.
- Selection and errors never communicated by color alone.
- All continuous animation respects reduced-motion preference.
- Decorative blooms are hidden from assistive technology unless they communicate state; stateful equivalents receive text.
- Product imagery / vessel visuals receive concise alt text when meaningful.
- Form fields use labels, descriptions, and accessible error linkage.
- 200% text scaling must not hide purchase-critical information.

## 20. Performance obligations

The site should feel rich without making the direct interaction path dependent on high-end GPU effects.

- Use transform/opacity/composited effects where possible.
- Keep ambient particle counts adaptive by viewport and reduced-motion state.
- Pause or reduce offscreen animation.
- Avoid layout-thrashing scroll handlers.
- Content and purchase actions render before noncritical ambience finishes.
- The app remains functionally usable if Canvas/SVG animation is unavailable.

## 21. State and failure behavior

Required states:

- loading / first render;
- no search results;
- empty saved list;
- empty bag;
- invalid checkout field;
- simulated checkout processing;
- simulated checkout success;
- simulated checkout failure with retry;
- animation unavailable / reduced motion.

No state may show an endless decorative loader without explaining what is happening.

## 22. Anti-generic constraints

The implementation must reject the following patterns unless a specific semantic need justifies them:

- uniform bento grids;
- identical rounded cards everywhere;
- purple/blue generic AI gradients;
- glowing borders as the main premium device;
- icon-plus-heading repeated in every section;
- generic `Learn more →` calls to action;
- all cards lifting by the same hover transform;
- excessive glassmorphism;
- template-like SaaS navigation;
- stock perfume bottle photography used as the main identity mechanism.

The shell should still look product-native after blinding the VÆL name.

## 23. Implementation architecture

The example is a self-contained responsive web app under `examples/vael-garden-of-stars/`.

Preferred implementation:

- React
- TypeScript
- Vite
- CSS custom properties / modern CSS
- SVG and Canvas 2D for authored visual systems
- native Web Animations API / CSS transitions for motion
- local fixture data for fragrances, bag, saved state, and checkout simulation

Avoid adopting a component framework whose default visual language becomes visible in the product.

### Suggested source boundaries

- `src/app/` — routing, app shell, global state boundaries
- `src/catalog/` — fragrance data and scent-DNA model
- `src/components/` — semantic reusable UI
- `src/bloom/` — deterministic Living Scent Bloom rendering and motion
- `src/features/discover/` — mood/filter exploration
- `src/features/universe/` — spatial and mobile scent universe
- `src/features/fragrance/` — detail journey
- `src/features/commerce/` — bag and checkout simulation
- `src/features/library/` — saved/owned scent library
- `src/styles/` — tokens, typography, layout, motion, responsive rules
- `tests/` — unit/component/e2e and accessibility checks
- `evidence/` — named renders and critique records used by NUI release gates

## 24. Testing and evidence strategy

### Deterministic tests

- scent DNA maps to stable bloom parameters;
- mood filters return correct catalogue subsets;
- Add to Bag / quantity / remove state transitions;
- checkout validation and simulated success/failure;
- reduced-motion branch changes motion behavior without changing required information;
- keyboard-reachable alternatives for Scent Universe.

### Runtime verification

Capture named states at the four target viewports for:

- home hero;
- discover with selected mood;
- Scent Universe;
- ASTER I detail opening;
- ASTER I bloom act;
- mobile fragrance detail;
- bag;
- checkout validation;
- reduced-motion variant.

Check:

- browser errors;
- overflow;
- focus visibility;
- text clipping;
- interactive reachability;
- resolved font behavior;
- bloom integration / crop;
- state continuity.

### Critique loops

Two loops are required before the product can make a bounded flagship completion claim.

**Loop A — visual/taste:** compare rendered hierarchy, negative space, typography, material restraint, signature-to-quiet ratio, and generic-transfer resistance. Record one or more causal findings, repair them, and capture a named after-render.

**Loop B — responsive/UX/accessibility:** inspect mobile recomposition, keyboard flow, reduced motion, purchase-action reachability, and form/error behavior. Record findings, repair them, and capture a named after-render.

Generator self-review is correlated evidence. Completion language must identify that limitation unless a genuinely independent critic is available.

## 25. Definition of bounded completion

The VÆL example may be described as a completed flagship **artifact** only when:

- all required routes are implemented;
- catalogue/discovery/product/bag/checkout/library flows are reachable;
- Living Scent Bloom is product-data-driven and visibly distinct across fragrances;
- desktop and mobile are structurally recomposed;
- automated tests pass;
- production build succeeds;
- target viewport renders are captured;
- no known browser-console blocker remains;
- no critical overflow/focus/contrast/purchase-flow blocker remains;
- two critique/correction/re-observation loops are recorded;
- remaining unknowns and evidence limitations are explicitly listed.

This completion state proves facts about the VÆL artifact only. It does not prove that NUI caused better output relative to a baseline, and it does not support a market-valuation claim.
