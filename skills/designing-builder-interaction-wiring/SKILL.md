---
name: designing-builder-interaction-wiring
description: Use when a visual builder lets authors connect events to navigation, state changes, data mutations, overlays, animations, external actions, or custom logic and must make trigger, target, scope, ordering, authority, and failure explicit.
---

# Designing Builder Interaction Wiring

## Parent Contract

**Required parent:** `designing-visual-application-builders`.

This skill owns the authoring graph that connects user/system events to effects. It is not a general end-user interaction skill. Its concern is whether the builder author can understand and safely edit executable behavior without hiding side effects behind small lightning-bolt icons or property strings.

## Action graph

Represent a wire as `trigger → guards/context → action/effect → result/error → next state`. Triggers may be click/press, submit, value change, lifecycle, viewport, data completion, timer or custom events. Actions differ in consequence: local state update, navigation, overlay, animation, data mutation, message/send, download, external URL, privileged tool call. Surface consequence class and authority at authoring time.

Define scope. An event can originate in a component instance but target local component state, page state, selected repeated item, global application state or external system. Resolve targets by stable semantic identity; visual proximity is not a valid target model. When a reusable component emits an event, prefer a declared event output that the instance wires externally rather than reaching through component internals.

Ordering and concurrency matter. Multiple actions on one trigger may be sequential, parallel, conditional or transactional. A navigation that occurs before a save resolves can abandon error handling. A double press can duplicate mutations unless the runtime defines idempotency/pending state. Builders should expose at least the execution order and failure path for consequential chains.

Preview must distinguish safe simulation from real side effects. Authors need to test interactions without accidentally emailing customers, deleting records or publishing changes. Where a true integration test is necessary, bind it to an explicit environment/permission and show evidence of the target.

## Evidence

Use runtime event/action schema, component event contracts, navigation/data mutation APIs, error propagation, async behavior, preview sandboxing and exported implementation. Inspect real workflows with several actions and failures, not only button→page transitions.

## Failure topology

Failures include wiring to element IDs that change after reparenting; hidden action chains with no ordering; duplicated mutation on rapid trigger; preview executing production side effects; an instance reaching into its component definition's private node; failed async action followed by navigation anyway; and no visible explanation of what currently listens to or emits an event.

## Falsification

Build chains with local update, guarded data mutation, error handling and navigation. Rename/reparent targets, duplicate component instances, trigger rapidly, simulate failure/offline and run preview in a non-production environment. The contract is falsified if target scope changes silently, if ordering cannot be predicted, if error paths disappear, if a reusable component's private structure becomes an external dependency, or if preview safety is ambiguous.

## Recovery

Move wires to stable declared events/actions, split long opaque chains into named flows, introduce pending/idempotency guards, and expose failure branches. Replace production preview side effects with mocks/sandboxes or explicit test environments. Preserve broken target references as repairable diagnostics rather than dropping actions silently.

## Output contract

Return a `builder-interaction-wiring-contract` containing trigger taxonomy, action consequence classes, target/scope model, guard/order/concurrency semantics, async/error paths, reusable-component event boundary, preview side-effect policy, broken-reference recovery and runtime verification scenarios.

## Handoffs

Use data binding for values and write-back, navigation owners for route actions, permissions/high-stakes owners for consequential operations, component authoring for declared event APIs, and design-to-code interaction handoff when builder wires map into source implementations.