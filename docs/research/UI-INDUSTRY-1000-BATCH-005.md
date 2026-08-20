# UI Industry 1000 — Batch 005 Research, Provenance, and Ownership Ledger

## Status and scope

Batch 005 starts from the **674-node canonical graph** on `main` at `00d00252f74fb4fc77b97337591190933d1cc223` and admits exactly **100 additional decision owners**, producing a 774-node target graph. The number 100 is an acceptance count, not an authorization to manufacture weak siblings. Candidates that collapsed into an existing owner were rejected and replaced only after a separate decision/failure boundary was established.

This record is provenance and ownership evidence. It is **not a prose-generation template**. No external repository text, demo composition, brand styling, or trade dress was copied into canonical skills. External systems are used only to expose mechanisms, state models, failure classes, domain vocabulary, and implementation constraints that can be independently synthesized under NUI's authority hierarchy.

Canonical `SKILL.md` prose for this batch was authored independently. Deterministic automation was limited to graph registration, count bookkeeping, tests, duplicate detection, and provenance indexing. It did not generate or rewrite canonical skill bodies.

## Source-role rules

A source can hold different authority on different decisions. Batch 005 uses these roles:

- **Normative / public-authority guidance** — may constrain service/accessibility/platform obligations within its applicable jurisdiction or standard scope; it does not become universal visual authority.
- **Mature system evidence** — demonstrates that a decision class recurs in a maintained production ecosystem; it does not prove that the same implementation is right for NUI users.
- **Mechanism implementation evidence** — exposes concrete state, lifecycle, routing, synchronization, or authoring mechanisms; code details are not universal law.
- **Domain evidence** — demonstrates domain-specific entities, risks, and workflow states; it does not transfer branding or local policy.
- **Discovery/corroboration** — helps identify a frontier or confirm that a mechanism appears in more than one ecosystem; it cannot by itself authorize material adoption.

Every material transfer still requires local product truth, applicable standards, platform guidance, and rendered/runtime verification. Repository popularity, star count, or an attractive demo is never treated as authority.

## Snapshot matrix

Snapshots are pinned so that later research can distinguish what was actually inspected from a moving `main` branch.

| Court | Primary snapshot | Secondary snapshot | Role / mechanism boundary |
|---|---|---|---|
| Mobile native | `react-navigation/react-navigation@73f8c2982a8999f1e1dfb1cfbeae9d8dab0c1cc2` | `expo/expo@5a97a546476fd0bea35227b60297ad472f065168` | Navigation/lifecycle/platform mechanism evidence; not art direction. |
| Visual builders | `penpot/penpot@f29a94058af9b6b66309d430e7c822b1e1996052` | `webstudio-is/webstudio@626b5e741bf6fad87a96e2fc352396721b0193d4` | Canvas/model/editor and authored-fragment mechanism evidence; no product trade dress transfer. |
| BI / analytics | `apache/superset@e7dccd44a7c212739147155548e689e9d6b3408f` | `grafana/grafana@a693ff4dc37be00c8abde3a69b6ac407fdc88bf9` | Query/dashboard/alert investigation evidence; neither source certifies analytical truth. |
| Clinical | `openmrs/openmrs-esm-patient-chart@224fd87d09711df2140cc1b101c8de023447dba0` | `OHIF/Viewers@6155c587988e351cdbbf4b7261a30f8eba95d083` | Clinical context and medical-imaging workflow evidence; safety/regulatory authority remains external and jurisdiction-specific. |
| Public service | `alphagov/govuk-frontend@26679248834fd3cae37dfeb494e6f0c765fcc86e` | `uswds/uswds@75a01d1114076274b9628826971562c9d494af20` | Mature public-service design evidence; local law, eligibility policy, identity rules, and accessibility obligations remain authoritative. |
| Marketplace | `medusajs/medusa@1a9fe477d265e8861ca68ef9a445b40d006b28ca` | `saleor/saleor-dashboard@852663206b2e8552c5eaf405e1a7614af74a3b86` | Commerce operations/domain mechanism evidence; not a universal marketplace policy. |
| Realtime communications | `element-hq/element-web@d0d5df51e5c8e8bf242d0b02107e166b9d82af52` | `mattermost/mattermost@bcc9ce5e4afc6c63aa9cc4166f09d998cb22e873` | Room/channel, sync, call, moderation and encrypted-state evidence; cryptographic claims require protocol authority. |
| Spatial / XR | `pmndrs/xr@8d2fda1ac27acb8959bd8055b8b3a1a7dcfb0611` | `BabylonJS/Babylon.js@4dd2f0692286e8b2439683d2cca91bd62f654f34` | XR interaction/spatial runtime mechanism evidence; platform safety and hardware guidance remain authoritative. |
| Recommendation / personalization | `discourse/discourse@7f60c555b2ba2aed167c675dea3a644be2c2ce88` | `mastodon/mastodon@60593f6a8de11effdcf0a0dcb40e22115ae9361a` | Feed/community preference and user-control corroboration; ranking truth and fairness need local measurement. |
| Design-to-code | `storybookjs/storybook@2c9c87e59adbb23bb56ca4f6cf055f536ecea54a` | `tokens-studio/figma-plugin@246098691ff74cc638d8749fed8ac2f146b75e45` plus the Penpot snapshot above | Component/token/design-representation evidence; implementation authority remains project-specific. |

## Admission court: rejected overlaps

The following candidates were explicitly rejected rather than cosmetically renamed:

- `designing-spatial-xr-interfaces` already exists in the 674-node graph and remains the XR parent. Batch 005 does not create a competing root.
- `designing-mobile-haptic-feedback` collapsed into existing `designing-haptics-and-multisensory-feedback`; mobile naming did not create new ownership.
- `designing-gaze-targeting` and `designing-hand-direct-manipulation` collapsed into existing `designing-gaze-hand-spatial-input`; they were replaced by XR near/far transition and origin-recovery decisions with distinct failure models.
- Dashboard-wide filter scope is kept separate from existing chart-mediated `designing-cross-filtering`.
- Analytical drill-context continuity is kept separate from the mechanics of existing `designing-dashboard-drilldown`.
- Service evidence meaning and case binding are kept separate from transfer mechanics in existing `designing-file-uploaders`.
- Public-service case status is kept separate from commerce shipment/order tracking.
- Recommendation-profile controls are kept separate from UI theme personalization in existing `managing-theming-and-personalization`.
- Design-to-code mapping owners translate between representations; they do not duplicate token, component-system, responsive, interaction, or fidelity owners.

---

# Court A — Mobile-native application shell and lifecycle

**Authority boundary:** React Navigation and Expo demonstrate navigation/platform mechanisms. Apple/Android platform behavior, app policy, privacy, and accessibility guidance outrank repository implementation choices. This court owns mobile application continuity where generic responsive-web or device-integration owners are insufficient.

1. `designing-mobile-native-application-shells` — owns the native app shell as a lifecycle/navigation/safe-area/system-surface coordination boundary; excludes ordinary responsive composition and individual device APIs.
2. `designing-native-navigation-stacks` — owns push/pop/replace/back stack identity, restoration, destructive route exits, and destination continuity; excludes global IA and web-history design.
3. `designing-tab-bar-state-continuity` — owns independent tab histories, reselection behavior, preserved scroll/task context, and tab reset semantics; excludes generic tab-component visuals.
4. `designing-mobile-safe-area-integration` — owns content/system-bar/inset negotiation under cutouts, gesture areas, keyboards and transient chrome; excludes generic spacing tokens.
5. `designing-virtual-keyboard-avoidance` — owns focus-visible geometry, pan/resize/scroll strategy, composer anchoring, and keyboard transition recovery; excludes text-input semantics themselves.
6. `designing-mobile-deep-link-routing` — owns external URI/notification/universal-link resolution into authenticated/restored app state, including invalid or stale destinations; excludes generic URL routing.
7. `designing-app-lifecycle-state-restoration` — owns foreground/background/process-death restoration, persisted-vs-authoritative state reconciliation, and privacy-sensitive restoration boundaries; excludes generic offline caching.
8. `designing-native-share-sheet-intents` — owns inbound/outbound share intent payload scope, preview, cancellation, target capability and failed handoff recovery; excludes custom sharing-dialog design.
9. `designing-mobile-app-switcher-privacy` — owns snapshot redaction and task-switcher exposure policy for sensitive visible state while preserving return continuity; excludes full authentication/session policy.
10. `designing-mobile-gesture-navigation-conflicts` — owns arbitration between OS edge/back/home gestures and app gestures, cancellation, precedence and alternate access; excludes generic drag physics.

# Court B — Visual application builders

**Authority boundary:** Penpot and Webstudio expose editor/model mechanisms. They do not authorize copying their panels, canvas treatment, terminology, shortcuts, or design language. Existing `designing-editor-canvas-workspaces` remains the broad workspace owner.

1. `designing-visual-application-builders` — owns the visual-builder contract connecting authored artifact, canvas, hierarchy, property model, preview and publish state; excludes generic editor chrome.
2. `designing-canvas-hierarchy-synchronization` — owns bidirectional identity/selection/order synchronization between canvas objects and structural trees; excludes tree-view component mechanics in isolation.
3. `designing-responsive-breakpoint-authoring` — owns how creators author inherited/overridden behavior across responsive conditions and see where a value originates; excludes runtime responsive layout policy.
4. `designing-style-inheritance-inspection` — owns provenance of effective style through tokens, classes, ancestors, breakpoint overrides and local declarations; excludes token-system governance itself.
5. `designing-component-instance-overrides` — owns instance-vs-definition identity, permitted overrides, reset/rebase, detach consequences and update conflict visibility; excludes generic component API evolution.
6. `designing-builder-component-authoring` — owns promoting authored structures into reusable builder components with stable props/slots/defaults and migration behavior; excludes production-code component architecture.
7. `designing-builder-slot-insertion` — owns valid insertion points, child constraints, empty-slot discoverability, reorder/reparent semantics and invalid drop feedback; excludes generic drag-and-drop.
8. `designing-builder-data-binding` — owns binding UI properties to runtime data expressions, missing data, type mismatch, preview values and source provenance; excludes general database/query design.
9. `designing-builder-conditional-visibility` — owns authoring conditional presence without losing editability, discoverability or state reasoning; excludes ordinary hide/show component state.
10. `designing-builder-interaction-wiring` — owns authoring event→action→target chains, parameter binding, side effects, broken references and preview execution boundaries; excludes the domain behavior of those actions.
11. `designing-builder-preview-publish-modes` — owns edit/preview/staged/published authority, unsaved change visibility and divergence between authoring runtime and released artifact; excludes generic content publishing.
12. `designing-builder-layout-constraint-editing` — owns creator-facing layout constraint intent, parent dependence, contradiction diagnosis and responsive consequence; excludes raw resize handles and generic CSS teaching.

# Court C — Business-intelligence workspaces

**Authority boundary:** Superset and Grafana show maintained query/dashboard/alert patterns. Data semantics, metric truth, freshness, authorization and operational policy must be validated against the local data platform; visual chart libraries cannot certify them.

1. `designing-business-intelligence-workspaces` — owns the BI workspace contract across datasets/metrics, filters, queries, dashboards, saved analysis and semantic context; excludes generic chart styling.
2. `designing-semantic-metric-browsing` — owns discovery of governed metrics/dimensions with definition, grain, owner, units and compatibility context; excludes visual encoding.
3. `designing-query-provenance-inspection` — owns traceability from visible result back through query, filters, dataset/model, parameters and execution context; excludes query-builder interaction itself.
4. `designing-dashboard-edit-view-modes` — owns authoring-vs-consumption authority, dirty state, preview, publish and reader-safe interaction boundaries; excludes generic builder mode switching.
5. `designing-dashboard-filter-scope` — owns where a dashboard filter applies, exclusions, inheritance, default/URL/session scope and visible effective state; existing cross-filtering owns chart-mediated propagation mechanics.
6. `designing-drill-path-continuity` — owns preservation of entity/filter/time/metric context and provenance while moving from aggregate to detail or across analysis surfaces; existing drilldown owns the triggering interaction.
7. `designing-data-freshness-communication` — owns timestamp, ingestion/query lag, partial freshness, stale warning and refresh authority without equating render time with data time.
8. `designing-metric-definition-comparison` — owns side-by-side semantic comparison when similarly named metrics differ by formula, grain, filters, currency, timezone or owner; excludes chart comparison aesthetics.
9. `designing-alert-to-analysis-handoffs` — owns transfer from an alert instance into a bounded investigative context with time window, labels, query, state and provenance; excludes alert-rule authoring.
10. `designing-saved-analysis-workspaces` — owns persistence/restoration of an analytical working set—queries, filters, layout, selections and revision identity—without silently turning ephemeral state into canonical truth.
11. `designing-dashboard-permission-boundaries` — owns visible read/edit/share/data-access effects and partial-denial behavior at dashboard scope; generic RBAC remains the policy owner.
12. `designing-data-lineage-exploration` — owns navigable upstream/downstream dependency and transformation context for analytical artifacts, with scope and confidence; excludes generic dependency-graph rendering.

# Court D — Clinical-care workflows

**Authority boundary:** OpenMRS and OHIF provide domain/mechanism evidence only. Clinical safety, terminology, prescribing, imaging, privacy, retention, and regulatory decisions require applicable medical authority and local governance. The OpenMRS snapshot itself demonstrates that patient-banner state can be clinically meaningful and requires contrast/accessibility verification; this is evidence of a failure class, not a visual style to copy.

1. `designing-clinical-care-workflows` — owns clinical context integrity across patient, encounter, orders, results, notes, handoff and imaging; generic high-stakes UX remains a parent obligation.
2. `designing-patient-identity-banners` — owns persistent patient identity and high-risk qualifiers sufficient to prevent wrong-patient action, including duplicate/similar identity and sensitive-status handling; excludes generic profile headers.
3. `designing-clinical-encounter-context` — owns current encounter/episode/location/provider/time context and safe transitions between them; excludes general navigation breadcrumbs.
4. `designing-medication-order-entry` — owns medication selection, dose/route/frequency/timing/indication, interaction with formulary/safety checks, review and signing states; excludes generic forms.
5. `designing-medication-reconciliation` — owns comparison and disposition of prior/current medication lists with source, uncertainty, continue/stop/change decisions and unresolved discrepancies.
6. `designing-lab-result-review` — owns result grouping, specimen/time/reference context, trend and acknowledgment/review workflow; excludes generic table browsing.
7. `designing-clinical-result-abnormality` — owns clinically significant abnormal/critical state communication with magnitude, direction, reference, trend and acknowledgment; generic color/status encoding is only a presentation obligation.
8. `designing-clinical-order-status` — owns requested/accepted/in-progress/resulted/cancelled/failed/held order lifecycle and actionable exceptions; excludes generic task status.
9. `designing-problem-list-management` — owns active/resolved/historical/duplicate/uncertain clinical problem state, provenance and reconciliation; excludes generic tag management.
10. `designing-clinical-note-signing` — owns draft/authored/attested/signed/amended state, authorship, lock/late-entry consequences and safe correction; excludes ordinary content publishing.
11. `designing-clinical-handoff-summaries` — owns transfer of patient context, active concerns, pending work, contingency and responsibility across clinicians/teams; excludes generic collaboration handoff.
12. `designing-radiology-study-navigation` — owns patient→study→series→instance/view context, comparison/prior orientation and hanging/navigation continuity; excludes generic media browsing.
13. `designing-medical-image-measurements` — owns measurement identity, units, image/frame/plane binding, edit provenance, calibration assumptions and report relationship; excludes generic CAD measurement tools.
14. `designing-clinical-alert-fatigue-controls` — owns prioritization, interruptiveness, suppression/snooze/escalation evidence and override accountability for repeated clinical alerts; excludes generic notification-center design.

# Court E — Public-service experiences

**Authority boundary:** GOV.UK Frontend and USWDS are mature public-sector systems, but service law, eligibility, evidence, identity, language, accessibility and assisted-digital obligations remain jurisdiction- and program-specific. Their visual treatment is never copied as trade dress.

1. `designing-public-service-experiences` — owns service-level continuity from eligibility through application, evidence, identity, status, change reporting and assisted routes; excludes generic marketing/government branding.
2. `designing-service-eligibility-checkers` — owns transparent rules-based eligibility exploration, uncertainty, evidence assumptions, ineligible outcomes and route-to-help; excludes final legal adjudication unless the system truly performs it.
3. `designing-government-application-journeys` — owns multi-session public application progress, declarations, dependencies, review, submission receipt and non-digital alternatives; generic multi-step forms remain implementation support.
4. `designing-service-evidence-upload` — owns evidence requirement meaning, claimant/case binding, accepted document semantics, privacy, receipt and missing/invalid evidence state; file uploader owns transfer mechanics only.
5. `designing-save-and-return-service-flows` — owns resumable service state across authentication/re-entry/expiry, what was saved, missing data, deadlines and safe recovery; excludes generic form drafts.
6. `designing-assisted-digital-handoffs` — owns continuity when a user moves between self-service, phone, in-person, proxy or support channels, including consent and case-context transfer.
7. `designing-public-service-status-tracking` — owns administrative case/application state, agency actions, evidence requests, deadlines and next user action; it is not commerce shipment tracking.
8. `designing-identity-proofing-service-flows` — owns service-specific identity proofing levels, evidence attempts, alternative routes, lockout/recovery and what the verified identity authorizes; authentication mechanics remain separate.
9. `designing-benefit-entitlement-explanations` — owns explanation of entitlement amount/period/basis/change and uncertainty with traceable rule/evidence context; excludes generic pricing or account balances.
10. `designing-public-service-change-reporting` — owns reporting material life/circumstance changes against an existing case, effective dates, evidence, downstream consequences and confirmation.

# Court F — Marketplace operations

**Authority boundary:** Medusa and Saleor expose commerce-domain mechanisms. Marketplace rules, consumer law, tax, payments, moderation, payout, KYC and liability are local authorities. Existing checkout/cart/product owners remain responsible for ordinary buyer commerce.

1. `designing-marketplace-operations` — owns multi-party marketplace state across seller, listing, inventory, order, fulfillment, dispute, payout and trust; excludes single-merchant storefront mechanics.
2. `designing-seller-onboarding` — owns seller eligibility/readiness, business/payout/compliance state, progressive activation and blocked-capability explanation; excludes generic account onboarding.
3. `designing-listing-moderation-workflows` — owns submitted/flagged/reviewed/rejected/appealed listing state, policy evidence, reviewer decisions and seller remediation; excludes generic content moderation UI.
4. `designing-marketplace-inventory-availability` — owns availability when stock, reservations, seller location, offer state and fulfillment capability differ by seller/variant; excludes simple product quantity display.
5. `designing-order-exception-management` — owns operational exception diagnosis and resolution when a marketplace order diverges from the normal lifecycle across buyer/seller/platform actors.
6. `designing-split-fulfillment-shipments` — owns one order decomposed across sellers/locations/packages with independent fulfillment state and coherent buyer/operator rollup.
7. `designing-marketplace-dispute-resolution` — owns claim, evidence, response, mediation/escalation, decision, appeal and financial consequence across multiple parties; excludes ordinary refund flow.
8. `designing-marketplace-payout-status` — owns seller-facing earned/pending/held/failed/paid payout state, deductions, settlement grouping and remediation; excludes buyer payment status.
9. `designing-buyer-seller-messaging-boundaries` — owns transaction-context messaging, privacy/contact boundaries, moderation/escalation and safe off-platform constraints; generic chat mechanics remain elsewhere.
10. `designing-marketplace-trust-signals` — owns evidence-backed seller/listing/transaction trust signals, freshness, scope and explanation without conflating badges with guaranteed safety.

# Court G — Realtime communications

**Authority boundary:** Element and Mattermost expose room/channel, synchronization, call and moderation mechanisms. Cryptographic/security claims require protocol and implementation evidence; this court must not claim security merely because an interface displays a lock icon.

1. `designing-realtime-communication-systems` — owns realtime conversation continuity across room identity, synchronization, encryption state, call state, moderation and degraded recovery; generic chat remains a child mechanism.
2. `designing-room-channel-membership` — owns joined/invited/knocked/left/banned/restricted membership, role changes, visibility and local-vs-server authority; excludes generic organization membership.
3. `designing-message-sync-gap-recovery` — owns detection and repair of missing timeline segments, discontinuity markers, pagination/sync-token failure and user-visible uncertainty; excludes ordinary loading states.
4. `designing-offline-message-reconciliation` — owns locally composed/sent messages reconnecting with server order, IDs, duplicates, edits, failures and retry without lying about delivery.
5. `designing-end-to-end-encryption-state` — owns visible encryption eligibility/state, unverified or unavailable conditions, history/key gaps and claim bounds; cryptography/protocol correctness is external authority.
6. `designing-key-verification-flows` — owns human/device verification state, comparison channel, mismatches, resets and post-verification consequences; excludes generic two-factor enrollment.
7. `designing-call-join-device-checks` — owns prejoin permission/device/media selection, preview, unavailable hardware, join intent and fallback before entering a realtime call.
8. `designing-call-participant-layouts` — owns participant/presenter/pinned/active-speaker/screen-share layout continuity under changing participant counts and limited viewport; excludes generic grids.
9. `designing-screen-share-control` — owns choosing source, disclosure scope, active-share visibility, pause/stop, permission/failure and accidental-sensitive-content risk; excludes generic external-display handoff.
10. `designing-moderation-action-surfaces` — owns realtime-context moderation actions with target, scope, duration, evidence, reversibility and permission visibility; policy remains external.

# Court H — Spatial / XR specialists

**Authority boundary:** Existing `designing-spatial-xr-interfaces` remains the parent. pmndrs/xr and Babylon.js provide runtime/interaction mechanism evidence. Hardware-platform safety guidance, comfort limits and accessibility authority outrank these libraries. Existing `designing-gaze-hand-spatial-input` retains gaze/hand modality ownership.

1. `designing-ray-pointer-interaction` — owns far-pointer ray acquisition, hover/target feedback, occlusion/depth ambiguity, selection and cancellation for XR pointers; excludes gaze/hand modality fundamentals.
2. `designing-xr-near-far-interaction-transitions` — owns continuity as one task switches between direct/near and ray/far interaction, including target handoff, capture, affordance change and accidental double activation.
3. `designing-xr-recenter-and-origin-recovery` — owns recovery when tracking origin, recenter, room alignment or user orientation changes and world-relative UI would otherwise become unreachable or misleading.
4. `designing-world-space-panel-placement` — owns authored/runtime placement of panels relative to user, object or world with reachability, visibility and task relationship; excludes generic 3D scene hierarchy.
5. `designing-spatial-ui-distance-scaling` — owns angular/readability/target-size behavior as interface distance changes, including near/far thresholds and non-linear scale decisions; excludes ordinary responsive breakpoints.
6. `designing-occlusion-aware-interface-placement` — owns when physical/virtual geometry hides critical UI, including depth testing, repositioning, edge indicators and intentional occlusion; excludes generic z-index.
7. `designing-spatial-anchor-persistence` — owns anchor identity and confidence across sessions/map updates/relocalization, drift, missing anchors and safe fallback; excludes generic saved layout persistence.
8. `designing-xr-locomotion-controls` — owns teleport/smooth/turn movement control, destination validity, orientation, interruption and comfort alternatives; excludes gamepad focus navigation.
9. `designing-xr-safety-boundaries` — owns communication and response to guardian/play-area/physical-boundary proximity without implying the UI itself certifies environmental safety.
10. `designing-xr-dom-overlay-coordination` — owns authority, focus, layering and input handoff between immersive content and DOM/system overlays, including session transitions and accessibility/fallback implications.

# Court I — Recommendation and personalization

**Authority boundary:** Discourse and Mastodon provide community/feed mechanism evidence, not ranking authority. Ranking quality, fairness, safety, consent, profiling law, and recommendation effectiveness require local empirical evidence and applicable policy. UI theme personalization remains outside this court.

1. `designing-recommendation-personalization-surfaces` — owns the user-visible contract around ranked/personalized content: what is inferred, what can change it, where uncertainty exists and how non-personalized alternatives behave.
2. `designing-recommendation-explanations` — owns bounded reason/explanation presentation tied to actual ranking signals without fabricated causal stories or false precision.
3. `designing-personalization-controls` — owns durable controls over recommendation profile/signals, reset/tune/disable consequences and effective state; excludes visual theme preferences.
4. `designing-ranking-feedback-loops` — owns explicit/implicit feedback capture, immediate effect expectations, reversibility, accidental signals and the visible transition from action to later ranking behavior.
5. `designing-cold-start-preference-capture` — owns sparse-evidence preference seeding, skip baseline, omission-as-unknown semantics, provisional commitment and transition into learned ranking; excludes generic onboarding.
6. `designing-recommendation-diversity-controls` — owns user-visible breadth/exploration controls and the tension between relevance, repetition, novelty and coverage without promising algorithmic fairness from a UI toggle.

# Court J — Design-to-code handoff

**Authority boundary:** Storybook, Tokens Studio and Penpot demonstrate component/token/design representations and documentation mechanics. The project design system, production APIs, accessibility semantics, runtime constraints and actual rendered product remain authoritative for implementation. No design-tool tree is assumed to map one-to-one to production code.

1. `designing-design-to-code-handoffs` — owns the cross-representation handoff envelope binding design revision, components, tokens, responsive intent, behavior, accessibility, assets, exceptions and implementation evidence.
2. `designing-component-mapping-to-code` — owns semantic design-component ↔ production-component identity, variant/prop/slot/composition mapping and unsupported override decisions; production component architecture remains authoritative.
3. `designing-token-mapping-to-code` — owns design-token identity/alias/mode translation into production token systems, unresolved raw values and semantic mismatch; token architecture itself remains with `architecting-design-tokens`.
4. `designing-responsive-intent-handoff` — owns translation of authored responsive conditions, reflow/reorder/visibility/priority intent and breakpoint assumptions into implementable constraints; runtime responsive design remains with its existing owners.
5. `designing-interaction-specification-handoff` — owns behavior/state/event/focus/keyboard/gesture/async/recovery specification across the design→implementation boundary; domain interaction owners still define correct behavior.
6. `designing-design-code-drift-review` — owns revision-bound comparison after design and production evolve independently, classifying intentional exceptions, stale side, regressions and authority by dimension; fidelity tools provide evidence but do not decide authority alone.

---

## Cross-court anti-overlap assertions

Batch 005 was reviewed against existing graph owners, not merely against other Batch 005 names. The intended ownership tests are:

- Removing the mobile court would leave native lifecycle/navigation continuity failures unowned even though responsive/device owners remain.
- Removing the builder court would leave authoring-model provenance and canvas↔model synchronization failures unowned even though editor/canvas primitives remain.
- Removing the BI court would leave semantic metric/query/freshness/lineage context failures unowned even though charts and dense interfaces remain.
- Removing the clinical court would leave patient/encounter/order/result/imaging safety-context failures unowned even though generic high-stakes and medical-safety parents remain.
- Removing the public-service court would leave service eligibility/evidence/assisted-digital/case-state continuity unowned even though forms/authentication exist.
- Removing the marketplace court would leave multi-party seller/listing/fulfillment/dispute/payout state unowned even though checkout and commerce lifecycle owners exist.
- Removing the realtime court would leave room membership, sync gaps, encryption-state communication and call-control continuity unowned even though chat/collaboration exists.
- Removing XR specialists would leave spatial persistence/placement/recovery/locomotion failure classes unowned while the existing XR root remains intentionally broad.
- Removing personalization specialists would leave ranking explanation/profile/feedback/cold-start/diversity control unowned while theme personalization remains intact.
- Removing design-to-code specialists would leave cross-representation mapping and drift authority unresolved even though design-system and fidelity owners remain.

A future semantic review that falsifies any of these statements should merge/remove the weaker owner rather than preserve it for count stability.

## Verification obligations

Admission and source provenance are necessary but not sufficient. Completion requires all of the following on the exact Batch 005 revision:

1. exactly 100 Batch 005 slugs and exactly 774 graph nodes;
2. frontmatter/parent/family/output metadata matching the acceptance lock;
3. parent reachability to `using-nolane-ui` with no cycle;
4. no Batch 005 output collision with the pre-existing graph;
5. every canonical body independently substantive, with no exact normalized duplicate, trivial rename pair, or mass-reused substantive paragraph;
6. complete repository unit/contract tests;
7. `nui-validate` and exact-revision completion packet validation;
8. no one-shot integration workflow/finalizer left in the product tree;
9. GitHub Actions green on the exact PR head before merge.

Until those gates pass, this ledger records research/admission evidence only and does **not** declare Batch 005 complete.
