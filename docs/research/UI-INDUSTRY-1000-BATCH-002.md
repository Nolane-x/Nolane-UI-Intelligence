# UI Industry 1000 — Batch 002 Provenance and Ownership Record

## Scope

Batch 002 adds exactly 100 canonical specialist faculties to the Batch 001 baseline, expanding `skills/skill-graph.json` from **274 to 374 nodes**. The historical 174-skill V6/V8 baseline and all 100 Batch 001 specialists remain unchanged in identity and ownership.

This record is an authorship, routing, and structural-evidence ledger. It does **not** claim that adding 100 skills empirically improves model output. NUI V10's empirical claim ceiling remains governed by its real-model evidence protocol.

## Authorship constraint

The 100 `SKILL.md` bodies in this batch were authored **individually**. No loop, template generator, macro expander, bulk prose transformation, cloned body, or programmatic prompt-to-skill generator produced the prose. Standard repository structure such as frontmatter and headings is shared, but each body owns a different decision boundary, failure topology, falsification court, and output contract.

A temporary deterministic bookkeeping script contained a literal 100-node metadata map solely to update `skills/skill-graph.json`. It did not create, transform, or touch any `SKILL.md`. That script and its temporary workflow were deleted after the graph commit, so no one-time integration tooling remains in the final branch.

## Exact inventory and canonical ownership

| # | Skill | Parent | Output |
|---:|---|---|---|
| 1 | `designing-field-validation-and-error-recovery` | `designing-forms` | `field-validation-recovery-contract` |
| 2 | `designing-dependent-form-fields` | `designing-forms` | `dependent-field-state-contract` |
| 3 | `designing-multi-step-forms` | `designing-forms` | `multi-step-form-contract` |
| 4 | `designing-form-autosave-and-drafts` | `designing-forms` | `form-draft-persistence-contract` |
| 5 | `designing-address-entry` | `designing-forms` | `address-entry-contract` |
| 6 | `designing-phone-number-entry` | `designing-forms` | `phone-entry-contract` |
| 7 | `designing-one-time-code-entry` | `designing-authentication-and-passkeys` | `one-time-code-entry-contract` |
| 8 | `designing-password-creation-and-strength` | `designing-authentication-and-passkeys` | `password-creation-contract` |
| 9 | `designing-monetary-input` | `designing-forms` | `monetary-input-contract` |
| 10 | `designing-measurement-and-unit-input` | `designing-forms` | `measurement-input-contract` |
| 11 | `designing-global-navigation-shells` | `designing-navigation` | `global-navigation-shell-contract` |
| 12 | `designing-sidebar-navigation` | `designing-navigation` | `sidebar-navigation-contract` |
| 13 | `designing-breadcrumb-navigation` | `designing-navigation` | `breadcrumb-navigation-contract` |
| 14 | `designing-mega-navigation` | `designing-navigation` | `mega-navigation-contract` |
| 15 | `designing-pagination` | `designing-navigation` | `pagination-contract` |
| 16 | `designing-infinite-scroll-browsing` | `designing-navigation` | `infinite-scroll-browsing-contract` |
| 17 | `designing-search-result-interfaces` | `designing-search` | `search-result-interface-contract` |
| 18 | `designing-faceted-search` | `designing-search` | `faceted-search-contract` |
| 19 | `designing-saved-searches-and-views` | `designing-search` | `saved-search-view-contract` |
| 20 | `designing-recent-items-navigation` | `designing-navigation` | `recent-items-navigation-contract` |
| 21 | `designing-toast-feedback` | `designing-notifications-and-interruptions` | `toast-feedback-contract` |
| 22 | `designing-inline-status-feedback` | `designing-notifications-and-interruptions` | `inline-status-feedback-contract` |
| 23 | `designing-persistent-banner-alerts` | `designing-notifications-and-interruptions` | `persistent-banner-alert-contract` |
| 24 | `designing-notification-centers` | `designing-notifications-and-interruptions` | `notification-center-contract` |
| 25 | `designing-background-task-progress` | `designing-latency-and-progressive-feedback` | `background-task-progress-contract` |
| 26 | `designing-indeterminate-progress` | `designing-latency-and-progressive-feedback` | `indeterminate-progress-contract` |
| 27 | `designing-skeleton-loading` | `designing-empty-loading-error-states` | `skeleton-loading-contract` |
| 28 | `designing-partial-failure-states` | `designing-empty-loading-error-states` | `partial-failure-state-contract` |
| 29 | `designing-retry-and-recovery-actions` | `designing-empty-loading-error-states` | `retry-recovery-action-contract` |
| 30 | `designing-connectivity-recovery` | `designing-offline-degraded-experiences` | `connectivity-recovery-contract` |
| 31 | `designing-chat-interfaces` | `designing-collaboration-and-presence` | `chat-interface-contract` |
| 32 | `designing-threaded-conversations` | `designing-chat-interfaces` | `threaded-conversation-contract` |
| 33 | `designing-message-composers` | `designing-chat-interfaces` | `message-composer-contract` |
| 34 | `designing-message-delivery-state` | `designing-chat-interfaces` | `message-delivery-state-contract` |
| 35 | `designing-read-receipts` | `designing-chat-interfaces` | `read-receipt-contract` |
| 36 | `designing-typing-indicators` | `designing-chat-interfaces` | `typing-indicator-contract` |
| 37 | `designing-message-reactions` | `designing-chat-interfaces` | `message-reaction-contract` |
| 38 | `designing-message-attachments` | `designing-message-composers` | `message-attachment-contract` |
| 39 | `designing-mentions-and-references` | `designing-collaboration-and-presence` | `mention-reference-contract` |
| 40 | `designing-conversation-search` | `designing-chat-interfaces` | `conversation-search-contract` |
| 41 | `designing-comment-systems` | `designing-collaboration-and-presence` | `comment-system-contract` |
| 42 | `designing-annotation-workflows` | `designing-comment-systems` | `annotation-workflow-contract` |
| 43 | `designing-collaborative-cursors` | `designing-collaboration-and-presence` | `collaborative-cursor-contract` |
| 44 | `designing-live-presence-indicators` | `designing-collaboration-and-presence` | `live-presence-contract` |
| 45 | `designing-sharing-dialogs` | `designing-collaboration-and-presence` | `sharing-dialog-contract` |
| 46 | `designing-invitation-flows` | `designing-collaboration-and-presence` | `invitation-flow-contract` |
| 47 | `designing-link-sharing` | `designing-collaboration-and-presence` | `link-sharing-contract` |
| 48 | `designing-collaboration-permissions` | `designing-permissions-and-consent` | `collaboration-permission-contract` |
| 49 | `designing-review-feedback-workflows` | `designing-task-flows` | `review-feedback-workflow-contract` |
| 50 | `designing-collaboration-awareness` | `designing-collaboration-and-presence` | `collaboration-awareness-contract` |
| 51 | `designing-first-run-onboarding` | `designing-onboarding` | `first-run-onboarding-contract` |
| 52 | `designing-product-tours` | `designing-onboarding` | `product-tour-contract` |
| 53 | `designing-coach-marks` | `designing-onboarding` | `coach-mark-contract` |
| 54 | `designing-onboarding-checklists` | `designing-onboarding` | `onboarding-checklist-contract` |
| 55 | `designing-contextual-help` | `designing-onboarding` | `contextual-help-contract` |
| 56 | `designing-help-center-navigation` | `designing-onboarding` | `help-center-navigation-contract` |
| 57 | `designing-progressive-feature-discovery` | `designing-onboarding` | `progressive-feature-discovery-contract` |
| 58 | `designing-sample-data-experiences` | `designing-onboarding` | `sample-data-experience-contract` |
| 59 | `designing-permission-onboarding` | `designing-permissions-and-consent` | `permission-onboarding-contract` |
| 60 | `designing-migration-onboarding` | `designing-onboarding` | `migration-onboarding-contract` |
| 61 | `designing-product-catalog-browsing` | `designing-commerce-checkout` | `product-catalog-browsing-contract` |
| 62 | `designing-product-detail-purchase-decisions` | `designing-commerce-checkout` | `product-purchase-decision-contract` |
| 63 | `designing-product-variant-selection` | `designing-commerce-checkout` | `product-variant-selection-contract` |
| 64 | `designing-shopping-carts` | `designing-commerce-checkout` | `shopping-cart-contract` |
| 65 | `designing-checkout-step-orchestration` | `designing-commerce-checkout` | `checkout-step-orchestration-contract` |
| 66 | `designing-shipping-method-selection` | `designing-commerce-checkout` | `shipping-method-selection-contract` |
| 67 | `designing-promotion-code-entry` | `designing-commerce-checkout` | `promotion-code-entry-contract` |
| 68 | `designing-order-tracking` | `designing-commerce-checkout` | `order-tracking-contract` |
| 69 | `designing-return-and-refund-flows` | `designing-financial-transaction-ui` | `return-refund-flow-contract` |
| 70 | `designing-wishlists-and-saved-items` | `designing-commerce-checkout` | `saved-commerce-intent-contract` |
| 71 | `designing-rich-text-editors` | `designing-editor-canvas-workspaces` | `rich-text-editor-contract` |
| 72 | `designing-markdown-editors` | `designing-editor-canvas-workspaces` | `markdown-editor-contract` |
| 73 | `designing-content-composer-workflows` | `designing-editor-canvas-workspaces` | `content-composer-workflow-contract` |
| 74 | `designing-content-preview` | `designing-editor-canvas-workspaces` | `content-preview-contract` |
| 75 | `designing-publishing-controls` | `designing-task-flows` | `publishing-control-contract` |
| 76 | `designing-content-scheduling` | `designing-task-flows` | `content-scheduling-contract` |
| 77 | `designing-editorial-status-workflows` | `designing-task-flows` | `editorial-status-workflow-contract` |
| 78 | `designing-content-taxonomy-management` | `architecting-information` | `content-taxonomy-contract` |
| 79 | `designing-media-library-interfaces` | `designing-editor-canvas-workspaces` | `media-library-interface-contract` |
| 80 | `designing-content-localization-workflows` | `designing-localized-interfaces` | `content-localization-workflow-contract` |
| 81 | `designing-api-explorers` | `designing-data-dense-interfaces` | `api-explorer-contract` |
| 82 | `designing-schema-explorers` | `designing-data-dense-interfaces` | `schema-explorer-contract` |
| 83 | `designing-query-builders` | `designing-data-dense-interfaces` | `query-builder-contract` |
| 84 | `designing-log-viewers` | `designing-data-dense-interfaces` | `log-viewer-contract` |
| 85 | `designing-trace-exploration` | `designing-data-dense-interfaces` | `trace-exploration-contract` |
| 86 | `designing-metrics-exploration` | `designing-data-visualization` | `metrics-exploration-contract` |
| 87 | `designing-feature-flag-management` | `designing-high-stakes-decisions` | `feature-flag-management-contract` |
| 88 | `designing-webhook-management` | `designing-data-dense-interfaces` | `webhook-management-contract` |
| 89 | `designing-secret-credential-management` | `designing-privacy-sensitive-interfaces` | `secret-credential-management-contract` |
| 90 | `designing-environment-management` | `designing-organization-administration` | `environment-management-contract` |
| 91 | `designing-consent-preference-centers` | `designing-permissions-and-consent` | `consent-preference-center-contract` |
| 92 | `designing-cookie-consent-controls` | `designing-permissions-and-consent` | `cookie-consent-control-contract` |
| 93 | `designing-privacy-control-centers` | `designing-privacy-sensitive-interfaces` | `privacy-control-center-contract` |
| 94 | `designing-security-centers` | `designing-privacy-sensitive-interfaces` | `security-center-contract` |
| 95 | `designing-device-session-management` | `designing-authentication-and-passkeys` | `device-session-management-contract` |
| 96 | `designing-two-factor-enrollment` | `designing-authentication-and-passkeys` | `two-factor-enrollment-contract` |
| 97 | `designing-recovery-code-management` | `designing-authentication-and-passkeys` | `recovery-code-management-contract` |
| 98 | `designing-data-export-portability` | `designing-privacy-sensitive-interfaces` | `data-export-portability-contract` |
| 99 | `designing-account-deletion` | `designing-authentication-and-passkeys` | `account-deletion-contract` |
| 100 | `designing-account-recovery-flows` | `designing-authentication-and-passkeys` | `account-recovery-flow-contract` |

## Coverage planes

Batch 002 expands ten areas that were still too broad after Batch 001:

- high-friction form/input state;
- navigation, browsing, and findability;
- feedback, waiting, and recovery;
- messaging protocols;
- collaboration and sharing;
- onboarding, learning, and adoption;
- commerce purchase/post-purchase lifecycle;
- content authoring and publishing;
- developer/technical operations surfaces;
- trust, privacy, and account lifecycle.

The batch deliberately decomposes existing broad owners rather than creating competing generic faculties. For example, `designing-forms`, `designing-search`, `designing-collaboration-and-presence`, `designing-onboarding`, `designing-commerce-checkout`, `designing-editor-canvas-workspaces`, `designing-authentication-and-passkeys`, and `designing-privacy-sensitive-interfaces` remain authoritative parents.

## Anti-overlap courts

The batch was authored with explicit sibling boundaries. These distinctions are structural requirements, not naming preferences:

- **field validation vs partial failure:** one repairs invalid user data; the other represents mixed outcomes of composite/system operations;
- **multi-step forms vs checkout orchestration:** generic staged capture versus commercial state whose totals/inventory/tax/payment dependencies can invalidate later stages;
- **pagination vs infinite scroll:** addressable bounded pages versus anchored continuous continuation;
- **search results vs faceted search:** interpretation of matches versus boolean refinement of the query universe;
- **toast vs notification center:** transient local acknowledgement versus durable cross-session attention debt;
- **typing vs presence:** ephemeral composing activity versus scoped collaborative membership/freshness;
- **comment vs annotation:** durable discussion versus discussion plus a resilient artifact anchor;
- **review feedback vs approval:** structured findings/re-review versus formal decision authority;
- **first run vs tour vs coach mark:** state initialization versus coherent multi-stop orientation versus one contextual teaching intervention;
- **sample data vs migration:** isolated synthetic learning substrate versus real production-data transition with provenance and rollback;
- **catalog vs product detail:** building a consideration set versus deciding on one exact commercial proposition;
- **rich text vs Markdown:** semantic WYSIWYG document model versus source-first markup truth;
- **preview vs publishing:** render evidence versus external/release commitment authority;
- **logs vs traces vs metrics:** discrete event evidence versus causal span graphs versus aggregated time-series measurements;
- **feature flags vs environments:** feature-exposure evaluation rules versus runtime/deployment context;
- **consent center vs privacy center:** purpose-based optional processing choices versus broader privacy settings/requests/actions;
- **recovery codes vs account recovery:** custody of one backup factor versus the entire identity-restoration lifecycle.

## Source and authority posture

No third-party skill prose was imported. Domain mechanisms are synthesized as NUI-owned decision contracts. Where a topic depends on volatile law, platform permission behavior, security policy, payment/logistics authority, or service implementation, the skill explicitly requires current authoritative verification rather than freezing a potentially stale rule into prose.

External documentation, standards, libraries, and research may later be used during task execution under NUI's existing authority hierarchy. Such sources remain mechanism/evidence authorities within bounded roles; they do not become universal visual or product authority.

## Structural verification gates

Batch 002's dedicated acceptance suite is `tests/test_ui_industry_batch_002.py`. It checks:

- exactly 100 literal unique slugs;
- file existence and exact frontmatter identity;
- substantive Decision / Failure / Falsification / Output content;
- canonical graph registration with valid parent/family/output;
- unique outputs with no collision against the pre-Batch-002 graph;
- acyclic parent chains reaching `using-nolane-ui`;
- exact graph count of 374;
- normalized exact-body duplicate rejection;
- pairwise trivial-rename suspicion threshold.

Graph integration was committed only after this acceptance suite passed on the integrated workspace.

Final repository closure additionally requires:

```bash
PYTHONPATH=src python -m unittest discover -s tests -v
python scripts/nui-validate .
```

and a green `Verify NUI` GitHub Actions run on the exact final PR head after temporary bookkeeping tools have been removed.

## Claim boundary

Passing these tests proves repository structure, routing ownership, authored-corpus constraints encoded by the tests, and canonical graph integrity. It does not prove that every individual recommendation is universally optimal or that NUI has a model-independent causal effect on generated UI quality. Those stronger claims remain subject to NUI's empirical evaluation protocol.