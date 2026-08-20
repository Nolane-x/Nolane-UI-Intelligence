---
name: designing-3d-scene-hierarchies
description: Own hierarchical organization of 3D entities, instances, parents, collections, visibility, selection, transforms, and outliner synchronization with the viewport.
---
# Designing 3D Scene Hierarchies

## Decision ownership

Own the scene/outliner structure that represents 3D objects, components, instances, groups, and parents. Decide hierarchy semantics, expansion, selection synchronization, visibility/lock state, parent transform implications, instance/source distinction, drag reparenting, and search. This owner does not replace layer/collection organization; hierarchy expresses structural parentage and model identity.

## Inputs and evidence

Require entity types, parent-child transform rules, instance/reference model, expected depth/count, visibility/selectability states, naming/IDs, assembly relationships, permissions, and viewport synchronization. Identify virtual/generated children that should not be edited like authored entities.

## Procedure

Use stable entity identity and type cues; duplicate names require path/context disambiguation. Selecting in outliner and viewport must converge on the same semantic entity while supporting multi-selection. Reparenting should preview transform consequences—preserve world transform, inherit new local transform, or another explicit rule. Visibility and lock/selectability need independent semantics. Instances must reveal source definition and whether edits affect one occurrence or all. Search should reveal ancestors and permit focus/isolation. Large trees may virtualize but cannot lose selected/focused identity.

## Failure topology

Failures include deleting an instance and removing the source unexpectedly, reparenting that moves geometry because transform semantics were hidden, viewport selection highlighting a different tree row, invisible-but-selectable ambiguity, duplicate names with no path, and generated children appearing editable. Another failure is collapsing hierarchy and hiding selected/errored descendants with no cue.

## Falsification

Reject if viewport/outliner disagree on identity; if reparent transform result cannot be predicted; if source versus instance edit scope is unclear; if hidden/locked/selectable states are conflated; if selected descendants can vanish under collapsed parents with no indicator; or if search cannot reveal hierarchy path for a result.

## Output contract

Return a `3d-scene-hierarchies-contract` with: entity/type identity; parent-child semantics; transform-on-reparent rule; instance/source behavior; visibility/lock/selectability; selection synchronization; collapse descendant cues; search/reveal; generated-entity treatment; and large-tree virtualization requirements. Include one instance edit and one preserve-world reparent case.

## Handoffs

Layer/collection management owns orthogonal organization, assembly hierarchy owns mechanical product structure, viewport navigation/focus consumes selection, and generic tree-view mechanics provide expansion/keyboard behavior.