# UI Industry 1000 — Batch 005 Research-First Inventory

Baseline: 674 canonical skills. Target: exactly 100 new canonical owners after admission review.

This inventory is an admission lock, not a prose-generation template. Every `SKILL.md` must be authored independently. If semantic review invalidates a candidate, the candidate is removed and any replacement must be independently researched and admitted; cosmetic rename/backfill is prohibited.

## Court A — Mobile-native application shell and lifecycle — 10

1. `designing-mobile-native-application-shells`
2. `designing-native-navigation-stacks`
3. `designing-tab-bar-state-continuity`
4. `designing-mobile-safe-area-integration`
5. `designing-virtual-keyboard-avoidance`
6. `designing-mobile-deep-link-routing`
7. `designing-app-lifecycle-state-restoration`
8. `designing-native-share-sheet-intents`
9. `designing-mobile-app-switcher-privacy`
10. `designing-mobile-gesture-navigation-conflicts`

## Court B — Visual application builders — 12

1. `designing-visual-application-builders`
2. `designing-canvas-hierarchy-synchronization`
3. `designing-responsive-breakpoint-authoring`
4. `designing-style-inheritance-inspection`
5. `designing-component-instance-overrides`
6. `designing-builder-component-authoring`
7. `designing-builder-slot-insertion`
8. `designing-builder-data-binding`
9. `designing-builder-conditional-visibility`
10. `designing-builder-interaction-wiring`
11. `designing-builder-preview-publish-modes`
12. `designing-builder-layout-constraint-editing`

## Court C — Business-intelligence workspaces — 12

1. `designing-business-intelligence-workspaces`
2. `designing-semantic-metric-browsing`
3. `designing-query-provenance-inspection`
4. `designing-dashboard-edit-view-modes`
5. `designing-dashboard-filter-scope`
6. `designing-drill-path-continuity`
7. `designing-data-freshness-communication`
8. `designing-metric-definition-comparison`
9. `designing-alert-to-analysis-handoffs`
10. `designing-saved-analysis-workspaces`
11. `designing-dashboard-permission-boundaries`
12. `designing-data-lineage-exploration`

## Court D — Clinical-care workflows — 14

1. `designing-clinical-care-workflows`
2. `designing-patient-identity-banners`
3. `designing-clinical-encounter-context`
4. `designing-medication-order-entry`
5. `designing-medication-reconciliation`
6. `designing-lab-result-review`
7. `designing-clinical-result-abnormality`
8. `designing-clinical-order-status`
9. `designing-problem-list-management`
10. `designing-clinical-note-signing`
11. `designing-clinical-handoff-summaries`
12. `designing-radiology-study-navigation`
13. `designing-medical-image-measurements`
14. `designing-clinical-alert-fatigue-controls`

## Court E — Public-service experiences — 10

1. `designing-public-service-experiences`
2. `designing-service-eligibility-checkers`
3. `designing-government-application-journeys`
4. `designing-service-evidence-upload`
5. `designing-save-and-return-service-flows`
6. `designing-assisted-digital-handoffs`
7. `designing-public-service-status-tracking`
8. `designing-identity-proofing-service-flows`
9. `designing-benefit-entitlement-explanations`
10. `designing-public-service-change-reporting`

## Court F — Marketplace operations — 10

1. `designing-marketplace-operations`
2. `designing-seller-onboarding`
3. `designing-listing-moderation-workflows`
4. `designing-marketplace-inventory-availability`
5. `designing-order-exception-management`
6. `designing-split-fulfillment-shipments`
7. `designing-marketplace-dispute-resolution`
8. `designing-marketplace-payout-status`
9. `designing-buyer-seller-messaging-boundaries`
10. `designing-marketplace-trust-signals`

## Court G — Realtime communications — 10

1. `designing-realtime-communication-systems`
2. `designing-room-channel-membership`
3. `designing-message-sync-gap-recovery`
4. `designing-offline-message-reconciliation`
5. `designing-end-to-end-encryption-state`
6. `designing-key-verification-flows`
7. `designing-call-join-device-checks`
8. `designing-call-participant-layouts`
9. `designing-screen-share-control`
10. `designing-moderation-action-surfaces`

## Court H — Spatial/XR specialists — 10

These route under the existing `designing-spatial-xr-interfaces` owner; Batch 005 does not create a competing XR root.

1. `designing-ray-pointer-interaction`
2. `designing-gaze-targeting`
3. `designing-hand-direct-manipulation`
4. `designing-world-space-panel-placement`
5. `designing-spatial-ui-distance-scaling`
6. `designing-occlusion-aware-interface-placement`
7. `designing-spatial-anchor-persistence`
8. `designing-xr-locomotion-controls`
9. `designing-xr-safety-boundaries`
10. `designing-xr-dom-overlay-coordination`

## Court I — Recommendation and personalization — 6

1. `designing-recommendation-personalization-surfaces`
2. `designing-recommendation-explanations`
3. `designing-personalization-controls`
4. `designing-ranking-feedback-loops`
5. `designing-cold-start-preference-capture`
6. `designing-recommendation-diversity-controls`

## Court J — Design-to-code handoff — 6

1. `designing-design-to-code-handoffs`
2. `designing-component-mapping-to-code`
3. `designing-token-mapping-to-code`
4. `designing-responsive-intent-handoff`
5. `designing-interaction-specification-handoff`
6. `designing-design-code-drift-review`

## Count lock

```text
mobile-native       10
visual-builder      12
business-intel      12
clinical            14
public-service      10
marketplace         10
realtime            10
xr-specialist       10
personalization      6
design-to-code       6
----------------------
total               100
```

## Immediate rejected overlaps

- `designing-spatial-xr-interfaces` was rejected as a new candidate because it already exists in the 674-node graph; it is reused only as an authoritative parent.
- `designing-mobile-haptic-feedback` was rejected because generic haptics/multisensory feedback already has a canonical owner; the batch does not create a mobile noun-variant of that decision.

Further rejections discovered during prose authoring must be recorded in the Batch 005 provenance ledger.
