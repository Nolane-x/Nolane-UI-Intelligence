# NUI V9 — Product Completeness & Taste Intelligence Closure

NUI V9 closes a different class of failure from V8. V8 substantially strengthened visual synthesis, media choice, reference authority, implementation ecosystem reasoning and anti-generic pressure. V9 addresses the remaining gap where an AI can build a coherent, attractive and internally closed interface while the **product model itself is too small**, or where the final render still contains perceptual/default-platform defects that text-level reasoning misses.

V9 therefore adds two linked planes:

1. **Product-completeness intelligence** — discover broadly before narrowing, explicitly disposition expected capabilities, model settings/account/workspace lifecycles, preserve complete professional tool workspaces, and independently challenge scope adequacy before a “full platform” claim.
2. **Perceptual/runtime craft intelligence** — compare aesthetic candidates instead of self-scoring, critique actual screenshots, use curated mechanism-level references, adapt aesthetics to domain and audience, audit browser/platform residue, enforce design-to-render fidelity, and deepen semantic motion.

The V9 implementation deliberately **preserves the 174 canonical-skill graph**. It does not create near-duplicate faculties merely to increase skill count. New deterministic kernels live in `src/nolane_ui/product_v9.py`, `scope_v9.py`, and `routing_v9.py`; deep V9 protocols are attached to existing canonical owners whose decision boundaries already own the work.

## 1. Broad-before-narrow capability envelope

A common AI failure is premature compression:

`“sales management platform” → Dashboard + Products + Orders + Customers`

The remaining system can then be beautifully designed and perfectly reachable while still omitting settings, account lifecycle, roles, import/export, notifications, reporting, recovery, integrations, audit/history or other capabilities implied by the actual product.

V9 separates **discovery breadth** from **implementation commitment**. `modeling-product-intent` explores a broad capability envelope based on actors, jobs, lifecycle, consequence, product class and ambition. `inventorying-product-capabilities` then assigns explicit dispositions:

- `REQUIRED`
- `EXPECTED`
- `OPTIONAL`
- `EXCLUDED`
- `UNKNOWN`

Discovering a family does not force it into the final UI. An intentionally small tool can exclude enterprise capabilities. The hard rule is that a high-ambition/full-platform claim cannot silently omit or leave material expected families unresolved.

`validate_capability_envelope()` makes that accounting deterministic. `validate_scope_adequacy()` is an independent critic that must challenge the generator with omitted-capability probes and an artificially tiny-but-coherent product model. This closes the loophole where ordinary functional closure verifies only the capabilities the generator happened to think of.

## 2. Settings are architecture, not a leftovers page

V9 deepens `architecting-information` with a settings architecture model. Material settings systems must establish:

- conceptual taxonomy;
- configuration scopes such as device, user, workspace, organization, project/document or policy;
- scope precedence and inheritance;
- effective versus stored value;
- search when scale actually requires it;
- persistence/sync;
- dependencies and validation;
- dangerous/irreversible setting consequence;
- preview where useful;
- reset/recovery at appropriate granularity.

A visually excellent Settings page that mixes MFA, appearance, billing, retention and notification policy in one flat list is not structurally complete. Conversely, V9 does **not** force a settings search box into a five-preference utility.

`validate_settings_architecture()` encodes these minimum contracts.

## 3. Authentication is connected to full account/workspace continuity

`designing-authentication-and-passkeys` remains the authority for sign-in/sign-up, passkeys, MFA, reauthentication, enumeration resistance and secure recovery ceremony. V9 does not blur that boundary. It adds an explicit continuity bridge to the broader account/workspace lifecycle:

- account establishment;
- authenticated session;
- profile/account identity;
- membership/invitation where relevant;
- workspace switching;
- session/device continuity;
- credential/security management;
- recovery;
- sign-out/revocation;
- ownership or membership transition;
- deactivation/deletion.

This prevents “we built login” from being mistaken for “we built accounts.” `validate_account_workspace_lifecycle()` blocks high-level completion when the lifecycle ends at `signed-in`.

## 4. Professional workspace and instrument completeness

V9 deepens both `designing-editor-canvas-workspaces` and `designing-desktop-windowed-workspaces`.

For editors and creative/professional tools, the system inventories **instruments** based on capabilities rather than copying another product’s panel layout. Relevant instruments may include:

- global shell/orientation;
- document/object switching;
- selection;
- modes and tools;
- context toolbar;
- context inspector;
- layers/object hierarchy;
- canvas/timeline/work area;
- asset/resource discovery;
- command/search surface;
- history/undo-redo;
- zoom/navigation;
- status/progress;
- import/export/publish;
- collaboration/version/history;
- help and preferences.

No category is mandatory merely because VS Code, Canva, CapCut or Adobe uses it. Every instrument must trace to a real capability. Completeness is proven by semantic command reachability, not by exposing every control simultaneously.

Desktop professional workspaces additionally model primary/secondary sidebars, secondary panels, status surfaces, command surfaces, density, collapse/detach and persistent user-owned workspace state.

## 5. Interface residue: modernity without anti-native dogma

V9 formalizes the class of defect where a carefully art-directed UI accidentally falls back to browser/OS defaults. The user-visible scrollbar example belongs here, but the audit is deliberately broader:

- scrollbar;
- select;
- file input;
- date/time/number/range controls;
- focus ring;
- text/object selection;
- caret;
- resize handle;
- drag ghost;
- browser validation UI;
- context menu;
- tooltip/popover;
- cursor;
- overscroll.

The rule is **not** “customize everything” or “hide scrollbars.” Native controls are valid when intentional, platform-appropriate and coherent. V9 blocks accidental residue, platform mismatch, or visual cleanup that destroys operability.

`validate_interface_residue_audit()` and the `verifying-design-fidelity` V9 protocol enforce the distinction.

## 6. Comparative taste discrimination

Correctness is not taste. A UI can pass spacing, hierarchy and accessibility rules and still feel generic, cheap-looking, plasticky, overly AI-generated, visually timid, insufficiently premium or insufficiently editorial.

V9 adds a comparative taste contract through `exploring-aesthetic-directions` and `validate_taste_comparison()`:

- compare at least two actual rendered candidates/refinement states;
- judge named dimensions instead of producing one opaque score;
- bind preferences to rendered evidence;
- decompose qualitative judgments into causal visual relations;
- allow `tie` or `re-diverge` when evidence is inconclusive;
- never let taste overrule accessibility, security, product truth, platform fit or functional closure.

Important discriminators include focal authority, negative-space quality, density modulation, typographic character, optical alignment, material restraint, border/elevation calibration, visual rhythm, signature-to-quiet ratio, domain fit, audience fit and perceived production maturity.

“Premium” is not shorthand for dark + thin type + whitespace. “Editorial” is not shorthand for serif display type. “Cheap-looking” is not a personal insult; it must be decomposed into observable causes.

## 7. Screenshot-based design-director court

`critiquing-visual-design` now contains a V9 rendered design-director loop:

`render → capture → inspect → causal critique → repair → re-render → A/B compare`

The court inspects:

- first/second/third focal point;
- compositional hierarchy;
- noise and competing saliency;
- macro and micro visual rhythm;
- dense versus quiet regions;
- actual rendered typography and line breaks;
- spacing breath and optical alignment;
- material consistency;
- default-browser residue;
- mobile/small-screen preservation;
- representative states, not only hero screenshots.

A design spec or component source cannot prove final visual quality. `validate_render_critique()` requires actual render references and evidence-bound observations.

## 8. Curated benchmark memory

`knowledge/v9-design-benchmark-gallery.json` provides a curated reference memory across products and systems such as Stripe, Linear, Notion, Framer, Apple platform guidance, Airbnb, Arc, Vercel, Ramp, Raycast, Visual Studio Code, Canva, CapCut and Adobe Spectrum.

The gallery stores **mechanism lessons**, not screenshots/templates to copy. Each record contains:

- source;
- category;
- mechanisms;
- useful comparison contexts;
- anti-copy boundary;
- refresh policy.

References raise the aesthetic/interaction comparison bar while remaining subordinate to product-local evidence. Current concrete behavior must be re-inspected from first-party sources when it matters because live products drift.

## 9. Domain signatures + audience sensitivity

`knowledge/v9-domain-signatures.json` provides strategic priors for fintech, medtech, developer tools, creative tools, AI products, education, commerce and consumer social/content surfaces.

Each domain describes:

- trust profile;
- density expectation;
- emotional profile;
- interaction tone;
- risk profile;
- multiple audience variants;
- anti-patterns.

The signatures are **not themes**. A fintech consumer app and institutional operations console may need very different density and explanation. `modeling-users-and-tasks` now explicitly models audience decision posture such as `trust-first`, `delight-first`, `speed-first`, `precision-first`, `comprehension-first` or `exploration-first`, then requires real design consequences.

`validate_domain_audience_fit()` ensures both domain and audience axes exist before a high-ambition visual claim is closed.

## 10. Design intelligence → code/render fidelity

`knowledge/v9-render-fidelity.json` and `verifying-design-fidelity` bridge design reasoning to runtime implementation. V9 checks the chain:

`intent → semantic tokens → component constraints → CSS/platform expression → runtime render → visual regression`

The knowledge plane covers typography, line-height, weight, spacing, radii, border opacity, elevation, semantic color, density and motion; component states; overlay/focus behavior; default chrome; responsive transformation; implementation rules; and visual-regression obligations.

`validate_render_fidelity()` requires token, component, responsive, motion, native-control, runtime and visual-regression evidence. A perfect design file does not close implementation quality.

## 11. Motion direction and implementation fidelity

V9 deepens motion in two places.

`designing-motion` asks four product-level questions:

1. what structure does motion teach?
2. what causality does it confirm?
3. what emotional cadence does it contribute?
4. where is intentional absence stronger?

It also formalizes reduced-motion equivalence and a priority hierarchy in which ambient/signature decoration degrades before task feedback, progress and direct manipulation.

`engineering-rich-interactive-components` translates semantic motion into runtime state, interruption, retargeting, reduced-motion and performance behavior. Animation libraries do not own product truth.

## 12. Deterministic routing

V9 routing is enforced in `src/nolane_ui/routing_v9.py` and merged into `mandatory_routes_for_profile()`.

Examples:

- full-platform → product intent + capability inventory + scenario coverage + functional completeness critic;
- material settings → information architecture + capability inventory;
- account/workspace → auth + capability inventory;
- professional editor → editor instruments + keyboard power UX + desktop workspace when applicable;
- exceptional/flagship visual → aesthetic exploration + user/audience model + visual critique + design fidelity;
- material rendered UI → design fidelity + platform conventions;
- rich interaction → motion direction + rich-interaction engineering.

This makes V9 activation executable rather than dependent on whether an agent remembers a prose paragraph.

## 13. Adversarial corpus

`evals/v9-product-completeness-adversarial.json` attacks both false negatives and false positives. It includes under-scoped full platforms, settings/account lifecycle omissions, tool-panel dumping, classic scrollbar/default-control residue, native-control false-positive traps, opaque taste scores, spec-only critique, mobile omission, reference copying, domain/audience stereotypes, token-to-runtime drift, visual-regression noise and semantic/reduced-motion failures.

ALLOW cases are deliberate. V9 must not become a bureaucracy that always asks for more features, always customizes native controls, always chooses more motion, or always rejects simple products.

## 14. Completion semantics

`validate_v9_completion_evidence()` inherits V8 completion gates and adds conditional V9 gates.

A product-wide/full-platform claim requires:

- valid capability envelope;
- independent scope adequacy challenge.

Material settings/account systems require their dedicated contracts. Material rendered UI requires residue audit. Flagship/exceptional/experiential visual claims additionally require:

- V8 flagship visual synthesis;
- V9 comparative taste evidence;
- actual render critique;
- domain/audience fit;
- design-to-render fidelity.

No aggregate beauty score can offset a failed hard gate.

## 15. What V9 does not claim

V9 does **not** prove that every generated UI will be beautiful or complete. Repository CI proves that the reasoning/evidence contracts and adversarial gates exist and are internally consistent. Real product work still needs product truth, real runtime behavior, captures at relevant states/viewports, accessibility/security verification, and—where appropriate—human/user evidence.

V9’s stronger claim is narrower and testable:

> NUI no longer permits an AI to equate the first small feature list with the full product, or to equate a correct design spec with a visually excellent final render, without passing explicit product-scope, comparative-taste, rendered-critique and runtime-fidelity evidence gates.
