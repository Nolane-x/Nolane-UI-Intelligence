---
name: inventorying-product-capabilities
description: Use when a product contains multiple features, roles, workflows, settings, integrations, or lifecycle states and the UI must prove that none of the required capabilities disappear during design.
---

# Inventorying Product Capabilities

## Parent Contract
**Required parent:** `modeling-product-intent`.

Consume the accepted product intent, actors, requirements, constraints, existing implementation evidence, and explicit exclusions. This skill does not invent product strategy. It converts product truth into a canonical inventory that later UI artifacts must account for.

## Decision Boundary
This faculty owns **what the product must let each actor accomplish or perceive**, before deciding where controls live or what screens look like. It is not information architecture, navigation, interaction design, visual styling, or component selection. A capability is a stable product obligation such as “workspace owner can invite a member,” “editor can restore a previous version,” “viewer can export permitted data,” or “system communicates synchronization conflict.” It is not a button label, route name, modal, API endpoint, database table, or vague epic such as “settings.”

Use this skill when a task is product-wide, multi-feature, inherited from an existing application, or likely to lose small features during redesign. For a one-control local edit, the parent may justify not invoking it.

## Product Truth
AI-generated UI often loses requirements during compression. A prompt says “build a project management system,” a codebase contains twenty capabilities, and a generated mockup preserves only dashboard, tasks, and profile. The missing audit log, member roles, import, archive, recovery, notification controls, empty-state creation paths, or destructive confirmations may be individually small yet collectively make the product unusable.

Treat capability inventory as lossless accounting. A capability may be hidden behind progressive disclosure, role gating, context menus, command palettes, keyboard shortcuts, system automation, or a secondary settings surface, but it may not silently vanish. Completeness is not the same as visible clutter: the ledger records existence and required access; later faculties choose appropriate disclosure.

Requirements can come from PRDs, tickets, source routes, commands, menus, analytics events, permission tables, tests, localization keys, API schemas, screenshots, existing production behavior, and user statements. These sources can conflict. Preserve disagreement instead of flattening it into a guess.

## Decision Model
1. **Collect product truth.** Enumerate explicit user requirements first. Then inspect available implementation evidence: route tables, menus, command registries, feature flags, permission checks, tests, analytics event names, localized copy, integration manifests, settings models, import/export handlers, and recovery flows. Record the origin of each claim.
2. **Normalize capability identity.** Give each capability a canonical ID independent of presentation. Prefer actor + verb + object + meaningful qualifier: `owner.invite-member`, `editor.restore-version`, `viewer.export-report`, `system.resolve-sync-conflict`. Merge aliases only when their outcome, authority, data effect, and failure semantics are equivalent.
3. **Classify consequence.** Mark whether it is core, supporting, administrative, rare-but-critical, safety/privacy, destructive, reversible, background/system-assisted, or informational. Frequency does not determine importance. “Delete organization” may be rare and still release-critical.
4. **Bind actors and authority.** Record which roles may discover, invoke, approve, observe, or never see the capability. If authority depends on state, plan, locale, device, or organization policy, make the condition explicit.
5. **Bind product states.** State prerequisites and lifecycle availability: first-run, empty, populated, offline, read-only, archived, trial, expired, conflict, loading, degraded, error, success. A capability available only in the happy path is not fully inventoried.
6. **Mark surface obligations without designing surfaces.** State whether the capability needs at least one interactive surface, can be system-only, must be globally reachable, may be contextual, or needs an alternative modality. This is an obligation passed to reachability and action faculties, not a layout decision.
7. **Record exclusions.** If a requested redesign intentionally removes a legacy capability, name the authority and rationale. Absence is allowed only when explicit.
8. **Reconcile duplicates.** Detect two capability IDs that differ only by wording but own the same product effect, and detect one broad capability that actually hides several independently authorized actions.
9. **Assign evidence status.** Use `CONFIRMED`, `INFERRED`, `CONFLICTED`, or `UNKNOWN`. Inference never upgrades itself to confirmed because the UI needs an answer.

A useful audit question is: “If every screen vanished and I had to reconstruct the product from this ledger, would I know every meaningful thing each actor needs to accomplish or observe?” If not, keep discovering.

## Evidence
Prefer product-local evidence over generic UI conventions. Strong evidence includes accepted product requirements, current behavior verified in the application, source code or tests that clearly encode a capability, permission models, and authoritative stakeholder decisions. Screenshots are evidence of visible behavior at a moment, not proof that invisible states do not exist. Repository search is useful for discovering hidden actions, but implementation residue can be stale; mark uncertainty.

For migrations or redesigns, compare old and proposed capability sets. Every removed, merged, split, newly introduced, or authority-changed capability needs an explicit delta. For greenfield work, use scenario decomposition and domain research to expose likely omissions, but label domain assumptions until accepted.

## Output Contract
Return `capability-ledger` with:
- `capabilities[] {id, actor_roles, outcome, consequence, frequency, authority, prerequisites, lifecycle_states, surface_obligation, reversibility, evidence_refs, status}`
- `aliases[] {term, canonical_id}`
- `conflicts[] {claim_a, claim_b, required_authority}`
- `intentional_exclusions[] {capability, authority, rationale}`
- `coverage_summary {confirmed, inferred, conflicted, unknown, release_critical_unknowns}`
- `discovery_sources[]`

The ledger is canonical input to action registration, reachability proof, scenario coverage, implementation specification, and completeness criticism. IDs are stable across surface redesigns unless product semantics change.

## Failure Traps
- Turning every navigation destination into a capability. Destinations organize access; capabilities describe outcomes.
- Treating backend endpoints as the inventory. APIs expose implementation, not necessarily user obligations.
- Deleting rare actions because they would clutter a mockup. Progressive disclosure solves clutter; erasure creates product loss.
- Merging actions that share a noun but differ in authority or consequence, such as “archive,” “delete,” and “leave workspace.”
- Assuming mobile and desktop have identical capability availability without evidence.
- Recording “manage settings” as one item when billing, security, notifications, members, export, and retention have independent authority and recovery rules.
- Allowing a redesign to remove features because the generated visual reference did not show them.
- Marking inferred capability truth as confirmed to unblock layout.

**Hard gate:** a product-wide design cannot claim functional closure while a release-critical capability is `UNKNOWN`, `CONFLICTED`, or has no explicit disposition.

## V6 Capability Inventory Protocol
Separate **capability-action distinction**: a system capability may enable multiple user actions; a visible action may require several capabilities. Assign a **source-of-truth owner** for each capability (service, local state, platform API, policy, integration) and its current availability evidence.

Represent **permission-dependent capability** states so UI does not advertise impossible actions or erase discoverability before access is requested appropriately. Classify every **capability gap class** as unavailable, unimplemented UI, permission blocked, unsupported platform, degraded/offline, experimental, or unknown. Add an **inventory freshness checkpoint** before major routing/implementation when backend/platform flags or integrations can drift.

### Falsification
Compare the inventory against actual runtime/API permissions and search for hidden backend actions or dead UI actions. Any mismatch falsifies capability truth.

### Recovery
Refresh authoritative sources, update action registry/routes, and explicitly mark unknown/unavailable capability instead of designing around an assumption.

## V9 Expected-Capability Disposition
Consume the parent's broad product envelope as **candidate obligations**, not as a mandatory feature dump. Every expected capability family must be reconciled into concrete capability records and receive one explicit product disposition: `REQUIRED`, `EXPECTED`, `OPTIONAL`, `EXCLUDED`, or `UNKNOWN`. These labels govern scope accounting; they do not directly prescribe visual prominence.

`REQUIRED` means the claimed product outcome or release cannot truthfully succeed without it. `EXPECTED` means the family is strongly implied by product class, actor lifecycle, consequence or production ambition and therefore needs an explicit implementation/exclusion decision. `OPTIONAL` is valid enrichment whose absence does not break the stated outcome. `EXCLUDED` is deliberate absence with authority and rationale. `UNKNOWN` preserves unresolved truth and blocks high-ambition closure when material.

Do not let broad nouns collapse independent obligations. “Settings” may conceal security, notifications, billing, workspace policy, appearance, accessibility, data/export, integrations and retention. “Account” may conceal registration, recovery, session/device management, profile, workspace membership, invitations, switching, ownership transfer, deactivation and deletion. “Editor tools” may conceal selection, history, assets, inspectors, export and precision alternatives. Split only where actor authority, lifecycle, consequence, state or recovery differs materially.

Maintain **family coverage accounting** alongside the canonical ledger. A family counts as covered only when discovery evidence exists and its concrete capabilities have dispositions. A family is not covered because a page with the same noun exists. An `EXCLUDED` family remains visible in coverage accounting so future designers cannot accidentally rediscover or silently reintroduce it without the prior rationale.

### V9 Falsification
Take a full-platform ledger and remove one unglamorous expected family while leaving every remaining route and scenario perfectly closed. If the inventory still reports complete without surfacing the missing family/disposition, the ledger is only internally complete, not scope-adequate.

### V9 Recovery
Return to the product envelope, restore the family, split it into independently meaningful capabilities, assign evidence/dispositions and rerun downstream action, route, scenario and runtime closure. Do not compensate for missing product breadth by increasing visible widget count.
