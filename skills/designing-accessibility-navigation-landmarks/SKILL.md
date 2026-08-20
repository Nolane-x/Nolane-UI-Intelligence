---
name: designing-accessibility-navigation-landmarks
description: Use when a page or application needs reliable structural regions that let assistive-technology users understand, traverse, and distinguish major areas without converting every visual section into a landmark.
---

# Designing Accessibility Navigation Landmarks

## Parent Contract
**Required parent:** `designing-accessible-interfaces`.

This faculty owns the structural-region model exposed to assistive navigation: which areas deserve landmark semantics, how repeated regions are distinguished, and how the region model remains stable while a dynamic application changes. It does not own the visual grid, generic screen-reader behavior, or skip-link mechanics. Its question is narrower: what meaningful page regions should exist in the accessibility tree, and can a user navigate them without ambiguity?

## Decision Boundary
Start from product structure rather than DOM containers. Identify regions that users genuinely reason about as destinations: primary navigation, main task content, contextual search, complementary information, and footer-like supporting material. Promote only those regions whose boundaries help orientation. A visually boxed panel is not automatically a landmark, and nested landmarks are not automatically useful.

Repeated landmark types require an accessible identity when they coexist. Two navigation regions should expose why they differ, such as product navigation versus account navigation, rather than forcing users to hear an undifferentiated list of “navigation” entries. The main region should correspond to the current route or task surface, not to a shell that permanently wraps every route. Dynamic portals, drawers, and embedded workspaces must not create a second contradictory map of the page.

Treat landmark stability as part of interaction state. Loading, empty, error, and permission states may change contents while preserving the same semantic destination. Conversely, a modal task that intentionally isolates the background should expose the modal's meaningful regions without leaving inert background landmarks discoverable as if they were actionable.

## Failure Topology
- Every card, panel, or section becomes a landmark and landmark navigation becomes noisier than heading navigation.
- Multiple navigation or complementary regions have identical accessible names, so the user cannot predict where each jump lands.
- A persistent app shell owns `main` while route content is nested beneath it, causing the semantic primary content to be unclear.
- Client-side route changes replace content but leave stale region labels or duplicate main regions in the accessibility tree.
- A dialog opens while background landmarks remain traversable even though the background is inert.
- Visual redesign moves functions between regions without updating the semantic region model.

## Falsification and Recovery
Test the rendered experience with landmark quick-navigation, not source inspection alone. Enumerate every exposed region on representative routes, route transitions, empty/error states, drawers, and modal states. The design fails if a user hearing only region type and accessible label cannot explain the purpose of each region, if two active `main` destinations coexist, or if moving by landmarks routinely lands on decorative structure.

Recover by collapsing low-information regions, naming repeated region types from product semantics, binding the main region to route ownership, and synchronizing modal/inert state with the exposed accessibility tree. Re-test after responsive recomposition because desktop sidebars and mobile drawers can produce different region topology.

## Output Contract
Return `accessibility-landmark-contract` with the canonical region inventory, semantic type for each region, accessible naming rules for repeated types, route ownership of main content, dynamic/modal behavior, responsive deltas, prohibited over-landmarking cases, and assistive-navigation verification scenarios.
