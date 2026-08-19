# UI Industry 1000 — Batch 002 Design

## Purpose

Batch 002 expands the canonical NUI graph from 274 to 374 skills by adding exactly 100 specialist faculties. The batch continues the roadmap without treating skill count as quality: every new skill must own a decision boundary or failure topology that is narrower and behaviorally distinct from its parent and from every sibling.

The user constraint is hard: the 100 `SKILL.md` bodies are authored individually. No loop, template generator, macro expansion, bulk prose transformation, cloned body, or prompt-programmatic skill generation is allowed. Automation may be used only for deterministic bookkeeping such as graph insertion, inventory validation, exact counts, and duplicate detection; it may not create or rewrite skill prose.

## Baseline invariants

- Starting canonical graph: exactly 274 skills at main commit `250cae20b42534de78f4b4913573049f9460dc28`.
- Ending canonical graph: exactly 374 skills.
- Historical 174-skill V6/V8 depth baseline remains intact.
- Batch 001's 100 slugs remain intact and are not renamed or repurposed.
- One canonical graph remains authoritative: `skills/skill-graph.json`.
- Every Batch 002 skill has a unique slug, unique graph output, valid existing parent, and parent chain reaching `using-nolane-ui`.
- Every body contains an explicit Decision boundary, observable inputs, conditional tradeoffs, named Failure modes, a Falsification test, recovery guidance, and a meaningful Output contract.
- Structural tests may prove corpus integrity; they must not claim model-independent UI quality or empirical superiority.

## Ownership strategy

Batch 002 deliberately decomposes already-existing broad owners instead of creating competing generic experts. Examples:

- `designing-forms` remains the owner of general form architecture; Batch 002 owns narrower validation, dependency, multi-step, autosave, and input-specific contracts.
- `designing-navigation` and `designing-search` remain generic owners; Batch 002 owns concrete findability and browsing state machines.
- `designing-notifications-and-interruptions`, `designing-latency-and-progressive-feedback`, `designing-empty-loading-error-states`, and `designing-offline-degraded-experiences` remain broad temporal owners; Batch 002 owns specialist feedback/recovery mechanisms only.
- `designing-collaboration-and-presence` remains the collaboration owner; Batch 002 decomposes messaging, comments, sharing, invitations, and awareness.
- `designing-onboarding` remains the onboarding owner; Batch 002 decomposes first-run, tours, coach marks, checklists, contextual help, and migration paths.
- `designing-commerce-checkout` and `designing-financial-transaction-ui` remain transaction owners; Batch 002 owns commerce lifecycle decisions around catalog, cart, fulfillment choice, tracking, returns, and saved intent.
- `designing-editor-canvas-workspaces`, `writing-interface-copy`, `designing-localized-interfaces`, and `designing-task-flows` remain broad authoring/workflow owners; Batch 002 adds content-production specialists.
- Trust/account specialists inherit from `designing-authentication-and-passkeys`, `designing-permissions-and-consent`, and `designing-privacy-sensitive-interfaces`; they do not redefine those parents.

## Exact 100-skill inventory

### A. Forms and high-friction input — 001–010

1. `designing-field-validation-and-error-recovery`
2. `designing-dependent-form-fields`
3. `designing-multi-step-forms`
4. `designing-form-autosave-and-drafts`
5. `designing-address-entry`
6. `designing-phone-number-entry`
7. `designing-one-time-code-entry`
8. `designing-password-creation-and-strength`
9. `designing-monetary-input`
10. `designing-measurement-and-unit-input`

### B. Navigation, browsing, and findability — 011–020

11. `designing-global-navigation-shells`
12. `designing-sidebar-navigation`
13. `designing-breadcrumb-navigation`
14. `designing-mega-navigation`
15. `designing-pagination`
16. `designing-infinite-scroll-browsing`
17. `designing-search-result-interfaces`
18. `designing-faceted-search`
19. `designing-saved-searches-and-views`
20. `designing-recent-items-navigation`

### C. Feedback, waiting, and recoverability — 021–030

21. `designing-toast-feedback`
22. `designing-inline-status-feedback`
23. `designing-persistent-banner-alerts`
24. `designing-notification-centers`
25. `designing-background-task-progress`
26. `designing-indeterminate-progress`
27. `designing-skeleton-loading`
28. `designing-partial-failure-states`
29. `designing-retry-and-recovery-actions`
30. `designing-connectivity-recovery`

### D. Messaging and conversation — 031–040

31. `designing-chat-interfaces`
32. `designing-threaded-conversations`
33. `designing-message-composers`
34. `designing-message-delivery-state`
35. `designing-read-receipts`
36. `designing-typing-indicators`
37. `designing-message-reactions`
38. `designing-message-attachments`
39. `designing-mentions-and-references`
40. `designing-conversation-search`

### E. Collaboration and sharing — 041–050

41. `designing-comment-systems`
42. `designing-annotation-workflows`
43. `designing-collaborative-cursors`
44. `designing-live-presence-indicators`
45. `designing-sharing-dialogs`
46. `designing-invitation-flows`
47. `designing-link-sharing`
48. `designing-collaboration-permissions`
49. `designing-review-feedback-workflows`
50. `designing-collaboration-awareness`

### F. Onboarding, education, and adoption — 051–060

51. `designing-first-run-onboarding`
52. `designing-product-tours`
53. `designing-coach-marks`
54. `designing-onboarding-checklists`
55. `designing-contextual-help`
56. `designing-help-center-navigation`
57. `designing-progressive-feature-discovery`
58. `designing-sample-data-experiences`
59. `designing-permission-onboarding`
60. `designing-migration-onboarding`

### G. Commerce purchase lifecycle — 061–070

61. `designing-product-catalog-browsing`
62. `designing-product-detail-purchase-decisions`
63. `designing-product-variant-selection`
64. `designing-shopping-carts`
65. `designing-checkout-step-orchestration`
66. `designing-shipping-method-selection`
67. `designing-promotion-code-entry`
68. `designing-order-tracking`
69. `designing-return-and-refund-flows`
70. `designing-wishlists-and-saved-items`

### H. Content authoring and publishing — 071–080

71. `designing-rich-text-editors`
72. `designing-markdown-editors`
73. `designing-content-composer-workflows`
74. `designing-content-preview`
75. `designing-publishing-controls`
76. `designing-content-scheduling`
77. `designing-editorial-status-workflows`
78. `designing-content-taxonomy-management`
79. `designing-media-library-interfaces`
80. `designing-content-localization-workflows`

### I. Developer and technical operations surfaces — 081–090

81. `designing-api-explorers`
82. `designing-schema-explorers`
83. `designing-query-builders`
84. `designing-log-viewers`
85. `designing-trace-exploration`
86. `designing-metrics-exploration`
87. `designing-feature-flag-management`
88. `designing-webhook-management`
89. `designing-secret-credential-management`
90. `designing-environment-management`

### J. Trust, privacy, and account lifecycle — 091–100

91. `designing-consent-preference-centers`
92. `designing-cookie-consent-controls`
93. `designing-privacy-control-centers`
94. `designing-security-centers`
95. `designing-device-session-management`
96. `designing-two-factor-enrollment`
97. `designing-recovery-code-management`
98. `designing-data-export-portability`
99. `designing-account-deletion`
100. `designing-account-recovery-flows`

## Anti-overlap courts

The following pairs must remain materially distinct in their bodies and graph outputs:

- field validation vs partial failure: local form correctness vs distributed/system operation degradation;
- multi-step forms vs checkout orchestration: generic staged data capture vs transaction-specific commitment/risk boundaries;
- pagination vs infinite scroll: explicit addressable page state vs continuous feed continuation;
- search results vs faceted search: result interpretation/ranking vs query-space narrowing;
- toast feedback vs notification center: transient local acknowledgement vs durable cross-session attention debt;
- typing indicators vs live presence: transient composing activity vs workspace occupancy/availability;
- message reactions vs review feedback: lightweight social acknowledgement vs structured evaluative work;
- first-run onboarding vs product tour vs coach mark: initial activation sequence vs multi-stop orientation vs single-context teaching cue;
- sample data vs migration onboarding: reversible learning substrate vs real-data transition and trust;
- product catalog vs product detail: browse/compare set construction vs single-item purchase confidence;
- rich-text editor vs markdown editor: structure-first WYSIWYG semantics vs source/preview duality;
- content preview vs publishing controls: representation fidelity vs irreversible/external release authority;
- logs vs traces vs metrics: event stream inspection vs causal request path vs aggregated signal behavior;
- feature flags vs environments: runtime exposure policy vs deployment/configuration target context;
- consent preference center vs privacy control center: legal/purpose permission state vs durable privacy/account data controls;
- account recovery vs recovery-code management: identity re-entry lifecycle vs custody/use of a specific recovery factor.

## Graph metadata rules

Each node receives:

- a `family` ending in `-specialist` appropriate to its plane;
- a parent that already exists in the canonical graph (or another earlier Batch 002 node where the hierarchy is semantically necessary);
- a unique `output` noun that describes an artifact, not a vague `result` or duplicated generic contract.

No Batch 002 node may become a second root-level generic owner when a suitable parent already exists.

## Acceptance gates

A dedicated `tests/test_ui_industry_batch_002.py` must prove at minimum:

1. exact inventory is 100 unique slugs;
2. all 100 files exist and frontmatter names match slugs;
3. each body is substantive and contains Decision, Failure, Falsification, and Output semantics;
4. all 100 nodes exist in the canonical graph;
5. each node has family/parent/output and an existing parent;
6. outputs are unique inside Batch 002 and do not collide with the existing graph;
7. every parent chain reaches `using-nolane-ui` without cycles;
8. final graph count is exactly 374;
9. Batch 001 inventory remains present;
10. no exact duplicate normalized body exists within Batch 002;
11. no body is a trivial rename of another body after removing slug/title/frontmatter;
12. repository-wide `python -m unittest discover -s tests -v` passes;
13. `python scripts/nui-validate .` passes;
14. GitHub Actions Verify NUI passes on the final PR head.

## Documentation and provenance

Create `docs/research/UI-INDUSTRY-1000-BATCH-002.md` with the exact inventory, parent/output map, authorship constraints, overlap courts, bounded source posture, and verification evidence. README EN/VN/CN and `AGENTS.md` move from 274 to 374 only after graph and tests are green.

External sources may inform standards, semantics, platform behavior, and mechanism discovery. They are not copied as skill prose and do not become universal aesthetic authority. High-drift legal/platform details must be treated as verification obligations rather than timeless facts embedded in a skill.

## Completion definition

Batch 002 is complete only when the clean final branch contains 100 new independently authored skill bodies, canonical graph integration, tests, provenance, updated count documentation, no one-time tooling, and a green full GitHub Actions run. A partial corpus, green Batch-only test with red repository suite, or 100 files without routing ownership is not completion.
