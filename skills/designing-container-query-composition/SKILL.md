---
name: designing-container-query-composition
description: Use when a reusable region must adapt to the space allocated by its containing layout rather than to the global viewport and container-local composition rules need explicit task-preserving behavior.
---

# Designing Container-Query Composition

## Composition Intent
Viewport breakpoints cannot explain a card, sidebar module, embedded inspector, or nested panel whose usable width depends on its parent. This skill owns the decision of how a region changes composition from measured container conditions while preserving its semantic task and avoiding hidden coupling to page-level breakpoints.

## Parent Contract
**Required parent:** `adapting-responsive-layouts`.

The parent owns broad responsive strategy. This specialist governs local composition where the same viewport can legitimately host several different component arrangements because their containers differ.

## Container State
Model state as `(container inline-size/block-size, style context, content pressure, current composition, task state)`. Define named composition states from observed constraints rather than device labels. A state transition should have a reason such as loss of readable measure, command collision, or insufficient comparison width.

A container query may change columns, label placement, supporting detail, or action arrangement, but it must not silently change the meaning or availability of the task. Nested containers require clear ownership so parent and child do not oscillate each other across thresholds.

## Transition Invariants
- the local rule depends on the intended query container, not accidental ancestry;
- state transitions are monotonic around thresholds or protected from oscillation;
- task-critical actions remain reachable in every admitted state;
- DOM/reading order stays coherent when visual composition changes;
- content growth can trigger a valid alternative without requiring a viewport change.

## Evidence
Evidence includes container-resize traces at fixed viewport size, long/localized content, nested-container cases, representative task completion in each composition, and threshold-neighbor screenshots or measurements. Record the queried container identity and computed state so evidence is reproducible.

## Failure Topology
Characteristic Failure includes local widgets staying desktop-shaped inside narrow columns, nested query loops, thresholds chosen from phone/tablet labels, actions disappearing when a container shrinks, and source order that becomes nonsensical after grid rearrangement. Another failure is tying a local component to page CSS classes so reuse in a different shell breaks its logic.

## Falsification
Falsification holds the viewport constant while resizing only the container, moves the component into a differently sized parent, injects long content near thresholds, and nests it under another querying component. If the task state is unpredictable or context leakage changes behavior, the contract fails.

## Recovery
Recovery identifies the true constraint, moves the query boundary to the owning container, and replaces device assumptions with content/task conditions. If local state changes require global navigation or workflow changes, route back to the parent rather than overloading a container query.

## Output and Handoff
Output: `container-query-composition-contract` containing query-container identity, state thresholds, task-preservation rules, nested ownership, and verification cases. Handoff generic viewport strategy to the parent and content-derived threshold evidence to content-pressure breakpoint design.

## Sibling Boundary and delete-the-skill
Sibling content-pressure breakpoints determine when content actually fails; this skill determines the local container context that owns the transition. The delete-the-skill test passes because viewport-responsive ownership alone cannot determine correct behavior for multiple differently sized containers on one page.