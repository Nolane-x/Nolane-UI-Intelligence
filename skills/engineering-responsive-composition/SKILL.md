---
name: engineering-responsive-composition
description: Engineer responsive interfaces as explicit composition state changes driven by available space, content pressure, and interaction needs rather than width-only scaling.
---

# Engineering responsive composition

Responsive design becomes fragile when every component independently reacts to arbitrary viewport numbers. Use this skill when a product must preserve task hierarchy and interaction integrity as space changes across phones, tablets, desktop windows, embedded regions, split views, and zoomed layouts.

## Decision ownership

Own the composition model that maps environmental constraints to layout states. Decide which regions resize continuously, which reflow, which reorder, which collapse behind alternate navigation, and which must remain invariant. Define where responsiveness is governed by viewport, container, content, input modality, or product state.

## Inputs and evidence

Collect representative content lengths, localization expansion, user zoom, minimum and maximum window sizes, nested container sizes, touch and pointer constraints, task priority, persistent actions, and screenshots or recordings from real products. Identify layouts whose current breakpoints only work because sample content is short.

Measure each region’s minimum viable width and height before it becomes unreadable or operationally compromised.

## Procedure

Model a small set of meaningful composition states rather than dozens of device labels. For each state, define hierarchy, order, visibility, overflow, navigation, and continuity of user state. Allow fluid sizing inside a state, but use discrete transitions when the information architecture changes.

Prefer local container ownership when a component can appear in several shells. Reserve global viewport decisions for shell-level composition. Coordinate nested responsive rules so a card does not compact while its surrounding layout still allocates enough space.

Test state transitions while dialogs, forms, selection, scroll positions, and asynchronous content are active.

## Failure topology

Width-only shrinking can create controls that technically fit but no longer communicate hierarchy. Breakpoints tied to popular devices fail in split-screen and browser zoom. Another failure is independent component adaptation that produces contradictory states, such as a toolbar collapsing while a neighboring panel expands into the freed space and then oscillates around a threshold.

Responsive transitions can also destroy user context by remounting regions or changing navigation position without state preservation.

## Falsification

Sweep available width and height continuously rather than testing only canonical breakpoints. Inject long labels, error messages, banners, and late-loading content. Resize during active interaction and verify focus, selection, scroll, and unfinished input survive. Test 200–400% zoom where viewport CSS width changes but user intent does not.

If a layout needs ad hoc exceptions for each page using the same component, the responsive ownership boundary is wrong.

## Output contract

Produce a `responsive-composition-contract` containing composition states, triggers, region priority, resize/reflow/reorder rules, visibility and overflow behavior, viewport-versus-container authority, state preservation requirements, and evidence across continuous resize, zoom, localization, and active interaction.

## Handoffs

Use `designing-container-query-layouts` for local space adaptation, `designing-content-driven-breakpoints` for threshold derivation, `designing-responsive-region-reordering` for order changes, and `verifying-responsive-state-parity` for cross-state behavioral equivalence.