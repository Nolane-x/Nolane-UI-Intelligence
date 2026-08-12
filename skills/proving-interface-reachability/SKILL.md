---
name: proving-interface-reachability
description: Use when a multi-screen or multi-surface product must prove that every required destination and capability can actually be reached by intended users without secret URLs or undocumented knowledge.
---

# Proving Interface Reachability

## Parent Contract
**Required parent:** `designing-navigation`.

Consume the navigation contract, actor roles, capability ledger, action registry, and known entry points. Navigation design owns hierarchy and orientation; this faculty owns the **proof** that required destinations are reachable under real role/state constraints.

## Decision Boundary
Reachability is a graph property, not a screenshot property. This skill models interactive surfaces as nodes and valid user transitions as directed edges. It answers: “Starting from a legitimate entry point, can the intended actor discover and traverse a valid path to every required capability, and can they escape or recover afterward?”

A route existing in code is not sufficient. A deep link may support sharing or restoration but does not prove ordinary discoverability. A hidden command may be valid for expert acceleration but cannot be the only access path to a capability required for first-time users. Likewise, a visible navigation item that leads to a permission dead-end is not a valid edge for that role.

## Product Truth
One of the most damaging small AI UI failures is an orphan destination: the agent designs a polished settings page, detail view, import workflow, history panel, or admin tool but never creates a path to it. Every individual screen can look complete while the product graph is broken. Other failures are subtler: a modal can open but not close with keyboard; an empty state removes the only “create” path; mobile hides an overflow action that desktop exposes; after a destructive action the user is left on a non-existent object; back navigation crosses account boundaries; a role sees a CTA but lacks permission to complete it.

Reachability proof forces product-level reasoning across these edges.

## Decision Model
1. **Define surface nodes.** A surface is a navigable or interaction-significant context: page, panel, modal route, sheet, full-screen editor, settings subsection, canvas mode, wizard step, command context, or native destination. Do not create nodes for every tooltip.
2. **Define legitimate entry nodes.** Include application launch, authenticated home, deep-link entry when explicitly supported, notification entry, shared link, restored session, and role-specific start points. Mark which entry is primary for each actor.
3. **Define edges from real bindings.** An edge requires an action plus a discoverable binding in the source context. “User can go there” without a control, menu item, contextual affordance, keyboard command with discovery, or accepted external entry is not an edge.
4. **Attach predicates.** Record role, entitlement, object state, viewport, platform, connectivity, selection, and feature flag constraints. Reachability must be proven under each required profile, not in an abstract super-user state.
5. **Compute required-node reachability.** Traverse from each relevant entry and identify unreachable required surfaces. Separate intentionally inaccessible surfaces from accidental orphans.
6. **Check capability reachability.** A surface can be reachable while its capability remains hidden. Prove that required actions on the destination also have valid bindings.
7. **Check exit and recovery edges.** Modals, full-screen modes, destructive results, permission denial, validation failures, offline states, expired sessions, and interrupted wizards need paths forward or back. A path that enters a state but cannot safely exit is a dead end.
8. **Check responsive transformations.** If desktop sidebar navigation becomes mobile tabs/menus, verify every required destination survives. Do not accept “mobile version simplified” as justification for silent capability loss.
9. **Check alternate modalities.** Keyboard, assistive technology, remote, touch, and gesture constraints can invalidate an edge even if pointer traversal works.
10. **Record shortest and expected paths.** Excessive path depth is not automatically failure, but frequent/high-consequence capabilities should not depend on obscure multi-step discovery without rationale.

## Evidence
The strongest evidence combines the design graph with an inspectable implementation. Static route tables show destinations, menus and command registries show potential edges, runtime traversal proves actual behavior, and accessibility trees can reveal whether bindings are operable/announced. For proposed UI, evidence may be a fully specified prototype; mark unimplemented edges as design evidence rather than runtime evidence.

Use model-based testing thinking: nodes and edges should be enumerable enough that an automated or human probe can attempt representative paths. Preserve failed traversal observations as evidence; do not erase them after fixing the route.

## Output Contract
Return `reachability-proof` with:
- `surfaces[] {id, kind, required_capabilities, actor_profiles, lifecycle_states}`
- `entry_points[] {surface_id, actor_profile, context, primary}`
- `edges[] {from, to, action_id, binding_ref, predicates, modalities, evidence_refs}`
- `reachable_by_profile {profile_id: surface_ids[]}`
- `orphan_surfaces[]`
- `dead_ends[] {surface, state, missing_exit_or_recovery}`
- `secret_only_paths[]`
- `responsive_losses[]`
- `status: PASS|FAIL|UNKNOWN`

`PASS` requires every required surface/capability to be reachable for its intended profile and every material entered state to have an appropriate exit/recovery disposition.

## Failure Traps
- Counting a route definition as navigation evidence.
- Letting a direct URL rescue a settings page that ordinary users must discover from the product.
- Testing reachability only as an administrator.
- Proving desktop but assuming mobile overflow menus preserve all destinations.
- Treating browser Back as the universal recovery mechanism for modal/workflow state.
- Ignoring focus trapping or keyboard inoperability when an edge technically exists for pointer users.
- Adding a hamburger menu entry without checking whether its parent menu itself is reachable/operable.
- Marking intentionally role-inaccessible surfaces as orphans instead of encoding predicates.
- Forgetting post-action destinations: after archive/delete/move, where is the user placed and is that node valid?

**Hard gate:** a required destination that exists only by secret URL, undocumented expert command, or inaccessible modality is not product reachability.
