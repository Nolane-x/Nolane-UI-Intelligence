---
name: designing-canvas-hierarchy-synchronization
description: Use when a visual builder exposes the same authored objects through a rendered canvas and structural tree and selection, ordering, nesting, hidden state, generated wrappers, and virtualized nodes must stay synchronized.
---

# Designing Canvas Hierarchy Synchronization

## Parent Contract

**Required parent:** `designing-visual-application-builders`.

This skill owns correspondence between spatial representation and authored structural representation. It does not decide general drag selection or DOM implementation. Its concern is whether an object visible, hidden, repeated or generated in one representation can be reliably located and manipulated in the other without changing identity.

## Correspondence model

Define three identities explicitly: **authored identity**, **runtime/render identity**, and **editor presentation identity**. They may coincide for simple elements, but wrappers, repeated collection items, portals, fragments, slots, conditional branches and virtualized regions often create runtime nodes that should not masquerade as authored objects. Decide which runtime surfaces are directly selectable and how selection resolves back to the nearest meaningful authored owner.

Selection synchronization must be bidirectional. Clicking the canvas should reveal the correct tree node and ancestor path; choosing a tree node should locate or explain its canvas representation. Hidden/off-breakpoint/conditional objects need truthful outcomes such as reveal in outline only, switch context, or show an absent-state marker—not an inexplicable no-op. Multi-selection must preserve structural distinctions when selected objects live under different parents.

Ordering is also contextual. Tree order may encode DOM/semantic order while canvas uses grid placement, absolute positioning or z-order. Do not imply that dragging a tree row always changes visual stacking, or that changing z-index changes accessibility/reading order. Expose which ordering dimension an operation mutates.

For repeated data, distinguish template node from runtime item occurrence. Selecting the third rendered card may enter occurrence context for preview/debugging, but editing structure usually targets the template. If per-item overrides exist, represent that scope explicitly rather than silently writing a special case.

## Evidence

Use the actual document schema, renderer mapping, selection protocol, conditional/repeat examples, portals/overlays, component slots, hidden states, keyboard navigation through tree/canvas and collaboration updates. Capture identity traces showing authored ID → render node(s) → editor selection before and after structural mutations.

## Failure topology

Failures include canvas clicks selecting invisible implementation wrappers; tree selection scrolling to the wrong repeated instance; deleting a runtime child that is actually generated from a template; reordering nodes in tree and accidentally changing semantic order when the user expected only stacking; or selection jumping to an ancestor after another collaborator inserts a sibling.

A dangerous failure is ghost selection: the inspector continues editing an old ID after the canvas has rerendered a replacement object, so visible highlight and mutation target diverge.

## Falsification

Exercise nested components, slots, repeated items, conditional absence, off-breakpoint elements, overlays/portals, absolute layers and collaborative insertion. Perform selection from both surfaces, reorder, reparent, hide/show and undo. The contract fails if the selected authored identity cannot be named before mutation, if one surface points at stale identity, or if a runtime implementation node can be mutated as though it were authored without an explicit conversion boundary.

## Recovery

Reconnect representations through stable authored IDs and a declared renderer mapping. Drop stale editor selections atomically when targets are deleted/replaced. Provide contextual navigation for hidden/conditional objects instead of fabricating render presence. Split semantic order, layout order and stacking controls where users otherwise conflate them.

## Output contract

Return a `canvas-hierarchy-synchronization-contract` containing identity layers, selectable-node rules, authored↔render mapping, bidirectional selection behavior, hidden/conditional/repeat handling, order dimensions, multi-selection scope, collaboration reconciliation, stale-selection recovery and verification cases.

## Handoffs

Use component-instance owners for definition/instance boundaries, slot insertion for legal reparenting targets, conditional-visibility owners for branch state, layout-constraint owners for spatial movement, and accessibility/navigation owners when structural order has semantic consequences.